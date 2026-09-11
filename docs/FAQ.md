# SLPT — Frequently Asked Questions

---

## About the specification

**Q: Why exactly five dimensions?**

A: The five were selected from a larger candidate set on three criteria: each
must be observable from interaction logs without self-report, each must be
non-redundant with the others, and each must be motivated by documented work on
knowledge-work quality. **No correlation with productivity outcomes has been
established.** The procedure was internal and reconstructed afterwards; it was
not a Delphi, consensus or content-validity study, and it is not validation
evidence. §4.0 and §3 Principle 4 apply: the dimensions are revisable.

**Q: Why are the dimension weights configurable?**

A: Institutions can configure dimension weights to reflect their learning
objectives. **v1.2 defines no normative default weighting**, and each
configuration carries its own identifier, version and digest so a record names
the configuration that produced it. **Estimates produced under different
configurations are not comparable across institutions**, and same-version
issuance does not make them comparable either — Principle 7 governs, and
comparability requires linking or equating evidence that does not exist.

**Q: How is this different from xAPI or CLR?**

A: xAPI and CLR are transport standards — they describe how learning data
moves between systems. SLPT is a semantic standard — it describes what to
measure in the first place. The two layers are complementary. SLPT Learning
Provenance Records will export to xAPI and CLR via adapters on the roadmap.

**Q: How is this different from existing AI literacy frameworks?**

A: Validated AI-literacy instruments in the comparison set use either
self-report scales, for example MAILS and SNAIL, or objective and contrived
tests, for example AICOS. **AICOS is an objective multiple-choice instrument,
not a self-report scale.** Within the search frame reported with the
accompanying SoftwareX article, none derives its score from authentic
naturalistic interaction traces. SLPT records observable interaction features
and is **not** a validated instrument; it does not replace one.

---

## About the open / hosted boundary

**Q: Why isn't the scorer open source?**

A: Hosting keeps the record contract stable while the implementation changes.
**Changing the scoring logic is not assumed to preserve the meaning of estimates
already issued.** Each scoring-model version is a new assessment form:
comparability across versions requires anchor tasks, linking or equating
evidence, and subgroup drift analysis (§9.4). Records carry the scoring-model
version and interaction epoch so that drift is detectable. The specification
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

A: **No. Schema conformance does not establish legal compliance, and this
specification does not claim it does.** Where a deployment falls under Annex III
point 3(b), the LPR provides fields that **may support** provider record-keeping
under Article 12 and transparency to deployers under Article 13. Whether a given
deployment satisfies the Act depends on the scoring service, the institutional
workflow and the applicable legal role, and is a question for the deployer and
its counsel.

---

## About implementation

**Q: How does implementation work?**

A: Implementation is available through a direct partnership with Answer Labs
Inc. Once onboarded, your team accesses the Answerr educator dashboard,
generates your API key, and your LMS administrator registers Answerr as an
approved external tool via LTI 1.3. Contact **tech@answerr.ai** to begin.

**Q: What LMS platforms does Answerr support?**

A: Canvas, Moodle, Blackboard and Brightspace via LTI 1.3. Assignment and
Grade Services is an available transport, **but §12.4.5 prohibits automated
summative gradebook passback of SLPT estimates**, and the reference connector
rejects passback where use is prohibited or unvalidated. AGS carries
completion and enrolment data, not dimension estimates.

**Q: How does this work with FERPA?**

A: Query text is SHA-256-hashed; the plaintext never enters the record. That
reduces the learner content retained and **may support** your FERPA
obligations. **It does not by itself establish FERPA compliance**, which
depends on your deployment context and how your institution handles education
records. Compliance status is not asserted by this specification; ask
tech@answerr.ai for current scoped attestations. Institutions should sign a
data processing agreement as part of onboarding.

**Q: What compliance certifications does Answerr hold?**

A: Certification status is a matter for Answer Labs Inc. and is not asserted by
this specification. Certification and legal compliance are different things, and
FERPA and HIPAA are statutory regimes rather than certifications a vendor holds.
Ask tech@answerr.ai for current attestations and their scope.

**Q: Can a student be under 13?**

A: COPPA applies to learners under 13. Under-13 learners require parental
consent before interaction logging. Age-gating at the authenticated session
layer is a platform responsibility governed by §7.1 of the specification.

---

## About credentials

**Q: What are the two credential tiers?**

A: `AIQ_LEARNER` and `AIQ_CERTIFIED` are values the `credential_tier` field may
carry. **A tier is conformant only under rule R5** (§6.4): credentialing use, a
validation-gated authorization state, and populated validation evidence attached
to the record. **No completed validation study exists at this release, so no
record produced under v1.2.0 can conformantly carry a tier.** No proficiency
band or score interpretation is validated. Tier identifiers issued outside the
gate are not SLPT-conformant credentials.

**Q: How does an employer verify a credential?**

A: **Employment, hiring and selection use is not authorized** (§11), and the
prohibition is recorded in every record. Cross-institutional comparison is also
a non-permitted use, because weighting configurations differ by institution.
Verification tooling exists for institutional partners, but it establishes the
provenance of a record, not the meaning of an estimate.

**Q: Do estimates expire?**

A: Estimate windows are configurable. **This is a data-recency setting, not a
statement that an estimate was valid within the window and ceases to be
afterwards** — no interpretation of an estimate is validated at this release,
so there is no validity to expire. Windows also do not make estimates
comparable across scoring-model versions; see §9.4.

**Q: Can a credential be revoked?**

A: Institutional co-signatures can be withdrawn if the institution determines
that events did not occur within its governed environment; see §10. Separately,
**where a learner's dispute is upheld, §12.4.4 and schema rule R6 require the
record itself to be marked corrected or invalidated** — a reassessment is not a
correction.

**Q: What if a learner's behaviour changes over time?**

A: Recorded features reflect behaviour within the configured window, and
Adaptability is defined across episodes rather than within one. **The record
does not track capability**: no interpretation of an estimate as capability is
validated, and change in an estimate across scoring-model versions may reflect
scorer drift rather than the learner (§9.4).

---

## About governance

**Q: Who can change the specification?**

A: The SLPT Governance Council. Initial composition is convened by Answer
Labs Inc. Target composition over 24 months includes universities, enterprise
employers, independent researchers, representatives from platforms
implementing SLPT, and a learner advocate. See §12 of the specification.

**Q: What comes after v1.2?**

A: The interoperability adapters — xAPI, CLR / Open Badges, Common Cartridge,
CTDL, European Learning Model — remain roadmap, together with multi-implementation
exchange testing, which is what an interoperability claim would require. Timing
follows Council ratification under §12.2; no date is committed.

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
