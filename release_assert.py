#!/usr/bin/env python3
"""Release gate: fail if a retired claim reappears anywhere in the release tree.

Every rule here exists because the string it forbids was already published once and
had to be withdrawn. CHANGELOG.md and files named *history* are exempt, because a
changelog must be able to say what was removed.

Usage:  python3 release_assert.py [tree_root]
Exit 0 clean, 1 on any violation. Wire into CI on pull request and tag.
"""
import sys, pathlib, re

EXEMPT_NAMES = {"CHANGELOG.md", "release_assert.py"}
EXEMPT_SUBSTR = ("history", "SUPERSEDED")
# Superseded schema versions are retained in the tree for lineage and legitimately
# describe the fields as they were named at that version.
CURRENT_SCHEMA = "lpr_v1.2.0.json"
EXEMPT_PATTERNS = (r"lpr_v\d+\.\d+\.\d+\.json",)

# A withdrawal statement must be able to name what it withdraws. A hit is not a
# violation if the surrounding text marks it as retired rather than asserted.
WITHDRAWAL_MARKERS = (
    "withdraw", "superseded", "supersedes", "formerly named", "renamed",
    "change at v1.2", "is removed", "removed rather than", "no successor",
    "replaced by", "prohibited", "not a self-report", "objective multiple-choice",
    "no claim is made", "unable to reproduce", "does not by itself",
)
TEXT_SUFFIX = {".md", ".json", ".py", ".yml", ".yaml", ".cff", ".txt"}

# (rule id, description, predicate over lowercased text -> list of offending excerpts)
def near(text, a, b, window=120):
    """a and b occurring within `window` characters of each other."""
    out = []
    for m in re.finditer(re.escape(a), text):
        seg = text[max(0, m.start() - window): m.start() + len(a) + window]
        if b in seg:
            out.append(seg.replace("\n", " ").strip())
    return out

def strip_code(text):
    """Remove fenced blocks and indented command lines. Prose rules should not fire
    on `--schema schema/...`, which is an argument followed by a directory."""
    out, fenced = [], False
    for line in text.split("\n"):
        if line.strip().startswith("```"):
            fenced = not fenced
            continue
        if fenced or line.startswith("    "):
            continue
        out.append(line)
    return "\n".join(out)

def plain(text, needle, window=220):
    """Return a wide excerpt: wide enough that a withdrawal marker in the same
    sentence or the same banner paragraph is visible to the exemption check."""
    return [text[max(0, m.start()-window):m.start()+len(needle)+window].replace("\n", " ").strip()
            for m in re.finditer(re.escape(needle), text)]

RULES = [
    ("R-AICOS", "AICOS described as self-report — withdrawn in R1, caught by Reviewer #1",
     lambda t: [x for x in near(t, "aicos", "self-report") if "not a self-report" not in x
                and "objective multiple-choice" not in x]),
    ("R-PENALTY", "the recommended 20% Bloom-inversion penalty — withdrawn at v1.2",
     lambda t: [x for x in near(t, "20%", "inversion", 200) + near(t, "20%", "bloom", 200)]),
    ("R-TASTE", "the Discernment and Taste dimension name — withdrawn at v1.2",
     lambda t: plain(t, "discernment and taste")),
    ("R-VELOCITY", "the Learning Velocity dimension name — withdrawn at v1.2",
     lambda t: plain(t, "learning velocity")),
    ("R-EMPLOYER", "the employer mapping — withdrawn at v1.2",
     lambda t: plain(t, "employer mapping")),
    ("R-INTEROP", "conformance described as demonstrated interoperability",
     lambda t: plain(t, "machine-checkable interoperability")),
    ("R-PERMANENT", "dimensional permanence — replaced by revisability at v1.2",
     lambda t: plain(t, "permanent dimension") + plain(t, "permanent aiq dimension")),
    ("R-IRREPLACEABLE", "unsupported claim that AI cannot replicate the chosen capabilities",
     lambda t: [x for x in plain(t, "cannot replicate") + plain(t, "irreplaceable")
                if "no claim is made" not in x and "unable to reproduce" not in x]),
    ("R-VALIDSIGNAL", "a value called valid while measurement validity is unestablished",
     lambda t: plain(t, "valid aiq signal")),
    ("R-CALIBRATED", "components described as calibrated against deployment data",
     lambda t: near(t, "calibrated", "deployment", 120)),
    # --- added after QC v3.0: every one of these shipped in a file the gate passed ---
    ("R-SELFREPORT-ALL", "the false universal that every validated instrument is self-report",
     lambda t: [x for x in near(t, "validated ai literacy instrument", "self-report", 200)
                + near(t, "validated ai-literacy instrument", "self-report", 200)
                if "either" not in x and "objective" not in x]),
    ("R-FUTURE-SCHEMA", "the schema or OpenAPI described as a future release when both ship now",
     lambda t: [x for x in near(t, "json schema", "subsequent release", 300)
                + near(t, "json schema", "will be published", 300)
                + near(t, "openapi", "subsequent release", 300)
                + near(t, "openapi", "will be published", 300)
                if "adapters remain" not in x and "adapters — xapi" not in x]),
    ("R-COMPLIANCE-SATISFIED", "a legal requirement described as satisfied by the artifact",
     lambda t: near(t, "article 12", "satisfied", 200) + near(t, "article 13", "satisfied", 200)
             + near(t, "ferpa compliance", "preserved", 120)),
    ("R-CERTIFIED-TABLE", "a blanket certified-or-compliant claim",
     lambda t: plain(t, "certified or compliant")),
    ("R-CROSSINST", "a claim that estimates or tiers mean the same across institutions",
     lambda t: plain(t, "mean the same thing regardless of which institution")
             + plain(t, "regardless of which institution")),
    ("R-COMPARABILITY", "a claim that changing scoring logic preserves prior meaning",
     lambda t: plain(t, "without invalidating previously issued credentials")),
    ("R-PROFICIENCY", "a proficiency band or exact score presented as a validated reading",
     lambda t: [x for x in plain(t, "proficiency band") + plain(t, "exact score")
                + plain(t, "proficiency_band", 600)
                if "not validated" not in x and "no proficiency band" not in x
                and "not an slpt-conformant" not in x and "carry no validated" not in x
                and "gated, not awarded" not in x and "not validated" not in x]),
    ("R-SCHEMA-IDENTITY", "the current schema describing itself as an earlier version",
     lambda t: near(t, "learning provenance record v1.1", "description", 300)
             + near(t, "conforms to slpt-aiq-v1.1", "record", 300)),
    # --- added after QC v4.0: semantic drift the 19-rule gate did not catch ---
    ("R-VALIDATOR-ENFORCES", "the validator claimed to enforce evidential adequacy",
     lambda t: [x for x in near(t, "no record", "conformantly carry", 200)
                + near(t, "validator enforces", "tier", 300)
                if "does not establish evidential adequacy" not in x]),
    ("R-SAMEVERSION", "same-version issuance claimed to preserve comparability",
     lambda t: near(t, "same version", "comparable", 200)
             + near(t, "remain comparable", "version", 200)),
    ("R-WHAT-TO-MEASURE", "SLPT described as specifying what to measure",
     lambda t: plain(t, "what to measure")),
    ("R-FERPA-COMPLIANT", "a bare assertion of FERPA compliance",
     lambda t: [x for x in plain(t, "ferpa compliant") + near(t, "ferpa", "compliant", 60)
                if "does not by itself establish" not in x and "may support" not in x
                and "not asserted" not in x]),
    ("R-AUTO-PASSBACK", "automated gradebook passback of estimates",
     lambda t: [x for x in near(t, "pass back automatically", "gradebook", 200)
                + near(t, "grade passback", "ags", 200)
                if "prohibits" not in x and "rejects passback" not in x
                and "not permitted" not in x]),
    ("R-EMPLOYMENT-INTEGRATION", "integration into HR or talent systems, prohibited by §11",
     lambda t: [x for x in plain(t, "hr platforms") + plain(t, "talent management")
                if "not authorized" not in x and "outside permitted use" not in x]),
    ("R-DEAD-SECTION-REF", "a cross-reference to a section that does not exist",
     lambda t: plain(t, "§10.2") + plain(t, "section 10.2")),
    ("R-SLPT-COMPLIANT", "a platform called SLPT-compliant before §12.4 confirmation",
     lambda t: [x for x in plain(t, "slpt-compliant")
                if "determined by validating" not in x and "note on the word" not in x
                and "outstanding" not in x]),
    ("R-DUPHEADING", "the same H2 heading twice in one file",
     lambda t: [f"duplicate heading: {h}" for h in
                {x for x in re.findall(r"^## (.+)$", t, re.M)
                 if re.findall(r"^## (.+)$", t, re.M).count(x) > 1}]),
    # A duplicated word split across a line break is invisible to any single-line
    # check. One shipped in the v1.2 draft as "an open / open specification" and a
    # line-oriented grep reported the file clean.
    ("R-DUPWORD", "a word duplicated across whitespace, including across a line break",
     lambda t: [m.group(0).replace("\n", " / ")
                for m in re.finditer(r"\b([a-z]{3,})(\s+)\1\b", strip_code(t))
                # A blank line or a heading between the two is a paragraph boundary,
                # not a duplicated word: a section title may legitimately end with the
                # same token the next paragraph opens with.
                if "\n\n" not in m.group(2) and m.group(1) not in {"had", "that", "very"}]),
]

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
violations = []
scanned = 0
for f in sorted(root.rglob("*")):
    if not f.is_file() or f.suffix.lower() not in TEXT_SUFFIX:
        continue
    if f.name in EXEMPT_NAMES or any(x.lower() in str(f).lower() for x in EXEMPT_SUBSTR):
        continue
    if any(re.fullmatch(pat, f.name) for pat in EXEMPT_PATTERNS) and f.name != CURRENT_SCHEMA:
        continue
    try:
        text = f.read_text(encoding="utf-8").lower()
    except UnicodeDecodeError:
        continue
    scanned += 1
    for rid, desc, pred in RULES:
        for hit in pred(text):
            if any(m in hit for m in WITHDRAWAL_MARKERS):
                continue          # a withdrawal statement, not an assertion
            violations.append((rid, desc, f.relative_to(root), hit[:160]))

print(f"release_assert: {scanned} text files scanned, {len(RULES)} retired-claim rules")
if not violations:
    print("PASS — no retired claim found outside CHANGELOG and history files")
    sys.exit(0)
print(f"FAIL — {len(violations)} violation(s)\n")
for rid, desc, path, hit in violations:
    print(f"  [{rid}] {path}\n      {desc}\n      ...{hit}...\n")
sys.exit(1)
