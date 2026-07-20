---
name: jail-prospect
metadata:
  version: 1.2.0
description: >-
  Research a US private company as a business-brokering (sell-side) and consulting
  prospect using only FREE, authoritative sources. Use when evaluating whether to
  approach an owner about selling their business, or about a consulting engagement.
  Produces a one-page brief with a Likelihood-to-Sell score, a Consulting-Opportunity
  score, red flags, an outreach hook, and a fully cited source appendix. Triggers:
  "research this company", "is this a good brokerage prospect", "prospect brief",
  "should I approach this owner", "sell-side screen", "consulting opportunity".
---

# JAIL-PROSPECT — Company Prospect Research (brokering-led)

Turn a company name + website into a decision: **pursue as a brokerage prospect / pursue as a consulting prospect / pass / need more** — grounded only in free, authoritative sources, with every material claim cited.

## When to use
A user names a target company (or a list) and wants to know whether it's worth approaching the owner about selling the business or about a consulting engagement. Brokering (sell-side) is the primary lens; consulting is the secondary lens scored in parallel.

## Non-negotiable rules
1. **Free sources only.** No PitchBook, ZoomInfo, paid databases, or paywalled data. The catalog is in `references/free-sources.md`. If a fact is only available behind a paywall, mark it **Missing Evidence**.
2. **Label every line.** Each claim is one of: **Fact** (cited primary/official source) · **Source-Backed Inference** (cited, but interpreted) · **Analyst Judgment** (your read, no direct source) · **Missing Evidence** (unknown).
3. **No fabricated financials, ever.** Private SMB revenue/EBITDA/owner comp are not public. Never invent them. Provide only an **indicative size band** built from disclosed/derivable proxies (headcount × industry revenue-per-employee, federal awards, facility footprint), and state every assumption. This is triangulation, **not a valuation**.
4. **Cite or omit.** Every Fact and Inference carries a source URL + date accessed. No citation → it's Analyst Judgment or it's cut.
5. **Owner privacy / compliance.** B2B prospecting only. Capture business-relevant facts about the owner (tenure, public role, public statements), not personal data unrelated to the engagement. No scraping behind logins, no intrusive technical testing.
6. **Recency matters.** Note the date of every time-sensitive claim (reviews, news, filings). Flag anything older than ~24 months as potentially stale.

## Workflow (4 stages)
Run as a chain — each stage hands off to the next. Full copy-paste prompts are in `prompts/prompt-chain.md`.

1. **Entity Resolution & Firmographics** — confirm the exact legal entity, formation date, officers/registered agent, locations, industry (NAICS), and headcount range. Output feeds every later stage. Key sources: state Secretary of State registry, USPTO, company site + Wayback, LinkedIn.
2. **Brokering Signal Sweep** — succession/owner-tenure signals, exit/transition signals, saleability/quality, market pull, and the indicative size band. Key sources: SOS formation date + officer tenure, UCC lien search, court/bankruptcy records, BizBuySell/BizQuest listings, USAspending/SAM.gov, local business-journal news.
3. **Consulting Signal Sweep** — operational gaps (review themes), digital/tech maturity gaps (site quality, e-commerce/booking, BuiltWith), growth strain (hiring velocity, expansion), and compliance/risk exposure (OSHA/EPA/DOL, litigation, licensing). Key sources: Google/Yelp/BBB reviews, Glassdoor/Indeed, job postings, regulator databases.
4. **Score & Synthesize** — apply `references/scoring-rubric.md`, fill `assets/brief-template.md`, write the outreach hook. Deliver the finished brief to the user; if a working folder is available, also save it there as `<company-slug>-brief.md`.

## How to score (summary)
Two independent 0–100 scores, bands Low (0–39) / Medium (40–69) / High (70–100). Full weights and signal definitions in `references/scoring-rubric.md`.

- **Likelihood-to-Sell** = succession (30) + exit/transition signals (25) + saleability/quality (25) + market pull (20).
- **Consulting-Opportunity** = operational gaps (30) + digital/tech maturity gaps (25) + growth strain (25) + compliance/risk exposure (20).

Each score must cite the specific signals that drove it. A high score on thin evidence is a fail — if confidence is low, say so and route to "need more."

## Output
A **one-page brief** per company (template in `assets/brief-template.md`): snapshot, the two scores with drivers, indicative size band + assumptions, red flags, a 1–2 sentence outreach hook tailored to the strongest angle, the recommendation (pursue-brokering / pursue-consulting / pass / need more) with a confidence %, and the source appendix.

For a list of companies, produce one screening-table row each (template in the same file) and only write full briefs for the rows that clear your pursue threshold.

## Gotchas
Failure modes seen in practice — check before delivering:
- **Wrong legal entity.** Common names collide in SoS registries and USAspending; a DBA is not the registrant. Confirm state + registered agent + address agree before attributing anything.
- **Stale signals scored as current.** Old reviews, a years-old news item, or a Wayback snapshot scored as if current. Date every time-sensitive claim; >~24 months = flag stale.
- **LinkedIn headcount inflation.** "Associated members" includes alumni and contractors; treat it as an upper bound, corroborate with job postings or facility size.
- **Score without signal.** A component score with no named, cited signal behind it. Unknown component = 0 + a diligence question, never a guessed midpoint.
- **Size band read as valuation.** The indicative band is triangulation from stated assumptions — label it, show the assumptions, never present it as what the business is worth.
- **Consulting score ignoring ability to pay.** Gaps at a 3-person shop don't fund an engagement; apply the ability-to-pay modifier in the recommendation, not just the score.

## Related skills
- Want a 0–10 quality/marketability rating of the business itself (not a prospect decision)? Use **jail-rate**.
- Turning this brief's next step into an engineered prompt or chain? Use **jail-prompt**.

## Self-check before delivering (structural — all must pass)
- Brief contains every template section (snapshot, scores, drivers, size band, red flags, hook, recommendation, source appendix); none left as placeholders.
- Every Fact/Inference has a live, free-source citation with a date accessed; anything uncitable is relabeled Analyst Judgment or Missing Evidence.
- No invented financials; size band shows each assumption; labeled "NOT a valuation."
- Each component score traces to ≥1 named cited signal, or is scored 0 with a diligence question — never a guessed midpoint.
- Recommendation is exactly one of: pursue-brokering / pursue-consulting / pass / need more; confidence % present for both scores.
- Owner data is business-relevant only; every time-sensitive claim dated, >~24-month items flagged stale.
- 1–5 self-score on grounded / verifiable / scoped / format-matched, plus an overall confidence %.
