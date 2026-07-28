# jail-cpr

This skill turns a meeting idea into an agenda that must produce something, a personal or team commitment into a dated Results contract with no meeting at all, or a transcript/check-in into a scored record of what actually got decided.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.5.0.

## What it does

CPR stands for Context, Purpose, Results. Three lanes:

- **DESIGN** — give it a meeting's basics (who, when, why) and it writes the Results first: the exact decisions or outputs that must exist by the end. It then builds the agenda backward from those Results, so every item has an owner, a time slot, and a stated output. A closing check blocks the agenda from shipping if any item does not trace back to a Result.
- **COMMIT** — give it a defined period (a quarter, a fixed number of weeks) and the life/business domains it spans, with no meeting involved. It writes a Context/Purpose/Results contract where every Result is self-contained testable — a date, a number, or a cadence, checkable from the document alone, with no unprompted third-party corroboration and no vague qualifier left undefined.
- **DEBRIEF** — after the fact (a transcript, notes, or a period check-in), it pulls out what was decided, who owns what, and audits the planned Results against what actually landed.

## Use it when

- "Build an agenda for Thursday's roadmap meeting"
- "We keep having status-update meetings that decide nothing — fix that"
- "Write my commitment contract for this quarter — budget, health, the business, the relationship"
- "Pull the decisions and action items out of this meeting transcript"
- "Score this meeting — or this quarter — against what we said we'd get done"

## Don't use it for

- Generic non-CPR task scoping with no Context/Purpose/Results shape — use [`jail-task-contract`](../jail-task-contract/) instead.
- Turning an already-made decision into a runnable operating process — use [`jail-plan`](../jail-plan/)'s OPERATE lane.
- Writing the pre-read material for a meeting topic — use [`jail-summarize`](../jail-summarize/); jail-cpr builds the agenda around it.

## What you get

A Context/Purpose/Results block, a time-boxed agenda where each item names its owner and expected output, a pre-work list, and an action-items table. The finished document ships as a Word file by default, a PDF on request, or clean Markdown when no document tool is available.

## Example — DESIGN

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

## Example — COMMIT

**You ask:**

> I'm starting a 12-week personal reset on August 3. Domains: finances, health, and the business. I want to close my emergency fund gap, get back to the gym consistently, and land two new client contracts. I also promised my partner more dedicated time together, and I want to actually use a daily journaling habit instead of just meaning to. Build my COMMIT contract.

**It produces:**

```
DEADLINE: Oct 25 (started Aug 3 · 12 weeks)

CONTEXT: Personal Reset

PURPOSE: To close the gap between what I say I want and what I actually do,
by making a small number of measurable commitments and following through on
every one, so the next 12 weeks build proof instead of more intentions.

RESULTS (by close):
- R1 (Finance) — Emergency fund reaches $10,000, verified by account
  balance on Oct 25.
- R2 (Health) — Gym attended ≥3x/week for all 12 weeks, logged same-day.
- R3 (Business) — 2 new signed client contracts, dated and on file.
- R4 (Relationship) — 1 dedicated evening/week, phone away, logged
  same-day — flagged: drop "and she'd agree we've gotten closer," that's
  not a check you control; the logged-evenings count is the testable part.
- R5 (Habit) — Daily journal entry logged every day of the 12 weeks; by
  week 2, converted into a working prioritization system — flagged:
  "a system I actually use" needs its definition attached (which tool,
  reviewed when) before it counts as testable.

CHECK-IN CADENCE: Weekly, every Sunday, self-reported against R1–R5.

VERDICT: FAIL any check — R4 and R5 as drafted carry an undefined
qualifier / unverifiable corroboration. Fix inline before rendering:
- R4 → keep "logged same-day" as the sole check; drop the "she'd agree" clause.
- R5 → name the system now (which tool, reviewed on what cadence) or mark
  it Unknown and revisit at the week-2 check-in.
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
