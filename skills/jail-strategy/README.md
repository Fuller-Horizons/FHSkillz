# jail-strategy

Turn a business situation into one strategy call you can act on.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.2.0.

## What it does

This skill runs one strategy analysis in three lanes. The **INTERNAL** lane sorts your strengths and weaknesses against outside chances and threats. That is a SWOT. It then turns the SWOT into moves you can act on, called a TOWS. The **MACRO** lane scans six outside forces: political, economic, social, tech, legal, and environmental. That is a PESTLE. Each force must tie to your actual decision, not just be a trend. The **FULL SWEEP** lane runs both off one shared set of facts, then checks where they collide.

## Use it when

- You want a straight SWOT before a go/no-go call: "where do we stand, and what should we do about it."
- You need a macro scan tied to one decision, not a generic trend list: "what's coming at us."
- You want the full picture, both lanes off one evidence set, before a big move like a market entry.

## Don't use it for

- Building the business model itself, block by block — use [`jail-bmc`](../jail-bmc/) instead.
- Rating one named subject on a 0-10 scale — use [`jail-rate`](../jail-rate/) instead.
- Gathering evidence with no strategy step at the end — use [`jail-research`](../jail-research/) instead.

## What you get

Sorted SWOT and/or PESTLE tables, each entry backed by a source. Then a TOWS table of moves you can act on, plus a dated source list and a short handoff block for whatever comes next.

## Example

**You ask:**

> We're deciding whether to launch a wholesale single-serve compostable coffee-pod line for independent boutique hotels in Oregon and Washington within the next 12 months. Give me the SWOT and TOWS before I take this to the board.

**It produces:**

```
# JAIL-STRATEGY — INTERNAL lane

**Subject:** Riverbend Roasters (Portland, OR specialty coffee roaster, ~40 employees, $9M FY2025 revenue). **Decision:** launch a wholesale single-serve compostable coffee-pod line for independent boutique hotels in Oregon and Washington. **Lane:** INTERNAL (SWOT → TOWS). **Scope:** OR/WA, independent/boutique lodging segment only (not hotel chains, not consumer retail). **Horizon:** 12 months.

...

## INTERNAL — SWOT

| Quadrant | Statement | Evidence ref | Materiality | Confidence |
| :--- | :--- | :---: | :---: | :---: |
| S | 94% 18-month retention across Riverbend's 61 wholesale-cafe accounts, evidencing reliable delivery and account service | [2] | H | H |
| W | No existing single-serve packaging line; both copacker quotes carry a 22-week tooling lead time before first production run — over 40% of the 12-month horizon | [3] | H | H |
| O | Cascade Hospitality Supply's amenity program opens its spring 2027 catalog refresh for new in-room coffee SKUs, and boutique-hotel guests increasingly expect an elevated in-room coffee experience [mechanism: refresh window + guest-expectation trend → an open distributor slot Riverbend could fill] | [5][8] | H | M |
| T | Oregon DEQ's SB 543 compostable-packaging rule requires state-certified compostability labeling before a food-contact pod can be marketed in-state, separate from and untracked against copacker tooling [mechanism: uncertified pod cannot legally ship into OR hotels regardless of copacker readiness] | [6] | H | M |

...

*Tie-break applied:* the missing-distributor-contact fact could read as a Threat (the external distributor market is hard to break into) — filed **W**: the proximate causal mechanism is Riverbend's own sales process (no rep assigned, no meeting booked), not an external condition.

*Cut, not classified:* "the CEO personally knows the GM of a boutique hotel group" was proposed as a Strength during classification and cut — no evidence ref exists for it beyond an anecdote; filing it would fabricate a specific to fill a gap. Fails closed per the constitution's evidence rule.
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
