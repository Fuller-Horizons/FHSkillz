# FHSkillz — Gap + Enhancement Report

*Audit of the FHSkillz library against the SHARPER-OS Enhancement Audit Brief (Part 1 skill-craft + Part 2 14 frameworks). Generated 2026-06-08.*

> **Adoption gate.** Everything below is an **option for Jonathan to approve**, not a change made. Nothing has been edited. The 14 frameworks are *Under Evaluation* in the Knowledge — Thinking Tools DB and are not authoritative until explicitly adopted.

---

## 0. Scope note + one correctness flag

- **Library is small and high-quality.** Only **3 skills** are registered (`marketplace.json` v0.8.0): `company-prospect-research`, `jail-prompt`, `rate-skill`. All three are listed correctly; `strict:false` is set. No invariant violations found.
- **9-category taxonomy caveat.** The brief asks for classification into "the 9 categories," but that list is not enumerated in the brief — it lives in the SHARPER-OS Knowledge DB. Categories below are **functional placeholders**; confirm against the canonical 9 before treating them as final.
- **✅ Resolved — "truncation" was a sandbox artifact, not a repo defect.** Initial reading via the Linux sandbox mirror showed `rate-skill/SKILL.md` truncated at 38 lines (ending mid-table at `…| Post R`). On follow-up the **authoritative host file is complete — 76 lines, full Output Format + IDE/CLI matrices + a Gotchas section** — and matches the committed version. The sandbox mirror was frozen/out-of-sync this session, so it can't be trusted for this file; no repair to the real file was needed (it was re-verified and re-asserted to the known-good content). *Implication: the rate-skill notes below are corrected to reflect the complete file.*

---

## 1. Inventory

| Skill | One-line purpose | Functional category | Version |
|---|---|---|---|
| **company-prospect-research** | Free-sources-only brief scoring a US private company as a sell-side + consulting prospect | Research / analysis generator | *(none in frontmatter)* |
| **jail-prompt** | Pre-flight workflow that triages a vague goal and turns it into a verifiable, lean prompt — or a STOP | Meta / prompt-engineering router | 1.4.0 |
| **rate-skill** | Deterministic 10-category scoring of any skill directory, with validated JSON record + history | Evaluator / QA grader | 1.2.0 |

Maturity at a glance: **jail-prompt** is a near-reference implementation; **rate-skill** is strong (config, memory, gotchas, injection defense) but has no eval set; **company-prospect-research** is well-disciplined on grounding but has no scripts, gotchas, evals, or memory.

---

## 2. Per-skill assessment

### company-prospect-research — Research / analysis generator

**Already has**
- Description written as a router with literal triggers (Part 1 #1). ✅
- Rigorous evidence labeling — Fact / Source-Backed Inference / Analyst Judgment / Missing Evidence (serves Part 2 #5 spirit + #14 uncertainty permission). ✅
- Hard guardrails: free-sources-only, "no fabricated financials, ever," cite-or-omit, owner-privacy. ✅
- 4-stage chain with copy-paste prompts in `prompts/prompt-chain.md` (Part 2 #2 pipeline + Part 1 #3 progressive disclosure). ✅
- References/assets split (`free-sources.md`, `scoring-rubric.md`, `brief-template.md`) — main file stays light. ✅
- Self-check + confidence %, four allowed recommendation values incl. "need more" (Part 2 #14). ✅

**Could adopt**
- **Gotchas section** (Part 1 #2) — *quick win.* No accumulated-failure-points block. Capture real traps: wrong legal entity vs. DBA, common-name collisions in SoS/USAspending, stale reviews/news, headcount inflation from LinkedIn. Add a short `## Gotchas` or `references/gotchas.md`.
- **Deterministic helper script** (Part 1 #5) — *medium.* The size-band triangulation (headcount × industry rev/employee) and the two 0–100 score aggregations are repeatable math currently done in-head each run. A `scripts/score.py` would cut tokens and remove arithmetic drift.
- **Separate Doer from Judge** (Part 2 #5) — *medium, gated to high-value targets.* The brief can drive a real outreach/money decision but self-grades. Optional skeptical pass: a separate verifier asks "what single fact, if wrong, flips this recommendation?" before delivery. Pairs naturally with `rate-skill` infrastructure.
- **Tiny eval set** (Part 2 #12) — *larger rework, high value.* No evals. Author 15–30 cases from real targets: known company → expected pursue/pass + must-cite signals; grade grounding and no-fabrication, not phrasing.
- **Config + memory** (Part 1 #6/#8) — *quick–medium.* Store Jonathan's standing context (target industries, geography, pursue thresholds, outreach tone) in `config.json`; `AskUserQuestion` when missing. Append-only run log lets it stay consistent across a list.
- **Frontmatter version** — *trivial consistency.* The other two skills carry `metadata.version`; this one doesn't.

---

### jail-prompt — Meta / prompt-engineering router

**Already has** (the most framework-complete skill in the library)
- Description = trigger, **including negative triggers** ("do not trigger for…") (Part 1 #1). ✅
- Gotchas via `references/antipatterns.md`, sanity-checked in Phase 3 (Part 1 #2 + Part 2 #3 generate-and-filter). ✅
- Anti-railroading by design — Instant / Lite / Full stakes lanes (Part 1 #7). ✅
- Progressive disclosure across 4 reference files (Part 1 #3, Part 2 #4). ✅
- Scripts: `validate-skills.py`, `pre-commit-hook.sh` (Part 1 #5). ✅
- Delegatable-task / right-tool gate, incl. auto-triage to other installed skills + MCP binding (Part 2 #7, #8, #9). ✅
- Adversarial pass for high-stakes/contested tasks (Part 2 #3). ✅
- Eval-driven: 11 behavioral + 20 triggering cases, results tracked (Part 2 #12). ✅
- Prompt-engineering core habits baked into the Phase 3 skeleton — explicit, intent, self-score, uncertainty (Part 2 #14). ✅

**Could adopt**
- **Close the live-harness eval gap** (Part 2 #12) — *medium.* `evals/RESULTS.md` flags an open item: results are **subagent-proxy**, not the live `claude -p` harness, and behavioral runs were single-turn. The enhancement isn't more evals — it's running the existing set on the real harness so "proxy" can be upgraded to "harness-verified."
- **"What can I stop doing?"** (Part 2 #6) — *medium, context win.* SKILL.md is dense and carries heavyweight scaffolding (Dry Run Sandbox verification, save-to-`prompts.json`, full METADATA skeleton). Some of this fights the lightweight intent for median tasks. Move the heaviest mechanics into a reference loaded only on high-stakes lanes.
- **Doer/Judge separation for its own output** (Part 2 #5) — *medium, gated.* The Phase-3 adversarial pass is still self-grading. For consequential prompts it could hand the draft to a *separate* verifier subagent (or `rate-skill`) rather than introspecting.
- **Memory log** (Part 1 #6) — *optional.* An append-only log of STOP reasons / gate verdicts would let it surface recurring bad-fit patterns over time.

*Net: this skill is mostly polish, not gaps.*

---

### rate-skill — Evaluator / QA grader

**Already has**
- Description = trigger incl. slash-command form (Part 1 #1). ✅
- **Treats the target as untrusted data** — injection-attempt detection, obey-nothing, cap Safety category at 4.0 (Part 2 #5 doer/judge + #14). Strong. ✅
- Deterministic scoring at temperature 0.0 with rubric anchors (Part 2 #3 reproducibility). ✅
- Think-through-setup via `config.json` + `AskUserQuestion` fallback (Part 1 #8). ✅
- **Memory built in**: `save-rating.py` stores history and reports deltas across re-rates (Part 1 #6). ✅
- Scripts validate + persist the JSON record (Part 1 #5). ✅
- Progressive disclosure — rubric/examples loaded on demand (Part 1 #3). ✅
- Batch mode with roll-up (Part 2 #2). ✅
- **Gotchas section already present** (Part 1 #2) — 7 grader-specific failure modes incl. obeying the target, rating-from-name, score drift, false precision (corrected after reading the full file). ✅

**Could adopt**
- **Eval the rater itself** (Part 2 #12) — *medium, high value.* A grader with no eval can't defend its determinism claim. Hold a few gold-standard rated skills (one known-good, one known-weak, one injection-laden) and assert the rater reproduces scores within tolerance.
- **Tournament mode** (Part 2 #3) — *optional, gated.* For "pick the best of N similar skills," pairwise comparison can beat absolute scoring. Additive to current batch mode.
- **Advisor tiering** (Part 2 #10) — *optional.* Cheap model fills the matrix cells; escalate to a frontier model only for rationale + recommendation.

---

## 3. Missing skills the captured knowledge suggests

| Suggested skill | Why (which framework) | Notes |
|---|---|---|
| **adversarial-review / verifier** | Part 2 #5 (separate Doer from Judge), #3 (adversarial verification) | A standalone skeptical second-pass any high-stakes skill can delegate to. `rate-skill` judges *skills*; this would judge *outputs* (a brief, a prompt, a doc) against explicit criteria. Highest-leverage gap. |
| **eval-runner** | Part 2 #12 (eval-driven development) | jail-prompt's eval loop is hand-rolled in `scripts/` + `evals/`. Generalize it into a reusable skill: author 20–50 cases, grade outcome-not-path, track variance. Would let every other skill earn an eval cheaply. |
| **skill-author / skill-upgrader** | Part 1 (all) + Part 2 #1 (9-category design) | You consume Anthropic's `skill-creator`; a FHSkillz-native authoring skill could bake in your invariants (folder==name, description-as-router, gotchas, scripts) and the 9-category classifier so new skills are born compliant. |
| **delegation-triage** | Part 2 #7 (Five Ingredients of a Delegatable Task) | A lightweight "should this even be a skill / a Project / an MCP / a human task?" router. Partly lives inside jail-prompt Phase 2; could be its own pre-flight. |

---

## 4. Top 5 highest-leverage upgrades (ranked)

1. **Add an `adversarial-review` / verifier skill.** *Larger, highest strategic value.* Directly serves the doer/judge guardrail and unblocks Part 2 #5 for *every* skill (prospect briefs, jail-prompt outputs) without each re-implementing it.
2. **Give `company-prospect-research` an eval set + no-fabrication assertion.** *Medium–large, high value.* It's the most money-adjacent skill and the only mature one with zero evals; ungrounded grounding-claims are the biggest exposure.
3. **Close jail-prompt's live-harness eval gap.** *Medium.* Turn the flagged subagent-proxy results into harness-verified ones; cheap credibility on your flagship skill.
4. **Eval the rater itself (`rate-skill`).** *Medium, high value.* The grader has no eval; gold-standard fixtures (known-good / known-weak / injection-laden) would let it defend its determinism claim.
5. **Add a `## Gotchas` block to `company-prospect-research`** — *quick win.* It's now the only skill lacking one (jail-prompt has `antipatterns.md`; rate-skill has Gotchas). Highest-signal-per-line content per Part 1 #2.

---

## 5. Cross-library quick wins (each ≤ a few minutes)

- Add `metadata.version` to `company-prospect-research` for consistency with the other two.
- Standardize a `## Gotchas` heading convention so future skills inherit it (rate-skill already models it).
- Decide a house rule on Doer/Judge: which skills are allowed to self-grade vs. must delegate to the future verifier.

*Awaiting your go-ahead before editing any skill. Tell me which items to action and I'll run the proper `scripts/` + commit flow.*
