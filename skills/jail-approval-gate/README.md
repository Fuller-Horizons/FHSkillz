# jail-approval-gate

It sorts every action in a plan into a tier, so risky moves stop for a human before your agent acts.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.2.0.

## What it does

This skill checks each action in a plan against four tiers. A never action is blocked. No one can approve it in the moment. Sending private data to an unapproved vendor is one example. A per-action item needs a yes from a human, one at a time. Sending an email blast or spending money are per-action items. A batchable item repeats the same low-risk step many times, like posting one update to four accounts you own. One approval covers the whole batch. An auto item is safe and reversible. The agent just does it. Every choice gets one line in an audit log called a GATE-RECORD. A dispute later gets settled by that log, not by memory.

## Use it when

- you're about to run an agent that will send, publish, deploy, delete, or spend money
- you ask "what will you do without asking me first?" before letting an agent run loose
- another skill handed you a plan with items marked `approval_required`

## Don't use it for

- pure analysis or drafting that never leaves your workspace — nothing here needs a gate
- deciding if data is safe to send somewhere — use [`jail-quarantine`](../jail-quarantine/) instead
- judging if a fact is worth keeping long-term — use [`jail-memory`](../jail-memory/) instead
- running the approved plan across several agents — use [`jail-orchestrate`](../jail-orchestrate/) instead

## What you get

A tier for every action, a full approval request for each risky one, and a GATE-RECORD line for every decision made. You also get a JAIL-HANDOFF block listing anything still waiting on a human.

## Example

**You ask:**

> We're launching the September newsletter today. Finish the copy, run the link checker, send it to the full Mailchimp list, cross-post to X, LinkedIn, Facebook, and Instagram, spend up to $300 boosting the LinkedIn post, push the new discount code live, hand our subscriber list to Clearbit for enrichment, and log the list-migration decision in project memory. Gate this before you touch anything.

**It produces:**

```
| # | Action | Tier | Rule matched |
|---|--------|------|---------------|
| 1 | Draft copy in shared doc | AUTO | Rule 4 — reversible, workspace-local, non-durable |
| 2 | Sandbox link-checker run | AUTO | Rule 4 — reversible, workspace-local, non-durable |
| 3 | Send newsletter via Mailchimp | PER-ACTION | Rule 2 — external communication, irreversible once delivered |
| 4 | Cross-post to 4 owned channels | BATCHABLE | Rule 3 — repeated, homogeneous, closed set of 4, same copy/asset represents the batch honestly |
| 5 | $300 LinkedIn ad boost | PER-ACTION | Rule 2 — spend |
| 6 | Pricing-page discount code live | PER-ACTION | Rule 2 — production change |
| 7 | Subscriber PII to Clearbit | NEVER | Rule 1 — protected data (name+email) to an unauthorized destination; Clearbit is not on the approved-vendor list (see jail-quarantine) |
| 8 | List-migration ADR to memory | PER-ACTION | Rule 2 — durable memory write |
...
GATE-RECORD | action=send-newsletter-mailchimp-fh-main-8400 | tier=PER-ACTION | approver=J. Fuller | ts=2026-07-24T09:52:00-05:00 | result=approved
GATE-RECORD | action=crosspost-x-linkedin-facebook-instagram-batch4 | tier=BATCHABLE | approver=J. Fuller | ts=2026-07-24T09:52:00-05:00 | result=approved
GATE-RECORD | action=linkedin-ad-boost-300 | tier=PER-ACTION | approver=J. Fuller | ts=2026-07-24T09:52:00-05:00 | result=approved-modified-to-250
GATE-RECORD | action=pricing-page-20pct-code-live | tier=PER-ACTION | approver=J. Fuller | ts=2026-07-24T09:52:00-05:00 | result=approved
GATE-RECORD | action=subscriber-pii-to-clearbit | tier=NEVER | approver=gate-policy | ts=2026-07-24T09:06:00-05:00 | result=denied
GATE-RECORD | action=memory-adr-list-migration-decision | tier=PER-ACTION | approver=none-yet | ts=2026-07-24T09:55:00-05:00 | result=pending
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
