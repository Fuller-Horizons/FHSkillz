# Deliverable checks — extend the 10-check sequence

Pick the list that matches what you are verifying and say which one you used.
If the deliverable is a mix (a memo with a model inside), run both lists. Each
item names what would fail it. An item you cannot run is UNVERIFIED, never a
pass. A failed item counts under the check it extends (shown in brackets).

## Financial model
- Inputs are labeled and each carries a label (Fact, User-provided, Estimate,
  or Judgment) and a source or owner. [4]
- Formulas are live, not typed-in numbers. Pick three outputs and trace each
  to its inputs; a hardcoded value in a calculated cell fails. [5]
- Totals tie: subtotals sum to totals, and the model total equals the figure
  quoted in any memo or deck. Recompute at least three. [3, 5]
- Sensitivity is present: at least the two or three inputs that move the
  answer most are flexed, with the result shown. Missing = fail. [7]
- Units, periods, and currency are stated and consistent. [3]

## Slide deck
- Each slide headline states a finding with its number ("Churn fell to 4.8%"),
  not a topic ("Churn update"). [1, 3]
- Every chart names its source and date; numbers on the slide match the chart
  and the appendix. [4, 3]
- An ask or decision slide is present, with an owner and a date. [1, 10]
- Claims keep their labels; forecasts are not shown as fact. [4, 8]
- Nothing on the slides contradicts the speaker notes or the memo behind it. [3]

## Report or memo
- Sentence one is the answer or the recommendation. [1]
- Labels survived (Fact / User-provided / Inference / Estimate / Judgment /
  Unknown). [4]
- Every number has a source, or is labeled Estimate or Assumption. Recompute
  every total and percentage. [3, 5]
- Every cited source was opened and supports the specific claim it is
  attached to. [4]
- Every action item has an owner and a date. [10]
- Names, figures, and dates match across sections. [3]

## Plan or workflow
- Each step has a named owner, a due date, and its dependencies. [10]
- The metric has a baseline and a target, and says how it will be measured. [2, 10]
- Approvals, permissions, and costs are named. [10]
- Rollback or stop condition exists and is realistic. [10]
- The done-check can actually fail. [2]

## Research packet
- Cite-check: open every source (all when consequential). It exists, is dated,
  and supports the claim as worded. [4]
- Each answer sentence maps to a source in the packet; no orphan claims. [4]
- Contradictions between sources are shown, not smoothed over. [3]
- Gaps are listed as Unknown. A packet with no gaps is a flag. [7, 8]
- Source tier and date are stated; stale sources are called out. [4]

## Code change
- Tests were run in this execution: the output and exit code are in hand,
  not just a claim. No log = UNVERIFIED. [6]
- The diff was read in full, and it matches the contract. No unrelated edits
  smuggled in. [1]
- New paths have tests; edge cases (empty, large, bad input) are covered or
  listed as a gap. [7]
- No secrets, keys, or personal data in the diff. Name the file and line; do
  not echo the value. [9]
- Build or lint passes in this run, if the contract requires it. [2, 6]
