**Status: not rendered.** The closing gate failed on two checks, so I haven't produced the DOCX. Nothing in the project (searched the CRM, owner and ops-manager context) has notes on this client or the three CRM options. I'm not going to invent names or options.

**What blocks it**
1. **Owners are not named people.** I don't have the owner's or ops manager's name, or the client.
2. **Pre-work can't be pinned.** I need the three CRM options and the date, so I know what has to be in the decision package beforehand.

Send me these and I'll render the DOCX:
- Client name, meeting date and time
- Owner's and ops manager's names. Also say who facilitates (you, I assume)
- The 3 CRM options by name
- Budget ceiling and go-live deadline, if the client has stated them
- Whether a decision package or comparison already exists

**Draft CPR (structure settled, names pending)**

- **Context.** The client has to pick one of 3 CRMs. *Unknown:* the trigger and the deadline, which would resolve the "why now."
- **Purpose.** The owner and ops manager choose a CRM today because the owner holds the budget authority and the ops manager owns day-to-day adoption. *Judgment.* The "owner holds budget authority" part is an assumption.
- **Results (testable at close)**
  - **R1.** One of the 3 options, or an explicit "none yet," is recorded as the decision, with the owner named as the decider. Made or not made.
  - **R2.** The top decision criteria are written down and ranked. These cover cost, fit with ops workflows, and adoption effort.
  - **R3.** Next steps (contract, data migration owner, kickoff) each have an owner and a date.
  - **R4.** If R1 isn't met, one blocking question is recorded with an owner and a date, so the deferral has a clock.

**Agenda, built backwards from the Results**

| # | Topic | Owner | Time | Expected output | Result |
|---|---|---|---|---|---|
| 1 | Confirm criteria and the ranking | Facilitator | 5 | Alignment | R2 |
| 2 | Three options against the criteria | Facilitator | 15 | Information | R1 |
| 3 | Ops fit: workflows, adoption, migration effort | Ops manager | 10 | Information | R1, R2 |
| 4 | Cost, risk and payback | Owner | 10 | Information | R1 |
| 5 | **Decision** | Owner | 10 | Decision | R1, R4 |
| 6 | Assign actions and dates | Facilitator | 5 | Assigned actions | R3 |

**Time check:** 5+15+10+10+10+5 = 55 + 5 buffer = 60 of 60. ✔

**Pre-work (the decision can't happen without it)**
- Facilitator sends a one-page comparison of the 3 options to both attendees, due 2 business days before.
- Ops manager lists their top 5 daily workflows the CRM must support.
- Owner brings the budget ceiling.

Updates stay out of the meeting. Everything informational is pre-read.

**Gate results**
- Every Result is covered by an item. ✔
- Every item traces to a Result. ✔
- The time sum is written out. ✔
- Decision inputs are in pre-work. ✔
- Owners are named people. ✘ (names missing)

```
JAIL-HANDOFF:
  skill: jail-cpr
  status: partial
  facts: ["Meeting is 60 minutes", "Attendees: client owner + ops manager", "Goal: pick 1 of 3 CRM options by end of meeting"]
  assumptions: ["Owner is the decider", "Facilitator is the user", "Criteria are cost, ops fit, adoption effort"]
  unknowns: ["Client name", "Meeting date", "Attendee names", "The 3 CRM options", "Budget ceiling and go-live deadline", "Whether a comparison already exists"]
  outputs: ["Draft CPR and agenda in chat (not rendered)"]
  evidence: ["Project search found no prior notes on this client or CRM decision"]
  risks: ["Decision ambush if the comparison isn't sent ahead", "Deferral if the owner isn't the real decider"]
  confidence: medium
  next: "Collect the missing inputs, then re-run jail-verify and render the DOCX. If no comparison exists, run jail-decide first."
  approval_required: ["Sending the DOCX or pre-work to the client"]
```