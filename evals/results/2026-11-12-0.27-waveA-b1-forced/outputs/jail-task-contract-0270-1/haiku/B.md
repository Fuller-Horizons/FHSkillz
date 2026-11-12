**Mode: default lane, round 1 of 2.** Project search found no file on this owner, so every business fact below is still unknown. The Hicks Nurseries brief is a separate sell-side prospect, not this company.

# DRAFT CONTRACT: Landscaping marketing fix (not ship-ready)

Three fields have UNKNOWNs, so this is for discussion with the owner, not sign-off. Fields 1–14 are in order.

1. **Objective:** Get enough spring-season jobs booked to justify the spend, by fixing the marketing basics. "Fixing marketing" is the stated ask. The underlying need is more booked estimates and jobs before spring, not more marketing activity.
2. **Stakeholder:** The owner. The decision it feeds is whether to keep funding marketing for spring and which channels to keep. The owner also approves the $6k.
3. **Required outcome:** By ~Mar 20, 2027 (assumed spring start), a working lead-capture and tracking system is live, with a measured count of inbound leads and booked estimates against a baseline. Target number: **UNKNOWN — what spring result counts as success? (see Q1)**
4. **Deliverables:**
   - (a) Baseline diagnostic: current leads and sources, Google Business Profile (GBP), website, reviews, and three local competitors (by Dec 15)
   - (b) 90-day plan with a budget split (by Jan 10)
   - (c) GBP, service pages, and review-request workflow fixed (by Jan 31)
   - (d) Lead-tracking log that records source and outcome for every lead (by Jan 31)
   - (e) Spring campaign live with conversion tracking (by Feb 1)
   - (f) Results report against baseline (by Mar 20)
5. **Constraints:** Budget $6k (whether ad spend is inside it is UNKNOWN, see Q2). Spring 2027 timing. No fabricated or incentivized reviews. No guaranteed rankings or revenue. Customer names and contact details are handled as PII and never pasted into the contract or handoff.
6. **Non-goals:** Not a full website rebuild, unless approved as a change. Not hiring, crew management, pricing, or operations consulting. Not a retainer beyond the 90-day term. Not a logo or brand redesign.
7. **Inputs available:** Industry (landscaping), a $6k budget, a spring deadline, and the owner's stated goal. Nothing else is confirmed.
8. **Inputs missing (owner provides):** Website URL; GBP, website, and analytics access; 12 months of job and lead records; service list and margins; service area; current marketing spend and channels; close rate; who answers leads and how fast.
9. **Assumptions:**
   - A1: Spring starts ~Mar 20, 2027. Changes if the location is far north or south.
   - A2: The $6k is all-in, including media. Changes if the owner expects media billed separately.
   - A3: The owner is the sole decision maker. Changes if a partner must sign.
   - A4: Service area is local, roughly under 30 miles. Changes if the owner sells regionally.
   - A5: The owner grants account access within 7 days. Changes if access is slower.
10. **Dependencies:** Owner access to GBP, website host, and analytics. Owner time for a 30-minute weekly check. Owner consent for customer review requests. Any web developer or ad platform the owner already uses.
11. **Material risks:**
    - **Off-season timing:** Search demand is low Nov–Feb. A late setup misses spring. Mitigation: launch by Feb 1.
    - **Thin budget:** Paid search in a competitive market can burn $6k with few leads. Consequence: wasted spend and a failed-looking result.
    - **Undefined "results":** Without a number, success can't be shown and the owner may dispute it.
    - **Lead-handling gap:** Leads arrive but calls go unanswered. Marketing looks broken when the problem is follow-up.
    - **Scope creep:** The owner adds "one more thing" mid-run, such as social, logo, or the website.
    - **Platform policy:** Review-solicitation rules can be violated if done carelessly.
12. **Success criteria:** The owner can name the pipeline number and its source. The plan is actionable without us in the room. Cost per booked estimate is known.
13. **Completion criteria (each fails if the work is wrong):**
    - GBP check: all fields complete (primary and secondary categories, services, hours, service area, 10+ photos). Fails if any is blank on the checklist.
    - Lead log: four consecutive weeks where every inbound lead has a source and an outcome tag. Fails if any untagged leads remain.
    - Conversion test: a test form submission appears in analytics. Fails if it doesn't.
    - Spend check: total ad spend ≤ the approved cap. Fails if over.
    - Results report: booked estimates compared with the baseline. Fails if the baseline comparison is missing.
14. **Approval-required actions:**
    - The $6k commitment and payment schedule
    - Any ad account creation or ad purchase
    - Publishing or changing public business info (GBP, website, social)
    - Contacting customers, including review requests
    - Granting account credentials
    - Any scope addition

# Round 1 questions for the owner (answers unblock the contract)

1. **Q1, what is "results"?** More booked estimates, more revenue, or a number? What is the current baseline per month?
2. **Q2, is the $6k all-in, or are ad dollars separate?**
3. **Q3, what services make the money, and what is your service area?** Residential, commercial, or both?
4. **Q4, can you grant access to GBP, the website, and analytics this week? Who answers leads, and how fast?**
5. **Q5, when do you need the first booked jobs, and where are you located?** Location sets the real spring date.

I'm stopping at round 1. Round 2 is only needed if the answers raise new branches. Mark the assumptions A1–A5 as unconfirmed until the owner responds.

**Recommendation for the agreement:** Define success as booked estimates and a tracked pipeline by Mar 20, not revenue. A revenue promise on $6k in a four-month off-season window is not one we can make honestly.

```yaml
JAIL-HANDOFF:
  skill: jail-task-contract
  status: partial — draft, not ship-ready (UNKNOWN: field 3 target, field 2 budget scope, field 8 inputs)
  facts: [landscaping company; $6k budget; spring 2027 deadline; owner wants marketing fixed]
  assumptions: [A1 spring ~Mar 20 2027; A2 $6k all-in; A3 owner decides; A4 local service area; A5 access in 7 days]
  unknowns: [success metric and baseline; budget scope; service area and offer; access; location]
  outputs: [draft contract, fields 1-14]
  next: jail-plan (after owner answers Q1-Q5) — or jail-research for local market conditions
  approval_required: [$6k commitment; ad purchases/accounts; public business info changes; customer contact/review requests; credentials; scope additions]
```

I haven't saved this to the project, since it's a draft for one owner. I can save it as `claude/prospect-landscaping-marketing-contract.md` once you confirm.