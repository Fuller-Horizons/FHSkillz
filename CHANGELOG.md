# Changelog

All notable changes to the FHSkillz repo and its skills. Format follows [Keep a Changelog](https://keepachangelog.com/); versioning is [SemVer](https://semver.org/). Per-skill versions live in each `SKILL.md`; the plugin version lives in `marketplace.json`.

## [plugin 0.11.0] — 2026-06-14

### jail-rate → 1.0.0 (new)
- **New skill.** Rates software products on a disciplined 0.0–10.0 scale across five weighted dimensions — software quality 25%, features 20%, usability 20%, security 20%, marketability 15%. Includes named calibration bands (anti-inflation), a critical-flaw cap (a blocking issue caps its dimension ≤4.0), prioritized impact×effort recommendations, and a projected **post-improvement** rating (current → potential) shown as a scorecard.

## [plugin 0.10.0] — 2026-06-08

### jail-prompt → 1.6.0
- **Bundled, runnable guardrails (was: instructions-only).** Three stdlib scripts now back the behaviors the skill used to merely describe, lifting Execution Reliability / Safety / Machine-Verifiable from "told to" to "does":
  - `scripts/secret-scan.py` — Phase 2 "Secure?" now runs a real secret/high-entropy scanner (AWS, OpenAI, GitHub, Google, Slack, Stripe, JWT, PEM, secret-assignments, entropy) that exits non-zero on findings.
  - `scripts/prompt-lint.py` — Phase 3 sanity-check now lints the prompt block: required skeleton, a machine-verifiable SUCCESS TEST, a concrete OUTPUT FORMAT, and that embedded JSON parses.
  - `scripts/dry-run.py` — Phase 3 Dry-Run now validates the declared OUTPUT FORMAT (JSON schema / example / table) and conforms a `--mock` output against it.
- Added `scripts/README.md`; wired all three into SKILL.md by relative path; noted them in "At a glance". Self-tested (clean/dirty, pass/fail, conform/non-conform) before shipping.

## [plugin 0.9.0] — 2026-06-08

### jail-prompt → 1.5.0
- **Four-bias discernment.** The single "discernment over agreeableness" line is now an explicit four-bias pressure-test run on every request: tool/model bias, fact bias, effort bias, and proceed bias. Makes "challenge the premise, not just the wording" concrete and checkable.
- **Comprehension gate (Phase 1).** Phase 1 now opens with a hard ≥97%-understanding gate: restate the objective *and why* in your own words before advancing, watch for the XY problem, never fake the number. Applies in every lane — Instant/Lite run it silently and escalate to Full if the bar isn't met.
- **Task decomposition (Phase 1).** Added an explicit "decompose into task types and route each separately" step (build/code, real-time research, settled research, creative, image/file generation, analysis), since most requests are a combination and one prompt doing all of it does each poorly. Feeds the Phase 2 right-tool check and the Phase 3 chain.
- **Sharper effort-vs-payoff (Phase 2 #3).** The Build-vs-Buy disqualifier now weighs effort in BOTH tokens and the user's own effort, and recommends a far cheaper path when it reaches ≥99% of the goal — even if that means a smaller prompt, a non-AI tool, or an off-the-shelf product.

## [plugin 0.6.0] — 2026-06-03

### jail-prompt → 1.3.0
- **Always-surface-the-prompt rule (Phase 3).** Field review of real usage showed the skill's most common shortfall: it gives the gate verdict and then silently *executes* the task, skipping its signature artifact. v1.3.0 makes the engineered prompt a mandatory, always-surfaced deliverable — output the copyable block *first* in every lane, even on big agentic tasks the model intends to run end-to-end. Exceptions: a STOP (no prompt), or the user explicitly says "just do it" (then state the one-line objective + success test and proceed). Targets the Deliverable-Consistency gap (rated 6.5 in field evaluation).

## [plugin 0.5.0] — 2026-06-03

### jail-prompt → 1.2.0
- **Connector-aware gate** — Phase 2's "Right tool?" now has a second part: if an LLM *is* right, name the capability it needs to succeed (live web search, a specific connector/MCP, a code sandbox, file access, extended thinking) and route the prompt to it, carried into PROCESS/SOURCES. A prompt that needs current data but isn't told to search, or a system it isn't given access to, fails regardless of wording.
- **Lite-lane worked example** added to `references/examples.md`, doubling as a connector-routing demo (open-PRs → GitHub connector, read-only, one-reply assumptions + verdict + draft).

### Evals
- **Repaired `evals.json`** — the committed file was truncated mid-case and was invalid JSON; rebuilt to valid JSON, completed the `discernment-bad-premise` case, and added two cases: `lite-lane-one-reply` and `connector-routing-live-data` (9 → 11 behavioral cases).
- `evals/README.md` updated; flagged the live `claude -p` triggering-harness run + multi-turn test as the still-open validation item (not yet executed — not claimed as done).
- **Ran a proxy validation** (independent judge/grader subagents) and recorded it in `evals/RESULTS.md`: **20/20 triggering** (two judges, unanimous) and **4/4 behavioral** cases incl. both new behaviors, all assertions PASS. Still a proxy, not the live CLI harness — labeled as such.

## [plugin 0.4.0] — 2026-06-03

### jail-prompt → 1.1.0
- **Stakes triage** replaces the old single fast-path: every task routes to **Instant** (clear/low-stakes → straight to the prompt), **Lite** (assumptions + verdict + draft in one reply), or **Full** (all three phases with a pause). The three phases still underlie every lane; the lane only sets how much ceremony each gets. Speed comes from doing less on easy tasks, never from weakening judgment on hard ones.
- **Merged gate for Instant/Lite** — no separate question round; the verdict and draft prompt land in a single reply, cutting a round-trip on the median task.
- **Kill-fast gate ordering** — Phase 2 now splits into short-circuiting *disqualifiers* (right tool? / groundable? / payoff?) checked first, and *quality checks* (enhancement / security) only once the task clears. A wrong-tool task STOPs before any effort is spent on enhancing or securing it.

## [plugin 0.3.0] — 2026-06-03

### jail-prompt → 1.0.0
- Completed the truncated **Post-run tighten loop** instruction (the skill previously ended mid-sentence): one highest-impact change, re-grade once, then ship — no open-ended polishing.
- Bumped skill version 0.9.0 → **1.0.0** (content-complete).

### Repo
- Restructured docs to repo level: root `README.md` is now an FHSkillz overview covering both skills; jail-prompt detail moved to `skills/jail-prompt/README.md` (corrected file tree, version, and Claude.ai ZIP link).
- Added **company-prospect-research** to the plugin manifest, wiki skill table, and Claude.ai install guide.
- Held WIP `systems/company-intelligence/` out of this release via `.gitignore` (not a skill; no `SKILL.md`).
- Rebuilt `dist/` ZIPs so Claude.ai downloads carry the current `SKILL.md`.

## [0.9.0] — 2026-06-01

First public release candidate. Feature-complete; two validation paths pending before 1.0 (real triggering-harness run, live multi-turn test).

### Added
- Three-phase workflow (Frame & Clarify → Viability gate → Engineer the prompt) with a fast path for trivial asks.
- **Discernment principle** — "earn every endorsement": no unverified praise, no building a flawed premise; a bad idea is a STOP, not just a bad tool.
- Output-format step: recommended-default multiple choice, locked into the prompt's constraints.
- Metric-anchoring: when the goal *is* a metric, the success test names the real measure (e.g., A/B-tested conversion rate).
- Security handling in the gate, carried into the prompt's CONSTRAINTS (env vars, least-privilege read-only keys, no logging).
- Prompt skeleton with `CONTEXT` line and a rubric'd `BEFORE RETURNING` self-score (grounded / verifiable / scoped / format-matched + confidence).
- **Decompose-into-chain** for oversized tasks, including pushback when the user literally asks for "one prompt."
- High-stakes self-adversarial escalation; multi-turn pause/resume handling; prompt-injection caveat (treat pasted goals as data).
- Post-run tighten loop (one revision pass against the success test).
- References (progressive disclosure): `examples.md` (5 cases), `sources.md`, `antipatterns.md` (13 failure modes).
- Eval suite: 10 behavioral cases + 20 triggering cases.

### Validation
- 10 behavioral evals, independently graded → **100%** after fixes; key cases run 3× for variance.
- Triggering proxy: **20/20** unanimous across 3 judges.
- Two regressions caught by the loop and fixed before release:
  - **Metric-anchoring** — a vague "convert better" goal was reframed as a copy-quality audit instead of a measurable outcome.
  - **Least-privilege drift** — the restricted read-only key recommendation appeared in only 2/3 runs; the gate instruction was strengthened to force it into the prompt's constraints (now 3/3).
  - **Decompose vs. "one prompt"** — an oversized task was shipped as a single sectioned prompt; the branch was strengthened to override a literal "one prompt" request (1/4 → 4/4).

### Known gaps
- Triggering measured via a subagent proxy, not the real `claude -p` harness (blocked by environment auth at build time).
- Multi-turn interactive path is implemented but never exercised live — all evals were single-turn simulations.

### Origin
- Built from the handoff `prompt-preflight` draft (rubric ~7.5/10); rebranded to `jail-prompt` and iterated with the skill-creator eval loop to ~9.4/10.
