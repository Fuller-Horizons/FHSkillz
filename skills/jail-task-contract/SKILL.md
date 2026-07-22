---
name: jail-task-contract
metadata:
  version: 1.1.0
description: >-
  Convert an ambiguous, multithreaded, or high-stakes request into an
  executable TASK CONTRACT before work begins — objective, stakeholder,
  deliverables, constraints, non-goals, missing inputs, assumptions, risks,
  testable success + completion criteria, and approval-required actions. Also
  guards scope after work starts: a material change in goal, audience, data
  classification, output, or authority is a NEW contract, not a revision. Use
  when starting any non-trivial task, when a request has multiple threads or
  unclear scope, when the user says "make sure we're aligned", or when
  revisions start drifting. Do NOT use to engineer a prompt (jail-prompt) or
  for trivial single-step asks.
---

# JAIL-TASK-CONTRACT

No serious work starts without a contract, and no contract changes silently.
This is jail-prompt's Phase-1 discipline applied to *any* execution — by you,
another model, an agent team, or a human.

## Step 1 — Cross-examine (staged, not an interrogation)
**Look up facts; ask only decisions.** Anything discoverable from the
environment (files, tools, prior artifacts) gets looked up, never asked —
the human's attention is spent exclusively on decisions that are theirs.
Default lane: **3–5 related questions per round, maximum two rounds.**
**Grill mode (high-stakes):** when a wrong guess is expensive, switch to an
exhaustive branch-walk — ONE question at a time, each with your recommended
answer, walking every branch of the decision tree until shared
understanding is reached; the two-round cap lifts. Say which mode you're in.
Force the WHY before optimizing the HOW. Challenge vague or conflicting
answers directly — "fast and comprehensive" is a conflict to resolve, not
transcribe. Then split
remaining ambiguity into two piles:
- **Resolvable** → make the reasonable assumption, mark it, proceed.
- **Blocking** → genuinely prevents execution (wrong guess = wasted work or
  real harm). Name it and stop until answered. Prefer a marked UNKNOWN + one
  targeted question over a confident guess — never fill a field by vibes.

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
13. **Completion criteria** — the *testable* done-check (a script, a diff, a
    named observation — never "looks good") [Constitution Rule 7]
14. **Approval-required actions** — anything irreversible, external, durable,
    or spend-related a human must authorize [Rule 5]

Get the stakeholder's nod on the contract before execution begins (skip the
pause only when they've explicitly said "just do it" — then state 1, 13, 14
and proceed).

## Step 3 — Guard the contract during execution
- Revisions that keep fields 1–3 materially unchanged → same contract, note
  the revision.
- A material change to goal, audience, data classification, deliverable, or
  authority → **STOP, new/child contract** with a one-line diff of what
  changed [Rule 4]. Endless-revision loops are a symptom of a drifted
  contract, not a picky stakeholder.

End with the JAIL-HANDOFF block (see docs/JAIL-CONSTITUTION.md): status,
facts/assumptions/unknowns, outputs (the contract), `next` (usually
jail-research, problem decomposition, or direct execution), and
approval_required carried from field 14.

## Related skills
Deliverable is a *prompt* → **jail-prompt**. Contract complete and research
needed → **jail-research**. Multi-agent execution → **jail-orchestrate**.
Verify the finished work against this contract → **jail-verify**.

## Gotchas
- **Question fatigue.** In the default lane, more than two rounds means you're
  outsourcing thinking — round 3 = marked assumptions, shown. Grill mode is
  exempt by declaration, but even grilling asks decisions, never facts.
- **Contract theater.** Filling all 14 fields with restated request text. Each
  field must add information the request didn't state.
- **Untestable done.** "Completion: report delivered" fails Rule 7. What check
  would FAIL if the report were bad or incomplete?
- **Silent scope creep.** Absorbing "one more thing" into a running contract.
  Additions touch field 4 → note them; touch fields 1–3 → new contract.
- **Assumption laundering.** An assumption that survives two rounds unmarked
  becomes treated as fact downstream. Keep the label attached.
