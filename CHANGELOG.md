# Changelog

All notable changes to the FHSkillz repo and its skills. Format follows [Keep a Changelog](https://keepachangelog.com/); versioning is [SemVer](https://semver.org/). Per-skill versions live in each `SKILL.md`; the plugin version lives in `marketplace.json`.

## [plugin 0.23.1] — 2026-07-22

**Wave 2b: behavioral executor — first measured behavioral run, 76/76 assertions PASS.** No skill content changed; evidence-only release.

- 23 cases via producer/grader split (producers blind to assertions; 5 independent adversarial graders, quoted evidence mandatory): kernel 8 required types 25/25 · jail-rate 14/14 (live-research hardware rating, private subject, people-boundary decline, ≤4.0 critical-flaw cap) · jail-council 7/7 (honest Tier-C full protocol + evidence-beats-votes chairman) · mp-wave 12/12 (incl. grep-verified secret redaction) · wave-2 lanes 18/18 (full sweep, mini-council invariants, debrief no-guess, FYI refusal, profile diff).
- Deferred honestly: integration chains i1/i2 + jail-prompt behavioral re-run (queued, 0.24); chain i3 credited live-fire only.
- New: evals/results/2026-07-22-wave2b-behavioral/ (summary + all 23 producer outputs) · behavioral-pass-ledger.jsonl entry #0.

## [plugin 0.23.0] — 2026-07-22

**Wave 2: the 8.5 enhancement program.** 19 skills enhanced, 4 merged into 2 (29 → 27), re-baselined and re-rated with evidence. Suite mean value 8.15 → 8.50; 18/27 at ≥ 8.5 (honest remainder documented).

### Consolidations
- **jail-strategy-scan 1.0.0** = jail-swot + jail-pestle: INTERNAL (SWOT→TOWS) / MACRO (PESTLE+tripwires) / FULL SWEEP lanes off ONE evidence sweep, with the cross-lane interaction pass; tripwires hand to jail-memory. Legacy keywords route to it (measured: w1–w3, k14/k15).
- **jail-py-toolkit 1.0.0** = jail-py-prompt-tools + jail-py-rate-tools: 9 scripts, two check families, one install; release validator now runs its checks every release.

### Enhancements (19 skills, per-skill changelogs have detail)
task-contract 1.2.0 (type presets) · research 1.1.0 (claim-class routing + freshness windows + live-search detection) · decide 1.1.0 (quantified lane + council escalation + quantified-comparison triggers) · council 1.1.0 (MINI-COUNCIL lane) · approval-gate 1.1.0 (standing profile) · quarantine 1.1.0 (INLINE SCAN + protected-class table) · red-team 1.1.0 (falsifier-first + PRE-MORTEM-LITE) · prospect 1.3.0 (COMPANY SNAPSHOT) · baton 1.1.0 (proactive offer + shared ledger shape) · orchestrate 1.2.0 (SOLO lane) · memory 1.2.0 (file-ledger fallback) · cpr 1.2.0 (DEBRIEF lane) · prototype 1.1.0 (spike ledger) · exec-brief 1.1.0 (decision-forcing mandate + audience table) · rate-skill 2.2.0 (measured-evidence rule) · skill-miner 1.2.0 (continuous self-maintenance mode) · py-lab 1.1.0 (lab-compare.py regression gate) · bmc 1.2.0 (lab-shaped experiments + canvas-delta mode) · wayfind 1.1.0 (map-as-baton-spine + ADRs at resolution).

### Measured (wave-2 trigger baseline, blind judges)
95 cases · fire 79/79 (100%) · false-fire 0/16 (0%) · collision variance 36/36. One fix-loop pass: wn1 (quantified comparison) missed pre-fix (98.7%) → jail-decide description fix → blind re-judge with 4/4 regression holds; wn1 retained as the regression case. Ledger entries #1–#2; evidence in evals/results/2026-07-22-wave2-baseline/.

### Re-rate
docs/skill-catalog.md rewritten at 0.23.0 with per-skill evidence for every score move (determinism rule: untouched skills unmoved). docs/wave2-scorecard.md is the release gate summary.

## [plugin 0.22.0] — 2026-07-22

**Wave 1: trigger baseline measured — gate PASS.** First real (non-proxy-claimed) run of the full trigger surface under the enhancement-metrics contract; no skill content changed.

### Added
- **scripts/run-trigger-evals.py** — model-agnostic blind trigger-eval harness: `manifest` emits label-free judging batches (29 descriptions + queries; scoring key isolated in `private/`), `score` computes fire/false-fire vs the ≥95%/≤5% gate and exits pass/fail. Repo infrastructure, not skill content.
- **evals/trigger-accept-map.json** — accept-sets + fire/nofire kind for all 80 trigger cases across 5 suites; designed-ambiguity alternates encoded explicitly; behavioral suites excluded via `_exclude_files` (Wave 1b).
- **evals/results/2026-07-22-trigger-baseline/** — evidence bundle: baseline-report.json, all 80 picks, collision variance (3 independent judgments), RUN.md methodology incl. the 3 disclosed alternate-accept passes.
- **evals/results/trigger-accuracy-ledger.jsonl** — jail-py-lab ledger entry #0 (baseline 100.0) so future description edits measure against a number.
- **docs/wave1-scorecard.md** — gate table, scope honesty (what the run proves/doesn't), Wave 1b next.

### Measured
Fire 63/63 (100%) · false-fire 0/17 (0%) · collision-set variance 36/36 picks identical across 3 independent blind judges · per-suite 29/29 kernel, 16/16 rate, 20/20 prompt, 8/8 mp-wave, 7/7 council. Strict-primary scoring: 96.3%/0% — PASS either way. Zero failures → no description fixes this wave; ledger baseline recorded instead.

## [plugin 0.21.0] — 2026-07-19

**Matt Pocock adaptation wave** (github.com/mattpocock/skills, MIT — patterns re-derived under the JAIL constitution; 41 skills reviewed via jail-skill-miner, 8 items approved by Jonathan from the recommended set).

### New kernel skills (4 × 1.0.0)
- **jail-diagnose** — feedback-loop-first diagnosis: red-capable repro signal before any hypothesizing (8 escalating techniques), tighten/minimize/instrument, confirmed-cause fixes, mandatory regression case (matches the enhancement contract's regression rule). Refuses to guess loopless.
- **jail-prototype** — throwaway prototypes answering a named design question; one command, no persistence, state surfaced; the verdict graduates, the artifact dies off-main.
- **jail-baton** — session handoff batons: state with proof pointers, decisions-with-why, reference-don't-duplicate, suggested skills, quarantine-class redaction; sized to the recipient (small-context aware).
- **jail-wayfind** — decision-ticket maps for foggy multi-session work; plan-don't-do; resolve via kernel skills until the way to a named destination clears.

### Deltas into existing skills (5 × 1.1.0)
jail-task-contract (grill mode: one-question-at-a-time exhaustive branch-walk for high stakes + look-up-facts/ask-only-decisions) · jail-verify (two-axis Spec ∥ Standards parallel review + pin-the-fixed-point preflight) · jail-orchestrate (tracer-bullet vertical slices + expand–contract for wide refactors) · jail-memory (ADR entry shape) · jail-skill-miner (invocation economics: context load vs cognitive load, description pruning).

### Not adopted (recorded)
research (duplicate — ours stronger), to-spec/implement/tdd/codebase-design/triage/merge-conflicts et al. (deferred to wave-3 software-build-governor as feeders), teaching/personal/installer skills (out of scope). Plugin: 29 skills; evals/mp-wave-evals.json seeded; 4 fixture smokes PASS (smoke doc addendum).

## [plugin 0.20.0] — 2026-07-19

### jail-council → 1.0.0 (new, kernel) — the LLM-council pattern, accuracy-first
- Blind independent answers (3–5 members) → **anonymized adversarial review** (mandatory error-hunt per answer) → **verification round** on disputed load-bearing facts → **chairman synthesis decided by evidence, never votes**, with dissent register + audit appendix. Pattern inspired by Karpathy's llm-council (concept only — repo has no license; no code reused).
- **Accuracy outranks cost by charter (Jonathan's directive):** cost disclosed, never gating; invoking the skill is the Rule-11 justification.
- Independence tiers A/B/C always declared; **Tier-A cross-provider councils are native in OpenCode CLI** — verified runbook (skills load from ~/.claude/skills; per-agent `model: provider/model-id` in opencode.json) in references/opencode-runbook.md.
- **Proven live:** a real Tier-C council ran as the smoke test (7 subagent executions) — 3/3 members landed the troy/avoirdupois trap, and the review round still caught a material overgeneralization all three reviewers flagged independently. See docs/smoke-tests-0.19.0.md addendum.
- Wired in: escalation hooks in jail-verify, jail-decide, jail-rate, jail-prompt; constitution Layer-1 + skill-graph rows; absorbs the wave-3 `model-validation-council` candidate; eval seeds in evals/jail-council-evals.json. Plugin: 25 skills.

## [plugin 0.19.0] — 2026-07-19

**Unified JAIL naming + full smoke pass.**

### Renamed (folder + frontmatter + every cross-reference; history entries keep old names)
- `rate-skill` → **jail-rate-skill** (2.1.0) · `company-prospect-research` → **jail-prospect** (1.2.0) · `pestle-analysis` → **jail-pestle** (1.1.0) · `swot-analysis` → **jail-swot** (1.1.0) · `business-model-canvas` → **jail-bmc** (1.1.0) · `cpr-agenda-builder` → **jail-cpr** (1.1.0). All 24 skills now carry the jail- prefix. 37 files rewired; `~/.rate-skill/` history path deliberately unchanged (data dir, not a skill name).

### Smoke tests — 24/24 PASS (`docs/smoke-tests-0.19.0.md`)
- One fixture per skill on a shared scenario; jail-py-* entries are real executions (secret-scan detection, prompt-lint pass, validate-rating tamper rejection, lab keep/discard ledger). Six skills pass by correctly refusing/halting/failing (jail-verify FAIL with named observations, jail-quarantine sensitive halt + injection defusal, jail-memory secret refusal, jail-prospect score-without-signal refusal, jail-orchestrate unverified-claim rejection, jail-lab regression discard). Supplied-materials modes used where live research would be required — no fabricated citations.
- Smoke tests are shape + guardrail demonstrations, not the multi-case behavioral evals (still authored-not-run).

## [plugin 0.18.0] — 2026-07-19

**The JAIL OS release** — plugin grows 6 → 24 skills in three governed layers, built by consolidating ~44 candidates (ChatGPT's 16-core + 20 follow-ons, 8 disciplines mined from SharperOS/VanguardOS, karpathy/autoresearch) down to what survived dedup against the existing six.

### New — Layer 1 reasoning kernel (12 × v1.0.0)
jail-task-contract · jail-research · jail-verify · jail-decide · jail-red-team · jail-orchestrate · jail-approval-gate · jail-quarantine · jail-memory · jail-lab · jail-skill-miner (+ jail-prompt, already shipped). Lean, small-context-first, code-free, each ending in the JAIL-HANDOFF block, each with negative-trigger routing and a Gotchas section.

### New — workflow + frameworks + companion
jail-operationalize (13-field operating workflows) · jail-exec-brief (executive synthesis + technical translation) · pestle-analysis · swot-analysis · business-model-canvas · cpr-agenda-builder (each chains the kernel by name with inline fallbacks) · **jail-py-lab** (runnable experiment-ledger harness for jail-lab, 9/9 self-tests green; keep/discard/tie verdicts, direction lock, metric-cmd parsing).

### System
- **docs/JAIL-CONSTITUTION.md** — 12 rules binding every skill + the JAIL-HANDOFF contract.
- **docs/skill-graph.md** — routing registry: consumes/produces, may-invoke/invoked-by, data sensitivity, failure behavior, forbidden patterns (cycles, unbounded recursion, duplicate research, silent overrides, approval laundering).
- **docs/ROADMAP-wave3-domain-packs.md** — 17 staged domain skills with the entry bar (4-box filter, dedup, rate-skill ≥8.0).
- **evals/** — kernel-trigger-evals.json (17 + 12 collision near-misses) and kernel-evals.json (8 required case types + 3 integration chains). Authored, not yet run.
- jail-prompt auto-triage now names the kernel; jail-rate claim labels reference the constitution taxonomy; CLAUDE.md carries the constitution/graph/small-context conventions.
- Attribution: jail-lab / jail-py-lab pattern adapted from Andrej Karpathy's autoresearch (MIT).

## [plugin 0.17.0] — 2026-07-19

The **code-free core** release: every core skill is now instruction-only; all runnable code lives in dedicated JAIL-PY companion skills. Plugin grows from 4 to 6 skills.

### jail-rate → 2.0.0 (universal rebuild)
- Rates **anything** — software, codebases, hardware, people (professional/public roles only), ideas, programs, services, businesses, content — not just software. Classifies the subject first; the rubric must match the type.
- New `references/rubric-library.md`: 8 built-in weighted rubrics (weights + per-dimension evidence sources + rationale) and a meta-procedure for deriving a declared rubric for any other type. The rubric is always shown before the scores.
- New `references/evidence-standards.md`: live research by default, tiered sources, URL + date-accessed citations, Fact/Inference/Judgment labeling, ≥2-independent-sources target per dimension, confidence rules, private-subject handling. Marketing claims are not evidence.
- Hard people-rating boundaries; handoffs to rate-skill (AI skills) and company-prospect-research (prospect decisions).

### jail-py-prompt-tools → 1.0.0 (new) · jail-py-rate-tools → 1.0.0 (new)
- JAIL-PY companion skills receiving, unchanged, the Python previously bundled inside jail-prompt (secret-scan, prompt-lint, chain-lint, truth-lint, dry-run) and rate-skill (validate-rating, save-rating, variance-check, validate-skill-structure). Optional installs; the core skills document manual fallbacks.

### jail-prompt → 2.0.0 · rate-skill → 2.0.0
- Instruction-only cores. Every checkpoint that ran a bundled script now names the companion-skill run *and* a manual fallback. rate-skill's duplicated history paragraph fixed. `validate-skills.py` promoted to repo `scripts/` (maintenance tooling); repo-level `scripts/pre-commit-hook.sh` replaces the per-skill hooks.

### company-prospect-research → 1.1.0
- Added `metadata.version`, a Gotchas section (entity collisions, stale signals, headcount inflation, score-without-signal, size-band ≠ valuation, ability-to-pay), Related-skills pointers, and a README.

### Repo
- Every skill now has a README + CHANGELOG; root README/wiki updated to all 6 skills (dead `dist/` links removed).
- Legacy/design docs (HANDOFF, FHSkillz-Setup, Enhancement-Audit, AI-Control-Surface ×2, FH-AI-OS reference) moved to `docs/`.
- CLAUDE.md: code-free-core convention + validator added to pre-commit CHECKS.

## [plugins 0.12.0–0.16.0] — 2026-06-14 → 2026-06-26 (backfill)

Root changelog was not updated during this span; the detail lives in the per-skill changelogs. Summary: **jail-prompt 1.7.0** (standardized METADATA keys, output sanitization + malicious-sample success test, determinism self-test), **1.8.0** (chain manifests + chain-lint, self-critique pass, portable meta-prompt), **1.9.0** (schema-based truth-tagging + truth-lint, external/second-model verification, VERIFICATION PLAN line, per-mode generation settings), **1.9.1** (validator false-positive fix); **rate-skill 1.3.0** (variance-check, skill-creator handoff), **1.4.0** (summarizer guide, structure validator, scan-target-scripts rule, history fallback path).

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
