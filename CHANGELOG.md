# Changelog

All notable changes to the SLPT specification are documented here. The format
is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this
project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.2.0] — 2026-08

Alignment release. v1.1.0 shipped a schema that had already superseded the
specification prose it was released alongside; this release makes the text, the
schema and the conformance corpus describe the same object.

### Specification — withdrawn

- **§8.3 Boolean bloom-inversion flag and its recommended minimum 20% score
  reduction.** Removed rather than recalibrated. No successor penalty is defined.
- **§3 Principle 4, dimensional permanence.** Replaced by dimensional revisability.
- **§4.3 Discernment and Taste** → **Source and Output Discernment**. "Taste" is
  culturally situated and is withdrawn.
- **§4.5 Learning Velocity and Adaptability** → **Adaptability**, with a normative
  constraint prohibiting scoring on elapsed time.
- **§11 Employer mapping.** Withdrawn in its entirety; employment use is prohibited.

### Specification — added

- **§1.5** the four-claim boundary: schema conformance, measurement validity,
  educational interpretation, decision use, with the status of each.
- **§6.4** cross-field conformance rules R1–R6.
- **§12.4** normative deployment governance: equivalent route, independent appeal,
  retention on dispute, record correction, separation of formative from summative.
  These rules define SLPT-conformant deployment behaviour. **They do not assert that
  every existing deployment already satisfies them**; they are added prospectively and
  operator confirmation is outstanding.

### Schema — `schema/lpr_v1.2.0.json`

- **R1 recast.** Summative or credentialing use may be asserted as authorized only
  where a *populated* `validation_status` is attached. The bar is evidence, not a
  release flag. An empty object no longer satisfies it.
- **R5 added — the credential gate.** A non-null `credential_tier` requires
  credentialing use, an authorization state, and populated validation evidence. Under
  v1.1.0 a conformant record could carry `AIQ_CERTIFIED` alongside
  `use_authorization_status: prohibited`.
- **R6 added.** A dispute upheld for the learner requires a `record_action` of
  `corrected` or `invalidated`.
- **R3 repaired — it was not enforced.** Since v1.1.0 the rule's `then` constrained
  `task_frame`'s type but never required the property, so a record declaring a
  frame-relative delegation state with `task_frame` omitted validated with zero errors.
  Its only negative fixture set the value to `null`, which trips a type check rather than
  the rule. `then` now carries `required: ["task_frame"]`, and the corpus has a true
  omission fixture alongside the null one.
- `rule_probe.py` added. It checks that every conditional rule requires each property its
  `then` constrains, unless the root schema or the rule's own `if` guarantees presence,
  and runs an omission probe per rule. It fails when R3's defect is reintroduced.
- `dispute_status` extended with `opened_at_utc`, `resolved_at_utc`, `outcome` and
  `record_action`.
- `$defs.populated_validation_status` added.

### Conformance

- Corpus extended from 61 to 71 fixtures: 17 positive, 54 negative. All 71 reproduce
  their expected validator outcome.
- The current exemplar `conformance/tests/valid_minimal.json` and the corpus base record
  now carry `record_version: "1.2.0"`; both had inherited `1.1.0`.
- Machine-readable manifest `CONFORMANCE_MANIFEST.json` added alongside the Markdown
  manifest, carrying toolchain versions, per-fixture digests and observed output.

### Repository

- `CITATION.cff` added. Authorship metadata now matches the README citation block.
- **README, FAQ, implementer guide and CONTRIBUTING rewritten to the same claim
  discipline as the specification.** They previously asserted that every validated
  AI-literacy instrument relies on self-report; that the schema and OpenAPI contract
  were future work; that Articles 12 and 13 were *satisfied* and FERPA *preserved* by
  the record structure; a blanket "certified or compliant" table; that credentials
  mean the same thing across institutions; and that scoring logic improves without
  invalidating previously issued credentials. All withdrawn.
- **`api/openapi.json` boundary made explicit.** `AIQResponse` is a proprietary product
  object. It is not a Learning Provenance Record, carries none of the fields rule R5
  evaluates, and cannot establish SLPT conformance. Its vocabulary deliberately differs
  from the schema.
- **Schema self-identity corrected.** `lpr_v1.2.0.json` described itself as
  "Learning Provenance Record v1.1 ... conforms to SLPT-AIQ-v1.1 §6".
- `release_assert.py` added: a release gate that fails on any retired claim
  reappearing outside this changelog, now **19 rules**. Every rule exists because the
  string it forbids was published once and had to be withdrawn, and each has a
  negative control confirming it can fail. **28 rules at this build.** The gate is a
  regression detector, not a semantic reviewer: it found none of the defects an
  independent read found, and both the R3 defect and the FAQ and implementer-guide
  contradictions passed it before being caught by hand.
- **R5 wording corrected across spec, README, FAQ and implementer guide.** The earlier
  text said no record could conformantly carry a tier and that the validator enforced
  it. The corpus disproves that: the gated path with populated evidence is a positive
  case. Schema validation checks the consistency of a declaration; it does not establish
  evidential adequacy, which is a governance determination.

---

## [1.1.0] — 2026-08

Not recorded at the time. Reconstructed here from the release tree.

### Added

- `schema/lpr_v1.1.0.json` — the Learning Provenance Record JSON Schema, Draft 2020-12.
- `conformance/` — command-line validator and a 61-fixture corpus.
- `api/openapi.json` — OpenAPI 3.1.0 contract for the hosted scoring endpoint.
- Cross-field conformance rules R1–R4.
- `credential_tier` and the dimension estimates made nullable. Under v1.0.0 both were
  required and `credential_tier` was enum-constrained with no null member, so a record
  could not be structurally conformant without asserting a credential and five scores.

### Fixed

- The v1.0.0 tag did not contain `schema/`; the schema was committed after the tag was
  cut. The v1.1.0 tag is cut from a tree containing both `schema/` and `conformance/`.

---

## [1.0.0] — 2026-05

Initial public release.

### Specification

- Published SLPT-AIQ-v1.0 specification document under Apache 2.0 (software)
  and CC BY 4.0 (text).
- Five permanent dimensions: Judgment Quality, Question Originality,
  Discernment & Taste, Synthesis Under Ambiguity, and Learning Velocity &
  Adaptability. *(Superseded at 1.2.0 — see above.)*
- Two credential tiers: AIQ™ Learner and AIQ™ Certified.
- Seven core principles (§3): behavioral evidence only, longitudinal validity,
  context integrity, dimensional permanence, transparent methodology, learner
  data sovereignty, anti-inflation.

### Integrations

- LTI 1.3 + AGS integration for single sign-on and grade passback into Canvas,
  Moodle, Blackboard, and Brightspace.

### Documentation

- Repository README explaining the open / hosted boundary.
- Implementer Guide (`docs/IMPLEMENTER_GUIDE.md`).
- FAQ (`docs/FAQ.md`).
- Contributing guide and Code of Conduct.

### Roadmap for subsequent releases

- JSON Schema for the Learning Provenance Record.
- Public OpenAPI contract for the hosted scoring API.
- Interoperability adapters — xAPI, CLR / Open Badges, Common Cartridge,
  CTDL, European Learning Model.
- Conformance validator and converter tools.

---

[1.0.0]: https://github.com/answerrai/SLPT/releases/tag/v1.0.0

[1.1.0]: https://github.com/answerrai/SLPT/releases/tag/v1.1.0
[1.2.0]: https://github.com/answerrai/SLPT/releases/tag/v1.2.0
