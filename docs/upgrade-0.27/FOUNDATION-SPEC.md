# Foundation spec (Phase 1) — build before any skill is authored

Repo: `/home/claude/fhskillz-work` (branch `upgrade/0.27-wave-a`). ECC reference checkout (read-only): `/home/claude/ext/ecc`.
House rules: stdlib-only Python 3.8+; every script takes files/stdin as args; exit codes `0 pass · 1 fail · 2 usage/IO`; each new script gets a unit test file under `skills/jail-py-toolkit/tests/test_<script>.py` (unittest, stdlib) using fixtures in `skills/jail-py-toolkit/tests/fixtures/`. Run all tests with `python3 -m unittest discover -s skills/jail-py-toolkit/tests -v`. Never print secret values — print class + line number only.

## F1 — Canonical labels + handoff schema (done by orchestrator)
- `docs/JAIL-CONSTITUTION.md` → section **Canonical claim labels** (six labels + mapping table).
- `docs/schemas/jail-handoff.schema.json` → JSON Schema for the JAIL-HANDOFF block.

## F2 — New toolkit scripts (`skills/jail-py-toolkit/scripts/`)
| Script | Checks | Fail when |
|---|---|---|
| `handoff-lint.py <file>` | Finds every fenced ```yaml block starting `JAIL-HANDOFF:` and validates it against `docs/schemas/jail-handoff.schema.json` rules (implement a minimal stdlib parser for `key: value`, `key: [a, b]`, and `- item` lists) | missing `skill`/`status`/`unknowns`/`approval_required`; `status` ∉ {complete, partial, blocked, stop}; `confidence` ∉ {high, medium, low}; unknown top-level key; keys out of canonical order |
| `label-lint.py <file> [--require-evidence]` | Every bracketed or bold claim label in the text belongs to the canonical set (Fact, User-provided, Inference, Estimate, Judgment, Assumption, Unknown) or a declared domain mapping (`VALIDATED`, `HYPOTHESIS`); with `--require-evidence` every `Fact` occurrence on a line must carry a `[n]` citation | non-canonical label (e.g. `Known`, `Analyst Judgment`, `Missing Evidence`); `Fact` without `[n]` under the flag |
| `cite-check.py <file>` | Answer/packet citation integrity: every `[n]` in the body resolves to a numbered source line; every numbered source is cited ≥1×; every source line has a URL/ref and an ISO date | orphan marker, uncited source, source line missing URL or date |
| `gate-record-lint.py <file>` | Every `GATE-RECORD` line has action, tier ∈ {NEVER, PER-ACTION, BATCHABLE, AUTO}, approver, ISO-8601 ts, result ∈ {approved, denied, pending} | any field missing/invalid |
| `pii-scan.py <file|->` | Extends secret-scan with personal-data classes: SSN (`\b\d{3}-\d{2}-\d{4}\b`, excluding 000/666/9xx areas), payment card (13–19 digits passing Luhn), US bank routing (ABA checksum), email+phone pairs, DOB-labelled dates | any hit (report class + line, never the value) |
| `desc-check.py <skills-dir>` | Every SKILL.md: description ≤ 450 chars, contains `Do NOT use` (negative trigger), core ≤ 160 lines (excluding frontmatter), has `metadata.version` | any violation |
| `score-check.py <file>` | jail-rate / jail-prospect scorecards: weights sum to 100%, overall = Σ(score×weight) to 1 decimal, each score 0.0–10.0 (or 0–100 for prospect components that sum to the declared total) | arithmetic mismatch |

Wire all new scripts into `scripts/validate-skills.py` release checks where they apply to the repo itself (`desc-check.py` over `skills/`, `handoff-lint.py` over every `skills/*/references/example*.md`).

## F3 — Opt-in enforcement hooks (`hooks/`, Python, stdlib)
Mode via env `FHSKILLZ_HOOKS` = `off` (default) | `warn` | `block`; per-gate override `FHSKILLZ_HOOK_<NAME>=off|warn|block`. In `off` mode a hook must exit 0 within 50 ms. All hooks append one JSON line per decision to `${CLAUDE_PLUGIN_DATA:-~/.fhskillz}/gate-ledger.jsonl` (`GATE-RECORD` fields).
- `hooks/quarantine_guard.py` — PreToolUse on `Write|Edit|MultiEdit|Bash`: scan `tool_input` (content / new_string / command) with the secret + PII patterns from F2. `warn` → stderr warning, exit 0. `block` → exit 2 with a message naming the class (never the value).
- `hooks/approval_gate.py` — PreToolUse on `Bash` and `mcp__.*`: classify external-effect actions (git push, npm publish, curl/wget with -X POST/PUT/DELETE or --data, rm -rf outside cwd, kubectl delete, DROP TABLE; MCP tool names containing send|post|publish|delete|create_event|share|transfer|buy). In `warn`/`block` mode emit Claude Code JSON `{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"<APPROVAL REQUEST summary>"}}` so a human must approve; `block` uses `deny` for NEVER-tier patterns (`curl … | sh`, `rm -rf /`, `--no-verify` pushes).
- `hooks/verify_gate.py` — Stop: if the last assistant message claims completion ("done", "complete", "all tests pass", "shipped") and the transcript tail has no `VERIFICATION:` verdict line and no JAIL-HANDOFF with `status`, `warn` prints a reminder; `block` blocks ONCE (honor `stop_hook_active` → exit 0).
- `hooks/handoff_nudge.py` — PreCompact: print a one-line nudge to write a jail-handoff baton; never blocks.
- Update `hooks/hooks.json` to register them (keep the existing skill-invocation logger). Add `hooks/README.md` documenting modes and how to enable.
- Unit tests in `hooks/tests/` feeding sample hook JSON on stdin for each mode.

## F4 — Live A/B eval runner (`scripts/run-live-evals.py`)
Pattern adapted from ECC `skill-comply` (MIT) — written fresh.
- Inputs: `--cases <eval json> [...]`, `--old <plugin dir>`, `--new <plugin dir>`, `--models haiku,sonnet`, `--out <dir>`, `--jobs 6`, `--max-cases-per-skill N`, `--allowed-tools "Skill,Read,WebSearch,WebFetch"`, `--timeout 600`.
- For each case × version × model: fresh temp workspace; run `claude -p <prompt> --model <m> --setting-sources project --plugin-dir <version dir> --output-format stream-json --verbose --allowedTools <list> --permission-mode default`; store `<out>/raw/<run-id>.jsonl` and extract the final result text to `<out>/outputs/<case>/<label>.md` where label ∈ {A, B} is assigned by a seeded shuffle per case. The mapping goes ONLY to `<out>/private/key.json`.
- Also record per run: skills invoked (from `Skill` tool_use events), tools used, cost (`total_cost_usd`), turns, duration, exit status → `<out>/runs.jsonl`.
- `--dry-run` prints the run plan and estimated run count without calling claude.
- Subcommand `score --out <dir> --grades <grades.jsonl>` joins grades with the private key and prints per-skill pass rates for old vs new, per model, and writes `<out>/summary.json`.
- Unit tests with a fake `claude` shim (env `FHSKILLZ_CLAUDE_BIN`) — no real calls in tests.

## F5 — Host-compat projection (`scripts/project-hosts.py`)
- Generates `.agents/skills/<name>/SKILL.md` (Codex) from `skills/<name>/SKILL.md`: frontmatter keeps only `name`, `description`, `metadata` (drop nothing else is allowed by Codex: `name, description, metadata, license, allowed-tools`); rewrites `${CLAUDE_PLUGIN_ROOT}` / `${CLAUDE_SKILL_DIR}` in executable fences to a relative path; copies `references/`.
- `--check` mode fails if projections are stale or contain Claude-only substitutions in executable fences. Pattern adapted from ECC `skill-host-compat` (MIT).
- Unit test over a fixture skill.

## Acceptance for Phase 1 (orchestrator verifies)
`python3 -m unittest discover -s skills/jail-py-toolkit/tests` and `-s hooks/tests` and `-s scripts/tests` all pass; `python3 scripts/validate-skills.py` exit 0; `python3 scripts/run-live-evals.py --dry-run …` prints a plan; hooks in `off` mode are no-ops.
