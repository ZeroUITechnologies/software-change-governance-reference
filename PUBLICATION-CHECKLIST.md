# Publication and follow-up checklist

This is an operational record for release `v0.1.0`. Checked items were
verified in the prepared repository package. Unchecked items are explicit
owner or platform follow-ups; their presence does not state that this package
is unpublished or that the licensing decision remains open.

## 1. Repository identity and licensing — completed

- [x] Repository: `ZeroUITechnologies/software-change-governance-reference`.
- [x] Publisher and copyright holder: `ZeroUI Technologies LLP`.
- [x] Apache-2.0 applies to schema, example, validation, requirements, and workflow files.
- [x] CC-BY-4.0 applies to prose, citation/release metadata, and control-matrix data.
- [x] Full official license texts and machine-readable SPDX file scopes are included.
- [x] Attribution, `NOTICE`, and trademark-reservation language are included.
- [x] DCO 1.1 sign-off is the inbound contribution model.
- [x] `README.md`, `CONTRIBUTING.md`, `CITATION.cff`, and release metadata agree with the licensing decision.
- [x] `LICENSE-DECISION-REQUIRED.md` is retained as a closed resolution record so earlier links do not break.

## 2. Artifact and claims verification — completed

- [x] The control-matrix JSON and CSV representations contain the same twelve rows and values.
- [x] The DER schema is valid JSON Schema Draft 2020-12.
- [x] The synthetic DER example validates against the schema.
- [x] The example is explicitly synthetic and contains no real customer, credential, personal, or production data.
- [x] The final example record occurs after its illustrative deployment event.
- [x] “Public reference draft,” “ZeroUI-defined,” and scope limitations remain explicit.
- [x] No standards certification, compliance proof, customer result, integration, benchmark, or endorsement is claimed.
- [x] The repository language is consistent with the current ZeroUI product description.

## 3. Release verification — completed

- [x] `python scripts/validate.py --require-jsonschema` passes in an isolated dependency environment.
- [x] Repository JSON files parse and `CITATION.cff` plus GitHub YAML files parse.
- [x] Repository and website copies of the matrix JSON, matrix CSV, DER schema, and DER example are byte-identical.
- [x] The schema `$id` resolves to bytes matching the repository schema.
- [x] Full Apache-2.0 and CC-BY-4.0 texts match their official sources byte-for-byte.
- [x] Release notes link directly to versioned artifacts.
- [x] SHA-256 checksums are recorded in the root `SHA256SUMS` file.
- [x] CI actions and the validation dependency are pinned to exact reviewed versions.
- [x] REUSE metadata covers every repository file and `reuse lint` passes.

## 4. Publication-time platform setup — owner follow-up

- [ ] Enable branch protection and require validation plus review on the default branch.
- [ ] Enable and test GitHub private vulnerability reporting; `SECURITY.md` links to the private report form.
- [ ] Decide whether GitHub issues, discussions, and pull requests are enabled at launch.
- [ ] Decide whether releases must be signed or otherwise authenticated.
- [ ] Assign a primary maintainer and a backup maintainer.
- [x] Assign `@ZeroUITechnologies`, the confirmed authenticated publisher account, as the default code owner.
- [ ] Define issue labels, triage ownership, response expectations, and release authority if community features are enabled.
- [ ] Add a code of conduct if active community participation is invited.

## 5. Owner and legal review follow-ups

- [ ] Retain private evidence of ownership or assignments for every included file.
- [ ] Record the authorized internal claims approver and approval evidence privately.
- [ ] Reconfirm third-party reference descriptions and rights before each release.
- [ ] Obtain legal review if the project scope, license allocation, trademark policy, or contribution model changes.

## 6. Discoverability and post-publication follow-ups

- [ ] Confirm the live website, `llms.txt`, AI content index, sitemap, and structured data link to the published repository and release.
- [ ] Consider an immutable archive and DOI; add it to `CITATION.cff` without replacing canonical URLs.
- [ ] Publish an illustrative incident-to-policy-to-DER walkthrough without implying a customer deployment.
- [ ] Schedule a 30-day review of issues, citations, implementation questions, and ambiguous terms.
- [ ] Publish corrections transparently in `CHANGELOG.md`.
- [ ] Keep released version directories resolvable and do not rewrite semantic content in place.

