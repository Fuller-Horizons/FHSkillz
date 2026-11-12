# jail-prompt end-to-end test: plain request vs jail-prompt's prompt (2026-11-12)

What it measures: whether running jail-prompt's engineered prompt gives a better FINAL output than sending the plain request.
- old arm = the plain one-line request + inputs, sent straight to the model.
- new arm = jail-prompt 2.10.0 (on Opus 5.5, medium effort) writes a prompt for the task; that prompt + the same inputs run on the same model.
- Final runs on Sonnet 5.5 and Haiku 5.5 at medium effort. 4 synthetic business tasks: P&L cost drivers, customer-complaint ranking, cold outreach email, vendor quote comparison. 16 runs, 0 errors; jail-prompt produced a usable prompt 8/8 times.

Grading: two blind Sonnet graders (labels A/B; key withheld), 2 disagreements resolved blind by the orchestrator → `grades/resolved.jsonl`.

| | Plain request | jail-prompt's prompt |
|---|---|---|
| Outputs passing every check | 4/8 (50%) | **8/8 (100%)** |
| Assertions passed | 40/44 (91%) | **44/44 (100%)** |
| Per case × model | — | won 4, tied 4, lost 0 |
| Average cost per task | $0.023 | $0.242 |

Where the plain request fell short: no business meaning per cost driver (P&L, both models); one complaint without a direct quote (Haiku); invented facts in the cold email ("recently helped", "20 years") (Sonnet).

Cost note: jail-prompt's prompt-writing step runs on Opus 5.5, about 10× the cost of the plain request per task. The prompt is reusable, so that cost is paid once per prompt, not per run.

Caveats: 4 tasks, synthetic data; ties come from both arms scoring at or near the ceiling, so these tasks don't separate the arms well on the easy cases.
