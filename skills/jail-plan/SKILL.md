---
name: jail-plan
metadata:
  version: 1.1.0
description: >-
  Turn intent into an executable plan — two lanes. OPERATE: convert a
  decision, recommendation, or idea into a runnable OPERATING WORKFLOW
  (trigger, inputs, actions, tool, owner, approval, output, evidence,
  metric, frequency, risk, testable completion). MAP: navigate work too big
  and foggy for one session by charting a MAP of DECISION TICKETS and
  resolving them one at a time until the path to a named destination is
  clear. Use when analysis stops at "you should…" and someone must actually
  run it ("make this operational", "turn this into a process", "who does
  what", "how do we actually do this"), OR when a loose, months-long idea
  arrives with no clear path ("we should overhaul X", "figure out how to
  enter Y", "no idea where to start"). Do NOT use to scope a single up-front
  task (jail-task-contract) or to coordinate a multi-agent run
  (jail-orchestrate).
---

# JAIL-PLAN

Planning turns intent into something a named human can execute. Two lanes,
declared up front: **OPERATE** (a decision → a runnable process) and **MAP**
(a foggy destination → a path of decisions). [Constitution Rules 6, 7]

## Lane pick (say which)
- **OPERATE** — the path is known; the job is to make it runnable and owned.
  Downstream of jail-decide, or "turn this into a process."
- **MAP** — the destination is describable but the *way* isn't, and the work
  spans many sessions. Charging at execution would build the wrong thing.
- Big efforts often need both: MAP first to clear the fog, then OPERATE each
  cleared path into a workflow.

## OPERATE lane — the 13-field workflow spec
Every field, every workflow; "n/a" must be earned.
1. **Trigger** — the observable event or schedule that starts it. "Ongoing"
   is not a trigger.
2. **Inputs** — what must exist at start, and where it comes from.
3. **Actions** — numbered steps, each a verb, each small enough that "did it
   happen?" is yes/no.
4. **Tool** — the specific system/skill per step (least complex capable tool
   [Rule 11]; deterministic code beats a model where either works).
5. **Owner** — a named person or role per step. "The team" owns nothing.
6. **Approval** — which steps pause for a human, per **jail-approval-gate**
   tiers; irreversible/external/durable steps default to per-action [Rule 5].
   Fail-closed: any step tagged irreversible / spend / external left without
   a resolved approval tier blocks the plan from shipping — resolve via
   jail-approval-gate before delivering the spec (unavailable: state the
   tier and get an explicit human approval in-line).
7. **Output** — the artifact each cycle produces, by name and location.
8. **Evidence** — what proves a cycle ran (log, file, record); completion
   claims need artifacts.
9. **Metric** — the number that says it's working, with baseline + direction
   of good.
10. **Frequency** — cadence or SLA.
11. **Risk** — top failure modes + what the runner does on failure (retry /
    stop / escalate to whom) [Rule 6].
12. **Next action** — the single first step that starts adoption, owner + date.
13. **Completion standard** — the testable check that one cycle is done-done
    [Rule 7]; if finite, what retires it.

Method: start from the decision + its evidence (a jail-decide package). If
still contested, route to **jail-red-team** first — operationalizing a bad
idea just industrializes it. Draft the 13 fields, then walk the workflow as
its owner on a bad day (missing input, tool down, approver away) and patch
what breaks. Right-size ceremony: 13 fields compress, they don't inflate.

## MAP lane — the decision-ticket map
1. **Name the destination.** What exists when the fog clears — a spec, a
   locked decision set, a migration, a launch plan; if it can't be named
   even loosely, test the *idea* first (jail-red-team / jail-prompt) rather
   than mapping it.
2. **Chart the map** — one index artifact (a tracker issue, else a
   `PLAN-MAP-<topic>.md`) that lists decisions-made, points at the tickets
   holding their reasoning, and declares the blocking edges between them.
3. **Resolve tickets, one at a time** — work the highest-leverage unblocked
   ticket with the right skill (jail-research, jail-prototype, jail-decide,
   jail-council); record decision · why · evidence on the ticket and update
   the map index [Rule 4].
4. **Declare the way clear** — done when nothing decision-shaped remains,
   every leftover is executable [Rule 7]; hand off the destination artifact
   + the map into jail-task-contract / jail-orchestrate.

Full detail (index-vs-store, ticket-resolution protocol, map as the
handoff's spine): `references/jail-plan-map.md`.

**Success test:** OPERATE ships only if all 13 fields are filled or an n/a
is justified and field 6 is resolved per step; MAP ships only if the
destination is named, no ticket is task-shaped, and every ticket carries
edges + status.

## Output
OPERATE → the filled 13-field spec (table or labeled list). MAP → the map
index (destination · tickets with edges/status · decisions-so-far) + the
cleared-way handoff. Then the JAIL-HANDOFF block — `next:` **jail-verify**
(OPERATE readiness: owners real? permissions exist? metric measurable
today?) or **jail-lab** (drive the metric); MAP hands to
jail-task-contract / jail-orchestrate for execution.

## Related skills
Choosing what to do → **jail-decide** (first). One-time task scoping →
**jail-task-contract**. Approval tiers for OPERATE's field 6 →
**jail-approval-gate**. Session continuity on MAP work → **jail-handoff**.
Decisions worth keeping → **jail-memory** (ADRs). Delegating execution →
**jail-orchestrate**. Metric-driven iteration → **jail-lab**.

## Gotchas
- **Recommendation cosplay.** Restating "you should do X" across 13 fields
  without executable detail. Field 3's yes/no test catches it.
- **Ownerless steps.** "The team" / "someone" = nobody. A name or a role with
  a person in it, per step.
- **Metric-free workflows.** No metric = no way to notice failure. If none
  exists, field 12's first action creates the baseline.
- **Charging the destination (MAP).** Building while the way is foggy makes
  confident wrong artifacts. Plan-don't-do is the default; execution is an
  explicit handoff.
- **Task-shaped tickets (MAP).** "Implement X" on the map means execution
  leaked in. Reshape as the decision it hides, or hand it off.
- **Eternal map.** Resolving tickets forever without the way clearing —
  re-test the destination; it may have changed (a new contract, Rule 4).
- **Ceremony inflation.** Both lanes compress to the work's real size; a
  weekly two-step check is two steps, not a governance framework.
