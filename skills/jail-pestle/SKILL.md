---
name: jail-pestle
metadata:
  version: 1.1.0
description: >-
  Produce an evidence-grounded PESTLE analysis (Political, Economic, Social,
  Technological, Legal, Environmental) for a defined organization, market, or
  decision — every factor cited, scored for likelihood/magnitude/time-to-
  impact, and tied to the decision it serves. Use when asked for "PESTLE",
  "PESTEL", "macro-environment analysis", "external factors affecting X", or
  strategic-landscape scans for a market entry, investment, or planning
  cycle. Do NOT use for internal-capability analysis (jail-swot), a
  business-model design (jail-bmc), or generic trend listicles
  with no defined subject and decision.
---

# JAIL-PESTLE

A PESTLE is only useful when every factor has a defensible relationship to a
**specific subject and decision** — otherwise it's a macro-trend listicle.
This skill chains the JAIL kernel; where a named skill isn't installed,
apply its rule inline (noted per step).

## Chain
1. **jail-task-contract** — pin: subject organization/initiative/market,
   geography, industry, the strategic question/decision, time horizon,
   constraints. Missing any of these = ask; a PESTLE without a decision is a
   scope smell. *(Fallback: capture those six fields yourself.)*
2. **jail-research** — evidence sweep per dimension, tiered sources, dated
   citations, contradictions preserved. *(Fallback: cite-or-label per the
   constitution.)*
3. **Classify findings** into the six dimensions. Per factor record:
   finding (labeled Fact/Inference/Estimate) · evidence ref · **trend
   direction** (rising/stable/declining) · **likelihood** (H/M/L) ·
   **magnitude of impact** on the subject (H/M/L) · **time to impact**
   (near <1y / mid 1–3y / long 3y+) · **opportunity or threat** · confidence.
   A factor with no defensible link to the subject's decision is cut, not
   kept for completeness.
4. **jail-red-team** — attack the classification: missing stakeholders,
   survivorship in the sources, factors that are true but immaterial,
   **cross-dimensional interactions** (a Legal shift that flips an Economic
   factor). *(Fallback: run the three lenses inline.)*
5. **jail-decide** — translate surviving factors into strategic
   implications and priority actions for the stated decision.
6. **jail-exec-brief** — final voice, leading with the answer.
7. **jail-verify** — checks before shipping: every factor cited or labeled,
   six dimensions covered *or* an explicit "nothing material" per empty
   dimension, scores consistent with evidence, gaps declared.

## Output
Scope + horizon → findings tables by dimension (factor · trend ·
likelihood · magnitude · time · O/T · confidence · evidence) →
cross-dimensional interactions → evidence gaps → strategic implications →
priority actions → **early-warning indicators** (the observable that says a
factor is materializing — each factor's tripwire). Sources appendix, dated.
JAIL-HANDOFF block closes it.

## Gotchas
- **Trend listicle drift.** "AI is growing" with no link to the subject's
  decision. The materiality test is step 3's cut line.
- **Six-boxes compulsion.** Padding an empty dimension with filler.
  "Nothing material found (searched: …)" is the honest cell.
- **Uncited macro claims.** GDP figures, regulation timelines, adoption
  stats — all carry a dated source or an Estimate label.
- **Static snapshot.** No trend direction or time-to-impact = a photo, not
  a forecast. Both fields are mandatory per factor.
- **Missing tripwires.** Analysis that can't tell the reader what to WATCH
  wasn't finished. Every high-magnitude factor gets its indicator.
