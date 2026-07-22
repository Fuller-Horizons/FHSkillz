---
name: jail-strategy-scan
metadata:
  version: 1.0.0
description: >-
  One evidence-grounded strategy analysis with three lanes — INTERNAL (SWOT
  with enforced sorting rules → TOWS strategy combinations), MACRO (PESTLE:
  Political/Economic/Social/Technological/Legal/Environmental factors scored
  and tied to a decision, each with an early-warning tripwire), or FULL SWEEP
  (both + cross-lane interactions). Use when asked for "SWOT", "TOWS",
  "strengths and weaknesses", "where do we stand competitively", "PESTLE",
  "PESTEL", "macro-environment analysis", "external factors affecting X", or
  a full strategic-landscape read before a market entry, investment, or
  planning cycle. Do NOT use for business-model design (jail-bmc), rating a
  named subject 0-10 (jail-rate), or bare evidence-gathering with no
  strategy output (jail-research).
---

# JAIL-STRATEGY-SCAN

Successor to jail-swot + jail-pestle (merged 0.23.0 — one entry point, shared
evidence base, no duplicate research). The two failure modes it exists to
kill: **wishful sorting** (aspirations filed as strengths, market weather
filed as opportunity) and **trend listicles** (macro factors with no link to
a decision).

## Lane pick (say which)
- **INTERNAL** — subject-controlled capabilities vs external conditions →
  SWOT + TOWS. For "where do we stand / what should we do about it".
- **MACRO** — environment scan for a defined subject + decision → six
  PESTLE dimensions + tripwires. For "what's coming at us".
- **FULL SWEEP** — both lanes off one evidence base + the interaction pass.
  Default when the ask is "the whole strategy picture".

## Chain (both lanes share 1–2, 6–8)
1. **jail-task-contract** — pin subject, the decision this serves, scope,
   geography/industry, horizon. No decision named = scope smell; ask.
   *(Fallback: capture inline.)*
2. **jail-research** — ONE evidence sweep serving both lanes: internal
   record (results, capabilities, churn, delivery) + external (market,
   competitors, regulation, macro). Tiered dated sources; user-provided
   facts labeled. *(Fallback: cite-or-label per the constitution.)*
3. **INTERNAL classify** — sorting rules enforced:
   - **S/W = internal + evidenced + controlled.** An aspiration is not a
     strength; a known unfixed defect is a weakness even when uncomfortable.
   - **O/T = external + specific mechanism for THIS subject.** "Market is
     growing" qualifies only with the link.
   - Symptom vs root cause: classify the evidenced cause, not the symptom.
   - One point, one quadrant; per entry: statement · evidence ref ·
     materiality (H/M/L) · confidence.
4. **MACRO classify** — per factor: finding (Fact/Inference/Estimate) ·
   evidence ref · trend direction · likelihood (H/M/L) · magnitude (H/M/L) ·
   time-to-impact (<1y / 1–3y / 3y+) · opportunity-or-threat · confidence.
   No defensible link to the decision = cut, not kept for completeness.
   Empty dimension = "nothing material found (searched: …)", never filler.
5. **Interaction pass (FULL SWEEP)** — macro factors that flip internal
   entries (a Legal shift that expires a Strength; an Economic turn that
   converts a Weakness into a W×T vulnerability); cross-dimensional macro
   interactions.
6. **jail-red-team** — attack the sort: flattering misclassifications, the
   competitor nobody named, expired strengths, true-but-immaterial factors,
   survivorship in sources. *(Fallback: three lenses inline.)*
7. **Strategy step (mandatory — boxes alone are inventory):**
   - INTERNAL → **TOWS**: S×O · W×O · S×T · W×T (the vulnerability list),
     2–4 per cell, each traceable to specific entries.
   - MACRO → strategic implications + priority actions for the decision,
     plus **tripwires**: every high-magnitude factor gets its observable
     early-warning indicator (hand to jail-memory as monitored entries so
     future sessions check them).
8. **jail-decide** → strategic choices; **jail-exec-brief** for voice;
   **jail-verify** (rules held, entries evidenced/labeled, TOWS/tripwires
   traceable, gaps declared).

## Output
Scope + lane + horizon → classified tables (per lane, fields above) →
interactions (full sweep) → vulnerabilities (W×T) → TOWS strategies and/or
implications + priority actions → tripwires → validation requirements →
dated sources appendix → JAIL-HANDOFF block.

## Gotchas
- **Aspirations as strengths / weather as opportunity.** Demonstrated and
  mechanism-linked, or cut. The sorting rules are the skill.
- **Trend listicle drift.** A factor that survives with no decision link
  means step 1 was skipped.
- **Quadrant duplication.** Same fact as S and O double-counts; pick where
  it's causal.
- **Boxes without strategy.** TOWS / implications are mandatory; a scan
  that can't say "so do this" isn't finished.
- **Missing tripwires.** Analysis that can't tell the reader what to WATCH
  is a photo, not a forecast.
- **Double research.** Running separate sweeps per lane duplicates cost —
  one evidence base serves both; that's why the merge exists.
