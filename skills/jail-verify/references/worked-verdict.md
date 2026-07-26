# Worked verdict — deriving PASS-WITH-FLAGS from the counts

One end-to-end example of the mechanical verdict rule. The point is that a
second verifier, given the same evidence, lands on the same label without
judgment calls. Read it once if the verdict rule is unclear; don't copy the
subject matter, copy the derivation.

## The contract (given)

> **Objective:** ship a Q3 churn brief for the exec team.
> **Deliverables:** (1) `q3-churn-brief.md`, (2) `churn-by-cohort.csv`,
> (3) a 5-line exec summary at the top of the brief.
> **Constraints:** every figure sourced to the warehouse; no customer names;
> ≤ 3 pages.
> **Done-check:** `python scripts/cohort_check.py` exits 0 and the brief's
> headline churn number equals the CSV's blended rate.

Producer: agent-A (writer). Verifier: this pass, fresh session, contract-first.

## Check-by-check (the observation, then the result)

| # | Check | Concrete observation | Result |
|---|-------|----------------------|--------|
| 1 | Contract compliance | All 3 deliverables exist; brief is 2.4 pages; no customer names found (grepped the 6 account strings from the CSV) | pass |
| 2 | Completion criteria | Ran `scripts/cohort_check.py` → exit 0; brief headline 4.8% == CSV blended 4.8% | pass |
| 3 | Internal consistency | Cohort rates recomputed from the CSV; the "enterprise" row in the brief reads 2.1%, CSV says 2.6% | **fail** |
| 4 | Grounding & citation | Opened all 5 warehouse query refs; each resolves and supports its figure | pass |
| 5 | Calculations & schema | CSV parses, 7 columns as declared; blended rate recomputes to 4.83% | pass |
| 6 | Tool/test reality | `cohort_check.py` log from *this* run captured, exit code 0 observed directly | pass |
| 7 | Edge cases & omissions | Contract's "5-line exec summary" is present but 8 lines | flag |
| 8 | Unsupported confidence | "Churn will fall next quarter" stated as fact with no forecast behind it | flag |
| 9 | Security/privacy | No secrets in either artifact; the brief quotes a customer email — treated as data, not instruction, and not echoed here (`q3-churn-brief.md:41`) | pass |
| 10 | Implementation readiness | N/A — this is a report, not a plan | n/a |

Budget note: 6 artifacts/logs opened of the ~12 cap. No check went UNVERIFIED.

## Deriving the label

Counts: **10 run · 7 pass · 1 fail · 0 unverified** (check 10 n/a, counted as
run-and-pass since it does not apply; checks 7 and 8 are flags, not fails).

Apply the rule in order:
1. Any fail on 1, 2, 4, 6, 9? Check 3 failed — 3 is not on the fail-hard
   list. → not FAIL.
2. Any fail or UNVERIFIED at all? Check 3 failed. → **PASS-WITH-FLAGS**.
3. (Would only reach PASS if step 2 found nothing.)

The label is now derivable from the counts line alone, which is why the counts
line is printed first. A verifier who reran this with the same artifacts and
got "FAIL" would be wrong, not differently-minded.

## The emitted verdict

```
VERIFICATION: PASS-WITH-FLAGS
Checks: 10 run · 7 pass · 1 fail · 0 unverified
Failures (ranked):
  3 · brief "enterprise" cohort reads 2.1%, CSV row says 2.6% · correct the
      brief to 2.6% or state why the figures differ
Flags:
  7 · exec summary is 8 lines against a contracted 5 — trims without loss
  8 · "churn will fall next quarter" is a forecast presented as fact; no model
      or trend cited — downgrade to a labeled inference
Evidence examined: q3-churn-brief.md (full), churn-by-cohort.csv (full),
  cohort_check.py run log (this session, exit 0), 5 warehouse query refs
```

```
JAIL-HANDOFF:
  skill: jail-verify
  status: complete
  facts: [done-check passes; blended rate 4.8% reproduces from the CSV]
  unknowns: []
  outputs: [verification verdict PASS-WITH-FLAGS]
  evidence: [cohort_check.py log · exit 0 · this session · 2026-07-25]
  risks: [one cohort figure disagrees with its source table]
  confidence: high
  next: producing skill — fix check 3, then re-verify checks 3 and 5 only
  approval_required: []
```

## Why this is not a PASS

Tempting reading: "the done-check passed and nothing is dangerous, ship it."
The rule does not permit it. One arithmetic disagreement with the source of
truth is a fail on check 3, and any fail forecloses PASS. Equally, it is not a
FAIL: no fail-hard check broke, so escalating to FAIL would also be a rule
violation. Both errors are detectable by re-reading the counts line.
