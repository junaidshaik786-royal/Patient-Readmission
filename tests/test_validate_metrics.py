import csv
import tempfile
import unittest
from pathlib import Path

from scripts.validate_metrics import summarize_csv


FIELDS = [
    "encounter_id", "patient_nbr", "age", "readmitted",
    "time_in_hospital", "num_medications", "num_lab_procedures",
    "weight", "medical_specialty", "payer_code", "race", "diag_1",
]


class SummarizeCsvTests(unittest.TestCase):
    def write_csv(self, headers, rows):
        handle = tempfile.NamedTemporaryFile(
            mode="w", newline="", encoding="utf-8", delete=False
        )
        self.addCleanup(lambda: Path(handle.name).unlink(missing_ok=True))
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
        handle.close()
        return handle.name

    def test_calculates_encounter_level_metrics_and_missingness(self):
        rows = [
            {
                "encounter_id": "1", "patient_nbr": "10", "age": "[20-30)",
                "readmitted": "<30", "time_in_hospital": "2",
                "num_medications": "5", "num_lab_procedures": "20",
                "weight": "?", "medical_specialty": "Cardiology",
                "payer_code": "?", "race": "Caucasian", "diag_1": "250.83",
            },
            {
                "encounter_id": "2", "patient_nbr": "10", "age": "[20-30)",
                "readmitted": ">30", "time_in_hospital": "4",
                "num_medications": "7", "num_lab_procedures": "30",
                "weight": "", "medical_specialty": "?", "payer_code": "MC",
                "race": "?", "diag_1": "250.83",
            },
            {
                "encounter_id": "3", "patient_nbr": "20", "age": "[30-40)",
                "readmitted": "NO", "time_in_hospital": "6",
                "num_medications": "9", "num_lab_procedures": "40",
                "weight": "?", "medical_specialty": "?",
                "payer_code": "?", "race": "AfricanAmerican", "diag_1": "428",
            },
        ]
        result = summarize_csv(self.write_csv(FIELDS, rows))

        self.assertEqual(result["encounters"], 3)
        self.assertEqual(result["unique_patients"], 2)
        self.assertEqual(result["readmitted_lt30"], 1)
        self.assertEqual(result["readmitted_gt30"], 1)
        self.assertEqual(result["readmitted_no"], 1)
        self.assertEqual(result["readmission_30_encounter_percent"], 33.33)
        self.assertEqual(result["mean_hospital_days"], 4.0)
        self.assertEqual(result["mean_medications"], 7.0)
        self.assertEqual(result["mean_lab_procedures"], 30.0)
        self.assertEqual(result["missingness_percent"]["weight"], 100.0)
        self.assertEqual(result["missingness_percent"]["medical_specialty"], 66.67)
        self.assertEqual(result["age_band"]["[20-30)"]["encounters"], 2)
        self.assertEqual(result["age_band"]["[20-30)"]["readmitted_lt30_percent"], 50.0)
        self.assertFalse(result["matches_reviewed_source"])

    def test_rejects_missing_required_columns(self):
        path = self.write_csv(["patient_nbr"], [{"patient_nbr": "1"}])
        with self.assertRaisesRegex(ValueError, "Missing required columns"):
            summarize_csv(path)

    def test_rejects_header_only_file(self):
        path = self.write_csv(FIELDS, [])
        with self.assertRaisesRegex(ValueError, "no data rows"):
            summarize_csv(path)


if __name__ == "__main__":
    unittest.main()
