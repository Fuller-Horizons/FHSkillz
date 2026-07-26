# jail-lab

Run disciplined, measured experiments on anything you're trying to improve, and keep a record of what actually worked.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.1.0.

## What it does

You give it one metric and a budget before you start. It runs one change at a time and measures the result. Each try gets compared to your best result so far — keep it, or throw it away. Every try goes into a ledger (a running log you never edit by hand), so failed tries count as evidence too, not wasted effort. If you have Python, the companion skill [`jail-py-lab`](../jail-py-lab/) can keep that ledger for you. This skill works fine by hand as well.

## Use it when

- "I want to iterate on this until it's actually better, not just different."
- "Help me A/B test this prompt, email, or landing page instead of guessing."
- "I keep changing things and can't remember what I already tried and ruled out."

## Don't use it for

- A gut-feel quality check with no hard number behind it — use [`jail-rate`](../jail-rate/) instead.
- A single before/after check that doesn't need an ongoing ledger — use [`jail-verify`](../jail-verify/).
- Deciding what the metric or workflow should even be — [`jail-plan`](../jail-plan/) sets that up first.

## What you get

A declared lab (one metric, a baseline, a budget, a stop point) and a ledger that logs every try with its result and a keep-or-discard call. You also get a clear read on what to test next.

## Example

**You ask:**

> We send a follow-up email after every discovery call, offering our brand audit as the next step. Baseline: 22.5% reply rate (9/40). I want to test one change at a time on batches of 20, budget of 4 batches, stop at 3 discards in a row. This only touches our own CRM and real prospects — treat it as approved.
>
> Already ran: Batch 1 moved the calendar link to the first sentence (6/20). Batch 2 personalized the subject line (8/20). Batch 3 swapped the recap paragraph for 3 bullets (5/20).
>
> Set this up as a proper lab, tell me what to keep, and give me the next thing to test.

**It produces:**

```
**Step 0 — Lab declared**

- **Metric:** reply rate, % of follow-ups that get a reply — higher is better.
- **Baseline:** 22.5% (9 replies / 40 follow-ups, calls before 6/29).
- **Budget:** 4 batches of 20 follow-ups each (80 sends total), one change per batch. Same conditions every batch: single decision-maker, first-time prospects, same day-of-week send window.
- **Blast radius:** real prospects, real CRM — no jail-approval-gate installed. Tier: PER-ACTION. You flagged this as approved inline for all 4 batches, since it's your own send list and nothing irreversible is at stake. Logged as approved.
- **Stop condition:** 4 batches exhausted, or 3 discards in a row — whichever comes first.
...
**Ledger**

| id | timestamp | change | hypothesis | metric result | verdict | evidence ref |
|----|-----------|--------|------------|---------------|---------|--------------|
| 0 | 2026-06-28 | unmodified baseline template | — | 22.5% (9/40) | BASELINE | CRM reply log, calls before 6/29 |
| 1 | 2026-07-06 | calendar link moved to first sentence | less scrolling before the ask → more clicks | 30.0% (6/20) | KEEP | CRM reply log, batch 1 (wk of 6/29) |
| 2 | 2026-07-13 | personalized subject line: "{Company} — quick audit idea" | personalized subject gets opened → opened gets replied | 40.0% (8/20) | KEEP | CRM reply log, batch 2 (wk of 7/6) |
| 3 | 2026-07-20 | 3-bullet call recap instead of one paragraph | bullets are easier to scan, prove we listened | 25.0% (5/20) | DISCARD | CRM reply log, batch 3 (wk of 7/13) |

**Self-check:** 4 ledger rows = 4 experiments run (baseline + 3). Best-so-far = row #2 at 40.0% — the current template is baseline + #1 + #2, with #3 reverted out.

**Stop condition check:** not met. 1 of 4 budget batches remain; consecutive discards = 1 (threshold 3). Lab stays open — one more experiment to run.
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
