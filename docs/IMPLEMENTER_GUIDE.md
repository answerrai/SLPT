# SLPT Implementer Guide

A practical guide for universities and enterprise partners adopting the
Standard Learning Provenance Taxonomy through Answerr.

---

## Who this guide is for

This guide is for university administrators, IT teams, and enterprise
learning and development leads who are evaluating or deploying Answerr
as their SLPT-compliant AI learning platform.

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
Analytics — all instrumented to produce SLPT-compliant Learning Provenance
Records automatically.

### LTI 1.3 integration

Answerr connects to your existing LMS — Canvas, Moodle, Blackboard, or
Brightspace — via LTI 1.3 with Assignment and Grade Services (AGS).
This means:

- Learners access Answerr directly from within your LMS
- Single sign-on using your institution's existing identity provider
- Grades and completion data pass back automatically into your gradebook
- No separate login or platform switching required for learners

### AIQ credentials

Every learner on the Answerr platform generates an AIQ credential
automatically as they interact with AI. Two tiers are available:

- **AIQ Learner** — issued and co-signed by Answer Labs Inc. Shows a
  proficiency band across the five SLPT dimensions — from Initializing
  through to Frontier. Available to all learners meeting the minimum
  activity threshold.

- **AIQ Certified** — issued and co-signed by Answer Labs Inc. Shows
  an exact AIQ credential across all five SLPT dimensions. Institutions
  and enterprises who are active Answerr partners may also add their
  own co-signature, carrying their authority alongside the Answer Labs
  Inc. signature.

Both credentials can be generated directly through the Answerr platform
or programmatically via the AIQ API, available to partners on request.

### Configurable dimension weights

Both universities and enterprise partners can configure dimension weights
to reflect the skills most relevant to their learning objectives. A
university might weight question originality and synthesis more heavily
for research programmes. An enterprise might weight strategic framing
and judgment more heavily for senior leadership development. Default
weights are operated as part of the hosted scoring service.


### Privacy and compliance

Answerr is FERPA compliant and certified or compliant with SOC 2
Type II, GDPR, HIPAA, and ISO 27001. Query text is SHA-256-hashed — the plaintext
of what your learners type never enters the credential record.

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
- AIQ credentials are generated automatically — no manual intervention
  required
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

For partners who want to integrate AIQ credentials programmatically into
their own systems — HR platforms, talent management tools, internal
dashboards, or LMS platforms — API access is available on request.

Contact **tech@answerr.ai** to discuss integration options.

---

## Contact

For all partnership and implementation enquiries:

**tech@answerr.ai**

Answer Labs Inc. — Newark, Delaware, USA — [answerr.ai](https://answerr.ai)
