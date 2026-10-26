# Lessons learned and next iteration

This is a reflection on the current portfolio artifact, not a claim about measured business impact.

## What I learned from working through the analysis

- **The denominator changes the story.** The source has 101,766 encounters but 71,518 distinct patient IDs. I need to say clearly whether a KPI is encounter-based or patient-based.
- **A percentage needs its count beside it.** The 14.24% observed in the `[20-30)` band is 236 of 1,657 encounters. The count makes the size of the group visible and helps avoid reading a raw percentage as a prediction.
- **Data quality affects what can be said.** Weight, medical specialty and payer code have substantial missingness. Any comparison involving those fields needs to show how unknown values are treated.
- **A chart can invite an incorrect comparison.** The dashboard's average-measures visual combines metrics with different units. A better version would separate days, medications, procedures and diagnoses into clearer individual visuals.

## What I would do next

1. Redesign the average-measures visual so values with different units are not compared on one shared axis.
2. Put encounter counts and denominators next to key subgroup percentages.
3. Confirm metric definitions with a real subject-matter expert in a future project before proposing operational action.
4. Re-run the queries in MySQL Workbench and confirm that its outputs match the validated CSV results.

## What this project does not prove

It does not show that a hospital reduced readmissions, saved money, deployed a workflow or validated a clinical risk model. Those outcomes would require separate evidence and real-world evaluation.
