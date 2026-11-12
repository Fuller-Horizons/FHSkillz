# Chain assembly & verification

Load this when Phase 3 decides the goal needs a **chain** (2–4+ sequenced
prompts) instead of one prompt. A chain is only as good as its handoffs — this
file defines the manifest that makes handoffs explicit, the gates that run
between steps, and the linkage check that proves the chain is wired correctly
before you run a single token.

## When to chain

Chain when distinct stages need **different expertise, separate verification, or
human judgment between them** — e.g. `extract findings → derive personas →
prioritize roadmap → model finances`. One great prompt beats a bloated one; a
clear chain beats a single impossible one. If one prompt can do the job well,
do not chain — added stages cost tokens and add failure points.

## The chain manifest

Emit one manifest per chain so the steps are machine-checkable and any agent can
resume mid-chain. Each step's `produces` keys are the only things later steps may
name in `requires`. Keep keys stable, lowercase-hyphenated.

```json
{
  "chain": "research-to-roadmap",
  "inputs": ["transcripts"],
  "success_test": "roadmap.json validates against roadmap.schema.json and every item traces to >=1 finding id",
  "steps": [
    {
      "id": "extract",
      "requires": ["transcripts"],
      "produces": ["findings"],
      "success_test": "findings.json parses; each finding has id + source quote",
      "on_fail": "retry"
    },
    {
      "id": "personas",
      "requires": ["findings"],
      "produces": ["personas"],
      "success_test": "personas.json parses; each persona cites >=2 finding ids",
      "on_fail": "stop"
    },
    {
      "id": "roadmap",
      "requires": ["findings", "personas"],
      "produces": ["roadmap"],
      "success_test": "roadmap.json validates against schema; items ranked",
      "on_fail": "stop"
    }
  ]
}
```

Each step is *also* a full JAIL Phase 3 prompt block (the manifest is the wiring;
the prompt blocks are the work). The step's `requires`/`produces`/`success_test`
must match the `METADATA` and `SUCCESS TEST` lines of its prompt block.

## Checkpoint gates (between every step)

Each step is graded against its own `success_test` before the next step starts.
`on_fail` declares what happens when it falls short — never silently continue:

| `on_fail` | Behavior |
|---|---|
| `retry` | Re-run the step once with the failure noted; if it fails again, escalate to `stop`. |
| `stop`  | Halt the chain, return what's produced so far + the failing step's gaps. The default for any step a later step depends on. |
| `rollback` | Discard this step's output and return to the prior checkpoint (use when a step can corrupt an earlier artifact). |
| `human` | Pause for human review before continuing (use for irreversible or high-stakes steps — pairs with the Phase 2 high-stakes escalation). |

A step whose output feeds a dependent step should never be `retry`-forever; cap
retries at one, then `stop`. The chain-level `success_test` is graded only after
the final step and is the contract for the whole chain — per-step tests passing
does not guarantee the chain goal is met.

## Fan-out / fan-in

The default chain is linear. Two non-linear shapes are allowed when they fit:

- **Fan-out** — one step's output feeds *several* independent steps that can run
  in parallel (e.g. `brief → [draft-email, draft-tweet, draft-blog]`). In the
  manifest, multiple steps share the same key in `requires`.
- **Fan-in** — several steps' outputs merge into one (e.g.
  `[scan-pricing, scan-features, scan-reviews] → synthesize`). The merge step
  lists every upstream `produces` key in its `requires`; `chain-lint` confirms
  all are satisfied before the merge can run.

Keep parallel branches genuinely independent — if branch B needs branch A's
output, it is sequential, not fan-out, and must say so in `requires`.

## Verify before running

With the companion **jail-py-toolkit** skill installed, run its linker
check on the manifest:

```bash
python3 <jail-py-toolkit>/scripts/chain-lint.py chain.json   # 0 pass · 1 errors · 2 IO
```

Without it, walk the manifest manually: every `requires` key traced to an
earlier `produces` (or declared `inputs`), and a success test present per step
and for the chain.

It fails if any step `requires` a key that no earlier step (or declared `inputs`)
`produces` — i.e. a broken handoff — and warns on steps with no
machine-verifiable `success_test`, a missing chain-level `success_test`, or keys
that are produced but never consumed. Fix every error before emitting the chain;
a chain that doesn't lint will fail at runtime no matter how good each prompt is.
