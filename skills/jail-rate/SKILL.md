---
name: jail-rate
metadata:
  version: 1.0.0
description: >-
  Rate and judge a software product on a disciplined 0.0–10.0 scale across five
  weighted dimensions — software quality, features, usability, marketability,
  and security — then give prioritized recommendations for improvement and a
  projected post-improvement rating (current → potential). Use whenever the user
  asks to "rate", "score", "judge", "grade", or "review" a software product,
  app, SaaS, website, or codebase; says "how would you rate this", "give it a
  0–10", "what's its score out of 10"; or wants a before/after rating that shows
  the upside of fixing issues.
---

# JAIL-RATE — Software Product Rating (0.0–10.0)

Produce a consistent, evidence-based rating of a software product, the
improvements that would raise it, and the score it would reach once those
improvements are made. Always separate **current** reality from **potential**.

## When to use
- "Rate / score / judge / grade this app, SaaS, website, or codebase."
- "How would you rate this out of 10?" / "Give it a 0–10."
- "What would the score be after we fix it?" (before/after rating)
- After a code review or product teardown, to attach a numeric verdict.

## The five dimensions (default weights)

| Dimension | Weight | What it measures | Look for |
|-----------|:------:|------------------|----------|
| Software quality | 25% | Architecture, code health, reliability, tests, maintainability | Clear structure, test coverage, error handling, no obvious bugs, CI |
| Features | 20% | Completeness, depth, differentiation, fit to the job-to-be-done | Core flows present, breadth vs. competitors, no critical gaps |
| Usability | 20% | UX, onboarding, clarity, accessibility, ease of ownership | Intuitive flows, sensible defaults, a11y, good empty/error states |
| Security | 20% | Auth, data protection, vulnerability posture, compliance | Input validation, secrets handling, authz, dependency hygiene |
| Marketability | 15% | Market fit, positioning, differentiation, discoverability, GTM readiness | Clear value prop, target audience, SEO/visibility, pricing, traction |

Weights are defaults. If the user supplies weights, use theirs; they must sum to
100%. State the weights you used.

## The 0.0–10.0 scale (calibration anchors)

Score each dimension to **one decimal**. Decimals are meaningful — 7.4 ≠ 7.8.

- **9.0–10.0 — Exceptional.** Best-in-class; hard to meaningfully improve. Rare.
- **8.0–8.9 — Excellent.** Strong across the board, only minor gaps.
- **7.0–7.9 — Good.** Solid and competitive; a few real weaknesses.
- **6.0–6.9 — Above average.** Works well but clearly behind the best.
- **5.0–5.9 — Average / competent.** Does the job; notable rough edges.
- **3.0–4.9 — Weak.** Significant problems undermine it.
- **1.0–2.9 — Poor.** Largely fails at its purpose.
- **0.0–0.9 — Broken / unusable.**

### Calibration rules
- **Evidence over vibes.** Every sub-score cites a specific observation.
- **No grade inflation.** Reserve 9+ for the genuinely exceptional; "good and
  competent" is a 7, not a 9.
- **Critical flaws cap a dimension.** A blocking issue caps the relevant
  dimension at **≤ 4.0** regardless of other strengths — e.g. an exploitable
  vulnerability caps Security; a feature that silently fails caps Features.
- **Consistency.** The same product, same evidence → the same score on re-rating.
- **Confidence.** If evidence is missing, state the assumption (or ask) and note
  it lowered confidence; don't guess silently.

## Process

1. **Gather evidence.** Inspect the product / read the code / use the relevant
   tools. Note what you could and couldn't verify.
2. **Score each dimension** 0.0–10.0 with a one-sentence justification tied to
   specific evidence. Apply the critical-flaw cap where warranted.
3. **Compute the overall**: `Σ(score × weight)`, rounded to one decimal.
4. **Write recommendations**, ranked by **impact × (1/effort)** — biggest score
   movers for least effort first. Tie each to the dimension(s) it lifts.
5. **Project the post-improvement rating.** Re-score each dimension assuming the
   *recommended* fixes (only those) are implemented competently — not
   perfection. Recompute the weighted overall. Show **current → projected** and
   the delta. Label it an estimate.

## Output format

Lead with the headline, then the scorecard, then the reasoning.

> **Overall: X.X / 10**  →  **Y.Y / 10** projected after fixes  (▲ +Z.Z)

| Dimension | Weight | Now | Projected | One-line basis |
|-----------|:------:|:---:|:---------:|----------------|
| Software quality | 25% | 0.0 | 0.0 | … |
| Features | 20% | 0.0 | 0.0 | … |
| Usability | 20% | 0.0 | 0.0 | … |
| Security | 20% | 0.0 | 0.0 | … |
| Marketability | 15% | 0.0 | 0.0 | … |

**Why this score** — 2–4 sentences on the biggest drivers up and down.

**Top recommendations (ranked)**
1. *(Dimension)* Action — expected impact, rough effort.
2. …

**Projected rating** — which fixes move which dimensions, and why the new total
is realistic (not a 10).

For a quick ask, a single line is acceptable — `X.X/10 — one-sentence why` — but
offer the full scorecard.

## Guardrails
- Never blend current and potential into one number; always show both.
- Justify with specifics; no unsupported adjectives.
- Don't inflate; 9+ is exceptional, not merely good.
- State assumptions and anything you couldn't verify.
- The projected score is an estimate of upside, clearly labeled as such.

## Brief example

> **Overall: 6.2 / 10 → 8.1 / 10 projected (▲ +1.9)**

| Dimension | Weight | Now | Projected | Basis |
|-----------|:------:|:---:|:---------:|-------|
| Software quality | 25% | 6.5 | 8.5 | Clean modules, but no tests / CI gaps |
| Features | 20% | 7.0 | 7.5 | Core flows solid; thin reporting |
| Usability | 20% | 6.0 | 7.5 | Works, weak onboarding & empty states |
| Security | 20% | 4.0 | 8.5 | Capped: unescaped output (stored XSS) |
| Marketability | 15% | 7.5 | 8.0 | Clear niche, good SEO surface |

Security caps the current total; fixing the XSS plus adding tests/CI is the fast
path from 6.2 to ~8.1.
