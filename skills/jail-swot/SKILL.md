---
name: jail-swot
metadata:
  version: 1.1.0
description: >-
  Produce an evidence-grounded SWOT that cleanly separates internal
  capabilities (Strengths/Weaknesses) from external conditions
  (Opportunities/Threats), then converts it into TOWS strategy combinations
  and recommended actions. Use when asked for "SWOT", "strengths and
  weaknesses", "where do we stand competitively", or a strategic self-
  assessment feeding a plan. Do NOT use for macro-environment scans
  (jail-pestle feeds the O/T side), business-model design
  (jail-bmc), or rating a product 0-10 (jail-rate).
---

# JAIL-SWOT

The failure mode of every SWOT is wishful sorting — aspirations filed as
strengths, market weather filed as company-specific opportunity. This skill
sorts by evidence and ships strategy (TOWS), not just quadrants.

## Chain
1. **jail-task-contract** — pin the subject, the decision this SWOT serves,
   scope (whole org vs product vs market), and horizon. *(Fallback: capture
   inline.)*
2. **jail-research** — where evidence is incomplete: internal evidence
   (results, capabilities, churn, delivery record) and external evidence
   (market, competitors, regulation — a prior jail-pestle slots in
   here). Dated citations; user-provided facts labeled as such.
3. **Classify — with the sorting rules enforced:**
   - **Strength/Weakness = internal + evidenced.** Demonstrated capability
     or deficit the org *controls*, backed by results — an aspiration
     ("we will be the premium option") is not a strength; an unfixed known
     defect is a weakness even when uncomfortable.
   - **Opportunity/Threat = external + specific.** A condition of the
     environment with a stated mechanism for THIS subject — "the market is
     growing" only qualifies with the link ("…and our licensure is the
     entry barrier competitors lack").
   - **Symptom vs root cause:** "losing deals" is a symptom; classify the
     evidenced cause ("no mid-market pricing tier").
   - One point, one quadrant — duplicates across quadrants get merged.
   - Per entry: statement · evidence ref · **materiality** (H/M/L) ·
     confidence.
4. **jail-red-team** — attack the sort: flattering misclassifications,
   missing threats (the competitor nobody named), strengths that expired.
5. **TOWS combinations** — the strategy step most SWOTs skip:
   **S×O** (use strengths to capture opportunities) · **W×O** (fix
   weaknesses that block opportunities) · **S×T** (use strengths to blunt
   threats) · **W×T** (defend where weakness meets threat — the
   vulnerability list). 2–4 per cell, each traceable to specific entries.
6. **jail-decide** — from TOWS to strategic choices + recommended actions.
7. **jail-exec-brief** → **jail-verify** (sorting rules held? every entry
   evidenced or labeled? TOWS traceable? vulnerabilities named?).

## Output
Scope → prioritized SWOT matrix (entries with evidence + materiality +
confidence) → key vulnerabilities (W×T) → TOWS strategies → strategic
choices + recommended actions → validation requirements (what to test
before betting on this). Sources appendix. JAIL-HANDOFF block.

## Gotchas
- **Aspirations as strengths.** "Committed leadership team" with no
  evidenced outcome. Demonstrated or it moves to unknowns.
- **Weather as opportunity.** Generic market growth without the
  subject-specific mechanism. State the link or cut it.
- **Quadrant duplication.** The same fact appearing as S and O (or W and T)
  double-counts it. Merge; pick the quadrant where it's causal.
- **SWOT without TOWS.** Four boxes and no strategy is inventory, not
  analysis. Step 5 is mandatory.
- **Comfortable omissions.** The weakness everyone knows and nobody wrote.
  jail-red-team's pass exists to catch the missing uncomfortable entry.
