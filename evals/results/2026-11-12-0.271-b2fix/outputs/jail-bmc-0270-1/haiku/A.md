# Business Model Canvas: Long Island Pool-Equipment Subscription

**Subject:** Monthly technician visits for residential pool equipment, $89/mo, Nassau and Suffolk counties, NY
**Stage:** Idea, no customers
**Decision served:** Whether to launch a pilot, and what to test before committing capital
**Research depth:** Standard search only. I read search snippets, not the underlying pages, so every price figure below has snippet-level confidence.

## Canvas

| Block | Element | Label (V/H) | Evidence ref | Confidence |
| :--- | :--- | :---: | :---: | :---: |
| Customer segments | Owner-occupied homes with in-ground pools, Nassau and Suffolk | H | none (no pool count found) | L |
| Customer segments | Pools 5+ years old with pumps, heaters, or automation that fail (hypothesized to drive buying) | H | none | L |
| Value propositions | Monthly equipment check (pump, filter, heater, automation) with a written condition report and early failure detection | H | none | L |
| Channels | Referral from pool-equipment installers and repair firms | H | none | L |
| Channels | Neighborhood social groups and local search ads | H | none | L |
| Customer relationships | Monthly subscription with a written report; repairs quoted separately | H | none | L |
| Revenue streams | $89/mo per home ($1,068/yr). Price is the founder's proposal, not tested | H | none | L |
| Revenue streams | Market price bands: full weekly service about $120–250/mo; biweekly about $80–180/mo; chemical-only about $100–160/mo | V | [1][2][3] | L–M |
| Revenue streams | Repair and parts billed on top of subscription | H | none | L |
| Key resources | Qualified pool-equipment technician(s) | H | none | L |
| Key resources | Vehicle, insurance, route and scheduling software | H | none | L |
| Key activities | Monthly equipment visits and report generation | H | none | L |
| Key activities | Route density management (stops per tech-day) | H | none | L |
| Key partnerships | Equipment installers and repairers (referral, but also potential competitors) | H | none | L |
| Key partnerships | Pool-supply retailers | H | none | L |
| Cost structure | Technician labor, about $30–45 per visit at a loaded rate of about $40/hr (rate and visit time assumed) | H | none | L |
| Cost structure | Vehicle, fuel, and insurance, about $12 per visit | H | none | L |
| Cost structure | Customer acquisition cost (CAC): no data | H | none | — |
| Cost structure | Card processing and admin, about $5.70 per customer per month | H | none | L |

**Labels summary:** 15 of 19 elements are HYPOTHESIS. The only VALIDATED element is the market price band, and it is a benchmark. It shows what competitors charge. It does not show that Long Island homeowners will pay $89 for equipment-only visits.

## Coherence pass

1. **Segment ↔ value proposition: holds with a gap.** The proposition is written for equipment health, which fits owners with aging equipment. It does not fit owners who only want cleaning. The segment definition needs an age or equipment condition filter to be specific enough to reach.
2. **Revenue ↔ segments: holds.** The homeowner pays, and no free "users" sit outside the revenue model. Property managers and HOAs are a separate segment and are not counted here.
3. **Finding: scope is undefined.** "Service pool equipment" does not say whether chemicals, cleaning, and parts are included. Every full-service competitor includes chemistry and cleaning. If this offer excludes them, customers keep a second pool vendor, and the $89 competes with a bundled $120–250 service. If it includes them, the margin falls further.
4. **Finding: seasonality contradicts 12-month billing.** Most Long Island in-ground pools are used roughly May through September (H; not verified). A flat $89 × 12 charges for about six months of low-need visits. Either the price is effectively $178 per active month, or winter visits waste labor. The plan needs a seasonal structure or a seasonal visit schedule.
5. **Unit economics: depend on unstated scale.** See the next section. Margin depends on visit duration and route density, and neither is known.
6. **Key activities ↔ value proposition: flagged, not evidenced.** Equipment repair often involves electrical work. Whether a non-electrician can perform the monthly check, and what licensing or insurance applies in Nassau and Suffolk, is unknown. This must be checked before launch. I have not assumed an answer.

## Unit economics (hypothesis model, not validated)

Assumptions: one visit per home per month; $89 price; labor at $40/hr loaded; vehicle $12 per visit; card processing 3%; admin $3 per customer. Excludes parts, chemicals, repairs, rent, and software beyond $3.

| Scenario | Visit + drive time | Labor | Total variable cost | Contribution/mo | Margin |
| :--- | :---: | :---: | :---: | :---: | :---: |
| A: efficient route | 45 min | $30.00 | $47.67 | $41.33 | 46% |
| B: sparse route | 65 min | $43.33 | $61.00 | $28.00 | 31% |

Lifetime value (contribution basis):
- A at 4% monthly churn (25-month life): about $1,033
- B at 6% monthly churn (about 17-month life): about $467

CAC ceiling (LTV ÷ 3): about $344 for A, about $156 for B. Payback at a $150 CAC: 3.6 months for A, 5.4 months for B.

**Dependency finding:** The model works only if routes are dense and visits are short (Scenario A). At 8 stops per tech-day and 21 working days, one technician covers about 168 homes. A pilot with 20 to 40 homes leaves the technician mostly idle, so early economics look like Scenario B or worse. Unit economics are therefore a function of scale, and the canvas does not yet show how many homes are needed in a single route cluster.

## Top risky assumptions and experiments

Ranked by impact if wrong × evidence weakness. Experiments follow the jail-lab spec shape. jail-lab was not run in this session. These are specs ready to hand off.

1. **Homeowners will pay $89/mo for equipment-only monthly visits** (impact H, evidence weak, comparable-based)
   - Metric: prepaid signups per qualified visitor, higher is better
   - Variable: price shown on the offer page ($89)
   - Bound: 14 days, about $400 ad spend, 10 hours setup, targeting Nassau and Suffolk owners
   - Threshold: at least 3% of at least 200 qualified visitors sign up (6+) → keep and continue. Below that → demote the price or the offer scope before building anything.

2. **Route density supports a positive margin** (impact H, evidence none)
   - Metric: average homes per tech-day within a 10-mile cluster, higher is better
   - Variable: service-area radius
   - Bound: desk exercise, one day, $0, using public addresses from a sample of permit or parcel data (if accessible)
   - Threshold: at least 8 homes per day in a single cluster → keep. Below that → narrow the service area before launch.

3. **Equipment visits find problems often enough to justify monthly service** (impact H, evidence none)
   - Metric: share of visits that produce a documented finding or fix, higher is better
   - Variable: monthly visit (versus no visit) in the pilot homes
   - Bound: 3 months, 10 homes, about 10 visits per month
   - Threshold: at least 40% of visits produce a finding → keep. Below that → the value proposition is "peace of mind" only, and it needs a different price or scope.

4. **Target channel reaches the segment at an acceptable CAC** (impact M, evidence none)
   - Metric: CAC per signup, lower is better
   - Variable: one channel only (start with installer referrals, the cheapest to test)
   - Bound: 45 days, $500 budget
   - Threshold: CAC at or below $150 → keep. Above that → test the next channel.

5. **Seasonal billing structure is acceptable to customers** (impact M, evidence none)
   - Metric: renewal rate after the first season, higher is better
   - Variable: seasonal plan (April–October) versus a 12-month plan
   - Bound: one season, the pilot homes from #3
   - Threshold: renewal at or above 70% → keep. Below that → revisit the price structure.

**Sequence (cheapest decisive first):** #2 (desk, $0, one day) → #1 (price test, about $400) → #4 (channel test, $500) → #3 (pilot, labor cost, three months) → #5 (season, runs with #3).

## Customer validation questions

For 15 to 20 Long Island pool owners:
1. What do you pay now for pool service, and what does that cover?
2. When did your pool equipment last fail or need repair, and how did you find out?
3. Would you pay a monthly fee for someone to check the equipment, and what would you need to see to keep paying?
4. Do you want cleaning and chemicals included, or do you already have someone for those?
5. Which months does your pool actually get used?
6. Who do you trust to recommend a pool equipment person?
7. At what monthly price would this be too expensive, and at what price would it seem too cheap to be serious?

## Sources (accessed 2026-11-12, snippet level)

[1] Fixr, "How much does it cost to maintain a swimming pool?" https://www.fixr.com/costs/swimming-pool-maintenance. National monthly service range $30–90. Note: conflicts with the other sources.
[2] HomeYou, Babylon and Bohemia NY pool service cost pages (generated estimates, not quotes). Babylon $175–182/mo; Bohemia $175–191/mo, four visits. https://www.homeyou.com/ny/pool-services-babylon-costs and https://www.homeyou.com/ny/pool-cleaning-bohemia-costs
[3] Pool-service pricing benchmarks, 2026 (search summary, not opened). Weekly residential service about $120–250/mo; biweekly $80–180; chemical-only $100–160; median submitted price $205/mo. Candidate source: https://pooldial.com/resources/articles/business/pool-service-pricing-benchmarks-2026. Attribution not confirmed.
[4] Thumbtack, Long Beach NY pool maintenance listing. Weekly cleaning about $86/mo. Low-quality source. https://www.thumbtack.com/ny/long-beach/swimming-pool-maintenance

**No source found:** Count of residential in-ground pools in Nassau and Suffolk. IBISWorld offers paywalled county data. Census and county permit records are the likely route.

## Strategic implications

- **The price is not the main question. Scope is.** Decide whether the offer is equipment-only or bundled before testing $89. The answer changes the competitive set and the margin.
- **Route density decides viability.** The business works only in a tight cluster. Launch in one town cluster, not all of Long Island.
- **The offer sits in a gap.** No direct comparable for monthly equipment-only service turned up. That could be an opening, or a sign that the buyer does not exist. The price test (#1) will show which.
- **Licensing is a gate, not an assumption.** Before taking customers, confirm with counsel or the relevant Nassau and Suffolk offices what is required for equipment checks and any electrical work.

## Next actions

1. Decide the scope: equipment-only, or equipment plus chemicals. (Founder, this week.)
2. Run #2 desk route test (one day, $0).
3. Draft the 14-day landing page and price test for #1 (about $400). Run it after the scope decision.
4. Schedule 15 owner interviews using the questions above.
5. Get a written licensing answer for equipment checks and electrical work in Nassau and Suffolk before any paid customer.

## SUCCESS-TEST

- **Labels intact:** every row is labeled V or H. Pass.
- **Coherence pass done:** six findings logged, including the scope gap, seasonality, and unit-economics dependency. Pass.
- **Top 5 assumptions carry experiments:** each has metric, variable, bound, and threshold, sequenced cheapest first. Pass. Experiments are specs, not runs.
- **No VALIDATED element lacks an evidence ref:** the one V row cites [1]–[3]. Pass, with the caveat that the evidence is snippet-level and the benchmark is not demand evidence.

**Fail-closed check:** The strongest V label in this canvas describes competitor pricing, not customer behavior. No element claims that a Long Island homeowner will pay $89. That claim stays HYPOTHESIS until experiment #1 produces signups.

## JAIL-HANDOFF

```
status: canvas complete (idea stage); 15 H / 1 V (benchmark only)
decision: pilot go/no-go pending scope decision
blocking: scope (equipment-only vs bundled); licensing for equipment/electrical work
next: #2 route desk test ($0) → #1 price test ($400) → #4 channel → #3 pilot
open data gap: Nassau/Suffolk residential pool count (not found)
re-run: jail-bmc canvas-delta mode after each experiment result
```

I did not write this to the Business Consulting Tools project, since it is a venture canvas rather than a consulting deliverable. I can save it there if you want it alongside the other project docs.