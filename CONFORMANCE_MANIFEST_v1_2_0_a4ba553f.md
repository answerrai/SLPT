# SLPT conformance manifest — v1.2.0 build a4ba553f

**Build a4ba553f** = first 8 hex of sha256 over the hashes of all 21 content
files in the release tree, listed in `RELEASE_FILES.sha256`. Any change to any file —
specification, schema, validator, changelog, citation metadata, README, OpenAPI, docs —
produces a new build id and a new filename. Two manifests with different build ids
describe different releases and must never be compared by date.

Generated 2026-08-31T20:17:30+00:00 from `conformance/slpt_validate.py` against `schema/lpr_v1.2.0.json`,
Python 3.12.3, jsonschema 4.26.0. Exit code 0.

    schema    sha256 82834d14ce6580d1d2d6640fe9309a1f4a87d24cfc0909bb992cbb5248a9137e
    validator sha256 e43ff78428adc44374b04b2d48ad5fc85b2a9ae80a3b0e376b778085c6fc4b0f
    spec      sha256 fe7977c507f27f42cfd930f2d61dcab9b40a576dce8c4421bc4f90709c0056a8

**71 fixtures · 17 positive · 54 negative · 71 expected outcomes reproduced · 0 not reproduced**

A negative fixture reproduces its expected outcome by being *rejected*. Each negative
fixture was constructed from a conformant base record by introducing one targeted
violation, so the expected failure condition is identifiable for each case.

## Class totals

| Class | Constraint under test | Cases | Expected outcome reproduced |
|---|---|---|---|
| Positive | Conformant fixtures: base record, optional fields, boundary values, enum members, nullable fields, and the R1/R5/R6 satisfied paths | 17 | 17 |
| Negative | Required fields, root and nested objects | 22 | 22 |
| Negative | Enumerations | 6 | 6 |
| Negative | Semantic-version, hash and digest patterns | 5 | 5 |
| Negative | Value range and type | 5 | 5 |
| Negative | additionalProperties, both levels | 2 | 2 |
| Negative | Privacy: plaintext leakage | 1 | 1 |
| Negative | R1 cross-field: authorization requires populated evidence | 3 | 3 |
| Negative | R2 cross-field: authorization requires validation_status | 1 | 1 |
| Negative | R3 cross-field: delegation state requires a task frame | 2 | 2 |
| Negative | R4 cross-field: dispute requires learner access | 1 | 1 |
| Negative | R5 cross-field: the credential gate | 5 | 5 |
| Negative | R6 cross-field: dispute upheld requires action on the record | 1 | 1 |
| **Total** | | **71** | **71** |

## Fixture manifest

| Fixture | Expected | Observed | Reproduced | Constraint under test | First validator error |
|---|---|---|---|---|---|
| P01 | valid | valid | yes | minimal conformant record with all required fields |  |
| P02 | valid | valid | yes | optional institution_id omitted |  |
| P03 | valid | valid | yes | boundary scores at 0.0 and 1.0 accepted |  |
| P04 | valid | valid | yes | R5 future path: tier + credentialing + conditionally_authorized + populated evidence |  |
| P05 | valid | valid | yes | null credential_tier accepted (v1.1) |  |
| P06 | valid | valid | yes | null dimension_estimates accepted (v1.1) |  |
| P07 | valid | valid | yes | context_type TUTOR accepted |  |
| P08 | valid | valid | yes | context_type ASSISTANT accepted |  |
| P09 | valid | valid | yes | context_type QUIZ accepted |  |
| P10 | valid | valid | yes | context_type ASSIGNMENT accepted |  |
| P11 | valid | valid | yes | context_type REFLECTION accepted |  |
| P12 | valid | valid | yes | uppercase hex hash accepted |  |
| P13 | valid | valid | yes | credentialing use with unvalidated status and null tier permitted |  |
| P14 | valid | valid | yes | dispute upheld for the learner with the record invalidated |  |
| P15 | valid | valid | yes | adjudicated dispute with trace unavailable |  |
| P16 | valid | valid | yes | audit bundle fully populated |  |
| P17 | valid | valid | yes | delegation state relative to a declared task frame |  |
| N01 | invalid | invalid | yes | required: record_id | at <root>: 'record_id' is a required property |
| N02 | invalid | invalid | yes | required: record_version | at <root>: 'record_version' is a required property |
| N03 | invalid | invalid | yes | required: platform_id | at <root>: 'platform_id' is a required property |
| N04 | invalid | invalid | yes | required: session_id | at <root>: 'session_id' is a required property |
| N05 | invalid | invalid | yes | required: timestamp_utc | at <root>: 'timestamp_utc' is a required property |
| N06 | invalid | invalid | yes | required: context_type | at <root>: 'context_type' is a required property |
| N07 | invalid | invalid | yes | required: context_id | at <root>: 'context_id' is a required property |
| N08 | invalid | invalid | yes | required: verified_context | at <root>: 'verified_context' is a required property |
| N09 | invalid | invalid | yes | required: query_text_hash | at <root>: 'query_text_hash' is a required property |
| N10 | invalid | invalid | yes | required: dimension_estimates | at <root>: 'dimension_estimates' is a required property |
| N11 | invalid | invalid | yes | required: credential_tier key present | at <root>: 'credential_tier' is a required property |
| N12 | invalid | invalid | yes | required: intended_use | at <root>: 'intended_use' is a required property |
| N13 | invalid | invalid | yes | required: use_authorization_status | at <root>: 'use_authorization_status' is a required property |
| N14 | invalid | invalid | yes | required: scoring_model | at <root>: 'scoring_model' is a required property |
| N15 | invalid | invalid | yes | required: delegation_annotation | at <root>: 'delegation_annotation' is a required property |
| N16 | invalid | invalid | yes | scoring_model.required: weight_config_id | at scoring_model: 'weight_config_id' is a required property |
| N17 | invalid | invalid | yes | scoring_model.required: weight_config_digest | at scoring_model: 'weight_config_digest' is a required property |
| N18 | invalid | invalid | yes | scoring_model.required: calibration_epoch | at scoring_model: 'calibration_epoch' is a required property |
| N19 | invalid | invalid | yes | use_authorization_status not in enum | at use_authorization_status: 'fine' is not one of ['prohibited', 'unvalidated', 'conditionally_authorized', 'authorized'] |
| N20 | invalid | invalid | yes | delegation state not in enum | at delegation_annotation/state: 'definitely_delegated' is not one of ['consistent_with_task_frame', 'inconsistent_with_task_frame', 'not_assessable'] |
| N21 | invalid | invalid | yes | weight_config_digest fails sha256 pattern | at scoring_model/weight_config_digest: 'abc' does not match '^sha256:[a-fA-F0-9]{64}$' |
| N22 | invalid | invalid | yes | required: context_filter_passed | at <root>: 'context_filter_passed' is a required property |
| N23 | invalid | invalid | yes | dimension_estimates.required: jq | at dimension_estimates: {'qo': None, 'sod': None, 'sa': None, 'ad': None, 'signal_confidence': None, 'computation_method': 'answerlabs_scorer_v1.1.0'} is not valid under any of the given schemas |
| N24 | invalid | invalid | yes | dimension_estimates.required: signal_confidence | at dimension_estimates: {'jq': None, 'qo': None, 'sod': None, 'sa': None, 'ad': None, 'computation_method': 'answerlabs_scorer_v1.1.0'} is not valid under any of the given schemas |
| N25 | invalid | invalid | yes | dimension_estimates.required: computation_method | at dimension_estimates: {'jq': None, 'qo': None, 'sod': None, 'sa': None, 'ad': None, 'signal_confidence': None} is not valid under any of the given schemas |
| N26 | invalid | invalid | yes | score above maximum 1.0 | at dimension_estimates: {'jq': 1.4, 'qo': None, 'sod': None, 'sa': None, 'ad': None, 'signal_confidence': None, 'computation_method': 'answerlabs_scorer_v1.1.0'} is not valid under any of the given schemas |
| N27 | invalid | invalid | yes | score below minimum 0.0 | at dimension_estimates: {'jq': None, 'qo': -0.1, 'sod': None, 'sa': None, 'ad': None, 'signal_confidence': None, 'computation_method': 'answerlabs_scorer_v1.1.0'} is not valid under any of the given schemas |
| N28 | invalid | invalid | yes | score wrong type (string) | at dimension_estimates: {'jq': '0.78', 'qo': None, 'sod': None, 'sa': None, 'ad': None, 'signal_confidence': None, 'computation_method': 'answerlabs_scorer_v1.1.0'} is not valid under any of the given schemas |
| N29 | invalid | invalid | yes | credential_tier not in enum | at credential_tier: 'AIQ_PLATINUM' is not one of ['AIQ_LEARNER', 'AIQ_CERTIFIED', None] |
| N30 | invalid | invalid | yes | context_type not in enum | at context_type: 'SOCIAL' is not one of ['TUTOR', 'ASSISTANT', 'QUIZ', 'RESEARCH', 'ASSIGNMENT', 'REFLECTION'] |
| N31 | invalid | invalid | yes | record_version fails semver pattern | at record_version: 'v1.0' does not match '^\\d+\\.\\d+\\.\\d+$' |
| N32 | invalid | invalid | yes | query_text_hash wrong length | at query_text_hash: 'abc123' does not match '^[a-fA-F0-9]{64}$' |
| N33 | invalid | invalid | yes | query_text_hash non-hex characters | at query_text_hash: 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz' does not match '^[a-fA-F0-9]{64}$' |
| N34 | invalid | invalid | yes | verified_context wrong type | at verified_context: 'true' is not of type 'boolean' |
| N35 | invalid | invalid | yes | additionalProperties false at root | at <root>: Additional properties are not allowed ('unexpected_field' was unexpected) |
| N36 | invalid | invalid | yes | additionalProperties false in dimension_estimates | at dimension_estimates: {'jq': None, 'qo': None, 'sod': None, 'sa': None, 'ad': None, 'signal_confidence': None, 'computation_method': 'answerlabs_scorer_v1.1.0', 'xx': 0.5} is not valid under any of the given schemas |
| N37 | invalid | invalid | yes | plaintext query leaked into record | at <root>: Additional properties are not allowed ('query_text' was unexpected) |
| N38 | invalid | invalid | yes | R1: credentialing use asserted as authorized without validation evidence | at validation_status: None is not of type 'object' |
| N39 | invalid | invalid | yes | R1: summative assessment asserted as authorized without validation evidence | at validation_status: None is not of type 'object' |
| N40 | invalid | invalid | yes | R2: authorized status without validation_status evidence | at validation_status: None is not of type 'object' |
| N41 | invalid | invalid | yes | R3: delegation state relative to an OMITTED task_frame | at <root>: 'task_frame' is a required property |
| N42 | invalid | invalid | yes | R3: delegation state relative to a null task_frame | at task_frame: None is not of type 'object' |
| N43 | invalid | invalid | yes | R4: open dispute on a record the learner cannot read | at learner_access: True was expected |
| N44 | invalid | invalid | yes | dispute_status.adjudicator not in enum | at dispute_status/adjudicator: 'registrar' is not one of ['answer_labs', 'institution', None] |
| N45 | invalid | invalid | yes | dispute_status wrong type (v1.0 string form) | at dispute_status: 'none' is not of type 'object' |
| N46 | invalid | invalid | yes | conformance_suite_version fails semver pattern | at scoring_model/conformance_suite_version: 'v1' does not match '^\\d+\\.\\d+\\.\\d+$' |
| N47 | invalid | invalid | yes | R5: tier asserted with formative use | at intended_use: 'credentialing' was expected |
| N48 | invalid | invalid | yes | R5: tier asserted with credentialing use left unvalidated | at use_authorization_status: 'unvalidated' is not one of ['conditionally_authorized', 'authorized'] |
| N49 | invalid | invalid | yes | R5: tier asserted with credentialing use prohibited | at use_authorization_status: 'prohibited' is not one of ['conditionally_authorized', 'authorized'] |
| N50 | invalid | invalid | yes | R5: tier authorized but no validation evidence attached | at validation_status: None is not of type 'object' |
| N51 | invalid | invalid | yes | R5: tier authorized with an empty validation_status object | at validation_status: 'validation_evidence_uri' is a required property |
| N52 | invalid | invalid | yes | R1: summative use asserted as authorized with an empty validation_status object | at validation_status: 'validation_evidence_uri' is a required property |
| N53 | invalid | invalid | yes | R6: dispute upheld for the learner with no action on the record | at dispute_status/record_action: 'none' is not one of ['corrected', 'invalidated'] |
| N54 | invalid | invalid | yes | dispute_status.record_action not in enum | at dispute_status/record_action: 'rescored' is not one of ['none', 'corrected', 'invalidated', 'reassessment_required', None] |
