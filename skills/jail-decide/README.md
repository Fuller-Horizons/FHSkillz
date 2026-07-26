# jail-decide

Turn a choice and the facts you have into one clear, defensible pick.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.2.1.

## What it does

You give it a decision and the facts behind it. It writes the judging criteria first, before it looks at any option — so a favorite option can never rig its own scoring. It prices every option, including doing nothing, by benefits, costs, risks, and **reversibility** (can you undo it, or is it a one-way door). It ends with one clear pick, a confidence level, and the exact facts that would flip the call.

## Use it when

- "Should we do X or Y" or "help me decide"
- You already have quotes, numbers, or research and need one clear recommendation
- A build-vs-buy call, a vendor switch, or any choice where "do nothing" is a real option hiding in plain sight

## Don't use it for

- Scoring one thing on its own, like a 0-10 rating — use [`jail-rate`](../jail-rate/) instead.
- Gathering the facts themselves — use [`jail-research`](../jail-research/) first, then bring the results here.
- Attacking the winning option's reasoning after the pick is made — use [`jail-red-team`](../jail-red-team/).

## What you get

A short decision package: priced options, one recommendation with its reasoning, a confidence level, and the conditions that would change the call. It closes with a one-line gate check that confirms the package met every rule before it shipped.

## Example

**You ask:**

> We need to decide on our Salesforce renewal before it auto-renews Sept 30. Our AE quoted $65,520/year for our 40 seats, and verbally offered 15% off for a 2-year deal. Separately, HubSpot quoted $28,800/year, but migration runs about $23,000 and their demo showed no real territory-management feature — our 40 reps are organized by territory. Our CFO wants a 20% cut to SaaS spend, but Q4 is our biggest quarter, with $2.1M in open pipeline. We must decide by Aug 15. I'm Maria Chen, VP of Sales — help me decide: renew as-is, take the discount, or switch to HubSpot.

**It produces:**

```
Ship-check: criteria-first PASS · do-nothing priced PASS · door type per option PASS · ≥2 change-conditions PASS · every number carries Fact/Estimate+source PASS · owner named PASS · council check recorded PASS

DECISION PACKAGE
Decision: Renew Salesforce as-is, negotiate a discounted 2-year renewal, or switch to HubSpot before the Salesforce contract auto-renews on Sept 30 · Owner: Maria Chen, VP of Sales · Needed by: Aug 15, 2026 (45-day notice deadline)

Criteria (weighted):
1. Cut SaaS spend toward the CFO's 20% target [High]
2. Protect Q4 pipeline — $2.1M open [High]
3. Keep the territory management and forecasting the 40 reps use [Medium]
4. Minimize lock-in [Medium]

...

Recommendation: Negotiate the 2-year Salesforce discount. It cuts spend now — $19,656 over two years versus do-nothing [see table] — without touching the system 40 reps depend on during Q4, their biggest quarter. HubSpot has bigger upside, a risk-adjusted EV of ~$35K–$50K over two years [Estimate], but the missing territory tool and Q4 timing make that risk premature. Do-nothing doesn't move the CFO's mandate.

Confidence: medium — discount isn't in writing yet; savings only partly meets the CFO's target.

Council: not convened — high-stakes but not contested; the tradeoff is risk tolerance, not a disputed fact.

Would change this call:
- No written 15% confirmation by Aug 15 → default to do-nothing, revisit HubSpot in Q1.
- HubSpot ships real territory management before Aug 15 → reopen the switch; it wins on cost.
- CFO rejects the 15% cut as insufficient → escalate the tradeoff to Maria and the CFO jointly.
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
