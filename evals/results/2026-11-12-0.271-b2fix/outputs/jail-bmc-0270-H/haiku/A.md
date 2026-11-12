# JAIL-BMC: Mobile dog-grooming van business

**Decision this serves:** Should you add a third van?
**Short answer:** Not yet. A third van adds profit only if it brings in at least **139 new regular customers**, about 45% growth on today's 310. Your current margin is thin, so the first moves should be to measure churn and van capacity and to test price, before buying a van.

**Method:** Inline fallbacks ran in place of the sub-skills (task-contract, research, red-team, decide, summarize, verify). jail-lab was not run. All figures are yours, unverified, so every element is labeled HYPOTHESIS. **No element is VALIDATED yet** because none has a checkable evidence ref.

## 1. Nine-block canvas

| Block | Element | Label (V/H) | Evidence ref | Confidence |
| :-- | :-- | :-: | :-- | :-: |
| Customer segments | 310 regular dog owners on a recurring schedule, about every 6 weeks | H | none (user-stated; check against booking export) | Medium |
| Value propositions | Groom at the customer's door, no drop-off, $95 per visit | H | none (why customers stay is untested) | Low–Med |
| Channels | Rebooking at each visit; referrals (assumed, not measured) | H | none | Low |
| Channels | New-customer acquisition: no channel data, CAC unknown | H | none | Low |
| Customer relationships | Recurring appointments, about 8.7 visits per customer per year | H | none | Medium |
| Revenue streams | $95 × 0.722 visits per customer per month = $68.61; about $21,269/mo, $255k/yr | H | none (arithmetic on user figures) | Medium |
| Revenue streams | Add-ons, tips, cancellation fees: unknown, not modeled | H | none | Low |
| Key resources | 2 vans, presumed one groomer each | H | none | Medium |
| Key resources | Customer list and booking system | H | none | Low |
| Key activities | Routing, scheduling, grooming, van upkeep | H | none (time per groom unknown) | Low |
| Key partnerships | None stated; supplies, fuel, insurance unknown | H | none | Low |
| Cost structure | Van + groomer $9,500/mo per van, $19,000 for two, 89% of revenue | H | none (fixed vs variable unconfirmed) | Medium |
| Cost structure | Cost per groom at current density ≈ $85 | H (derived) | none | Medium |

## 2. Internal inconsistencies and findings

- **F1. Thin margin.** Monthly surplus is about $2,269 on $21,269 revenue (10.7%). A small rise in churn, a slower visit cycle, or a cost increase erases most of it.
- **F2. Growth thesis.** A third van is profitable only above 139 net new customers. Below that it loses money, and at 100 customers it loses about $2,639 a month.
- **F3. "Fixed" cost vs. groomer pay.** The $9,500 is treated as fixed. If the groomer is paid per groom, part of it is variable and the break-even moves.
- **F4. Cycle assumption.** Revenue assumes every customer keeps the 6-week cycle. A customer on an 8-week cycle is worth 25% less.
- **F5. Capacity is unproven.** Current volume is about 112 grooms per van per month (about 5 per working day at 22 days). If vans are already full with a waitlist, the third van serves demand you already have. If they have open slots, it adds no revenue.

## 3. Unit-economics worksheet

Inputs are H (user-stated). Churn and CAC are placeholders, not data.

| Step | Calculation | Result |
| :-- | :-- | --: |
| Revenue per customer per month | 95 × (52 ÷ 6) ÷ 12 | $68.61 |
| Cost per customer per month (fully loaded) | 9,500 ÷ 155 | $61.29 |
| Margin per customer per month | 68.61 − 61.29 | $7.32 (10.7%) |
| Lifetime at 3% churn (placeholder) | 1 ÷ 0.03 | 33 months |
| Monthly discount rate (10%/yr, chosen) | 1.10^(1/12) − 1 | 0.797% |
| LTV, discounted, 3% churn | 7.32 ÷ (0.00797 + 0.03) | $193 |
| Max CAC for LTV:CAC = 3 | 193 ÷ 3 | $64 |
| CAC payback at an illustrative $100 CAC | 100 ÷ 7.32 | 13.7 months |
| Break-even customers per van | 9,500 ÷ 68.61 | 139 (≈100 grooms/mo) |

**Sensitivity:**
- At 2% churn, LTV is $262 and max CAC is $87. At 5% churn, LTV is $126 and max CAC is $42.
- **Marginal view:** if a new customer fills a van that is already paid for, the margin is closer to the full $68.61 minus variable supply costs (unknown). That gives a far higher LTV, but it only holds if the van has spare capacity (F5).
- **Churn cost:** while van cost is fixed, each customer you lose costs about $69 a month in revenue.

**Third-van incremental profit (fully loaded):**

| Customers on van 3 | Monthly profit change |
| --: | --: |
| 0 | −$9,500 |
| 60 | −$5,383 |
| 100 | −$2,639 |
| 139 | ≈ $0 |
| 155 | +$1,134 |
| 200 | +$4,222 |

**Price lever:** +$5 per groom on the current base adds about +$1,120 a month (about half of current surplus), assuming no churn response.

## 4. Top risky assumptions and experiments

Ranked by impact if wrong × evidence weakness, cheapest decisive test first:

1. **A-cap: Are existing vans full?** Impact: if not, no van is needed. Evidence: none.
   - **E0 (1 week, no cost):** Pull 12 months of booking and payment data. Metric: booked hours ÷ available hours per van, weekly. Pass: vans are ≥85% booked in peak weeks with a waitlist. Fail: below 80% means no van.
2. **A-churn: What share of customers leaves each month?** Impact: LTV and all of the above. Evidence: none. Measured in E0 from the same export.
3. **A-cost: Is the $9,500 fixed?** Impact: break-even moves. Evidence: none. Split the cost into fixed and per-groom pay in E0.
4. **A-demand: Can 139+ net new recurring customers be won and kept?** Impact: decides the purchase. Evidence: none.
   - **E2 (jail-lab runnable, 60 days):** Referral offer to the 310 customers: one free groom credit when a referral books a second groom. Metric: new customers with ≥2 grooms, direction up. Pass: ≥40 in 60 days (on pace for 139 in about 6 months). Fail: <20. Cost cap: set by you.
5. **A-price: Will customers accept +$5?** Impact: +$1,120/mo lever.
   - **E3 (60 days, one route):** Test +$5 on new bookings against a control route. Pass: churn rises less than 1 point and revenue per customer rises $5. Fail: churn rises more than 1 point.

**Sequence:** E0 → E2 → E3 → decision gate.

## 5. Customer validation questions

1. If you could book every 4 weeks, would you? What would stop you?
2. What made you choose a van over a salon?
3. Would you pay $100 for the same visit? At what price would you switch?
4. Have you ever stopped booking? Why?
5. Would you refer a friend for a free groom credit?

## 6. Strategic implications and next actions

- **Do not buy van #3 on current evidence.** Revisit after E0 and E2 (60–90 days).
- **Buy van #3 only when all of these hold:**
  - Existing vans are at least 85% booked in peak weeks, with a waitlist.
  - There are at least 139 net new recurring customers booked, or a proven pace of about 23 a month for 3 months.
  - The $9,500 is split into fixed and variable and confirmed.
  - Churn and CAC are measured, and LTV:CAC is at least 3 on those numbers.
  - You have cash to cover the ramp. At 60 customers, the van loses about $5,400 a month.
- **Margin before volume:** the price test (E3) is the fastest lever.
- **Next action this week:** export 12 months of bookings and payments, and get the cost breakdown and groomer pay structure.

**To move elements to VALIDATED:** send the booking/payment export. It would cover customer count, visit cadence, churn, price, and grooms per van, and I'd relabel each element with its evidence ref.

## Sources appendix

- User-provided figures in this session (2026-11-12): 2 vans, 310 regular customers, $95 average per groom, one groom every 6 weeks, $9,500/month per van.
- No external sources. No market validation has been assumed. Market size, competitor pricing, and local demand are not in the canvas.

```yaml
JAIL-HANDOFF:
  venture: mobile dog-grooming van business (2 vans operating)
  stage: operating
  decision: add van #3? -> defer to 60-90 day gate
  canvas: complete; 13 elements, all H; 0 VALIDATED (no evidence refs yet)
  key_numbers: revenue 21269/mo; van cost 19000/mo; surplus 2269/mo (10.7%); per-customer margin 7.32/mo; van break-even 139 customers
  assumptions: [A-cap, A-churn, A-cost, A-demand, A-price]
  experiments: [E0 data pull, E2 referral pilot, E3 price test] -> jail-lab
  open_gaps: churn, CAC, fixed vs variable cost, van capacity, service-area geography, add-on revenue
  next_action: E0 booking/payment/cost export
```