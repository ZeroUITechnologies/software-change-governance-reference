# ZeroUI Software Change Governance Reference

Canonical repository: [ZeroUITechnologies/software-change-governance-reference](https://github.com/ZeroUITechnologies/software-change-governance-reference)

This repository package contains two versioned, machine-readable ZeroUI reference artifacts:

1. the **Software Change Governance Control Matrix v0.1**, a tool-neutral set of twelve controls spanning actor identity through production learning; and
2. the **Decision Evidence Record (DER) v0.1**, a JSON Schema for recording the context, policy, evidence, rationale, outcome, accountability, remediation, re-check, and release context associated with a governed software change decision.

The artifacts are intended to make ZeroUI's software change governance model inspectable and discussable. They are public reference drafts—not independent standards, compliance certifications, or evidence that ZeroUI has implemented or validated every represented capability.

## Repository contents

| Path | Purpose |
| --- | --- |
| [`control-matrix/v0.1/control-matrix.json`](control-matrix/v0.1/control-matrix.json) | Canonical structured control matrix for this repository version |
| [`control-matrix/v0.1/control-matrix.csv`](control-matrix/v0.1/control-matrix.csv) | Tabular export of the same twelve controls |
| [`decision-evidence-record/v0.1/schema.json`](decision-evidence-record/v0.1/schema.json) | Draft 2020-12 JSON Schema for a Decision Evidence Record |
| [`decision-evidence-record/v0.1/examples/complete.json`](decision-evidence-record/v0.1/examples/complete.json) | Synthetic, non-customer example that satisfies the v0.1 schema |
| [`docs/claims-and-scope.md`](docs/claims-and-scope.md) | What the artifacts do and do not claim |
| [`docs/references.md`](docs/references.md) | Primary external context; no standards mapping or endorsement is implied |
| [`docs/versioning.md`](docs/versioning.md) | Versioning and compatibility policy for the drafts |
| [`scripts/validate.py`](scripts/validate.py) | Consistency and schema validation |

## Control matrix

Each control has a stable v0.1 identifier and describes:

- the lifecycle stage where it applies;
- the risk it addresses;
- relevant actor classes;
- possible governance decisions;
- evidence needed to reconstruct the decision;
- accountable ownership;
- remediation; and
- re-check expectations.

The matrix's row-level `decision` text describes workflow actions for each
control. It is intentionally distinct from the named Decision Evidence Record
outcome enumeration stored in `decision_evidence_outcome_vocabulary`.

The identifiers are namespace labels for this ZeroUI draft. They are not control identifiers from NIST, CISA, ISO, SOC 2, or another external framework. No formal mapping is asserted.

## Decision Evidence Record

The DER is designed as a portable decision receipt. The schema deliberately separates:

- the actor from the accountable owner;
- the changed artifact from the evidence used to evaluate it;
- policy evaluation from approval;
- an initial outcome from remediation and re-check; and
- a change decision from the later release event.

The example is fictional and uses placeholder identifiers and digests. It is not a customer record, benchmark, production result, or attestation.

## Validate the artifacts

Python 3.10 or later is recommended.

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py --require-jsonschema
sha256sum --check SHA256SUMS
```

The validator checks that:

- JSON files parse;
- matrix control identifiers are unique;
- the JSON and CSV matrix exports contain the same rows and values;
- the example validates against the DER schema; and
- expected version and draft-status fields remain explicit; and
- a final synthetic record does not predate its example deployment event.

The checksum command verifies that the four versioned release artifacts match
the digests recorded for `v0.1.0`.

## Versioning

The matrix and DER are versioned independently. Paths include the artifact version so a breaking revision can coexist with earlier drafts. See [`docs/versioning.md`](docs/versioning.md).

Version `0.1` is exploratory. Fields, enumerations, identifiers, and semantics may change in a later draft. Pin consumers to an explicit version and do not treat the unversioned repository default branch as a stable API.

## Citation

Repository citation metadata is provided in [`CITATION.cff`](CITATION.cff). The canonical web pages currently are:

- [Software Change Governance Control Matrix v0.1](https://www.zeroui.dev/software-change-governance/control-matrix/)
- [Decision Evidence Record v0.1](https://www.zeroui.dev/decision-evidence-record/)

The repository URL and release version are recorded in the citation metadata.
If an immutable archive DOI is created later, add it without replacing the
canonical web pages or repository URL.

## Release

The initial repository release is `v0.1.0`; the embedded artifact version is
`0.1`. See [`releases/v0.1.0.md`](releases/v0.1.0.md) for the prepared release
notes and [`CHANGELOG.md`](CHANGELOG.md) for change history.

## Product boundary

ZeroUI is building a software change governance control plane. Product behavior, availability, integrations, and validation status should be confirmed directly with ZeroUI. This reference repository must not be used to infer capabilities beyond statements on the official website or a separately executed agreement.

## License and contributions

This is a mixed-license repository:

- the DER schema, synthetic example, validation code, dependency manifest, and
  workflow automation are licensed under Apache License 2.0; and
- prose documentation, citation and release metadata, and control-matrix data
  are licensed under Creative Commons Attribution 4.0 International.

Exact file scopes, full license texts, attribution guidance, and trademark
terms are in [`LICENSE`](LICENSE), [`NOTICE`](NOTICE), and
[`TRADEMARKS.md`](TRADEMARKS.md).

Contributions must be signed off under the Developer Certificate of Origin
1.1 and are accepted under the license applicable to the contributed file.
See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`DCO`](DCO).

