# Worked example — landscaping firm trend, Suffolk County NY

Input (synthetic request): "Is the number of landscaping businesses in
Suffolk County, NY growing or shrinking? I need it for a client deck. Our
client says there are about 2,000 of them." Web search was available, but the
statistical tables could not be opened in this run (the pages loaded as
descriptions only, not data), so figures are Unknown, not recalled.

## PART 1 — SYNTHESIZED ANSWER

**Short answer: this run cannot say whether the count is growing or
shrinking, and the deck should not claim a direction yet.** The two official
sources that can answer it are known, and the exact tables to pull are named
below.

Landscaping services have their own industry code (NAICS 561730), so the
count can be isolated by county [3]. The Census Bureau's County Business
Patterns reports establishments with paid employees, by industry and county,
once a year [1] (Fact). The Nonemployer Statistics program reports the
businesses with no paid employees, which matters because many landscapers
are one-person firms [2] (Fact). The BLS quarterly wage series gives a second
count of establishments by industry and county [4] (Fact).

The client's number, "about 2,000," is User-provided (stated by the client,
not checked). It does not say which population it covers (employer firms,
non-employer firms, or both) or which year. If it covers only employer
firms, a total that includes non-employers would be larger, so the two could
not be compared as-is (Inference, from [1] and [2] covering different
populations).

Trend direction: Unknown. Compare the same NAICS code, the same county, and
the same population across at least three consecutive years from [1], then
check that direction against [4]. Vintage rule applied: slow-moving
structure, so data up to 3 years old is acceptable; newer is better.

## PART 2 — EVIDENCE PACKET

```
EVIDENCE PACKET
Objective + consuming decision: Direction of the landscaping-business count
in Suffolk County NY over recent years, for a client deck claim.
Questions:
  Q1: Which official source counts landscaping employer establishments by county?
      Answer: County Business Patterns, NAICS 561730, county level — Fact · high
      Evidence: [1] CBP program page · defines coverage (establishments with
        paid employees, by industry and geography) · 2026-11-12
      Contradictions/limitations: excludes firms with no paid employees.
  Q2: Which source covers the firms with no paid employees?
      Answer: Nonemployer Statistics — Fact · high
      Evidence: [2] NES program page · counts and receipts of businesses with
        no paid employees · 2026-11-12
      Contradictions/limitations: separate program; years and codes must be
        matched to Q1 before adding.
  Q3: Is the Suffolk County count rising or falling, and does the client's
      "about 2,000" hold?
      Answer: Unknown — the tables were not opened this run. The client's
        figure is User-provided and its population and year are unstated.
      Evidence: [3] NAICS lookup · confirms the industry code scheme · 2026-11-12;
        [4] BLS QCEW · second county-by-industry count for cross-checking · 2026-11-12
      Contradictions/limitations: none found yet; nothing to reconcile until
        figures are retrieved.
Cross-cutting findings: the three-way gap (employer, non-employer, client
  definition) is the likeliest source of any later disagreement.
Unresolved gaps (+ what would resolve each):
  - Counts by year: open CBP, filter NAICS 561730, Suffolk County NY, last 3+ years.
  - Non-employer counts: open NES, same filters.
  - Client's 2,000: ask the client for the source, year, and definition.
Source list (numbered, dated):
```

### Sources

1. U.S. Census Bureau, County Business Patterns — https://www.census.gov/programs-surveys/cbp.html [accessed 2026-11-12]
2. U.S. Census Bureau, Nonemployer Statistics — https://www.census.gov/programs-surveys/nonemployer-statistics.html [accessed 2026-11-12]
3. U.S. Census Bureau, NAICS — https://www.census.gov/naics/ [accessed 2026-11-12]
4. BLS, Quarterly Census of Employment and Wages — https://www.bls.gov/cew/ [accessed 2026-11-12]

## Delivery

For the client deck, the answer goes out as a clean document in plain
English with labels kept and no YAML. The line to use today: "The direction
is not yet confirmed; the Census and BLS tables will settle it."

## Handoff

```yaml
JAIL-HANDOFF:
  skill: jail-research
  status: partial
  facts:
    - "CBP covers employer establishments by NAICS and county [1]"
    - "NES covers firms with no paid employees [2]"
  assumptions:
    - "Client's 2,000 is User-provided; population and year unknown"
  unknowns:
    - "Suffolk NAICS 561730 count by year (resolver: CBP, NES, QCEW tables)"
    - "Source and definition of the client's 2,000 (resolver: ask client)"
  outputs: ["synthesized answer", "evidence packet"]
  evidence:
    - "[1] Census CBP page · coverage · https://www.census.gov/programs-surveys/cbp.html · 2026-11-12"
    - "[2] Census NES page · coverage · https://www.census.gov/programs-surveys/nonemployer-statistics.html · 2026-11-12"
  risks: ["Deck claim of growth or decline would be unsupported until tables are pulled"]
  confidence: low
  next: "retrieve the tables, then jail-verify before the deck ships"
  approval_required: []
  checks:
    cite-check.py: pass
    label-lint.py: pass
```
