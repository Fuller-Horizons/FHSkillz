# JAIL-DECIDE: Nassau County expansion

**Package withheld.** I can't tell who "we" is, and nothing in the project covers a Nassau expansion. I searched the project docs, and the only Nassau mentions are an unrelated prospect brief (Hicks Nurseries) and a generic geo-expansion prompt. Any recommendation now would rest on assumptions.

## Step 1: Frame
- **Decision:** Whether to expand into Nassau County, NY.
- **Owner:** Unknown.
- **Needed by:** Open. No real date was given, and I won't invent one.
- **Who "we" is:** This could be Signal Results Group, a client such as the Suffolk-based Harbor Ridge Mechanical, or another business. It changes everything below.

## Criteria (set before any option is scored)
1. **Demand:** Is there enough addressable demand in Nassau to justify entry?
2. **Unit economics:** Does the expansion pay back within a tolerable window?
3. **Competitive position:** Can you win against incumbents there?
4. **Capacity and attention:** Can the current team absorb it without hurting the core business?
5. **Reversibility:** How much is sunk if it fails?
6. **Regulatory fit:** Do licensing, permits, or labor rules differ?

All six are **judged on assumption** right now. Confidence is capped at **low**.

## Options (framework only, not scored)
| Option | Door type | Price of the option |
|---|---|---|
| **Do nothing / defer** | Two-way | Forfeits Nassau demand each month, plus any competitor head start. It can't be priced until the market is known. |
| **Test entry** (partner, referral, one account or contract) | Two-way | Small spend and attention. Tests criteria 1–3 cheaply. |
| **Serve from the existing base** (travel radius, no new office) | Mostly two-way | Mid cost. Tests demand without a fixed footprint. |
| **Full entry** (staff, office or yard, marketing) | One-way | Highest cost and hardest to reverse. |

This is only a framework. The cost and risk columns stay empty because no inputs exist. I did not invent numbers.

## Ship-check
`Ship-check: criteria-first PASS · do-nothing priced FAIL · door type per option PASS · ≥2 change-conditions FAIL · every number carries Fact/Estimate+source PASS (no numbers used) · owner named FAIL · council check recorded PASS (not convened, because the question isn't yet contested or high-stakes)`

## What closes the FAILs
1. **Who is "we"?** What business, and what does it do today? Who decides?
2. **Where do you operate now?** (Suffolk only? Revenue and capacity roughly, as bands.)
3. **What's driving the question?** (Inbound demand, a client, a competitor move, a growth target?)
4. **Constraints:** Budget ceiling, hiring capacity, and any date that matters.
5. **Any data in hand?** (Nassau leads, win rates, pricing.)

## JAIL-HANDOFF
```yaml
JAIL-HANDOFF:
  skill: jail-decide
  status: blocked
  facts: [No project doc defines the entity or a Nassau expansion thesis]
  assumptions: [All six criteria judged on assumption]
  unknowns: [Entity, owner, current footprint, demand, budget, deadline]
  outputs: [criteria set, option skeleton, ship-check]
  risks: [Confident call on no evidence]
  confidence: low
  next: jail-research
  approval_required: [Any final expansion commitment, which is a one-way door for full entry]
```

Answer the five questions above and I'll rerun this. If you'd rather start with evidence, I can run **jail-research** on Nassau market size, competitors, and licensing first.