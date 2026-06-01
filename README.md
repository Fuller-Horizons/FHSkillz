# JAIL-PROMPT

**J**onathan's **A**ctually **I**ntelligent **L**ogic for **P**rompting — a Claude skill that turns a half-formed goal into either a **STOP** (when AI is the wrong tool, or the idea itself is flawed) or an **engineered, verifiable, token-efficient prompt** that succeeds on the first run.

Part of the **FHSkillz** (Fuller Horizons Skill Directory) collection.

> Version 0.9.0 · feature-complete, two validation paths pending (see [Status](#status)).

## What it's for

Most prompting fails before a single token is written — the task is a bad fit for an LLM, the goal is misframed, or the prompt is vague, unverifiable, or bloated. JAIL-PROMPT runs a short pre-flight that catches those failures early and engineers the rest.

It triggers when you:

- state an outcome but haven't written a real prompt ("I just want my landing page to convert better"),
- ask to "make this prompt better,"
- want to know whether AI is even the right tool,
- or paste a rough goal and want it done *correctly* without wasting time or tokens.

It deliberately does **not** trigger for a finished prompt you just want run verbatim, or for plain conversation.

## How it works

Three phases, scaled to stakes:

1. **Frame & Clarify** — one batched round of questions, stated assumptions, a one-sentence objective + a one-line success test, and a recommended-default choice of output format. Trivial asks skip this via the **fast path**.
2. **Viability gate (the core)** — Right tool? Groundable? Effort vs. payoff? Enhancement? Secure? Plus a readiness check that the *goal itself is sound*. Outcome is **GO** or **STOP** (with a multiple-choice next step). A flawed premise is a STOP no matter how good a prompt you could write.
3. **Engineer the prompt** — a copyable `ROLE / CONTEXT / OBJECTIVE / SUCCESS TEST / PROCESS / SOURCES / CONSTRAINTS / BEFORE RETURNING` skeleton, decomposed into a **chain** when one prompt can't do the job, then offered to run with a one-pass tighten loop.

A guiding stance runs through all three: **discernment over agreeableness** — no unverified praise, no building a bad idea just because it was asked for.

## Contents

```
jail-prompt/
├── SKILL.md                    # the skill (always loaded)
├── references/
│   ├── examples.md             # 5 worked examples (STOP, fast-path, GO, format/multi-turn, adversarial)
│   ├── sources.md              # source tiering, recency, cross-checking, honesty rules
│   └── antipatterns.md         # 13 named prompt-engineering failure modes (tell + fix)
└── evals/
    ├── evals.json              # 10-case behavioral eval suite
    ├── trigger_evals.json      # 20-case triggering eval set
    └── README.md               # how to re-run the validation loop
```

The references use progressive disclosure — they load only when relevant, keeping the always-on SKILL.md lean.

## Install

**Cowork:** open the `jail-prompt.skill` file and click **Save skill**.

**Claude Code / manual:** copy the `jail-prompt/` folder into your skills directory (e.g. `~/.claude/skills/jail-prompt/`). The skill auto-triggers from its description; no command needed.

## Status

| Dimension | State |
|---|---|
| Behavioral evals | 10 cases, independently graded, **100%** after fixes; key cases run 3× for variance |
| Triggering | 20-case proxy: **20/20** — *real `claude -p` harness run still pending* |
| Multi-turn interactive | logic in place; **not yet exercised live** (evals were single-turn) |
| Overall (weighted rubric) | ~9.4 / 10 |

Two honest gaps remain before a 1.0 tag: a real triggering-harness run and a live multi-turn test. See [CHANGELOG](CHANGELOG.md).

## L