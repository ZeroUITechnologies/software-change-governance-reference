# Claims and scope

This document is the release-time boundary for public descriptions of the repository.

## What may be said

- The Software Change Governance Control Matrix and Decision Evidence Record are **ZeroUI-defined public reference drafts**.
- The matrix organizes twelve tool-neutral governance concerns across the software-change lifecycle.
- The DER schema is designed to record decision context, policy versions, supporting evidence, rationale, outcome, accountability, remediation, re-check, and release context.
- The artifacts can be inspected, discussed, reused, and evaluated by
  implementers under the file-specific terms in [`../LICENSE`](../LICENSE).
- ZeroUI is building a software change governance control plane. Current product scope and validated capabilities must be confirmed directly with ZeroUI.

## What must not be said without new evidence and approval

- that either artifact is an industry, consensus, de jure, or de facto standard;
- that an independent standards body, regulator, customer, analyst, or listed source endorses ZeroUI;
- that the controls are formally mapped to NIST, CISA, ISO, SOC 2, PCI DSS, OWASP, or another framework;
- that producing a complete DER proves compliance, control effectiveness, software safety, audit readiness, or non-repudiation;
- that the schema is validated for every storage, privacy, evidentiary, cryptographic, regulatory, or jurisdictional requirement;
- that ZeroUI has implemented every field, control, workflow, or integration represented here;
- that fictional examples describe customer deployments or production results; or
- that the entire mixed-license repository is governed by a single license.

## Intended scope

The artifacts focus on governance of a software change from proposal through production learning. They model questions such as:

- who or what is acting and under whose authority;
- whether the action is within approved scope;
- which approved organizational intent applies;
- what validation, review, recovery, and release conditions apply;
- what evidence supports the decision;
- who remains accountable;
- how remediation and re-check are recorded; and
- how production observations can propose—but never silently enact—policy change.

## Out of scope in v0.1

Version 0.1 does not define:

- a policy language or evaluation engine;
- an authorization protocol;
- a cryptographic signing or transparency-log profile;
- evidence retention, residency, privacy, redaction, or disclosure requirements;
- a universal risk-scoring system;
- a conformance test suite or certification program;
- mappings to external frameworks;
- transport, storage, query, or API protocols;
- the operational semantics of a specific ZeroUI product release; or
- legal or regulatory advice.

## Evidence-handling warning

A real decision record can point to sensitive material. Implementations should use controlled references and integrity-protected digests instead of embedding secrets, source code, prompts, personal data, proprietary evidence, or credentials. Access control, retention, redaction, privacy, audit logging, and correction procedures are implementation responsibilities outside the v0.1 schema.

## Review checklist for any new claim

Before merging a new public claim, record:

1. whether it describes this conceptual artifact or a shipping product;
2. the evidence supporting it;
3. the primary source for any external fact;
4. whether the wording implies endorsement, certification, formal mapping, or validation;
5. who approved the wording; and
6. when the claim should be rechecked.

