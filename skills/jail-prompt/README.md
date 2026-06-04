# JAIL-PROMPT

**J**onathan's **A**ctually **I**ntelligent **L**ogic for **P**rompting — a Claude skill that turns a half-formed goal into either a **STOP** (when AI is the wrong tool, or the idea itself is flawed) or an **engineered, verifiable, token-efficient prompt** that succeeds on the first run.

Part of the **[FHSkillz](../../README.md)** collection.

> Version 1.0.0 · content-complete. Two validation paths remain open (see [Status](#status)).

> **Just want to use it on Claude.ai? No coding required.** [Download `jail-prompt.zip`](../../dist/jail-prompt.zip) and follow the [3-minute install guide](https://github.com/Fuller-Horizons/FHSkillz/wiki/Install-on-Claude-ai).

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
skills/jail-prompt/
├── SKILL.md                  # the skill (always loaded)
├── README.md                 # this file
└── references/               # progressive disclosure — load only when relevant
    ├── examples.md           # worked examples (STOP, fast-path, GO, format/multi-turn)
    ├── sources.md            # source tiering, recency, cross-checking, honesty rules
    └── antipatterns.md       # named prompt-engineering failure modes (tell + fix)
```

The behavioral and triggering eval suites live at the repo root in [`evals/`](../../evals/).

## Install

**Claude Code / plugin:** installed automatically with the `fh-skillz` plugin — see the [repo README](../../README.md#install). The skill auto-triggers from its description; no command needed.

**Claude.ai:** [download `jail-prompt.zip`](../../dist/jail-prompt.zip) and upload it under **Settings → Customize → Skills** ([guide](https://github.com/Fuller-Horizons/FHSkillz/wiki/Install-on-Claude-ai)).

**Manual:** copy this `jail-prompt/` folder into your skills directory (e.g. `~/.claude/skills/jail-prompt/`).

## Status

| Dimension | State |
|---|---|
| Behavioral evals | 11 cases; v1.2.0 spot-check **4/4** (incl. both new behaviors), independently graded, all assertions pass — see [`evals/RESULTS.md`](../../evals/RESULTS.md) |
| Triggering | 20-case proxy, refreshed at v1.2.0: **20/20**, two independent judges unanimous — *real `claude -p` harness run still pending* |
| Multi-turn interactive | exercised via a 2-turn proxy at v1.4.0: Full-lane **pause + resume verified**; plus **3/3 variance** on a repeated case — see [`evals/RESULTS.md`](../../evals/RESULTS.md). Live `claude -p` run still pending. |

Content is at 1.2.0. Two honest validation gaps remain: a live `claude -p` triggering-harness run and a true multi-turn test (current evidence is a strong subagent proxy). See [`evals/RESULTS.md`](../../evals/RESULTS.md) and the [CHANGELOG](../../CHANGELOG.md).
