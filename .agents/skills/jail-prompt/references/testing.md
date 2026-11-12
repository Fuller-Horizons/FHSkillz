# Testing prompts and the prompt library

Part 1: testing a prompt before trusting it. Part 2: reusing tested prompts and saving new ones.


## Testing a prompt before trusting it

Load this when a prompt will be reused, run at volume, or shipped to a client,
and in every Full-lane run. The goal is a prompt proven on real inputs, not one
that only reads well.

### 1. Build a small test set (5 inputs: 3 to fix on, 2 held out)

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

### 2. Run and grade

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

**Grade in layers, cheapest first** (pattern from JEV / jevals, see below):
1. **Code checks** for anything a script can decide: counts, word limits,
   JSON parses, required headings, sums. No model needed.
2. **One typed call per output.** A cheap grader (Haiku or Sonnet) answers
   every remaining check for that output in **one** call, each as
   `{"check": <n>, "pass": true|false, "confidence": 0.0-1.0, "note": "<why, if false>"}`.
   No essays, no score out of 10.
3. **Escalate** to a strong grader (Opus, or a different model family) every
   check that failed, every check under **0.9 confidence**, and every check
   that needs math, logic, code tracing or judgment of tone. The strong
   grader's answer replaces the cheap one.
4. **Human** for high-stakes or disputed checks.

Calibrate before trusting the cut-off: the first time a prompt is tested,
send all checks to both graders; keep the 0.9 cut-off only if the cheap
grader agreed on every check it marked ≥ 0.9 (otherwise raise the cut-off or
skip step 2 for that prompt). Never trust a confidence number on its own: a
polished but wrong answer can fool the cheap grader.

### 3. Fix one thing, re-run, keep only improvements

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

### 4. Prove it beats the plain request (baseline)

For a prompt that will be reused or sold as a deliverable, also run the
user's original one-line request on the same inputs and settings, and grade
both outputs blind (labels A/B, order shuffled). Report:

`Baseline: engineered prompt won X, tied Y, lost Z of N inputs.`

If the engineered prompt doesn't win, say so plainly and ship the simpler one.
Extra structure that doesn't improve the output is cost, not quality.

### Picking the model by test

The same test set picks the model: run it on 2–3 candidate models, grade
blind, take the top score (tie → cheaper; quality-first needs a tie with the
strong model). Record the result in RUN SETTINGS (`model sonnet · effort
medium · selected by test: 4 items, sonnet 16/16 = opus 16/16`) and in the
library entry. Delegation sets record it per step (delegation.md).

### 5. Report in the reply

```
TEST RESULTS: 5 inputs (3 fix, 2 held out; 2 real, 3 synthetic) · fix set 12/15 → 15/15 after 1 fix · held out 10/10 · pass^3: 5/5 inputs
Fix kept: added a filled example row to OUTPUT FORMAT (grader notes: 2 malformed tables)
Baseline: won 4, tied 1, lost 0 of 5
Graded by: code checks → Haiku typed pass (14/15 settled) → Opus on 1 escalated (blind)
```

No way to run the prompt in this session → skip the runs, list the test set,
and mark the prompt "untested; run the test set before relying on it".

### Lanes

- **Instant:** no test set. One run if the user asked to run it.
- **Lite:** one run on the user's input, graded against the SUCCESS TEST.
- **Full, or any prompt that will be reused, run at volume, or shipped:** steps 1–5,
  with the held-out split and pass^3.

Layered typed grading adapted from JEV / jevals (Openlayer, openlayer.com/blog/introducing-jevals-agent-evals-guardrails, Sept 2026; idea only, no code or model used). Patterns adapted from GEPA (reflective fixing from failure notes, held-out
validation; gepa-ai on GitHub) and ECC's eval-harness (pass^k; github.com/affaan-m/ECC,
MIT, © 2026 Affaan Mustafa).

## Prompt library: reuse what already worked

Load this at the start of Phase 3 (check the library) and after a prompt passes
its tests (save it). A tested prompt that fits beats a new one.

### Where it lives

Use the first that exists:
1. The attached claude.ai Project: doc `claude/prompt-library.md`
   (visible in Claude Code, the Claude app, and chat).
2. The repo or working folder: `prompts/` with one file per prompt plus
   `prompts/INDEX.md`.
3. Neither: offer to create option 1 or 2. Never save without the user's OK.

### Before writing a new prompt

Search the library for the task type and keywords. If a saved prompt fits:
- Reuse it, filling in the new CONTEXT and inputs.
- Re-run its saved test set if the model or effort changed since it was tested.
- Say "reused <name> v<n>, tested <date>".

### Entry format (one per prompt)

```
### <name> v<n> — <one-line purpose>
Tested: <date> · <model> · effort <level> · score <passed>/<run> · baseline won <x>/<n>
Use when: <trigger, one line>
Inputs: <tag names>
Test set: <where the inputs are saved>
Changes: v<n>: <what changed and why>
<the full prompt block>
```

### Rules

- Save only prompts that passed their test set (testing.md). Untested
  drafts stay out, or are marked `untested`.
- Never save secrets, client personal data, or real customer records in a
  prompt or test set. Mask them first.
- A new version keeps the old one's entry (one line in Changes) so a
  regression can be rolled back.
- Retire an entry when a newer version beats it on the same test set.
