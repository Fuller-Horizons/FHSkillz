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
