# Free, Authoritative Sources — US Private Company Research

[checked 2026-11-12] — each URL below was opened with WebFetch on that date. Link status is in the
"Link check" column; "not confirmed" means the fetch tool could not open it (blocked, robots, or
JavaScript-only), NOT that the link is dead. Open those by hand before relying on them.

Use in tier order. Prefer Tier 1 for any consequential claim; cross-check anything
that drives a score across 2+ independent sources. Everything here is free to access.

## Tier 1 — Primary / official (government)
| Source | URL | What it gives you | Best for |
|---|---|---|---|
| State Secretary of State business registry | (per state, e.g. sos.state.xx.us; not checked) | Legal name, status/good standing, **formation date**, officers, registered agent, amendments | Entity resolution, owner tenure, succession timing |
| SEC EDGAR | https://www.sec.gov/search-filings | Filings incl. **Form D** (private placements), any public parent | Funding signals, ownership |
| SAM.gov | https://sam.gov | Federal registration, UEI/CAGE, NAICS, socio-economic status | Fed-contractor status, size |
| USAspending.gov | https://www.usaspending.gov | Federal award history + $ amounts | Revenue floor (federal portion) |
| Federal contract awards (FPDS data, now searched in SAM.gov) | https://sam.gov/contracting | Detailed federal contract actions. FPDS.gov redirects here and its ezSearch was retired | Contract concentration |
| USPTO trademark search (replaces TESS) / patent search | https://tmsearch.uspto.gov/ , https://www.uspto.gov | Trademarks, patents | IP assets, brand value, age |
| State UCC filing search | (per state SOS) | **Liens / secured debt**, lenders, equipment financing; lien releases | Debt load, distress vs. clean-exit signals |
| PACER + state court portals | https://pacer.uscourts.gov | Litigation, **bankruptcy** | Risk, distress |
| OSHA Establishment Search | https://www.osha.gov/ords/imis/establishment.html | Inspections, violations | Compliance exposure (consulting) |
| EPA ECHO | https://echo.epa.gov | Environmental compliance/violations | Risk, consulting |
| DOL WHD / enforcement data | https://www.dol.gov/agencies/whd/data (links to the DOL Enforcement Database; enforcedata.dol.gov now redirects to data.dol.gov) | Wage/hour violations | Risk, consulting |
| Census Economic Census, Nonemployer Statistics, SUSB, CBP / BLS | see `size-band-worksheet.md`; https://www.bls.gov | Industry sales/receipts, employment, establishments (CBP has no revenue) | Indicative size band |
| SBA size standards | https://www.sba.gov/federal-contracting/contracting-guide/size-standards (old /size-standards path redirects to a legacy page) | NAICS size thresholds | Sizing, fed eligibility |
| State professional licensing boards | (per state/profession) | License status, disciplinary actions | Risk, legitimacy (trades, health, finance) |

## Tier 2 — Reputable secondary
| Source | URL | What it gives you | Best for |
|---|---|---|---|
| Better Business Bureau | https://www.bbb.org | Rating, complaint themes, **years in business** | Stability, ops gaps |
| Google Business Profile / Maps | https://www.google.com/maps | Reviews, hours, longevity, photos | Ops gaps, foot traffic |
| Yelp | https://www.yelp.com (fetch tool blocked by robots; open by hand) | Review themes, volume trend | Ops gaps |
| Glassdoor / Indeed | https://www.glassdoor.com , https://www.indeed.com | Employee reviews, **open roles / hiring velocity**, est. headcount | Growth strain, culture, ops |
| LinkedIn company page | https://www.linkedin.com (fetch tool blocked; company pages may ask for login, so use only what is shown logged out) | Headcount trend, leadership tenure, locations | Firmographics, succession |
| Wayback Machine | https://web.archive.org (fetch tool blocked; archive.org/web/ errored; open by hand) | Site history — investment cadence, staffing, "about" changes | Distress/stale signals, history |
| BuiltWith / Wappalyzer (free tier) | https://builtwith.com (home page now stresses paid data products; free lookup not confirmed) | Public tech stack | Digital maturity (consulting) |
| BizBuySell / BizQuest (browse) | https://www.bizbuysell.com (home page frames browsing as a free account feature; account may be needed) | Active sale listings + **free industry multiple insight reports** | Already-for-sale, market multiples |
| Local business journals / press | (varies) | Ownership changes, expansions, retirements, awards | Transition signals, market pull |
| Data.gov | https://www.data.gov | Misc. federal/state datasets | Niche signals |

## Source-quality rules
- Government filing > company-controlled page > news > review aggregator > inference.
- Company website and LinkedIn are **company-controlled** — label claims from them as company claims, not independent facts.
- News must carry a publication date. Reviews must carry the period observed.
- Cross-check any signal that moves a score by a band.

## Link check — 2026-11-12 (WebFetch)
Opened and loaded: sec.gov/search-filings (company search + full-text search), sam.gov, sam.gov/contracting,
usaspending.gov (page opened, body text thin), uspto.gov, pacer.uscourts.gov, osha.gov, echo.epa.gov,
census.gov (+ SUSB, Economic Census, Nonemployer, CBP program pages), bls.gov, sba.gov contracting guide,
bbb.org, indeed.com, glassdoor.com, bizbuysell.com, data.gov, dol.gov/agencies/whd/data.
Moved: fpds.gov to sam.gov/contracting; enforcedata.dol.gov to data.dol.gov (JavaScript app, not rendered by the tool); sba.gov/size-standards to a legacy page.
Not confirmed (tool blocked or no rendered content): yelp.com, linkedin.com, web.archive.org, google.com/maps (needs JavaScript), tmsearch.uspto.gov (opened, no body text), census.gov/naics, builtwith.com free tier.
Login or fees: PACER offers registration and charges per page (pricing page not read; confirm); SAM.gov entity search login need not stated on the page; LinkedIn and Glassdoor may gate content; BizBuySell frames browsing as a free-account feature.
State Secretary of State and UCC portals are per-state and were not checked.
