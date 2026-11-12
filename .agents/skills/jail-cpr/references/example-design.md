# Worked example — DESIGN lane (client strategy session)

**Input:** "Build the agenda for a 90-minute client strategy session with the
owner and the operations manager of a 14-person landscaping company. They need
to choose one of three CRM options (A, B, C) by the end. Meeting is
2026-12-03 at 10:00. I am the facilitator."

**Task contract (inline):** meeting = CRM selection · 90 min · participants:
owner (decider), ops manager (user of the tool), facilitator · outcome: one
CRM chosen and a first-30-days owner named. Assumption: the three options and
their quotes already exist.

---

# CRM Selection Session — 2026-12-03 · 10:00 · 90 minutes

**Participants:** Owner — makes the final decision · Operations Manager —
runs the tool daily, tests fit · Facilitator — keeps time, records output

**Context:** The company tracks leads in spreadsheets and has missed
follow-ups. **User-provided** (owner, intake call): three options are
shortlisted (A, B, C) and each has a written quote. **Unknown:** whether the
current lead list can be exported cleanly (resolved by pre-work item 2).

**Purpose:** To pick one CRM today, so setup can start before the spring season.

**Results (must exist by 11:30):**
- R1. One CRM (A, B, or C) is chosen, or a dated no-go is recorded. Testable: a named option appears in the decision log.
- R2. The monthly budget cap the owner accepts is written down as a number.
- R3. One named person owns the first 30 days of setup, with a start date.

**Pre-work:**
| Item | Owner | Due |
|---|---|---|
| One-page comparison of A, B, C: price, setup time, must-have features | Facilitator | 2026-12-01 |
| Export of the current lead list (test import file) | Ops Manager | 2026-12-01 |
| Owner reads the comparison and ranks the options 1-3 | Owner | 2026-12-02 |

**Required inputs:** comparison page, three quotes, ranked list from the owner.

**Agenda:**
| # | Topic | Owner | Time | Objective | Expected output | Result |
|---|---|---|---|---|---|---|
| 1 | Goal and ground rules | Facilitator | 5 min | Confirm what "decided" means today | Alignment | R1 |
| 2 | Must-have check | Ops Manager | 15 min | Test each option against the must-have list | Information | R1 |
| 3 | Cost and budget cap | Owner | 15 min | Compare total first-year cost | Decision (R2) | R2 |
| 4 | Choose the CRM | Owner | 20 min | Rank, discuss, choose | Decision (R1) | R1 |
| 5 | Setup owner and first 30 days | Ops Manager | 15 min | Name the owner and start date | Assigned action | R3 |
| 6 | Read-back of decisions and actions | Facilitator | 10 min | Confirm what was decided | Alignment | R1-R3 |
| - | Buffer | - | 10 min | Overrun room | - | - |

Time check: 5 + 15 + 15 + 20 + 15 + 10 + 10 = 90 minutes.

**Parking lot:** data migration details, staff training plan (for the next session).

**Action items (live):** action · owner · deadline (filled in during item 5).

**Follow-up:** facilitator sends the decision log and actions within 24 hours;
owner confirms by reply.

**Verify gate:** every Result is covered by at least one item: PASS. Every
item traces to a Result: PASS. Times sum to 90 including buffer: PASS. The
decision items (3, 4) have their inputs in pre-work: PASS. Owners are named
roles: PASS.

```yaml
JAIL-HANDOFF:
  skill: jail-cpr
  status: complete
  facts: ["Agenda times sum to 90 minutes including a 10-minute buffer"]
  assumptions: ["The three CRM options and written quotes already exist"]
  unknowns: ["Whether the current lead list exports cleanly (pre-work item 2)"]
  outputs: ["CRM Selection Session CPR + agenda (DOCX)"]
  evidence: ["Owner intake call - three shortlisted options - User-provided"]
  risks: ["Owner does not read the comparison before the meeting, so the decision slips"]
  confidence: medium
  next: jail-decide (build the option comparison package for pre-work)
  approval_required: ["Sending the agenda and pre-work requests to the client"]
```
