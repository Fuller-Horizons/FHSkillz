---
name: jail-rate
metadata:
  version: 2.3.0
description: >-
  Rate, score, grade, judge, or evaluate ANY named subject 0.0-10.0 (software,
  code, hardware, small business, idea, plan, program, content, a person's
  public work role) with a weighted rubric, cited evidence, ranked
  fixes, and current to projected scores. Triggers: "rate this", "give it a
  0-10", "how would you grade", "is this idea any good". Do NOT use for AI skill
  folders (jail-rate-skill), prospect calls (jail-prospect), SWOT (jail-strategy).
---

# JAIL-RATE — Universal Evidence-Based Rating (0.0–10.0)

Rate any subject with a rubric built for **what it is**, scores grounded in
cited evidence, and a clear split between **current** reality and
**potential** after fixes. No vibes, no grade inflation, no unlabeled guesses.

## Process

### 1 — Classify the subject
Name what you are rating first. Built-in rubrics (see
[rubric-library.md](references/rubric-library.md)): software product ·
codebase · hardware · person (professional role) · idea/plan · program ·
service/business · **small business (diagnostic)** · **sales & marketing
function** · **leadership team (professional role)** · content/media. Anything
else: derive a rubric with the library's meta-procedure. AI skill directory →
**jail-rate-skill**. Pursue/pass prospecting call on a company → **jail-prospect**.

### 2 — Declare the rubric (before scoring)
Show each dimension, its weight, and one line on why it is weighted that way.
Weights sum to 100%. User-supplied weights win; say so. Never score against an
undisclosed rubric.

### 3 — Gather evidence (default: live research)
Scores follow evidence. Search authoritative sources per
[evidence-standards.md](references/evidence-standards.md) (tiered, dated, each
citation = source · what it evidenced · URL · date accessed) and inspect what
the user supplied. **Private or internal subjects:** rate from supplied
materials, mark external evidence **N/A — private subject**, and say what
independent evidence would raise confidence. Label every claim behind a score:
**Fact** (cited) · **User-provided** (said by the owner/client, unverified,
name who) · **Inference** (reasoned from cited Facts) · **Estimate** (stated
method) · **Judgment** (expert read, no source) · **Unknown**. A dimension
resting only on Judgment or User-provided claims has confidence capped at Low.

### 4 — Apply the bias controls
*Pattern adapted from ECC (github.com/affaan-m/ECC, MIT, © 2026 Affaan Mustafa).*
- **Asserted vs proven.** Self-reported or marketing claims with no
  corroboration are downgraded: score them as claims (User-provided) and seek
  a Tier 1–2 source. Site copy, vendor badges, and owner statements are not Facts.
- **Aesthetic, recency, survivorship.** Polish is not quality; flashy recent
  wins do not outweigh the long record; the visible examples are not the whole
  field (note quiet or failed comparables). Score craft and substance separately.
- **Side-by-side sets.** Rate every subject on the same rubric and calibrate
  across the set (a 7.0 means the same for each). Report **per-dimension
  scores for every subject**, never only a blended composite.

### 5 — Score each dimension (0.0–10.0, one decimal)
Calibration anchors, same for every subject type:
- **9.0–10.0 Exceptional** — best-in-class; rare.
- **8.0–8.9 Excellent** — strong everywhere, minor gaps.
- **7.0–7.9 Good** — solid; a few real weaknesses.
- **6.0–6.9 Above average** — works, clearly behind the best.
- **5.0–5.9 Average** — does the job; notable rough edges.
- **3.0–4.9 Weak** — significant problems.
- **1.0–2.9 Poor** — largely fails its purpose.
- **0.0–0.9 Broken.**

Rules: every score cites its evidence; no 9+ for merely good; a **critical
flaw caps its dimension at ≤ 4.0** (exploitable vulnerability, safety defect,
fatal feasibility blocker, disqualifying integrity issue, or a material
concentration risk such as one customer carrying a large share of revenue);
same subject + same evidence → same score; missing evidence lowers
confidence and never becomes a guessed score. Maximum-stakes ratings →
**jail-council** on the contested dimensions.

### 6 — Compute, recommend, project
**Overall = Σ(score × weight)**, one decimal. Recommendations ranked by
impact ÷ effort, each tied to the dimensions it lifts. Re-score assuming only
the recommended fixes land competently (not perfection); show **current →
projected (Δ)**, labeled **Estimate**.

## Output format
Headline, declared rubric, scorecard (Now and Projected as separate columns),
why, ranked recommendations, projected rating, sources, confidence. Exact
template: [references/output-format.md](references/output-format.md). Worked
small-business run: [references/example-scorecard.md](references/example-scorecard.md).
**Default to the quick answer** when the ask is a plain "rate this" with no
stated stakes: one line (`X.X/10 — why + strongest evidence`) plus the top
fix, then offer the full scorecard. Full scorecard first when the user asks
for detail, a rubric, a comparison, or money rides on it.

## Self-check before delivering (all must pass)
- Weights shown, sum to 100%; rubric declared **before** any score.
- Overall recomputed as Σ(score × weight) to one decimal; Projected the same way.
  Run `python3 skills/jail-py-toolkit/scripts/score-check.py <scorecard.md>`
  (jail-py-toolkit). **Manual fallback:** multiply each score by its weight,
  add, round half-up to one decimal, compare to the headline.
- Every row has ≥1 evidence entry (numbered citation or explicit label); no bare adjectives.
- Every citation resolves in Sources (URL + date accessed) or the private-subject statement is present.
- Critical-flaw caps applied; current and projected never blended.
- No vendor/owner claim is labeled Fact without corroboration.
- Confidence stated, with the one action that would most raise it.
- Same subject + same evidence reproduces the same scores; a divergent re-run means re-examine the evidence.
One failed line = fix before delivering.

## Rating people — hard boundaries
Professional or public role only, from public verifiable evidence only. Never
private lives, character, protected attributes, health, habits, or rumor and
allegations. Decline those parts without repeating or scoring them; offer a
role-performance assessment (named role, documented outcomes). Thin evidence →
Low confidence. Full rules: [references/people-boundaries.md](references/people-boundaries.md).

## Delivery (client-facing)
When the rating goes to a client, render it as a clean document (docx skill or
Docs artifact when available; otherwise clean Markdown). Plain 9th-grade
English, short sentences, labels kept, no YAML in the client copy. The
JAIL-HANDOFF stays in the chat or working copy.

## Guardrails
Never blend current and potential. Rubric before scores. Uncited marketing
claims are claims, not evidence. State assumptions and unknowns. Failure
modes: [references/gotchas.md](references/gotchas.md).

## JAIL-HANDOFF
```yaml
JAIL-HANDOFF:
  skill: jail-rate
  status: complete | partial | blocked | stop
  facts: [..]
  assumptions: [..]
  unknowns: [..]
  outputs: [scorecard, rubric]
  evidence: [..]
  risks: [..]
  confidence: high | medium | low     # mirrors Self-check confidence
  next: jail-rate-skill | jail-prospect | jail-council | none
  approval_required: [..]
  checks:
    score-check.py: pass | fail | error | n/a
```
