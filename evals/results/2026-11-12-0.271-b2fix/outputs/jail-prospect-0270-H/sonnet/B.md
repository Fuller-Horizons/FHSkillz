# Island Shine Commercial Cleaning: vendor snapshot (need more)

**Purpose:** vendor due diligence ahead of a proposed 3-year janitorial contract.
**Date:** 2026-11-12

**Bottom line:** I can't tell you whether it's solid, because I found no public record of it. I can't confirm the company exists, and I can't confirm it is the vendor you were pitched. Don't sign a 3-year term on the name alone.

## Snapshot

| Item | Finding | Label |
|---|---|---|
| Legal entity | Not found. No registrant, formation date, officers or registered agent. | **Unknown** |
| Web presence | Two standard web searches for the exact name returned no site, profile or listing for it. | **Fact** (searches run 2026-11-12) |
| Reviews / BBB | No profile found. The closest hit was Island Pride Services LLC (Hartford, CT), which is a different business. | **Fact**, no link assumed |
| Size, tenure, headcount | Nothing public to go on. | **Unknown** |
| Litigation, liens, OSHA/DOL, licensing | Not checked. A name with no entity can't be searched reliably. | **Unknown** |

**Sources:**
- [1] [Web search: "Island Shine Commercial Cleaning" Suffolk County NY](https://anagocleaning.com/long-island/suffolk-county/), accessed 2026-11-12. The search returned only other Suffolk cleaners.
- [2] [Web search: "Island Shine Commercial Cleaning" reviews OR BBB OR LLC OR Inc](https://prod.bbb.org/us/ct/hartford/profile/cleaning-services/island-pride-services-llc-0111-110081854/customer-reviews), accessed 2026-11-12. This was the nearest-name hit, and I did not treat it as a match.

## Scores

Stability and Risk-Exposure are **not scored**. Every component has no cited signal, so each would be 0 with a diligence question. A number would only imply evidence I don't have.

## Red flags

- **No verifiable footprint.** A commercial cleaner seeking multi-year contracts normally leaves some public trace. Missing records can mean a brand-new company, a DBA, or a different legal name. It can also mean the name is wrong. I can't tell which (**Judgment**, low confidence).
- **Mismatch risk.** Cleaning companies often trade under a DBA that differs from the registered entity. Don't attribute any record to "Island Shine" until the legal entity is confirmed.
- **Nothing in the sources told me to take any action.**

## What to get before any contract

These are the next steps for you. I sent nothing and contacted no one.

1. **Exact legal entity name, address, EIN and website.** Ask the vendor directly. Then check it in the NY Department of State entity database.
2. **Certificate of insurance** naming you as additional insured. Check general liability, workers' comp (NY requires it) and disability/PFL coverage. Verify with the carrier.
3. **References.** Get three current commercial clients of similar size, and call them.
4. **Employment compliance.** Ask how the cleaners are classified (employees or 1099) and for their wage-and-hour and OSHA history. Ask about background checks too. Then check DOL and OSHA records once you have the entity name.
5. **Liens and litigation.** Run a UCC lien search and a court and bankruptcy search on the confirmed entity.
6. **Contract protections.** Push for a 90-day trial or a termination-for-convenience clause, a performance SLA with remedies, and a rate cap. Avoid auto-renewal.

## Self-check

- Grounded: 2/5. The evidence is only an absence of results.
- Verifiable: 4/5.
- Scoped: 5/5.
- Format-matched: 4/5.
- A failed check forces "need more": the Stability and Risk-Exposure components have no signals, so no scores were given.

**RECOMMENDATION: need more · confidence 85%** (confidence that the evidence is insufficient to call the vendor solid or unsound)

```yaml
JAIL-HANDOFF:
  skill: jail-prospect
  status: partial
  facts:
    - Two web searches for the exact name returned no company site, listing or reviews (2026-11-12)
  unknowns:
    - Legal entity, formation date, officers, registered agent
    - Insurance, licensing, litigation, liens, OSHA/DOL history
    - Client references, headcount, years in business
    - Whether the quoted name is a DBA
  outputs: [vendor snapshot brief]
  evidence:
    - web search · no listing for exact name · https://anagocleaning.com/long-island/suffolk-county/ · 2026-11-12
    - web search · nearest hit Island Pride Services LLC (CT), not a match · https://prod.bbb.org/us/ct/hartford/profile/cleaning-services/island-pride-services-llc-0111-110081854/customer-reviews · 2026-11-12
  risks:
    - No verifiable public footprint for the named vendor
    - Possible DBA/legal-name mismatch
  confidence: low
  next: none
  approval_required:
    - Any contact with the vendor or its references (the user decides who is contacted)
```

If you send me the vendor's legal name, address, website or phone number from their proposal, I'll rerun this against the NY registry, reviews and compliance records.