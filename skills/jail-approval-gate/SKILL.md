---
name: jail-approval-gate
metadata:
  version: 1.2.0
description: >-
  Classify every intended action into approval tiers BEFORE acting — never /
  per-action approval / batchable approval / auto-allowed — and fail closed:
  irreversible, external, durable, spend, or sensitive-data actions pause for
  a human with a proper approval request (what, why, blast radius,
  reversibility, safer alternative). Use at the start of any agentic run that
  will act on the world (send, publish, deploy, delete, buy, write durable
  memory, contact someone), when the user asks "what will you do without
  asking me", or when another skill's plan contains approval_required items.
  Do NOT use for pure analysis/drafting tasks that touch nothing external.
---

# JAIL-APPROVAL-GATE

Skills recommend; humans authorize. The gate is designed before the run, not
improvised mid-run — and where a tier is unclear, the gate **fails closed**.
[Constitution Rules 3, 5]

## Step 1 — Inventory the actions
Before executing a plan, list every action that touches the world: sends,
publishes, deploys, deletes, purchases, commitments, credential use, data
egress, durable memory/knowledge writes, external contacts. If the plan is
another skill's output, its `approval_required` list is the starting
inventory — but re-derive it; upstream may have missed some.

## Step 2 — Tier every action
First matching rule wins — tier assignment is a lookup, not judgment;
stricter tiers are checked first, so ties favor the stricter tier. [Rule 3]
1. Violates law, policy, the strictest applicable requirement, or sends
   protected data to an unauthorized destination (see jail-quarantine) →
   **NEVER** — blocked outright; not approvable in-run.
2. Irreversible, an external communication, a production change, spend, a
   credential-scope change, a durable memory write, or blast radius beyond
   the workspace → **PER-ACTION** — a human approves each instance.
3. Repeated, homogeneous, low-variance, and one example represents the
   batch honestly → **BATCHABLE** — approved as a pattern once per run.
4. Reversible AND workspace-local AND non-durable (drafting, analysis,
   sandbox runs, reading permitted sources) → **AUTO** — proceed without
   asking.
5. Else → **PER-ACTION** (the default; unclear tiers fail closed).

## Step 2b — The standing profile (stop re-deriving the gate every run)
- **First run in a project:** after the human has tiered the inventory,
  offer to persist the tier map as an **APPROVAL PROFILE** — an ADR-shaped
  jail-memory entry (context: this project · decision: the tier map ·
  consequences: what auto-proceeds · status: accepted, dated). The write
  itself is PER-ACTION (it's durable).
- **Later runs:** load the profile, apply it, and say so ("standing profile
  2026-07-22 applied — say 'retier' to revise"). Then DIFF: action types
  not covered by the profile default to PER-ACTION until the human tiers
  them; never stretch an old approval over a new action type.
- A profile is a memory, so jail-memory's freshness rule applies: one
  contradicted by current instructions is flagged and updated, not obeyed.
  No jail-memory / no platform memory → keep the profile as a dated block
  the user can paste into future sessions (the manual fallback).

## Step 3 — The approval request (what the human sees)
Per approval, one compact block — a human can't authorize what they can't
evaluate:
```
APPROVAL REQUEST
Action: <exactly what will happen, to what, where>
Why: <the objective it serves>
Blast radius: <who/what is affected if this goes wrong>
Reversibility: <one-way | two-way — and the undo path if two-way>
Safer alternative: <the more conservative option and its cost>
```
No response = not approved. Proceed-by-timeout is forbidden.

## Step 4 — Audit trail
Before asking, restate the action's effects, targets, and reversibility in
one line — a human approves the summary, not just the tier. Record every
tier assignment and approval/denial as one line — a disputed action later is
settled by the ledger, not by memory:
```
GATE-RECORD | action=<> | tier=<NEVER|PER-ACTION|BATCHABLE|AUTO> | approver=<> | ts=<ISO8601> | result=<approved|denied|pending>
```
No validator script exists for this — eyeball each GATE-RECORD line for all
five fields.

Close with the JAIL-HANDOFF block: `approval_required` carries every
PER-ACTION and BATCHABLE item still pending.

## Related skills
Sensitive-data handling and egress → **jail-quarantine** (its NEVER rules
feed this gate). Durable memory writes → **jail-memory** (they arrive here
as PER-ACTION). Executing the gated plan across agents →
**jail-orchestrate** (each agent inherits the tiers; delegation never
launders an approval).

## Gotchas
- **Tier inflation for comfort.** Marking everything PER-ACTION buries the
  human in prompts until they approve blind. AUTO exists so approvals stay
  meaningful — tier honestly.
- **Batch smuggling.** Approving "send the outreach" then adding recipients
  the human never saw. A batch is closed at approval time; additions are new
  requests.
- **Fail-open drift.** "It was probably fine" on an unclassified action. The
  default is PER-ACTION; unclear = ask.
- **Approval by ambiguity.** Reading "sounds good" about the *plan* as
  authorization for the *actions*. Approval attaches to the specific request
  block, nothing wider.
- **Delegation laundering.** A subagent doing what the orchestrator couldn't
  do unapproved. Tiers travel with the work.
