# Findings and what I would check next

These are descriptive findings from the historical UCI diabetic hospital-encounter dataset (1999–2008). They are not predictions or clinical recommendations.

## 1. Readmission categories

| Recorded outcome | Encounters | Share of all encounters |
|---|---:|---:|
| Readmitted within 30 days (`<30`) | 11,357 | 11.16% |
| Readmitted after 30 days (`>30`) | 35,545 | 34.93% |
| No recorded readmission (`NO`) | 54,864 | 53.91% |

**What it tells me:** The under-30-day label is a smaller share of encounters than the other two categories, but it is the group relevant to this project's main business question.

## 2. Comparing age groups

The 20–30 age band contains 1,657 encounters, of which 236 carry the `<30` label (**14.24%**). In the 0–10 band, only 3 of 161 encounters have that label (**1.86%**).

**What I'd check next:** Group size, repeat encounters and other characteristics before trying to interpret differences between age bands. These raw percentages alone cannot establish why a patient was readmitted.

## 3. Data quality is part of the analysis

The source contains missing values in:
- Weight: **96.86%**
- Medical specialty: **49.08%**
- Payer code: **39.56%**
- Race: **2.23%**

**What I'd check next:** Which questions can reliably be answered without those fields, and whether charts using payer or specialty information clearly show how missing records are handled.

## 4. How I would use these findings in an operations discussion

I would present the readmission breakdown and subgroup counts first, then ask a healthcare operations or quality team which additional information would be needed to review discharge follow-ups or repeat hospital use. That would be a **proposal for further investigation**, not a claim that I improved hospital performance.

## Limits of this coursework

- The dataset covers **1999–2008**, not current hospital operations.
- One row represents an encounter; there are multiple encounters for some patients.
- No predictive model, clinical validation or real hospital workflow was implemented.
- The course BRD included hypothetical accuracy, reporting-efficiency and ROI targets. They were **not** measured achievements.
- Original coursework is evidenced by screenshots; extra reproducibility scripts were prepared later for the portfolio.
