# Example — Filled PROSPECT Brief

_Fictional example for format reference — Cascade Ridge Mechanical, LLC does not exist. Every figure below still carries the skill's Fact / Source-Backed Inference / Analyst Judgment / Missing Evidence label, exactly as a real brief must._

---

# Prospect Brief — Cascade Ridge Mechanical, LLC
_Researched: 2026-07-24 · Researcher: jail-prospect · Free-sources-only_

## Snapshot
- **Legal entity / DBA:** Cascade Ridge Mechanical, LLC, DBA "Cascade Ridge HVAC" (WA · formed 2004 · active/good standing) — _Fact, WA SOS UBI lookup, accessed 2026-07-24_
- **Industry (NAICS):** 238220 — Plumbing, Heating, and Air-Conditioning Contractors
- **Locations / HQ:** Wenatchee, WA (HQ) + satellite branch, Chelan, WA
- **Est. headcount:** 28–35 — _Indeed job-postings page + LinkedIn company page, cross-checked, accessed 2026-07-24_
- **Owner / principals:** Daryl Voss, Founder/President, 21-yr tenure since formation — _Fact, WA SOS officer listing, accessed 2026-07-24_
- **One-line description:** Residential/light-commercial HVAC install & service contractor serving the central-Washington Cascade corridor.

## Scores
| Lens | Score | Band | Confidence |
|---|---|---|---|
| **Likelihood-to-Sell** | 74 | High | 65% |
| **Consulting-Opportunity** | 52 | Medium | 55% |

### Likelihood-to-Sell drivers
- Succession: Owner tenure 21 yrs since 2004 formation, no successor officer in most recent SOS annual report — _Fact, WA SOS UBI lookup, accessed 2026-07-24_
- Exit/transition: Site design unchanged since 2021 Wayback snapshot; open roles on Indeed dropped from 4 (2024 snapshot) to 0 (2026-07-24) — _Source-Backed Inference, Wayback Machine + Indeed, accessed 2026-07-24_
- Saleability: BBB-accredited since 2006, A+ rating, "20+ years in business" — _Fact, bbb.org profile, accessed 2026-07-24_
- Market pull: Regional HVAC roll-up activity noted in trade press covering the Wenatchee Valley — _Source-Backed Inference, Wenatchee Valley Business Journal, dated 2026-03-11_

### Consulting-Opportunity drivers
- Operational: "Long wait for callback" theme in 12 of last 30 Yelp reviews, 2024–2026 — _Fact, Yelp, accessed 2026-07-24_
- Digital/tech: No online booking/scheduling on site (manual review 2026-07-24); BuiltWith shows only Google Analytics, no CRM/booking integration — _Fact, BuiltWith, accessed 2026-07-24_
- Growth strain: Zero open roles currently (down from 4) — reads as stagnation, not strain — _Analyst Judgment_
- Compliance/risk: One closed OSHA inspection (2022), no violation found — _Fact, OSHA Establishment Search, accessed 2026-07-24_

## Indicative size band (NOT a valuation)
- **Range:** $2.8M–$3.6M revenue (rough) — _Source-Backed Inference_
- **Method & assumptions:** 30-employee midpoint (est. range 28–35) × ~$105K/employee (Census County Business Patterns 2023 revenue-per-employee benchmark, NAICS 238220) ≈ $3.15M; no USAspending federal awards found, so no federal-contract add-on
- **Actual financials:** Missing Evidence (private company)

## Red flags
- Single-location revenue concentration — 80%+ of Google reviews reference the Wenatchee shop only, despite a 2nd Chelan location — _Analyst Judgment, Google Business Profile, accessed 2026-07-24_
- One 2019 equipment-loan UCC filing with no release found in a 2026-07-24 search — confirm status before any LOI — _Fact, WA SOS UCC filing search, accessed 2026-07-24_

## Outreach hook
"You've kept Cascade Ridge's fleet and reputation strong for two decades without a listed successor — worth a confidential conversation about what a clean exit could look like on your own timeline."

## Recommendation
**Pursue — brokering** · Confidence 65%
- Why: Succession + exit signals corroborate across two independent Tier-1/Tier-2 sources; consulting angle is secondary given thinner, single-source operational evidence.
- If "Need more": n/a — evidence cleared the pursue threshold.

## Source appendix
| # | Claim | URL | Source type | Date accessed |
|---|---|---|---|---|
| 1 | Formation date, officer, good standing | https://ccfs.sos.wa.gov/ (UBI lookup) | Primary (gov) | 2026-07-24 |
| 2 | UCC equipment-loan filing, no release on record | https://ccfs.sos.wa.gov/ (UCC search) | Primary (gov) | 2026-07-24 |
| 3 | OSHA inspection closed, no violation | https://www.osha.gov (Establishment Search) | Primary (gov) | 2026-07-24 |
| 4 | Revenue-per-employee benchmark, NAICS 238220 | https://www.census.gov (County Business Patterns) | Primary (gov) | 2026-07-24 |
| 5 | BBB accreditation since 2006, A+ | https://www.bbb.org | Secondary (review aggregator) | 2026-07-24 |
| 6 | Review theme: callback wait times | https://www.yelp.com | Secondary (review aggregator) | 2026-07-24 |
| 7 | Open-roles trend 4→0 | https://www.indeed.com | Secondary (job board) | 2026-07-24 |
| 8 | Site unchanged since 2021 | https://web.archive.org | Secondary (archive) | 2026-07-24 |
| 9 | Tech stack — no booking/CRM integration | https://builtwith.com | Secondary (tech scanner) | 2026-07-24 |
| 10 | Regional roll-up activity | Wenatchee Valley Business Journal | News | 2026-03-11 |

---

## JAIL-HANDOFF
```yaml
JAIL-HANDOFF:
  skill: jail-prospect
  status: complete
  facts:
    - "Cascade Ridge Mechanical, LLC formed 2004, WA, active/good standing — WA SOS UBI lookup, 2026-07-24"
    - "BBB-accredited since 2006, A+ rating — bbb.org, 2026-07-24"
    - "Open roles on Indeed fell from 4 (2024) to 0 (2026-07-24)"
  assumptions:
    - "Size band uses 30-employee midpoint (est. 28-35) x ~$105K/employee (Census CBP 2023, NAICS 238220) = ~$3.15M; explicitly NOT a valuation"
  unknowns:
    - "Actual revenue/EBITDA — Missing Evidence, private company"
    - "Whether the 2019 UCC lien has since been released — none found as of 2026-07-24 search"
  outputs: [prospect brief]
  evidence:
    - "WA SOS UBI lookup — formation date, officer tenure, good standing — https://ccfs.sos.wa.gov/ — 2026-07-24"
    - "WA SOS UCC search — open 2019 equipment-loan lien — https://ccfs.sos.wa.gov/ — 2026-07-24"
    - "BBB profile — years in business, A+ rating — https://www.bbb.org — 2026-07-24"
    - "Indeed — hiring-velocity trend (4 to 0 open roles) — https://www.indeed.com — 2026-07-24"
    - "Wayback Machine — site staleness since 2021 — https://web.archive.org — 2026-07-24"
  risks:
    - "Single-location revenue concentration (Wenatchee) despite a 2nd Chelan site"
    - "Unreleased 2019 UCC lien — confirm status before any LOI"
  confidence: medium
  next: jail-prompt
  approval_required:
    - "Any first contact/outreach to the owner — humans authorize external communications (Rule 5)"
```
