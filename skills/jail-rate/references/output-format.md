# Output format — jail-rate scorecard template

Lead with the headline, then the declared rubric, then the evidence-backed
scorecard, then sources. Keep Now and Projected in separate columns.

```
> **[Subject] — [type] — Overall: X.X / 10 → Y.Y / 10 projected (▲ +Z.Z)**

**Rubric used** (declared before scoring; weights sum to 100%)

| Dimension | Weight | Why this weight for a [type] |
|---|:---:|---|

**Scorecard**

| Dimension | Weight | Now | Projected | Evidence (label + source) |
|---|:---:|:---:|:---:|---|

**Why this score** — 2-4 sentences on the biggest drivers up and down.

**Top recommendations (ranked)** — numbered; each names its dimension,
expected impact, rough effort.

**Projected rating** — which fixes move which dimensions; why the new total is
realistic (not a 10). Label it Estimate.

**Sources** — numbered: source · what it evidenced · URL · date accessed.
Private-subject ratings state "rated from supplied materials only."

**Confidence** — High / Medium / Low per evidence-standards.md, with the one
thing that would most raise it.
```

Rules for the template:
- The headline must use the form `Overall: X.X / 10 → Y.Y / 10 projected` so
  `score-check.py` can read it.
- Weights in the table are written as percentages that sum to 100.
- Evidence cells start with a canonical label (Fact, User-provided, Inference,
  Estimate, Judgment, Unknown) and a `[n]` reference where one exists.
- When several subjects are rated side by side, add one scorecard per subject
  (or one table with a column per subject) and show per-dimension scores for
  all of them. A blended composite may be added, never shown alone.
- Quick ask: one line, `X.X/10 — one-sentence why + strongest evidence`, then
  offer the full scorecard.
