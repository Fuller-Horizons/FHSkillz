**Recommendation: need more. Don't approach the Hicks owners yet.** Confidence 60%.

I re-ran the checks from this morning's project brief (`claude/prospect-hicks-nurseries-brief.md`). Nothing new points to a sale, so the scores stay where they were. The main open items are still unresolved.

**Scores (unchanged after re-check)**
- Likelihood-to-Sell: **34/100 (Low)**. Drivers: succession 10/30, exit/transition 0/25, saleability 18/25, market pull 6/20.
- Consulting-Opportunity: **23/100 (Low)**. Drivers: operational 5/30, digital 8/25, growth strain 10/25, compliance 0/20.

**What this run found**
- **Sale or succession: no signal.** A search for a sale, acquisition, or retirement returned only company press and directory pages. Current press still calls it family-owned, with Stephen Hicks as President. *Fact (search summary), low coverage.* [1]
- **Entity record: still not verified.** No NY Department of State filing turned up, so formation date, status, and registered agent remain Missing Evidence. The FMCSA carrier profile matches the 100 Jericho Turnpike address. *Fact.* [2]
- **Safety record: still open.** I found no OSHA inspection for the Westbury site. The April 21, 2025 amputation report is a workplace injury record, not a citation. The fastdol aggregator's fatality line conflicts with its own zero-violation figure, so it stays unverified. *Fact (search summaries).* [3][4]
- **2026 activity (company-announced):** a landscape design award (Feb 2026), a marketing partnership (announced Jul 2, 2026), and a redesigned wholesale e-commerce site (date unclear). *Fact (company or trade press).* [5][6]
- **Listings:** no Hicks listing on BizBuySell or in a broker search. The Mount Sinai garden center on N. Country Road (listed at $8.78M, Mar 2025 per Landsearch) is a different property in Suffolk County, not Hicks. It is only market context. [7]

**Why it stays "need more"**
- Owner ownership split, ages, and any successor plan are still unknown. Those are the questions that decide whether a sale conversation makes sense.
- The company's own pages, the Garden Center "six generations" article, and the injury report page could not be opened. The proxy refused them, so those claims rest on search summaries.
- Size band: no revenue figure is public. The Top 100 list PDF would give a flagship revenue proxy, but the page was not opened. Treat the size band as unknown for now.

**Diligence before any approach (in order)**
1. NY DOS entity record: formation date, status, and registered agent (try the Division of Corporations search directly).
2. OSHA establishment search for 100 Jericho Turnpike: the April 2025 injury and the fatality entry.
3. Ownership and succession: who holds the operating company and the real estate, and whether a successor is named.
4. Owner tenure and roles for Stephen Hicks and Karen Hicks Courts, business-relevant only.
5. Flagship 2024 revenue from the 2025 Top 100 PDF, to set a size band.

**Outreach:** nothing has been sent or drafted for use. A draft hook is in the project brief and should wait until items 1–3 are answered. Any contact needs your approval.

**Project doc:** I did not rewrite the existing brief, because this run changed no scores or findings. Say if you want the re-check logged there.

Sources (all accessed 2026-11-12):
1. [Hicks Nurseries search results, sale/succession check](https://hicksnurseries.com/about-us/); [Farmingdale State 2026 article](https://fscnow.farmingdale.edu/2026/rooted-campus-community/) (search summary)
2. [FMCSA carrier profile, Hicks Nurseries Inc](https://ai.fmcsa.dot.gov/SMS/Carrier/1483291/CompleteProfile.aspx) (search summary)
3. [Injury report, Apr 21, 2025](https://recallcheck.net/workplace-safety/2025043692) (search summary; page not opened)
4. [Fastdol profile](https://www.fastdol.com/employers/hicks-nurseries-inc-8be02b54-d418-a31d-bc77-57d1d3ba3ace) (search summary; conflicting figures)
5. [LINLA awards, Feb 2026](https://lifestyle.kccrradio.com/story/57573/hicks-landscapes-earns-four-linla-awards-for-standout-residential-landscape-design-across-long-island/) (search summary)
6. [MAXPlaces marketing release, Jul 2, 2026](https://startupfortune.com/press-release/hicks-nurseries-is-excited-to-announce-the-launch-of-their-marketing-campaign/) (search summary)
7. [Mount Sinai listing, Landsearch](https://landsearch.com/properties/185-191-n-country-rd-mount-sinai-ny-11766/4277905) (search summary; a different property)

```yaml
JAIL-HANDOFF:
  skill: jail-prospect
  status: partial
  facts: [no sale, listing, or succession signal found this run; 2026 company announcements (LINLA awards, MAXPlaces, e-commerce redesign); Likelihood-to-Sell 34 Low; Consulting 23 Low]
  assumptions: [scores carried from the 2026-11-12 project brief; no revenue figure public]
  unknowns: [NY DOS record; ownership and succession; owner tenure; OSHA injury and fatality entries; flagship revenue from Top 100 PDF; court, UCC, and real-estate checks]
  outputs: [prospect brief, re-check of existing project brief]
  evidence: [search summaries listed above; company pages and injury report not opened (proxy refused)]
  risks: [April 2025 injury report; conflicting fatality aggregator figure; company pages not opened this run]
  confidence: medium
  next: none
  approval_required: [any outreach to the owners]
```