---
name: jail-bmc
metadata:
  version: 1.4.2
description: >-
  Build or evaluate a nine-block Business Model Canvas: "business model
  canvas", "BMC", "map the business model", pressure-test how a venture or
  product idea makes money. Marks every element validated vs hypothesis,
  checks unit economics (CAC, LTV, payback), ranks the riskiest assumptions
  with tests. Do NOT use for SWOT/PESTLE or macro scans (jail-strategy),
  0-10 scoring (jail-rate), or entity/legal-structure questions.
---

# JAIL-BMC

A canvas full of hopes is brainstorming with borders. This skill's contract:
**validated information and hypotheses never wear the same clothes**, and
the riskiest assumption leaves with an experiment attached.

**Wrong-lane check first.** Asked for a SWOT, TOWS, PESTLE, five forces or
competitor scan? That is **jail-strategy**'s job: say so in one line and
hand off to it by name, or (if it isn't available) write the SWOT now in
jail-strategy's shape from what was given, with stated assumptions; any
questions come after the analysis. Never force a canvas, and never reply
with questions only.

**Label mapping (declared once).** This skill keeps two domain labels:
**VALIDATED** = a Fact-backed element (it carries a checkable evidence
ref); **HYPOTHESIS** = an Assumption (it goes in the handoff
`assumptions:` list). Any prose claim outside the canvas table uses the
canonical labels: Fact · User-provided · Inference · Estimate · Judgment ·
Unknown.

## Chain
1. **jail-task-contract** — pin the venture/product, its stage (idea vs
   operating), the decision the canvas serves (invest? pivot? launch?), and
   what evidence already exists. *(Fallback: capture inline.)*
2. **jail-research** — evidence per block where it exists: pricing
   comparables, channel economics, competitor models, cost benchmarks.
   Dated citations. **Do not invent market validation** — absence of
   evidence is recorded as hypothesis, never papered over. *(Fallback:
   cite-or-label per the constitution.)*
3. **Populate the nine blocks.** Every material element carries:
   statement · **VALIDATED** (evidence ref: real transactions, signed
   customers, measured data) **or else HYPOTHESIS** (assumption label +
   evidence strength: none/weak/comparable-based) · confidence.
   **Fail closed:** VALIDATED needs a checkable evidence ref (dated
   citation, transaction, signed commitment) or it defaults to
   HYPOTHESIS. An operating owner's own current figures (customers, prices,
   costs, volumes) are VALIDATED with ref `User-provided: owner, <date>`
   and a spot-check note; forecasts and plans stay HYPOTHESIS; step 4 may not start until every element is labeled.
   **Fixed schema**, blocks always in this order (customer segments,
   value propositions, channels, customer relationships, revenue
   streams, key resources, key activities, key partnerships, cost
   structure): `Block | Element | Label(V/H) | Evidence ref |
   Confidence`.
4. **Coherence pass — blocks must agree:**
   - Segment ↔ value proposition: each segment maps to a proposition
     written in that segment's words.
   - Revenue ↔ segments: someone specific pays; "users" who don't pay push
     the payer into its own segment.
   - **Unit-economic dependency:** revenue per customer vs cost to acquire
     + serve — name the numbers or name the hypothesis. A model whose
     economics only work at unstated scale says so. Fill the worksheet in
     [references/unit-economics.md](references/unit-economics.md): CAC by
     channel, margin, churn, lifetime, LTV, LTV:CAC, payback, contribution
     margin; every input labeled VALIDATED (evidence ref) or HYPOTHESIS.
     *(Fallback: if the reference is unavailable, compute CAC = spend ÷ new
     customers; margin = price − cost to serve; lifetime = 1 ÷ monthly
     churn; LTV = margin × lifetime; payback = CAC ÷ margin.)*
   - Key activities/resources ↔ value proposition: the thing you must be
     good at is listed, and it's evidenced or flagged.
   Contradictions between blocks are findings, not footnotes.
5. **jail-red-team** — attack the model: the segment that won't pay, the
   channel that doesn't reach them, the partnership that's actually a
   dependency risk, second-order competitor response. *(Fallback: run
   these attack points inline.)*
6. **Rank assumptions by risk** (impact-if-wrong × evidence weakness) and
   attach to each of the top 3–5 a **validation experiment in jail-lab
   spec shape**: metric + direction · the ONE variable under test · bounded
   run (with whom, how long, cost) · measurable pass/fail threshold —
   sequenced cheapest-decisive-first. Runnable experiments hand off to
   **jail-lab** directly (results land in its ledger; a KEEP promotes the
   hypothesis toward VALIDATED on the next canvas pass). *(Fallback:
   without jail-lab, log metric/variable/bound/threshold inline and run
   it manually.)*
7. **jail-decide** → strategic implications and next actions. *(Fallback:
   state implications inline.)* **jail-summarize** for voice. *(Fallback:
   tighten inline.)* Then the **SUCCESS-TEST** below gates the
   JAIL-HANDOFF — run it via **jail-verify**. *(Fallback: walk the
   checklist manually.)*

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

**Visual canvas (optional).** If an artifact, HTML, or Design tool is
available, render the nine blocks as a one-page grid in the standard BMC
layout with V/H badges, following
[references/canvas-render.md](references/canvas-render.md). Otherwise use
the fixed table from step 3. Same content either way.

## Delivery
When the canvas goes to a client, render it as a clean document (docx
skill or a Docs artifact when available; otherwise clean Markdown).
Plain 9th-grade English, short sentences, few or no analogies. Keep the
V/H labels and the canonical claim labels. No YAML in the client copy;
the JAIL-HANDOFF stays in the chat or working copy.

## SUCCESS-TEST (run before shipping)
Gates the JAIL-HANDOFF; a fail sends it back to the failing step, not out
the door.
- Labels intact — every material element is VALIDATED or HYPOTHESIS.
- Coherence pass (step 4) done, contradictions logged, not smoothed over.
- Top 3–5 assumptions carry a jail-lab-spec experiment, cheapest-first.
- No VALIDATED element lacks a checkable evidence ref.

Worked examples: [references/worked-canvas.md](references/worked-canvas.md)
(operating business) and
[references/example-pool-subscription.md](references/example-pool-subscription.md)
(pre-revenue, full run with JAIL-HANDOFF).

## Gotchas
- **Invented validation.** "Customers love it" pre-revenue. VALIDATED means
  transactions, commitments, or measured behavior — with the ref.
- **Everyone-segments.** "SMBs and enterprises and consumers" is not a
  segment, it's a hedge. Segments are specific enough to name a channel.
- **Coherence skipped.** Nine beautiful blocks that contradict each other —
  step 4 is where canvases earn their keep.
- **Ranking dodged.** Ten assumptions listed flat. The top-3
  ranking + experiments is the deliverable investors actually use.
- **Costless models.** Cost structure as an afterthought while revenue gets
  three colors. Unit economics or hypothesis-labeled — both sides.
