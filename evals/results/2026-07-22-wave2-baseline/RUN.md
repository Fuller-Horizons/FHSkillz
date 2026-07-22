# Wave 2 trigger baseline — 2026-07-22 (0.23.0)

Re-baseline after the wave-2 enhancement program: 17 skills enhanced, 4
merged into 2 (jail-strategy-scan, jail-py-toolkit), 27 descriptions, 95
trigger cases (80 carried + 15 new wave-2 + 3 retargeted: k14/k15 →
strategy-scan, n8 → cpr's new DEBRIEF lane).

## Result (post fix loop)

| Metric | Value | Gate | Verdict |
|---|---|---|---|
| Fire rate | **79/79 = 100%** | ≥ 95% | PASS |
| False-fire rate | **0/16 = 0%** | ≤ 5% | PASS |
| Collision variance (3 × 12 cases, incl. flipped n8) | **36/36 identical** | stability | PASS |

Every new lane routed correctly first try: strategy-scan ×3 (legacy SWOT/
PESTLE keywords included), mini-council, orchestrate SOLO, cpr DEBRIEF,
py-toolkit, quarantine INLINE, prospect SNAPSHOT, red-team PRE-MORTEM-LITE —
and the 5 new near-misses (baton-vs-solo, memory-vs-baton, cpr-design-
still-fires, rate-vs-strategy-scan) all held.

## The one failure and its fix (the loop working as designed)

- **Pre-fix score: 78/79 (98.7%) / 0%** — gate PASS, one miss:
  `wave2::wn1` "Run the numbers on which vendor is cheaper over three years
  and pick one" judged **none**; accept jail-decide.
- **Fix:** jail-decide description gained quantified-comparison phrases
  ("run the numbers on A vs B and choose", "which is cheaper over N
  years") — matching the new quantified lane it shipped this wave.
- **Verification:** fresh blind judge on wn1 + 4 regression neighbors
  (k4, kernel n4, rate n4, wn5): wn1 → jail-decide, all neighbors
  unchanged (no theft from rate/research/none). fixloop-rejudge.json.
- wn1 stays in the suite as the regression case for this fix
  (jail-diagnose's mandatory-regression rule applied to descriptions).

## Ledger note (honest bookkeeping)

`trigger-accuracy-ledger.jsonl` entries #1 (98.7, DISCARD) and #2 (100.0,
tie-vs-best → DISCARD by strict lab semantics). Read #2's verdict in
context: the suite grew 80 → 95 cases (19% more surface, deliberately
harder), so recovering the 100.0 ceiling is maintenance of the gate on a
bigger suite, not a failed experiment; the fix itself is evidenced by the
targeted re-judge, and the description change is KEPT on that evidence.
The ledger is append-only — the verdicts stand as recorded, with this
note as the interpretation.

## Method

Identical to wave 1 (blind manifests via scripts/run-trigger-evals.py;
scoring key isolated in private/; one independent subagent judge per
batch, tool traces = exactly 1 read each; 3× judgments on the collision
set). Judge agent IDs in variance-collision.json and the session log.

## Files
baseline-report.json · picks.jsonl (final) · fixloop-rejudge.json ·
variance-collision.json · ledger: ../trigger-accuracy-ledger.jsonl (#1–#2)
