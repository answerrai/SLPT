# SLPT Implementer Guide

A practical guide for universities and enterprise partners adopting the
Standard Learning Provenance Taxonomy through Answerr.

---

## Who this guide is for

This guide is for university administrators, IT teams, and enterprise
learning and development leads who are evaluating or deploying Answerr as an
SLPT-integrated AI learning platform.

**A note on the word compliant.** Record conformance is determined by validating
a record against `schema/lpr_v1.2.0.json`. Deployment conformance is determined
by §12.4 of the specification, and **§12.4 was added prospectively at v1.2.0;
operator and institutional confirmation is outstanding.** Neither is established
by using this platform.

---

## How implementation works today

SLPT implementation is available through a direct partnership with
Answer Labs Inc. To get started, institutions and enterprises partner
directly with Answer Labs Inc. Once onboarded, API access is available
for programmatic integration into your existing systems.

To begin, contact **tech@answerr.ai**. The Answerr team will guide you
through the full onboarding process.

---

## What you get as a partner

### The Answerr platform

A fully hosted AI learning environment that your learners access directly.
The platform includes AI Tutors, AI Assistants, Quizzes, Grading, and
Analytics — instrumented to serialize candidate Learning Provenance Records.
**Whether a given record conforms is determined by validating it against the
schema**, not by the platform that produced it.

### LTI 1.3 integration

Answerr connects to your existing LMS — Canvas, Moodle, Blackboard, or
Brightspace — via LTI 1.3 with Assignment and Grade Services (AGS).
This means:

- Learners access Answerr directly from within your LMS
- Single sign-on using your institution's existing identity provider
- Completion and enrolment data pass back into your gradebook
- **No automated summative passback of SLPT dimension estimates.** §12.4.5
  prohibits it, and the reference connector rejects passback where use is
  prohibited or unvalidated. Estimates return to an institutional dashboard
  post hoc, not to a gradebook view
- No separate login or platform switching required for learners

### AIQ™ credentials

`AIQ_LEARNER` and `AIQ_CERTIFIED` are values the `credential_tier` field may
carry. **They are gated, not awarded.** Rule R5 in §6.4 of the specification
makes a non-null tier conformant only where the record declares credentialing
use, carries a validation-gated authorization state, and attaches populated
validation evidence.

**No completed validation study is reported by the authors at this release, so the
authors claim no current tier as validated**, and no proficiency band or score
interpretation is validated by this specification. Schema validation checks the
consistency of the declaration a record makes; **it does not establish evidential
adequacy**, which is a governance determination. Where the hosted product emits tier
identifiers outside the gate, those outputs are not SLPT-conformant credentials.

Institutions and enterprises who are active Answerr partners may also add their
own co-signature. **A co-signature attests that events occurred within a governed
institutional environment. It does not validate the meaning of any estimate**, and
lifts no prohibition in §10 or §11.

The Answerr platform and the AIQ API can emit proprietary AIQ product outputs.
**Those are product outputs, not SLPT-conformant credential tiers**, and the
AIQResponse object returned by the API is not a Learning Provenance Record — see
the boundary statement in `api/openapi.json`.

### Configurable dimension weights

Both universities and enterprise partners can configure dimension weights
to reflect the skills most relevant to their learning objectives. A
university might weight question originality and synthesis more heavily
for research programmes. An enterprise might weight strategic framing
and judgment more heavily for senior leadership development. Default
weights are operated as part of the hosted scoring service.


### Privacy and compliance

Query text is SHA-256-hashed: the plaintext of what your learners type never
enters the record. That reduces the learner content retained and **may support**
your institutional privacy obligations; it does not by itself establish FERPA,
GDPR or any other compliance, which depends on your workflow and legal role.
For current certifications and their scope, ask tech@answerr.ai. Certification
and legal compliance are different things.

Answerr also provides PII detection and redaction capabilities for uploaded
documents:

- Uploaded documents are automatically scanned for personally identifiable
  information before ingestion
- Administrators receive alerts when PII is detected in uploaded content
- Institutional policies are configurable — options include do not store,
  anonymize before storage, or redact from administrator view
- All PII detection events and policy actions are audit logged

Institutions deploying Answerr should sign a data processing agreement with
Answer Labs Inc. as part of onboarding.

---

## What you need to do

### Before onboarding

- Confirm your LMS platform — Canvas, Moodle, Blackboard, or Brightspace
- Identify your LMS administrator who will register Answerr as an
  approved external tool inside your LMS — this is a one-time step
  required by LTI 1.3
- Identify the courses or programmes where Answerr will be deployed
- Confirm your Microsoft or Google SSO configuration if applicable

### During onboarding

Once your partnership is confirmed:

1. Your team accesses the Answerr educator dashboard and generates
   your institution's API key
2. Your LMS administrator uses the API key to register Answerr as
   an approved external tool in your LMS via LTI 1.3
3. Answerr configures your AI Tutors and Assistants for your
   learning context
4. A test session confirms SSO and grade passback are working
5. Your faculty or L&D team is briefed on the platform

### After go-live

- Answerr provides an analytics dashboard for instructors and
  administrators
- Proprietary AIQ product outputs are generated automatically. **They are not
  SLPT-conformant credential tiers**, and no record produced under v1.2.0 carries
  a tier the authors claim as validated
- The Answerr team remains available for ongoing support via
  **tech@answerr.ai**

---

## For enterprise partners

The onboarding process for enterprise partners follows the same pattern
as universities. Answerr supports deployment across large employee populations with 
customAI configurations tailored to your organisation's learning objectives and
industry context.

---

## API access

API access is available on request for integration into learning-administration
systems: institutional dashboards, LMS platforms and reporting tools.

**Employment, hiring and selection use is not authorized** (§11 of the
specification). That prohibition is recorded in every record through
`intended_use` and `use_authorization_status`, is carried into customer
agreements, and is not lifted by institutional co-signature. Integration into HR
or talent-management systems is outside permitted use.

Contact **tech@answerr.ai** to discuss integration options.

---

## Contact

For all partnership and implementation enquiries:

**tech@answerr.ai**

Answer Labs Inc. — Newark, Delaware, USA — [answerr.ai](https://answerr.ai)
