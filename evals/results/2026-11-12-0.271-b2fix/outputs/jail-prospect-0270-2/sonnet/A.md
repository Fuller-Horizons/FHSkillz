**Verdict: need more (confidence 20%). I can't say whether it's a good brokerage prospect, because I can't confirm the company exists.**

The project already held a brief for this company, written earlier today. I re-ran two fresh searches and got the same result:

- **No match anywhere.** Nothing turned up for the exact name, with or without "LLC", and nothing for "Zephyrine" plus millwork on Long Island. That covers directories and the registry mirrors the search reached.
- **NY registry not checked.** I couldn't query the state registry from this session. The earlier attempt on the NY Department of State public inquiry page was blocked by the proxy. This time I tried the state's open-data business-entity dataset on data.ny.gov, and that call needed approval I didn't have, so I stopped.
- **No scores, size band or outreach hook.** Any number would be invented, and the skill rules forbid that.
- **Look-alike names.** Nearby shops include Edge Millwork & Mouldings (East Patchogue), BauTia Millwork (Patchogue), H.B. Millwork (Medford) and SMS Millwork (Deer Park). None is shown to be this company, so I attributed nothing to them.

**Why there's no website:** a missing site tells you little by itself, since many small millwork shops run on referrals. But with no registry record and no directory listing either, the name may be misspelled, a DBA, a brand-new LLC, or wrong.

**Next steps for you:**
1. Check the exact name on the NY DOS entity search (apps.dos.ny.gov/publicInquiry). Try variants like "Brookhaven Millwork LLC", "Corp" and "Inc". Record the formation date, status, process address and registered agent.
2. Ask where the name came from, such as an invoice, referral or ad, and check the spelling against it.
3. If you have a Patchogue street address, send it and I'll match it against the record.
4. If you want me to run the registry query myself, approve the data.ny.gov call and I'll do it.
5. Once the entity is confirmed, send me the details and I'll run the full brokerage and consulting sweep and score it.

I made no outreach and sent nothing. The saved brief at `claude/prospect-zephyrine-brookhaven-millwork-brief.md` is still accurate, so I didn't rewrite it.

```yaml
JAIL-HANDOFF:
  skill: jail-prospect
  status: partial
  facts: [No web presence, directory listing, or registry-mirror match for the name (searched 2026-11-12, twice)]
  assumptions: [Name as given is the intended legal name; Patchogue location is user-provided]
  unknowns: [NY DOS record; formation date; registered agent; principals; headcount; revenue proxies; UCC/court/OSHA checks]
  outputs: [prospect brief (existing, unchanged)]
  evidence: [project doc source appendix; two new negative searches 2026-11-12]
  risks: [Entity unverified; wrong-entity risk with similarly named shops]
  confidence: low
  next: none
  approval_required: [data.ny.gov registry query; any outreach to owners]
```