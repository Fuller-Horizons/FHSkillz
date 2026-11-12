# jail-prompt old vs new, blind A/B (2026-11-12)

old = jail-prompt 2.1.0 (0.27 wave-A rewrite), new = 2.10.0 (the 0.27.0 release). Both arms on Claude Opus 5.5 at medium effort (2.10.0 pins that model; running both on it isolates the instructions). 7 cases (3 spec + 4 delegation), forced invocation, 14 runs, 0 errors, $4.81. Two blind Sonnet graders; 2 disagreements resolved blind → `grades/resolved.jsonl`.

| Case | 2.1.0 | 2.10.0 |
|---|---|---|
| 0270-1 cost drivers prompt | 4/4 | 4/4 |
| 0270-2 add 40 numbers (STOP) | 3/3 | 2/3 (no multiple-choice next step) |
| 0270-3 reusable coding prompt | 3/3 | 3/3 |
| D1 parallel research → delegation set | 5/6 | 3/6 (wrote the prompts to a file; reply showed a summary) |
| D2 40 websites, cheap models | 5/6 | 5/6 |
| D3 thank-you email: don't delegate | 2/3 | 3/3 |
| D4 free ChatGPT, paste-in chain | 4/4 | 4/4 |
| **Cases fully passed** | **4/7** | **4/7** |
| **Assertions** | **26/29 (90%)** | **24/29 (83%)** |

Verdict by the pre-set rule: tie on cases → not a win. Cost per run $0.33 vs $0.36; time 51 s vs 53 s.

Diagnosis: D1 — 2.10.0's delegation design was strong (Opus discovery, Sonnet profiles with Opus escalation, quote check, merge on Opus high, Fable 5.2 verifier) but it put the prompts in `prompts.md` and showed a summary, which broke its own "surface the prompt in the reply" rule and left the graders nothing to grade. 0270-2 — the STOP omitted the lettered next-step choice.

Fixes → 2.10.1 (both rules tightened); the three affected cases are re-tested in `../2026-11-12-0.2101-prompt-retest/`.

Caveat: 7 cases, one run each; one case flips the case rate by 14 points.
