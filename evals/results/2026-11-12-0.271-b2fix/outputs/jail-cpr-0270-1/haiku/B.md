# CPR Agenda: CRM Selection Decision (60 min, Client Owner + Ops Manager)

**Status: draft with open inputs.** The client name, the three CRM options, the meeting date, and the owner and ops manager names are not in the request. I used bracketed placeholders and flagged them in the verify check below. I searched the project for prior CRM or client notes and found nothing that applies, so there was no carry-forward.

## MEETING
**Title:** CRM selection: decide which of three options to adopt
**Date / duration:** [date] · 60 min
**Participants:**
- [Owner name] (Client owner): decision-maker, signs the choice
- [Ops manager name] (Operations manager): runs day-to-day use of the CRM and owns the data
- [Your name] (Facilitator): runs the clock, scores options live, records the decision

## CONTEXT
The client has to pick one of three CRM options. Each option has a different cost, integration effort, and learning curve. The team's current process is not documented, so the choice is being made on fit and risk, not preference. Both participants must walk in having read the option scorecard (pre-work) so the time is spent deciding, not learning the options.

## PURPOSE
Leave the room with one CRM option selected, or an explicit no-go with a named next step. Either outcome is a decision. Discussion without a decision is not a purpose for this meeting.

## RESULTS (by close)
- **R1:** One of the three options is chosen by the owner, or an explicit no-go is recorded with its reason. Testable: the option name or "no-go" is written in the minutes.
- **R2:** The owner and ops manager agree on the must-have criteria and weights used to choose. Testable: the criteria list with weights is in the minutes and signed off.
- **R3:** A budget ceiling and go-live target date are agreed. Testable: both figures are written down.
- **R4:** The implementation lead, first data-migration step, and go-live checkpoint date are assigned. Testable: each has a named person and a date.

## PRE-WORK (due 3 business days before the meeting)
| Item | Owner | Due | Why it's needed |
|---|---|---|---|
| Three-option scorecard against draft criteria (fit, cost over 3 years, integration, mobile use, data export, support) | Facilitator | T−3 days | Decision input; avoids live research |
| Three-year total cost quotes per option (license, setup, training, integrations) | Ops manager | T−4 days | Budget ceiling (R3) needs real numbers |
| Current data inventory: what customer and job data exists and where | Ops manager | T−4 days | Migration effort is a deciding factor |
| Reference check: one user per option | Facilitator | T−3 days | Verifies vendor claims |
| Pre-brief: tell owner the decision is on the agenda and what the three options are | Facilitator | T−5 days | Avoids a decision ambush |

## REQUIRED INPUTS
- Three-option scorecard with sources
- Three-year cost quotes
- Current data inventory
- Decision package (jail-decide format) listing options, criteria, costs, risks, and recommendation

## AGENDA
| # | Topic | Owner | Time | Objective | Expected output | → Result |
|---|---|---|---|---|---|---|
| 1 | Open: state the decision and the rules | Facilitator | 3 min | Confirm the meeting ends in a decision | Alignment | R1 |
| 2 | Current pain: what breaks today and the cost of it | Ops manager | 6 min | Name the 2–3 problems the CRM must solve | Information | R2 |
| 3 | Criteria and weights: set the must-haves and budget ceiling | Owner | 8 min | Agree how options will be judged | Alignment | R2, R3 |
| 4 | Option review: score each of the three against the criteria | Facilitator (ops manager challenges) | 18 min | Confirm or correct the pre-work scores, about 6 min per option | Information | R1 |
| 5 | Decision: choose one option or record a no-go | Owner | 12 min | Make the call and record the reason | Decision | R1 |
| 6 | Implementation: who leads, first migration step, go-live checkpoint | Ops manager | 8 min | Assign the next actions | Assigned action | R3, R4 |
| 7 | Close: read back decision, actions, parking lot | Facilitator | 2 min | Confirm what was agreed | Alignment | R1–R4 |
| | **Buffer** | | **3 min** | | | |
| | **Total** | | **60 min** | | | |

Agenda sequence logic: criteria are set (item 3) before options are scored (item 4), so the owner cannot pick the option first and then reverse-engineer the criteria.

## ACTION ITEMS (live template, filled in the meeting)
| Action | Owner | Deadline |
|---|---|---|
| Implementation lead named | [to be filled in meeting] | [date] |
| First data-migration step defined | [to be filled in meeting] | [date] |
| Go-live checkpoint set | [to be filled in meeting] | [date] |

## PARKING LOT
Captured, not discussed. Examples: integrations beyond the first release, user training schedule, reporting dashboards.

## FOLLOW-UP
Facilitator sends the minutes within 24 hours, with the decision, criteria, budget ceiling, and actions. Actions are logged in the tracking system. If the decision is a no-go, the next step is a scoped request to re-evaluate.

## JAIL-VERIFY (gate result)
- **Every Result covered by an agenda item:** pass (R1 → items 1, 4, 5, 7; R2 → 2, 3; R3 → 3, 6; R4 → 6)
- **Every item traces to a Result:** pass
- **Time sums to duration:** pass (57 min + 3 min buffer = 60)
- **Decisions have inputs in pre-work:** pass (scorecard, cost quotes, data inventory)
- **Owners are named people:** **FLAG.** Owner and ops manager names are placeholders. Fill them in before the meeting. Ops manager and implementation lead are roles until named.
- **Date:** **FLAG.** The meeting date is not set, so pre-work deadlines are relative (T−3, T−4, T−5 days).

## JAIL-HANDOFF
```
lane: DESIGN
meeting: CRM selection (3 options) · 60 min
results: R1 option chosen or no-go · R2 criteria+weights · R3 budget+go-live · R4 implementation owner+date
open_inputs: client name, 3 option names, meeting date, owner name, ops manager name
verify: PASS except owner-name and date flags
next: fill the placeholders, then run jail-decide to produce the decision package (required pre-work input)
```

## Next steps
1. Send me the client name, the three CRM options, the meeting date, and the two names. I will fill in the placeholders and rerun the verify check.
2. I can render this as a DOCX file with a fillable owner and deadline column, which is the default format for this skill. I did not build the file this time because the request did not ask for one and the placeholders need filling first.
3. The three-option scorecard in pre-work can be produced with jail-decide once the options are named.