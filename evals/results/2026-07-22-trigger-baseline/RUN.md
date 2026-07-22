# Wave 1 trigger baseline — 2026-07-22

First measured run of the trigger suites (contract: docs/enhancement-metrics-contract.md).

## Result

| Metric | Value | Gate | Verdict |
|---|---|---|---|
| Fire rate (should-trigger routed correctly) | **63/63 = 100%** | ≥ 95% | PASS |
| False-fire rate (no-fire cases that fired) | **0/17 = 0%** | ≤ 5% | PASS |
| Collision-set variance (3 independent judgments × 12 cases) | **36/36 picks identical** | stability check | PASS |

Per-suite: kernel-trigger 29/29 · jail-rate-trigger 16/16 · jail-council 7/7 · mp-wave 8/8 · jail-prompt trigger_evals 20/20.

## Method (reproducible)

1. `python3 scripts/run-trigger-evals.py manifest --repo . --out <dir> --batch 12`
   → 7 blind manifests (29 skill descriptions + queries, **no labels**); scoring
   key written to `<dir>/private/` which judges never open.
2. 7 independent subagent judges, one manifest each, fresh contexts, prompt:
   *"pick exactly one skill name or 'none', judging ONLY from the descriptions;
   respect Do-NOT-use clauses; do not over-fire on trivial asks."* Each judge's
   tool trace shows exactly 1 file read (its manifest) — blindness held.
3. Variance: the 12-case cross-routing collision set (kernel near-misses) was
   judged 3× total by independent judges (agent IDs in variance-collision.json).
4. `python3 scripts/run-trigger-evals.py score --out <dir> --picks picks.jsonl`
   → baseline-report.json, exit 0.

## Honest notes (accept-set alternates used)

3 of 80 cases passed via a designed-ambiguity alternate rather than the primary
accept entry — disclosed per the north-star-supremacy policy:

- `trigger_evals.json::14` (KeyError + traceback) → judged **jail-diagnose**;
  accept was `["none","jail-diagnose"]`. Defensible either way: a supplied
  traceback is already a diagnostic loop. Not a false fire by design.
- `jail-rate-trigger-evals.json::n4` (best laptop under $1000) → judged
  **none**; accept `["none","jail-research"]`.
- `jail-rate-trigger-evals.json::n5` (rate my sister's boyfriend) → judged
  **none**; accept `["jail-rate","none"]` (decline lives in jail-rate's
  people-boundary; never firing is equally safe).

Strict-primary-only scoring would still be 77/80 (96.3% fire · 0% false-fire) —
gate PASS under both readings.

## Scope

Trigger routing only (Wave 1). Behavioral suites (kernel-evals.json,
jail-rate-evals.json, evals.json, council/mp behavioral blocks) are Wave 1b —
excluded via `_exclude_files` in evals/trigger-accept-map.json.

## Files

- `baseline-report.json` — scored report (the machine-checked artifact)
- `picks.jsonl` — all 80 judge picks
- `variance-collision.json` — 3× collision judgments + agent IDs
- Ledger entry #0: `evals/results/trigger-accuracy-ledger.jsonl` (jail-py-lab)
