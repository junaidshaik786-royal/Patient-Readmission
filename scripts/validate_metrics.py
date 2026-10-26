#!/usr/bin/env python3
"""Recalculate aggregate readmission metrics from the UCI source CSV.

This is a reproducibility companion written for the portfolio, not the
original coursework script. It prints aggregate results only; it does not
export encounter-level rows.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

EXPECTED_SOURCE_SHA256 = (
    "0689e7ec031237dc63031b938805c48377748761a3b26acab621567afa24df97"
)
REQUIRED_COLUMNS = {
    "encounter_id",
    "patient_nbr",
    "age",
    "readmitted",
    "time_in_hospital",
    "num_medications",
    "num_lab_procedures",
}
AUDITED_FIELDS = ("weight", "medical_specialty", "payer_code", "race", "diag_1")


def summarize_csv(filename: str | Path) -> dict[str, Any]:
    """Read a source CSV and return aggregate KPIs plus data-quality checks."""
    path = Path(filename)
    if not path.is_file():
        raise FileNotFoundError(f"CSV file not found: {path}")

    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    outcomes: Counter[str] = Counter()
    age_counts: dict[str, Counter[str]] = defaultdict(Counter)
    missing: Counter[str] = Counter()
    patient_ids: set[str] = set()
    encounters = total_stay = total_medications = total_lab_procedures = 0

    with path.open("r", newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        columns = set(reader.fieldnames or [])
        absent = sorted(REQUIRED_COLUMNS - columns)
        if absent:
            raise ValueError("Missing required columns: " + ", ".join(absent))

        for line_number, row in enumerate(reader, start=2):
            if not row or not any(value not in (None, "") for value in row.values()):
                continue

            encounters += 1
            patient_id = (row.get("patient_nbr") or "").strip()
            if patient_id:
                patient_ids.add(patient_id)

            outcome = (row.get("readmitted") or "").strip()
            outcomes[outcome] += 1

            age_band = (row.get("age") or "Unknown").strip() or "Unknown"
            age_counts[age_band]["encounters"] += 1
            if outcome == "<30":
                age_counts[age_band]["readmitted_lt30"] += 1

            try:
                total_stay += int(row["time_in_hospital"])
                total_medications += int(row["num_medications"])
                total_lab_procedures += int(row["num_lab_procedures"])
            except (TypeError, ValueError) as exc:
                raise ValueError(
                    f"Invalid numeric value on CSV line {line_number}: {exc}"
                ) from exc

            for field in AUDITED_FIELDS:
                value = (row.get(field) or "").strip()
                if value in ("", "?"):
                    missing[field] += 1

    if encounters == 0:
        raise ValueError("CSV contains a header but no data rows")

    age_summary = {
        age: {
            "encounters": counts["encounters"],
            "readmitted_lt30": counts["readmitted_lt30"],
            "readmitted_lt30_percent": round(
                100 * counts["readmitted_lt30"] / counts["encounters"], 2
            ),
        }
        for age, counts in sorted(age_counts.items())
    }

    return {
        "file_sha256": digest,
        "matches_reviewed_source": digest == EXPECTED_SOURCE_SHA256,
        "encounters": encounters,
        "unique_patients": len(patient_ids),
        "readmitted_lt30": outcomes["<30"],
        "readmitted_gt30": outcomes[">30"],
        "readmitted_no": outcomes["NO"],
        "readmission_30_encounter_percent": round(
            100 * outcomes["<30"] / encounters, 2
        ),
        "mean_hospital_days": round(total_stay / encounters, 2),
        "mean_medications": round(total_medications / encounters, 2),
        "mean_lab_procedures": round(total_lab_procedures / encounters, 2),
        "missingness_percent": {
            field: round(100 * missing[field] / encounters, 2)
            for field in AUDITED_FIELDS
        },
        "age_band": age_summary,
        "disclosure": (
            "Descriptive encounter-level metrics from historical UCI data "
            "(1999–2008); not a validated clinical prediction."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print(
            "Usage: python scripts/validate_metrics.py /path/to/diabetic_data.csv",
            file=sys.stderr,
        )
        return 2

    try:
        result = summarize_csv(args[0])
    except (OSError, ValueError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
