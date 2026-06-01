# Source tiering & verification reference

Load this when the engineered prompt involves research, factual claims, pricing, statistics, current events, or anything a reader could act on. It is the detailed version of the **Authority** rule in SKILL.md — pull it in when grounding actually matters, skip it for non-factual tasks.

## Source tiers (prefer higher tiers; drop to lower only when forced)

1. **Primary / official** — the entity that owns the fact. Vendor pricing pages, official docs/API references, company filings (10-K, 10-Q, 8-K), government data (.gov), standards bodies, the original dataset or paper. Highest trust for *what a thing is, costs, or officially states*.
2. **Peer-reviewed / expert-reviewed** — journal articles, systematic reviews, reputable standards and technical specs. Highest trust for *empirical claims and mechanisms*.
3. **Reputable secondary** — established outlets and analysts with editorial standards and a correction policy (major newspapers, Reuters/AP, well-known domain publications, Wirecutter/RTINGS-class reviewers). Good for synthesis and context; verify their underlying source where it matters.
4. **Crowd / community** — Reddit, forums, Stack Overflow, star ratings, social posts. Use only for *leads, sentiment, and what to go verify* — never as the sole support for a consequential claim.
5. **Avoid as authority** — SEO listicles, content farms, undated blog posts, vendor marketing copy presented as neutral, and AI-generated pages with no sourcing.

## Recency

State an explicit freshness window appropriate to the domain and reject anything older:
- Prices, availability, rankings, "best X" → **within ~30 days** (often less).
- Software/API behavior, versions → current major version; check release notes/changelog dates.
- Laws, regulations, policies → confirm still in force; check effective/repeal dates.
- Scientific consensus → prefer recent reviews, but a foundational older paper can still be primary.
Always show the date of each consequential source so staleness is visible.

## Cross-checking

- Cross-check any **consequential** claim (one the reader will spend money or make a decision on) against **2+ independent** sources — independent meaning not republishing each other.
- If sources conflict, say so and present the disagreement rather than silently picking one.
- Separate **fact** (sourced, datable) from **inference** (your reasoning on top of it). Label inference as inference.

## Honesty rules (non-negotiable)

- Never claim a source is "verified" you didn't actually check.
- Never state a confidence number you haven't earned.
- If a claim can't be grounded, say "unverified" and flag it — an honest gap beats a confident fabrication.
- No invented statistics, quotes, citations, or URLs. If you're not sure a source exists, don't cite it.
