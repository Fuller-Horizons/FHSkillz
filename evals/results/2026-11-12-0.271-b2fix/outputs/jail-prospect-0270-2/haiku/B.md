**Short answer: I can't tell whether this is a good brokerage prospect. The company itself could not be verified, so there is nothing to score.** Recommendation: **need more**, confidence 20%.

**What I checked today (2026-11-12)**
- **Name searches:** "Zephyrine Brookhaven Millwork" with Patchogue NY, "Brookhaven Millwork" Patchogue, and "Zephyrine" with "Brookhaven Millwork" in quotes. None returned an entity by that name. Results were other Long Island millwork shops. [Search results only; no hit for the subject.]
- **Nearby shops that are not this company (as far as the results show):** HB Millwork (Medford, [News 12](https://westchester.news12.com/made-on-long-island-hb-millwork-inc-in-medford)), SMS Millwork (Deer Park), Edge Millwork & Mouldings (East Patchogue, [Houzz](https://www.houzz.co.nz/professionals/specialty-contractors/c/East-Patchogue--NY)), BauTia Millwork (Patchogue), and Melfi Group Contracting (East Patchogue).
- **NY Department of State registry:** the direct fetch of [apps.dos.ny.gov/publicInquiry](https://apps.dos.ny.gov/publicInquiry/) was refused by the agent proxy, so the official registry was not searched. This is the most important missing check.

**Why it's "need more" and not a score**
- Without a confirmed legal entity, I can't attribute an owner, formation date, tenure, or any succession or exit signal to this company. Scoring it would produce numbers with no cited basis.
- Having no website is consistent with a small private shop, but it is not a scoring signal and doesn't help the brokering case. It's a judgment, not evidence.
- No indicative size band can be built, since there is no headcount, facility, or revenue proxy.

**To get to a real answer, I need one of these from you**
1. **The exact legal name and where it came from** (invoice, referral, ad, contract). The name may be misspelled, a DBA, or a recalled name.
2. **A street address or phone number in Patchogue.** That lets me match against NY DOS and county records.
3. **A manual NY DOS search** at apps.dos.ny.gov/publicInquiry for the exact name and variants (Brookhaven Millwork LLC/Corp/Inc). Record the formation date, status, and registered agent, then send them to me.

Once the entity is confirmed, the stage 2 sweep (owner tenure, UCC liens, court records, BizBuySell listings, USAspending) can run.

The project already has today's brief on this company (`claude/prospect-zephyrine-brookhaven-millwork-brief.md`), reaching the same conclusion. The searches above found nothing new, so I did not write a duplicate. Tell me if you want it updated with today's search log.

```yaml
JAIL-HANDOFF:
  skill: jail-prospect
  status: partial
  facts: [No entity match for the name in three search rounds on 2026-11-12; NY DOS direct fetch refused by agent proxy]
  assumptions: [Name as given by user is the intended legal name; Patchogue location is user-provided]
  unknowns: [Legal entity and status; formation date; registered agent; principals; headcount; size band; liens, court, and compliance checks]
  outputs: [existing brief claude/prospect-zephyrine-brookhaven-millwork-brief.md, unchanged]
  evidence: [BBB Patchogue millwork listing (https://www.bbb.org/us/ny/patchogue/category/millwork), 2026-11-12; search-result negatives only]
  risks: [Entity unverified; wrong-entity risk with similarly named Long Island millwork shops]
  confidence: low
  next: none
  approval_required: [any outreach to owners or principals]
```