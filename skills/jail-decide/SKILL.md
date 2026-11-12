---
name: jail-decide
metadata:
  version: 1.3.0
description: >-
  Turn a choice into a defensible DECISION PACKAGE: options incl. do-nothing,
  criteria first, one recommendation with confidence and change-conditions.
  Use for "which should we pick", "should we do X or Y", "build vs buy", "is
  this worth doing", "help me decide", "run the numbers on A vs B and pick
  one", "cheaper over N years". Do NOT use to score one subject 0-10
  (jail-rate), gather evidence (jail-research), or attack an option
  (jail-red-team).
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
- **When evidence is thin:** If the criteria that decide the call rest only on
  assumptions or Unknowns (no data supplied), do NOT issue a confident
  recommendation: mark those criteria "judged on assumption", cap confidence
  at low, name the specific evidence needed, and route to jail-research.
- Evidence base: pull the jail-research packet or the supplied facts; every
  load-bearing fact keeps its label and source. Thin evidence → say which
  criteria are being judged on assumption, or route back to jail-research.
  **Sensitive inputs**: personnel, comp, health, and privileged facts plus NDA
  figures enter the package as roles, bands, and ranges — never verbatim
  records or names. No raw evidence dump inside the package. If the call cannot
  be made without exposing regulated data, stop and ask the named owner rather
  than restating it.

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
  prose — the lane is earned by evidence, not ambition. Worksheet and a
  checked numeric example: [references/expected-value.md](references/expected-value.md).

## Step 3 — Recommend
Budget: package ≤450 words (options table ≤5 rows, rationale ≤4 sentences) —
cite the jail-research packet by reference, never restate its evidence. Fixed
order: do-nothing first, then the rest by recommendation rank. Two options
inside the evidence noise are declared a **tie** and broken by a named
criterion — never a silent pick.
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
jail-plan turns the chosen option into a working process;
jail-summarize presents it. A complete worked run (ship-check line, package,
handoff): [references/example-package.md](references/example-package.md).

**Decision log (optional, durable decisions only).** If the decision will
outlive this session, add one line for jail-memory in ADR shape:
`context: … · decision: … · consequences: … · status: proposed|accepted`.
jail-memory decides whether to store it; this skill never writes memory itself.

## Ship-check
Run all 7 gates before releasing the package and emit the verdict as ONE line:

```
Ship-check: criteria-first PASS|FAIL · do-nothing priced PASS|FAIL · door type
per option PASS|FAIL · ≥2 change-conditions PASS|FAIL · every number carries
Fact/Estimate+source PASS|FAIL · owner named PASS|FAIL · council check
recorded PASS|FAIL
```
Given an existing draft/package/recommendation as input: run this line FIRST
against it as received and keep the real FAILs — that line is the audit
record that the gate bit. Then fix the package and emit a SECOND line. Never
emit only a clean line for a draft that arrived violating a gate.

Fail-closed: any FAIL → fix the package and re-run the line. A gate that
can't be closed from the input at hand (no owner nameable, no source
obtainable) is never left a silent open FAIL on a shipped package: emit the
FAIL, name the specific question or evidence that would close it, and
withhold the package — never invent a value to make the line read clean.

## Delivery (client-facing)
When the package goes to a client, render it as a clean document (docx skill
or a Docs artifact when available; otherwise clean Markdown): plain
9th-grade English, short sentences, labels (Fact, Estimate, …) kept, options
table kept, no YAML in the client copy. The JAIL-HANDOFF block stays in the
chat/working copy, never in the client document.

## Related skills
Score one subject → **jail-rate**. Evidence missing → **jail-research**.
Pressure-test the winning option → **jail-red-team**. Make it operational →
**jail-plan**.

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
