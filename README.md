# SLPT — Standard Learning Provenance Taxonomy

**An open specification and JSON Schema for recording learner–AI interaction.**

[![License](https://img.shields.io/badge/license-Apache_2.0-blue.svg)](LICENSE)
[![Spec Version](https://img.shields.io/badge/spec-v1.2-green.svg)](spec/SLPT-AIQ-v1.2.md)

---

## What this is

SLPT is an open specification for recording how individuals interact with generative AI
during learning. It defines five proposed dimensions — four first-order and one candidate
composite: judgment quality, question originality, source and output discernment,
synthesis under ambiguity, and adaptability. It specifies a machine-readable data
contract, the Learning Provenance Record (LPR), that platforms can use to document
AI-mediated learning events in a portable, privacy-preserving form.

**SLPT records the provenance of an interaction, not the provenance of a learner's
knowledge.** Conformance to the schema establishes that a record satisfies published
structural rules. It does not establish measurement validity, interoperability between
independent implementations, or legal compliance. Those four claims are separated in §1.5
of the specification, and the boundary between them is enforced by the cross-field rules
in §6.4.

### What is in this release

| Component | Path |
|---|---|
| Specification document, SLPT-AIQ v1.2 | `spec/SLPT-AIQ-v1.2.md` |
| Learning Provenance Record JSON Schema, Draft 2020-12 | `schema/lpr_v1.2.0.json` |
| Conformance validator and 70-fixture corpus | `conformance/` |
| OpenAPI contract for the hosted scoring endpoint | `api/openapi.json` |
| Release gate for retired claims | `release_assert.py` |
| Implementer guide and FAQ | `docs/` |
| Changelog and citation metadata | `CHANGELOG.md`, `CITATION.cff` |
| LTI 1.3 + AGS integration contract | described in the specification |

**Roadmap, not in this release:** the interoperability adapters — xAPI, CLR / Open Badges,
Common Cartridge, CTDL, European Learning Model.

**Not in this repository at all:** scoring logic, dimension formulas, signal weights, tier
thresholds, classifier code, and prompt templates. Those are operated as a hosted service
by Answer Labs Inc. See [The open / hosted boundary](#the-open--hosted-boundary).

---

## Why this exists

Conventional educational records usually preserve outcomes, completion states, grades or
assessment results rather than the sequence and context of the learner–AI interaction that
contributed to an activity. Two learners may produce similar outputs while interacting with
generative AI in materially different ways, and ordinary records need not preserve that
distinction.

Validated AI-literacy instruments in the comparison set use either self-report scales, for
example MAILS and SNAIL, or objective and contrived tests, for example AICOS. **AICOS is an
objective multiple-choice instrument, not a self-report scale.** Within the search frame
reported with the accompanying SoftwareX article, no psychometrically validated instrument
was identified whose reported score is derived directly from authentic, naturalistic
learner–AI interaction traces.

SLPT addresses a record-structure gap: it specifies what counts as a qualifying learning
event, what is observable from it, and how that serializes into a portable record. It does
**not** claim that interaction traces are superior to conventional assessment, that
existing credentials have ceased to be informative, or that recorded values validly
measure cognition.

The dimensions are revisable on evidence (§3 Principle 4). The construct model is
unvalidated and the validation programme must be free to merge, rename or delete any of
them.

### On regulation

Where a deployment falls under Annex III point 3(b) of the EU AI Act, the LPR contains
fields that **may support** provider record-keeping (Article 12) and transparency to
deployers (Article 13) workflows. Query-text hashing and the prohibition on plaintext
persistence reduce the learner content retained in a record and may support institutional
privacy and data-minimisation requirements.

**Schema conformance does not establish legal compliance.** Whether a given deployment
satisfies the AI Act, FERPA, GDPR or any other instrument depends on the scoring service,
the institutional workflow and the applicable legal role. SLPT is compliance-supporting
infrastructure, not a compliance mechanism.

---

## Getting started

**Read the specification.** `spec/SLPT-AIQ-v1.2.md`. Start with §1.5, the four-claim
boundary, then §6.4, the cross-field conformance rules. Where the specification text and
the JSON Schema disagree, **the schema is normative for record conformance.**

**Validate a record.** From the repository root:

```
pip install jsonschema
python3 conformance/slpt_validate.py conformance/tests/valid_minimal.json --schema schema/lpr_v1.2.0.json
python3 conformance/slpt_validate.py --run-corpus --schema schema/lpr_v1.2.0.json
python3 release_assert.py .
```

The corpus contains 71 fixtures, 17 positive and 54 negative. A negative fixture
reproduces its expected outcome by being *rejected*: each was built from a conformant base
record by introducing one targeted violation. Class totals and per-fixture results are in
`CONFORMANCE_MANIFEST.md` and its JSON sibling, together with the toolchain versions and
the SHA-256 of the schema, validator and specification.

**Integrate.** If you are deploying Answerr at your institution or integrating via
LTI 1.3, start with `docs/IMPLEMENTER_GUIDE.md`. For hosted scoring API access, contact
tech@answerr.ai.

---

## The record and the credential gate

### The Learning Provenance Record

Each qualifying learning event produces an LPR: a structured, privacy-preserving object
carrying the event context, the observable interaction features, the episode-level
delegation annotation with its own uncertainty state, the identity of the scoring model
and weighting configuration, the declared use and authorization status, dispute state and
learner access, and the SHA-256 hash of the query text. **The plaintext never enters the
record.** The complete field set, types and constraints are normative and defined in
`schema/lpr_v1.2.0.json`.

Dimension estimates are nullable. A record can be structurally conformant while declining
to assert any measurement.

### Credential tiers are gated, not awarded

SLPT defines two credential tier identifiers, `AIQ_LEARNER` and `AIQ_CERTIFIED`, as values
the `credential_tier` field may carry. **A tier is conformant only under rule R5** (§6.4):
the record must declare `intended_use` as `credentialing`, carry a
`use_authorization_status` of `conditionally_authorized` or `authorized`, and attach a
populated `validation_status` naming the evidence, the population it was established on,
and the context it covers.

**No completed validation study is reported by the authors at this release, so the
authors claim no current tier as validated.** Structurally, R5 permits a tier only where
credentialing use, an authorization state and populated validation metadata are declared
together. **Schema validation checks the consistency of that declaration; it does not
establish evidential adequacy** — whether attached evidence actually supports the use is
a governance determination, not a JSON Schema result.

No proficiency band, score interpretation or statement about learner capability is
validated by this specification. Where an implementation issues tier identifiers outside
the R5 gate, **those outputs are not SLPT-conformant credentials**, and no claim about
learner competence follows from them here.

Weighting configurations differ by institution and are disclosed to the deploying
institution rather than published. **Estimates produced under different configurations are
not comparable across institutions, and cross-institutional comparison is a non-permitted
use.** Employment, hiring and selection use is not authorized (§11).

---

## The open / hosted boundary

SLPT is published under Apache 2.0. The specification, JSON Schema, conformance harness,
OpenAPI contract and implementer documentation are free to use, implement and extend. Two
parts of the system are operated as a hosted service rather than published as source: the
dimension scoring engine and the institutional co-signature infrastructure.

**Why scoring is hosted.** The scoring layer translates observable signals into dimension
estimates. Hosting keeps the record contract stable while the implementation changes.

**What that costs, stated plainly.** A scorer informed by one generation of models drifts
as those models change. Each scoring-model version is a new assessment form: comparability
across versions requires anchor tasks, linking or equating evidence, and analysis of
subgroup scale drift. Records carry the scoring-model version, the weight-configuration
identity and the interaction epoch so that drift is detectable. **A version identifier
establishes provenance, not comparability, and changing the scoring logic is not assumed
to preserve the meaning of estimates already issued.**

**Why this is still open.** Publishing the specification and the schema lets institutions
and third-party implementers validate records without adopting the hosted service, and
build independent scorers against the published dimension definitions. Every record names
the scorer and configuration that produced it, so records from different implementations
are **distinguishable**. They are not thereby comparable, and this repository makes no
claim that a tier means the same thing across institutions.

**Institutional co-signature** attests that events occurred within a governed institutional
environment. It is an institutional relationship rather than a software artifact, and it
does not lift any prohibition in §10 or §11.

---

## Deployment governance

§12.4 of the specification is normative for deployments: an equivalent non-scored route or
a documented necessity-and-proportionality basis; the deploying institution as authority of
last resort for consequential disputes; suspension of evidence deletion while a dispute is
open; correction or invalidation of a record where a dispute is upheld, since reassessment
is not correction; and separation of formative estimates from summative judgment.

**These rules define SLPT-conformant deployment behaviour. They do not assert that any
existing deployment already satisfies them.** They are added prospectively at v1.2.0.

---

## Compatible standards

SLPT is designed to interoperate with, not replace, existing learning-data infrastructure.
**Interoperability with independent implementations is an intended system property that
this release does not demonstrate**; it would require multi-implementation exchange
testing.

### Current

| Standard | Body | Use |
|---|---|---|
| **LTI 1.3 + AGS** | 1EdTech | Single sign-on and grade passback into Canvas, Moodle, Blackboard, Brightspace. AGS is an available transport, not a permitted deployment: the reference connector rejects summative passback where use is prohibited or unvalidated. |

### Roadmap

| Standard | Body | Use |
|---|---|---|
| xAPI 1.0.3 | ADL Initiative | Statement-based event transport into a Learning Record Store |
| CLR 2.0 / Open Badges 3.0 | 1EdTech | Verifiable credential packaging |
| cmi5 | ADL Initiative | xAPI profile for completion and progress |
| Common Cartridge 1.3 | 1EdTech | Course packaging with embedded provenance |
| CTDL | Credential Engine | Machine-readable credential description |
| European Learning Model | European Commission | EU-compatible record portability |

---

## Citing this work

```
Undheim, T. A., Malik, M. Qaiser, Hashmi, N. (2026). SLPT — Standard Learning
Provenance Taxonomy for AI-Mediated Education, v1.2.0. Answer Labs Inc.

Malik, M. Qaiser., & Undheim, T. A. (2025). AI infrastructure for trust and learning
in education: The emergence of the 'Learning Provenance' concept. NEAIS 2025
Proceedings. https://aisel.aisnet.org/neais2025/2
```

Machine-readable metadata is in `CITATION.cff`. A SoftwareX submission describing the
schema, conformance tooling and claim boundary is under review.

---

## Repository layout

```
slpt/
├── spec/                       SLPT-AIQ-v1.2 specification
├── schema/                     LPR JSON Schema, current and superseded versions
├── conformance/                validator, 70-fixture corpus, test records
├── api/                        OpenAPI contract for the hosted scoring endpoint
├── docs/                       implementer guide and FAQ
├── release_assert.py           release gate for retired claims
├── build_manifest_v120.py      regenerates the conformance manifests
├── CHANGELOG.md
├── CITATION.cff
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE                     Apache 2.0
└── README.md                   (this file)
```

---

## Governance

The SLPT Governance Council, composition in §12.1 of the specification, governs revisions.
Major version changes require a 75% Council supermajority; minor versions a simple
majority. §12.2 defines what counts as major.

## Contributing

Independent scorers built against the specification, adapter contributions, translations,
and clarification requests are welcome. See `CONTRIBUTING.md`.

## License

Apache License 2.0 — see [`LICENSE`](LICENSE). Specification text is also released under
CC BY 4.0 for non-software reuse.

## Contact

**tech@answerr.ai** — Answer Labs Inc., Newark, Delaware, USA — [answerr.ai](https://answerr.ai)
