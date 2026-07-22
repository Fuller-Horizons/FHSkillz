---
name: jail-wayfind
metadata:
  version: 1.0.0
description: >-
  Navigate work too big and too foggy for one session by building a MAP of
  DECISION TICKETS — questions whose resolution is a decision, not build
  tasks — and resolving them one at a time until the way to a named
  destination is clear. Use when a loose big idea arrives ("we should
  overhaul X", "figure out how to enter Y") where the path is genuinely
  unknown, work will span many sessions, and charging at execution would
  build the wrong thing. Do NOT use for scoped single tasks
  (jail-task-contract), executable parallel work (jail-orchestrate), or a
  single researchable question (jail-research).
---

# JAIL-WAYFIND

Fog work: the destination is describable but the way isn't. Wayfinding
charts the way — it does not charge at the destination. Adapted from Matt
Pocock's `wayfinder` ([mattpocock/skills](https://github.com/mattpocock/skills),
MIT), generalized past issue trackers and bound to JAIL rules.

## Step 1 — Name the destination
First act, shapes every ticket: what exists when the fog is gone? A spec
ready to execute · a locked decision · a completed migration · a launch
plan. If the destination can't be named even loosely, this is jail-red-team
or jail-prompt territory (the idea itself needs testing), not wayfinding.

## Step 2 — Chart the map
The **map** is one index artifact — an issue labeled for wayfinding where a
tracker exists, otherwise a `WAYFIND-<topic>.md` file in the workspace.
Rules:
- The map is an **index, not a store**: it lists decisions-made and points
  at the tickets that hold their reasoning. Detail lives in tickets.
- **Tickets are decisions, not tasks.** Each ticket is a question whose
  resolution is a *decision* ("Which data model survives multi-tenant?"),
  never a build slice ("implement the schema"). The pull to just build is
  the signal you've reached the map's edge — hand off to execution
  (jail-task-contract → build, or jail-orchestrate) instead of smuggling
  it into the map.
- **Blocking edges declared**: which decisions depend on which. Unblocked
  tickets are workable now.
- **Refer by name.** Humans read names, not id soup — every ticket has a
  title used in all narration; ids/links ride inside the name.

## Step 3 — Resolve tickets, one at a time
Work the highest-leverage unblocked ticket:
- Resolve with the right kernel skill: **jail-research** (evidence),
  **jail-prototype** (build-to-learn), **jail-decide** (the decision
  itself), **jail-council** (contested + must-be-right).
- Record on the ticket: the decision · the why · the evidence pointer.
  Update the map's decisions-so-far index (one line each).
- New fog discovered = new tickets with their edges — the map grows
  honestly rather than the work drifting silently [Constitution Rule 4].
- Each session ends with the map current and a **jail-baton** if the next
  session is far away.

## Step 4 — Declare the way clear
The map is done when nothing decision-shaped remains between here and the
destination — every remaining item is executable. Close by handing off:
the destination artifact (spec/plan/decision set) + the map as its
reasoning trail, into jail-task-contract / jail-orchestrate for execution.
A map that never closes is a planning habit, not a discipline — the
destination test (Step 1) is the completion standard [Rule 7].

## Related skills
Scoped task now → **jail-task-contract**. Parallel execution →
**jail-orchestrate**. One question → **jail-research**. Session
continuity → **jail-baton**. Decisions worth keeping forever →
**jail-memory** (ADR entries).

## Gotchas
- **Charging the destination.** Building while the way is foggy produces
  confident wrong artifacts. Plan-don't-do is the default; execution
  needs an explicit handoff.
- **Task-shaped tickets.** "Implement X" on the map means execution
  leaked in. Reshape as the decision it hides, or hand it off.
- **Map as junk drawer.** Detail hoarded in the map index makes it
  illegible. Index points; tickets hold.
- **Id soup.** Narration by number instead of name. Names, always.
- **Eternal map.** Resolving tickets forever without the way clearing —
  re-test the destination; it may have changed (that's a new contract,
  Rule 4).
