---
name: jail-decide
metadata:
  version: 1.1.0
description: >-
  Convert analysis into a defensible DECISION PACKAGE — options (always
  including do-nothing), explicit criteria, costs/risks/reversibility per
  option, a recommendation with confidence and change-conditions, and
  immediate next actions. Use when someone must choose among options: "which
  should we pick", "should we do X or Y", "build vs buy", "is this worth
  doing", "help me decide", or downstream of research/analysis that ends in a
  choice — including quantified comparisons that end in a pick: "run the
  numbers on A vs B and choose", "which is cheaper/better over N years",
  "compare the costs and pick one" (the numbers feed the decision; the
  deliverable is the defensible pick, not the arithmetic). Do NOT use to
  score a single subject 0-10 (jail-rate), to gather the evidence itself
  (jail-research), or to attack one option's reasoning (jail-red-team).
---

# JAIL-DECIDE

A decision the owner can defend a year later: criteria stated before options
are scored, indecision priced, and the conditions that would flip the call
written down. [Constitution Rules 6, 11, 12]

## Step 1 — Frame
- **Decision statement** — one sentence: what is being decided, by whom
  (**decision owner**), by when (if a real date exists; don't invent one).
- **Criteria before options.** List the evaluation criteria and constraints
  FIRST, from the stakeholder's goals — not reverse-engineered from a
  favorite option. Weight them only if the stakes justify it.
- Evidence base: pull the jail-research packet or the supplied facts; every
  load-bearing fact keeps its label and source. Thin evidence → say which
  criteria are being judged on Assumption, or route back to jail-research.

## Step 2 — Options, honestly
- 2–5 real options. **Do-nothing / defer is always one of them**, priced like
  the rest: its costs, risks, and what delay forfeits. [Rule 12]
- Per option: benefits · costs (money, time, attention) · material risks ·
  **reversibility** (one-way vs two-way door) · dependencies · opportunity
  cost · consequences of delay. [Rule 6]
- A weighted decision matrix is optional equipment: use it when criteria and
  evidence support real numbers; otherwise comparative prose beats false
  precision — never let a made-up 7.2 outvote a true sentence.
- **Quantified lane** (money/time is load-bearing AND real numbers exist):
  per option add **expected value** (probability-weighted benefit − cost,
  as a RANGE when inputs are uncertain), **cost of delay** (what each
  month of not deciding forfeits — this prices do-nothing honestly), and
  payback/break-even where applicable. Every number carries its basis
  (Fact/Estimate + source); when inputs are gut-feel, stay in comparative
  prose — the lane is earned by evidence, not ambition.

## Step 3 — Recommend
```
DECISION PACKAGE
Decision: <statement> · Owner: <who> · Needed by: <date|open>
Criteria (+weights if used):
Options table: option · benefits · costs · risks · reversibility · delay cost
Recommendation: <option> — rationale in ≤4 sentences tied to the criteria
Confidence: high|medium|low — and why
Would change this call: <2–4 concrete conditions/observations>
Approval required: <anything in the recommendation a human must authorize>
Next actions: <first 1–3 steps, each with an owner>
```
Then the JAIL-HANDOFF block — `next:` jail-red-team for consequential or
contested calls (irreversible, money, legal/safety). **Council escalation
check (run it explicitly):** contested + high-stakes + hinging on a disputed
factual/interpretive question → convene **jail-council** on that question
(record "council: convened/not — why" in the package; a cheap Tier-D
mini-council covers cases that are contested but not existential).
jail-operationalize turns the chosen option into a working process;
jail-exec-brief presents it.

## Related skills
Score one subject → **jail-rate**. Evidence missing → **jail-research**.
Pressure-test the winning option → **jail-red-team**. Make it operational →
**jail-operationalize**.

## Gotchas
- **Criteria after options.** Scoring rubrics invented once a favorite exists
  always crown the favorite. Criteria are Step 1, in writing.
- **The missing do-nothing.** Omitting it hides the real baseline and
  railroads action. It's an option with a price — show the price.
- **False numerical precision.** A matrix full of gut-feel decimals is
  costume math. Downgrade to comparative prose when evidence is thin. [Rule 11]
- **Reversibility blindness.** Treating a one-way door like a two-way door is
  how bad decisions become permanent. Name the door type per option.
- **Recommendation without change-conditions.** If nothing could change the
  call, it wasn't analysis. State what evidence would flip it.
- **Deciding past the owner.** The package recommends; the named owner
  decides. Irreversible actions wait for them. [Rule 5]
