**Short answer: I can't vet this vendor yet, and I wouldn't sign a 3-year contract on this name alone.** I found no public record of a business called "Island Shine Commercial Cleaning" in Suffolk County or anywhere on Long Island. The result is **NEED MORE**.

This was a Company Snapshot for vendor due diligence. The scores below are evidence gaps, not findings of weakness.

## Snapshot

- **Legal entity:** Unknown. No New York Department of State record matched the name. I could not open the NY DOS database itself (the proxy refused the fetch), so this is a search-index result, not a registry check. _Fact (search, no match), 2026-11-12._
- **Industry:** Commercial cleaning / janitorial (per your brief). _User-provided._
- **Locations / HQ:** Unknown. No address, phone, or website tied to this name in Suffolk County. _Fact (search, no match), 2026-11-12._
- **Years in business / headcount / owners:** Unknown. Not fabricated.
- **Financials:** Unknown. Private company, and no size band is possible without an entity match.

## Scores (Vendor due-diligence lens)

| Component | Score | Max | Basis |
|---|---|---|---|
| Stability (tenure, registration, ownership) | 0 | 100 | No evidence found. Scored 0 by rule, not a midpoint. |
| Risk exposure (litigation, liens, violations, insurance) | 0 | 100 | No evidence found. Scored 0 by rule, not a midpoint. |

Confidence on the scores: **low**. Confidence that "need more" is the right call: **high (about 90%)**. This brief cannot say whether the vendor is solid.

## Why the name doesn't resolve

- **No Suffolk County match.** Three search passes and an extended search returned Suffolk and Long Island cleaning companies (Anago, Shoreline, Shore To Shore, Advance Industrial, Empire Building Maintenance), none named Island Shine. _Fact, 2026-11-12._
- **Several same-named businesses exist elsewhere.** Using these as a stand-in for the vendor would be a wrong-entity error:
  - Island Shine Cleaning, Fort Lauderdale/Lauderhill, FL: [Angi listing](https://www.angi.com/companylist/us/fl/fort-lauderdale/island-shine-cleaning-reviews-9192683.htm). Wrong state, not attributable.
  - Island Shine Pressure Washing (Maui); Island Shine Services (Pender Island, BC); Island Shine Windows (Lopez Island, WA). Different businesses.
  - **Island Shine SI**, [islandshinesi.com](https://islandshinesi.com/), appeared as a Staten Island cleaning site. Staten Island is in NYC, not Suffolk. I could not open the site, so its service area is **Unknown**. It may be worth asking the vendor directly whether they have any NYC or Staten Island affiliation.

## Red flags

- None. No source text addressed the assistant or asked for an action.

## Outreach hook

Not drafted. The vendor's identity has to be confirmed first. Nothing was contacted or sent.

## Recommendation

**NEED MORE** · Confidence 90% that this call is right.

- **Why:** The vendor cannot be identified from public sources. Any stability or risk score would rest on a different company.
- **Do not sign on the name alone.**

**Top diligence questions (ask the vendor, then verify):**

1. What is the exact legal name on the contract and W-9, and what is the EIN? Is the counterparty an LLC, corporation, or a DBA? Which registered entity do they name?
2. Can they give the NY DOS ID, registered agent, and street address? Check each one at the NY DOS Corporation and Entity Database (apps.dos.ny.gov/publicInquiry). I could not run that search.
3. Can they provide a current certificate of insurance (general liability, workers' comp, and crime/bonding) and check it against the NY Workers' Compensation Board's coverage search?
4. Who are the principals, and how long has the business operated under this name? Can they provide three Suffolk County references with contact details you verify yourself?
5. Have you checked whether the company has any NY DOL, OSHA, or BBB history? (OSHA Establishment Search: osha.gov/ords/imis/establishment.html.)

## Source appendix

| # | Claim | URL | Source type | Date accessed |
|---|---|---|---|---|
| 1 | No "Island Shine Commercial Cleaning" match in Suffolk County search results | (WebSearch, query: "Island Shine Commercial Cleaning" Suffolk County) | Search | 2026-11-12 |
| 2 | No NY DOS match in search index | (WebSearch, query: Island Shine Commercial Cleaning LLC New York Department of State entity) | Search | 2026-11-12 |
| 3 | Island Shine Cleaning is in Fort Lauderdale/Lauderhill, FL | https://www.angi.com/companylist/us/fl/fort-lauderdale/island-shine-cleaning-reviews-9192683.htm | Review aggregator | 2026-11-12 |
| 4 | Island Shine SI serves Staten Island (service area not verified) | https://islandshinesi.com/ | Company-controlled (not opened) | 2026-11-12 |

## Scope and gaps

- Not run: the NY DOS database, NY Workers' Compensation Board insurance search, OSHA, BBB, and Google Business Profile. Most need a manual lookup or a live browser, which I did not have here. _Unknown._
- The NY DOS fetch and the Island Shine SI fetch both failed through the proxy.
- No scores were run through `score-check.py` because every component is 0 by rule.
- I did not save this to the Business Consulting Tools project because it's a one-off vendor check. I can save it as a project doc if you want it on file.

```yaml
JAIL-HANDOFF:
  skill: jail-prospect
  status: partial
  facts:
    - No Suffolk County or Long Island business named "Island Shine Commercial Cleaning" in public search results (2026-11-12)
    - No NY DOS search-index match for the name (2026-11-12)
  assumptions:
    - Vendor is a commercial cleaning company in Suffolk County (user-provided, unverified)
  unknowns:
    - Legal entity, formation date, officers, registered agent, address
    - Insurance and bonding status; litigation, liens, violations
    - Whether Island Shine SI (Staten Island) is related
    - Diligence questions 1-5 in brief
  outputs: [prospect brief]
  evidence:
    - "No match in Suffolk search · WebSearch · 2026-11-12"
    - "No NY DOS match · WebSearch · 2026-11-12"
    - "Island Shine Cleaning FL · https://www.angi.com/companylist/us/fl/fort-lauderdale/island-shine-cleaning-reviews-9192683.htm · 2026-11-12"
  risks:
    - "No risk signals found; the vendor's absence from the public record is itself the risk to close"
  confidence: low
  next: none
  approval_required:
    - Any contact with the vendor or its references (none sent)
```