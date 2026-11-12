# Worked example — HVAC dispatch decision

Synthetic client. Input from the owner: "We're a 12-person HVAC company.
Choose between hiring a second dispatcher ($52k/yr loaded), buying dispatch
software ($400/mo + $3k setup), or doing nothing. Overtime is $1,800/mo now.
I need to decide by Dec 15."

## Output

```
Ship-check: criteria-first PASS · do-nothing priced PASS · door type per option PASS · ≥2 change-conditions PASS · every number carries Fact/Estimate+source PASS · owner named PASS · council check recorded PASS
```

```
DECISION PACKAGE
Decision: Pick a dispatch fix for the next 12 months · Owner: company owner (the requester) · Needed by: Dec 15, 2026

Criteria (stated before options): 1 Cut overtime cost [high]; 2 Keep cash
outlay low and recoverable [high]; 3 Keep dispatch reliable in busy season
[medium].

Options (do-nothing first):
| Option | Benefits | Costs | Risks | Door | Delay cost |
| Do nothing | None | Overtime $21,600/yr continues (User-provided) | Burnout, missed calls | Two-way | $320-$860/mo forfeited (Estimate) |
| Dispatch software | Overtime cut | $7,800 in year 1 (User-provided quote); EV +$840 to +$7,320 (Estimate) | Staff adoption; vendor claim untested | Two-way (monthly plan, assumed) | Same as above |
| Hire dispatcher | Capacity, coverage | $52,000/yr (User-provided); EV −$36,880 to −$32,560 on overtime alone (Estimate) | Fixed cost; hard to undo | One-way in practice | Not priced; extra-job value is Unknown |

Recommendation: Buy the software. It is the only option with a positive
expected value on the overtime numbers. Payback is about 3.5 to 9.4 months
(Estimate). It is easy to cancel, and it can be tested before a larger commitment.
Hiring costs more than the whole overtime bill, so only unmeasured benefits
could justify it.
Confidence: medium. Probabilities are estimates; break-even is 0.36 and the
low estimate is 0.40.
Council: not convened; no disputed fact, the numbers are the owner's own.
Would change this call:
- A 30-day trial shows less than 36% of overtime removed: stop and reconsider.
- Owner can show a hire would book enough extra jobs to cover the gap: reopen the hire.
- Software contract needs a long lock-in: treat it as one-way and re-run.
Approval required: Owner signs the vendor contract and any spend.
Next actions: 1 Owner asks vendor for a 30-day trial and month-to-month terms (by Nov 30). 2 Owner records current monthly overtime as the baseline (this week).
```

Numbers and method: [expected-value.md](expected-value.md).

```yaml
JAIL-HANDOFF:
  skill: jail-decide
  status: complete
  facts:
    - "Overtime is $1,800/mo, software is $400/mo plus $3,000 setup, hire is $52,000/yr loaded — User-provided by the owner"
  assumptions:
    - "Software can be cancelled monthly (to confirm with the vendor)"
    - "Horizon is the first 12 months"
  unknowns:
    - "Extra jobs a second dispatcher would book"
    - "Real share of overtime software removes (no pilot yet)"
  outputs: [decision package, expected-value worksheet]
  evidence:
    - "Owner's request message — all dollar inputs — 2026-11-12"
  risks:
    - "Probabilities are estimates; break-even 0.36 sits close to the low case 0.40"
  confidence: medium
  next: jail-red-team
  approval_required:
    - "Owner authorizes the software purchase and any vendor contract (Rule 5)"
```

Decision-log line for jail-memory (optional): `context: overtime $1,800/mo, 12-person HVAC firm · decision: buy dispatch software, trial first · consequences: hire deferred; revisit if trial < 36% overtime cut · status: proposed`
