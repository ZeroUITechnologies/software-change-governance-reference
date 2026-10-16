#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 ZeroUI Technologies LLP
# SPDX-License-Identifier: Apache-2.0
"""Validate the ZeroUI v0.1 reference artifacts and their cross-format parity."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MATRIX_JSON = ROOT / "control-matrix" / "v0.1" / "control-matrix.json"
MATRIX_CSV = ROOT / "control-matrix" / "v0.1" / "control-matrix.csv"
DER_SCHEMA = ROOT / "decision-evidence-record" / "v0.1" / "schema.json"
DER_EXAMPLE = ROOT / "decision-evidence-record" / "v0.1" / "examples" / "complete.json"
CONTROL_FIELDS = [
    "id",
    "control",
    "stage",
    "risk",
    "actor",
    "decision",
    "evidence",
    "owner",
    "remediation",
    "recheck",
]
CONTROL_ID = re.compile(r"^SCG-[A-Z]{2}-[0-9]{2}$")
DER_OUTCOMES = [
    "guide",
    "allow",
    "warn",
    "hold_for_review",
    "block",
    "correct",
    "recheck",
    "record_evidence",
    "route_for_approval",
]
DECISION_FIELD_NOTE = (
    "Control-level decision values are descriptive workflow actions, not an enumeration "
    "constrained to Decision Evidence Record outcome codes."
)


class ValidationFailure(Exception):
    """Raised for a repository invariant failure."""


def load_json(path: Path) -> Any:
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationFailure(f"{path.relative_to(ROOT)}: {exc}") from exc


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationFailure(message)


def parse_datetime(value: Any, field: str) -> datetime:
    require(isinstance(value, str), f"{field} must be an ISO 8601 string")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        return datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValidationFailure(f"{field} is not a parseable ISO 8601 date-time") from exc


def validate_matrix() -> None:
    matrix = load_json(MATRIX_JSON)
    require(matrix.get("version") == "0.1", "matrix version must remain 0.1")
    require(
        matrix.get("status") == "public reference draft",
        "matrix status must explicitly remain 'public reference draft'",
    )
    require(
        "outcome_vocabulary" not in matrix,
        "ambiguous outcome_vocabulary key must not be reintroduced",
    )
    require(
        matrix.get("decision_evidence_outcome_vocabulary") == DER_OUTCOMES,
        "matrix must retain the Decision Evidence Record outcome vocabulary",
    )
    require(
        matrix.get("decision_field_note") == DECISION_FIELD_NOTE,
        "matrix must distinguish descriptive control decisions from DER outcome codes",
    )
    controls = matrix.get("controls")
    require(isinstance(controls, list), "matrix controls must be an array")
    require(len(controls) == 12, "v0.1 matrix must contain exactly 12 controls")

    identifiers: list[str] = []
    normalized_json: list[dict[str, str]] = []
    for index, control in enumerate(controls, start=1):
        require(isinstance(control, dict), f"matrix control {index} must be an object")
        missing = [field for field in CONTROL_FIELDS if not control.get(field)]
        require(not missing, f"matrix control {index} has empty fields: {', '.join(missing)}")
        extra = sorted(set(control) - set(CONTROL_FIELDS))
        require(not extra, f"matrix control {index} has unexpected fields: {', '.join(extra)}")
        identifier = control["id"]
        require(bool(CONTROL_ID.fullmatch(identifier)), f"invalid control id: {identifier}")
        identifiers.append(identifier)
        normalized_json.append({field: str(control[field]) for field in CONTROL_FIELDS})

    require(len(set(identifiers)) == len(identifiers), "matrix control ids must be unique")

    try:
        with MATRIX_CSV.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            require(reader.fieldnames == CONTROL_FIELDS, "CSV columns or order differ from v0.1")
            normalized_csv = [dict(row) for row in reader]
    except OSError as exc:
        raise ValidationFailure(f"{MATRIX_CSV.relative_to(ROOT)}: {exc}") from exc

    require(
        normalized_csv == normalized_json,
        "CSV controls must match JSON controls exactly, including order",
    )


def validate_der(require_jsonschema: bool) -> bool:
    schema = load_json(DER_SCHEMA)
    example = load_json(DER_EXAMPLE)

    require(
        schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema",
        "DER schema must declare JSON Schema Draft 2020-12",
    )
    require(
        schema.get("$id")
        == "https://www.zeroui.dev/schemas/decision-evidence-record-v0.1.schema.json",
        "DER schema $id changed without a version change",
    )
    require(
        schema.get("properties", {}).get("schema_version", {}).get("const") == "0.1",
        "DER schema_version const must remain 0.1",
    )
    require(example.get("schema_version") == "0.1", "example must identify schema version 0.1")
    require(
        example.get("extensions", {}).get("example_only") is True,
        "example must remain explicitly marked as synthetic example data",
    )
    policies = example.get("policies", [])
    require(
        all(
            isinstance(policy, dict)
            and isinstance(policy.get("id"), str)
            and not CONTROL_ID.fullmatch(policy["id"])
            for policy in policies
        ),
        "example policy ids must be synthetic organization policies, not matrix control ids",
    )

    release = example.get("release")
    if example.get("status") == "final" and isinstance(release, dict) and release.get("deployed_at"):
        require(
            parse_datetime(example.get("recorded_at"), "example.recorded_at")
            >= parse_datetime(release.get("deployed_at"), "example.release.deployed_at"),
            "a final DER example must not be recorded before its deployment event",
        )

    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ModuleNotFoundError as exc:
        if require_jsonschema:
            raise ValidationFailure(
                "jsonschema is required; run: python -m pip install -r requirements-dev.txt"
            ) from exc
        return False

    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(example), key=lambda error: list(error.path))
    if errors:
        details = []
        for error in errors:
            location = ".".join(str(item) for item in error.absolute_path) or "<root>"
            details.append(f"{location}: {error.message}")
        raise ValidationFailure("DER example failed schema validation:\n- " + "\n- ".join(details))
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--require-jsonschema",
        action="store_true",
        help="fail if the jsonschema package is unavailable (required in CI)",
    )
    args = parser.parse_args()

    try:
        validate_matrix()
        full_schema_validation = validate_der(args.require_jsonschema)
    except ValidationFailure as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        return 1

    print("matrix: JSON/CSV parity, ids, fields, version, and status are valid")
    if full_schema_validation:
        print("DER: schema is valid and the synthetic example conforms")
    else:
        print("DER: structural invariants passed; install requirements-dev.txt for full schema validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

