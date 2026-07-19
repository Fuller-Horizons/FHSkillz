# company-prospect-research

Researches a **US private company as a sell-side brokerage / consulting prospect** using only free, authoritative sources. Produces a one-page brief: Likelihood-to-Sell score (0–100), Consulting-Opportunity score (0–100), red flags, an outreach hook, and a fully cited source appendix.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.1.0.

## Non-negotiables

Free sources only (no PitchBook/ZoomInfo); every line labeled Fact / Source-Backed Inference / Analyst Judgment / Missing Evidence; **no fabricated financials, ever** (indicative size band with stated assumptions only); cite or omit; owner privacy — business-relevant facts only.

## How it works

A 4-stage chain (full copy-paste prompts in [`prompts/prompt-chain.md`](prompts/prompt-chain.md)): Entity Resolution → Brokering Signal Sweep → Consulting Signal Sweep → Score & Synthesize into [`assets/brief-template.md`](assets/brief-template.md), scored per [`references/scoring-rubric.md`](references/scoring-rubric.md) against the source catalog in [`references/free-sources.md`](references/free-sources.md).

Related: a 0–10 quality rating of a business (not a prospect decision) is [`jail-rate`](../jail-rate/); the deeper multi-agent pipeline lives in `systems/company-intelligence/` (not a skill).

## Contents

```
skills/company-prospect-research/
├── SKILL.md · README.md · CHANGELOG.md
├── assets/brief-template.md
├── prompts/prompt-chain.md
└── references/
    ├── free-sources.md
    └── scoring-rubric.md
```
