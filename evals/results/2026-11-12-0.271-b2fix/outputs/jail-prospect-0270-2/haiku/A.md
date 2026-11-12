**Recommendation: need more.** Confidence is 20%. I can't say whether Zephyrine Brookhaven Millwork LLC is a good brokerage prospect, because I can't verify that the company exists.

I re-ran the name searches today and got the same result as the earlier brief in the project. No search turned up a business called "Zephyrine Brookhaven Millwork," in Patchogue or anywhere else. The results were near-misses:

- **Brookhaven LLC** (NY DOS doc 1916998) is a different entity, based in Flushing. [bizprofile.net](https://www.bizprofile.net/ny/new-york/brookhaven-llc)
- **Syd Millwork LLC** (Brooklyn) and **City Millwork LLC** (Manhattan) share the "millwork" word but not the name. [bizprofile.net](https://www.bizprofile.net/ny/brooklyn/syd-millwork-llc)
- **ZCI Woodworks** (Islandia) and **Z-Carpentry** (Huntington) are Long Island millwork firms with similar initials. Nothing links them to "Zephyrine," so I haven't treated either as the subject. [Houzz](https://www.houzz.com/professionals/carpenter/c/South-Huntington--NY/p/105)
- **Edge Millwork & Mouldings** (East Patchogue) and **BauTia Millwork** (Patchogue) are local shops, also not linked to this name. [Houzz](https://www.houzz.co.nz/professionals/specialty-contractors/c/East-Patchogue--NY)

The NY Department of State lookup is the authoritative check, and I couldn't run it. The proxy refused the fetch of apps.dos.ny.gov/publicInquiry, both today and earlier.

**Why no score:** A score needs a verified entity to attach signals to. Without one, anything I scored would be invented. The size band is also withheld, since there's no headcount or facility to base it on.

**What would resolve it (in order):**
1. **Check the exact name against the source.** Was it from an invoice, a referral, an ad, or a contract? Misspellings are the most likely cause of zero matches. If the name came from a similar local shop, that shop is not assumed to be this company.
2. **Run the NY DOS search yourself** at apps.dos.ny.gov/publicInquiry, using "Zephyrine Brookhaven Millwork," "Brookhaven Millwork," and their Corp and Inc variants. If it exists, send me the formation date, status, DOS process address, and registered agent, and I'll run the full brokering and consulting sweep.
3. **Send a street address or phone number for Patchogue.** I can check it against county and business records.
4. **Check for a DBA.** The NY assumed-name filings may show a different legal registrant.

**Outreach:** None drafted. Don't approach the owner until the entity is confirmed.

I didn't update the project brief, because today's searches added nothing new. The existing brief at `claude/prospect-zephyrine-brookhaven-millwork-brief.md` still holds the full source appendix. Tell me if you'd like it refreshed once you've run the DOS check.

```yaml
JAIL-HANDOFF:
  skill: jail-prospect
  status: partial
  facts: [No web presence; no NY DOS match in three searches today; no directory match for the name]
  assumptions: [Name as given is the intended legal name; Patchogue location is user-provided]
  unknowns: [Legal entity status; formation date; registered agent; principals; headcount; revenue proxies; NY DOS record (not reachable from this session); court, UCC, OSHA checks]
  outputs: [prospect brief (existing project doc, unchanged)]
  evidence: [project brief source appendix; bizprofile.net and Houzz results from 2026-11-12]
  risks: [Entity unverified; wrong-entity risk with similarly named businesses]
  confidence: low
  next: none
  approval_required: [any outreach to the owner or principals]
```