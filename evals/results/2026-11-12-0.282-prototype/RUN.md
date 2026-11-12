# jail-prototype 1.2.0 vs 2.0.0 — clean run (2026-11-12)

8 cases (4 original 0.25 + 4 new review-page cases) × Haiku/Sonnet, Project access blocked (`--disallowed-tools Projects`; 0 runs used it). Two blind Sonnet graders; 5 disagreements, scored strict.

| | 1.2.0 | 2.0.0 |
|---|---|---|
| Cases fully passing | 7/16 (44%) | 4/16 (25%) |
| Assertions | 76% | 67% |

VERDICT: REVERT 2.0.0. It built better pages (numbered blocks, three layouts behind one switch, Copy my answers), but lost on what the reply says:
- Build replies didn't restate the shape, timebox, how the variants differ, numbered points, or phone check, so a reviewer reading only the reply couldn't tell.
- The 6-clause SHIP GATE failed closed when the ledger or archive couldn't be reached: a clear reviewer pick shipped as `inconclusive` (0280-2).
- Offered three candidate questions instead of one; promotion refusals didn't cite the gate or name polish-to-ship.

Fix → 2.0.1: PROTOTYPE BRIEF at the top of every build reply; hard gate = verbatim evidence, no production paths, marking (ledger/archive/lint recorded, not blocking); exactly one proposed question; promotion refusals cite the gate. Retest: `2026-11-12-0.283-prototype`.
