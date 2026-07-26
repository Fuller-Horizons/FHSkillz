# jail-diagnose

You give it a bug report. It builds a failing test first, proves the real cause, and fixes it for good.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.1.0.

## What it does

This skill hunts down hard bugs: crashes, slow code, and flaky failures that only happen sometimes. First it builds a loop — a single check that fails every time on the real bug — before it guesses at any cause. Once the loop is red (it fails), the skill shrinks the failing case, tests one guess at a time, and fixes only the cause it can prove. The fix always ships with a permanent test, so the bug cannot come back unnoticed.

## Use it when

- You tell it to debug or diagnose something broken, slow, or flaky.
- A bug only shows up sometimes, and you cannot pin down why.
- A first fix attempt did not work, and the real cause is still unclear.

## Don't use it for

- Checking finished work before it ships — use [`jail-verify`](../jail-verify/) instead.
- Improving a metric on something that already works — use [`jail-lab`](../jail-lab/) instead.

## What you get

A diagnosis report: the bug, the exact loop command, the proven cause with evidence, the fix, and proof it worked. It ends with a handoff block for whatever skill runs next.

## Example

**You ask:**

> Our nightly billing job puts $0.00 on some invoice line items even though the line has real hours and a real rate. Last night's run made 37 broken invoices out of 452. The code is in `billing/invoice_calc.py`. Can you diagnose this?

**It produces:**

````
## Phase 1 — Build the loop

Escalating through the loop types in order. A failing test at the function
seam nearest the defect is the top of the list and looks reachable here —
`invoice_calc.py` is a pure function, no I/O — so I'll pull one real broken
row and turn it into a test before touching any theory of the cause.

...

Run:
```
$ pytest tests/billing/test_invoice_calc.py::test_discount_pct_from_broken_2026_07_24_run -v
FAILED tests/billing/test_invoice_calc.py::test_discount_pct_from_broken_2026_07_24_run
AssertionError: assert Decimal('0.00') == Decimal('2280.13')
```

**Phase-1 done-check:** `pytest tests/billing/test_invoice_calc.py::test_discount_pct_from_broken_2026_07_24_run` — one command, fails on the real defect, no DB or network needed. Tight, red-capable.
````

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
