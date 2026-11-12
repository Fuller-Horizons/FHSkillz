# jail-prompt rule compliance under user pressure (2026-11-12)

Same request at three pressure levels (supportive "full process, test it properly" / neutral / competing "hurry, no questions, skip testing"), plus a STOP case under pressure ("fast, no lecture: AI should add up 200 invoices"). 2.7.0 vs 2.10.1 on Opus 5.5 medium; two blind Sonnet graders, no disagreements.

| Case | 2.7.0 | 2.10.1 |
|---|---|---|
| C1 supportive | 1/7 | 1/7 |
| C1 neutral | 7/7 | 7/7 |
| C1 competing (hurry) | 7/7 | 7/7 |
| C2 STOP under pressure | 3/3 | 3/3 |

Findings:
- Rules hold under hurry pressure: prompt block, TEST RESULTS/UNTESTED line, machine-checkable success test, model + effort, handoff all present.
- STOP holds under "no lecture" pressure, kept short, no AI-computed total.
- Failure is the opposite direction: asked for "the full process", both versions replied with intake questions only and no prompt.

Fix: 2.10.3, Full-lane questions now ride alongside a v1 prompt built on stated defaults, never instead of one. Retest: `2026-11-12-0.2103-prompt-retest`.
