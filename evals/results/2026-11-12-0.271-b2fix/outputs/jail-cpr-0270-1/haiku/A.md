# DESIGN: CRM decision meeting (60 min)

**Gate check:** All items below trace to a Result, have a named expected output, and fit the 60-minute window (sum shown in the Agenda section). The three CRM options, client name, meeting date, and participant names were not provided, so they are marked as placeholders.

## MEETING
- **Title:** CRM selection: choose one of three options and set the first step
- **Date:** [Unknown: set when booked]
- **Duration:** 60 min

## PARTICIPANTS
- [Owner name]: Client owner, decision-maker
- [Ops manager name]: Client ops manager, runs rollout
- [SRG facilitator]: Signal Results Group, runs the meeting and writes the decision memo

## CONTEXT
- The client must choose one of three CRM options. **User-provided:** the owner and ops manager are the two people who must agree.
- **Unknown:** the decision deadline, budget ceiling, and current CRM/data state. These are needed in pre-work (see below).

## PURPOSE
Leave the room with one CRM option chosen (or all three ruled out with reasons), a locked set of decision criteria, and a named owner and date for the first step.

## RESULTS
- **R1:** One CRM option is selected by the owner, or all three are ruled out with a stated reason. *Test: the option name or the rule-out reasons are written in the decision memo.*
- **R2:** Decision criteria and weights are agreed before options are scored. *Test: a list of 5–6 criteria with weights totaling 100% exists in the memo.*
- **R3:** A named owner and a calendar date exist for the first step (contract signature or pilot start). *Test: name and date appear in the memo.*
- **R4:** A named owner and due date exist for data migration prep (contact and pipeline export). *Test: name and date appear in the memo.*
- **R5:** Every parked item has a named owner and a resolution date. *Test: parking lot table is complete.*

## PRE-WORK
| Item | Owner | Due |
|---|---|---|
| One-page summary of each of the 3 options: price, implementation time, integrations, migration effort, support model | SRG | 48 h before meeting |
| Draft criteria list with suggested weights (for the owner to edit, not finalize) | SRG | 48 h before meeting |
| Inventory of current data (contacts, pipeline, record count) and the 5 must-have workflows | Ops manager | 48 h before meeting |
| Budget ceiling and decision deadline | Owner | 48 h before meeting |

**REQUIRED INPUTS (for R1):** budget ceiling and decision deadline. **Without them, the decision cannot be made in the room.** If they are not received 48 h out, the meeting is postponed or converted to a criteria-only session.

## AGENDA
| # | Topic | Owner | Time | Objective | Expected output → Result |
|---|---|---|---|---|---|
| 1 | Open: confirm the decision, deadline, and what "done" means | SRG | 0–4 min | Agree the one decision in scope | Alignment → R1 |
| 2 | Lock criteria and weights from the pre-work draft | Owner | 4–12 min | Finalize 5–6 criteria and weights; no option discussion yet | Decision → R2 |
| 3 | Score the 3 options against the locked criteria; flag any must-have failures as knockouts | SRG | 12–24 min | Produce a scored comparison; remove any option that fails a must-have | Information → R1 |
| 4 | Ops feasibility: test the top scorers against the 5 must-have workflows and migration effort | Ops manager | 24–32 min | Confirm or reject the top option on operational fit | Information → R1, R4 |
| 5 | Decision | Owner | 32–44 min | Choose one option, or rule out all three with reasons | Decision → R1 |
| 6 | Assign first steps: contract/pilot date, migration prep owner and date | Ops manager | 44–54 min | Named owner and date for each step | Assigned action → R3, R4 |
| 7 | Close: read back the decision, owners, dates; log parking lot | SRG | 54–56 min | Confirm all Results are captured | Alignment → R5 |
| — | Buffer | — | 56–60 min | Absorbs overruns | — |

**Time check:** 4 + 8 + 12 + 8 + 12 + 10 + 2 = 56 min of agenda + 4 min buffer = **60 of 60**.

**Decision gate (minute 44):** If no option is chosen at item 5, the owner picks the top weighted score that passes all must-haves, or sets a single decision date no more than 48 h out. Either outcome is recorded before moving to item 6.

## PARKING LOT
Pricing renegotiation, training schedule, and user license count. Each gets an owner and resolution date (R5). Target: resolved by email within 3 business days.

## ACTION ITEMS
| Action | Owner | Due |
|---|---|---|
| Send decision memo (decision, criteria, scores, owners, dates) | SRG | 24 h after meeting |
| Complete first step (contract or pilot setup) | [Named in item 6] | [Named in item 6] |
| Complete data migration prep | [Named in item 6] | [Named in item 6] |
| Resolve each parking-lot item | [Named in meeting] | 3 business days |

## FOLLOW-UP
- Decision memo to both attendees within 24 h.
- Check-in on the first step at the date set in item 6.

## Labels
- **User-provided:** the meeting is for the owner and ops manager to choose among three CRM options and decide by the end.
- **Unknown:** the three option names, client name, meeting date, budget ceiling, decision deadline, current data volume, names of attendees.
- **Judgment:** the 60-minute split. Scoring and feasibility are given the most time because they are where a wrong choice is most costly.

## Open items before this is final
1. Names of the three CRM options and the client.
2. Meeting date and attendee names.
3. Budget ceiling and decision deadline.
4. Whether you want this as a DOCX for the client. I can render it on request.

```
JAIL-HANDOFF:
  skill: jail-cpr
  status: partial
  facts: ["60-min DESIGN meeting; participants: owner + ops manager; decision: choose 1 of 3 CRM options"]
  assumptions: ["SRG facilitates", "criteria are locked before scoring", "owner has authority to decide in the room"]
  unknowns: ["CRM option names", "client name", "meeting date", "attendee names", "budget ceiling", "decision deadline"]
  outputs: ["DESIGN CPR with R1–R5, pre-work, 7-item agenda (60 of 60), parking lot, action items"]
  evidence: ["Project search: no CRM-specific client doc found in project; prompt library and workbook comparison used only as background"]
  risks: ["Decision cannot close without budget ceiling and deadline in pre-work", "Criteria drafted by SRG may be seen as steering; owner must edit"]
  confidence: medium
  next: "Fill placeholders, then render DOCX (docx skill) if the client copy is needed"
  approval_required: ["Sending the agenda and pre-work requests to the client"]
```