---
name: jail-cpr
metadata:
  version: 1.1.0
description: >-
  Build a CPR (Context · Purpose · Results) and an execution-oriented meeting
  agenda where every item produces information, alignment, a decision, or an
  assigned action — never a generic sequence of updates. Use when asked to
  "build an agenda", "prep this meeting", "create a CPR", "structure this
  board/client/team session", or to turn a goal into a meeting plan. Do NOT
  use to process a meeting AFTER it happened (decisions/actions extraction),
  or for project task planning with no meeting (jail-task-contract).
---

# JAIL-CPR

Meetings exist to produce Results; the agenda is reverse-engineered from
them. CPR here means **Context · Purpose · Results** — in that order on the
page, in reverse order in the design.

## Chain
1. **jail-task-contract** — pin: meeting title, date/duration (when known),
   participants + roles, and the decision(s) or outcomes the organizer
   actually needs. *(Fallback: capture inline.)*
2. **jail-memory** — retrieve prior commitments, open action items,
   standing decisions, and last session's parking lot; carry forward what's
   still live. *(Fallback: ask for the prior notes.)*
3. **Write the CPR** (jail-exec-brief voice — lead with what matters):
   - **Context** — why this meeting is happening now and what participants
     must understand walking in. Facts labeled; no surprise framing.
   - **Purpose** — why these people, in one sentence. If the purpose is
     "update everyone," challenge it: updates are pre-work, not meetings.
   - **Results** — the specific decisions, commitments, outputs, or
     measurable outcomes that must EXIST by the end. Each result is
     testable at close: made/not made, assigned/not assigned. [Rule 7]
4. **Build the agenda from the Results, backwards.** Every agenda item
   traces to a Result and declares: topic · owner · time allocation ·
   discussion objective · **expected output** (decision | alignment |
   information | assigned action). An item with no expected output is cut
   or demoted to pre-work.
5. **jail-verify** — the closing check: every Result covered by ≥1 item;
   every item traces to a Result; time allocations sum to the duration
   (with buffer); decisions have their needed inputs in pre-work; owners
   are named people.

## Output template
```
MEETING: <title> · <date · duration> 
PARTICIPANTS: name — role (why they're needed)
CONTEXT: <the walking-in understanding>
PURPOSE: <one sentence>
RESULTS (by close):  R1… R2… (each testable)
PRE-WORK: item · owner · due (what must be read/done BEFORE)
REQUIRED INPUTS: documents/data on the table
AGENDA:
  # · topic · owner · time · objective · expected output → Result#
PARKING LOT: (captured, not discussed)
ACTION ITEMS (live template): action · owner · deadline
FOLLOW-UP: how minutes/decisions/actions get distributed + tracked
```
JAIL-HANDOFF block when feeding another skill; humans get the template only.

## Related skills
Present complex material inside the meeting → **jail-exec-brief** builds
the pre-read. Decision on the agenda → bring a **jail-decide** package as
its required input. After the meeting → actions flow into **jail-memory**
(commitments) and **jail-operationalize** (recurring processes).

## Gotchas
- **Update theater.** An agenda of round-robin updates produces nothing a
  document couldn't. Updates → pre-work; meeting time is for Results.
- **Untestable Results.** "Align on strategy" can't be checked at close.
  "Decide between options A/B and assign the owner" can.
- **Ownerless items.** Topics without a named owner drift. Every item, one
  name.
- **Time fiction.** Eight items, sixty minutes, no buffer. Verify the
  arithmetic; cut items, not corners.
- **Decision ambush.** A decision item whose inputs weren't in pre-work
  produces a deferral, not a decision. The verify step checks the pairing.
