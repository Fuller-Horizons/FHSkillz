# Upgrade 0.27 ledger

NODE F1 | STATUS: verified | ARTIFACT: docs/JAIL-CONSTITUTION.md (Canonical claim labels) + docs/schemas/jail-handoff.schema.json (valid JSON)
NODE F5 | STATUS: verified | ARTIFACT: scripts/project-hosts.py --check exit 0; test_project_hosts 6 OK; .agents/skills = 26 + README
NODE F4 | STATUS: verified | ARTIFACT: scripts/tests 15 OK; run-live-evals.py --dry-run plan printed (12 runs for 3 cases)
NODE F2 | STATUS: verified | ARTIFACT: jail-py-toolkit tests 42 OK; pii-scan exit 1 with no values printed; label-lint/handoff-lint/desc-check run on live skills
NODE FIX | STATUS: verified | ARTIFACT: evals/behavioral-0.27 36 cases, all assertions tagged [O]/[F], JSON valid
NODE F3 | STATUS: verified | ARTIFACT: hooks/tests 19 OK; quarantine block exit 2 without value; off mode exit 0; approval_gate emits ask JSON for git push
NODE A-verify | STATUS: verified | ARTIFACT: desc-check OK, handoff-lint OK, label-lint OK, 147 lines
NODE A-decide | STATUS: verified | ARTIFACT: desc/handoff/label checks OK; EV arithmetic python-checked by author
NODE A-research | STATUS: verified | ARTIFACT: desc/handoff/label/cite-check OK (example URLs not fetched by author — orchestrator to verify)
NODE A-task-contract | STATUS: verified | ARTIFACT: desc/handoff/label checks OK; 154 body lines
NODE A-red-team | STATUS: verified | ARTIFACT: desc/handoff/label checks OK; 141 lines
NOTE heldout | 12 held-out cases authored by orchestrator after specs, stored outside repo until test time (authors never saw them)
NODE A-summarize | STATUS: verified | ARTIFACT: desc/handoff checks OK; toolkit tests 48 OK; readability.py added
VERIFY research-example-urls | cbp.html OK, nonemployer-statistics.html OK, bls.gov/cew OK (WebFetch 2026-11-12); census.gov/naics/ fetch error — unverified
NODE A-prompt | STATUS: verified | ARTIFACT: desc/handoff OK; 1,649 words (from 3,072); key rules present inline (grep audit); toolkit tests 57 OK
NODE A-strategy | STATUS: verified | ARTIFACT: desc/handoff/label OK; 154 lines; COMPETITIVE lane added
FIX label-lint | flag only known legacy labels (false positives on headings like 'Fact bias' removed); tests 57 OK
NODE A-prospect | STATUS: verified | ARTIFACT: desc/handoff/score-check OK; free-sources 17/24 URLs confirmed live (7 blocked/JS-only, marked)
NODE A-rate | STATUS: verified | ARTIFACT: desc/handoff/score-check OK; 140 lines
NODE A-bmc | STATUS: verified | ARTIFACT: desc/handoff OK; unit-economics arithmetic re-checked (LTV 1600, LTV:CAC 6.7, payback 5.0)
NODE A-cpr | STATUS: verified | ARTIFACT: desc 418 chars (from 1,386), desc/handoff OK
NODE T-routing | STATUS: verified | ARTIFACT: evals/results/2026-11-12-0.27-trigger/ — 3 Haiku judges each 100% fire / 0% false-fire on 109 cases
FINDING natural-arm | b1: 96 runs, 0 errors, $5.02; skill auto-invoked in only 10/48 old and 11/48 new runs (research 0/8 both) — natural routing in claude -p rarely loads the skill, so content A/B uses a FORCED arm (/fh-skillz:<skill>); natural arm kept as invocation-rate evidence only
NODE T-live-b1 | STATUS: verified | ARTIFACT: evals/results/2026-11-12-0.27-waveA-b1-forced/ — 96 forced runs, 0 errors, $6.28; 2 blind Sonnet graders + 14 blind Opus tie-breaks (grades/resolved.jsonl)
RESULT b1 | KEEP decide 8/8 vs 7/8 · research 5/8 vs 3/8 · summarize 6/8 vs 5/8 · task-contract 6/8 vs 4/8 | TIE red-team 7/8, verify 6/8 (rule says REVERT; owner call pending)
RESULT b1-heldout | new 10/12 vs old 8/12 cases (46/48 vs 42/48 assertions) — no overfitting signal
NODE A-prompt-deleg | STATUS: verified | ARTIFACT: jail-prompt 2.2.0 delegation lane (references/delegation.md, example-delegation-competitor-scan.md); chain-lint orchestration checks + tests/test_chain_lint.py 15 OK; toolkit 72 OK; desc 448 chars; core 113 lines; codex projections in sync; live A/B queued (evals/behavioral-0.27/jail-prompt-delegation.json, 4 cases, old = 2.1.0 snapshot)
NODE A-prompt-2.3 | STATUS: verified | ARTIFACT: jail-prompt 2.3.0 — pinned Opus 5.5/medium (frontmatter), claude-prompting.md, generation-settings.md rewritten from Anthropic docs (no sampling knobs), QUALITY BAR/EXAMPLES/RUN SETTINGS, prompt-testing.md (test set + baseline), prompt-library.md, gather-before-asking; prompt-lint new checks + 7 tests; toolkit 79 OK; both example prompts pass prompt-lint --strict; core 124 lines; desc 448
NOTE eval-design | jail-prompt now pins its model, so A/B arms run both versions on claude-opus-5-5 --effort medium (a haiku/sonnet arm would be overridden by the new version only); end-to-end test (scripts/run-e2e-prompt-evals.py) grades FINAL outputs: plain request vs jail-prompt prompt, final runs on sonnet+haiku at medium
NODE A-prompt-2.5 | STATUS: verified | ARTIFACT: jail-prompt 2.5.0 quality-first default + measured model selection (selected_by); chain-lint mode/selection checks; toolkit 100 OK; snapshot /home/claude/snap/new-jp23 used by 12:22 tests
NODE A-prompt-2.6 | STATUS: verified | ARTIFACT: jail-prompt 2.6.0 core 96 lines/1,304 words; models.md single dated reference; prompt-lint --reply (TEST RESULTS/UNTESTED); validate-skills lints examples + stale-fact warning (verified to catch a missing test line and a 103-day-old date); toolkit 103 OK
NODE A-prompt-library | STATUS: verified | ARTIFACT: Project doc claude/prompt-library.md (prospect → jail-prospect route + 4 prompts, all prompt-lint --strict PASS, marked untested); evals/e2e/library/ + map.json; run-e2e-prompt-evals.py --library mode (plumbing verified with a stand-in); select-models.py + 7 tests (toolkit 110 OK)
NODE A-prompt-2.7 | STATUS: verified | ARTIFACT: jail-prompt 2.7.0 quote-before-claim + portable meta-prompt + tiers; jail-py-toolkit 1.4.0 quote-check.py (6 tests) + description 838->450 chars; toolkit 117 OK; validation pass; desc violations 14->13 skills
