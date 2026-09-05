#!/usr/bin/env python3
"""Cross-field rule prober.

Two checks, because a conformance corpus proves only what its fixtures happen to
exercise. R3 shipped in v1.1.0 and v1.2.0 unenforced for the omitted-property case:
its `then` constrained task_frame's type but never required the property, and its only
negative fixture set the value to null. A null trips a type check. It is not absence.

CHECK 1 (structural): for every conditional rule, any property the `then` constrains
must also appear in the `then`'s `required`. Otherwise the rule is a no-op whenever
that property is simply missing.

CHECK 2 (executable): each rule gets an explicit omission probe built by deleting the
property from a conformant base record.

Usage: python3 rule_probe.py    Exit 0 clean, 1 on any unenforced rule.
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent / "conformance"))
import slpt_validate as V
from jsonschema import Draft202012Validator

schema = json.loads(pathlib.Path("schema/lpr_v1.2.0.json").read_text())
val = Draft202012Validator(schema)
fail = []

print("CHECK 1 — every property a `then` constrains must also be required by it\n")
for rule in schema.get("allOf", []):
    rid = rule["$comment"].split(" - ")[0].split(" —")[0].strip()
    then = rule.get("then", {})
    constrained = set(then.get("properties", {}))
    required = set(then.get("required", []))
    # A property is safely constrained if the `then` requires it, OR the schema
    # requires it globally, OR the rule's own `if` already required it to be present.
    guaranteed = (required
                  | set(schema.get("required", []))
                  | set(rule.get("if", {}).get("required", [])))
    gap = constrained - guaranteed
    status = "OK  " if not gap else "GAP "
    if gap:
        fail.append(f"{rid}: constrains {sorted(gap)} without requiring it, and nothing else "
                    f"guarantees its presence — the rule is a no-op when the property is absent")
    via = []
    for k in sorted(constrained):
        if k in required: via.append(f"{k}(then)")
        elif k in set(schema.get("required", [])): via.append(f"{k}(root-required)")
        elif k in set(rule.get("if", {}).get("required", [])): via.append(f"{k}(if-required)")
        else: via.append(f"{k}(UNGUARANTEED)")
    print(f"  {status}{rid:4s} {', '.join(via) or '-'}")

print("\nCHECK 2 — executable omission probes\n")
def base(): return json.loads(json.dumps(V.BASE))
def without(rec, key):
    r = json.loads(json.dumps(rec)); r.pop(key, None); return r

probes = []
r = base(); r["delegation_annotation"]["state"] = "consistent_with_task_frame"
probes.append(("R3", "task_frame omitted while state is frame-relative", without(r, "task_frame"), False))
r = base(); r["intended_use"] = "credentialing"; r["use_authorization_status"] = "authorized"
probes.append(("R1", "validation_status omitted while authorized", without(r, "validation_status"), False))
r = base(); r["use_authorization_status"] = "conditionally_authorized"
probes.append(("R2", "validation_status omitted while conditionally authorized", without(r, "validation_status"), False))
r = base(); r["dispute_status"] = {"state": "open"}
probes.append(("R4", "learner_access omitted while disputed", without(r, "learner_access"), False))
r = base(); r["credential_tier"] = "AIQ_CERTIFIED"
probes.append(("R5", "tier with everything else omitted", without(without(r, "validation_status"), "intended_use"), False))
r = base(); r["dispute_status"] = {"state": "upheld"}
probes.append(("R6", "dispute upheld with no record_action", r, False))
probes.append(("--", "unmodified base record still validates", base(), True))

for rid, name, rec, expect in probes:
    errs = list(val.iter_errors(rec))
    ok = (not errs) == expect
    if not ok:
        fail.append(f"{rid}: {name} — schema {'accepted' if not errs else 'rejected'} it")
    print(f"  {'PASS' if ok else 'FAIL'} {rid:4s} {name:52s} "
          f"{'valid' if not errs else errs[0].message[:44]}")

print()
if fail:
    print(f"UNENFORCED OR MISBEHAVING RULES — {len(fail)}\n")
    for f in fail: print("  -", f)
    sys.exit(1)
print("PASS — every conditional rule requires what it constrains, and every omission probe behaves")
sys.exit(0)
