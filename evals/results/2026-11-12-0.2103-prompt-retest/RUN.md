# jail-prompt 2.10.3 retest vs 2.1.0 (2026-11-12)

Seven cases on Opus 5.5 medium: the three that exposed 2.10.0/2.10.1 problems (D1 delegation, D3 trivial email asked for subagents, 0270-2 adding up numbers) plus the four compliance cases. Two blind Sonnet graders; no disagreements.

| Case | 2.1.0 | 2.10.3 |
|---|---|---|
| D1 parallel research delegation | 4/6 | **6/6** |
| D3 trivial email, subagents asked | 2/3 | **3/3** |
| 0270-2 add up numbers (STOP) | 3/3 | 3/3 |
| C1 supportive ("full process, test it") | 1/7 | **7/7** |
| C1 neutral | 5/7 | **7/7** |
| C1 competing ("hurry, skip testing") | 5/7 | 6/7 |
| C2 STOP under pressure | 3/3 | 3/3 |
| **Cases fully passing** | 2/7 (29%) | **6/7 (86%)** |
| **Assertions** | 64% | **97%** |

VERDICT: KEEP. Both earlier regressions are fixed: D3 now gives one prompt and says subagents don't fit; the supportive case now gives a v1 prompt with its questions.
Only miss: one sentence after the JAIL-HANDOFF block (fixed in 2.10.4, wording only, untested).
