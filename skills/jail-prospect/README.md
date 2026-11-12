# jail-prospect

Research a private company before you approach it, buy from it, or partner with it.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.4.0.

## What it does

You give it a company name and a website. It checks free public sources: state business registries, court records, reviews, and job boards. It never guesses at private financial numbers. It scores the company and hands you a one-page brief you can act on.

It runs in two modes. PROSPECT checks if an owner might sell, or might need a consultant. SNAPSHOT checks a company you plan to buy from, compete against, or partner with.

## Use it when

- You want to know if a business owner might sell, before you reach out
- You want to spot gaps a consultant could fix and pitch
- You need to vet a vendor, competitor, or partner before you commit

## Don't use it for

- Rating how strong a business looks on paper, with no buy/pass call attached — use [`jail-rate`](../jail-rate/) instead.
- Public companies, or anything that needs paid data like PitchBook or ZoomInfo. This skill only uses free sources.

## What you get

A one-page brief: two 0–100 scores (Likelihood-to-Sell and Consulting-Opportunity), a rough size estimate built from public clues, red flags, an outreach hook, and a list of every source used. The size estimate is never a real revenue number.

## Example

_Ridgeline Powder Coating is a made-up company, used here to show the format. The skill runs the same checks on any real company you name._

**You ask:**

> Can you put together a prospect brief on Ridgeline Powder Coating, Inc.? It's a metal-finishing shop in Boise, Idaho... I want to know if he's a good brokerage prospect, or if there's a consulting angle instead if he's not ready to sell.

**It produces:**

```
# Prospect Brief — Ridgeline Powder Coating, Inc.
_Researched: 2026-07-25 · Researcher: jail-prospect · Free-sources-only_

## Snapshot
- **Legal entity / DBA:** Ridgeline Powder Coating, Inc. (ID · formed 2008 · active/good standing) — _Fact, Idaho SOS business entity search, accessed 2026-07-25_
- **Industry (NAICS):** 332812 — Metal Coating, Engraving (except Jewelry and Silverware), and Allied Services
...
## Scores
| Lens | Score | Band | Confidence |
|---|---|---|---|
| **Likelihood-to-Sell** | 75 | High | 62% |
| **Consulting-Opportunity** | 45 | Medium | 50% |

### Likelihood-to-Sell drivers
- Succession: Owner tenure 18 yrs since 2008 formation, no successor officer listed in most recent SOS annual report — _Fact, Idaho SOS business entity search, accessed 2026-07-25_
...
## Recommendation
**Pursue — brokering** · Confidence 62%
- Why: Succession and cleared-debt exit signals corroborate across two independent Tier-1 sources (Idaho SOS entity + UCC records); the consulting angle is secondary given thinner, single-source operational evidence and a size band that limits ability to pay for a full engagement.
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
