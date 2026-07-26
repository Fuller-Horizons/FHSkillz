# jail-handoff

It writes a baton — a short handoff note — so you or another agent can pick up your work later.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.3.0.

## What it does

A baton is a short handoff file. It holds only what a fresh session needs to keep going. That means the goal, what's done, what's next, and why you made each choice. It never copies a spec or a log into itself — it points to them instead. That keeps the baton small. It also keeps one source of truth.

## Use it when

- your context is filling up and you want to save your place before it fades
- you're ending a session mid-project and want to pick it up tomorrow
- you say "hand this off," "save where we are," or "continue this later"
- the work needs to move to another agent or a smaller model

## Don't use it for

- the in-run handoff between skills — use the JAIL-HANDOFF block in the [constitution](../../docs/JAIL-CONSTITUTION.md) instead
- durable lessons you want to keep for good — use [`jail-memory`](../jail-memory/) instead
- resuming a multi-agent run — use [`jail-orchestrate`](../jail-orchestrate/)'s ledger instead; the baton just points at it

## What you get

You get a markdown file with eight short parts. It covers the goal, what's done, what's next, decisions with reasons, live gotchas, and any pending approvals.

## Example

**You ask:**

> Write the baton for the intake-bot project so I can pick this up tomorrow.

**It produces:**

```
Baton written. Running the pre-emit gate first: all 8 parts below carry real content or an explicit N/A — none silently blank. Gate passes.

# Baton — Brightleaf Dental intake-bot (2026-07-24, end of session)

1. **Objective + contract state** — Build an intake chatbot for Brightleaf
   Dental Group that collects a new patient's demographics and insurance
   info before their first visit, verifies insurance eligibility through
   the Availity API, and hands the verified record to Brightleaf's PMS
   (Dentrix Ascend) via a nightly CSV import. Contract:
   `docs/brightleaf-intake-contract.md` v1. "Done" = the bot completes
   intake for a new patient end to end, the verified insurance status is
   stored, and one full nightly Dentrix import runs clean with no manual
   correction.
...
8. **Approval state** — Dr. Osei (practice owner) approved the Availity
   integration and its per-query cost in the June 30 kickoff email —
   that's covered. Denise's text-confirmation request is NOT yet
   approved for this phase of scope; it is flagged for Dr. Osei, not
   started, and not assumed.
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
