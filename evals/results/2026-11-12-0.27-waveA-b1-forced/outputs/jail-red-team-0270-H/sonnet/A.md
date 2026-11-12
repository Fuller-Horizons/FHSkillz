# RED-TEAM: First salesperson hire to reactivate 300 dormant customers

**Lane:** THREE LENSES. The stakes are real, roughly $30–40k at risk, but the move is reversible, so I didn't run the full sweep.

**Steelman:** You have 300 customers who already bought, which is the warmest list a new rep can get. A $65k base plus commission keeps fixed cost modest and ties upside to results. Calling existing customers needs less sales skill than prospecting new ones, and four months is short enough to cut losses if it fails.

**Assumptions I used (yours to correct):** loaded cost is about 1.2× base. Recruiting and onboarding add about $5k. Contribution margin is 40–50%. The hire starts in month 1 and the first month is mostly ramp. The reactivation rate range is a benchmark estimate, not data from your list.

## RED-TEAM FINDINGS (ranked by severity × likelihood)

1. **The 4-month payback only works under narrow conditions** — severity: critical · basis: Inference: the arithmetic below.
   - Cost over 4 months is about $26k loaded base plus about $5k setup, so roughly $31k before commission. At 40–50% margin she must generate $62–78k of collected revenue.
   - With about 1 month of ramp, that is $21–26k per selling month.
   - At a $5k average first order, that is about 13–16 reactivated customers from 300, or 4–5% within about 3 months. That is the optimistic end of cold reactivation.
   - At $1k orders it can't happen. At $25k+ it's easy. Everything depends on your deal size and sales cycle, which the plan doesn't state.
   - Any sales cycle longer than about 60 days pushes revenue past the 4-month window, even if she sells well.
   - → Fix: define "pay for herself" as collected gross margin versus fully loaded cost. Then either extend the window to 6–9 months or confirm that your cycle and deal size fit.
   - → falsifier: back-solve breakeven from your real average order, margin and cycle length. · falsifier-status: **RUN-NOW → result: confirmed, conditional.** It fails for any average first order under about $4k or any cycle over about 60 days, and it passes comfortably above about $15k. I can't resolve this without your deal numbers.

2. **The dormant list is an untested asset and the plan's whole engine** — severity: critical · basis: Inference: the plan has no revenue source beyond this list, and nothing says why these customers went dormant.
   - Customers who lapsed often did so for a reason, such as price, a bad experience, a lost need or a competitor. Contact data is also usually stale. A common pattern is 10–20% connect rates and low-single-digit conversion.
   - 300 names, called 5–6 times each, are exhausted in about a month. After that she has no pipeline and has to prospect cold, which is a different job.
   - → Fix: don't hire yet. Run the test below first.
   - → falsifier: you or a team member call 30 randomly chosen dormant customers in one week. Track connect rate, conversations, interested leads, meetings and orders. Confirmed if the extrapolated conversion is under about 2%. Disproved if you get 3 or more real opportunities from 30. · falsifier-status: **HANDOFF → owner: Jonathan, about 1 week, spec: random sample, same script, log outcomes and each customer's stated reason for lapsing.**

3. **The first sales hire fails despite good execution: no process, no collateral, no coach** — severity: major · basis: Judgment.
   - A first rep with no CRM hygiene, no script, no offer, no reporting and no manager usually spends the first 6–8 weeks guessing.
   - A rep experienced enough to work alone expects more than $65k base. A junior rep needs coaching you may not have time to give. Which one are you hiring?
   - → Fix: before the offer, write the call script, the reactivation offer, the target list segments, a weekly activity and outcome scorecard, and who manages her.
   - → falsifier: can you hand a candidate a one-page playbook and a CRM export on day 1? If not, the finding stands. · falsifier-status: **RUN-NOW → result: confirmed on the information in hand.** The plan mentions none of these.

4. **Compensation and success are undefined** — severity: major · basis: Inference: "commission" is the only comp detail given.
   - There is no commission rate, no quota and no ramp or guarantee. There is no rule on whether reactivated customers count as "new" revenue, and no view on whether you'd be paying commission on revenue the customers would have given anyway.
   - Disputes about list ownership and attribution tend to start after the first few wins.
   - → Fix: write the comp plan before the offer: rate on margin or on revenue, a 90-day ramp, a clear definition of a "reactivated" account, and a cap or clawback for returns and non-payment.
   - → falsifier: model the same comp plan at the worst, expected and best case, and see whether you can afford all three. · falsifier-status: **HANDOFF → owner: Jonathan, a 30-minute spreadsheet.**

5. **Missing options: do-nothing, founder-led, and cheaper alternatives** — severity: major · basis: Judgment.
   - Option not written down: you run a 2-week reactivation sprint yourself with email, SMS or a call day, which costs about $0 in hiring and gives you the data from finding 2.
   - Other options: a part-time or contract SDR, or commission-only for the first 90 days.
   - There are also no kill criteria. If month 4 misses, do you keep going, extend or let her go? A plan that can't fail is faith, not strategy.
   - → Fix: set tripwires in advance, such as month 2 with at least X conversations per week, month 3 with at least Y open opportunities, and month 4 with at least Z collected margin. Below the tripwires, you act on the pre-agreed decision.
   - → falsifier: if the founder-led sprint produces at least 3 real opportunities from 30 calls, the hire is justified, but on a longer window. · falsifier-status: **HANDOFF → Jonathan.**

6. **Compliance and data hygiene** — severity: minor · basis: Judgment: it depends on whether your customers are businesses or consumers.
   - If any are consumers, check Do-Not-Call and TCPA rules before calling. B2B calling is generally lower risk.
   - → falsifier: check whether the list has consumer numbers or mobile numbers. · falsifier-status: **HANDOFF → Jonathan.**

**Survives the attack:** hiring to monetize an existing relationship base is a sound instinct, and calling past customers is the cheapest sales motion there is. The base salary is reasonable for a first hire. The weak point is the 4-month promise and the lack of any pre-hire test, not the idea of hiring.

**Verdict: PROCEED-WITH-FIXES.** Run the 30-call test and write the comp plan and playbook first. If the test shows under 2% conversion, move to RETHINK and don't hire until the lapse reasons are understood.

---

**JAIL-HANDOFF**
- next: **producer** (run the 30-call test, then write the comp plan, playbook and tripwires), then **jail-decide** to re-choose between hire now, hire later and founder-led, using the test results.
- open questions for you: average first-order value, gross margin, typical sales cycle, B2B or consumer, and why the 300 went dormant. With those I can replace my assumptions with real breakeven numbers.
- Not saved to the project. I can add this to "Business Consulting Tools" if you want it kept there.