**DECISION PACKAGE**
**Decision:** Which dispatch fix to commit to · **Owner:** you (business owner) · **Needed by:** 2026-12-15 (33 days out)

**Evidence base.** Facts you supplied: hire at $52k/yr fully loaded; software at $400/mo plus $3,000 setup; overtime at about $1,800/mo. Unknown: whether overtime comes from dispatch time or from technician count and demand spikes; how many calls go unbooked; your gross margin; software contract terms. I ran no outside research.

**Criteria (set before scoring):**
1. Net annual cash effect against current overtime
2. Recovered capacity (missed or late-booked work)
3. Reversibility: the cost of being wrong
4. Time to relief before the winter peak
5. Owner attention and adoption risk

Criteria 2 and 4 are **judged on assumption**. Confidence is capped accordingly.

**Pricing (Estimates from your figures):**
- Do nothing: $21,600/yr overtime (assumes a steady rate). Lost calls and technician burnout are unpriced.
- Hire: $4,333/mo. Even if it removed all overtime, the net cost is $2,533/mo, or about $30,400/yr. It must recover that from booked work.
- Software: $7,800 in year one, $4,800/yr after. It pays for itself on overtime alone only if it cuts overtime by about 36% in year one, or about 22% from year two.

| Option | Benefits | Costs | Risks | Door type | Cost of delay |
|---|---|---|---|---|---|
| 3. Do nothing | None new | $21.6k/yr overtime | Overtime and missed jobs compound | Two-way | $1,800/mo plus unpriced lost work |
| 1. Hire second dispatcher | Capacity and coverage | $52k/yr | Overpaying if dispatch isn't the bottleneck; ramp time | One-way in practice | Waiting costs less cash than hiring |
| 2. Software now | Less dispatch time per job | $7.8k in year one | Adoption; may not fix root cause | Mostly two-way; $3k setup is sunk | About $1,800 × X − $400/mo forgone, where X is the overtime cut |
| 4. Software now, hire gated | Same as 2, plus a hire if a trigger is hit | Same as 2 | Slower capacity if the trigger fires late | Two-way at each gate | Same as 2 |

**Recommendation: Option 4, software first with a gated hire.** Overtime alone ($1,800/mo) cannot justify a $4,333/mo hire. The software pays back if it cuts overtime by about 36%, and a trial can test that before you sign. The hire is the hard-to-reverse option, and waiting costs less cash than hiring does.

**Confidence: low overall.** The hire-not-justified-on-overtime result is high confidence, since it is arithmetic from your numbers. The software's benefit is judged on assumption.

**Would change this call:**
1. Dispatch is not the bottleneck (overtime comes from technician count or demand spikes). Neither option fixes that.
2. Lost work exceeds about $2,500/mo in gross margin. A hire then becomes competitive now.
3. A trial shows the software cuts dispatch time by less than about a third. Drop option 2.
4. The vendor requires a 12-month-plus commitment. The door becomes one-way, so raise the bar.

**Approval required:** the $3,000 setup, any software contract, and any hire offer. You decide.

**Next actions:**
1. You, by Dec 1: pull four weeks of data on overtime hours by cause, missed or unanswered calls, and late-booked jobs.
2. You, by Dec 10: trial two or three dispatch tools on your real schedule. Ask for month-to-month terms and a setup-fee waiver.
3. You, Dec 15: sign or pass on the software, and set a Feb 15 checkpoint against the hire trigger.

**Decision log (proposed):** context: dispatch bottleneck, $1,800/mo overtime · decision: software first, hire gated · consequences: $7.8k year-one spend; hire deferred · status: proposed

**Council:** not convened. The question is not contested, and the gap is missing data, which a council cannot supply.

**Ship-check:** criteria-first PASS · do-nothing priced PASS · door type per option PASS · ≥2 change-conditions PASS · every number carries Fact/Estimate+source PASS · owner named PASS · council check recorded PASS

```
JAIL-HANDOFF
next: jail-red-team
reason: money commitment ($52k hire or $7.8k software), partly irreversible
target: option 4 (software first, hire gated)
open: benefit side judged on assumption; four-week data pull pending
```