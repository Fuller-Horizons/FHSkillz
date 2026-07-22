# Wave 1 scorecard — trigger baseline (0.22.0)

Date: 2026-07-22 · Contract: [enhancement-metrics-contract.md](enhancement-metrics-contract.md)

## Ship-gate status

| Gate | Target | Measured | Status |
|---|---|---|---|
| Trigger fire rate | ≥ 95% | **100%** (63/63) | ✅ PASS |
| False-fire rate | ≤ 5% | **0%** (0/17) | ✅ PASS |
| Variance ×3 (collision set) | stable | **36/36 picks identical** | ✅ PASS |
| Behavioral assertions | 100% pass | not yet run | ⏳ Wave 1b |
| jail-rate-skill ≥ 8.0 / validator / 5-min friend test | — | carried from 0.21.0 checks | ✅ standing |

Method, evidence files, judge agent IDs, and the 3 disclosed accept-set
alternates: [evals/results/2026-07-22-trigger-baseline/RUN.md](../evals/results/2026-07-22-trigger-baseline/RUN.md).
Strict-primary-only scoring is 96.3% / 0% — PASS under both readings.

## What this run proves — and doesn't

**Proves:** the 29 descriptions route correctly under blind judging, including
the hard collision set (verify vs rate vs red-team, decide vs rate, prompt vs
research, memory-refuses-secrets, council vs orchestrate, diagnose vs verify,
baton vs memory, wayfind vs orchestrate), and the no-fire discipline holds on
trivial asks. Judged from descriptions alone — exactly what a router sees.

**Doesn't prove:** in-skill behavior (assertion suites), multi-turn chains, or
live-platform installs. Those are Wave 1b (behavioral executor), already
authored in the excluded suites.

## Fix loop

Zero failures → no description changes this wave. Ledger entry #0 (baseline,
metric 100.0) recorded in `evals/results/trigger-accuracy-ledger.jsonl` so any
future description edit measures against a real number, per jail-lab rules.

## 0.22.0 release contents

- `scripts/run-trigger-evals.py` — reusable blind trigger-eval harness (infra, not skill content)
- `evals/trigger-accept-map.json` — scoring key for all 80 trigger cases
- `evals/results/2026-07-22-trigger-baseline/` — evidence bundle
- `evals/results/trigger-accuracy-ledger.jsonl` — jail-py-lab ledger, baseline #0
- README/scorecard/dashboard updates. **No SKILL.md content changed.**

## Next (Wave 1b, on approval)

Behavioral executor: run the 8 kernel case types + integration chains +
council/mp/rate/prompt behavioral suites with fresh-grader assertion checks,
variance ×3 on flaky-prone cases.
