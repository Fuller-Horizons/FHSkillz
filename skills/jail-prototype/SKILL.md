---
name: jail-prototype
metadata:
  version: 1.1.0
description: >-
  Build a THROWAWAY prototype whose only job is to answer a stated design
  question — "does this logic/state model feel right?", "what should this
  look like?", "will this approach hold?" — then fold the validated answer
  into real work, register it in the SPIKE LEDGER (so answered questions are
  never re-prototyped), and discard the prototype. Use when the user wants
  to sanity-check a design, explore variations, "mock something up to see",
  "try it before we build it", or when jail-decide/jail-bmc needs a cheap
  experiment answered by building. Do NOT use for production implementation,
  metric-driven iteration on an existing thing (jail-lab), or verification
  of finished work (jail-verify).
---

# JAIL-PROTOTYPE

A prototype is **throwaway work that answers a question**. The question is
named first; the answer — not the artifact — is what survives. Discipline
adapted from Matt Pocock's `prototype`
([mattpocock/skills](https://github.com/mattpocock/skills), MIT), under
JAIL evidence rules.

## Step 0 — Name the question
One sentence, falsifiable-ish: *"Does the three-state approval flow feel
right for batch sends?"* · *"Which of three layouts makes the scorecard
scannable?"* · *"Can this parse strategy survive real inputs?"* No stated
question = no prototype — that's just building without a contract
[Constitution Rule 8]. The question decides the shape:
- **Logic/state question** → smallest interactive harness (terminal app,
  script, spreadsheet, even a paper walkthrough) that pushes the model
  through the cases hard to reason about in the abstract.
- **Look/feel question** → several **radically different** variations,
  switchable in one place — contrast answers look-questions; near-identical
  variants answer nothing.
- **Feasibility question** → the thinnest end-to-end spike through the
  riskiest part only.

## Rules (all of them, every prototype)
1. **Throwaway from day one, visibly marked.** Named so no casual reader
   mistakes it for production (`proto-`, `PROTOTYPE — wipe me`); lives near
   its target for context but never inside production paths.
2. **One command to run.** Whoever's judging the answer starts it without
   thinking.
3. **No persistence by default.** State lives in memory; durability is
   usually what's being *tested*, not a dependency. If storage IS the
   question, use a scratch target with a wipe-me name.
4. **Skip the polish.** No tests, no error handling beyond runnable, no
   abstractions. Every hour of polish is an hour not answering the
   question.
5. **Surface the state.** After every action, show the full relevant state
   — the judge must see what changed, not trust that it did.
6. **Timebox it.** A prototype that outlives its timebox without an answer
   has become a project — stop, report what was learned, re-scope the
   question.

## Step N — Capture the answer, kill the artifact
- **The verdict is the deliverable**: the question, the answer, and the
  evidence (what the prototype showed), recorded where the real work lives
  (decision note, ticket, jail-memory entry when durable).
- **Register it in the SPIKE LEDGER** — one line per answered question in
  the project's memory (jail-memory entry type: decision/spike; file-ledger
  fallback works): question · verdict · date · archive pointer. **Check
  the ledger BEFORE prototyping** — a question answered last month is
  retrieved, not rebuilt; a changed premise reopens it explicitly (new
  entry superseding the old, never silent re-litigation).
- **Feed the consuming decision**: when jail-decide (or jail-bmc's
  experiment sequence) sent the question here, the verdict returns as
  labeled evidence in that decision's options table — a prototyped answer
  is Fact-of-the-prototype, not Judgment.
- Fold the validated decision into the real implementation plan.
- The prototype itself is archived out of the mainline (throwaway branch,
  scratch folder) with a pointer — kept as a primary source, never merged.
  **Main keeps only the validated decision.**

## Related skills
Choosing among prototyped options → **jail-decide** (the verdicts are its
evidence). Business-assumption experiments → **jail-bmc** (its experiment
sequence often lands here). Iterating a *kept* thing by metric →
**jail-lab**. Durable design decision → **jail-memory** (ADR entry).

## Gotchas
- **Question-free prototyping.** "Let's just build something and see" —
  see *what*? Name the question or don't start.
- **Prototype promotion.** The demo works, deadline looms, throwaway code
  ships. The naming + branch rules exist for exactly this moment; the
  answer graduates, the code does not.
- **Polish creep.** Adding tests and error handling "while we're here."
  That's implementation wearing a prototype's name — stop or re-contract.
- **Twin variants.** Look-question variants that differ by a border color
  answer nothing. Radically different, or it's one option twice.
- **Unwitnessed state.** A prototype that hides its state proves only that
  it runs. Rule 5 is the evidence rule in miniature.
