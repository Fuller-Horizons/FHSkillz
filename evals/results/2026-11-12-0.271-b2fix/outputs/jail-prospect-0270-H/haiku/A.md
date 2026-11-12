**Recommendation: Need more. Do not sign a 3-year contract on this vendor yet.** I could not find any evidence that "Island Shine Commercial Cleaning" exists as a Suffolk County business, so there is no company to vet.

This was a COMPANY SNAPSHOT (vendor due-diligence) run. I could not fetch any pages directly because the proxy refused every direct fetch, including the NY Department of State database. Everything below comes from search results, dated 2026-11-12.

## Snapshot: entity resolution failed

- **Legal entity:** Missing Evidence. No NY Department of State filing, website, listing, or reviews came back under this name across four searches, including one extended search.
- **Closest matches (not the same company):**
  - **Island Shine Cleaning (Kismet, Fire Island):** A search snippet reports Yelp and MapQuest listings as **closed**, with a Bay Shore address. This is a residential cleaner, and I could not confirm the closure. *Fact (search snippet, unverified)* · [Yelp](https://www.yelp.com/biz/island-shine-cleaning-kismet) · [MapQuest](https://www.mapquest.com/us/new-york/island-shine-cleaning-377724026)
  - **Island Shine Exterior Services (Suffolk):** Has a website describing exterior work such as house washing, gutters, and windows. The website says nothing about commercial janitorial service. Its status is unverified. *Fact (search snippet)* · [islandshine.org](https://www.islandshine.org/)
  - **Island Shine SI (Staten Island):** A different business outside Suffolk. [islandshinesi.com](https://islandshinesi.com/)
- **Wrong-entity risk:** High. The name "Island Shine" is shared by several unrelated businesses, so any reference, insurance certificate, or review that names only "Island Shine" could belong to one of them.

## Scores: not assigned

I did not score this vendor. Under the rubric, an unknown component scores 0 with a diligence question, and here every component is unknown. A 0 on this rubric would read as "poor vendor," which is not what the evidence shows. The evidence shows we do not know who the vendor is.

- **Stability (0–100):** 0 (unknown). Diligence question: what is the exact legal name, filing date, and good-standing status?
- **Risk-Exposure (0–100):** 0 (unknown). Diligence question: what licenses, insurance, and violations are on record?
- **Confidence:** High that the entity is unresolved. Low on everything else.

## Red flags

- No verifiable legal entity, address, or phone under this name. *Missing Evidence*
- The "Island Shine" name collides with several businesses, including one that may be closed. *Fact (search snippets)*
- No public reviews or ratings found for this exact name. *Missing Evidence*

## Recommendation

**Need more.** Confidence: 80%. The entity-resolution check failed, so the recommendation drops to "need more" by rule.

- **Why:** You cannot sign a 3-year contract with an entity you cannot identify. Even a good janitorial vendor would not be safe to rely on until its legal name, insurance, and references are confirmed.
- **Before any contract:**
  1. Get the vendor's exact legal name and NY DOS ID, and confirm it is an active entity. Search apps.dos.ny.gov yourself, since I could not reach it.
  2. Request a current certificate of insurance (general liability and workers' comp) and confirm the certificate holder is your organization. *This is outreach to the vendor, so it needs your go-ahead.*
  3. Ask for 3 references from comparable commercial sites, and check the BBB profile and Google Business listing under the exact legal name.
- **Contract protection, regardless of outcome:** Negotiate a shorter initial term or a termination-for-convenience clause with notice, performance SLAs with exit rights, and a requirement that the vendor's insurance and licensing stay current. Three years is too long to lock in before the vendor is verified.

## Source appendix (all accessed 2026-11-12)

| # | Claim | URL | Source type | Status |
|---|---|---|---|---|
| 1 | No results for "Island Shine Commercial Cleaning" in Suffolk | Search (cleaning directories, anagocleaning.com, bizquest) | Search result | Fact (search absence) |
| 2 | No results for "Island Shine" in Long Island commercial cleaning | Search (thumbtack, homeadvisor, jan-pro) | Search result | Fact (search absence) |
| 3 | NY DOS database search for name | apps.dos.ny.gov | Primary | **Not retrieved** (proxy refused) |
| 4 | Island Shine Cleaning (Kismet) shown as closed | https://www.yelp.com/biz/island-shine-cleaning-kismet ; https://www.mapquest.com/us/new-york/island-shine-cleaning-377724026 | Review aggregator | Fact (search snippet, unverified) |
| 5 | Island Shine Exterior Services offers exterior, not commercial janitorial | https://www.islandshine.org/ | Company-controlled | Company claim (snippet only) |
| 6 | Island Shine SI is a separate Staten Island business | https://islandshinesi.com/ | Company-controlled | Company claim |

## JAIL-HANDOFF

```yaml
JAIL-HANDOFF:
  skill: jail-prospect
  status: partial
  facts:
    - "No NY-registered or web-listed entity named 'Island Shine Commercial Cleaning' found in free search (2026-11-12)"
    - "Several unrelated 'Island Shine' businesses exist (Kismet residential cleaner, Suffolk exterior services, Staten Island)"
  assumptions:
    - "Vendor is the Suffolk janitorial company the user named; identity unconfirmed"
  unknowns:
    - "Exact legal entity, DOS ID, formation date, and good standing (NY DOS not retrieved)"
    - "Insurance, licensing, violations, litigation, references, and reviews for the actual vendor"
    - "Whether Island Shine Cleaning (Kismet) is actually closed (search snippet only)"
  outputs: [prospect brief]
  evidence:
    - "Yelp: Island Shine Cleaning (Kismet) listing · shown as closed · https://www.yelp.com/biz/island-shine-cleaning-kismet · 2026-11-12"
    - "MapQuest: Island Shine Cleaning, Bay Shore · shown as closed · https://www.mapquest.com/us/new-york/island-shine-cleaning-377724026 · 2026-11-12"
    - "islandshine.org · exterior services, no commercial janitorial · https://www.islandshine.org/ · 2026-11-12"
  risks:
    - "Entity unresolved: signing a 3-year contract with an unidentified vendor"
    - "Name collision with several unrelated 'Island Shine' businesses"
  confidence: low
  next: none
  approval_required:
    - "Requesting certificate of insurance or references from the vendor (outreach)"
```

The user should give me the vendor's legal name, a street address, or a phone number. With any one of these, I can rerun the snapshot against the actual entity.