# Dataset Provenance and Reproducibility

**Primary source:** [UCI Diabetes 130-US Hospitals for Years 1999–2008](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008)

**DOI:** https://doi.org/10.24432/C5230J

**Attribution:** Clore, J., Cios, K., DeShazo, J., & Strack, B. (2014). *Diabetes 130-US Hospitals for Years 1999–2008*, UCI Machine Learning Repository.

## Reviewed source
- Input file: diabetic_data.csv
- Size: 19,159,383 bytes
- SHA-256: 0689e7ec031237dc63031b938805c48377748761a3b26acab621567afa24df97
- Rows: 101,766
- Columns: 50
- Distinct patient IDs: 71,518

## Important fields
- encounter_id: identifier for an encounter.
- patient_nbr: identifier for a patient, may appear in multiple rows.
- readmitted: NO, >30 or <30.
- age: pre-grouped age bands; not exact ages.
- time_in_hospital: inpatient stay in days.
- num_medications, num_lab_procedures: counts recorded during an encounter.
- weight, payer_code and medical_specialty: contain substantial missingness encoded as '?'.

## Reproduce
Download the original CSV from the UCI source and run:

    python scripts/validate_metrics.py /path/to/diabetic_data.csv

The script prints headline metrics, age-band outputs and a SHA-256 match flag using only standard-library Python. For MySQL, see [SQL README](../sql/README.md).

## Scope, ethics and credit
These are historical U.S. hospital encounter records from 1999–2008. Their characteristics and collection methods may not represent present-day healthcare. Public project outputs are aggregates; the raw patient-level CSV is not republished. The project does not use hospital clients, real stakeholders or production clinical records.
