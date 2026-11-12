# Worked example — FULL SWEEP with one re-attack round

Synthetic scenario. Firm, numbers, and people are invented for illustration.

## Input

> Poke holes in this before I send it to my partners: "Harbor Ledger, a
> 12-person bookkeeping firm with 140 clients, will double revenue next year
> by raising prices 25% across the board. Our clients love us, so churn will
> not change." Sources: [1] the plan paragraph above; [2] last year's client
> list with fee amounts, supplied by the owner.

## Output

```
LANE: FULL SWEEP. Consequential (price change touches every client, hard to
reverse) and contested (two partners disagree). A lighter lane would under-serve it.

STEELMAN: Harbor Ledger has not raised fees across the board in years [2],
clients rely on the firm for monthly close and tax filing, and switching
bookkeepers is a real hassle. A 25% rise on an under-priced book lifts revenue
with no added headcount. If churn stays low, margin improves sharply. The
plan's logic is sound if price sensitivity is low.

RED-TEAM FINDINGS (ranked by severity x likelihood)
1. "Churn will not change" is unsupported, and the plan needs it — severity: critical
   · basis: Fact [1] the plan states it with no data; Inference: a 25% rise is
   large enough that some clients will compare alternatives, and the plan's own
   goal (double revenue) cannot be met by price alone, since 1.25x is not 2x.
   → fix: model the plan at 0, 10, and 20 percent churn before sending.
   → falsifier: 5 structured calls with the firm's 5 largest-fee clients
     (last time they compared providers, what they pay elsewhere, what rise
     would make them look). Confirms: 2 or more say they would shop around.
     Disproves: all 5 accept without trading down.
     · falsifier-status: HANDOFF → owner: managing partner; jail-lab spec:
       5-call script, 2 weeks, pass line pre-set at fewer than 2 shoppers.
2. Revenue arithmetic does not reach "double" — severity: critical
   · basis: Inference from Fact [1]: a 25% increase on the same client count
   gives 1.25x revenue, so doubling needs about 60% more clients or scope too.
   → fix: restate the goal as +25% at flat churn, or add a named growth lever.
   → falsifier: multiply last year's fee total from [2] by 1.25.
     · falsifier-status: RUN-NOW → result: confirmed (1.25x, not 2x).
3. A uniform 25% rise treats all 140 clients alike — severity: major
   · basis: Judgment (no fee-by-client margin data was provided; [2] gives fees only).
   → fix: segment by margin and fee level; rise more where underpriced.
   → falsifier: 1:1 interview with the partner who runs the smallest-fee
     clients, and a fee-versus-hours check on 10 clients.
     · falsifier-status: HANDOFF → owner: operations partner.
4. Staff capacity if volume holds but complaints rise — severity: minor
   · basis: Judgment.
   → fix: plan who answers the first 20 pushback calls.
   · falsifier: Reference class: check how the firm handled its last fee change.
     · falsifier-status: HANDOFF → owner: office manager.

Survives the attack: the firm is under-priced relative to the value clients
describe, and some increase is likely justified.

Verdict (round 1): RETHINK — findings 1 and 2 are critical and the headline
claim does not follow from the plan.

RE-ATTACK LOG
Round 1 fixes: goal restated to +25% at flat churn; churn modeled at 0/10/20%;
rise tiered by fee level.
Round 2 (fresh reviewer, fixed version): finding 2 closed; finding 1 downgraded
to major, since the 5 calls are scheduled but not done; new finding: tiering
rule not yet tested on 10 clients (major, HANDOFF to operations partner).
Open after round 2: findings 1 and 3, new tiering finding. Escalated to the
managing partner.
Final verdict: PROCEED-WITH-FIXES — do not send the "double revenue" claim;
send the +25% tiered plan only after the 5 client calls report.
```

```yaml
JAIL-HANDOFF:
  skill: jail-red-team
  status: partial
  facts: ["Plan states 25% rise and unchanged churn, no data [1]", "1.25x revenue at flat client count (RUN-NOW, confirmed)"]
  assumptions: ["Fee totals in [2] are current; no change in service scope"]
  unknowns: ["Client price sensitivity", "Margin by client", "Capacity to absorb pushback"]
  outputs: ["Ranked findings with falsifiers", "Re-attack log, 2 rounds", "Verdict PROCEED-WITH-FIXES"]
  evidence: ["[1] plan paragraph, owner message, 2026-11-12", "[2] client fee list, owner supplied, 2026-11-12"]
  risks: ["Churn above 10 percent erases the gain", "Uniform rise hits low-margin clients"]
  confidence: medium
  next: jail-decide
  approval_required: ["Client calls need the managing partner to approve contact"]
```
