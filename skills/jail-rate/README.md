# jail-rate

Give any subject a fair, evidence-based score out of 10.

Part of the **[FHSkillz](../../README.md)** collection. Version 2.1.0.

## What it does

You name a subject: software, hardware, an idea, a business, a piece of content. jail-rate builds a rubric for it first. A rubric is a weighted list of what matters most for that type of subject. It scores each item against real evidence, not gut feel. Every claim is labeled Fact, Inference, or Judgment, so you can see how solid each score is. Then it ranks the fixes that would raise the score the most.

## Use it when

- "Should we adopt this SaaS tool? Rate it and show your sources."
- "Score this business plan out of 10 and tell me what to fix first."
- "How does this hardware compare to the competition?"

## Don't use it for

- Rating an AI skill folder in this repo. Use [`jail-rate-skill`](../jail-rate-skill/) instead.
- A buy-or-pass call on a company for sales or consulting. Use [`jail-prospect`](../jail-prospect/) instead.
- Judging a person's character or private life. jail-rate refuses this outright. It will only rate a person's public track record in a professional role, using public evidence.

## What you get

You get a declared rubric with weights, shown before any score. Each scorecard row carries a score and cited evidence. You also get a ranked list of fixes, and a projected score for after those fixes land.

## Example

**You ask:**

> We're a 40-person company evaluating whether to roll out Bitwarden as our standard password manager. Rate it for us with the full scorecard and your sources.

**It produces:**

```
> **Bitwarden — software product (SaaS / password manager) — Overall: 6.8 / 10 → 7.9 / 10 projected (▲ +1.1)**

**Rubric used** (declared before scoring; weights sum to 100%)

| Dimension | Weight | Why this weight for a software product |
|---|:---:|---|
| Software quality | 25% | Everything else — features, security, reputation — decays if the underlying build/release process is unreliable. |
| Features | 20% | Determines whether it actually covers your SSO/SCIM roadmap, not just today's needs. |
| Usability | 20% | A password manager 40 people fight with gets bypassed; adoption is the product. |
| Security | 20% | Weighted equal to usability — for this category, one breach outweighs years of polish. |
| Marketability | 15% | Pricing trajectory and market position affect total cost and renewal risk over a multi-year rollout. |

...
| Security | 20% | **4.0 (critical-flaw cap)** | 7.8 | Fact [1]: SOC2 Type II + SOC3, ISO 27001, HIPAA compliance, annual third-party pentests, HackerOne bug bounty. Fact [2]: CVE-2026-42994 — Bitwarden CLI 2026.4.0 shipped with embedded malicious code via a compromised npm publish (CVSS 3.1 9.8 Critical). Fact [3]: CVE-2026-43640 — Bitwarden Server missed master-password re-auth on org SCIM key retrieval/rotation prior to v2026.4.1 (CVSS 4.0 8.6 High). Critical-flaw cap applied per Self-check rule regardless of the compliance program. |
...
1. Bitwarden, "Compliance" — SOC2 Type II/SOC3, ISO 27001, HIPAA, annual pentests, HackerOne bug bounty — https://bitwarden.com/compliance/ — opened directly, accessed 2026-07-26.
2. NVD, CVE-2026-42994 — Bitwarden CLI 2026.4.0 npm supply-chain compromise, CVSS 3.1 9.8 Critical — https://nvd.nist.gov/vuln/detail/CVE-2026-42994 — opened directly, accessed 2026-07-26.
...
**Confidence** — **Medium overall.** Security confidence is High — both CVEs are documented directly in NVD (Tier 1-2, opened directly) and cross-confirmed by Bitwarden's own compliance claims. Usability and Marketability pull the average down to Medium because their key numbers (G2 ratings) came from search-engine aggregation after a direct G2 fetch was blocked (HTTP 403) — pattern evidence, not independently verified. **The one action that would most raise confidence:** pull Bitwarden's actual SOC 2 Type II report and G2's raw review export directly (rather than through vendor pages and search snippets) to move Usability and Marketability from Medium to High.
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
