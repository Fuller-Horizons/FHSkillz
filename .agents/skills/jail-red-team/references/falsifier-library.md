# Falsifier library

Cheapest test by finding type. Pick one, state the result that confirms the
finding and the result that disproves it BEFORE running it. If you cannot run
it now, mark it `HANDOFF` with an owner. Tests that touch real customers,
systems, or money need the owner's approval; this skill only specifies them.

| Finding type | Cheapest test | Confirms the finding | Disproves it |
|---|---|---|---|
| Demand or pricing assumption | 5 structured customer calls using the interview questions from jail-research (I-CUSTINT style): last time the problem came up, what they did about it, what they pay now, what they would give up to avoid it. Optional: a price-test landing page with the new price shown. | Most of the 5 describe no recent pain, no current spend, or would switch or leave at the new price; landing page visitors do not click through. | Most of the 5 name a current workaround and spend, and accept the new price without trading down. |
| Adoption | A small pilot with ONE adoption metric and its pass line set before the pilot starts (for example, share of the pilot group using it weekly by week 4). | Metric misses the pre-set line. | Metric meets the line with no extra push from the team. |
| Cost or timeline | Reference class: find 3 comparable past projects (internal or published) and compare their actual cost and duration to the plan. | The plan sits well below all 3 actuals with no stated reason. | The plan is inside the range of the 3 actuals, or the gap has a named, checkable cause. |
| Dependency | Written confirmation from the dependency's owner of date, scope, and what happens if it slips. | Owner cannot confirm, confirms a later date, or confirms a narrower scope. | Owner confirms in writing, including the fallback. |
| Regulatory or contractual | Quote the exact rule or clause text and check the plan against the words, not a summary of them. | The text requires something the plan does not do. | The text permits the plan, or the requirement is met by a named feature. |
| Financial model | Change the top 3 inputs by plus and minus 20 percent, one at a time, and record the change in the result. | The conclusion flips, or the margin goes negative, inside that range. | The conclusion holds across the range. |
| Stakeholder | One 1:1 interview with the named stakeholder, asking what they would have to change and what they would do if they disagreed. | They name a cost or a veto the plan ignores. | They name no blocking cost and can state their role in the plan correctly. |

## Rules
- One finding, one falsifier. If a test would settle two findings, say so and
  list it under both.
- Prefer a test that finishes in a day or less. A cheaper test beats a
  better test that never runs.
- "Inconclusive" is a valid result. Record it and keep the finding as an open
  question rather than rounding up to confirmed.
- Manual fallback: every test above can be done by hand with a spreadsheet,
  a call list, or a document search. No scripts are needed.
