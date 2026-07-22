---
name: jail-bmc
metadata:
  version: 1.2.0
description: >-
  Build or evaluate a nine-block Business Model Canvas (customer segments,
  value propositions, channels, customer relationships, revenue streams, key
  resources, key activities, key partnerships, cost structure) using
  evidence — every material element marked validated vs hypothesis, with the
  riskiest assumptions and the experiments to test them. Use when asked for
  a "business model canvas", "BMC", "map the business model", evaluating a
  venture/product idea's model, or pressure-testing how a business makes
  money. Do NOT use for macro scans or competitive
  self-assessment (jail-strategy-scan), or entity/legal-structure questions.
---

# JAIL-BMC

A canvas full of hopes is brainstorming with borders. This skill's contract:
**validated information and hypotheses never wear the same clothes**, and
the riskiest assumption leaves with an experiment attached.

## Chain
1. **jail-task-contract** — pin the venture/product, its stage (idea vs
   operating), the decision the canvas serves (invest? pivot? launch?), and
   what evidence already exists.
2. **jail-research** — evidence per block where it exists: pricing
   comparables, channel economics, competitor models, cost benchmarks.
   Dated citations. **Do not invent market validation** — absence of
   evidence is recorded as hypothesis, never papered over.
3. **Populate the nine blocks.** Every material element carries:
   statement · **VALIDATED** (evidence ref: real transactions, signed
   customers, measured data) **or HYPOTHESIS** (assumption label +
   evidence strength: none/weak/comparable-based) · confidence.
4. **Coherence pass — blocks must agree:**
   - Segment ↔ value proposition: each segment maps to a proposition
     written in that segment's words.
   - Revenue ↔ segments: someone specific pays; "users" who don't pay push
     the payer into its own segment.
   - **Unit-economic dependency:** revenue per customer vs cost to acquire
     + serve — name the numbers or name the hypothesis. A model whose
     economics only work at unstated scale says so.
   - Key activities/resources ↔ value proposition: the thing you must be
     good at is listed, and it's evidenced or flagged.
   Contradictions between blocks are findings, not footnotes.
5. **jail-red-team** — attack the model: the segment that won't pay, the
   channel that doesn't reach them, the partnership that's actually a
   dependency risk, second-order competitor response.
6. **Rank assumptions by risk** (impact-if-wrong × evidence weakness) and
   attach to each of the top 3–5 a **validation experiment in jail-lab
   spec shape**: metric + direction · the ONE variable under test · bounded
   run (with whom, how long, cost) · measurable pass/fail threshold —
   sequenced cheapest-decisive-first. Runnable experiments hand off to
   **jail-lab** directly (results land in its ledger; a KEEP promotes the
   hypothesis toward VALIDATED on the next canvas pass).
7. **jail-decide** → strategic implications and next actions.
   **jail-exec-brief** → **jail-verify** (labels intact? blocks coherent?
   riskiest assumptions have experiments? no invented validation?).

## Canvas-delta mode (revisiting an existing canvas)
Input: the prior canvas + what changed (experiment results, new evidence,
a pivot). Don't rebuild: **diff** — list blocks touched by the change ·
promote/demote labels where evidence moved (HYPOTHESIS → VALIDATED needs
the evidence ref; VALIDATED → stale gets re-flagged) · re-run the
coherence pass ONLY on touched blocks + their dependents · re-rank
assumptions (a resolved top-3 assumption pulls the next one up). Output
leads with the delta table (block · was → is · driver), then the updated
canvas. Cheap by design — this is what makes the canvas a living document
instead of a one-shot workshop artifact.

## Output
The nine-block canvas (each element labeled V/H + confidence) → internal
inconsistencies found → unit-economic dependencies → top risky assumptions
with their experiments and sequence → customer validation questions →
strategic implications + next actions. Sources appendix. JAIL-HANDOFF.

## Gotchas
- **Invented validation.** "Customers love it" pre-revenue. VALIDATED means
  transactions, commitments, or measured behavior — with the ref.
- **Everyone-segments.** "SMBs and enterprises and consumers" is not a
  segment, it's a hedge. Segments are specific enough to name a channel.
- **Coherence skipped.** Nine beautiful blocks that contradict each other —
  step 4 is where canvases earn their keep.
- **Assumption ranking dodged.** Ten assumptions listed flat. The top-3
  ranking + experiments is the deliverable investors actually use.
- **Costless models.** Cost structure as an afterthought while revenue gets
  three colors. Unit economics or hypothesis-labeled — both sides.
