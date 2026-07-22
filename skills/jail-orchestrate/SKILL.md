---
name: jail-orchestrate
metadata:
  version: 1.1.0
description: >-
  Run multiple agents/subagents as one coordinated system — decide when
  delegation earns its cost, assign non-overlapping scopes with minimum
  sufficient context, keep a dependency graph and resume ledger, audit
  progress against real tool results, reconcile conflicts by evidence, and
  integrate one final result. Use when work splits across parallel agents or
  research streams: "fan this out", "use subagents", "divide this up",
  long-horizon multi-part execution, or when jail-research/jail-task-contract
  hands off a parallelizable plan. Do NOT use for single-agent tasks or for
  defining the human-run process itself (jail-operationalize).
---

# JAIL-ORCHESTRATE

Delegation is a cost — paid in context, coordination, and conflicting
outputs. It must be earned, bounded, and audited. [Constitution Rule 11]

## Gate 1 — Is delegation worth it?
Delegate only when at least one is true: streams are **independent** (true
parallelism), a stream needs **isolation** (fresh perspective, verifier ≠
worker), or the work **exceeds one context window**. Otherwise one agent,
sequential, wins — coordination overhead is real work lost.

## Gate 2 — Scope the squad
- **Non-overlapping scopes.** Each agent gets ONE question or workstream;
  write the boundary ("A: pricing evidence; B: security posture — neither
  touches the other's topic"). Overlap = duplicated work + merge conflicts.
- **Minimum sufficient context.** Each agent receives only what its scope
  needs — the relevant contract fields, not the whole conversation. Smaller
  briefs = cheaper, faster, less anchored agents.
- **Expected output + acceptance criteria per agent**, stated in the brief:
  format (prefer the JAIL-HANDOFF block or the evidence-packet shape), the
  done-check, and the citation rule if it researches.
- **Recursion bound:** agents may not re-delegate beyond depth 1 without the
  orchestrator's explicit approval; cap total agents up front.

**Slice work as tracer bullets.** When scoping build-type nodes, each
slice cuts a narrow but COMPLETE path through every layer — vertical, never
a horizontal slice of one layer; demoable/verifiable on its own; sized to
one fresh context window; prefactoring first ("make the change easy, then
make the easy change"). **Exception — wide refactors:** one mechanical
change whose blast radius spans the codebase can't land as a vertical
slice; sequence it expand–contract (add the new alongside, migrate
callers, remove the old) instead of forcing a tracer bullet.

## During the run — the ledger
Maintain a **dependency graph + completed-nodes ledger**: for every node
record scope, status, and the *artifact* proving completion. Rules:
- A node is complete when its artifact is **verified**, not when the agent
  says so — audit claims against actual tool results (files, logs, outputs).
- The ledger makes the run **resumable**: on crash or interruption, restart
  from the last verified node, never from zero, and never re-run verified
  work (idempotence).
- Watch for: duplicated work (two agents converging on one topic — re-fence
  the scopes), stalled dependencies, and scope drift inside an agent.

## Merge — where orchestration is won or lost
- **Reconcile conflicts by evidence**, not seniority or recency: apply
  jail-research's contradiction rule (strongest currently-applicable source
  wins; preserve the losing finding + why).
- Detect **incomplete handoffs**: every key a downstream node requires must
  have been produced upstream — a missing key stops the merge, it doesn't
  get improvised.
- Produce **one integrated result** with unified voice and one source list —
  never a stapled stack of agent outputs. Integration is the orchestrator's
  own work; budget for it.

Close with the JAIL-HANDOFF block — `next:` **jail-verify** (mandatory for
consequential runs: the orchestrator's own claims of completion are subject
to the same audit rule).

## Related skills
Contract first → **jail-task-contract**. Research streams → each agent runs
**jail-research** discipline. Final check → **jail-verify** (independent).
Human-run processes → **jail-operationalize**.

## Gotchas
- **Delegation as a reflex.** Fanning out a task one agent does better. Gate
  1 exists because the failure is silent — the result is just worse and
  slower.
- **Context dumping.** Pasting the whole history into every brief. Anchored
  agents converge on the same blind spots; minimum context is a feature.
- **Trusting the squad's self-reports.** "All agents report success" is
  hearsay. The ledger holds artifacts or the node isn't done.
- **Merge by concatenation.** Stapling outputs together and calling it
  synthesis. If the merged doc has three voices and two source lists, the
  orchestrator skipped its own job.
- **Unbounded recursion.** Agents spawning agents spawning agents. Depth cap
  and agent budget are set before the first brief goes out.
