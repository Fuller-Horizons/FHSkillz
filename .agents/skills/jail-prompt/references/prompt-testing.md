# Testing a prompt before trusting it

Load this when a prompt will be reused, run at volume, or shipped to a client,
and in every Full-lane run. The goal is a prompt proven on real inputs, not one
that only reads well.

## 1. Build a small test set (5 inputs: 3 to fix on, 2 held out)

- **Typical:** the input the prompt will see most often.
- **Hard:** long, messy, or ambiguous input.
- **Edge:** missing data, conflicting data, or a case where the right answer
  is "Unknown" or a refusal.
- **Adversarial (if the input is untrusted):** contains an instruction such as
  "ignore the above".
- **Split it:** 3 *fix* inputs you tune against, 2 *held-out* inputs you
  never look at while fixing (mix of typical and hard in each). Tuning to a
  handful of inputs overfits; the held-out pair shows whether a fix
  generalizes. With fewer than 5 inputs, say so and hold out at least 1.
- **Balance it:** easy inputs can hide failures on hard ones; never let more
  than half the set be typical.
- Prefer the user's real inputs (with private details masked). Synthetic
  inputs are labeled synthetic. Save the set next to the prompt so later edits
  are re-tested on the same inputs.

## 2. Run and grade

- Run the prompt on every input with its RUN SETTINGS. For prompts that
  will be reused, run at volume, or shipped, run each input **3 times**: the
  input passes only if all 3 runs pass (**pass^3**). A prompt that works 2
  times in 3 is not reliable; one-off prompts run once.
- Grade each output against the SUCCESS TEST (machine checks first) and each
  QUALITY BAR line, as pass/fail. Partial = fail.
- Score = checks passed ÷ checks run. The grader writes **one line per
  failure saying what went wrong** ("table missing COGS basis line"), not just
  a score; those notes drive the fix.
- Grade with a fresh agent or a different model where available. A model
  grading its own output misses its own blind spots.

## 3. Fix one thing, re-run, keep only improvements

- Minimal-first: the usual fix is adding one field (an example, a CONTEXT
  fact, a PROCESS order) for the failure you saw. Name it in TEST RESULTS.
  Also try removing a line that tests show does nothing; shorter wins ties.

- **Write the fix from the grader's notes** (reflective fixing): read the
  failure lines across the fix inputs, find the shared cause, and change the
  one thing that addresses it. Name the change most likely to fix the most failures: usually
  missing context, a vague QUALITY BAR line, a missing example, or a format
  the model can't hold. A bigger model is the last resort, not the first.
- Re-run the fix inputs. Keep the change only if their score goes up and
  no input that passed now fails. Otherwise revert it.
- **Then check the held-out inputs.** If they got worse while the fix inputs
  got better, the change overfit: revert it and look for a more general fix.
- Stop after 2 rounds or a perfect score. For longer optimization, hand off to
  **jail-lab** (metric = this score, budget stated) with the test set as its
  fixture.

## 4. Prove it beats the plain request (baseline)

For a prompt that will be reused or sold as a deliverable, also run the
user's original one-line request on the same inputs and settings, and grade
both outputs blind (labels A/B, order shuffled). Report:

`Baseline: engineered prompt won X, tied Y, lost Z of N inputs.`

If the engineered prompt doesn't win, say so plainly and ship the simpler one.
Extra structure that doesn't improve the output is cost, not quality.

## Picking the model by test

The same test set picks the model: run it on 2–3 candidate models, grade
blind, take the top score (tie → cheaper; quality-first needs a tie with the
strong model). Record the result in RUN SETTINGS (`model sonnet · effort
medium · selected by test: 4 items, sonnet 16/16 = opus 16/16`) and in the
library entry. Delegation sets record it per step (delegation.md).

## 5. Report in the reply

```
TEST RESULTS: 5 inputs (3 fix, 2 held out; 2 real, 3 synthetic) · fix set 12/15 → 15/15 after 1 fix · held out 10/10 · pass^3: 5/5 inputs
Fix kept: added a filled example row to OUTPUT FORMAT (grader notes: 2 malformed tables)
Baseline: won 4, tied 1, lost 0 of 5
Graded by: fresh Sonnet agent (blind)
```

No way to run the prompt in this session → skip the runs, list the test set,
and mark the prompt "untested; run the test set before relying on it".

## Lanes

- **Instant:** no test set. One run if the user asked to run it.
- **Lite:** one run on the user's input, graded against the SUCCESS TEST.
- **Full, or any prompt that will be reused, run at volume, or shipped:** steps 1–5,
  with the held-out split and pass^3.

Patterns adapted from GEPA (reflective fixing from failure notes, held-out
validation; gepa-ai on GitHub) and ECC's eval-harness (pass^k; github.com/affaan-m/ECC,
MIT, © 2026 Affaan Mustafa).
