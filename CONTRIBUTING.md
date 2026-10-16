# Contributing

This repository accepts narrowly scoped proposals that improve clarity,
interoperability, safety, or implementation usefulness without overstating the
status of the artifacts. Opening an issue does not require a contribution
sign-off. Every commit submitted for inclusion does.

## Proposed contribution workflow

1. Open an issue describing the problem, affected artifact version, intended users, and compatibility impact.
2. For semantic changes, include at least one concrete example and explain how existing consumers should migrate.
3. Keep pull requests focused on one issue.
4. Run `python scripts/validate.py --require-jsonschema` before requesting review.
5. Update the changelog when behavior, vocabulary, identifiers, or interpretation changes.

## Developer Certificate of Origin

All commits must include a `Signed-off-by` line certifying the Developer
Certificate of Origin 1.1 in [`DCO`](DCO). Add it with:

```sh
git commit -s
```

The sign-off must use a name and email address that identify the contributor:

```text
Signed-off-by: Contributor Name <contributor@example.com>
```

By submitting a contribution, you agree that it may be distributed under the
license applicable to the file being changed:

- `Apache-2.0` for schema, example, validation, requirements, and workflow files;
- `CC-BY-4.0` for prose, citation/release metadata, and control-matrix data.

See [`LICENSE`](LICENSE) for the controlling file scopes. A pull request that
mixes both classes of files applies the appropriate license to each file; it
does not relicense the repository as a whole.

## Artifact-specific requirements

### Control matrix

- Treat JSON as the canonical structured representation.
- Update CSV in the same change and keep values byte-for-byte equivalent after CSV parsing.
- Do not reuse or silently redefine an existing control identifier.
- Identify whether a proposal adds a control, narrows a control, broadens a control, or changes only wording.
- Do not assert a mapping to an external standard without documented methodology, primary-source references, and explicit maintainer approval.

### Decision Evidence Record

- Keep the schema valid against JSON Schema Draft 2020-12.
- Add or update synthetic examples for every semantic change.
- Classify compatibility according to [`docs/versioning.md`](docs/versioning.md).
- Never put real credentials, source code, prompts, personal data, customer data, production identifiers, or confidential evidence in an example.
- Prefer references, digests, and controlled identifiers over embedded sensitive content.

## Evidence and claims

Every factual statement about an external framework, product, organization, or specification should cite a primary source. A citation provides context; it does not imply endorsement, validation, equivalence, or formal alignment.

Do not submit:

- invented customers, testimonials, integrations, certifications, metrics, or benchmarks;
- confidential or personally identifiable information;
- claims that these drafts are industry standards;
- claims that a complete DER proves compliance or control effectiveness; or
- third-party material that the contributor lacks the right to submit.

## Maintainer review

Before merging a change, maintainers should obtain the review appropriate to
its scope, including:

- an artifact maintainer for semantic consistency;
- a security reviewer for evidence-handling guidance;
- a legal approver for licensing and third-party rights; and
- a final claims reviewer for release notes and public descriptions; and
- confirmation that every commit carries a valid DCO sign-off.

