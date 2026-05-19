# SLPT — Frequently Asked Questions

---

## About the specification

**Q: Why exactly five dimensions?**

A: The five dimensions were selected from a larger candidate set by applying
three constraints: each must be observable from interaction logs without
self-report, each must be non-redundant with the others, and each must
correlate with documented knowledge-work productivity outcomes. The selection
rationale is documented in §4.0 of the specification.

**Q: Why are the dimension weights configurable?**

A: Both universities and enterprise partners can configure dimension weights
to reflect the skills most relevant to their learning objectives. Default
weights are operated as part of the hosted scoring service and are stable
across the version — ensuring that credentials issued under the same version
remain comparable. Weights can only change by major version revision with
75% Council supermajority per §12.

**Q: How is this different from xAPI or CLR?**

A: xAPI and CLR are transport standards — they describe how learning data
moves between systems. SLPT is a semantic standard — it describes what to
measure in the first place. The two layers are complementary. SLPT Learning
Provenance Records will export to xAPI and CLR via adapters on the roadmap.

**Q: How is this different from existing AI literacy frameworks?**

A: Every validated AI literacy instrument relies on self-report — asking
the learner what they know or believe. SLPT measures observable behavior
in interaction logs. The two are not directly comparable — they answer
different questions about different evidence.

---

## About the open / hosted boundary

**Q: Why isn't the scorer open source?**

A: The hosted-service model allows scoring logic to improve continuously
without invalidating previously issued credentials. This is the same pattern
major model APIs use — stable contract, evolving inference. The specification
describes the dimensions and their observable signals at the conceptual level
needed for independent implementation.

**Q: Can I implement my own scorer?**

A: Yes. The specification documents the five dimensions and their observable
signals at the conceptual level needed for independent implementation. We
welcome independent scorers — file an issue tagged `independent-implementation`
and we will link to yours from the README.

**Q: Is this really open if the scorer is hosted?**

A: The specification, implementer documentation, and LTI 1.3 integration
are openly published under Apache 2.0. The data contract is open. The
inference behind the contract is hosted. This is the same architecture used
by major API-first platforms — open contract, hosted inference, single-vendor
reference implementation. Anyone is free to build their own implementation.

**Q: Does this satisfy the EU AI Act?**

A: Article 12 record-keeping is satisfied by the Learning Provenance Record
structure, fully described in the specification. Article 13 transparency is
satisfied by the published specification, the documented purpose and
capabilities of the system, and the OpenAPI contract for the scoring endpoint
available to institutional partners. The Act does not require disclosure of
source code for the inference layer of high-risk AI systems.

---

## About implementation

**Q: How does implementation work?**

A: Implementation is available through a direct partnership with Answer Labs
Inc. Once onboarded, your team accesses the Answerr educator dashboard,
generates your API key, and your LMS administrator registers Answerr as an
approved external tool via LTI 1.3. Contact **tech@answerr.ai** to begin.

**Q: What LMS platforms does Answerr support?**

A: Canvas, Moodle, Blackboard, and Brightspace via LTI 1.3 with Assignment
and Grade Services for grade passback.

**Q: How does this work with FERPA?**

A: Query text is SHA-256-hashed — the plaintext of what learners type never
enters the credential record. Answerr is FERPA compliant. Institutions
deploying Answerr should sign a data processing agreement with Answer Labs
Inc. as part of onboarding.

**Q: What compliance certifications does Answerr hold?**

A: Answerr is certified or compliant with FERPA, SOC 2 Type II, GDPR,
HIPAA, and ISO 27001.

**Q: Can a student be under 13?**

A: COPPA applies to learners under 13. Under-13 learners require parental
consent before interaction logging. Age-gating at the authenticated session
layer is a platform responsibility governed by §7.1 of the specification.

---

## About credentials

**Q: What are the two credential tiers?**

A: AIQ Learner shows a proficiency band across the five SLPT dimensions —
from Initializing through to Frontier — and is issued and signed by
Answer Labs Inc. AIQ Certified shows an exact AIQ credential across all
five dimensions and is issued and signed by Answer Labs Inc., with the
option for the institution or employer to add their own co-signature.

**Q: How does an employer verify a credential?**

A: Credential verification is available via the AIQ API, accessible to
institutional partners on request. Contact **tech@answerr.ai** to discuss
verification integration.

**Q: Do credentials expire?**

A: Validity windows are configurable by universities and enterprise partners
to reflect their own assessment policies. Contact **tech@answerr.ai** to
discuss configuration options during onboarding.

**Q: Can a credential be revoked?**

A: Yes. Institutional co-signatures can be withdrawn if the institution
determines that learning events did not occur within their governed
environment, per §10.2 of the specification.

**Q: What if a learner's AI capability improves over time?**

A: AIQ credentials reflect current behavior within the configured validity
window. A learner who consistently challenges AI output and verifies across
models will see their Judgment Quality improve over time. The credential
is designed to be a live reflection of capability, not a static snapshot.

---

## About governance

**Q: Who can change the specification?**

A: The SLPT Governance Council. Initial composition is convened by Answer
Labs Inc. Target composition over 24 months includes universities, enterprise
employers, independent researchers, representatives from SLPT-compliant
platforms, and a learner advocate. See §12 of the specification.

**Q: When will v1.1 be released?**

A: When the Council convenes and ratifies the v1.1 changes. Current candidate
additions include xAPI and CLR adapters, CTDL, European Learning Model
portability, and EU AI Act Article 12 audit-trail export. Targeting June 2026.

**Q: How do I propose a change?**

A: File an issue on this repository. Issues tagged `governance-review` go
to the Council for evaluation.

---

## Practical questions

**Q: My institution wants to pilot SLPT. What is the path?**

A: Contact **tech@answerr.ai**. The Answerr team will walk you through
partnership options, onboarding, and pilot configuration for your
institution or organisation.

**Q: Can I get API access for testing?**

A: Yes. API access for testing and integration is available to partners
on request. Contact **tech@answerr.ai** to discuss options.

**Q: I found something in the specification that is unclear or contradictory.**

A: File an issue on this repository describing the ambiguity and where it
appears in the document. Most clarifications become patch-level releases.