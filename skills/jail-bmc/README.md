# jail-bmc

Turn a business idea into a nine-block map that separates proof from guesswork.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.3.0.

## What it does

This skill builds or checks a Business Model Canvas. That's a one-page map of how a business works, split into nine blocks: customers, value, channels, and more. Every claim gets one of two labels. VALIDATED means real evidence backs it, like a signed contract or billing data. HYPOTHESIS means it's still a guess. The skill checks the blocks against each other for contradictions, then picks the riskiest guesses to test first.

## Use it when

- You need a business model canvas for a real decision, like a seed round, a pivot, or a new-market launch.
- You want someone to check if your "proven" facts are actually proven, not just hopes.
- You need to know which guesses are riskiest, and what cheap test would prove them right or wrong.

## Don't use it for

- Macro market scans or competitive self-assessment — use [`jail-strategy`](../jail-strategy/) instead.
- Entity or legal-structure questions, like choosing an LLC over a C-corp. This skill does not cover that.

## What you get

A labeled nine-block canvas, a list of contradictions between blocks, and the top few risky assumptions, each paired with a cheap experiment to test it.

## Example

**You ask:**

> Build a business model canvas for GreenCart Wholesale — our B2B ordering platform connecting independent grocery stores to regional produce/dairy distributors in the Pacific Northwest. We're 10 months post-launch, and the board wants to decide whether to raise a $1.5M seed round to expand into the Mountain West region.

**It produces:**

```
## Task contract
**Venture:** GreenCart Wholesale — B2B ordering platform connecting independent grocery stores to regional produce/dairy distributors. **Stage:** operating, 10 months post-launch, live in the Pacific Northwest (PNW) only. **Decision this canvas serves:** go/no-go on raising a $1.5M seed round to fund Mountain-West expansion. **Evidence on hand:** platform billing/transaction export, 12 signed PNW distributor contracts, onboarding-specialist and support-ticket logs, an 8-store order-entry time-tracking study, the PNW Grocers Association partnership agreement, and engineering payroll allocation for the EDI integration team. **Evidence not on hand:** anything from the Mountain-West region — no distributors, stores, or chain-grocer buyers there yet.
...
## Canvas

| Block | Element | Label(V/H) | Evidence ref | Confidence |
| :--- | :--- | :---: | :---: | :---: |
| Customer segments | Independent grocery stores (3–15 registers) ordering from multiple distributors | V | [1] | H |
| Customer segments | Regional chain grocers (5–20 stores) in a new geography | H | — | L |
| Value propositions | Single dashboard replacing phone/fax ordering across distributors, cuts order-entry time ~70% | V | [2] | H |
| Value propositions | Fewer order errors and lower call-center load for distributors | V | [4] | M |
| Channels | Distributor-led onboarding (distributor pushes its buyers onto the platform) | V | [6] | H |
| Channels | PNW Grocers Association referral partnership | V | [3] | M |
| Channels | Paid digital ads to independent grocers | H | — | L |
| Customer relationships | Dedicated onboarding specialist for first 30 days, self-serve after | V | [4] | M |
| Revenue streams | Distributors pay 2.5% transaction fee on orders routed through the platform; stores pay nothing | V | [1] | H |
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
