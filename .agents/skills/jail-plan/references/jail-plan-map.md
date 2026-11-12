# JAIL-PLAN — MAP lane, full detail

Elaboration on the MAP lane's four steps in `SKILL.md`. Open this when the
inline one-line statement isn't enough to act on.

## 2. Chart the map
- **Index, not a store**: lists decisions-made and points at the tickets
  holding their reasoning. Detail lives in tickets.
- **Tickets are decisions, not tasks** — each is a question whose
  resolution is a *decision* ("Which data model survives multi-tenant?"),
  never a build slice. The pull to just build = you've hit the map's edge:
  hand off to execution (jail-task-contract → build, or jail-orchestrate),
  don't smuggle it into the map.
- **Blocking edges declared** — which decisions depend on which; unblocked
  tickets are workable now.
- **Refer by name**, not id soup — every ticket has a title used in all
  narration.

## 3. Resolve tickets, one at a time
Work the highest-leverage unblocked ticket with the right skill:
**jail-research** (evidence), **jail-prototype** (build-to-learn),
**jail-decide** (the decision), **jail-council** (contested +
must-be-right). Record on the ticket: decision · why · evidence pointer;
update the map index. New fog = new tickets with their edges — the map
grows honestly rather than the work drifting silently [Rule 4].

- **The map is the handoff's spine (multi-session persistence):** each
  session ends with the map current + a **jail-handoff** whose state
  POINTS at the map (never re-describes it) and names the active ticket;
  resuming sessions open the map first. Ticket resolutions worth keeping
  land in **jail-memory** as ADR entries at resolution time.

## 4. Declare the way clear
Close by handing off the destination artifact + the map (its reasoning
trail) into jail-task-contract / jail-orchestrate. A map that never closes
is a planning habit, not a discipline — the destination test is the
completion standard [Rule 7].
