# Worked example: verifying a client memo (single lane)

Synthetic data. Checklist used: Report or memo.

## Input

User: "Verify this before I send it to the client."

Task contract (reconstructed from the request): a one-page memo to a
three-location home-services owner. Deliverable: Q3 revenue summary plus
three actions. Constraints: every figure sourced; every action has an owner
and a date; sentence one gives the recommendation.

Memo under review (`q3-memo.md`, excerpt):
- Sentence one: "Shift 15% of ad budget to the plumbing line."
- Revenue table: Plumbing $182,400 · HVAC $140,900 · Electrical $96,300 ·
  **Total $428,600** (source: client's accounting export, `q3-export.csv`)
- Claim: "Local construction firms grew 14% last year (U.S. Census Bureau,
  County Business Patterns, https://www.census.gov/programs-surveys/cbp.html
  [accessed 2026-11-12])."
- Actions: (1) Reallocate ad budget, owner: Dana, due 2026-12-01.
  (2) Retire the Electrical coupon, owner: blank, due 2026-12-15.
  (3) Review pricing, owner: Dana, due 2026-12-20.

## Verification run

Evidence opened: `q3-memo.md`, `q3-export.csv`, the cited Census page.
Producer was a different session; this pass started from the contract.

| # | Check | Observation | Result |
|---|-------|-------------|--------|
| 1 | Contract compliance | Sentence one is a recommendation; three actions present; one has no owner | fail |
| 2 | Completion criteria | Contract's done-check "every action owned and dated": action 2 has no owner | fail |
| 3 | Internal consistency | Table rows sum to $419,600; memo states $428,600 (difference $9,000) | fail |
| 4 | Grounding & citation | Cited page is the program landing page for the dataset, with no table or row given; the 14% cannot be traced to it | fail |
| 5 | Calculations & schema | CSV parses; the CSV column sum is $419,600, so the table rows are right and the total is wrong | pass |
| 6 | Tool/test reality | No tool claims in the memo | pass |
| 7 | Edge cases & omissions | No sensitivity on the 15% shift; not required by the contract | pass |
| 8 | Unsupported confidence | "Will increase leads" is stated as fact; no basis shown (Inference at best) | flag |
| 9 | Security/privacy | No secrets or personal data found | pass |
| 10 | Implementation readiness | Action 2 has no owner; others have owner and date | fail |

Counts: passes are checks 5, 6, 7, 9; fails are checks 1, 2, 3, 4, 10; check
8 is a flag and is counted as a pass. Nothing was UNVERIFIED.
**10 run · 5 pass · 5 fail · 0 unverified**

Rule: a fail on check 1, 2, or 4 forces FAIL. All three failed. Verdict FAIL.

## Emitted verdict

```
VERIFICATION: FAIL
Checks: 10 run · 5 pass · 5 fail · 0 unverified
Failures (ranked):
  3 · revenue rows sum to $419,600, memo total says $428,600 ($9,000 gap)
      · correct the total to $419,600 (matches q3-export.csv)
  4 · the 14% construction-growth claim cites a Census program landing page
      with no table or row · cite the exact table, or label it Unknown and cut it
  2/10 · action 2 (retire Electrical coupon) has no owner · assign one
Flags:
  8 · "will increase leads" is stated as fact · relabel as Inference
Evidence examined: q3-memo.md (full), q3-export.csv (full, column sum
  recomputed), Census CBP program page (opened)
Checklist used: Report or memo
VERDICT-JSON: {"verdict":"FAIL","run":10,"pass":5,"fail":5,"unverified":0,"lane":"single"}
```

```yaml
JAIL-HANDOFF:
  skill: jail-verify
  status: complete
  facts: [table rows sum to $419,600 per q3-export.csv; memo total is $428,600]
  unknowns: [source of the 14% construction-growth figure]
  outputs: [verification verdict FAIL]
  evidence: [q3-export.csv · supports the $419,600 sum · local file · 2026-11-12; Census County Business Patterns program page · cited, but names no table · https://www.census.gov/programs-surveys/cbp.html · 2026-11-12]
  risks: [client sees a wrong total and an untraceable statistic]
  confidence: high
  next: producing skill fixes the 4 ranked items, then re-verify checks 1-4 and 10
  approval_required: []
```
