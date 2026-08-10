#!/usr/bin/env python3
"""SLPT conformance harness: validator + positive/negative corpus.

Validates Learning Provenance Records against the published SLPT JSON Schema
(Draft 2020-12) and runs a labelled conformance corpus in which every negative
case targets exactly one schema constraint.

Usage:
    python slpt_validate.py <record.json> [--schema PATH]
    python slpt_validate.py --run-corpus [--schema PATH]
"""
import json, sys, argparse, copy, hashlib, pathlib

try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit("pip install jsonschema")

H = hashlib.sha256(b"illustrative").hexdigest()
D = "sha256:" + H

BASE = {
    "record_id": "9c2e1a6f-3b8d-4f47-a1e7-2c8b9d0e5f30",
    "record_version": "1.1.0",
    "platform_id": "answerr_v3.2",
    "session_id": "sess_b51e2c",
    "timestamp_utc": "2026-05-19T14:32:18Z",
    "context_type": "RESEARCH",
    "context_id": "research_workspace_42",
    "institution_id": "babson_college",
    "verified_context": True,
    "query_text_hash": "495b651357ec3680b88c57810ceee9bf05a1ddd0553b1e62e7e7a1f5977d22ea",
    "dimension_estimates": {
        "jq": None,
        "qo": None,
        "sod": None,
        "sa": None,
        "ad": None,
        "signal_confidence": None,
        "computation_method": "answerlabs_scorer_v1.1.0"
    },
    "score_status": "synthetic_example_not_validated",
    "intended_use": "formative_feedback",
    "use_authorization_status": "prohibited",
    "validation_status": None,
    "scoring_model": {
        "id": "answerlabs_scorer",
        "version": "1.1.0",
        "digest": "sha256:495b651357ec3680b88c57810ceee9bf05a1ddd0553b1e62e7e7a1f5977d22ea",
        "calibration_epoch": "2026-H1",
        "model_description_uri": None,
        "weight_config_id": "babson_default",
        "weight_config_version": "1.0.0",
        "weight_config_digest": "sha256:495b651357ec3680b88c57810ceee9bf05a1ddd0553b1e62e7e7a1f5977d22ea"
    },
    "task_frame": None,
    "delegation_annotation": {
        "episode_scoped": True,
        "state": "not_assessable",
        "evidence_basis": None,
        "confidence": None
    },
    "dispute_status": {"state": "none"},
    "learner_access": True,
    "context_filter_passed": True,
    "credential_tier": None
}


def drop(d, *path):
    d = copy.deepcopy(d)
    t = d
    for k in path[:-1]:
        t = t[k]
    t.pop(path[-1], None)
    return d


def setv(d, value, *path):
    d = copy.deepcopy(d)
    t = d
    for k in path[:-1]:
        t = t[k]
    t[path[-1]] = value
    return d


def corpus():
    """Return [(id, expect_valid, constraint_under_test, instance)]."""
    C = []
    # ---- positive cases ----
    C.append(("P01", True, "minimal conformant record with all required fields", BASE))
    C.append(("P02", True, "optional institution_id omitted", drop(BASE, "institution_id")))
    C.append(("P03", True, "boundary scores at 0.0 and 1.0 accepted",
              setv(setv(BASE, 0.0, "dimension_estimates", "jq"), 1.0, "dimension_estimates", "ad")))
    C.append(("P04", True, "AIQ_LEARNER tier accepted", setv(BASE, "AIQ_LEARNER", "credential_tier")))
    C.append(("P04b", True, "null credential_tier accepted (v1.1)", setv(BASE, None, "credential_tier")))
    C.append(("P04c", True, "null dimension_estimates accepted (v1.1)", setv(BASE, None, "dimension_estimates")))
    for ct in ["TUTOR", "ASSISTANT", "QUIZ", "ASSIGNMENT", "REFLECTION"]:
        C.append((None, True, f"context_type {ct} accepted", setv(BASE, ct, "context_type")))
    C.append((None, True, "uppercase hex hash accepted", setv(BASE, H.upper(), "query_text_hash")))
    # v1.1 cross-field and new-field positives
    C.append((None, True, "credentialing use with unvalidated status permitted",
              setv(setv(BASE, "credentialing", "intended_use"), "unvalidated", "use_authorization_status")))
    C.append((None, True, "adjudicated dispute with trace unavailable",
              setv(BASE, {"state": "rejected", "raised_at_utc": "2026-06-01T09:00:00Z",
                          "adjudicator": "answer_labs", "trace_available_for_review": False},
                   "dispute_status")))
    C.append((None, True, "audit bundle fully populated",
              setv(setv(setv(BASE, "1.1.0", "scoring_model", "conformance_suite_version"),
                        "2026-05-19T14:32:20Z", "scoring_model", "inference_timestamp_utc"),
                   "https://example.org/eval", "scoring_model", "evaluation_report_uri")))
    C.append((None, True, "delegation state relative to a declared task frame",
              setv(setv(BASE, {"pedagogical_purpose": "drafting", "permitted_ai_actions": ["outline"]}, "task_frame"),
                   "consistent_with_task_frame", "delegation_annotation", "state")))

    # ---- negative cases: one constraint each ----
    N = [
        ("required: record_id", drop(BASE, "record_id")),
        ("required: record_version", drop(BASE, "record_version")),
        ("required: platform_id", drop(BASE, "platform_id")),
        ("required: session_id", drop(BASE, "session_id")),
        ("required: timestamp_utc", drop(BASE, "timestamp_utc")),
        ("required: context_type", drop(BASE, "context_type")),
        ("required: context_id", drop(BASE, "context_id")),
        ("required: verified_context", drop(BASE, "verified_context")),
        ("required: query_text_hash", drop(BASE, "query_text_hash")),
        ("required: dimension_estimates", drop(BASE, "dimension_estimates")),
        ("required: credential_tier key present", drop(BASE, "credential_tier")),
        ("required: intended_use", drop(BASE, "intended_use")),
        ("required: use_authorization_status", drop(BASE, "use_authorization_status")),
        ("required: scoring_model", drop(BASE, "scoring_model")),
        ("required: delegation_annotation", drop(BASE, "delegation_annotation")),
        ("scoring_model.required: weight_config_id", drop(BASE, "scoring_model", "weight_config_id")),
        ("scoring_model.required: weight_config_digest", drop(BASE, "scoring_model", "weight_config_digest")),
        ("scoring_model.required: calibration_epoch", drop(BASE, "scoring_model", "calibration_epoch")),
        ("use_authorization_status not in enum", setv(BASE, "fine", "use_authorization_status")),
        ("delegation state not in enum", setv(BASE, "definitely_delegated", "delegation_annotation", "state")),
        ("weight_config_digest fails sha256 pattern", setv(BASE, "abc", "scoring_model", "weight_config_digest")),
        ("required: context_filter_passed", drop(BASE, "context_filter_passed")),
        ("dimension_estimates.required: jq", drop(BASE, "dimension_estimates", "jq")),
        ("dimension_estimates.required: signal_confidence",
         drop(BASE, "dimension_estimates", "signal_confidence")),
        ("dimension_estimates.required: computation_method",
         drop(BASE, "dimension_estimates", "computation_method")),
        ("score above maximum 1.0", setv(BASE, 1.4, "dimension_estimates", "jq")),
        ("score below minimum 0.0", setv(BASE, -0.1, "dimension_estimates", "qo")),
        ("score wrong type (string)", setv(BASE, "0.78", "dimension_estimates", "jq")),
        ("credential_tier not in enum", setv(BASE, "AIQ_PLATINUM", "credential_tier")),
        ("context_type not in enum", setv(BASE, "SOCIAL", "context_type")),
        ("record_version fails semver pattern", setv(BASE, "v1.0", "record_version")),
        ("query_text_hash wrong length", setv(BASE, "abc123", "query_text_hash")),
        ("query_text_hash non-hex characters", setv(BASE, "z" * 64, "query_text_hash")),
        ("verified_context wrong type", setv(BASE, "true", "verified_context")),
        ("additionalProperties false at root", setv(BASE, "x", "unexpected_field")),
        ("additionalProperties false in dimension_estimates",
         setv(BASE, 0.5, "dimension_estimates", "xx")),
        ("plaintext query leaked into record",
         setv(BASE, "How do I reconcile these accounts?", "query_text")),
        ("R1: credentialing use asserted as authorized",
         setv(setv(BASE, "credentialing", "intended_use"), "authorized", "use_authorization_status")),
        ("R1: summative assessment asserted as authorized",
         setv(setv(BASE, "summative_assessment", "intended_use"), "authorized", "use_authorization_status")),
        ("R2: authorized status without validation_status evidence",
         setv(BASE, "authorized", "use_authorization_status")),
        ("R3: delegation state relative to an absent task_frame",
         setv(BASE, "inconsistent_with_task_frame", "delegation_annotation", "state")),
        ("R4: open dispute on a record the learner cannot read",
         setv(setv(BASE, False, "learner_access"), {"state": "open"}, "dispute_status")),
        ("dispute_status.adjudicator not in enum",
         setv(BASE, {"state": "open", "adjudicator": "registrar"}, "dispute_status")),
        ("dispute_status wrong type (v1.0 string form)",
         setv(BASE, "none", "dispute_status")),
        ("conformance_suite_version fails semver pattern",
         setv(BASE, "v1", "scoring_model", "conformance_suite_version")),
    ]
    for i, (label, inst) in enumerate(N, 1):
        C.append((f"N{i:02d}", False, label, inst))
    out, pi = [], 0
    for cid, expect, label, inst in C:
        if expect and cid is None:
            pi += 1
            cid = f"P{pi:02d}"
        elif expect:
            pi += 1
            cid = f"P{pi:02d}"
        out.append((cid, expect, label, inst))
    return out


def run(schema, verbose=True):
    v = Draft202012Validator(schema)
    rows, npass = [], 0
    for cid, expect, label, inst in corpus():
        errs = sorted(v.iter_errors(inst), key=lambda e: e.path)
        valid = not errs
        ok = (valid == expect)
        npass += ok
        msg = "" if valid else errs[0].message
        rows.append((cid, expect, valid, ok, label, msg))
        if verbose:
            print(f"{cid}  {'PASS' if ok else 'FAIL'}  expect={'valid' if expect else 'invalid':7s} "
                  f"got={'valid' if valid else 'invalid':7s}  {label}")
            if not valid and verbose == 2:
                print(f"       -> {msg[:110]}")
    return rows, npass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("record", nargs="?")
    ap.add_argument("--schema", default="schema/lpr_v1.1.0.json")
    ap.add_argument("--run-corpus", action="store_true")
    a = ap.parse_args()
    schema = json.load(open(a.schema))

    if a.run_corpus:
        rows, npass = run(schema)
        pos = sum(1 for r in rows if r[1])
        neg = len(rows) - pos
        print(f"\n{'='*66}\nSLPT conformance corpus\n"
              f"  schema      : {schema.get('title')} ({a.schema})\n"
              f"  positive    : {pos}\n  negative    : {neg}\n"
              f"  total       : {len(rows)}\n  passed      : {npass}\n"
              f"  failed      : {len(rows)-npass}\n{'='*66}")
        json.dump([{"id": r[0], "expect_valid": r[1], "observed_valid": r[2],
                    "pass": r[3], "constraint": r[4], "first_error": r[5]} for r in rows],
                  open("conformance_results.json", "w"), indent=2)
        return 0 if npass == len(rows) else 1

    if not a.record:
        ap.error("give a record path or --run-corpus")
    inst = json.load(open(a.record))
    errs = sorted(Draft202012Validator(schema).iter_errors(inst), key=lambda e: e.path)
    if not errs:
        print(f"VALID  {a.record}  conforms to {schema.get('title')}")
        return 0
    print(f"INVALID  {a.record}  {len(errs)} error(s)")
    for e in errs:
        loc = "/".join(str(p) for p in e.absolute_path) or "<root>"
        print(f"  at {loc}: {e.message}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
