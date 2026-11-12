**Not ready to send.** The memo doesn't name a decision owner, so I've withheld the package. Below is a working copy with everything else fixed. Add one name and it can go out.

**Ship-check, as received:**
```
Ship-check: criteria-first FAIL · do-nothing priced FAIL · door type per option FAIL · ≥2 change-conditions FAIL · every number carries Fact/Estimate+source FAIL · owner named FAIL · council check recorded FAIL
```
The main problems: the do-nothing option wasn't priced, the recommendation rests on a 5-year cost comparison that isn't in the stated criteria, and the $64k vs $81k comparison isn't like-for-like (the lease includes a service plan and the purchase doesn't, and the purchase leaves you owning a machine).

**Working copy (HELD, not for sending):**
```
DECISION PACKAGE — HELD
Decision: Replace 2011 CNC router: buy Router X ($64,000 cash) or lease Router Y ($1,350/mo × 60)
Owner: [NAME REQUIRED] · Needed by: open (memo dated Nov 10)

Criteria (set before scoring): 1) upfront cash; 2) 5-year total cost, incl. service; 3) uptime; 4) delivery speed. Weights: not set; owner to confirm.

Evidence (requester's figures, Nov 10 memo):
- Old-router repairs: $9,200, 4 repairs this year [Fact, requester]
- Router X price: $64,000 cash [Fact, requester; quote to attach]
- Router Y payments: $1,350 × 60 = $81,000 [Fact, arithmetic]
- Lead time on new router: 10 weeks [Fact, requester; confirm which model]
- Inventory cash need: not quantified [Unknown]
- Router Y delivery date, service terms, early-exit/buyout terms: not supplied [Unknown]

Options:
| Option | Benefits | Costs | Risks | Door | Delay cost |
|---|---|---|---|---|---|
| 0. Keep old router | No cash out now | ~$900/mo repairs [Estimate: $9,200 YTD ÷ ~10 mo] plus unpriced downtime | Breakdown during production | Two-way | ~$900/mo |
| A. Buy Router X | Owned asset; $64k vs $81k before service and resale [Estimate] | $64k cash now; service cost unknown | Cash tied up; 10-week wait | One-way (cash spent; resale unknown) | ~$2,000 over the 10-week wait [Estimate] |
| B. Lease Router Y | Keeps cash free; service plan included [requester] | $81k over 60 months [Fact] | 60-month obligation; uptime and delivery unverified | One-way unless early exit exists [Unknown] | Delivery date unknown |

Break-even [Estimate]: the lease payments have a present value of about $64k at a 9.7% annual discount rate. The lease is cheaper only if the cash would otherwise earn more than about 10% a year. This ignores the resale value of an owned machine, service costs on Router X, and taxes.

Recommendation: Lease Router Y (provisional). Confidence: LOW. The deciding criterion is upfront cash, and the cash need is unquantified. On cost alone, buying wins unless capital costs more than ~10%. Uptime and delivery for Router Y are judged on assumption.

Would change this call:
1. Inventory cash need is small, or financeable below ~9% → buy Router X.
2. Lease has no early exit or buyout, or the service plan excludes repairs → re-price before signing.
3. Router Y delivers later than 10 weeks → re-compare repair exposure.
4. Router X quote includes a comparable service plan → buying likely wins on total cost.

Approval required: Signing the 60-month lease ($81,000 commitment). Decision owner only; do not sign yet.
Council: not convened. One unquantified input; gather evidence first.

Next actions:
1. Owner: name the decision owner.
2. Requester: quantify the inventory cash need; get written terms for Router Y (early exit, service coverage, delivery date) and the Router X service cost.
3. Owner: decide after items 1–2. No signature before then.
```

**Ship-check, after fixes:**
```
Ship-check: criteria-first PASS · do-nothing priced PASS · door type per option PASS · ≥2 change-conditions PASS · every number carries Fact/Estimate+source PASS · owner named FAIL · council check recorded PASS
```

**What closes the owner gate:** Who has authority to sign a $81,000 lease? Send me that name and I'll re-run the ship-check and release the package. Also, the memo is dated Nov 10, but today is Nov 12. Should I date it today?

The package also fails the evidence bar on the deciding criterion. Cash need is unquantified, so I'd send it as "lease, provisional" with a note that items 2 and 3 are open, not as a firm recommendation.

JAIL-HANDOFF
next: jail-research (inventory cash need, Router Y lease terms, delivery dates) → jail-red-team (one-way 60-month commitment, before signing)