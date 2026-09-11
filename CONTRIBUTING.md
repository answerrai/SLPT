# Contributing to SLPT

The Standard Learning Provenance Taxonomy is an open specification maintained
by Answer Labs Inc. This document explains how to contribute.

---

## What you can contribute today

- **Specification clarifications.** If something in the specification is
  ambiguous, contradictory, or difficult to interpret — file an issue
  describing the problem and where it appears in the document.

- **Documentation improvements.** Typos, broken links, unclear wording,
  or missing information in the implementer guide or FAQ.

- **Independent scorer implementations.** If you build your own scorer against
  the four first-order dimensions and the candidate Judgment Quality composite,
  using the published specification and schema, file an issue tagged
  `independent-implementation` and we will link to it from the README.

- **Conformance fixtures.** Cases the 71-fixture corpus does not cover,
  especially omitted-property cases for the cross-field rules. R3 shipped
  unenforced for an omitted `task_frame` because its only negative fixture set
  the value to null; `rule_probe.py` now checks for that class.

---

## What is coming

The schema, conformance harness and OpenAPI contract are published in this
release. The interoperability adapters — xAPI, CLR / Open Badges, Common
Cartridge, CTDL, European Learning Model — remain roadmap. Contributions are
welcome on adapter implementations, language ports, conformance fixtures and
tooling. This document is updated at each release.

---

## Process

1. Open an issue describing what you found or what you want to contribute.
2. Wait for a maintainer to respond and confirm scope.
3. Fork the repository and make your change in a feature branch.
4. Open a pull request referencing the issue.

Specification changes require Governance Council review per §12 of the
specification. Major changes require a 75% Council supermajority.

---

## Markdown style

- Use `-` for bullet lists, not `*`
- One blank line between every paragraph and heading
- Use backticks for file names and technical terms

---

## License

By contributing, you agree that your contributions will be licensed under
Apache License 2.0 for software and CC BY 4.0 for specification text,
matching the rest of the repository.

---

## Code of conduct

See `CODE_OF_CONDUCT.md`. Be respectful, focus on technical merits, and
assume good faith.

---

## Questions

For specification questions, institutional partnerships, API access, or general
enquiries, contact **tech@answerr.ai**
