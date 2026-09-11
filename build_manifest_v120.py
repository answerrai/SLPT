"""Generate the v1.2.0 conformance manifests, Markdown and JSON, with toolchain metadata."""
import json, sys, pathlib, hashlib, datetime, platform, subprocess
REL = pathlib.Path("/home/claude/v120")
sys.path.insert(0, str(REL / "conformance"))
import slpt_validate as V
from jsonschema import Draft202012Validator
import jsonschema, importlib.metadata as md

SCHEMA = REL / "schema" / "lpr_v1.2.0.json"
schema = json.loads(SCHEMA.read_text())
val = Draft202012Validator(schema)
VALIDATOR = REL / "conformance" / "slpt_validate.py"

def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

RULES = {"R1": "R1 cross-field: authorization requires populated evidence",
         "R2": "R2 cross-field: authorization requires validation_status",
         "R3": "R3 cross-field: delegation state requires a task frame",
         "R4": "R4 cross-field: dispute requires learner access",
         "R5": "R5 cross-field: the credential gate",
         "R6": "R6 cross-field: dispute upheld requires action on the record"}
def klass(label, expect):
    if expect: return "Conformant fixtures: base record, optional fields, boundary values, enum members, nullable fields, and the R1/R5/R6 satisfied paths"
    for k, v in RULES.items():
        if label.startswith(k + ":"): return v
    if "required" in label: return "Required fields, root and nested objects"
    if "enum" in label: return "Enumerations"
    if any(x in label for x in ("pattern", "length", "non-hex")): return "Semantic-version, hash and digest patterns"
    if any(x in label for x in ("maximum", "minimum", "wrong type")): return "Value range and type"
    if "additionalProperties" in label: return "additionalProperties, both levels"
    if "plaintext" in label: return "Privacy: plaintext leakage"
    raise AssertionError(label)

rows, order, counts = [], [], {}
for cid, expect, label, inst in V.corpus():
    errs = sorted(val.iter_errors(inst), key=lambda e: e.path)
    observed = not errs
    first = "" if observed else f"at {'/'.join(str(p) for p in errs[0].absolute_path) or '<root>'}: {errs[0].message}"
    k = klass(label, expect)
    if k not in counts: counts[k] = [0, 0]; order.append(k)
    counts[k][0] += 1; counts[k][1] += int(observed == expect)
    rows.append(dict(id=cid, expected_valid=expect, observed_valid=observed,
                     outcome_reproduced=(observed == expect), constraint=label,
                     fixture_sha256=hashlib.sha256(json.dumps(inst, sort_keys=True).encode()).hexdigest(),
                     first_error=first))

total = len(rows); ok = sum(r["outcome_reproduced"] for r in rows)
pos = sum(1 for r in rows if r["expected_valid"]); neg = total - pos
assert ok == total, "corpus did not reproduce every expected outcome"

# ---------------------------------------------------------------- build identity
# The build id is a hash over EVERY content file in the release tree, not a chosen
# subset. A subset was the earlier mistake: CITATION.cff and CHANGELOG.md could
# change without changing the id, so two different releases could share a name.
# Generated artefacts are excluded because they are derived from the tree and would
# make the hash self-referential.
GENERATED = ("CONFORMANCE_MANIFEST_", "RELEASE_FILES.sha256", "conformance_results.json")
def tree_files(root):
    out = []
    for f in sorted(root.rglob("*")):
        if not f.is_file():
            continue
        rel = f.relative_to(root).as_posix()
        if "__pycache__" in rel or any(g in rel for g in GENERATED):
            continue
        out.append((rel, sha(f)))
    return out

# The generator lives inside the tree it hashes. Install it first, so the hash covers
# the exact copy that shipped. Doing this after the hash was computed produced a
# build id that did not reproduce from the tarball — caught by the recompute check.
_self = pathlib.Path(__file__).resolve()
_installed = REL / "build_manifest_v120.py"
if _self != _installed:
    _installed.write_bytes(_self.read_bytes())

FILES = tree_files(REL)
BUILD = hashlib.sha256(
    "\n".join(f"{h}  {r}" for r, h in FILES).encode()
).hexdigest()[:8]
(REL / "RELEASE_FILES.sha256").write_text(
    "\n".join(f"{h}  {r}" for r, h in FILES) + "\n")

env = dict(build_id=BUILD, build_id_covers=f"{len(FILES)} content files, see RELEASE_FILES.sha256", generated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           python=platform.python_version(), jsonschema=md.version("jsonschema"),
           schema_file="schema/lpr_v1.2.0.json", schema_sha256=sha(SCHEMA),
           validator_file="conformance/slpt_validate.py", validator_sha256=sha(VALIDATOR),
           spec_file="spec/SLPT-AIQ-v1.2.md", spec_sha256=sha(REL / "spec" / "SLPT-AIQ-v1.2.md"),
           release_tag="v1.2.0", release_doi="PENDING — minted on deposit",
           exit_code=0)

(REL / f"CONFORMANCE_MANIFEST_v1_2_0_{BUILD}.json").write_text(json.dumps(
    {"summary": dict(total=total, positive=pos, negative=neg, outcomes_reproduced=ok, outcomes_not_reproduced=total-ok),
     "environment": env, "class_totals": {k: dict(cases=v[0], outcomes_reproduced=v[1]) for k, v in counts.items()},
     "cases": rows}, indent=2) + "\n")

L = [f"# SLPT conformance manifest — v1.2.0 build {BUILD}", "",
     f"**Build {BUILD}** = first 8 hex of sha256 over the hashes of all {len(FILES)} content",
     "files in the release tree, listed in `RELEASE_FILES.sha256`. Any change to any file —",
     "specification, schema, validator, changelog, citation metadata, README, OpenAPI, docs —",
     "produces a new build id and a new filename. Two manifests with different build ids",
     "describe different releases and must never be compared by date.", "",
     f"Generated {env['generated_utc']} from `{env['validator_file']}` against `{env['schema_file']}`,",
     f"Python {env['python']}, jsonschema {env['jsonschema']}. Exit code {env['exit_code']}.", "",
     f"    schema    sha256 {env['schema_sha256']}",
     f"    validator sha256 {env['validator_sha256']}",
     f"    spec      sha256 {env['spec_sha256']}", "",
     f"**{total} fixtures · {pos} positive · {neg} negative · {ok} expected outcomes reproduced · {total-ok} not reproduced**", "",
     "A negative fixture reproduces its expected outcome by being *rejected*. Each negative",
     "fixture was constructed from a conformant base record by introducing one targeted",
     "violation, so the expected failure condition is identifiable for each case.", "",
     "## Class totals", "", "| Class | Constraint under test | Cases | Expected outcome reproduced |", "|---|---|---|---|"]
for k in order:
    L.append(f"| {'Positive' if k.startswith('Conformant') else 'Negative'} | {k} | {counts[k][0]} | {counts[k][1]} |")
L += [f"| **Total** | | **{total}** | **{ok}** |", "", "## Fixture manifest", "",
      "| Fixture | Expected | Observed | Reproduced | Constraint under test | First validator error |", "|---|---|---|---|---|---|"]
for r in rows:
    L.append("| " + " | ".join([r["id"], "valid" if r["expected_valid"] else "invalid",
        "valid" if r["observed_valid"] else "invalid", "yes" if r["outcome_reproduced"] else "NO",
        r["constraint"].replace("|", "\\|"), r["first_error"].replace("|", "\\|")]) + " |")
(REL / f"CONFORMANCE_MANIFEST_v1_2_0_{BUILD}.md").write_text("\n".join(L) + "\n")
print(f"build {BUILD} · {total} fixtures · {pos} positive · {neg} negative · {ok} reproduced")
for k in order: print(f"  {counts[k][0]:>3} {counts[k][1]:>3}  {k}")
