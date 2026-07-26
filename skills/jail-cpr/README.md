# jail-cpr

This skill turns a meeting idea into an agenda that must produce something, or a transcript into a scored record of what actually got decided.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.4.0.

## What it does

CPR stands for Context, Purpose, Results. You give the skill a meeting's basics — who, when, why — and it writes the Results first: the exact decisions or outputs that must exist by the end. Then it builds the agenda backward from those Results, so every item has an owner, a time slot, and a stated output. A closing check blocks the agenda from shipping if any item does not trace back to a Result. After the meeting, the same skill can run in reverse: it reads notes or a transcript and pulls out what was decided, who owns what, and how the results measured up.

## Use it when

- "Build an agenda for Thursday's roadmap meeting"
- "We keep having status-update meetings that decide nothing — fix that"
- "Pull the decisions and action items out of this meeting transcript"
- "Score this meeting against what we said we'd get done"

## Don't use it for

- Planning project work with no meeting attached — use [`jail-task-contract`](../jail-task-contract/) instead.
- Writing the pre-read material for a meeting topic — use [`jail-summarize`](../jail-summarize/); jail-cpr builds the agenda around it.

## What you get

A Context/Purpose/Results block, a time-boxed agenda where each item names its owner and expected output, a pre-work list, and an action-items table. The finished document ships as a Word file by default, a PDF on request, or clean Markdown when no document tool is available.

## Example

**You ask:**

> We've got our Q3 roadmap prioritization meeting for Beacon Insights this Thursday, 3:00-3:45pm ET (45 min). Attendees: me (Jonathan, Product Lead), Maria (Design Lead), Sam (Eng Lead), Priya (Customer Success Lead). Engineering capacity only supports building 2 of our 3 scoped Q3 candidates. We also still have the international pricing tiers question parked from two weeks ago. Sam's worried we're going to burn the whole 45 minutes on status updates again instead of deciding anything. Can you build the agenda?

**It produces:**

```
### RESULTS (by close)
- **R1** — 2 of 3 candidates (scheduled exports, Slack alerts, multi-currency reporting) are selected for the Q3 slate; the third is explicitly deferred with a stated reason.
- **R2** — Each of the 2 selected features has a named owner and a due date for the spec draft.
- **R3** — International pricing tiers is either scheduled onto a specific future date or explicitly killed — not silently re-parked.

...

### AGENDA
| # | Topic | Owner | Time | Objective | Expected output | → Result |
|---|---|---|---|---|---|---|
| 1 | Confirm scoring rubric, flag disagreement | Jonathan | 5 min | Everyone read the pre-work and agrees how we score | Alignment | R1 |
| 2 | Score & down-select: 2 of 3 features | Jonathan facilitates, group decides | 20 min | Use rubric + estimates to cut one candidate | Decision | R1 |
| 3 | Assign spec owners for the 2 selected features | Jonathan | 8 min | Name who drafts each spec and by when | Assigned action | R2 |
| 4 | International pricing tiers: schedule or kill | Priya | 5 min | Resolve the carryover — no re-parking without a reason | Decision | R3 |
| — | Buffer | — | 7 min | — | — | — |

**Time check:** 5 + 20 + 8 + 5 = 38 min agenda + 7 min buffer = **45 min** — matches the meeting duration.

...

**VERDICT: PASS — render the document.**
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
