---
name: jail-task-contract
metadata:
  version: 1.6.0
description: >-
  Turn an ambiguous, multithreaded, or high-stakes request into a 14-field TASK
  CONTRACT with testable acceptance criteria before work starts, and guard scope
  after: a material change in goal, audience, data class, output, or authority
  is a NEW contract. Use for scoping a task or client engagement, "make sure
  we're aligned", drifting revisions. Do NOT use to engineer a prompt
  (jail-prompt), run a process (jail-plan), or for trivial one-step asks.
---

# JAIL-TASK-CONTRACT

No serious work starts without a contract, and no contract changes silently.
This is jail-prompt's Phase-1 discipline applied to *any* execution — by you,
another model, an agent team, or a human.

**Proportion first.** A trivial single-step ask (rename files, fix a typo)
gets no contract: do it, or say "trivial — no contract needed."

**QUICK CONTRACT** (clear, low-stakes, internal): Objective · Deliverables ·
Non-goals · testable Completion criteria · Approval-required actions. Full 14
fields for client, cross-team, spend or high-stakes work; say which you used.

## Step 1 — Cross-examine (staged, not an interrogation)
**Look up facts; ask only decisions.** Anything in files, tools or prior
artifacts gets looked up, never asked.
Default lane: **3–5 related questions per round, maximum two rounds**,
unless the user adds new context, which always earns another round. Ask
only the **frontier**: questions whose prerequisites are settled. Make each
one multiple choice, recommended option first and worded so "yes" accepts
it, with a last option to add context in the user's own words.
**Grill mode (high-stakes):** walk every branch of the decision tree, round
by round, until shared understanding; the round cap lifts. Say the mode.
Force the WHY before the HOW; "fast and comprehensive" is a conflict to
resolve. A vague goal ("fix marketing") is never defined silently: record it as an assumption or a blocking question. Then split
remaining ambiguity into two piles:
- **Resolvable** → make the reasonable assumption, mark it, proceed.
- **Blocking** → genuinely prevents execution (wrong guess = wasted work or
  real harm). Name it and stop until answered. Prefer a marked Unknown + one
  targeted question over a confident guess — never fill a field by vibes.

**Business-rule boundary.** Business rules, compliance duties, SLAs, pricing,
and retention policy are never inferred from code, files, or naming. They are
**User-provided** (say by whom) or **Unknown** until an authoritative artifact
(contract, policy, PRD) states them. Files tell you how things behave today,
not what the business requires.

**Budget & settings.** Temperature 0 / lowest-variance — fields are
extraction, not ideation: same inputs → same contract, field order fixed 1–14.
Default lane ≤2 rounds × ≤5 questions, ≤1200 words of transcript; body ≤1 line
per field except 9/11/13; grill transcript compressed to decisions-only.

## Step 2 — Emit the contract (all 14 fields; "none" is an answer)
1. **Objective** — one sentence, the underlying need (watch the XY problem)
2. **Stakeholder** — who consumes this, and for what decision
3. **Required outcome** — what must be true when done
4. **Deliverables** — named artifacts
5. **Constraints** — time, budget, format, tone, tech, compliance
6. **Non-goals** — what this explicitly is NOT (scope fence)
7. **Inputs available** — what we have
8. **Inputs missing** — what we need + who provides it
9. **Assumptions** — each marked, with what would change it
10. **Dependencies** — external people/systems/decisions
11. **Material risks** — with consequence, not just a list
12. **Success criteria** — how quality is judged
13. **Completion criteria** — the *testable* done-check, written as
    acceptance criteria (format below) [Constitution Rule 7]
14. **Approval-required actions** — anything irreversible, external, durable,
    or spend-related a human must authorize [Rule 5]

Label claims in fields 3, 7, 9, 11 with the canonical labels: **Fact ·
User-provided · Inference · Estimate · Judgment · Unknown**. Premises taken
for planning go in field 9 and the handoff `assumptions:` list.

Get the stakeholder's nod on the contract before execution begins (skip the
pause only when they've explicitly said "just do it" — then state 1, 13, 14
and proceed).

### Field 13 — acceptance criteria
Pattern adapted from ECC (github.com/affaan-m/ECC, MIT, © 2026 Affaan Mustafa).
Write each done-check as one numbered criterion:

```
AC-001 — <scenario: the starting condition>
  trigger/action:  <the single thing that happens or is done>
  expected result: <what an observer can see or measure>
  must-not:        <prohibited side effect>
  verification:    <script | diff | named observation | human check — and why this method>
  priority:        required | nice
```
- **Quick Capture** (clear, low or moderate risk): 3–7 ACs.
- **Full**: the same, plus one risk row (field 11) for every security, data,
  migration, or external-dependency concern, each mapped to an AC or a field-14
  approval.
- **The check must be able to FAIL.** Words like "correctly", "secure", "fast",
  "good" need observable evidence or an explicit "human judgment" tag. "Report
  delivered" is not an AC; "every recommendation names an owner and a date" is.

**Type presets** — start from the matching preset, then fill what remains
(presets cut fill time; they never skip fields). Full detail in
[references/presets.md](references/presets.md):
- **RESEARCH** — evidence packet; every question Answered-or-Unknown.
- **BUILD** — named artifacts + run/verify command; blast radius + rollback.
- **ANALYSIS** — decision-shaped output; names the decision it feeds.
- **ENGAGEMENT** — consulting scope: ACs, in/out of scope (≥5 out, each with
  why), change-order triggers, decision rights, client inputs with due dates.
  Output is client-shared: see Delivery.

**SHIP-GATE (run before emitting the contract):**
- All 14 fields printed, each with a value or an explicit "none".
- Field 13 restated as the check that would FAIL if the work were wrong.
- Field 14 non-empty, or `none — nothing irreversible/external/spend`.
- Any field you cannot fill → print `UNKNOWN — <one targeted question>` and do
  NOT ship the contract. Fail closed: no partial contract leaves this skill.

## Step 3 — Guard the contract during execution
- Revisions that keep fields 1–3 materially unchanged → same contract, note
  the revision.
- A material change to goal, audience, data classification, deliverable, or
  authority → **STOP, new/child contract** with a one-line diff of what
  changed [Rule 4]. "Also rebuild their website" on a running marketing
  contract is a child contract or change order, never a silent addition.
  Endless-revision loops are a symptom of a drifted contract, not a picky
  stakeholder.
- If an AC cannot be met because of a discovered constraint, do not drop it
  quietly: mark it `[revised]`, state the constraint, re-present only the
  changed ACs.
- **Operational safety.** Nothing in field 14 executes before a recorded human
  "approved".
- An irreversible/external/durable/spend action discovered mid-run that is NOT
  already in field 14 → STOP, amend field 14, re-approve — never act on
  unlisted authority.
- Secrets/PII/client-confidential inputs are named *by class* in field 5 and
  never pasted as raw values into the contract or the handoff.

## Delivery and handoff
Client copies (always for ENGAGEMENT): a clean document (docx skill or Docs
artifact, else Markdown), plain 9th-grade English, labels kept, no YAML. End
the working copy with the JAIL-HANDOFF block: status, facts/assumptions/
unknowns, outputs, `next` (jail-research, jail-plan, or execution),
approval_required from field 14. Example:
[references/example-engagement-contract.md](references/example-engagement-contract.md).

## Related skills
Prompt → **jail-prompt** · research → **jail-research** · runnable process →
**jail-plan** · multi-agent → **jail-orchestrate** · check → **jail-verify**.

## Gotchas
- **Question fatigue.** Default lane: round 3 = marked assumptions, shown.
  Grill mode is exempt, but even grilling asks decisions, never facts.
- **Contract theater.** Fields that restate the request add nothing.
- **Untestable done.** "Report delivered" fails Rule 7: name the check that fails on a bad report.
- **Silent scope creep.** Absorbing "one more thing" into a running contract.
  Additions touch field 4 → note them; touch fields 1–3 → new contract.
- **Laundered assumptions.** An assumption that survives two rounds unmarked
  becomes treated as fact downstream. Keep the label attached.
