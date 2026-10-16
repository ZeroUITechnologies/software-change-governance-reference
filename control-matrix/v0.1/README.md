# Software Change Governance Control Matrix v0.1

The matrix is a ZeroUI-defined, tool-neutral public reference draft. It organizes twelve governance concerns around a software change and connects each one to risk, lifecycle stage, actors, decisions, evidence, ownership, remediation, and re-check.

## Representations

- [`control-matrix.json`](control-matrix.json) is the canonical structured representation in this repository.
- [`control-matrix.csv`](control-matrix.csv) is an equivalent tabular export.

Validation fails if the parsed CSV and JSON controls differ.

## Decision language

The top-level `decision_evidence_outcome_vocabulary` lists the permitted
outcomes defined by the Decision Evidence Record schema. By contrast, each
matrix row's `decision` value is descriptive workflow language for that
control. Row values are not constrained to the DER outcome enumeration.

## Identifier policy

Identifiers such as `SCG-ID-01` are stable only within v0.1. They are not identifiers assigned by an external standards body. A future draft must not silently reuse an identifier for a different control meaning.

## Scope boundary

The matrix does not certify compliance, provide a formal mapping to an external framework, or prescribe a single technical implementation. Owners and decision vocabularies are reference-language starting points that an organization must adapt through its own accountable governance process.

## Canonical web page

[ZeroUI Software Change Governance Control Matrix](https://www.zeroui.dev/software-change-governance/control-matrix/)

## License

This README and the JSON and CSV matrix data are licensed under Creative
Commons Attribution 4.0 International. See [`../../LICENSE`](../../LICENSE)
for attribution and exact scope.

