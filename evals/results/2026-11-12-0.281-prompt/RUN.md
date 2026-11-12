# jail-prompt 2.13.0 vs 2.12.0 (2026-11-12)

10 cases on Opus 5.5 medium, Project access blocked (0 runs used it): 3 new question-round cases (`evals/behavioral-0.28/jail-prompt-questions.json`) plus the 7-case regression set (delegation, trivial email, STOP, four compliance cases). Two blind Sonnet graders; 1 disagreement (on a 2.12.0 output, no verdict change).

| | 2.12.0 | 2.13.0 |
|---|---|---|
| Cases fully passing | 8/10 | **10/10** |
| Assertions | 92% | **100%** |

- Q1 (ambiguous monthly report prompt): 2.12.0 asked open-ended questions with no options and no add-context option; 2.13.0 asked multiple-choice questions, recommended option first, an add-context option, and gave a v1 draft.
- Q2 (new bank context after two rounds): both updated the draft; only 2.13.0 kept questions multiple choice with an add-context option.
- Q3 (simple one-off): both asked nothing and gave the prompt.
- All 7 regression cases pass on both: no regression.

VERDICT: KEEP. Merged as plugin 0.28.1.
