# Standard Learning Provenance Taxonomy for AI-Mediated Education

**SLPT-AIQ Specification Document — Version 1.2**

Issued by Answer Labs Inc., May 2026. Revised August 2026.
Classification: Public Standard
Specification ID: SLPT-AIQ-v1.2

License: Apache 2.0 (software artifacts). Specification text dual-licensed under CC BY 4.0.

---

**SLPT-AIQ v1.2** · Standard Learning Provenance Taxonomy · Answer Labs Inc.
Apache 2.0 (software) · CC BY 4.0 (specification text)

> **Change at v1.2.** This revision withdraws four provisions of the v1.0 text that the
> v1.1.0 schema had already superseded in practice: the Boolean bloom-inversion flag and
> its recommended 20% penalty (§8.3), dimensional permanence (§3 Principle 4), the
> *Discernment and Taste* and *Learning Velocity* dimension names (§4.3, §4.5), and the
> employer mapping (§11) — all four withdrawn. It adds the four-claim boundary (§1.5), the cross-field
> conformance rules including the credential gate (§6.4), and normative deployment
> governance (§12.4). **Where this text and the JSON Schema disagree, the schema is
> normative for record conformance.**

## Executive summary

This document defines the Standard Learning Provenance Taxonomy (SLPT), an open
specification for recording how individuals interact with generative AI during
learning, in a portable and machine-checkable record format. SLPT records the
provenance of an interaction. It does not record, and does not claim to measure, the
provenance of a learner's knowledge.

As generative AI becomes more common in learning and knowledge work, institutions
increasingly need records that distinguish different patterns of human–AI interaction
rather than recording only task completion or final output. SLPT proposes a common
structural vocabulary for recording selected interaction features. **Whether those
features support valid inferences about learner capability remains an empirical
question outside schema conformance.**

SLPT provides a vocabulary and a JSON Schema through which platforms and institutions
can record those features in a common structure. **What conformance to this
specification establishes is that a record satisfies the published structural rules.
It does not establish measurement validity, educational interpretation, or fitness
for any consequential decision.** The four claims are separated in §1.5 and the
boundary is enforced by the cross-field rules in §6.4.

This specification covers: (1) the definition of qualifying learning events in AI
contexts, (2) the five proposed AIQ dimensions and their observable signals, (3)
the data schema for learning provenance records, (4) context filtering rules that
separate learning signal from general usage, and (5) governance principles for
standard evolution.

---

## Table of contents

1. Introduction and rationale (§1.1 interaction-record gap · §1.5 four-claim boundary)
2. Definitions
3. Core principles
4. The five proposed AIQ dimensions
5. Learning event classification
6. Data schema — Learning Provenance Record, including §6.4 cross-field conformance rules
7. Context filter rules
8. Bloom's taxonomy integration, including §8.3 delegation-pattern annotation
9. AIQ estimate computation
10. Verification and the credential gate
11. Employment use — prohibited
12. Governance and evolution, including §12.4 deployment governance
13. Related work
14. Appendix — observable signal examples

---

## 1. Introduction and rationale

### 1.1 The interaction-record gap

Conventional educational records usually preserve outcomes, completion states, grades
or assessment results rather than the sequence and context of the learner–AI
interaction that contributed to an activity. Two learners may produce similar outputs
while interacting with generative AI in materially different ways, and ordinary records
need not preserve that distinction.

SLPT addresses this record-structure gap. It does not claim that interaction traces are
superior to conventional assessment, that existing credentials have ceased to be
informative, or that interaction traces validly measure cognition. Those are empirical
questions outside schema conformance, and §1.5 states where they sit.

### 1.2 Interaction features represented in SLPT

SLPT represents a small set of proposed interaction features, chosen because they can
in principle be observed from learner–AI episodes and may be useful in subsequent
research on AI-mediated learning. **No claim is made here that these features are the
primary differentiator in knowledge work, that they are irreplaceable, or that AI is
unable to reproduce them.** Those are predictions about technology, not specification
content.

- how a problem is framed before model output exists
- how model output is disposed of: accepted, rejected, verified, cited, contradicted
- what happens when output is conflicting or low-confidence
- whether behaviour changes across episodes after corrective feedback

### 1.3 Why a standard is necessary

Without a shared record contract, platforms may represent learner–AI interaction using
incompatible field names, structures and context conventions. SLPT provides a proposed
common vocabulary and JSON Schema against which records can be validated.

**This establishes a portability target and a conformance mechanism. It does not
demonstrate semantic interoperability between independent implementations**, which
requires separate multi-implementation testing and is not attempted here. Employer
comparison and cross-institutional benchmarking are non-permitted uses under §10 and
§11, and are not offered as motivations for this specification.

The specification is intentionally narrow at its core. Five proposed dimensions, four
first-order and one candidate composite. A single schema. Clear context rules.

### 1.4 Open / hosted boundary

The specification and implementer documentation are openly published under Apache 2.0.
The dimension scoring implementation and the institutional co-signature infrastructure
are operated as a hosted service by Answer Labs Inc. rather than published as source.
Any implementer is free to build their own scorer against the dimension definitions
in §4. The specification documents the scoring methodology at the conceptual level
needed for independent implementation. The JSON Schema and the OpenAPI contract for the
scoring endpoint are published in this release. The xAPI, CLR / Open Badges, Common
Cartridge and CTDL adapters remain roadmap items. See the repository README for a fuller discussion.

---

### 1.5 The four claims this specification separates

Following the interpretation-and-use distinction in validity theory (Kane 2013;
Messick 1995), SLPT separates four claims and states the status of each at this
release.

| Layer | Claim | Status at v1.2.0 |
|---|---|---|
| L1 | **Schema conformance** — a record satisfies the published structural rules | **Demonstrated.** Validator and conformance corpus, §6.4 and `conformance/` |
| L2 | **Measurement validity** — evidence supports a specified interpretation of recorded values | **Not established.** No completed validation study |
| L3 | **Educational interpretation** — what a teacher or learner may infer in a defined context | **Formative only**, and gated on L2 |
| L4 | **Decision use** — grading, certification, progression, employment | **Not authorized.** Gated on L2, enforced by §6.4 R1 and R5 |

Each layer is gated on the one below it. **Conformance is not interoperability.** A
record satisfying the schema is testable against one published contract; whether
independent implementations exchange and correctly interpret records is a stronger
property that this release does not demonstrate.

---

## 2. Definitions

The following terms have precise meanings within this specification.

| Term | Definition |
|---|---|
| **Learning Event** | Any discrete interaction between a human and an AI model that occurs within a verified learning context and produces at least one observable signal across one or more AIQ dimensions. |
| **Learning Provenance** | A structured, timestamped record of learning events attributed to an individual, carrying the context, selected interaction features, provenance references and a query-text hash. **Plaintext query content is not part of the record**, and a field hash does not make the record as a whole tamper-resistant. |
| **AIQ (Artificial Intelligence Quotient)** | A composite estimate derived from normalized measurements across the five proposed dimensions. The interpretation of that estimate is **not established**: no completed validation study supports it, and §6.4 R5 makes any credential tier non-conformant until such evidence is attached to the record. |
| **Verified Learning Context** | An interaction occurring within an institutionally configured AI environment — AI tutors, structured assistants, quizzes, graded assignments, or deep research sessions — as distinct from general-purpose AI usage. |
| **Dimension Signal** | An observable feature of an interaction, proposed as candidate evidence for one or more dimensions and derived from interaction patterns rather than self-report. **Its validity as evidence of capability is not established.** |
| **Institutional Co-Signature** | The formal attestation by an accredited educational institution or qualified employer that a learning provenance record was generated within their governed AI environment and meets their quality threshold. |
| **Context Filter** | The rule set applied to raw interaction data to determine which events qualify as learning events for provenance purposes, excluding general-purpose usage, personal conversations, and non-educational interactions. |
| **Longitudinal Signal** | A dimension signal whose value is computed across a defined time window to reflect behavioral patterns rather than isolated instances. |
| **Bloom's Taxonomy** | The hierarchical classification of cognitive learning objectives (Remember, Understand, Apply, Analyze, Evaluate, Create) used as a secondary mapping layer within SLPT to connect AIQ signals to established academic frameworks. |
| **SLPT Record (LPR)** | A structured data object conforming to the schema defined in §6, representing a single learning event within the provenance system. |

---

## 3. Core principles

SLPT is governed by seven design principles that take precedence over implementation
convenience.

**Principle 1 — Behavioral evidence only.** AIQ dimensions are scored exclusively
from observable behavioral signals derived from interaction data. Self-reported skills,
endorsements, and declarative assessments are excluded from AIQ computation.

**Principle 2 — Minimum evidence window.** Implementations may require a configurable
minimum interaction history before reporting a dimension estimate, and single-session
performance is excluded. **These thresholds are implementation parameters and are not
validated in this release. A minimum history requirement does not establish measurement
validity.**

**Principle 3 — Context integrity.** Only events occurring within verified learning
contexts contribute to the provenance record. Platforms are required to implement
context filtering (§7) before computing any AIQ dimension estimate.

**Principle 4 — Dimensional revisability.** The five dimensions defined in §4 are
proposals, not fixtures. The construct model is unvalidated, and the validation
programme must be free to merge, split, rename or delete any dimension on evidence.
Changes follow the version procedure in §12; they are not prohibited by it. This
principle replaces the *dimensional permanence* rule of v1.0, which committed the
specification to a construct model no evidence supported.

**Principle 5 — Traceability by reference.** Any implementation producing dimension
estimates shall record a versioned computation-method identifier and the relevant
configuration identifiers, so that a record can be traced to the declared scoring
method. **These identifiers establish traceability by reference. They do not prove that
a hosted service executed the declared code, and they do not establish comparability
between estimates.**

**Principle 6 — Learner access and control.** The learner shall have access to the
learner-facing record and to the sharing and correction rights defined by the
deployment policy and applicable law. Institutional co-signature does not reduce those
rights. Ownership of an education record is a legal question that varies by
jurisdiction and institutional policy; this specification does not settle it.

**Principle 7 — Version and epoch traceability.** Each estimate shall identify the
scoring-model version, the configuration and the interaction epoch. **Comparability
across model versions or epochs is not assumed.** Longitudinal comparison requires
separate linking or equating evidence, including subgroup drift analysis where
relevant. A moving population baseline does not by itself equate forms or versions.

---

## 4. The five proposed AIQ dimensions

### 4.0 Dimension selection rationale

The five dimensions were identified by cross-referencing three bodies of evidence:
(1) established metacognitive and critical-thinking taxonomies with demonstrated
validity in educational and professional settings (Facione 1990; King and Kitchener
1994; Bloom revised 2001); (2) empirical studies of how generative AI affects
knowledge-work outcomes, which motivate attention to human judgment without establishing
these dimensions (Dell'Acqua et al. 2023; Brynjolfsson et al. 2025; WEF 2023); and (3) the constraint that each dimension must
be observationally distinct — measurable from interaction-log behavioral data without
self-report — and non-redundant with the others. Twelve candidate dimensions were
considered; consolidation to five was driven by parsimony and the
observable-evidence constraint. §3 Principle 4 governs: the set is revisable. The
procedure was internal and the record was reconstructed afterwards rather than kept
prospectively. It was not a Delphi study, a consensus study, or a content-validity
study, and it does not constitute validation evidence.
Alternatives considered and excluded include domain knowledge acquisition (measurable
only through assessment, not interaction patterns) and AI tool fluency (increasingly
non-differentiating as AI access universalises).

### 4.1 Judgment Quality (JQ) — candidate composite

**Judgment Quality is a candidate second-order or formative composite, not a
first-order dimension.** Its evidence is distributed across Question Originality,
Source and Output Discernment, Synthesis Under Ambiguity and Adaptability rather than
residing in a slice of the record they do not read. **It has no unique observable
indicator set in this release.**

The appropriate measurement model has not been established. Correlated-factor,
higher-order, bifactor and formative specifications remain to be compared, and whether
the composite is formative rather than reflective changes which validation methods are
admissible at all. **Implementations MUST NOT treat the current composite weighting, or
any interpretation of it, as validated.**

Motivated by Facione (1990) on evaluation and inference, and by King and Kitchener
(1994) on Reflective Judgment Model stages 6–7. Motivation is not validation.

*Candidate contributing signals, all already represented in the first-order
dimensions:* follow-up queries that challenge a previous model answer; explicit
corrections or disagreements; multi-model comparison within a session; citation
verification; requests for reasoning transparency; framing of tasks with defined
constraints, audience and output parameters.

### 4.2 Question Originality (QO)

Proposed to represent whether an individual generates queries that push beyond the
well-trained boundaries of AI models — indicating genuine intellectual initiative rather than
efficient information retrieval. Grounded in Oppenlaender et al. (2024) on creative
prompt quality as a skill-differentiating activity.

**Observable signals:** Queries classified as analytical, evaluative, or creative;
session-initiation patterns; topic trajectory; cross-domain query linking.

### 4.3 Source and Output Discernment (SOD)

Records the learner's disposition of model output: accept, reject, verify, cite or
contradict. Motivated by Dell'Acqua et al. (2023) on navigating the "jagged
technological frontier". **The dimension formerly named *Discernment and Taste* is
renamed.** "Taste" is culturally situated and does not belong in an assessment
specification; the term is withdrawn and does not appear in the schema.

**Observable signals:** Multi-model comparison selections; refinement patterns; query
iteration depth; feedback quality on AI outputs; cross-platform verification behavior.

### 4.4 Synthesis Under Ambiguity (SA)

Records candidate evidence of producing coherent understanding or direction from
conflicting, incomplete or uncertain model output. **No measurement model is validated.** Maps to King and Kitchener (1994)
Stages 6–7 for coherent construction from uncertain evidence.

**Observable signals:** Cross-model conflict acknowledgment queries; source
triangulation; explicit uncertainty documentation; multi-hop reasoning chains;
depth and quality progression across reasoning threads.

### 4.5 Adaptability (AD)

Records revision behaviour under corrective feedback across episodes. Motivated by the
inverse of the Fan et al. (2025) "metacognitive laziness" construct.

**Normative constraint: Adaptability shall not be scored on elapsed time, response
latency, or rate of progression.** The *Learning Velocity* framing of v1.0 is
withdrawn. Speed-based scoring disadvantages multilingual learners, neurodivergent
learners, and learners who pause to verify, and it measures fluency of interaction
rather than responsiveness to correction.

**Observable signals:** Revision after a contradiction or correction; reformulation
following a low-quality response; change in approach across episodes. Adaptability is
undefined on a single episode.

### 4.6 Dimension summary

| Dimension | What it measures |
|---|---|
| **Judgment Quality** | *Candidate composite.* No unique indicator set; evidence distributed across the four first-order dimensions |
| **Question Originality** | Intellectual initiative; problem-framing |
| **Source and Output Discernment** | Disposition of model output: accept, reject, verify, cite, contradict |
| **Synthesis Under Ambiguity** | Coherent reasoning across conflicting information |
| **Adaptability** | Revision behaviour under corrective feedback across episodes; never scored on elapsed time |

**SLPT does not prescribe validated universal weights, and v1.2 defines no normative
default weighting.** A hosted implementation may use institution-specific weight
configurations, each of which MUST carry its own identifier, version and digest.
Changing an institution-specific configuration does not change the SLPT specification
version. Any future normative default weighting defined by the specification would
require a major-version change under §12.

Configurations are disclosed to the deploying institution rather than published.
**Estimates produced under different weighting configurations are not comparable across
institutions, and cross-institutional comparison is a non-permitted use.**

---

## 5. Learning event classification

### 5.1 Qualifying event types

Qualifying learning events occurring within a verified learning context: AI Tutor
Session, Structured Assistant Interaction, Quiz Attempt, Deep Research Session,
Graded Assignment Interaction, Reflection Prompt Response.

### 5.2 Non-qualifying interaction types

Explicitly excluded: general-purpose chat not associated with a learning context;
personal, social, or lifestyle queries; image generation requests; administrative
queries; interactions outside an authenticated institutional or verified learner
session; interactions below the minimum session threshold.

### 5.3 Context classification schema

Each qualifying event must be tagged at ingestion with a context type from the
qualifying event list in §5.1, a unique identifier of the specific tutor, assistant,
or quiz instance, an optional institution identifier, a session identifier, a verified
context flag, and a learner-initiated flag.

---

## 6. Data schema — Learning Provenance Record

The complete LPR schema is published in this release as
`schema/lpr_v1.2.0.json`, a JSON Schema Draft 2020-12 document. All required fields,
types and constraints are normative and are defined there. **Where this section and the
schema disagree, the schema governs.** This section describes the schema conceptually.

### 6.1 Privacy-preserving design

Query text is stored as a SHA-256 hash — never the plaintext. Scoring runs on
plaintext before hashing; the LPR persists only the hash. This design enables
credentialing across institutions while preserving FERPA-protected student work
and platform-level conversation privacy.

Platforms implementing SLPT must also implement PII detection and redaction
capabilities for uploaded documents and interaction content. Required capabilities
include:

- Automatic detection of personally identifiable information in uploaded documents
  before ingestion into the learning environment
- An alert system that notifies administrators when PII is detected in uploaded
  content
- Configurable institutional policies governing PII handling — options must include
  at minimum: do not store, anonymize before storage, or redact from administrator
  view
- Audit logging of all PII detection events and policy actions applied

### 6.2 Structured behavioral fields

The LPR captures structured behavioral signals that are primary dimension inputs.
These fields exist alongside interaction-pattern signals to provide a reliable
behavioral baseline that does not depend solely on natural-language processing
accuracy. Behavioral signals include whether the learner initiated the query,
whether they challenged or corrected the AI response, whether they verified across
multiple models, and the depth of their reasoning chain.

### 6.3 Confidence weighting

Each LPR includes a signal confidence field that enables confidence-weighted rolling
averages in estimate computation. Events with low confidence contribute proportionally
less to the dimension estimate.

---

### 6.4 Cross-field conformance rules

Per-field validation cannot express the constraints this specification asserts. A
record could declare credentialing use and an authorized status simultaneously, or
carry a credential tier alongside a prohibited use, and remain structurally valid.
Version 1.2.0 therefore adds six cross-field rules, enforced by the schema's `allOf`
and exercised by both positive and negative fixtures in the conformance corpus.

| # | Rule |
|---|---|
| **R1** | Summative or credentialing use may be asserted as `conditionally_authorized` or `authorized` **only** where a populated `validation_status` object is attached. An empty object does not satisfy the rule. |
| **R2** | Any `conditionally_authorized` or `authorized` status requires an attached `validation_status`. |
| **R3** | A delegation state expressed relative to a task frame requires a `task_frame` to exist. |
| **R4** | A record under dispute requires `learner_access` to be true. A learner cannot contest a record they cannot read. |
| **R5** | A non-null `credential_tier` requires `intended_use` of `credentialing`, a `use_authorization_status` of `conditionally_authorized` or `authorized`, and a populated `validation_status`. |
| **R6** | A dispute upheld for the learner requires a `record_action` of `corrected` or `invalidated`. Reassessment alone does not correct or withdraw the original inference. |

**R1 replaces the flat prohibition of v1.1.** The bar on summative and credentialing
authorization is now attached evidence rather than a release flag, which defines a
path to future authorization instead of a dead end. Because no completed validation
study exists, the practical effect is unchanged: no record produced under this release
can conformantly assert authorized summative or credentialing use, or carry a tier.

**R5 is the credential gate.** Under v1.1 a conformant record could carry
`AIQ_CERTIFIED` alongside `use_authorization_status: prohibited`. That gap is closed.

**R6 answers a specific objection**: that a reassessment does not correct an inaccurate
record or remedy a burden already imposed. Where a dispute is upheld, the record itself
must be corrected or invalidated, and the action is recorded in the record.

---

## 7. Context filter rules

### 7.1 Mandatory filter criteria

An interaction must meet all of the following criteria to qualify as a learning event:

1. Authenticated session associated with a verified learner identity
2. Associated with a defined context type from §5.1
3. Session contains a minimum number of substantive exchanges
4. Does not match non-qualifying patterns from §5.2
5. Occurs within the platform's defined learning environment boundaries
6. Learner authenticated for a minimum duration before the interaction

### 7.2 Personal topic exclusion

Platforms must implement a personal topic classifier that excludes interactions
related to personal relationships, entertainment, financial or legal or medical
advice for non-academic situations, and non-academic political opinions. The personal
topic exclusion is a privacy protection as much as a data quality measure. Learners
must be able to use the platform for personal queries without that usage contributing
to or contaminating their AIQ estimate.

### 7.3 Minimum data requirements

A reportable AIQ estimate requires a minimum period of qualifying interaction
history and a minimum number of qualifying learning events. These thresholds are
configurable by institutional partners and subject to empirical validation in
subsequent versions of this specification. They will be reviewed by the SLPT
Governance Council following the first annual calibration exercise (§12.3).

---

## 8. Bloom's taxonomy integration

### 8.1 Bloom's level definitions within SLPT

REMEMBER, UNDERSTAND, APPLY, ANALYZE, EVALUATE, CREATE — as in Anderson and
Krathwohl (2001).

### 8.2 Bloom's distribution as AIQ evidence

The distribution of a learner's interactions across Bloom's levels is recorded as
observable evidence. Change in that distribution across episodes is one input to
Adaptability; it is not scored on the rate of change. Operation at ANALYZE, EVALUATE
and CREATE levels is recorded as evidence relevant to Question Originality and
Synthesis Under Ambiguity. **None of these mappings is validated**, and §8.3 applies:
a CREATE-level classification does not establish that the learner performed the
creation.

### 8.3 Delegation-pattern annotation

A CREATE-level query submitted to an AI may reflect cognitive delegation — the learner
requesting the model to perform the creation — rather than human cognition at the
CREATE level. Standard Bloom mappings treat both identically.

**The v1.0 Boolean bloom inversion flag and its recommended minimum 20% score
reduction are withdrawn.** The penalty was an implementation convention with no
empirical, consensual, or theoretical basis. It is removed rather than recalibrated,
and no successor penalty is defined.

Platforms implementing SLPT record an **episode-level delegation-pattern annotation**
in the `delegation_annotation` object: whether the annotation is episode-scoped, the
evidence basis, a confidence value, and a state that includes an explicit
`not_assessable` value, which most single episodes will carry. The state is evaluated
against an instructor-declared task frame held in the separate `task_frame` object;
§6.4 R3 makes a state relative to a task frame non-conformant where no task frame
exists.

**The annotation does not determine how cognition was distributed between learner and
model, and it does not modify dimension estimates.** Tool use and cognition co-occur
rather than trade off, and model generation can itself be an instructional component
rather than evidence of avoidance. The annotation is recorded alongside the estimates
as separate evidence carrying its own uncertainty.

This inversion risk was not found formalized in the AI-literacy or learning-analytics
frameworks surveyed during specification development, including LBET
(arXiv:2503.19434) and RUBICON (10.1145/3664646.3664778).

---

## 9. AIQ estimate computation

Platforms shall record a versioned computation-method identifier (§3 Principle 5) so
that a record can be traced to the scoring method that produced it. The approach below
defines the computation structure at the conceptual level needed for independent
implementation. The hosted scoring service implements classifiers against this
structure; **no calibration study has been completed, and "calibrated" is not claimed.**

### 9.1 Dimension estimate calculation

Each dimension estimate is computed as a confidence-weighted rolling average of
event-level signals over an institutionally configured time window:

```
D_estimate = Σ(signal_i × confidence_i) / Σ(confidence_i)
```

for all qualifying events i in the configured window.

### 9.2 AIQ composite estimate

The composite AIQ estimate is a weighted combination of the five dimension
estimates. Dimension weights are configurable at the institutional level within
the hosted scoring service. The composite formula structure is:

```
AIQ = weighted_combination(JQ, QO, SOD, SA, AD) × 100
```

The specific weights are part of the hosted scoring service methodology and are
disclosed to the deploying institution rather than published. Every record names the
weight-configuration identifier, version and digest, so an institution can determine
which configuration produced an estimate. **Estimates produced under different
configurations are not comparable across institutions.** A digest establishes the
identity of a configuration; it does not establish that the hosted service executed it,
and it establishes neither reproducibility nor validity.

### 9.3 Population reference — not established

**No population baseline exists, and none is assumed by this release.** Estimates are
raw and uncalibrated, and shall be labelled as such wherever reported.

A future population reference would not by itself make estimates comparable across
model versions or epochs; Principle 7 governs, and linking or equating evidence is
required. The v1.0 *anti-inflation* commitment — that a level in 2028 would represent
the same relative capability as the same level in 2026 — is **withdrawn**, because a
moving percentile does not equate forms.

### 9.4 Estimate currency and scoring-model drift

Estimate windows reflect the recency and volume of qualifying events and are
configurable by institutional partners.

**A scorer informed by one generation of models drifts as those models change.** Each
scoring-model version is therefore a new assessment form: comparability across versions
requires anchor tasks, linking or equating evidence, and analysis of total and subgroup
scale drift. Records carry the calibration epoch alongside the scoring-model version so
that stale calibration is detectable. A version number or digest establishes provenance,
not comparability, and re-equating is a precondition of any longitudinal claim rather
than an optional refinement.

---

## 10. Verification and the credential gate

SLPT defines two credential tier identifiers, `AIQ_LEARNER` and `AIQ_CERTIFIED`, as
values the `credential_tier` field may carry.

**A credential tier is conformant only under the gate in §6.4 R5.** A record carrying
a non-null tier must declare `intended_use` as `credentialing`, must carry a
`use_authorization_status` of `conditionally_authorized` or `authorized`, and must
attach a populated `validation_status` object naming the validation evidence, the
population it was established on, and the context it covers.

**No completed validation study is reported by the authors at this release, so the
authors make no claim that any current tier is validated or authorized.** Structurally,
R5 permits a tier only where credentialing use, an authorization state and populated
validation metadata are declared together. **Schema validation checks the consistency of
that declaration; it does not establish evidential adequacy.** Whether attached evidence
actually supports the claimed use is a governance and deployment determination, not a
JSON Schema result.

The corpus tests both directions: the gated path with populated evidence is a positive
case, and tier issuance without it is a negative case.

Where an implementation issues tier identifiers outside this gate, **those outputs are
not SLPT-conformant credentials**, and no claim about learner competence follows from
them under this specification.

**Institutional co-signature attests that events occurred within a governed
institutional environment. It does not validate the meaning of any estimate**, and it
lifts no prohibition in §10 or §11.

Vendor-neutral requirements on a co-signing institution: it operates a deployment with
context filtering active; attests that events occurred within its governed environment;
accepts liability for the accuracy of its attestation; maintains audit records for five
years; and reports co-signature volumes annually.

*Reference-implementation note, not a specification requirement:* co-signature through
the Answer Labs hosted service additionally requires an active partnership with Answer
Labs Inc. That is a property of one implementation. **An independent implementation of
this specification is not required to route co-signature through any vendor.**

---

## 11. Employment use — prohibited

**The employer mapping table of v1.0 is withdrawn in its entirety.** It mapped
credential tiers to job families on no evidence, and it was inconsistent with the
prohibition on employment use that every Learning Provenance Record carries.

Employment, hiring and selection use of SLPT records or any estimate derived from them
is **not authorized**. The prohibition is recorded in the record itself through
`intended_use` and `use_authorization_status`, is carried into customer agreements,
and is not lifted by institutional co-signature.

AIQ does not measure: domain-specific technical expertise; interpersonal skills; work
ethic; character; or capability in non-AI-mediated contexts. Nor, at this release, has
it been shown to measure what it does name.

---

## 12. Governance and evolution

### 12.1 SLPT Governance Council

The SLPT Governance Council is convened initially by Answer Labs Inc. and transitions
to a multi-institutional governance structure within 24 months. Target composition:
3 university representatives, 2 enterprise employers, 2 independent researchers,
1 representative per platform implementing SLPT with 10,000+ active learners, 1 learner
advocate.

### 12.2 Version control

| Type | Triggers | Required vote |
|---|---|---|
| Major (x.0) | Changes to the dimension set, schema breaking changes, credential gate definitions | 75% Council supermajority. Prior version remains valid for 24 months. |
| Minor (1.x) | Optional schema fields, clarifications, qualifying event additions | Simple majority. Backward compatible. |
| Patch (1.0.x) | Error corrections, clarifications, examples | Council chair approval. |

### 12.3 Annual evidence review

**No calibration baseline exists and no calibration protocol is defined at this release
(§9.3), so no calibration exercise can be required.** Implementations participate in an
annual evidence review: what validation work has been completed, what drift has been
observed across scoring-model versions, and what remains unestablished. There is no
SLPT compliance certification to lose, and none is issued.

---

### 12.4 Deployment governance — normative

These rules bind deployments, not record structure. They exist because consent,
appeal, retention and correction cannot be settled inside a schema, and because a
specification that leaves them unstated leaves the learner unprotected.

**12.4.1 Equivalent route.** Where an SLPT-scored activity is assigned as required
coursework, the deploying institution **shall** offer an equivalent route to
completing the learning objective that does not require automated scoring, **or**
shall record a documented necessity-and-proportionality basis for requiring it. A
deployment offering neither is not a conformant deployment of this specification.
Learners shall be informed which of the two applies before the activity begins.

**12.4.2 Independent appeal.** The operator performs first-line technical review of
scoring-model defects. **The deploying institution is the authority of last resort for
any dispute carrying academic or other consequential effect**, and this allocation
shall be recorded in the deployment agreement. An appeal path in which the operator is
the final authority over defects in its own scorer is not independent and does not
satisfy this section.

**12.4.3 Retention on dispute.** Interaction traces are retained for a default period
for adjudication only. **Opening a dispute suspends deletion of the evidence relevant
to that record until final adjudication, plus a defined post-decision period.** The
record states whether the evidence was still available when a dispute was adjudicated,
so a dispute rejected on the merits is distinguishable from one decided after the
evidence was gone.

**12.4.4 Record correction.** Where an inference is overturned, the original record
shall be marked corrected or invalidated under §6.4 R6, with the reason and the
adjudicator recorded, and any downstream representation updated or withdrawn.
Reassessment is not correction.

**12.4.5 Separation of formative estimates from summative judgment.** No automated
summative gradebook passback. No cross-learner ranking. Estimates return to an
institutional dashboard post hoc rather than surfacing in a gradebook view, and where
role-based access control permits, dimension estimates shall be withheld from the
instructor of record until the relevant grade is finalized. **This reduces the occasion
for a formative estimate to influence a summative judgment informally. It does not
eliminate it, and no logging requirement detects it.**

---

## 13. Related work

SLPT builds on and differentiates from prior work in three categories.

**AI literacy frameworks.** Long and Magerko (2020), Ng et al. (2021), and
Annapureddy et al. (2024) define competencies for AI literacy at the conceptual level.
Validated AI-literacy instruments in the comparison set use either self-report scales,
for example MAILS (Carolus et al. 2023) and SNAIL (Laupichler et al. 2022), or
objective and contrived tests, for example AICOS (Markus et al. 2025). **AICOS is an
objective multiple-choice instrument, not a self-report scale.** Within the search
frame reported with the accompanying SoftwareX article, no psychometrically validated
instrument was identified whose reported score is derived directly from authentic,
naturalistic learner–AI interaction traces. SLPT differs in specifying behavioural
signals observable from interaction logs; it is not a validated instrument and does not
replace one.

**Closest existing taxonomy: LBET** (Enhanced Bloom's Educational Taxonomy for
Fostering Information Literacy with LLMs, arXiv:2503.19434, 2025). Maps LLM
interaction behaviors to Bloom-derived levels using behavioral observation. SLPT
absorbs LBET's behavioural observation method and extends it by (a) defining question
originality and discernment as dimensions independent of Bloom levels, (b) targeting a
portable record structure rather than in-classroom pedagogy, and (c) specifying a
machine-readable schema and provenance fields. **Interoperability across independent
implementations and cross-platform comparability of estimates remain unestablished, and
no calibration protocol is defined at this release.**

**Closest existing technical system: RUBICON** (Microsoft Research,
10.1145/3664646.3664778, 2024). Scores multi-turn developer-AI conversations using
rubrics for correctness and coherence. SLPT extends to five judgment-centric
dimensions, non-developer learners, and a portable provenance schema rather than a
point-in-time rubric.

---

## 14. Appendix — observable signal examples

### Judgment Quality examples

| Behavior | JQ signal |
|---|---|
| "Are you sure about that?" after a factual claim | High — direct challenge |
| Same question checked across multiple AI models before accepting | High — multi-model verification |
| Accepts first answer without follow-up | Low / none |
| "What are the counterarguments to this?" | High — active evaluation |
| Corrects AI factual error explicitly | Very high — error detection |
| Asks AI to explain its reasoning | Medium — transparency request |
| Frames task with full context, audience, and constraints | High — strategic direction |

### Question Originality examples

- *"What would happen to YAP signaling if we disrupted chromatin tension?"* — high
  (cross-domain synthesis, beyond standard training)
- *"What is the acid mantle?"* — low (factual recall, well within training)
- *"How do principles of epidermal differentiation map to organizational change
  management?"* — very high (unexpected cross-domain connection)
- Learner initiates session defining their own research hypothesis — high

### Synthesis Under Ambiguity examples

- "These models contradict each other — how do I evaluate which is more reliable?"
  — high
- "I'm not sure if this applies to my context because..." — medium (gap awareness)
- "What would I need to know to be confident about this conclusion?" — high
  (gap identification)
- Triangulates AI output against uploaded primary source, notes discrepancy
  — very high

### Adaptability examples

- Learner proactively asks for v2 of previous output to improve it — high
- Learner recovers from a low-quality AI response by reformulating the question
  — high
- Learner revises an approach after a contradiction is surfaced — high
- Learner repeats identical queries across sessions with no change following
  correction — low

Adaptability is undefined on a single episode and is never scored on elapsed time.

---

*End of specification — SLPT-AIQ-v1.2*

*Answer Labs Inc. | answerr.ai | May 2026*

*This specification is released as an open standard under Apache 2.0 (software) and
CC BY 4.0 (specification text). Reproduction, adaptation, and implementation are
permitted with attribution.*
