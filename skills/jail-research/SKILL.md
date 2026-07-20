---
name: jail-research
metadata:
  version: 1.0.0
description: >-
  Plan, execute, and synthesize research into a structured, citable EVIDENCE
  PACKET — answerable questions, tiered authoritative sources, dates on every
  citation, contradiction handling, and honest gaps. Use when a task needs
  facts gathered from internal or external sources: "research X", "find
  evidence for", "what does the data say", "verify this claim", background for
  a decision/analysis/framework, or when another skill (jail-decide,
  jail-pestle, jail-swot, jail-rate) needs grounding. Do NOT use for
  US-private-company sell-side prospecting (jail-prospect) or when
  the user supplies all facts and just wants synthesis (jail-exec-brief).
---

# JAIL-RESEARCH

Research that a skeptic can audit: every conclusion travels with its source,
date, and confidence — or is labeled Unknown. [Constitution Rules 1, 2, 10]

## Step 1 — Plan before searching
- Restate the research objective and the **decision it serves** (research with
  no consuming decision is a scope smell — challenge it).
- Break it into **answerable questions** (each has a knowable answer).
- For each question, name the **evidence that would answer it** and the likely
  best source *before* searching — it keeps retrieval from wandering.
- Time-sensitive subjects (prices, versions, leadership, law, "latest") →
  live search is mandatory; model memory will be stale and will fabricate.

## Step 2 — Gather, tiered
Source order: **primary/official → independent measurement/peer-reviewed →
reputable secondary → crowd (pattern evidence only) → never** (marketing
copy, SEO farms, undated pages, uncited AI text). Rules:
- Record for every citation: source · what it evidences · URL/ref · **date
  accessed**. No citation you didn't open this session. [Rule 10]
- Cross-check consequential claims across **2+ independent** sources.
- Run independent question-streams in parallel (subagents where available);
  give each ONE question and require the citation format back.
- Log the **limitations** of each source (age, scope, conflict of interest).

## Step 3 — Reconcile
- **Contradictions:** surface them, don't average them. Prefer the *strongest
  currently-applicable* evidence — not automatically the newest statement.
  Preserve the losing side + why it lost; mark superseded findings.
- **Gaps:** unanswered questions stay in the packet as Unknowns with what
  would resolve them. An Unknown is a finding, not a failure. [Rule 2]

## Step 4 — Emit the evidence packet
```
EVIDENCE PACKET
Objective + consuming decision:
Questions:
  Q1: <question>
      Answer: <finding> — [Fact|Inference|Estimate|Unknown] · confidence
      Evidence: [1] source · what it supports · URL · date
      Contradictions/limitations:
Cross-cutting findings:
Unresolved gaps (+ what would resolve each):
Source list (numbered, dated):
```
Then the JAIL-HANDOFF block — `next` is usually the consuming skill
(jail-decide, jail-verify, a framework skill, or jail-exec-brief).

## Related skills
Company sell-side screen → **jail-prospect**. Rate the researched
subject → **jail-rate**. Contract unclear → **jail-task-contract** first.
A deep-research tool/agent, when present, may serve as the Step-2 engine —
its output still must be reformatted into the packet and its citations
spot-verified.

## Gotchas
- **Search-then-rationalize.** Forming the answer first and collecting
  agreeable sources. The question list (Step 1) exists to prevent this.
- **Citation decoration.** URLs pasted next to claims they don't actually
  support. Each citation names the specific claim it backs.
- **Recency worship.** Newest ≠ strongest. A 2023 RCT beats a 2026 blog post.
- **Averaged contradictions.** "Sources vary between X and Y" hides the
  question of which source is better. Weigh, pick, preserve the loser.
- **Fabricated confidence on paywalled/missing data.** If it can't be
  retrieved, it's Unknown — never reconstruct it "from memory."
- **Packet skipped under time pressure.** Downstream skills consume the
  packet, not your prose. No packet = the research didn't happen.
