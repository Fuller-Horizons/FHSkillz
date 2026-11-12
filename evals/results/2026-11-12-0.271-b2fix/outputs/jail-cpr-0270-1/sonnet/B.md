I've built the CPR and agenda, but I haven't rendered the DOCX. The closing gate failed, and the skill says not to render until it clears. The project has no prior notes on this client or the CRM options, so nothing carried forward from memory.

## Gate failures (need from you)
1. **Participant names.** I only have "owner" and "ops manager". Agenda owners must be named people.
2. **The 3 CRM options.** I need their names, and ideally a price and a one-line description of each.
3. **Date, time and your facilitator name.**
4. **Decision criteria and budget.** If the client hasn't set these, Item 2 below has them set in the room. Say so if you'd rather get them in pre-work.
5. **Who signs off.** I've assumed the owner has final authority and the ops manager is the key input. Correct me if not.

## Draft (placeholders in [brackets])

**MEETING:** CRM selection decision · [date] · 60 min
**PARTICIPANTS:**
- [Owner], owner: final decision authority.
- [Ops manager], ops manager: day-to-day user, owns adoption.
- [You], facilitator: runs the clock and records the decision.

**CONTEXT** (to be filled with facts, labeled):
- The client is choosing among [Option A / B / C].
- [Why now: current tool or lack of one, the trigger, any deadline or contract renewal.]
- Anything not yet known gets marked "Unknown", not assumed.

**PURPOSE:** The owner and ops manager must choose one CRM together, because the owner holds budget and authority and the ops manager owns whether it gets used.

**RESULTS (by close):**
- **R1.** One of A, B or C (or an explicit "none, because…") is chosen, and the owner states it aloud.
- **R2.** Criteria and weights are agreed and written down before options are scored.
- **R3.** Each remaining risk or condition on the choice has an owner and a date.
- **R4.** Next steps through to contract signature are assigned, each with an owner and date: contract, data migration, implementation lead.

**PRE-WORK** (decisions can't be made without it):
| Item | Owner | Due |
|---|---|---|
| One-page comparison of A/B/C: cost (year 1 and 3), features against need, migration effort, risks | [You] | [2 business days before] |
| Ops manager's must-have and nice-to-have list (10 minutes) | [Ops manager] | [2 days before] |
| Owner's budget ceiling and go-live deadline | [Owner] | [2 days before] |
| Recommendation (ideally a jail-decide package) | [You] | [1 day before] |

**AGENDA (60 min = 55 allocated + 5 buffer):**
| # | Topic | Owner | Time | Objective | Expected output | → Result |
|---|---|---|---|---|---|---|
| 1 | Frame and confirm the decision | [You] | 5 | Confirm the purpose, the decision rule, and that the owner decides today | Alignment | R1 |
| 2 | Lock criteria and weights | [You], with [Ops manager] and [Owner] | 10 | Agree must-haves, budget cap and weights before looking at options | Decision (criteria) | R2 |
| 3 | Score the options against the criteria | [You] | 15 | Walk A/B/C through the criteria and eliminate any that fail a must-have | Alignment (shortlist) | R1 |
| 4 | Ops manager reality check | [Ops manager] | 10 | Test the finalists on adoption, workflow fit and migration pain | Information | R1, R3 |
| 5 | **Decide** | [Owner] | 10 | State the choice, name conditions and dissent, and accept or reject the recommendation | **Decision** | R1, R3 |
| 6 | Assign next steps | [You] | 5 | Assign actions, owners and dates | Assigned actions | R3, R4 |
| – | Buffer | – | 5 | – | – | – |

**PARKING LOT:** Anything off-topic, such as integrations beyond the three options, or pricing negotiation tactics.

**ACTION ITEMS (live):** action · owner · deadline, filled in Item 6.

**FOLLOW-UP:** [You] send the decision record and action list within 24 hours of the meeting, and track the actions weekly until the contract is signed.

**Fallback rule:** If the owner can't decide by minute 50, Item 5 ends in a named decision date and the one missing input, not an open-ended "let's think about it".

Send me the names, the three options and the date, and I'll re-run the gate and produce the DOCX.

```
JAIL-HANDOFF
skill: jail-cpr (DESIGN)
status: DRAFT, gate FAILED (unnamed owners, undefined options, no date)
blocking: participant names; options A/B/C; date; facilitator
next: re-verify, then render DOCX
```