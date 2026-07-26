# Worked example — FULL SWEEP mini-example

Load this when checking the SUCCESS-TEST against a real run. Trimmed to a
few entries per table; a real sweep has more, but the shape and the
checklist walk-through below are the point.

**Subject:** Northwind Filtration (mid-size industrial water-filtration
manufacturer). **Decision:** enter the EU commercial water-filtration
market within 18 months. **Lane:** FULL SWEEP. **Horizon:** 18 months.

## INTERNAL — SWOT (excerpt)

| Quadrant | Statement | Evidence ref | Materiality | Confidence |
| :--- | :--- | :---: | :---: | :---: |
| S | ISO 14001-certified manufacturing, cited as a met requirement in 3 of 5 lost EU RFPs | [1] | H | H |
| W | Two core EU-relevant patents expire in France in 14 months, inside the entry horizon | [2] | H | H |
| O | New EU wastewater discharge directive raises the compliance bar, lifting demand for pre-compliant vendors [mechanism: directive → mandatory upgrade cycle → RFPs] | [3] | H | M |
| T | Two incumbents hold 60% EU share on long-term utility contracts [mechanism: entrenched contracts block near-term displacement] | [4] | M | M |

*Tie-break applied:* the patent-expiry fact could read as S (portfolio
exists) or W (protection lapsing in-window) — filed **W**: the more
proximate causal mechanism for this decision is the imminent loss of
protection, not the portfolio's existence.

## MACRO — PESTLE (excerpt)

| Dim | Finding | Evidence ref | Trend | Likelihood | Magnitude | Time-to-impact | O/T | Confidence |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Legal | EU single-use-plastics directive tightens cartridge-packaging rules | [5] | Tightening | H | H | <1y | T | H |
| Economic | EU industrial water-treatment capex forecast +6%/yr through 2029 | [6] | Rising | M | M | 1–3y | O | M |
| Political | *nothing material found (searched: EU trade-policy shifts affecting filtration imports)* | — | — | — | — | — | — | — |

*Tie-break applied:* the packaging rule could read as Legal or
Environmental — filed **Legal**: the proximate mechanism is the directive's
compliance mandate, not the underlying environmental policy goal.

*Table sort applied:* both tables sort materiality/magnitude descending,
then alphabetical within a tier — S before W at materiality H; Legal before
Economic since H outranks M.

## Interaction pass
The Legal tightening [5] raises compliance cost on the same cartridge line
the Economic growth trend [6] is expanding demand for — flagged as a
priority action (capex growth [6] outweighs the per-unit compliance cost
[5]), not a wash.

## TOWS (excerpt)

| Cell | Strategy | Traces to |
| :--- | :--- | :--- |
| S×O | Lead EU RFPs with the ISO 14001 certification against the new discharge directive | S[1] × O[3] |
| W×T | Do not anchor a France launch before the patent question resolves — incumbents will contest | W[2] × T[4] |

## Tripwires
- Legal[5] (magnitude H): monitor the EU packaging-directive
  enforcement-guidance publication date — hand to jail-memory as a
  monitored entry.

## Sources (dated)
[1] Northwind ISO 14001 cert record, accessed 2026-06-02.
[2] Northwind patent docket (EUIPO), accessed 2026-06-02.
[3] EU wastewater discharge directive text, published 2026-03-10, accessed 2026-06-03.
[4] AquaTec/Filtrion contract disclosures, accessed 2026-06-03.
[5] EU single-use-plastics directive, published 2025-11-01, accessed 2026-06-03.
[6] EU water-treatment capex forecast, industry report, published 2026-01, accessed 2026-06-03.

## SUCCESS-TEST walk-through
- S/W evidence-ref + materiality + confidence: S and W rows both carry
  [1]/[2] and H/H — present.
- O/T mechanism stated: O and T rows both carry a bracketed
  `[mechanism: …]` clause — present.
- Kept MACRO factor has decision-link or is cut: Legal[5] and Economic[6]
  both link to the EU-entry decision via the interaction pass; Political
  is cut with the searched-terms note, not kept for completeness.
- TOWS traceable: both cells above cite their source entries by ref.
- High-magnitude factor has a tripwire: Legal[5] (magnitude H) has one;
  Economic[6] (magnitude M) does not need one.
- Sources dated: all six entries carry a publish or accessed date.
