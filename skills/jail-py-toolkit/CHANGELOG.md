# Changelog — jail-py-toolkit

## 1.8.0 — 2026-11-12
- Merged jail-py-lab into the toolkit: `lab-run.py`, `lab-report.py`, `lab-compare.py` (and `_ledger_io.py`) now live here, unchanged; one Python companion to install instead of two.

## 1.7.0 — 2026-11-12

- **artifact-lint.py**: single-file HTML review pages (prototype marking, viewport, explicit background, no outside requests or local asset files, unique review ids, exactly 3 variants + 1 switch, answer controls need a copy button, revisions legend, sandbox-blocked calls outside try/catch). 11 tests.

## 1.6.0 — 2026-11-12

- handoff-lint: optional `tested` key after `checks` (tested | untested | n/a); +1 test.

## 1.5.0 — 2026-11-12

- prompt-lint: Claude 5 checks (written-out reasoning requests, "think carefully"/"don't think", prefill); minimal-first required sections (OBJECTIVE, SUCCESS TEST, OUTPUT FORMAT); +4 tests.
- select-models: `--repeats K` (pass^K per candidate); +1 test.

## 1.4.0 — 2026-11-12

- **quote-check.py**: verifies each Fact's verbatim quote appears in its saved source (normalizes case, spacing, quote/dash/hyphen variants, HTML tags and entities); flags Facts with no quote, unknown sources, quotes of 3 words or fewer; warns over 40 words. 6 tests.
- prompt-lint accepts tool-neutral tiers in RUN SETTINGS (+1 test).
- Description rewritten to 450 chars with a "Do NOT use" line (was 838) and the new checks; keeps the "scan for secrets" / "lint" / "dry-run" / "skill structure" / rating triggers.

## 1.3.0 — 2026-11-12

- **select-models.py**: pick a step's model by blind, measured trial (candidates × test items, separate grader model, `selected_by` record; tie → cheaper; quality-first / cost-first). 7 tests with an offline stand-in for `claude`.
- **chain-lint.py**: delegation manifests — orchestration block, agent model/effort/scope/context, verifier independence, parallel independence, Fable + full model IDs, escalation targets, output caps, batching, quality-first mode, `selected_by` validation. New `test_chain_lint.py` (35 tests).
- **prompt-lint.py**: QUALITY BAR, EXAMPLES, VERIFICATION PLAN, RUN SETTINGS sections; warns on missing QUALITY BAR / RUN SETTINGS, a Claude model without effort, sampling knobs on Claude; `--reply` mode requires a TEST RESULTS or UNTESTED line. New `test_prompt_lint.py` (11 tests).
- Toolkit tests: 110.

## 1.2.0 — 2026-11-12

- Added fh_patterns.py (shared secret + PII detectors, value-free results) and handoff-lint, label-lint, cite-check, gate-record-lint, pii-scan, desc-check, score-check; secret-scan.py now uses fh_patterns and prints file:line: kind only; unit tests + fixtures added.

## 1.1.0 — 2026-07-25 (plugin 0.25.0)

- De-duplicated the `VERIFIABLE` regex: chain-lint.py now imports it from
  prompt-lint.py (importlib-by-path, same pattern save-rating.py uses for
  validate-rating.py) instead of keeping a second, drifted copy; the shared
  pattern is the union of both prior regexes (adds `trace[sd]?` to
  prompt-lint's copy) so neither linter loses a match it had today.
- SKILL.md: added a "Handoff shape" line stating calling skills should
  record `checks: {<script>: "pass"|"fail"|"error"|"n/a", ...}` in their own
  JAIL-HANDOFF block, derived from exit code — `0`→pass, `1`→fail, `2`→error
  (usage/IO, the check did not run) — distinct from `"n/a"` for a check
  never attempted, sourced to jail-py-toolkit.
- save-rating.py: wrapped every history-file IO path in try/except OSError
  with an actionable message and exit 2 (usage/IO) instead of an unhandled
  traceback exiting 1 (previously the same code as "record failed
  validation") — `os.makedirs` in `history_path()`, the history read in
  `previous_overall()` (e.g. a directory planted at the history path), and
  the history-file `open(path, "a")` write. A missing history file (first
  run) still returns "no previous rating" normally, not an error.
- chain-lint.py: wrapped the importlib-by-path load of sibling
  prompt-lint.py (needed for the shared `VERIFIABLE` regex) in
  try/except (OSError, ImportError, AttributeError), printing an actionable
  message naming the missing sibling and exiting 2 (usage/IO) instead of an
  unhandled `FileNotFoundError` exiting 1 (previously indistinguishable
  from "chain has lint errors") when chain-lint.py is copied somewhere
  without prompt-lint.py next to it.

## 1.0.0 — 2026-07-22 (plugin 0.23.0)

Initial release as the merger of **jail-py-prompt-tools 1.0.0** (5 prompt
checks) and **jail-py-rate-tools 1.0.0** (4 rating checks), both retired
this release; script code carried over unchanged (git history holds
lineage).

- One toolkit, two check families, nine scripts, stable exit codes.
- New in the merge: the repo release validator (`scripts/validate-skills.py`)
  now runs the toolkit self-checks every release, so the checks fire on the
  release loop instead of only on request.
