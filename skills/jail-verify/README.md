# jail-verify

It checks finished work against what was actually asked for, using real evidence, before you ship it.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.2.0.

## What it does

You hand it a finished piece of work and the request behind it. It never trusts a claim like "tests passed" or "it's done" on its own word — it opens the real file, reruns the real math, and reads the real log. A "contract" here just means the deliverables, rules, and finish-line test you agreed on up front. The skill runs a fixed list of checks in order, then adds the passes and fails into one count. That count decides the final verdict by a fixed rule, so two people checking the same evidence land on the same answer.

## Use it when

- You say "verify this before it ships" or "is this actually done."
- Another agent, or another person, just claimed a task is finished, and you want proof, not their word for it.
- The deliverable has real stakes if it's wrong — money, a customer, a filing, a release.

## Don't use it for

- Scoring quality on a 0-10 scale — use [`jail-rate`](../jail-rate/) instead.
- Rating a skill or prompt library itself — use [`jail-rate-skill`](../jail-rate-skill/) instead.
- Attacking a plan's reasoning before anything is built — use [`jail-red-team`](../jail-red-team/) instead.

## What you get

One verdict — PASS, FAIL, or PASS-WITH-FLAGS — with the count of checks behind it, the specific failures ranked by importance, any flags that don't block shipping, and a handoff block for whatever runs next.

## Example

**You ask:**

> I finished reconciling June's vendor invoices. Can you verify this is ready to send to accounting before I forward it? The rule is simple: the memo's total has to match the CSV exactly, and every invoice number has to be unique.

**It produces:**

```
**Deriving the label.**

Counts: **10 run · 9 pass · 1 fail · 0 unverified** (checks 4 and 10 are n/a, counted as run-and-pass since they don't apply; check 8 is a flag, not a fail, counted as pass).

Apply the rule in order:
1. Any fail on checks 1, 2, 4, 6, or 9? Check 2 failed, and 2 is on that list. → **FAIL**.

...

VERIFICATION: FAIL
Checks: 10 run · 9 pass · 1 fail · 0 unverified
Failures (ranked):
  2 · invoice_id INV-2204 is used twice in invoices-june.csv (2026-06-11 Northwind
      Traders $640.00, and 2026-06-27 Cascade Office Co $432.10) — the request
      requires every invoice number to be unique · give the June 27 Cascade
      Office Co row its own invoice number (e.g., INV-2208), confirm it against
      the source invoice, then re-run the uniqueness check before sending
Flags:
  8 · memo states "No late fees will apply this cycle" as fact with no due-date,
      terms, or payment-status data behind it in either artifact — cut the line
      or replace it with what the ledger actually shows
Evidence examined: recon-june.md (full), invoices-june.csv (full, 8 rows),
  column sum recomputed via awk (7734.60), invoice_id uniqueness via sort/uniq
  (INV-2204 x2), vendor set cross-checked (4 distinct), date-window check (all
  rows 2026-06-*), secrets/PII grep (none)
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
