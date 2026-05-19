# SLPT — Standard Learning Provenance Taxonomy

**An open specification for documenting human judgment in AI-mediated learning.**

[![License](https://img.shields.io/badge/license-Apache_2.0-blue.svg)](LICENSE)
[![Spec Version](https://img.shields.io/badge/spec-v1.0-green.svg)](spec/SLPT-AIQ-v1.0.md)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20297510.svg)](https://doi.org/10.5281/zenodo.20297510)

---

## What this is

SLPT is an open specification for capturing how individuals learn and demonstrate judgment in AI-mediated environments. It defines five permanent dimensions of human capability that become more — not less — valuable as AI capability advances: judgment quality, question originality, discernment and taste, synthesis under ambiguity, and learning velocity. It specifies a machine-readable data contract — the Learning Provenance Record (LPR) — that platforms can use to document AI-mediated learning events in a way that is portable, privacy-preserving, and verifiable.

This repository contains:

- The **SLPT-AIQ-v1.0 specification document** (`spec/`)
- **LTI 1.3 integration** for single sign-on and grade passback into Canvas, 
  Moodle, Blackboard, and Brightspace
- Implementer documentation and FAQ (`docs/`)

What this repository does **not** contain: scoring logic, dimension formulas, signal weights, tier thresholds, classifier code, or prompt templates used to evaluate interactions. Those are operated as a hosted service by Answer Labs Inc. 

See [The open / hosted boundary](#the-open--hosted-boundary) below for why.

The JSON Schema, OpenAPI contract, and interoperability adapters — xAPI, 
CLR / Open Badges, Canvas, Common Cartridge — are on the roadmap and will be 
published alongside the hosted API. See [Roadmap](#roadmap) below.

---

## Why this exists

The credential gap in AI-mediated education has two forms. First, existing credentials measure what a person has been exposed to — courses completed, quizzes passed — not how they think when working with AI. A student who critically interrogates every AI output and one who passively accepts the first answer can receive identical credentials. Second, no existing standard specifies what behavioral evidence of AI-mediated learning should look like as machine-readable data. Every validated AI literacy instrument relies on self-report, which cannot scale to the volume of AI-assisted work now common in higher education and the workplace.

SLPT addresses both gaps by specifying (a) what counts as a qualifying learning event, (b) what behavioral signals are observable from the event, and (c) how those signals serialize into a portable record. The specification is intentionally narrow: five permanent dimensions, one schema, clear context rules. Narrowness is the source of its durability — it defines only what will remain relevant as AI capability advances, not what is merely interesting today.

The specification is also compliance infrastructure. The EU AI Act categorizes AI systems used in education as high-risk and requires record-keeping (Article 12) and transparency (Article 13). SLPT's LPR serves as that audit trail. Institutions need this kind of provenance regardless of which platform they use; the open specification gives them a vendor-neutral target.

---

## Getting started

SLPT v1.0 is a specification release. No tooling installation is required
to read, implement, or reference the standard.

**Read the specification**

The full SLPT-AIQ-v1.0 specification is in `spec/SLPT-AIQ-v1.0.md`. Start there to understand the five dimensions, qualifying event definitions, and the Learning Provenance Record structure.

**Read the implementer guide**

If you are deploying Answerr at your institution or integrating via LTI 1.3, start with `docs/IMPLEMENTER_GUIDE.md`.

**Request API access**

The hosted scoring API is operational and currently available to selected institutional partners. To request access or discuss integration,
contact tech@answerr.ai.

The JSON Schema, validator, adapters, and OpenAPI contract will be published
in a subsequent release alongside the hosted API.

---

## What's in v1.0

### The five permanent dimensions

| Dimension | What it measures |
|---|---|
| **Judgment Quality** | How critically a learner evaluates AI output — questioning, correcting, and strategically directing the AI rather than accepting responses at face value |
| **Question Originality** | The degree to which a learner drives the inquiry — initiating conversations, framing problems, and demonstrating intellectual initiative |
| **Discernment & Taste** | The ability to evaluate output quality across sources and models — distinguishing strong responses from adequate ones |
| **Synthesis Under Ambiguity** | Coherent reasoning across conflicting or incomplete information — building deeper understanding through sustained reasoning chains |
| **Learning Velocity & Adaptability** | How quickly a learner improves — recovering from setbacks and proactively refining their own work over time |

Dimension weights are configurable at the institutional level, allowing universities and enterprise partners to adjust emphasis across dimensions to reflect their
learning objectives. Default weights are operated as part of the hosted scoring service.

### The Learning Provenance Record

Each qualifying learning event produces a Learning Provenance Record (LPR) —  a structured, privacy-preserving object that captures four things:

- The **event context** — where and under what institutional conditions the interaction occurred
- The **learner's behavioral signals** — how the learner engaged with the AI, including whether they challenged, verified, refined or strategically directed 
  the interaction
- The **interaction quality classification** — the complexity, depth and Bloom's taxonomy level of the exchange
- The **institutional trust level** — the verification tier under which the 
  event was recorded

Query text is SHA-256-hashed. The plaintext never enters the record. The full LPR schema will be published alongside the hosted API.

### Credential tiers

SLPT supports two credential tiers, both issued by Answer Labs Inc.:

- **AIQ™ Learner** — awarded to any learner who meets the minimum activity
  threshold on the Answerr platform. Shows a proficiency band across the
  five SLPT dimensions — from Initializing through to Frontier. Signed by
  Answer Labs Inc.

- **AIQ™ Certified** — a co-signed credential issued jointly by Answer Labs Inc.
  and the learner's institution or employer once they are an active Answerr
  partner. Shows an exact score across all five SLPT dimensions. Carries
  institutional authority alongside the Answer Labs Inc. signature.

Both credentials can be generated directly through the Answerr platform or
programmatically via the AIQ API, currently available to institutional partners
on request. Contact tech@answerr.ai to discuss integration.

---

## The open / hosted boundary

SLPT is published under Apache 2.0. The specification, LTI 1.3 integration,
and implementer documentation are free to use, implement, and extend. Two parts
of the system are operated as a hosted service rather than published as source:
the dimension scoring engine and the institutional co-signature infrastructure.
This section explains why.

**Why scoring is hosted.** The scoring layer translates raw behavioral signals
into dimension scores and the AIQ™ credential. The hosted-service model
allows scoring logic to improve continuously without invalidating previously
issued credentials. This is the same pattern used by major model APIs: the
inference improves over time, the contract stays stable.

**Why this is still open.** SLPT is an open standard — not a proprietary
product. Publishing the specification allows universities, employers, and
developers to build on a common framework, reference it in academic work,
and trust that AIQ™ credentials mean the same thing regardless of which
institution issued them. The scoring implementation is hosted by Answer
Labs Inc. The standard itself belongs to the community.

**Why institutional co-signature is hosted.** Both AIQ Learner and AIQ
Certified credentials can carry an institutional co-signature once the
institution is an active Answerr partner. This co-signature attests that
learning events occurred within a governed institutional environment. It
is not a software artifact — it is an institutional relationship. The
hosted infrastructure manages those relationships on behalf of partner
institutions.

**What this means for compliance.** The EU AI Act Article 13 transparency
requirement is satisfied by the published specification, the documented purpose
and capabilities of the system, and the OpenAPI contract for the scoring
endpoint available to institutional partners. The Act does not require disclosure
of source code for the inference layer of high-risk AI systems. The Article 12
record-keeping requirement is satisfied by the LPR structure, fully described
in the specification. FERPA compliance is preserved by the query-text-hashing
design specified in §6.1 of the specification.
---

## Compatible standards

SLPT is designed to interoperate with, not replace, existing learning-data
infrastructure.

### Current integrations

| Standard | Body | Use |
|---|---|---|
| **LTI 1.3 + AGS** | 1EdTech | Single sign-on and grade passback into Canvas, Moodle, Blackboard, and Brightspace |

### Planned integrations

| Standard | Body | Use |
|---|---|---|
| xAPI 1.0.3 | ADL Initiative | Statement-based event transport into any Learning Record Store |
| CLR 2.0 / Open Badges 3.0 | 1EdTech | Verifiable credentials, one per dimension plus composite |
| cmi5 | ADL Initiative | xAPI profile for course completion and progress |
| Common Cartridge 1.3 | 1EdTech | Course packaging with embedded provenance |
| CTDL | Credential Engine | Machine-readable credential description |
| European Learning Model | European Commission | EU-compatible learning record portability |

### Compliance

Answerr is certified or compliant with the following frameworks:

| Framework | Scope |
|---|---|
| **FERPA** | Student data privacy — USA |
| **SOC 2 Type II** | Security, availability, and confidentiality controls |
| **GDPR** | Data protection and privacy — European Union |
| **HIPAA** | Health information privacy standards |
| **ISO 27001** | Information security management |

---

## Citing this work

If you reference SLPT in academic work, please cite both the specification and the underlying empirical foundation:

```
Undheim, T. A., Malik, M. Qaiser, Hashmi, N. (2026). SLPT — Standard Learning Provenance Taxonomy
for AI-Mediated Education, v1.0. Answer Labs Inc. DOI pending.

Malik, M. Qaiser., & Undheim, T. A. (2025). AI infrastructure for trust and learning in
education: The emergence of the 'Learning Provenance' concept. NEAIS 2025 Proceedings.
```

A SoftwareX submission describing the schema, adapter ecosystem, and conformance tooling is in preparation.

---


## Repository layout

```
slpt/
├── spec/                       SLPT-AIQ-v1.0 specification
├── docs/                       Implementer guide and FAQ
├── LICENSE                     Apache 2.0
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── README.md                   (this file)
```

---

## Roadmap

| Milestone | Contents | Status |
|---|---|---|
| **v1.0** | Specification, LTI 1.3 integration, implementer documentation | This release |
| **Hosted scoring API** | Public OpenAPI contract, JSON Schema | Available to partners on request |
| **v1.1** | xAPI, CLR / Open Badges, Common Cartridge, CTDL, ELM | 2026–2027 |

The SLPT Governance Council (composition described in §12 of the specification)
governs all subsequent revisions. Major version changes require a 75% Council
supermajority; minor versions require simple majority.

---

## Contributing

We welcome:

- Independent scorers built against the SLPT specification
- Adapter contributions for additional standards
- Translations of the specification document
- Issues and clarification requests against the specification

See `CONTRIBUTING.md` for the process. The specification document is governed
conservatively — see §12 of the spec — and changes require Council review.

---

## License

Apache License 2.0 — see [`LICENSE`](LICENSE). Specification text is also released under CC BY 4.0 for non-software reuse.

---

## Contact

For specification questions, institutional partnerships, API access,
or press enquiries, contact **tech@answerr.ai**

Answer Labs Inc. — Newark, Delaware, USA — [answerr.ai](https://answerr.ai)
