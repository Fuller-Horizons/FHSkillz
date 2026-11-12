# Spec — jail-strategy (1.2.0 → 1.3.0) · now 8.0 → target 9.1

Changes
1. New lane **COMPETITIVE** (pattern adapted from ECC competitive-platform-analysis + benchmark-methodology): (a) scope the competitor set — Direct / Adjacent / Aspirational tiers with inclusion reasons; (b) industry structure via Porter's Five Forces, each force rated High/Medium/Low only from evidence (concentration from Census CBP/Economic Census, new-entrant pressure from Census Business Formation Statistics, input-price pressure from BLS PPI, buyer power from the client's customer concentration, substitutes from customer research) — 2+ evidence items per force or the force is "Unknown (searched: …)"; (c) competitor profile cards scored per dimension with source per score, asserted-vs-proven tagging, no blended composite. Full detail in `references/competitive-lane.md`; the core keeps the lane pick, the evidence-per-force rule, and the bias rules.
2. MACRO lane: add a source map line per PESTLE dimension pointing to official sources (FRED, BEA, BLS, Census, Federal Register/eCFR) in `references/macro-sources.md`.
3. FULL SWEEP may include COMPETITIVE.
4. Client-facing Delivery section.
5. Canonical labels; description ≤ 450 (currently 759) and must now also route "Porter / five forces / competitor analysis / competitive landscape"; core ≤ 160 lines.
Client-facing: yes.

Test scenarios
S1 competitive: "Run a five forces and competitor analysis for a residential HVAC company in Suffolk County, NY that's thinking of adding commercial service." (web allowed)
  [O] each of the five forces has a rating AND at least one cited piece of evidence, or is marked Unknown
  [O] competitors are grouped into tiers (direct/adjacent/etc.) with a reason
  [O] ends with actionable strategic implications tied to the decision (add commercial service or not)
  [O] no market-size or revenue figure appears without a source or an Estimate label
S2 SWOT discipline: user lists "strengths: we want to be the premium brand; the market is growing" for a SWOT.
  [O] does not file the aspiration ("want to be premium") as a Strength
  [O] does not file generic market growth as an Opportunity without a mechanism for this company
S3 macro without decision: "Do a PESTLE on the US economy."
  [O] asks for / pins the decision the scan serves, or scopes it explicitly, rather than producing an unlinked trend list
