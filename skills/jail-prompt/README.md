# JAIL-PROMPT

**J**onathan's **A**ctually **I**ntelligent **L**ogic for **P**rompting — a Claude skill that turns a half-formed goal into either a **STOP** (when AI is the wrong tool, or the idea itself is flawed) or an **engineered, verifiable, token-efficient prompt** that succeeds on the first run.

Part of the **[FHSkillz](../../README.md)** collection. **Version 2.0.0** — instruction-only: all machine checks now live in the companion [`jail-py-prompt-tools`](../jail-py-prompt-tools/) skill, with manual fallbacks named at every checkpoint.

## What it's for

Most prompting fails before a single token is written — the task is a bad fit for an LLM, the goal is misframed, or the prompt is vague, unverifiable, or bloated. JAIL-PROMPT runs a short pre-flight that catches those failures early and engineers the rest.

It triggers when you state an outcome without a real prompt, ask to "make this prompt better," want to know whether AI is even the right tool, or paste a rough goal you want done correctly without wasting tokens. It deliberately does **not** trigger for a finished prompt you just want run verbatim, or for plain conversation.

## How it works

Stakes triage routes every task to a lane — **Instant** (clear, low-stakes), **Lite** (assumptions + verdict + draft in one reply), or **Full** (all three phases, pausing for answers) — over the same three phases:

1. **Frame & Clarify** — comprehension gate (≥97% understanding before advancing), task-type decomposition, epistemic mode, objective + success test, output format.
2. **Viability gate (the core)** — Right tool? Groundable? Effort vs. payoff? Enhancement? Secure? A flawed premise is a **STOP** no matter how good a prompt you could write.
3. **Engineer the prompt** — a copyable METADATA/ROLE/CONTEXT/OBJECTIVE/SUCCESS TEST/PROCESS/SOURCES/OUTPUT FORMAT/CONSTRAINTS/VERIFICATION PLAN/BEFORE RETURNING skeleton, chained when one prompt can't do the job, self-critiqued once, then offered to run.

Throughout: **discernment over agreeableness** — four-bias pressure-testing (tool, fact, effort, proceed), no unverified praise.

## Contents

```
skills/jail-prompt/
├── SKILL.md                      # the skill (always loaded) — instruction-only
├── README.md · CHANGELOG.md
└── references/                   # progressive disclosure — load only when relevant
    ├── examples.md               # worked examples incl. Lite vs Full lane comparisons
    ├── sources.md                # source tiering, recency, cross-checking
    ├── antipatterns.md           # named failure modes (tell + fix)
    ├── templates.md              # pre-engineered output schemas
    ├── chaining.md               # chain manifests, handoffs, checkpoint gates
    ├── truth-tagging.md          # ✓Known / ~Infer / ?Unknown as validated schema
    ├── generation-settings.md    # per-mode inference parameters
    └── meta-prompt.md            # portable, install-free single-block version
```

Machine checks (secret scan, prompt lint, chain lint, truth lint, dry-run) live in [`jail-py-prompt-tools`](../jail-py-prompt-tools/). Eval suites live at the repo root in [`evals/`](../../evals/).

## Install

Installed automatically with the `fh-skillz` plugin — see the [repo README](../../README.md#install). For single-skill upload to Claude.ai web, build a ZIP locally with `../../scripts/build-zips.sh` (ZIPs are not committed to the repo).

## Status

Behavioral evals: 11 cases, proxy-graded 100% (see [`evals/RESULTS.md`](../../evals/RESULTS.md)). Triggering: 20/20 proxy, two independent judges. Open items: live `claude -p` harness run and a true multi-turn exercise — proxy results are labeled as such and have not been upgraded.
