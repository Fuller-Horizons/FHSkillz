# jail-prototype

Build a small, throwaway version of an idea to answer one question before your team builds it for real.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.2.0.

## What it does

You name one question your team cannot settle just by talking — does this state model hold up, or which of three layouts reads best? This skill builds the smallest thing that can answer that one question, and nothing more. It shows the full state after every action, so you see the answer instead of guessing at it. Then it ships a short **SPIKE VERDICT** (a fixed, one-page verdict block), logs the answer so no one rebuilds it later, and throws the prototype away. Only the answer moves forward.

## Use it when

- "Let's mock this up before we build it for real."
- "Does this data model actually hold together, or are we missing a case?"
- "We have three ideas for this screen. Which one reads best?"

## Don't use it for

- Production code. This skill's whole point is to throw the code away. Use your normal build process instead.
- Iterating on something you are keeping and measuring — use [`jail-lab`](../jail-lab/) instead.
- Checking that finished work is done right — use [`jail-verify`](../jail-verify/) instead.

## What you get

A one-page **SPIKE VERDICT** — the question, the answer, and quoted proof from the run — plus one line added to a running ledger, so the same question never gets prototyped twice.

## Example

**You ask:**

> We're adding compliance approval to batch sends in Remind. The spec proposes three states for a batch: Draft, Pending, Approved. What happens when the compliance officer approves most of a batch but rejects a couple of items? Does the three-state model hold up, or do we need a fourth state? Prototype it before we build it.

**It produces:**

```
...
## SHIP GATE — 5 of 5

1. Ledger checked before building — PASS. Searched first; no prior entry on this question.
2. Throwaway name present — PASS. File header reads `PROTOTYPE — wipe me`; script lives in `proto-approval-flow/`, not `src/`.
3. Zero files under production paths — PASS. Nothing touched in the Remind codebase.
4. ≥1 surfaced-state observation quoted verbatim — PASS (see EVIDENCE below).
5. ARCHIVE pointer resolves — PASS. `scratch/proto-approval-flow.py` on throwaway branch `proto/batch-approval-states`, unmerged.

SPIKE VERDICT
QUESTION:     Does a three-state approval flow (Draft → Pending → Approved) hold for batch sends when a compliance officer partially rejects a batch, or does partial rejection force a fourth batch-level state?
SHAPE:        logic
TIMEBOX:      1 session → 1 session (no extension needed)
LEDGER-CHECK: none
EVIDENCE:     "batch B-1042 (Silvercrest Recovery) -> status: needs resubmission" with r1-r3 shown `approved` and r4-r5 shown `rejected` in the same state dump (step 3 of the run)
VERDICT:      answered
ARCHIVE:      scratch/proto-approval-flow.py (branch proto/batch-approval-states, not merged)
CONSUMER:     jail-memory

SPIKE LEDGER entry appended:
`2026-07-26 · Does a 3-state batch approval flow (Draft/Pending/Approved) hold under partial rejection? · answered · scratch/proto-approval-flow.py (branch proto/batch-approval-states) · supersedes:none`
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
