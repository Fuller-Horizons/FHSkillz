# Harness templates — one skeleton per Phase-1 loop type

Plain procedure skeletons for each loop type in Phase 1's escalation order.
Pick the matching skeleton, fill in the blanks, and confirm against the
Phase-1 done-check: one named command/procedure, tight and red-capable. No
code here by design — describe the steps, then implement them in whatever
the target system actually uses.

## 1. Failing test
1. Identify the seam nearest the defect (unit function, module boundary,
   e2e step).
2. Write a test that exercises that seam with the failing scenario's exact
   inputs.
3. Assert the specific wrong-vs-right output, not "doesn't throw."
4. Run it once to confirm it currently fails (red). If it passes, the seam
   is wrong — move closer to the defect.
5. Name it as the Phase-1 done-check: `<test file>::<test name>`.

## 2. Scripted invocation
1. Identify the entry point (CLI command, HTTP endpoint, function call)
   that reaches the defect.
2. Build a fixture input that triggers the defect deterministically.
3. Capture the known-good output for the same input (spec, prior version,
   or manual derivation).
4. Script the invocation + diff-against-known-good as one command.
5. Confirm the diff is non-empty (red) before proceeding.

## 3. Replay a captured artifact
1. Obtain the real payload/log/event that accompanied the failure (from
   the user, logs, or a bug report).
2. Isolate the path that consumes it — strip the unrelated surrounding
   system.
3. Feed the artifact through that isolated path in one call.
4. Assert the specific wrong output the artifact is known to produce.
5. Store the artifact alongside the harness so the loop is reproducible
   without re-fetching it.

## 4. Throwaway harness
1. Identify the minimal component that contains the defect.
2. Mock or stub every dependency the component needs but that doesn't
   determine the bug.
3. Drive the component directly with the triggering input, one call.
4. Assert the wrong output at the component boundary.
5. Mark the harness throwaway — it won't survive the fix — but keep it
   until Phase 4's regression case supersedes it.

## 5. Property/fuzz loop
1. State the property that should always hold (e.g. "output length ==
   input length").
2. Generate many random/edge-case inputs; pin the seed for determinism.
3. Run the target against each input, checking the property.
4. Capture the first (or smallest) input that breaks the property, plus
   the failure shape.
5. Re-run against that single captured input as the tightened,
   deterministic loop.

## 6. Bisection harness
1. Identify a known-good state and a known-bad state (commits, config
   versions, deploys).
2. Script "boot at state X, run the check, report pass/fail" as one
   repeatable step.
3. Walk the states (binary search if ordered) using that script.
4. Record the last-good/first-bad pair as the minimized defect window.
5. The bisection script's invocation becomes the Phase-1 done-check.

## 7. Differential loop
1. Identify the two variants to compare (old vs. new code, config A vs.
   B, model 1 vs. model 2).
2. Fix a representative input set that both variants can consume
   unchanged.
3. Run both variants against the same input(s) in one script.
4. Diff the outputs; assert the diff is non-empty where behavior should
   match.
5. Keep the input set small enough that the diff is easy to read at a
   glance.

## 8. Structured human loop
1. Confirm no automated loop (1–7) reaches the defect — this is the last
   resort.
2. Write the human's steps as a numbered, literal script (exact clicks,
   exact inputs, exact order) — not a paraphrase.
3. Have the human (or yourself, if reachable) execute the script once and
   record the observed output verbatim.
4. Mark the specific step and expected-vs-actual output that constitutes
   "red."
5. Re-run the same script to confirm the failure is repeatable before
   treating it as the Phase-1 done-check.
