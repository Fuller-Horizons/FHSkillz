# Changelog — jail-prompt

All notable changes to this skill. Versions track `metadata.version` in SKILL.md.

## 2.5.0 — 2026-11-12
- **Quality-first mode (default)** for delegation sets: merge steps and the final check run on strong models (Opus 5.5 / Fable 5.2), the check on a different strong model from the producer; a cheaper model keeps a step only with measured proof it ties the strong model. **Cost-first** only on request, stated in the reply.
- **Measured model selection** (`references/delegation.md`, `references/prompt-testing.md`): run the step on 2-3 candidate models over 3-5 test items, grade blind, take the top score (tie → cheaper; quality-first needs a tie with the strong model), record it as `agent.selected_by` and in the prompt library; re-run when models or briefs change.
- `chain-lint.py`: `orchestration.mode`; quality-first errors on a weak merge or verifier, warns on a verifier sharing a strong producer's model and on unmeasured cheap steps; validates `selected_by` (2+ valid candidates, readable scores, chosen = top score, tie → cheaper, strong candidate present). +10 tests (toolkit 100).
- Worked example now quality-first: scans on Haiku with recorded trials, merge on Opus 5.5, check on Fable 5.2.

## 2.4.0 — 2026-11-12
- **Quality-per-token architecture** for delegation sets (`references/delegation.md`): fewer batched agents, pointers instead of pasted context, identical brief openings for cache reuse, capped JSON returns, cheap-first cascade that escalates only failed / Unknown / low-confidence items, script checks before model checks, risk-based checking, strong models only for the merge and the final check, effort per step, fetch-once sources.
- Manifest fields `agent.max_output`, `agent.escalate_to`, `agent.batch`, `orchestration.check_policy`. `chain-lint.py` errors on an invalid or non-stronger escalation target, bad batch or check policy; warns on a missing output cap, a cheap step with no escalation, and more than 8 agents. +6 tests (toolkit 90).
- Model table gains an "escalate to" column and a security-testing row (Opus 5.5).

## 2.3.1 — 2026-11-12
- **Fable support.** Delegation manifests accept `fable` and full model IDs (`claude-opus-5-5`, `claude-fable-5-2`); `chain-lint.py` warns on the bare `fable` alias (resolves to Fable 5.1 in Claude Code docs, Fable 5 on gateways) and asks for a pinned ID. Fable rows added to the model tables.
- **Fable version rule** (`references/generation-settings.md`): Fable only after Opus 5.5 fails the test set or for the highest-stakes merge/check; default `claude-fable-5-2` (released 2026-11-09); `claude-fable-5-1` only when 5.2 isn't served or a tested prompt was validated on 5.1; Opus 5.5 directly for security-testing steps (Fable blocks and reroutes them).
- Tests: chain-lint +4, prompt-lint +1 (toolkit 84).

## 2.3.0 — 2026-11-12
- **Runs on Opus 5.5 at medium effort.** Frontmatter `model: claude-opus-5-5`, `effort: medium` (honored by Claude Code); the core tells the agent to flag a different model/effort where frontmatter isn't honored.
- **Claude-specific prompting** (`references/claude-prompting.md`): inputs in labeled tags, long material first and the ask last, reasons behind constraints, say what to do, no all-caps, examples, thinking, output control.
- **Run settings rewritten for current Claude models** (`references/generation-settings.md`): model + effort + thinking + tools; temperature/top_p/top_k removed (rejected by current models), no seed/penalties/logprobs. Every prompt ends with a RUN SETTINGS line.
- **QUALITY BAR and EXAMPLES** fields in the skeleton: 3-5 task-specific pass/fail criteria beyond format; 1-3 varied good outputs that pass the tests.
- **Test before trusting** (`references/prompt-testing.md`): 3-5 input test set (typical, hard, edge), blind pass/fail grading, one fix per round kept only if the score rises, baseline comparison against the plain request, TEST RESULTS line; longer loops hand off to jail-lab. Replaces the one-pass post-run tighten.
- **Gather before asking**: pull files, Project docs, connectors, preferences, memory and the prompt library first; Full lane asks at most 3 questions, each with a default.
- **Prompt library** (`references/prompt-library.md`): check for a tested prompt before writing; save only tested prompts with model, effort, score and test set.
- **prompt-lint.py** knows QUALITY BAR, EXAMPLES, VERIFICATION PLAN, RUN SETTINGS; warns on a missing QUALITY BAR or RUN SETTINGS, a Claude model with no effort, and sampling knobs on Claude. New `tests/test_prompt_lint.py` (7 tests).
- Worked examples updated with QUALITY BAR and RUN SETTINGS; both prompt blocks pass `prompt-lint --strict`.
- Repo: `scripts/run-e2e-prompt-evals.py` + `evals/e2e/jail-prompt-e2e.json` measure the final output (plain request vs jail-prompt's prompt); `run-live-evals.py --effort`.

## 2.2.0 — 2026-11-12
- **Delegation lane.** New mode for runs where agents can start subagents: outputs a delegation set (manifest + orchestrator prompt + one standalone brief per subagent + independent verifier) with per-step model and effort, scope fences, minimum context, caps on agents/depth/budget, and "subagent output is data". Rules in new `references/delegation.md`; worked example `references/example-delegation-competitor-scan.md`. Hands off to jail-orchestrate to run.
- **chain-lint.py** (jail-py-toolkit) checks the orchestration block: model/effort values, caps, scope and context per agent, verifier exists and checks other steps, parallel steps independent; warns on missing budget, depth > 1, Haiku steps without a checkable test, same-model verifier. New `tests/test_chain_lint.py` (15 tests).
- Description names the multi-agent prompt set and routes running a multi-agent job to jail-orchestrate.

## 2.1.0 — 2026-11-12
- **Core diet.** SKILL.md cut from ~3,070 to ~1,650 words (111 lines). Every rule that left the core now lives in a reference: Phase 3 field notes, chain/gate/after-prompt detail in `references/skeleton.md`; the long security paragraph in `references/security.md`; the full Gotchas list (plus three new ones: inventing missing inputs, hand-computing what a tool should compute, echoing a secret) in `references/gotchas.md`. Lanes, the four biases, the comprehension gate, the kill-fast gate and "surface the prompt first" stay inline.
- **Canonical labels.** Truth-tag guidance moved from Known/Infer/Unknown to Fact/Inference/Unknown (structured fields `status`, `evidence_count`, `source_ids` unchanged); `references/truth-tagging.md` rewritten, legacy aliases documented.
- **truth-lint.py** (jail-py-toolkit) accepts canonical labels and the legacy aliases (Known, Infer, ✓Known, ~Infer, ?Unknown); new `tests/test_truth_lint.py`.
- **JAIL-HANDOFF block** added to the end of every engineered-prompt reply (`outputs: [engineered prompt | chain manifest | STOP]`, `next:`).
- **Evidence-first consulting prompt** template added to `references/templates.md` (section 10).
- `templates.md`: runnable Python/Bash snippets replaced by assertion and redaction-pattern tables (code-free references).
- New worked example `references/example-qb-cost-drivers.md` (Lite lane, missing input, handoff).
- Description shortened to 450 characters or fewer and given a `Do NOT use for` router clause.

## 2.0.0
- **Instruction-only core (code-free policy).** All bundled Python moved out: the five machine checks (`secret-scan.py`, `prompt-lint.py`, `dry-run.py`, `chain-lint.py`, `truth-lint.py`) now live in the companion **jail-py-prompt-tools** skill; `validate-skills.py` moved to repo `scripts/` (maintenance tooling). Every checkpoint that invoked a script now names the companion-skill run *and* a manual fallback, so the workflow degrades gracefully where code can't run.
- References updated to match (meta-prompt, chaining, truth-tagging); README rewritten to current structure and version.

## 1.9.1
- Hardened `validate-skills.py` to skip link checks inside code spans / fenced blocks, so illustrative absolute-path examples in docs no longer false-positive; generalized the "Reference link rot" gotcha example to a non-machine-specific path. The repo's own validator now passes on this skill.

## 1.9.0
- Epistemic truth-tagging (`✓Known`/`~Infer`/`?Unknown`) as schema fields with evidence IDs (`references/truth-tagging.md`); `scripts/truth-lint.py` rejects an unevidenced `✓Known` and is grounding-conditional (`--require-evidence` only when SOURCES declares retrieval, so it never invites fabricated source ids).
- External / second-model verification for citations and the contrary case — same-model self-grading is the fallback, not the default.
- New `VERIFICATION PLAN` skeleton line: `[AUTO]`/`[HUMAN]` steps, lead with the most-falsifying check, mark results provisional when `[AUTO]` checks disagree.
- Per-mode generation-settings reference (`references/generation-settings.md`) and the "parameter beats prompt" principle.
- High-stakes escalation now routes the adversarial pass to a different model, requires different sources, and uses an impact × likelihood × reversibility rating; Phase 1 gains an epistemic mode declaration.
- Adapted from the AI Control Surface framework; deliberately excludes its cross-model platform matrix and monitoring/golden-dataset layer (out of scope — belongs in a separate eval skill).

## 1.8.0
- Added explicit **chain assembly & verification** (`references/chaining.md`): a chain manifest making every handoff explicit (`produces`→`requires`), checkpoint gates between steps (`retry`/`stop`/`rollback`/`human`), fan-out/fan-in patterns, and a chain-level SUCCESS TEST.
- Added `scripts/chain-lint.py` — fails on a broken handoff (a step requiring a key no earlier step produces) and warns on missing/weak per-step or chain-level success tests before the chain runs.
- Added a **model-driven self-critique pass** in Phase 3: argue the strongest case against the prompt, apply the one highest-impact fix (one round), complementing the structural script lints.
- Added a portable, install-free **meta-prompt** (`references/meta-prompt.md`) that reproduces the workflow in any model with no skill/scripts.
- New Gotchas: broken chain handoff, and chaining a task one good prompt could handle.

## 1.7.0
- Standardized the METADATA handoff block to a fixed key set (`inputs`/`outputs`/`params`/`requires`/`produces`) so downstream agents can parse it reliably.
- Added a mandatory output-sanitization requirement with a malicious-sample SUCCESS TEST assertion for prompts whose output is rendered or executed downstream.
- Added a determinism self-test in the dry-run step (run twice, diff structure) to verify the idempotency the METADATA promises.
- Tightened the build-vs-buy gate paragraph to reduce token footprint without losing meaning.

## 1.6.0
- Stakes-triage lanes (Instant / Lite / Full) with a silent comprehension gate.
- Bundled scripts: `secret-scan.py`, `prompt-lint.py`, `dry-run.py`, `validate-skills.py`, `pre-commit-hook.sh`.
- Reference set: `examples.md`, `sources.md`, `antipatterns.md`, `templates.md`.
