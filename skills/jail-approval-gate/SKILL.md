---
name: jail-approval-gate
metadata:
  version: 1.0.0
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
- **NEVER** — blocked outright: actions violating law, policy, the
  strictest applicable requirement [Rule 3], or sending protected data to an
  unauthorized destination (see jail-quarantine). Not approvable in-run;
  changing this tier is a human policy decision made outside the run.
- **PER-ACTION** — a human approves each instance: irreversible actions,
  external communications, production changes, spending, credential scope
  changes, durable memory writes, anything with a blast radius beyond the
  workspace. **The default tier for anything unclassified.**
- **BATCHABLE** — a human approves the pattern once per run ("send all 12
  outreach drafts after my review of the first"): repeated, homogeneous,
  low-variance actions where one example represents the batch honestly.
- **AUTO** — proceed without asking: reversible, workspace-local,
  non-durable work (drafting, analysis, sandbox runs, reading permitted
  sources).

Tie-break rule: when two tiers arguably apply, the stricter wins. [Rule 3]

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
Record every tier assignment and every approval/denial with timestamp and
approver — the run's authorization ledger. A disputed action later is
settled by the ledger, not by memory.

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
