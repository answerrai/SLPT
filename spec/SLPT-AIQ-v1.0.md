# Standard Learning Provenance Taxonomy for AI-Mediated Education

**SLPT-AIQ Specification Document — Version 1.0**

Issued by Answer Labs Inc., May 2026
Classification: Public Standard
Specification ID: SLPT-AIQ-v1.0

License: Apache 2.0 (software artifacts). Specification text dual-licensed under CC BY 4.0.

---

## Executive summary

This document defines the Standard Learning Provenance Taxonomy (SLPT) — an open
specification for capturing, classifying, and credentialing how individuals learn
and demonstrate judgment in AI-mediated environments.

As artificial intelligence handles an expanding share of knowledge work, the most
valuable human capabilities are no longer what a person knows or even how efficiently
they acquire knowledge. They are the irreplaceable cognitive and evaluative behaviors
that AI cannot replicate: judgment, original questioning, taste in discernment,
direction-setting under ambiguity, and synthesis across conflicting information.

SLPT provides a standardized vocabulary and data schema for platforms, institutions,
and employers to measure and verify these behaviors consistently — enabling the
emergence of the AIQ (Artificial Intelligence Quotient) as a portable, trusted
credential for the AI economy.

This specification covers: (1) the definition of qualifying learning events in AI
contexts, (2) the five permanent AIQ dimensions and their observable signals, (3)
the data schema for learning provenance records, (4) context filtering rules that
separate learning signal from general usage, and (5) governance principles for
standard evolution.

---

## Table of contents

1. Introduction and rationale
2. Definitions
3. Core principles
4. The five permanent AIQ dimensions
5. Learning event classification
6. Data schema — Learning Provenance Record
7. Context filter rules
8. Bloom's taxonomy integration
9. AIQ credential computation
10. Verification and credential tiers
11. Employer mapping
12. Governance and evolution
13. Related work
14. Appendix — observable signal examples

---

## 1. Introduction and rationale

### 1.1 The problem with existing credentials

Traditional credentials — degrees, certificates, test scores — measure what a person
has been exposed to, not how they think. This gap has always existed but was tolerable
when the primary differentiator in knowledge work was access to information. AI
eliminates information asymmetry as a differentiator entirely. Any person with access
to a capable AI model can now produce outputs that would previously have required years
of domain training. This renders most traditional credentialing signals obsolete as
proxies for actual capability.

### 1.2 The new signal that matters

What AI cannot replicate are the meta-cognitive behaviors that determine whether
AI-assisted output is good, appropriate, original, or trustworthy. These behaviors —
collectively the human judgment layer — become the primary differentiator in an
AI-augmented workforce:

- Knowing which questions are worth asking, not just how to answer them
- Evaluating whether an AI output is correct, appropriate, or trustworthy
- Setting direction when the problem itself is undefined
- Synthesizing conflicting information into coherent judgment
- Demonstrating taste — distinguishing good from merely adequate

### 1.3 Why a standard is necessary

Without a common taxonomy, every platform measuring AI-mediated learning invents its
own metrics. Employers cannot compare signals across platforms. Institutions cannot
benchmark against peers. Students cannot port their learning record between providers.

SLPT establishes the shared vocabulary that enables interoperability — the same
relationship that FICO has to credit scoring, xAPI has to learning records, or HL7
has to healthcare data. Platforms implementing SLPT produce records that are mutually
intelligible regardless of their underlying technology.

The specification is intentionally narrow at its core. Five permanent dimensions. A
single schema. Clear context rules. Narrowness is the source of its durability — it
defines only what will remain relevant as AI capability advances, not what is merely
interesting today.

### 1.4 Open / hosted boundary

The specification and implementer documentation are openly published under Apache 2.0.
The dimension scoring implementation and the institutional co-signature infrastructure
are operated as a hosted service by Answer Labs Inc. rather than published as source.
Any implementer is free to build their own scorer against the dimension definitions
in §4. The specification documents the scoring methodology at the conceptual level
needed for independent implementation. The JSON Schema, interoperability adapters,
and OpenAPI contract for the scoring service will be published in a subsequent release
alongside the hosted API. See the repository README for a fuller discussion.

---

## 2. Definitions

The following terms have precise meanings within this specification.

| Term | Definition |
|---|---|
| **Learning Event** | Any discrete interaction between a human and an AI model that occurs within a verified learning context and produces at least one observable signal across one or more AIQ dimensions. |
| **Learning Provenance** | The complete, timestamped, tamper-resistant record of learning events attributed to a specific individual, including the context, content, quality signals, and institutional verification status of each event. |
| **AIQ (Artificial Intelligence Quotient)** | A composite credential derived from normalized measurements across the five permanent dimensions, representing an individual's demonstrated irreplaceable cognitive capability in AI-mediated environments. |
| **Verified Learning Context** | An interaction occurring within an institutionally configured AI environment — AI tutors, structured assistants, quizzes, graded assignments, or deep research sessions — as distinct from general-purpose AI usage. |
| **Dimension Signal** | A measurable behavioral indicator that provides evidence of capability across one or more of the five AIQ dimensions, derived from observable interaction patterns rather than self-report. |
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

**Principle 2 — Longitudinal validity.** No dimension credential derived from
insufficient qualifying learning events shall be considered a valid AIQ signal.
Minimum data thresholds are configurable by institutional partners and subject to
empirical validation in subsequent versions of this specification. Single-session
performance is explicitly excluded.

**Principle 3 — Context integrity.** Only events occurring within verified learning
contexts contribute to the provenance record. Platforms are required to implement
context filtering (§7) before computing any AIQ dimension credential.

**Principle 4 — Dimensional permanence.** The five AIQ dimensions defined in §4 are
permanent. They shall not be added to, removed from, or renamed without a major
version revision of this specification.

**Principle 5 — Transparent methodology.** Any platform issuing AIQ credentials must
publish a methodology identifier sufficient for independent verification that the same
scoring logic produced any pair of comparable credentials. The methodology identifier
is included in every Learning Provenance Record and returned by the hosted scoring
service.

**Principle 6 — Learner data sovereignty.** The individual learner owns their
provenance record. Institutional co-signatures do not transfer ownership. The learner
controls visibility, sharing, and portability of their AIQ credential.

**Principle 7 — Anti-inflation.** AIQ credentials must be calibrated against a
population baseline to prevent credential inflation over time. As AI tools improve
and general AI fluency increases, the baseline adjusts to ensure that a credential
level in 2028 represents the same relative capability as the same level in 2026.

---

## 4. The five permanent AIQ dimensions

### 4.0 Dimension selection rationale

The five dimensions were identified by cross-referencing three bodies of evidence:
(1) established metacognitive and critical-thinking taxonomies with demonstrated
validity in educational and professional settings (Facione 1990; King and Kitchener
1994; Bloom revised 2001); (2) empirical studies documenting which human behaviors
predict knowledge-work quality in AI-augmented environments (Dell'Acqua et al. 2023;
Brynjolfsson et al. 2025; WEF 2023); and (3) the constraint that each dimension must
be observationally distinct — measurable from interaction-log behavioral data without
self-report — and non-redundant with the others. Twelve candidate dimensions were
considered; consolidation to five was driven by parsimony, the requirement for
permanent stability (§3 Principle 4), and the observable-evidence constraint.
Alternatives considered and excluded include domain knowledge acquisition (measurable
only through assessment, not interaction patterns) and AI tool fluency (increasingly
non-differentiating as AI access universalises).

### 4.1 Judgment Quality (JQ)

Measures whether an individual demonstrates critical discernment in their evaluation
of AI-generated outputs. Grounded in Facione (1990) on "evaluation" and "inference,"
and in King and Kitchener (1994) on Reflective Judgment Model stages 6–7.

**Observable signals:** Follow-up queries that challenge a previous AI answer;
explicit corrections or disagreements with AI output; multi-model comparison within
a session; citation verification actions; requests for reasoning transparency;
strategic framing of tasks with defined constraints, audience, and output parameters.

Judgment Quality carries the highest dimension weight because it is the most direct
proxy for irreplaceable human value in AI-augmented work environments. An individual
who cannot evaluate AI output is a passive conduit, not a knowledge worker.

### 4.2 Question Originality (QO)

Measures whether an individual generates queries that push beyond the well-trained
boundaries of AI models — indicating genuine intellectual initiative rather than
efficient information retrieval. Grounded in Oppenlaender et al. (2024) on creative
prompt quality as a skill-differentiating activity.

**Observable signals:** Queries classified as analytical, evaluative, or creative;
session-initiation patterns; topic trajectory; cross-domain query linking.

### 4.3 Discernment and Taste (DT)

Measures the ability to consistently identify higher-quality outputs among
alternatives. Operationalizes Dell'Acqua et al. (2023) on navigating the "jagged
technological frontier" — knowing which tasks to delegate to AI and which to retain.

**Observable signals:** Multi-model comparison selections; refinement patterns; query
iteration depth; feedback quality on AI outputs; cross-platform verification behavior.

### 4.4 Synthesis Under Ambiguity (SA)

Measures the ability to produce coherent understanding or direction from conflicting,
incomplete, or uncertain AI-generated information. Maps to King and Kitchener (1994)
Stages 6–7 for coherent construction from uncertain evidence.

**Observable signals:** Cross-model conflict acknowledgment queries; source
triangulation; explicit uncertainty documentation; multi-hop reasoning chains;
depth and quality progression across reasoning threads.

### 4.5 Learning Velocity and Adaptability (LV)

Measures how efficiently an individual moves from unfamiliarity to competent
engagement with new domains, and how they respond when their current approach is not
working. Operationalizes the inverse of Fan et al. (2025) "metacognitive laziness"
construct.

**Observable signals:** Longitudinal query complexity progression; Bloom's level
distribution shift over time; recovery patterns following gaps or low-quality
responses; proactive iterative refinement of previous work.

### 4.6 Dimension summary

| Dimension | What it measures |
|---|---|
| **Judgment Quality** | Critical evaluation of AI output; calibrated trust; strategic direction |
| **Question Originality** | Intellectual initiative; problem-framing |
| **Discernment and Taste** | Output evaluation across sources; refinement |
| **Synthesis Under Ambiguity** | Coherent reasoning across conflicting information |
| **Learning Velocity and Adaptability** | Acquisition rate; recovery; proactive improvement |

Dimension weights are configurable at the institutional level. Default weights are
operated as part of the hosted scoring service and are stable across the version —
ensuring credentials issued under the same version remain comparable. Weights change
only by major version revision with 75% Council supermajority per §12.

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

The complete LPR schema will be published as part of the hosted API release. All
required fields, types, and constraints are normative and will be published as a
JSON Schema Draft 2020-12 document. This section describes the schema conceptually.

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
averages in credential computation. Events with low confidence contribute
proportionally less to the dimension credential.

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
to or contaminating their AIQ credential.

### 7.3 Minimum data requirements

A reportable AIQ credential requires a minimum period of qualifying interaction
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

The distribution of a learner's interactions across Bloom's levels is primary
evidence for the Learning Velocity dimension. Upward shift over time provides strong
LV signal. Operation consistently at ANALYZE, EVALUATE, CREATE levels provides
strong Question Originality and Synthesis Under Ambiguity signal.

### 8.3 Bloom level inversion risk and mitigation

A CREATE-level query submitted to an AI may reflect cognitive delegation — the
learner requesting the AI to perform creation — rather than human cognitive work at
the CREATE level. When this occurs, the Bloom classification overstates the learner's
cognitive contribution and reduces the evidential value of the JQ, DT, and SA signals
from that event.

Platforms implementing SLPT must implement a bloom inversion flag in the Learning
Provenance Record that is set when the platform's classifier determines that the
learner delegated the primary cognitive work to the AI at the stated Bloom level.
Events with this flag active are included in the provenance record but their JQ, DT,
and SA signal contributions are reduced by the platform's implementation-defined
penalty factor. A minimum 20% reduction is recommended.

No prior equivalent of this construct was identified in 40 AI literacy and learning
analytics works surveyed during specification development, including the closest
precedents in LBET (arXiv:2503.19434) and RUBICON (10.1145/3664646.3664778).

---

## 9. AIQ credential computation

Platforms must publish a stable methodology identifier (§3 Principle 5) sufficient
to verify that two credentials were produced by the same scoring logic. The approach
below defines the required computation structure at the conceptual level needed for
independent implementation. The hosted scoring service uses production classifiers
calibrated to the same conceptual model.

### 9.1 Dimension credential calculation

Each dimension credential is computed as a confidence-weighted rolling average of
event-level signals over an institutionally configured time window:

```
D_credential = Σ(signal_i × confidence_i) / Σ(confidence_i)
```

for all qualifying events i in the configured window.

### 9.2 AIQ composite credential

The composite AIQ credential is a weighted combination of the five dimension
credentials. Dimension weights are configurable at the institutional level within
the hosted scoring service. The composite formula structure is:

```
AIQ = weighted_combination(JQ, QO, DT, SA, LV) × 100
```

The specific weights are part of the hosted scoring service methodology and are
available to institutional partners on request.

### 9.3 Population calibration

Raw AIQ credentials are adjusted against population percentiles annually. The
reported AIQ credential reflects percentile-adjusted performance against the full
SLPT platform network.

**Bootstrap period.** In advance of sufficient cross-platform data, SLPT-compliant
platforms shall report raw uncalibrated AIQ credentials and clearly label them as
such. The SLPT Governance Council will establish the first population baseline
calibration no later than 24 months after the first institutional deployment.

### 9.4 Credential validity windows

Credential validity windows reflect the recency and volume of qualifying events.
Windows are configurable by universities and enterprise partners to reflect their
own assessment policies. A credential may be current, historical, or provisional
depending on learner activity within the configured window. Contact Answer Labs Inc.
to discuss validity window configuration during onboarding.

---

## 10. Verification and credential tiers

SLPT supports two credential tiers, both issued and co-signed by Answer Labs Inc.

| Credential | Description |
|---|---|
| **AIQ Learner** | Issued and co-signed by Answer Labs Inc. Shows a proficiency band across the five SLPT dimensions — from Initializing through to Frontier. Available to all learners meeting the minimum activity threshold on the Answerr platform. |
| **AIQ Certified** | Issued and co-signed by Answer Labs Inc. Shows an exact AIQ credential across all five SLPT dimensions. Institutions and enterprises who are active Answerr partners may also add their own co-signature, carrying their authority alongside the Answer Labs Inc. signature. |

Both credentials can be generated directly through the Answerr platform or
programmatically via the AIQ API, available to institutional partners on request.

Institutional co-signature requirements: the institution must be an active Answerr
partner; must operate a deployment with context filtering active; must attest that
events occurred within their governed environment; must accept liability for
co-signature accuracy; must maintain audit records for five years; must report
co-signature volumes annually.

---

## 11. Employer mapping

Advisory, not normative.

| Role category | High-value dimensions | Recommended credential |
|---|---|---|
| Strategy and consulting | JQ, SA, QO | AIQ Certified |
| Engineering and product | QO, JQ, LV | AIQ Certified |
| Research and analysis | SA, DT, QO | AIQ Certified |
| Operations and management | JQ, DT, LV | AIQ Learner or above |
| Creative and marketing | DT, QO, SA | AIQ Learner or above |
| Entry level | LV, QO | AIQ Learner |

AIQ explicitly does not measure: domain-specific technical expertise; interpersonal
skills; work ethic; character; intelligence in non-AI-mediated contexts.

---

## 12. Governance and evolution

### 12.1 SLPT Governance Council

The SLPT Governance Council is convened initially by Answer Labs Inc. and transitions
to a multi-institutional governance structure within 24 months. Target composition:
3 university representatives, 2 enterprise employers, 2 independent researchers,
1 representative per SLPT-compliant platform with 10,000+ active learners, 1 learner
advocate.

### 12.2 Version control

| Type | Triggers | Required vote |
|---|---|---|
| Major (x.0) | Changes to permanent dimensions, schema breaking changes, credential tier definitions | 75% Council supermajority. Prior version remains valid for 24 months. |
| Minor (1.x) | Optional schema fields, clarifications, qualifying event additions | Simple majority. Backward compatible. |
| Patch (1.0.x) | Error corrections, clarifications, examples | Council chair approval. |

### 12.3 Annual calibration requirement

All SLPT-compliant platforms must participate in an annual calibration exercise.
Platforms that fail to participate for two consecutive years lose SLPT compliance
certification.

---

## 13. Related work

SLPT builds on and differentiates from prior work in three categories.

**AI literacy frameworks.** Long and Magerko (2020), Ng et al. (2021), and
Annapureddy et al. (2024) define competencies for AI literacy at the conceptual level.
Validated instruments — MAILS (Carolus et al. 2023), SNAIL (Laupichler et al. 2022),
AICOS (Markus et al. 2025) — rely on self-report. SLPT differs by specifying
behavioral signals observable from interaction logs, with no self-report component.

**Closest existing taxonomy: LBET** (Enhanced Bloom's Educational Taxonomy for
Fostering Information Literacy with LLMs, arXiv:2503.19434, 2025). Maps LLM
interaction behaviors to Bloom-derived levels using behavioral observation. SLPT
absorbs LBET's behavioral observation method and extends it by (a) defining question
originality and discernment as dimensions independent of Bloom levels, (b) targeting
portable interoperable credentialing rather than in-classroom pedagogy, and (c)
specifying a machine-readable schema with cross-platform calibration protocol.

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

### Learning Velocity and Adaptability examples

- Learner proactively asks for v2 of previous output to improve it — high
- Learner recovers from a low-quality AI response by reformulating the question
  — high
- Learner's query complexity increases consistently across sessions — very high
- Learner repeats identical queries across sessions with no progression — low

---

*End of specification — SLPT-AIQ-v1.0*

*Answer Labs Inc. | answerr.ai | May 2026*

*This specification is released as an open standard under Apache 2.0 (software) and
CC BY 4.0 (specification text). Reproduction, adaptation, and implementation are
permitted with attribution.*
