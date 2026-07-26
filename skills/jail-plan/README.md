# jail-plan

It turns a decision into a workflow someone can run, or maps a path through work that has no clear plan yet.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.1.0.

## What it does

This skill has two lanes. **OPERATE** turns a decision you already made into a runnable workflow. It says who does each step, which tool they use, and how you'll know it worked. **MAP** solves a different problem. The goal is clear, but the path there is not, and the work spans many sessions. It builds a map of the open decisions and works through them one at a time. Most people start with OPERATE, since the path is usually already known. Reach for MAP when a job feels too big and too foggy to plan in one sitting.

## Use it when

- You have a decision and need to turn it into a real process ("make this operational", "who does what")
- A plan stalls at "you should..." and someone has to actually run it
- A big idea has no clear starting point ("we should overhaul X", "no idea where to start") — that's MAP

## Don't use it for

- Scoping one task up front — use [`jail-task-contract`](../jail-task-contract/) instead.
- Coordinating several agents on a run — use [`jail-orchestrate`](../jail-orchestrate/) instead.
- Making the decision itself — use [`jail-decide`](../jail-decide/) first, then bring the result here.

## What you get

OPERATE gives you a 13-field spec: trigger, inputs, actions, tool, owner, approval, output, evidence, metric, frequency, risk, next action, and a testable completion line. MAP gives you a map of decision tickets instead. Each ticket is an open question, and the map shows how they block each other.

## Example

**You ask:**

> We just got a decision back: go proactive on at-risk accounts instead of waiting for a cancellation notice. Turn that into a process my CS team can run every week. We use ChurnZero for usage alerts and HubSpot for outreach. My CS lead is Priya Nair. I'm Sam Diaz, VP of Customer Success, and I sign off on any account credit myself.

**It produces:**

```
Gate check: all 13 fields filled or justified PASS · field 6 resolved per step (2 items sent for explicit approval, marked pending below) PASS · every action step is a yes/no-checkable verb PASS

OPERATING WORKFLOW: At-Risk Account Proactive Outreach — Fernbank Metrics CS team

Upstream decision: 2026-07-14 jail-decide package — "Launch proactive at-risk-account outreach instead of waiting for cancellation notices." Recommendation: proactive outreach, confidence high, not contested — jail-red-team not invoked.

1. **Trigger** — ChurnZero fires a "usage-drop" alert when a paying account's weekly active-seat usage falls 40% or more week-over-week for two consecutive weeks (two weeks, not one, to filter out single bad weeks from holidays or vacations).

2. **Inputs** — (a) the ChurnZero alert: account name, usage trend chart, current ARR; (b) the account's CS history in HubSpot (last touch, open tickets, renewal date); (c) the assigned CSM's current queue depth (HubSpot task list) to route review to whoever has capacity.

3. **Actions**
   1. The CSM assigned to the account opens the ChurnZero alert and confirms the drop is real usage (not a known outage, a billing pause, or a seasonal account) within 1 business day of the alert firing.
   2. If confirmed, the CSM logs an "At-Risk Outreach" task in HubSpot and sends a personalized check-in (email or call, CSM's judgment) within 2 business days of the alert.
   3. The CSM logs the customer's response and next step in HubSpot: resolved / needs a save offer / no response yet / escalate.
   4. If a save requires an account credit or discount, the CSM drafts the credit amount and reason in HubSpot before applying anything.
   5. Priya Nair (CS lead) reviews every open "At-Risk Outreach" task older than 5 business days each Monday and reassigns or escalates stalled ones.
   6. Priya reports the week's flagged-account count, outcomes, and any pending credit approvals to Sam Diaz at the Monday CS metrics meeting.

...

6. **Approval** — tiered per jail-approval-gate (the gate skill was not separately invoked this run; tiers are stated here and approvals requested inline, per the fail-closed fallback):
   - Steps 1-3 (review alert, send check-in, log outcome): reversible, matches an existing CS motion, homogeneous across accounts → tier **BATCHABLE**, approved as a pattern via the request below.
   - Step 4 (any account credit or discount): spend → tier **PER-ACTION**, no threshold exception under jail-approval-gate. Every credit needs Sam Diaz's sign-off before it is applied, regardless of size.
   - Steps 5-6 (internal review, internal reporting): reversible and workspace-internal → tier **AUTO**.
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
