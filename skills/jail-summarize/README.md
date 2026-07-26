# jail-summarize

Turn technical findings or a status update into a short brief a busy executive can act on.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.3.1.

## What it does

You give it raw material: research, findings, a project update, technical detail. It turns that into a short brief built to force a decision. The brief leads with the answer. It labels facts and analysis separately, so no guess passes as a fact. It also turns tech and compliance details into plain business terms: cost, risk, timing. The reader never has to decode jargon. It always ends with one clear recommendation and next actions.

## Use it when

- "Summarize this for the board" or "make this exec-ready"
- You have a technical finding and need the business version of it
- You need a decision memo that ends with a clear ask, not just an update

## Don't use it for

- Raw research notes with no executive reader yet — use [`jail-research`](../jail-research/) instead.
- Full decision analysis with weighed options — use [`jail-decide`](../jail-decide/); this skill presents its output.
- A plain recap of a meeting or thread — use [`jail-cpr`](../jail-cpr/)'s debrief, or just summarize it directly.

## What you get

A short brief that opens with the outcome. It also gives the key facts and risks (each labeled), priced options, one recommendation, and next actions with an owner and a date.

## Example

**You ask:**

> Summarize this for our VP of Customer Success. We're moving customer support off an old on-prem system (HelpDeskOS, running an unsupported OS) onto a cloud platform (ServiceHub). Tests show 99.2% of tickets map over cleanly; the rest need manual fixes. Cost goes up about $975 a month, but we skip an $85,000 hardware refresh. The old system already had a 14-hour outage in March. Engineering wants to migrate this quarter, with a pilot first.

**It produces:**

```
Audience calibration: **Operating exec** (VP, Customer Success) — brief + appendix, business-first, operator detail held in the appendix.

# Migrate Off HelpDeskOS This Quarter — Brief for VP, Customer Success

## Outcome
Migrate customer support off HelpDeskOS onto ServiceHub this quarter. The system we run support on today is already failing under normal load, and the next failure could take support down company-wide with no vendor fix available.

...

## Recommendation
Go with Option 1 — a two-week pilot on the East team, then a full rollout across the rest of the quarter. It is the only option that tests ServiceHub against real traffic before our highest-value accounts depend on it, and it avoids a redundant $85,000 infrastructure spend next quarter. Confidence: high. The cost of the status quo is already showing up as repeated server crashes; the pilot structure caps the downside of the new system.

## Immediate next actions
- Engineering starts Enterprise custom-field reconciliation this week; target completion before the pilot ends. Owner: Engineering lead. Due: 2 weeks from kickoff.
- Customer Success confirms the East team pilot group and briefs those 12 agents on the change. Owner: VP, Customer Success. Due: end of this week.
- Finance clears the $975/month recurring line and confirms the $85,000 server refresh comes off next quarter's budget. Owner: Finance, with VP Customer Success. Due: before pilot start.
- Legal checks whether any of the 340 Enterprise accounts have field-level contract terms that need review before company-wide rollout. Owner: Legal. Due: before company-wide rollout begins.

**Decision needed by end of this week** so the pilot can start on schedule. Every week of delay is another week on servers already failing roughly once every three weeks.
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
