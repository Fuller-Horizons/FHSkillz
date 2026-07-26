# jail-skill-miner

Find the parts of a codebase that should become a reusable skill, not a one-off feature.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.3.1.

## What it does

This skill reads a codebase, a chat history, or a stack of documents. It looks for disciplines — repeatable ways of working, not one-off features. Each find must pass a 4-box test before it counts as a candidate. Then it checks the survivors against every skill you already have, so you never build a duplicate. It stops and asks before it writes anything.

## Use it when

- "Mine this repo for skills we should pull out."
- "What rules does this codebase enforce that nobody wrote down?"
- "The same test keeps failing the same way — should that become a skill fix?"
- "Here's a list of skill ideas from another tool. Which ones are real?"

## Don't use it for

- Writing a skill you already picked — just follow the repo's normal build steps.
- Scoring how good an existing skill is — use [`jail-rate-skill`](../jail-rate-skill/) instead.

## What you get

A short table of candidates. Each row shows its evidence, the failure it stops, and whether it's new, an edit to an existing skill, or a duplicate of one. Then the skill stops, so a person picks which ones get built.

## Example

**You ask:**

> Mine this repo for skill-worthy disciplines. Check the build scripts and hooks too, not just the skills folder. Dedupe against what we already have first.

**It produces:**

```
| candidate | evidence file:line | discipline | failure-prevented | classification | rank |
|---|---|---|---|---|---|
| Never let the producer grade itself | evals/README.md:61-62 · scripts/run_evals.py:88-113 | independent verification: a fresh, blind grader, never the model that produced the answer | self-grading rubber-stamps its own errors ("that conflict cost real accuracy here" — evals/README.md:62) | DUPLICATE of jail-verify | 25 |
...

**Recommended (top 3 by rank — NEW, EXTENDS, and DUPLICATE all eligible):**
1. **Never let the producer grade itself** (rank 25) — the suite's
   highest-leverage discipline, confirmed independently enforced everywhere
   it matters; no action needed, but it's the reason jail-verify's
   independence rule should never be loosened.
2. **Pre-emit fail-closed checklist gate** (rank 20) — the second
   load-bearing pattern across the whole suite; confirms Constitution Rule 7
   is doing its job in 8+ skills, not just stated once and ignored.
3. **Fail-open side-channel instrumentation** (rank 16) — the one genuinely
   new candidate: no current skill teaches "wrap observability code so its
   own failure can't take down what it's watching," and the repo's own hook
   is a clean worked example to build from.

STATUS: AWAITING-SELECTION
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
