# Decision Evidence Record v0.1

The ZeroUI Decision Evidence Record (DER) is an unvalidated public reference draft designed to make governed software-change decisions portable and reconstructable.

## Files

- [`schema.json`](schema.json) — JSON Schema Draft 2020-12 schema.
- [`examples/complete.json`](examples/complete.json) — complete, synthetic example.

The example's `ORG-*` policy identifiers are fictional organization policy
IDs. They are intentionally distinct from the control-matrix `SCG-*`
identifiers.

## Design intent

A record associates:

- actor and accountable owner;
- authorized scope;
- changed artifacts and artifact digests;
- evaluated policy identifiers and versions;
- evidence references and results;
- outcome and rationale;
- approval and accountability;
- remediation and re-check; and
- optional release context.

## Safety boundary

The schema permits references and digests but does not define access control, cryptographic signing, retention, redaction, privacy, residency, or legal admissibility. Implementations should avoid embedding secrets, source code, prompts, personal information, credentials, or confidential evidence.

A schema-valid record is not proof that a decision was correct, a control operated effectively, an approval was authorized, evidence is authentic, or an organization complies with any standard.

## Extensibility

Top-level properties are closed in v0.1. Organization-specific additions belong under `extensions`. Nested objects allow additional properties to support controlled local metadata. Consumers should namespace extension keys to reduce collisions.

## Canonical identifiers

- Schema `$id`: `https://www.zeroui.dev/schemas/decision-evidence-record-v0.1.schema.json`
- Reference page: [Decision Evidence Record v0.1](https://www.zeroui.dev/decision-evidence-record/)

## License

The schema and synthetic example are licensed under Apache License 2.0. This
README is licensed under Creative Commons Attribution 4.0 International. See
[`../../LICENSE`](../../LICENSE) for exact scope.

