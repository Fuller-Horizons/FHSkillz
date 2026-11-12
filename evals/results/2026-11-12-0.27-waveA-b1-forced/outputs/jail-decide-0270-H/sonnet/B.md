# DECISION PACKAGE

**Decision:** How to replace or keep the 7-year-old file server. **Owner:** you, as firm owner or managing partner. **Needed by:** Jan 15, about 64 days out, which is a real date because tax season starts then.

**Criteria (set before scoring, unweighted):**
1. Risk of disruption in Jan–Apr
2. 5-year cost
3. Data-loss exposure
4. Compatibility with your tax and practice software
5. Reversibility

| Option | Benefits | Costs | Risks | Door | Delay cost |
|---|---|---|---|---|---|
| **Do nothing** | $0 now | $0 now, plus the full cost of a failure | Failure on the IT guy's "any month" warning (Estimate, unquantified). A failure in season could mean days of downtime or lost data. | Two-way, but a failure forces a rushed one-way purchase | Highest. Each month of waiting is another month of exposure, and Jan–Apr is the worst time for an outage. |
| **New server** | Same workflow, so little retraining. Can be ready before Jan 15. | $13k, about $2.6k a year over 5 years (Fact, your quote). Backup and maintenance costs are not included. | Migration slips past Jan 15. Hardware is 5-year-old tech again by 2031. | Mostly one-way, since the $13k is sunk | Hardware lead time eats into the 64 days. |
| **M365 + SharePoint** | No hardware, built-in redundancy, remote access | 9 × $38 × 12 = $4,104 a year, about $20.5k over 5 years (Fact, your quote). Migration labor is not quoted. | Mid-migration during tax prep. Tax software that expects a local server may not work. | Two-way (you can cancel), but migration effort is sunk | Same exposure as do-nothing until cutover |

**Tie note:** Cost is a near-tie. The cloud's $20.5k has no known offset until you check whether you already pay for email or Office. The server's $13k leaves out backup, power and IT time. The tie-breaker is **criterion 1, disruption risk before Jan 15**.

**Recommendation: buy the new server now and migrate before Jan 15. Revisit M365 after April 15.** This is the lowest-change path through tax season, and a like-for-like swap is the easiest migration to finish and test in time. Moving to the cloud is a bigger workflow change, and you shouldn't make one in January. The 2026 decision still leaves the cloud open for the next refresh, and a server's 5-year life gives you time to plan it. **This week, regardless of option, run a test restore of your current backup**, because it is your only protection until cutover.

**Confidence: medium.** The 5-year costs are incomplete. I also don't know your tax software's hosting requirements, your outage cost per week, or the IT guy's basis for "any month" (Estimate).

**Would change this call:**
- Your tax and practice software is cloud-native or supports SharePoint cleanly, and you already pay for most of M365.
- The IT guy can't deliver and test the server before about Jan 5, since slipping past Jan 15 makes the old server plus a verified backup the safer path.
- A quoted outage cost per week is small compared with $13k, which would make the cheaper plan reasonable.
- The server quote leaves out backup or off-site copy, which would tip the cost toward M365.

**Approval required:** The $13k purchase, which only you can authorize, and the IT guy's migration schedule.

**Next actions:**
1. You: this week, ask the IT guy to run and document a test restore of the current backup.
2. IT guy: within a week, give a written delivery and cutover date, with a rollback plan and total cost including backup.
3. You: confirm with your tax software vendor whether the new server meets their requirements, and whether you already pay for any M365 licenses.

**Council:** not convened. The call is not contested, and the key facts are checkable with a vendor call.

**Ship-check:** criteria-first PASS · do-nothing priced PASS · door type per option PASS · ≥2 change-conditions PASS · every number carries Fact/Estimate+source PASS · owner named PASS · council check recorded PASS

**JAIL-HANDOFF**
- next: jail-red-team. The call is money-related and hard to reverse.
- then: jail-plan, to turn the cutover into a dated runbook.