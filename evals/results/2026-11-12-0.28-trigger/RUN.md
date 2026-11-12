# 0.28 trigger gate — 2026-11-12

Re-run after description changes to jail-prototype (2.0.0), jail-prompt (2.10.x) and jail-py-toolkit (1.7.0). Same 109 cases (90 should-fire, 19 should-not) and 26 descriptions as `2026-11-12-0.27-trigger`.

Judges: three independent Haiku 5.5 agents, descriptions + queries only (accept key withheld in `private/`).

| Judge | Fire | False-fire | Gate (≥95% / ≤5%) |
|---|---|---|---|
| j1 | 90/90 (100%) | 0/19 (0%) | PASS |
| j2 | 90/90 (100%) | 0/19 (0%) | PASS |
| j3 | 90/90 (100%) | 0/19 (0%) | PASS |

No routing regression from the changed descriptions.
Inter-judge agreement: 109/109 unanimous.
