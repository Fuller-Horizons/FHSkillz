# JAIL-RESEARCH: Is the number of landscaping businesses in Suffolk County, NY growing or shrinking?

## Part 1: Synthesized answer

**I can't tell you yet. The Suffolk County trend is Unknown (until searched), and I would not put a direction in a client deck on what I have.**

- **What blocked me:** Every Suffolk-specific result was a business-for-sale listing, a company directory, or a paywalled IBISWorld page. None gave a county establishment count over time.
- **My direct Census API calls were blocked.** One needed a permission approval and the other was refused by the proxy. No Census page or table was opened this session.
- **Nothing below is cited as a source I opened [Rule 10].** The search tool returned only summaries, and I did not open the underlying pages.

Search summaries mentioned the following. Treat each as **unverified, secondhand**:

- **Statewide:** IBISWorld is said to estimate about 47,656 landscaping businesses in New York, growing about 3.0% a year from 2021 to 2026. That is a paid-vendor model, not a count.
- **National:** Census County Business Patterns (CBP) 2023 is said to show 117,969 employer establishments in NAICS 561730. A separate figure of 516,572 firms with no employees is attributed to Census Nonemployer Statistics.
- **Why neither answers your question:** They are not Suffolk figures. The employer and no-employee counts also cover different populations. A vendor model and a Census count should not be mixed.

I would not infer Suffolk's direction from the statewide or national numbers. That would be a Judgment, not evidence.

## Part 2: Evidence packet

```
EVIDENCE PACKET
Objective + consuming decision: Direction of landscaping-business count in
  Suffolk County, NY, for a client deck (what the deck decides: not stated).
Questions:
  Q1: Did Suffolk County's NAICS 561730 employer-establishment count rise or
      fall over recent years?
      Answer: Unknown (until searched). Confidence: n/a
      Evidence: none opened this session.
      Contradictions/limitations: Search returned listings and paywalled
      pages only. Volatile-class freshness window (≤12 months) cannot be
      applied because there is no source.
  Q2: How many no-employee landscaping firms are in Suffolk, and are they
      growing?
      Answer: Unknown (until searched). Confidence: n/a
Cross-cutting findings: Employer and no-employee counts must be reported
  separately. They cover different populations.
Unresolved gaps (+ resolver):
  G1 Suffolk employer establishments by year -> Census County Business
     Patterns API, state 36, county 103, NAICS 561730, multiple years
     (free; this call was blocked in this session).
  G2 Suffolk no-employee firms -> Census Nonemployer Statistics, same filter.
  G3 Employment/wage trend as a cross-check -> BLS Quarterly Census of
     Employment & Wages, Suffolk, NAICS 561730.
Source list (numbered, dated): none cited. Pages not opened this session.
```

Because no sources are cited, the pre-ship check passes trivially. The one real gap is that Q1 and Q2 have no answer.

## How to close this

- **Option A:** Approve a single `curl` call to the Census CBP API (free, no key at this volume). I'll pull 2017 to 2023 for Suffolk and chart it.
- **Option B:** Run the query yourself on data.census.gov (county FIPS 36103, NAICS 561730) and paste me the table.

A Census change in industry coding (NAICS 2017 to 2022) can break year-over-year comparisons. If I pull the data, I'll flag that in the packet.

```
JAIL-HANDOFF
status: blocked-on-data
next: jail-research (re-run after CBP pull) -> jail-summarize for the deck
approval_required: Census API call (curl) or user-supplied table
open_unknowns: G1, G2, G3
```