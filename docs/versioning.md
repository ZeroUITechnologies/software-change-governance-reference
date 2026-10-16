# Versioning and compatibility

The control matrix and Decision Evidence Record are versioned artifacts. Versioned directories are immutable after a release except for clearly non-semantic corrections. A changed interpretation receives a new artifact version.

## Version format

During the draft period, versions use `major.minor` labels such as `0.1` and `0.2`.

- A **minor draft version** may contain breaking changes while the major version is `0`.
- Version `1.0` should be considered only after public review, implementation
  feedback, stable terminology, and an explicit compatibility policy.

Repository release tags may use a patch component for packaging-only corrections, for example `v0.1.1`, while the embedded artifact version remains `0.1`. A packaging release must not change artifact semantics.

## Breaking changes

The following require a new artifact-version directory:

- removing or renaming a required DER field;
- changing the meaning or allowed values of a field;
- tightening a constraint so a previously valid record becomes invalid;
- changing a matrix control identifier or its normative meaning;
- splitting or combining controls in a way that changes implementation expectations; or
- changing the declared JSON Schema dialect.

## Additive changes

An optional field can still be semantically breaking if consumers are expected to interpret it. During the `0.x` period, additive semantic changes should therefore receive a new artifact version rather than modifying the released schema in place.

## Non-semantic corrections

Spelling, formatting, link repair, or an example correction may be applied in a packaging patch only when it cannot alter a reasonable implementation's interpretation. Record the correction in `CHANGELOG.md` and preserve the prior release in repository history.

## Canonical locations

The current website schema identifier is:

`https://www.zeroui.dev/schemas/decision-evidence-record-v0.1.schema.json`

Keep that identifier resolvable after a GitHub repository is published. If a GitHub raw URL or archive DOI is added, treat it as an additional distribution location, not a silent replacement for the schema `$id`.

## Consumer guidance

- Pin to an explicit artifact version.
- Preserve unknown values or extensions only where the schema permits them.
- Do not infer compatibility from repository tags alone.
- Validate records before processing them.
- Record the schema version and the policy versions used in every final decision record.

