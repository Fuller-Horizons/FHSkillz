# Company Prospect Research — Prompt Chain (4 stages)

Run in order. Each stage's output is the next stage's input. Human checkpoint between
each: confirm the entity is right before sweeping; sanity-check signals before scoring.
Free sources only (see ../references/free-sources.md). Label every claim:
Fact | Source-Backed Inference | Analyst Judgment | Missing Evidence.

---
## Stage 1 — Entity Resolution & Firmographics

```
ROLE: Entity-resolution research analyst.
CONTEXT: Target = "[COMPANY]" website [URL], believed to be in [city/state]. US private SMB.
OBJECTIVE: Confirm the exact legal entity and core firmographics so later research targets the right company.
SUCCESS TEST: Legal name, state, formation date, officers/agent, locations, NAICS, and headcount range are each stated with a free-source citation, or marked Missing Evidence. No second company conflated.
PROCESS:
  1) Find the entity in the state Secretary of State registry: legal name, status, formation date, officers, registered agent.
  2) Confirm domain ownership + business description from the company site; capture site history from Wayback.
  3) Cross-check leadership and headcount range via LinkedIn; note any other states/locations.
  4) Capture NAICS/industry and any USPTO trademarks.
SOURCES: Tier 1 (SOS, USPTO) first; company site/LinkedIn labeled as company-controlled. Cite URL + date.
CONSTRAINTS: Free sources only. If multiple candidate entities exist, list them and flag the ambiguity rather than picking silently.
BEFORE RETURNING: self-check vs SUCCESS TEST; 1–5 on grounded/verifiable/scoped/format; confidence %; list unresolved ambiguities.
```

---
## Stage 2 — Brokering Signal Sweep (primary)

```
ROLE: Sell-side business-brokerage analyst.
CONTEXT: Confirmed entity from Stage 1: [paste]. Goal is to judge likelihood the owner would/should sell.
OBJECTIVE: Gather succession, exit/transition, saleability, and market-pull signals, plus an indicative size band.
SUCCESS TEST: Each scoring component (succession, exit, saleability, market pull) has at least one cited signal or a Missing-Evidence note; size band shows its assumptions and invents no financials.
PROCESS:
  1) Succession: owner tenure (formation date + leadership tenure), estimated age, successor presence, single-owner dependency.
  2) Exit/transition: for-sale listings (BizBuySell/BizQuest), stale-site/slowed-hiring signals (Wayback/Indeed), UCC lien releases vs new liens, ownership-change filings, retirement language in news.
  3) Saleability/quality: years in business, recurring/diversified revenue signals, customer concentration (USAspending), transferable assets (USPTO/brand/location), legal/compliance cleanliness (courts/regulators).
  4) Market pull: consolidation/acquirer activity in the niche, industry multiples (BizBuySell insight reports), comparable local sales.
  5) Indicative size band ONLY: est. headcount × industry revenue-per-employee (Census/BLS) + any federal awards (USAspending). State every assumption. Mark actual financials Missing Evidence.
SOURCES: Tier 1 for facts; cross-check any band-moving signal across 2+ sources. Cite URL + date.
CONSTRAINTS: Free sources only. No fabricated revenue/EBITDA/owner comp. Owner data must be business-relevant.
BEFORE RETURNING: self-check vs SUCCESS TEST; flag the weakest-evidenced signal; confidence %.
```

---
## Stage 3 — Consulting Signal Sweep (secondary)

```
ROLE: Operations/management-consulting diligence analyst.
CONTEXT: Confirmed entity from Stage 1: [paste]. Goal is to find pitchable improvement opportunities.
OBJECTIVE: Gather operational, digital/tech-maturity, growth-strain, and compliance/risk signals.
SUCCESS TEST: Each consulting component has a cited signal or Missing-Evidence note; an ability-to-pay note is included given the size band.
PROCESS:
  1) Operational gaps: recurring negative review themes + complaint trend (Google/Yelp/BBB).
  2) Digital/tech maturity: site quality (manual + Wayback), e-commerce/booking presence, SEO/social footprint, tech stack (BuiltWith).
  3) Growth strain: hiring velocity/open roles (Indeed/LinkedIn), expansion/new locations, funding (Form D) without systems maturity.
  4) Compliance/risk: OSHA/EPA/DOL violations, litigation, licensing status.
SOURCES: Tier 2 review/hiring sources allowed but dated; regulator data is Tier 1. Cite URL + date.
CONSTRAINTS: Free sources only. No intrusive technical testing — public observation only.
BEFORE RETURNING: self-check vs SUCCESS TEST; note ability-to-pay; confidence %.
```

---
## Stage 4 — Score & Synthesize the brief

```
ROLE: Senior analyst producing an executive-ready prospect brief.
CONTEXT: Stage 1–3 findings: [paste]. Scoring rubric: ../references/scoring-rubric.md. Template: ../assets/brief-template.md.
OBJECTIVE: Produce the one-page brief with both scores, indicative size band, red flags, outreach hook, and recommendation.
SUCCESS TEST: A reader decides pursue-brokering / pursue-consulting / pass / need-more in under 5 minutes; every score component traces to a cited Stage 1–3 signal; no new uncited claims introduced.
PROCESS:
  1) Apply the rubric; compute both 0–100 scores with per-component justification.
  2) Fill the brief template exactly; preserve all citations from earlier stages.
  3) Write a specific outreach hook tied to the strongest real signal (no generic flattery).
  4) State the recommendation + confidence %; if "need more," list the top 3 diligence questions.
  5) Deliver the brief to the user; if a working folder is available, also save it there as [slug]-brief.md.
SOURCES: Reuse Stage 1–3 citations; add none that weren't gathered. 
CONSTRAINTS: One page. No fabricated financials. Recommendation must be one of the four allowed values.
BEFORE RETURNING: self-check vs SUCCESS TEST; 1–5 on grounded/verifiable/scoped/format-matched; overall confidence %; list assumptions + gaps. For a high-stakes pursue call, add one adversarial line: the strongest reason NOT to pursue, then resolve or flag it.
```
