The project has no client file for this check-in: no retainer terms, prior commitments, or last quarter's scorecard. So I'm building the agenda from the meeting brief, with placeholders where those facts go.

# DESIGN: Quarterly check-in (draft, 45 min)

**MEETING:** Quarterly check-in with client owner and CFO · Date: [TBD] · Duration: 45 min

**PARTICIPANTS**
- [Owner name], client owner: decides priorities and retainer
- [CFO name], client CFO: owns financial inputs and retainer cost terms
- Jonathan Fuller, consultant: facilitates, presents results and options

**CONTEXT**
- **Fact (User-provided):** The quarter is closing and the retainer is up for an extension decision.
- **Fact (User-provided):** Two decisions are needed: top 3 priorities for next quarter, and whether to extend the retainer.
- **Unknown:** Current retainer terms, fee, end date, and last quarter's targets and results. Nothing in the project file covers this client yet.

**PURPOSE:** Agree next quarter's top 3 priorities and decide whether to extend the retainer.
*Check: this is two decisions, not an update, so a meeting is justified. Any status update goes in the pre-read.*

**RESULTS (each testable at close)**
- **R1:** Three priorities for next quarter are named. Each has one named owner, one measurable target, and one due date.
- **R2:** The retainer decision is made: extend as-is, extend with changed scope, or end at term. If extended, the scope, term, and fee are confirmed in writing by [date].
- **R3:** Every action from the meeting has a named owner and a due date.

**PRE-WORK**

| Item | Owner | Due |
|---|---|---|
| Last quarter results vs targets (one page) | Jonathan | 2 business days before |
| Shortlist of 5–6 candidate priorities, each tied to a result | Jonathan | 3 business days before |
| Retainer options with fee and scope (extend / change / end) | Jonathan | 3 business days before |
| Confirm financial figures for the quarter | [CFO name] | 2 business days before |

*Approval needed: sending the pre-read and options to the client is outward-facing, so you confirm before it goes.*

**REQUIRED INPUTS:** client and owner/CFO names · meeting date · current retainer terms and end date · last quarter's targets and actuals · candidate priority list

**AGENDA**

| # | Topic | Owner | Time | Objective | Expected output → Result |
|---|---|---|---|---|---|
| 1 | Open: confirm the two decisions and the close time | Jonathan | 3 | Agree the agenda and that retainer is on it | Alignment → R1, R2 |
| 2 | Quarter results vs targets | [CFO name] | 7 | Establish which results the priorities must address | Information → R1 |
| 3 | Select top 3 priorities from shortlist | [Owner name] | 14 | Choose three; drop the rest to parking lot | Decision → R1 |
| 4 | Owner, target, and due date for each priority | [Owner name], [CFO name] | 8 | Make each priority testable | Assigned action → R1 |
| 5 | Retainer extension decision | [Owner name] decides; [CFO name] on cost | 8 | Decide extend / change / end, or set a dated follow-up | Decision → R2 |
| 6 | Recap actions, owners, dates | Jonathan | 3 | Confirm every action has an owner and date | Assigned action → R3 |
| — | Buffer | — | 2 | — | — |

**Time check:** 3 + 7 + 14 + 8 + 8 + 3 = 43 + 2 buffer = **45 of 45**

**PARKING LOT:** Priorities beyond the top 3 · any scope change not decided in item 5

**ACTION ITEMS:** Written to be filled in the meeting. Each needs an owner and date before close.

**FOLLOW-UP:** Written summary of decisions and actions within [24 hours]. If the retainer decision is deferred, the follow-up sets a decision date.

## Verify gate

- **FAIL (flagged):** Owners are placeholders, not named people. Fill in [Owner name] and [CFO name].
- **FAIL (flagged):** The meeting date is unknown, so the pre-work due dates are relative, not calendar dates.
- **Pass:** Every Result is covered by at least one item. Every item traces to a Result. Item times sum to 45 with the buffer shown.
- **Risk:** Item 5 gets 8 minutes for a retainer decision. If item 3 runs over, use the dated follow-up in item 5 rather than cutting it.

Send me the client and CFO names, the meeting date, your current retainer terms, and last quarter's targets and actuals. I'll fill in the placeholders, pass the gate, and produce the DOCX with a fillable owner/deadline column.

JAIL-HANDOFF:
  skill: jail-cpr
  status: partial
  facts: [Meeting is 45 min with client owner and CFO; two decisions needed: next-quarter top 3 priorities and retainer extension; no client file found in project]
  assumptions: [Jonathan facilitates; retainer is Jonathan's engagement; Results framed as decisions]
  unknowns: [client and owner/CFO names; meeting date; current retainer terms and end date; last quarter's targets and actuals; candidate priorities]
  outputs: [DESIGN draft agenda with flagged placeholders; verify gate FAIL on owner names and date, time sum passes]
  evidence: [project search for retainer/check-in returned no client-specific notes]
  risks: [retainer decision squeezed into 8 minutes; pre-read sent to client is outward-facing]
  confidence: medium
  next: fill inputs, re-run verify, render DOCX
  approval_required: [sending pre-read and retainer options to client]