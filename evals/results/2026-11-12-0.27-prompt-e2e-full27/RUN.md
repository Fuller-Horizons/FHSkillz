# Minimal-first vs full template: jail-prompt end-to-end (2026-11-12)

Question: does jail-prompt 2.10's minimal-first core (OBJECTIVE, SUCCESS TEST, QUALITY BAR, OUTPUT FORMAT, RUN SETTINGS + earned add-ons) give final outputs at least as good as 2.7.0's full template?

Same 4 tasks, same final models (Sonnet 5.5, Haiku 5.5, medium), same grader brief as `2026-11-12-0.273-prompt-e2e`. Two blind Sonnet graders.

| | Plain request | 2.7.0 full template | 2.10.0 minimal-first |
|---|---|---|---|
| Outputs passing every check | 2/8 | 6/8 | **8/8** |
| Assertions passed | 82% | 95% | **100%** |
| Prompt length (words) | — | 452–974 | 316–584 |
| Cost per task | $0.020 | $0.258 | $0.242 |

Full-template misses: the complaint-ranking task (jp-e2e-2) lacked a direct quote for one complaint on both models.

DECISION: keep minimal-first as the default (scores at least as well, prompts about 40% shorter). Caveat: plain-arm scores differ between runs (2/8 here, 4/8 before), so grader variance is about ±2 cases at n=8.
