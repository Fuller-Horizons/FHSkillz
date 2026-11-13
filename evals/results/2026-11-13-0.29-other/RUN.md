# 0.29 blind test: jail-task-contract 1.6.0 and new jail-questionnaire (2026-11-13)

Sonnet 5.5, old = main (0.28.1), new = branch. Two blind Sonnet graders.

| Skill | Old cases | New cases | Verdict |
|---|---|---|---|
| jail-task-contract 1.6.0 | 0/2 (38% asserts) | **2/2 (100%)** | KEEP: multiple-choice frontier rounds with an add-context option; kept the two-year horizon after new context. |
| jail-questionnaire 1.0.0 vs no skill | 0/2 (58%) | **1/2 (92%)** | KEEP: the no-skill baseline wrote 50 questions with no required/optional split. The one miss: the HVAC intake was saved to a file and only summarized, so its question wording couldn't be checked → 1.0.1 shows the full questionnaire in the reply (retest `2026-11-13-0.29r2-qn`). |
