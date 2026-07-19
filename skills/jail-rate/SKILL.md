---
name: jail-rate
metadata:
  version: 2.0.0
description: >-
  Rate and judge ANYTHING on a disciplined 0.0–10.0 scale — software, apps,
  SaaS, websites, codebases, code, hardware, physical products, people
  (professional/public roles only), ideas, business plans, programs,
  initiatives, services, businesses, content, processes — using a weighted
  rubric matched to what is being rated and empirical, cited evidence behind
  every score. Then give prioritized recommendations and a projected
  post-improvement rating (current → potential). Use whenever the user asks to
  "rate", "score", "judge", "grade", "review", or "evaluate" something; says
  "how would you rate this", "give it a 0–10", "what's its score out of 10",
  "is this idea any good"; or wants a before/after rating showing the upside of
  fixing issues. Do NOT use for rating an AI skill directory (use rate-skill)
  or for sell-side company prospecting briefs (use company-prospect-research).
---

# JAIL-RATE — Universal Evidence-Based Rating (0.0–10.0)

Rate any subject with a rubric built for **what it is**, scores grounded in
**cited empirical evidence**, and a clear split between **current** reality and
**potential** after fixes. No vibes, no grade inflation, no unlabeled guesses.

## Process

### 1 — Classify the subject
Name what you're rating before anything else. Types with built-in rubrics (see
[rubric-library.md](references/rubric-library.md)): **software product ·
codebase/code · hardware/physical product · person (professional) · idea/concept
· program/initiative · service/business · content/media**. Anything else: derive
a rubric with the library's meta-procedure. If the subject is an AI skill
directory, hand off to **rate-skill**; if the ask is a brokerage/consulting
prospect decision on a company, hand off to **company-prospect-research**.

### 2 — Declare the rubric (before scoring)
Pull the type's dimensions + weights from the library (or derive them), adjust
if the user's context demands it, and **show the rubric first**: each dimension,
its weight, and one line on why it's weighted that way for this subject type.
Weights must sum to 100%. If the user supplies weights, use theirs and say so.
Never score against an undisclosed rubric.

### 3 — Gather empirical evidence (default: live research)
Scores follow evidence, not the other way around. By default, **search
authoritative external sources** — benchmarks, reviews, studies, docs, filings,
issue trackers, changelogs, teardown reports — per
[evidence-standards.md](references/evidence-standards.md): tiered sources,
recency-checked, each citation carrying URL + date accessed. Also inspect
whatever the user supplied (code, product, document). Exceptions:
- **Private/internal subjects** (an unreleased app, an internal program, the
  user's own draft): rate from supplied materials, mark external evidence
  **N/A — private subject**, and say what independent evidence would upgrade
  confidence.
- Every claim behind a score is labeled **Fact** (cited) · **Inference**
  (reasoned from cited evidence) · **Judgment** (expert read, no direct
  source) — the compact form of the constitution's seven-class taxonomy
  (docs/JAIL-CONSTITUTION.md Rule 1); use the full set when the consumer
  needs Estimate/User-provided distinguished. A dimension resting only on Judgment gets its confidence capped at
  Low and says so.

### 4 — Score each dimension (0.0–10.0, one decimal)
Calibration anchors — identical for every subject type:

- **9.0–10.0 Exceptional** — best-in-class; hard to meaningfully improve. Rare.
- **8.0–8.9 Excellent** — strong across the board, only minor gaps.
- **7.0–7.9 Good** — solid and competitive; a few real weaknesses.
- **6.0–6.9 Above average** — works, clearly behind the best.
- **5.0–5.9 Average** — does the job; notable rough edges.
- **3.0–4.9 Weak** — significant problems undermine it.
- **1.0–2.9 Poor** — largely fails at its purpose.
- **0.0–0.9 Broken/untenable.**

Rules: every score cites its specific evidence; no 9+ for merely good;
**a critical flaw caps its dimension at ≤ 4.0** (an exploitable vulnerability,
a safety defect, a fatal feasibility blocker, a disqualifying integrity issue)
regardless of other strengths; same subject + same evidence → same score on
re-rating; missing evidence lowers stated confidence — it never silently
becomes a guessed score.

### 5 — Compute, recommend, project
**Overall = Σ(score × weight)**, one decimal. Recommendations ranked by
impact × (1/effort) — biggest movers first, each tied to the dimension(s) it
lifts. Then re-score assuming only the recommended fixes are implemented
competently (not perfection) and show **current → projected (Δ)**, labeled an
estimate.

## Output format

Lead with the headline, then the declared rubric, then the evidence-backed
scorecard, then sources.

> **[Subject] — [type] — Overall: X.X / 10 → Y.Y / 10 projected (▲ +Z.Z)**

**Rubric used** (declared before scoring; weights sum to 100%)

| Dimension | Weight | Why this weight for a [type] |
|---|:---:|---|

**Scorecard**

| Dimension | Weight | Now | Projected | Evidence (label + source) |
|---|:---:|:---:|:---:|---|

**Why this score** — 2–4 sentences on the biggest drivers up and down.

**Top recommendations (ranked)** — numbered; each names its dimension, expected
impact, rough effort.

**Projected rating** — which fixes move which dimensions; why the new total is
realistic (not a 10).

**Sources** — numbered list, each: source · what it evidenced · URL · date
accessed. Private-subject ratings state "rated from supplied materials only."

**Confidence** — High / Medium / Low per the evidence-depth rules in
[evidence-standards.md](references/evidence-standards.md), with the one thing
that would most raise it.

Quick ask → a single line (`X.X/10 — one-sentence why + strongest evidence`) is
acceptable; offer the full scorecard.

## Self-check before delivering (all must pass)
- Weights shown, sum exactly 100%; rubric declared **before** any score.
- Overall recomputed: Σ(score × weight) matches the headline to one decimal
  (show the arithmetic on request). Projected overall recomputed the same way.
- Every scorecard row has ≥1 evidence entry — a numbered citation or an
  explicit **Judgment** label; no bare adjectives.
- Every citation resolves in Sources with URL + date accessed (or the
  private-subject statement is present).
- Any critical flaw applied its ≤ 4.0 cap; current and projected never blended.
- Confidence stated with the one action that would most raise it.
One failed line = fix before delivering, not a footnote.

## Rating people — hard boundaries
Professional/public evaluation only, and only with public, verifiable evidence
(track record, published work, documented outcomes, public statements in the
role). Never: private individuals' personal lives, protected attributes (race,
religion, age, health, orientation, etc.), rumor/anonymous allegations as
evidence, or "character" scores. Frame the output as an **evidence-based
assessment of professional performance in a role**, name the role, and refuse
or reframe requests outside these lines (offer the role-performance version).
Thin public evidence → say so and keep confidence Low; a person is never rated
on vibes.

## Guardrails
- Never blend current and potential into one number; always show both.
- Rubric before scores; evidence before rubric-filling; cite or label Judgment.
- Uncited marketing claims are claims, not evidence — verify or downgrade.
- State assumptions and everything you couldn't verify.
- The projected score is an estimate of upside, clearly labeled.

## Gotchas
- **Scoring before evidence.** Deciding 7-ish then decorating it with sources.
  Gather first; let scores fall out of the anchors.
- **One rubric for everything.** Rating hardware on "software quality" or an
  idea on "usability." Classify first; the rubric must match the subject.
- **Hidden rubric.** Presenting scores without the weighted rubric that
  produced them. Declare it first, every time.
- **Marketing-claim laundering.** A vendor's "99.9% uptime" cited as Fact. That
  tier of source is a claim to verify, not evidence (see evidence-standards).
- **People-rating drift.** A role-performance rating sliding into character
  judgment or personal-life material. Re-read the boundaries section; reframe.
- **Stale evidence.** Reviews or benchmarks years old scored as current state.
  Date every citation; flag anything stale to the subject's cadence.
- **False precision.** A 7.4 the evidence can't distinguish from a 7.6. Anchor
  the band first; use the decimal only when evidence supports it.
- **Wrong skill.** AI skill directory → rate-skill. Prospect decision →
  company-prospect-research. Engineering the prompt to run a rating elsewhere →
  jail-prompt.
