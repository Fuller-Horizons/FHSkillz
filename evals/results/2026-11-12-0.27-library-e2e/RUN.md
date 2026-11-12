# Prompt library test: library prompt vs plain request (2026-11-12)

The four prompts seeded in the prompt library (Project doc `claude/prompt-library.md`), each run on its matching synthetic task against the plain one-line request, on Sonnet 5.5 and Haiku 5.5 at medium effort. 16 runs, 0 errors. Two blind Sonnet graders; 1 disagreement resolved blind.

| Library prompt | Library | Plain request | Per model |
|---|---|---|---|
| P&L cost drivers | 12/12 | 8/12 | won 2 |
| Interview complaints | 12/12 | 11/12 | won 1, tied 1 |
| Cold outreach email | 10/10 | 8/10 | won 2 (plain requests invented facts, including a made-up sender email) |
| Vendor quote comparison | 10/10 | 10/10 | tied 2 (not yet shown to beat a plain request) |
| **Outputs passing every check** | **8/8** | **3/8** | |

Cost per task: library $0.028 vs plain $0.020. The library's Tested lines were updated from these results.
