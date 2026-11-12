## Answer: Suffolk County's direction is Unknown. Don't put a trend on the client slide yet.

I could not find a Suffolk County count for landscaping businesses in any source I could open. The official Census County Business Patterns (CBP) and BLS data for Suffolk were blocked: the API call needed approval and the proxy refused the fetches. Everything below comes from search-result excerpts I did not open, so treat it as unverified.

- **Suffolk County:** No figure found. The only county-level data is IBISWorld's paywalled report, which lists Suffolk establishment counts [1].
- **New York State:** IBISWorld estimates about 47,656 landscaping businesses, growing about 3.0% a year from 2021 to 2026 [1]. This is a vendor estimate, not a count, and it does not split out Suffolk.
- **United States:** IBISWorld's own figures conflict. One excerpt gives 692,777 businesses in 2025, up 4.8% [2]. Another gives 556,238 in 2026, up 1.8%, but down about 2% a year on average over 2021–2026 [2]. The evidence splits, so neither figure should go on a slide.
- **Census 2023 (secondary):** About 117,969 employer landscaping establishments and 516,572 nonemployer businesses nationally. A third-party site computed these from Census data [3].

**What would settle it:** Pull the Census CBP series for NAICS 561730, Suffolk County (FIPS 36103), for 2017–2023, plus the Nonemployer Statistics for the same filter, from data.census.gov. Cross-check with the BLS QCEW Data Viewer for Suffolk, NAICS 561730. Compare at least five years. Once you paste the table here, I'll compute the trend and label it User-provided until a source confirms it.

**Suggested slide wording until then:** "Suffolk County landscaping establishment trend: pending Census CBP pull (NAICS 561730)."

---

### Part 2: Evidence packet

```
EVIDENCE PACKET
Objective + consuming decision: Is the number of landscaping businesses in Suffolk County, NY growing or shrinking? Needed for a client deck (direction and magnitude).
Questions:
  Q1: Suffolk County landscaping establishment trend (NAICS 561730), last 5 years?
      Answer: Unknown — no Suffolk-specific count was retrievable this session. · confidence: n/a
      Evidence: none opened. Census CBP API and BLS QCEW fetches blocked (approval required / proxy refused).
      Contradictions/limitations: Only paywalled county data found.
  Q2: New York State landscaping business trend, 2021–2026?
      Answer: Vendor estimate of growth ~3.0%/yr 2021–2026 for ~47,656 businesses — Estimate · confidence: low (vendor, unopened, paywalled)
      Evidence: [1] IBISWorld, NY Landscaping Services profile · excerpt only · https://www.ibisworld.com/us/industry/new-york/landscaping-services/12155/ · accessed 2026-11-12
      Contradictions/limitations: Estimate, not a count. Freshness window applied: slow-moving (≤3–5 yrs). No NY-level Census count was retrieved.
  Q3: US landscaping business trend?
      Answer: Evidence splits. IBISWorld gives 692,777 (2025, +4.8%) [2] and 556,238 (2026, +1.8%; −2.0%/yr avg 2021–2026) [2]. The vendor's own figures conflict. · confidence: low
      Evidence: [2] IBISWorld, Landscaping Services in the US – Number of Businesses · excerpts only · https://img2.ibisworld.com/united-states/number-of-businesses/landscaping-services/1497/ · accessed 2026-11-12
      Contradictions/limitations: Same vendor, two incompatible levels. Volatile freshness window (≤12 months) applied to the 2026 figure.
  Q4: Official US employer and nonemployer counts, 2023?
      Answer: ~117,969 employer establishments and 516,572 nonemployer businesses (2023), per third-party computation from Census data · confidence: medium (secondary, not verified against Census)
      Evidence: [3] startbusinessbystate.com, Service nonemployer share by state (CBP 2023 + NES 2023) · excerpt only · https://startbusinessbystate.com/service-nonemployer-share-by-state/ · accessed 2026-11-12
      Contradictions/limitations: Secondary and self-computed. Not used for a trend.

Cross-cutting findings: No source opened this session supports a Suffolk-specific direction. Direction is Unknown.
Unresolved gaps (+ what would resolve each):
  - Suffolk establishment trend, NAICS 561730, 2017–2023 → Census CBP at data.census.gov (county FIPS 36103), and BLS QCEW Data Viewer. Run by user or re-run with API access approved.
  - Suffolk nonemployer trend → Census Nonemployer Statistics, same filter.
  - Reconciling IBISWorld's conflicting US figures → Census CBP national totals for NAICS 561730.
Source list (numbered, dated):
  [1] IBISWorld, Landscaping Services in New York — NY count/growth estimate — https://www.ibisworld.com/us/industry/new-york/landscaping-services/12155/ — accessed 2026-11-12
  [2] IBISWorld, Landscaping Services in the US – Number of Businesses — US counts, conflicting — https://img2.ibisworld.com/united-states/number-of-businesses/landscaping-services/1497/ — accessed 2026-11-12
  [3] startbusinessbystate.com, Service nonemployer share by state — 2023 national counts — https://startbusinessbystate.com/service-nonemployer-share-by-state/ — accessed 2026-11-12

Risks: No agent-directed text was found in the excerpts. An unattributed BLS-style claim (businesses +1.9% to 124,018 in early 2026) appeared without a source and was excluded.
```

JAIL-HANDOFF
- `next`: jail-research (re-run Q1 once the Census CBP table is available), then jail-summarize for the client-ready slide text.
- `open_items`: Suffolk trend (Unknown), IBISWorld US conflict, Census API access.