# Spec — jail-bmc (1.3.0 → 1.4.0) · now 7.9 → target 8.7

Changes
1. `references/unit-economics.md`: worksheet for the step-4 unit-economic dependency — CAC (spend ÷ new customers, by channel), gross margin per customer, churn → expected lifetime, LTV (margin × lifetime, discounted when horizon > 1 yr), LTV:CAC, CAC payback months, contribution margin; every input labeled VALIDATED (with evidence ref) or HYPOTHESIS; one worked numeric example with checkable arithmetic.
2. Declared label mapping (VALIDATED → Fact-backed element, HYPOTHESIS → Assumption) stated once in SKILL.md; any prose claims use canonical labels.
3. Optional visual canvas: when an artifact/HTML/Design tool is available, render the nine blocks as a one-page grid (standard BMC layout) with V/H badges; otherwise the fixed table. Rendering instructions in `references/canvas-render.md` (layout only, no code).
4. Client-facing Delivery section.
5. Description ≤ 450 (currently 626).
Client-facing: yes.

Test scenarios
S1 pre-revenue: "Build a business model canvas for my idea: a subscription service that sends a technician to service residential pool equipment monthly, $89/mo, Long Island. No customers yet."
  [O] no element is labeled VALIDATED without a checkable evidence reference (pre-revenue → mostly HYPOTHESIS)
  [O] names the riskiest 3–5 assumptions with a concrete test for each
  [O] includes a unit-economics check (CAC vs margin/LTV) with labeled inputs
S2 operating business with data: fixture provides 18 months of numbers (customers, churn 3%/mo, CAC $240, price $89, cost to serve $41).
  [O] LTV / payback arithmetic is correct to the inputs given
  [O] segments are specific enough to name a channel (no "everyone" segment)
S3 wrong skill: "Do a SWOT for my pool service business."
  [O] routes to / mentions jail-strategy (or does a SWOT without forcing a BMC)
