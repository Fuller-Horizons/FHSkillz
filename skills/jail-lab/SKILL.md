---
name: jail-lab
metadata:
  version: 1.0.0
description: >-
  Run a metric-driven EXPERIMENT LOOP on anything improvable — a prompt, a
  skill, code, content, a workflow, a landing page: declare one metric and a
  budget, then propose → bounded run → measure → keep/discard → log every
  experiment in an append-only audit ledger with cited evidence. Use when the
  user wants to "iterate until it's better", "optimize this", "run
  experiments", "A/B this", "tune it", improve something measurable, or turn
  a vague "make it better" into disciplined trials. Do NOT use when no
  measurable metric can exist (taste-only judgments — use jail-rate for a
  scored assessment) or for one-shot verification (jail-verify).
---

# JAIL-LAB

Never trust an unmeasured improvement. One variable, one bounded run, one
number, one ledger entry — repeat. Pattern adapted from Andrej Karpathy's
[autoresearch](https://github.com/karpathy/autoresearch) (MIT), generalized
from ML training to anything with a metric, with JAIL evidence and audit
discipline added. [Constitution Rules 7, 10, 11]

## Step 0 — Declare the lab (before any experiment)
In plain language, fix four things — they don't change mid-run:
- **Metric** — ONE number and its direction of good ("pass rate, higher";
  "tokens per answer, lower"; "conversion %, higher"). No metric = no lab:
  either build the measurement first or route to jail-rate for a scored
  assessment instead.
- **Baseline** — measure the current state before touching anything.
  Experiment #0 is always the unmodified baseline.
- **Budget** — the bound per experiment (time, tokens, runs, dollars) and
  the total run budget. Autoresearch uses 5 minutes of training per
  experiment; pick your equivalent and enforce it.
- **Stop condition** — target reached, budget exhausted, or N consecutive
  discards (default 5) — whichever first. Endless tinkering is the failure
  mode this skill exists to kill.

## The loop
1. **Propose ONE change** with a one-line **hypothesis**: *why* this change
   should move the metric. One variable per experiment wherever feasible —
   two changes that help and hurt cancel invisibly.
2. **Bounded run** — apply the change, run within budget, same conditions
   as baseline (same inputs, same evaluation) or the comparison is fiction.
3. **Measure** — the declared metric, actually computed. "Feels better" is
   not a measurement.
4. **Compare vs current best** → **KEEP** (strictly better) or **DISCARD**
   (revert the change — a regression never stays because it "should have
   worked"). Ties discard: complexity must pay rent. [Rule 11]
5. **Ledger it** — append-only, every experiment including discards:
   `id · timestamp · change · hypothesis · metric result · verdict ·
   evidence ref`. External claims informing a hypothesis carry citations
   with dates. [Rule 10] Discards are data — they kill the same bad idea
   the second time it's proposed.
6. Loop until the stop condition. Then report: baseline → best, the kept
   changes in order, keep rate, and what the discards taught.

## Running it
- **With the companion skill `jail-py-lab` installed** (needs code
  execution): `lab-run.py` appends measured entries and computes verdicts;
  `lab-report.py` summarizes the ledger. Plain-language flow: tell it what
  you changed, why, and the number — it does the bookkeeping.
- **Manual fallback (no code):** keep the ledger as a markdown table with
  the same seven columns, compute keep/discard by hand, and re-state the
  current best after every entry. The discipline is identical; only the
  bookkeeper changes.

## Related skills
Score without iterating → **jail-rate**. Verify a single output →
**jail-verify**. The metric belongs to a workflow → **jail-operationalize**
defines it first. Skill improvement loops → this skill over jail-rate-skill
scores or eval pass-rates.

## Gotchas
- **Metric-free "labs."** Iterating on vibes and narrating progress. If the
  metric can't be stated in Step 0, this skill refuses — that's the point.
- **Multi-variable experiments.** "I also cleaned up X while at it" —
  now the number is unattributable. One change per entry.
- **Un-reverted regressions.** Keeping a worse result because the idea was
  elegant. The ledger's verdict column is the law.
- **Shifting baseline.** Comparing experiment 7 to experiment 6 instead of
  to the best. Best-so-far is the bar; the ledger tracks it.
- **Ledger amnesia.** Skipping entries for "quick tries." Unlogged
  experiments get re-run by the next session — the audit log IS the asset.
- **Goodhart drift.** The metric improving while the actual goal degrades
  (shorter answers scoring "efficient" but losing correctness). Pair the
  metric with a floor check (e.g. correctness must not drop) in Step 0.
