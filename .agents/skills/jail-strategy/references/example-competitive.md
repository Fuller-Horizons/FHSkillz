# Worked example — COMPETITIVE lane

Synthetic client and rivals (no real firms). Official sources are real
program pages. This run did not pull the data series, so forces that rest on
them without client-side evidence are marked Unknown. That is the rule
working, not a gap in the example.

**Request:** "Run a five forces and competitor analysis for a residential HVAC
company in Suffolk County, NY that's thinking of adding commercial service."

## Scope (task contract, inline)
- **Subject:** Harbor Comfort HVAC (synthetic), residential install and repair, 14 staff.
- **Decision:** add light commercial service (small offices, retail, restaurants) within 12 months, or stay residential.
- **Lane:** COMPETITIVE. **Area:** Suffolk County, NY. **Horizon:** 12 months.
- **User-provided** (owner, call notes): about 70% of revenue is repeat residential customers; no single customer is over 2% of revenue; two techs hold the licenses and training needed for commercial rooftop units; no commercial service contracts today.
- **Assumption:** "light commercial" means small units under the owner's current van and tool setup. Larger systems are out of scope.

## Competitor set (tiers with reasons)
| Tier | Rival (synthetic) | Inclusion reason |
| :--- | :--- | :--- |
| Direct | Bayline Heating & Air | Same residential offer and same towns; has added a small commercial line |
| Direct | North Fork Climate | Same buyers; sells service plans to homeowners |
| Adjacent | Suffolk Commercial Mechanical | Commercial only; would meet Harbor Comfort on small-office jobs |
| Adjacent | Property-manager in-house techs | Substitute for outside service at multi-unit buildings |
| Aspirational | Island Facility Services | Large commercial maintenance firm; sets the bar for contract terms and response time |

Substitutes noted as a threat vector: building owners using in-house techs; ductless units installed by general contractors.

## Five Forces
| Force | Rating | Evidence (label) | What it means for the decision |
| :--- | :---: | :--- | :--- |
| New entrants | Unknown (searched: Census Business Formation Statistics for NY; no HVAC-specific series pulled) | (1) Licensing and training needed for rooftop units — User-provided, owner. (2) New business applications by state — series at census.gov/econ/bfs/index.html, **not pulled**. Resolve: pull the NY series [1]. | Cannot say yet whether commercial is easier to enter than it looks. |
| Supplier power | Unknown (searched: BLS Producer Price Index; no equipment series pulled) | (1) Owner buys equipment from two distributors — User-provided. (2) PPI series at bls.gov/ppi/ **not pulled** [2]. | Check equipment price trend before pricing commercial contracts. |
| Buyer power | Medium | (1) Residential: no customer over 2% of revenue — User-provided, owner (low buyer power today). (2) Commercial buyers are not yet in the book; Suffolk Commercial Mechanical and Island Facility Services sell by multi-year contract per their sites — Inference from 2 rival pages `[3][4]`; commercial buyers can compare bids | Commercial buyers will have more leverage than current homeowners. |
| Substitutes | Medium | (1) Property managers use in-house techs — User-provided, owner (two lost bids). (2) Ductless units installed by general contractors — Inference from rival pages `[3]`. | In-house teams cap what you can charge for routine service. |
| Rivalry | Unknown (searched: Census County Business Patterns, Suffolk County, NAICS 238220; not pulled) | (1) Bayline already advertises commercial service `[5]` — Fact. (2) Establishment counts at census.gov/programs-surveys/cbp.html **not pulled** [6]. | One direct rival is already moving. Count of rivals is Unknown. |

No overall industry score is given. The forces that drive this decision: **buyer power** and **substitutes**.

## Profile cards (one shown; others use the same layout)
## Bayline Heating & Air (synthetic)
- Tier: Direct — same towns and offer; added commercial line
- Positioning in their words: "Comfort for homes and small businesses"
- Named customers or proof: two named restaurant clients on their site — asserted (no corroboration found)

| Dimension | Score | Why | Source | Proven / asserted |
| :--- | :---: | :--- | :---: | :---: |
| Offer clarity | 4 | Separate residential and commercial pages with plans | [5] | proven (page content) |
| Proof and reviews | 2 | Reviews are residential; commercial claims uncorroborated | [5] | asserted |
| Service speed | Unknown | No response-time claim found | — | — |
| Price signal | Unknown | No public pricing | — | — |

- Where they are strong: clear packaging (Fact, source 5).
- Where they are exposed: thin commercial proof (Inference from the scores above).
- What we do not know: commercial customer count. Resolve with a call to two of their named clients.

## Implications for the decision
1. **Conditional go.** Add commercial through a small pilot, not a full launch. Basis: Harbor Comfort has two licensed techs (User-provided) and residential cash flow, and Bayline's commercial proof is thin (Inference).
2. **Target the flank:** small offices and restaurants where in-house techs do not exist. Avoid multi-unit property managers first (substitute risk).
3. **Before committing money:** pull the three Unknown series (entrants, input prices, rival counts) — 1 day of work. If Bayline holds commercial reviews above 4.5 and a response-time promise, reconsider.
4. **Watch-list:** Bayline commercial hires; Suffolk Commercial Mechanical entering small accounts; equipment price moves in the PPI series.
5. No market-size or revenue figure is used. A sizing number would need a cited source or an Estimate label.

## Sources
[1] U.S. Census Bureau, Business Formation Statistics, https://www.census.gov/econ/bfs/index.html [accessed 2026-11-12] (program page; series not pulled)
[2] U.S. Bureau of Labor Statistics, Producer Price Index, https://www.bls.gov/ppi/ [accessed 2026-11-12] (program page; series not pulled)
[3] Rival site notes, Suffolk Commercial Mechanical (synthetic), working copy
[4] Rival site notes, Island Facility Services (synthetic), working copy
[5] Rival site notes, Bayline Heating & Air (synthetic), working copy
[6] U.S. Census Bureau, County Business Patterns, https://www.census.gov/programs-surveys/cbp.html [accessed 2026-11-12] (program page; series not pulled)

## JAIL-HANDOFF (working copy; not in the client document)
```yaml
JAIL-HANDOFF:
  skill: jail-strategy
  status: partial
  facts:
    - "Bayline Heating & Air advertises commercial service [5]"
    - "Owner: about 70% repeat residential revenue, no customer over 2% (User-provided)"
  assumptions:
    - "Light commercial means small units within current van and tool setup"
  unknowns:
    - "New-entrant pressure: Census Business Formation Statistics for NY not pulled"
    - "Supplier power: BLS PPI equipment series not pulled"
    - "Rival count: Census County Business Patterns for Suffolk, NAICS 238220 not pulled"
    - "Bayline commercial customer count and response time"
  outputs:
    - "Tiered competitor table"
    - "Five Forces table (3 of 5 Unknown)"
    - "Profile card: Bayline"
    - "Implications: conditional go, pilot"
  evidence:
    - "Census BFS program page · new-entrant series · https://www.census.gov/econ/bfs/index.html · 2026-11-12"
    - "BLS PPI program page · input-price series · https://www.bls.gov/ppi/ · 2026-11-12"
    - "Census CBP program page · establishment counts · https://www.census.gov/programs-surveys/cbp.html · 2026-11-12"
  risks:
    - "Entry decision leans on three unpulled series"
  confidence: low
  next: jail-research
  approval_required: []
```
