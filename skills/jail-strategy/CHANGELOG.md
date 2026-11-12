# Changelog — jail-strategy-scan

## 1.3.1 — 2026-11-12
- Every rate, fee or market number, including those in worked examples, needs a source or an Estimate / "my assumption" label (blind test: an unsourced card-fee rate and a "32% effective commission" example). Untested.

## 1.3.0 — 2026-11-12 (plugin 0.27.0)

- New COMPETITIVE lane: tiered competitor set (Direct / Adjacent / Aspirational with inclusion reasons), Five Forces rated High/Medium/Low only from evidence (2+ items per force, else Unknown with what was searched), profile cards with a source per score, asserted-vs-proven tags, and no blended composite. Detail in `references/competitive-lane.md`. Pattern adapted from ECC (MIT).
- MACRO lane: official-source map per PESTLE dimension (FRED, BEA, BLS, Census, Federal Register, eCFR) in `references/macro-sources.md`.
- FULL SWEEP may now include COMPETITIVE, with competitive-structure shifts added to the interaction pass.
- Added a client-facing Delivery section (clean document, plain English, handoff kept in the working copy).
- Strengthened task-contract step: no named decision means ask or state the scope as an assumption; user-supplied SWOT lists are sorted by the rules and changes reported.
- Canonical claim labels (Fact, User-provided, Inference, Estimate, Judgment, Unknown); legacy labels removed.
- Description cut to under 450 characters and now routes "five forces", "competitor analysis", "competitive landscape". Dropped phrases: "strengths and weaknesses", "where do we stand competitively", "PESTEL", "external factors affecting X" (now "external factors"), and the market-entry/investment sentence; the SWOT/PESTLE trigger cases (k14, k15, w1-w3) still match on SWOT, PESTLE, macro trends, and full strategy picture.
- Added `references/example-competitive.md` worked run with JAIL-HANDOFF; SUCCESS-TEST extended.

## 1.2.0 — 2026-07-25 (plugin 0.25.0)

- Added a SUCCESS-TEST pre-ship checklist (S/W evidence+materiality+
  confidence, O/T mechanism, MACRO decision-link, TOWS/implications
  traceability, tripwires, dated sources) plus a new `references/example.md`
  worked FULL SWEEP mini-example showing it applied — closes the "looked
  done but wasn't checked" gap before handoff.
- Added a Gotchas entry on sensitive inputs: mark CONFIDENTIAL sources in
  the appendix, never fabricate a specific to fill an evidence gap, fail
  closed on unsourced materiality.
- Added a fixed tie-break rule to INTERNAL and MACRO classify (file by the
  more proximate causal mechanism; never split/duplicate across two
  quadrants or dimensions) and a canonical table sort (materiality/magnitude
  descending, then alphabetical) so re-runs on identical evidence reproduce
  identical tables.

## 1.1.0 — 2026-07-22 (plugin 0.24.0)

- **Renamed jail-strategy-scan → jail-strategy.** Same three-lane strategy skill (INTERNAL SWOT→TOWS / MACRO PESTLE+tripwires / FULL SWEEP); shorter name. Cross-references updated; history preserves the jail-strategy-scan lineage.

## 1.0.0 — 2026-07-22 (plugin 0.23.0)

Initial release as the merger of **jail-swot 1.1.0** and **jail-pestle
1.1.0** (both retired this release; full lineage in their histories in git).

- Three lanes: INTERNAL (SWOT+TOWS) · MACRO (PESTLE+tripwires) · FULL SWEEP
  (both + interaction pass).
- Carried forward intact: SWOT sorting rules (internal+evidenced+controlled
  vs external+specific-mechanism, symptom-vs-root-cause, one-point-one-
  quadrant, materiality+confidence per entry), mandatory TOWS; PESTLE
  factor fields (trend/likelihood/magnitude/time-to-impact/O-T/confidence),
  materiality cut line, honest empty cells, mandatory tripwires.
- New in the merge: single shared evidence sweep (kills duplicate research
  cost), the cross-lane interaction pass (macro factor flips internal
  entry), tripwires handed to jail-memory as monitored entries.
