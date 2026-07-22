---
name: jail-council
metadata:
  version: 1.0.0
description: >-
  Convene an LLM COUNCIL for maximum-accuracy answers to consequential or
  contested questions: 3–5 independent models answer blind, adversarially
  review each other's ANONYMIZED answers, disputed facts get a targeted
  verification round, and a chairman synthesizes by evidence — never by vote —
  preserving dissent. Cost is disclosed, never a gate: invoking this skill
  means accuracy outranks tokens. Use when the user says "convene the
  council", "ask multiple models", "get a second/third opinion", "maximum
  accuracy", "I need this answer to be right", or when jail-verify /
  jail-decide / jail-rate / jail-prompt escalate a high-stakes contested
  call. Do NOT use for parallel division of labor across different subtasks
  (jail-orchestrate) or for questions with no knowable answer (STOP those).
---

# JAIL-COUNCIL — Maximum-Accuracy Deliberation

Multiple independent minds, blind first answers, anonymized adversarial
review, evidence-decided synthesis. Pattern inspired by Andrej Karpathy's
[llm-council](https://github.com/karpathy/llm-council) (no code reused;
protocol re-derived under JAIL evidence discipline).

**Charter — accuracy outranks cost, by design.** This skill inverts the
suite's efficiency default: invoking it IS the Constitution Rule-11
justification. Disclose the cost (≈ members + reviews + chairman ≈ N+2×
a single answer, more with a verification round) and proceed — never refuse
for expense. The only STOPs: the question has no knowable/groundable answer,
or the user declines Tier C when nothing stronger is available.

## Step 0 — Frame
- Restate the question and define **what would make an answer WRONG** (the
  accuracy rubric the reviewers will use). A question that can't be wrong
  can't be counciled — STOP toward jail-red-team (opinions) or jail-decide
  (preferences).
- Groundable check per jail-research rules; declare the epistemic mode.

## Step 1 — Seat the council (declare the independence tier)
3 members default, 5 for maximum stakes. Independence, strongest first:
- **Tier A — cross-provider** (strongest): different vendors' models.
  Native in OpenCode CLI — see
  [references/opencode-runbook.md](references/opencode-runbook.md) for the
  verified per-agent model config.
- **Tier B — different models, same provider** (e.g. distinct model
  families/sizes).
- **Tier C — independent same-model sessions** (weakest, available
  everywhere): fresh contexts, blind to each other, anonymized review.
  Still beats self-review — the anonymization and independence survive even
  when the weights don't differ.
**Always state the tier in the output.** Claiming Tier A while running
Tier C is a lie about the strength of the verification.
Chairman: the strongest available model; ideally not a member — if a member
must chair, disclose it.

## Step 2 — First opinions (blind)
Identical brief to every member. **No cross-talk, no shared context** —
independence before review is enforcement point #1 (kills anchoring).
Each member answers with house epistemics: material claims labeled
(Fact/Inference/Estimate/Unknown) with sources where retrieval exists.

## Step 3 — Anonymized adversarial review
The orchestrator strips ALL attribution → answers become A, B, C…
(**anonymization is enforcement point #2** — kills brand/self favoritism).
Each member reviews every anonymized answer:
- **Error-hunt first**: name ≥1 concrete error, unsupported claim, or
  material gap per answer — or state "none found" explicitly. Politeness is
  a review failure; agreement without inspection is convergence theater.
- Score each answer on: factual accuracy · completeness · reasoning
  soundness · evidence quality (rubric + format:
  [references/council-protocol.md](references/council-protocol.md)).
- Rank all answers, best-supported first.

## Step 4 — Verification round (the accuracy escalation)
If reviews disagree on a **load-bearing fact**, do not synthesize over the
dispute: dispatch a targeted evidence check (live search / primary source
per jail-research tiers) on exactly that fact. Evidence, not eloquence,
settles it. Optional one rebuttal round (members may revise seeing the
reviews) — **maximum 2 rounds total**: bounded not to save tokens but
because unbounded deliberation stops converging.

## Step 5 — Chairman synthesis
The chairman receives everything (answers, reviews, rankings, verification
results) and produces:
- **The final answer** — built from the best-*evidenced* claims. **Evidence
  beats votes**: a 4–1 majority loses to the 1 with the primary source.
- **Per-claim confidence** (High/Medium/Low) tied to evidence + agreement.
- **Dissent register** — surviving minority positions, stated fairly, each
  with the observation/evidence that would decide it. Dissent is preserved,
  never averaged away.
- **Audit appendix** — member roster + tier, the anonymized ranking table,
  verification-round results, cost disclosure.
Chairman rule: synthesize ONLY from reviewed material and verification
results — a chairman inserting new unreviewed claims is laundering.

Close with the JAIL-HANDOFF block; `next:` jail-verify for an independent
check of the synthesis when the stakes warrant even that.

## Related skills
Different subtasks in parallel → **jail-orchestrate** (division of labor,
not redundancy). Two-party check of finished work → **jail-verify** (this
skill is its N-party big sibling). Deciding between options the council
informed → **jail-decide**. Escalates INTO this skill: jail-verify,
jail-decide, jail-rate, jail-prompt (high-stakes contested calls).

## Gotchas
- **Convergence theater.** All members agreeing proves nothing if nobody
  error-hunted. The ≥1-error-or-"none found" rule is mandatory per review.
- **Majority-vote truth.** Votes weigh opinions; evidence decides facts.
  The chairman's synthesis cites evidence, not tallies.
- **Brand/self bias.** Reviewing named answers re-introduces favoritism —
  anonymize before every review, no exceptions.
- **Tier inflation.** Reporting a same-model council as if it were
  cross-provider. Declare the tier; it's part of the answer's credibility.
- **Chairman laundering.** New claims appearing at synthesis that no member
  made and no verification produced. The audit appendix makes this visible.
- **Council theater.** Narrating a council that never ran. The audit
  appendix (roster, rankings, reviews) is the proof-of-work — no appendix,
  no council.
- **Skipping the verification round.** Synthesizing over a live factual
  dispute converts disagreement into confident error — the exact failure
  this skill exists to prevent.
