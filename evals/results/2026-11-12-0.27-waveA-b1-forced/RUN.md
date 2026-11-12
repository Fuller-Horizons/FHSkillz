# 0.27 wave A, batch 1: forced-invocation blind A/B (2026-11-12)

Skills: jail-verify, jail-decide, jail-research, jail-task-contract, jail-red-team, jail-summarize.
Arms: old = 0.26.0 (commit a8c00d4), new = 0.27 wave-A snapshot. Each prompt prefixed `/fh-skillz:<skill>` so the skill always loads.
Cases: 3 spec cases + 1 held-out case per skill (authors never saw the held-out cases), × Haiku and Sonnet, × old and new = 96 runs, 0 errors, 0 timeouts, $6.28.

Grading: two blind Sonnet graders (g1, g2) per pack, labels A/B only (key in `private/key.json`, not shown to graders). 14 cells disagreed; the orchestrator (Opus) resolved them blind from the packs → `grades/resolved.jsonl`. A case passes only if every assertion passes.

| Skill | Old case pass | New case pass | Verdict (rule: new must beat old, no assertion regressing on ≥2 cases) |
|---|---|---|---|
| jail-decide | 7/8 | 8/8 | KEEP |
| jail-research | 3/8 | 5/8 | KEEP |
| jail-summarize | 5/8 | 6/8 | KEEP |
| jail-task-contract | 4/8 | 6/8 | KEEP |
| jail-red-team | 7/8 | 7/8 | TIE → REVERT by rule (pending owner call) |
| jail-verify | 6/8 | 6/8 | TIE → REVERT by rule (pending owner call) |

Overfitting check (held-out only): new 10/12 cases (46/48 assertions) vs old 8/12 (42/48). Spec cases: new 28/36 vs old 24/36. The new versions do as well or better on cases their authors never saw.

Before tie-break (strict AND of both graders) the verdicts were the same except decide and verify, which were TIE and old-better respectively; three of the verify tie-breaks concerned whether a PASS-WITH-FLAGS headline that explicitly says "UNVERIFIED" satisfies "marks the claim UNVERIFIED rather than PASS" (resolved: yes).

Caveat: 4 cases × 2 models per skill. One case is a 12.5-point swing; treat ties and 1-case wins as weak evidence.

Files: `runs.jsonl` (cost/duration per run), `outputs/` (A/B-labeled outputs), `grading/` (packs), `grades/` (g1, g2, resolved), `summary.json`, `private/key.json`. Raw stream transcripts (`raw/`) are kept locally, not committed.
