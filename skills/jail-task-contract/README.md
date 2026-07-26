# jail-task-contract

Turn a vague request into a clear contract before work starts.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.3.0.

## What it does

You give it a request that's vague, has many threads, or carries real risk if it goes wrong. It asks a short round of questions first. It only asks about decisions only you can make. Anything it can find on its own, like files or past work, it looks up instead of asking. Then it writes a 14-field contract. The contract names the goal, who it's for, what's in and out of scope, the risks, and a completion check — a test that would fail if the work turned out bad. If the audience, the deliverable, or the money involved changes later, that's a new contract. It is not a quiet edit to the old one.

## Use it when

- You're about to start a task with more than one thread, or unclear scope
- You want to say "make sure we're aligned" before anyone starts the work
- A request keeps drifting through revision after revision, and you need to know if the goal itself changed

## Don't use it for

- Writing or fixing a prompt for an AI — use [`jail-prompt`](../jail-prompt/) instead.
- A small, one-step task that doesn't need a contract.
- Gathering the actual facts or data — that's [`jail-research`](../jail-research/), once the contract says what to look for.

## What you get

A 14-field task contract: the goal, the stakeholder, the deliverables, the risks, and a testable completion check. If the request was vague, you also get the short round of questions that resolved it.

## Example

**You ask:**

> Comet Bikes' board meeting is Thursday and Priya wants a slide on customer retention. Can you pull together what we need? We've got the Shopify export and last quarter's churn numbers somewhere. Make sure we're aligned before anyone touches customer data.

**It produces:**

```
...
SHIP-GATE: 14/14 fields filled PASS · field 13 is a FAIL-triggering check PASS · field 14 non-empty PASS

TASK CONTRACT — Comet Bikes Q2 2026 board retention slide

1. Objective — Give the board an accurate, defensible read on the retention trend so they can judge whether it needs attention — not just a slide with a number on it.
2. Stakeholder — Priya Nair (COO), approves before it enters the deck; the board, reads it Thursday to judge whether retention needs follow-up.
3. Required outcome — One board-ready slide + appendix chart showing Q2 vs. Q1 2026 churn, aggregate numbers only, sitting in the deck Priya opens Wednesday.
4. Deliverables — Board slide (matching deck template); appendix backup chart; one-line source note for Priya's own reference.
5. Constraints — Due Wed EOD (day before the Thursday meeting); match the existing deck's template/format; aggregate data only — customer names/emails are PII and may not appear on either artifact; source files stay in the access-controlled "Board-Q2-2026" drive folder.
6. Non-goals — Not a full retention/cohort study; not a recommendation on what to do about churn; not CFO-reviewed this round.
7. Inputs available — Shopify export CSV (Q1+Q2 2026) and the ops team's retention tracker spreadsheet, both in the "Board-Q2-2026" shared drive folder, access already granted.
8. Inputs missing — None blocking. Open item: confirm the tracker's churn definition (logo vs. revenue) once opened — see Assumptions.
9. Assumptions — ASSUMED: "churn" means logo churn (% of customers lost), matching how the tracker has labeled it in prior quarters. Would change if the tracker turns out to track revenue churn — the chart and caption would need to be rebuilt around dollars, not customer counts.
10. Dependencies — Priya's sign-off before the slide is inserted into the deck; continued access to the shared drive folder.
11. Material risks —
   - Wrong churn definition used → the number stated on stage is wrong, and it undermines trust in the number if questioned.
   - Quarter definition mismatch (calendar vs. trailing 12mo) → doesn't match what the board saw last time, invites confusion mid-meeting.
   - A customer name or email slips into the appendix chart → a data-handling incident in front of the board.
12. Success criteria — Priya can present the number without hedging; the appendix answers the likely "why did it move" follow-up; no individual customer is identifiable anywhere in the deck.
13. Completion criteria — FAILS if: the slide/appendix are missing from the deck Priya opens Wednesday; the churn number doesn't reconcile against a manual recompute from the two source files; or a PII scan (search both artifacts for "@" and any name-shaped text) turns up a hit. PASSES when the slide + appendix are in the deck, the number reconciles, and the PII scan is clean.
14. Approval-required actions — Priya's sign-off before the slide enters the board deck (board-facing material is durable once presented). No spend. Nothing else irreversible or external.
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
