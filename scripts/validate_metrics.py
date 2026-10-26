#!/usr/bin/env python3
"""Independent verification companion for the UCI patient readmission dataset."""
import csv, hashlib, json, sys
from collections import Counter, defaultdict
from pathlib import Path
EXPECTED_SHA256 = "0689e7ec031237dc63031b938805c48377748761a3b26acab621567afa24df97"
def validate(filename):
    path=Path(filename)
    sha=hashlib.sha256(path.read_bytes()).hexdigest()
    counts=Counter(); missing=Counter(); patients=set(); age=defaultdict(Counter)
    n=days=medications=labs=0
    with path.open(encoding="utf-8-sig",newline="") as f:
        rows=csv.DictReader(f)
        for r in rows:
            n+=1; patients.add(r["patient_nbr"]); counts[r["readmitted"]]+=1
            age[r["age"]]["encounters"]+=1
            if r["readmitted"]=="<30":age[r["age"]]["lt30"]+=1
            days+=int(r["time_in_hospital"]); medications+=int(r["num_medications"])
            labs+=int(r["num_lab_procedures"])
            for k in ("weight","medical_specialty","payer_code","race","diag_1"):
                if r[k] in ("?",""):missing[k]+=1
    if n==0: raise ValueError("Empty CSV")
    result={"sha256":sha,"matches_reviewed_dataset":sha==EXPECTED_SHA256,
      "encounters":n,"unique_patients":len(patients),
      "readmitted_lt30":counts["<30"],"readmitted_gt30":counts[">30"],"readmitted_no":counts["NO"],
      "early_readmission_encounter_percent":round(100*counts["<30"]/n,2),
      "mean_hospital_days":round(days/n,2),"mean_medications":round(medications/n,2),
      "mean_lab_procedures":round(labs/n,2),
      "missingness_percent":{k:round(v*100/n,2) for k,v in missing.items()},
      "age_bands":{k:{"encounters":v["encounters"],"lt30":v["lt30"],
      "lt30_percent":round(100*v["lt30"]/v["encounters"],2)} for k,v in sorted(age.items())}}
    print(json.dumps(result,indent=2))
if __name__=="__main__":
    if len(sys.argv)!=2:raise SystemExit("Usage: python scripts/validate_metrics.py /path/to/diabetic_data.csv")
    validate(sys.argv[1])
