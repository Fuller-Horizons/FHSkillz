# FHSkillz full-plugin review & rating matrix — all 24 skills (0.18.0)

*2026-07-19 · rate-skill 10-category matrix, band-anchored · single-rater static audit. Determinism rule applied: skills unchanged since their last rating keep their scores (same evidence → same score); the fresh work in this pass is the design/efficiency review and the measured footprint data below. Behavioral evals remain authored-not-run — no score pretends otherwise.*

## Purpose & design review, by layer

**Layer 1 — reasoning kernel (12).** Purpose: make any model — frontier or small-context — work under Jonathan's decision architecture (goal → evidence → workflow → skill → tool last). Design: uniform anatomy (router description with negative triggers → discipline with checks that can fail → related-skills routing → gotchas → JAIL-HANDOFF), each skill self-sufficient with the constitution rules it needs inlined. The kernel's distinguishing design choices: verifier ≠ producer (jail-verify), fail-closed everywhere it matters (approval-gate, quarantine), evidence with provenance (research), bounded loops only (lab, orchestrate). Efficiency: kernel cores average **~4.3KB** — the small-context goal held.

**Layer 2 — workflow (5).** Purpose: repeatable business outcomes on top of the kernel. jail-rate and rate-skill form a clean two-instrument pair (anything vs AI-skills); jail-operationalize is the recommendation-to-runnable converter; jail-exec-brief is the voice layer; company-prospect-research the money-adjacent domain veteran. Design note: jail-exec-brief is deliberately the least mechanical — its 7.0 Machine-Verifiable is the price of a qualitative craft skill.

**Layer 3 — frameworks (4).** Purpose: commoditized frameworks (PESTLE/SWOT/BMC/CPR) made non-commodity by evidence discipline and kernel chaining. Design: thin orchestrators (3.7–4.1KB) that invoke by name and degrade to inline fallbacks — correct, but chaining 5–7 skills is real ceremony on a small model; the inline fallbacks are what make them viable there.

**JAIL-PY companions (3).** Purpose: the runnable halves, kept out of the cores per the code-free rule. All scripts stdlib-only with stable exit codes; jail-py-lab self-tested 9/9 this release. Portability 7.0 is inherent (code execution required) and mitigated by every core's manual fallback.

## Measured footprint (efficiency, empirical)

- Always-loaded description surface: **14,795 chars ≈ 3.7K tokens** for all 24 skills — the standing per-session tax of the one-plugin choice. Modest in a frontier window; material on an 8K-context model (~46%), which is why cores are self-sufficient and lean.
- Core SKILL.md total: 130.7KB; average 5.4KB. Outlier: **jail-prompt at 21.1KB** (16% of all core bytes) — the known efficiency ceiling, with the lane-loaded-reference refactor still the top structural fix. Second: jail-rate 9.0KB, rate-skill 9.6KB (both carry their rubric cores; acceptable).
- Progressive disclosure: 27 aux files (references/scripts) concentrated in the five skills that need them; 17 of 24 skills are a single lean core + README/CHANGELOG.

## The matrix (sorted by overall; plugin mean **8.30**)

| Skill | Layer | Utility | Clarity | ExecRel | Safety | Maint | TokenEff | Idempot | Handoff | MachVer | Portab | **Overall** |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| jail-verify | L1 | 9.0 | 9.0 | 8.5 | 9.0 | 8.0 | 8.5 | 8.5 | 8.5 | 9.0 | 9.0 | **8.7** |
| jail-lab | L1 | 8.5 | 9.0 | 8.5 | 8.0 | 8.0 | 8.5 | 9.0 | 8.5 | 9.0 | 8.5 | **8.6** |
| jail-approval-gate | L1 | 8.5 | 9.0 | 8.0 | 9.0 | 8.0 | 8.5 | 8.5 | 8.5 | 8.0 | 9.0 | **8.5** |
| jail-operationalize | L2 | 8.5 | 9.0 | 8.0 | 8.0 | 8.0 | 8.5 | 8.5 | 8.5 | 8.5 | 9.0 | **8.5** |
| jail-orchestrate | L1 | 8.5 | 8.5 | 8.0 | 8.5 | 8.0 | 8.5 | 8.0 | 9.0 | 8.5 | 8.0 | **8.4** |
| jail-prompt | L1 | 9.0 | 8.5 | 8.0 | 8.5 | 8.5 | 7.0 | 8.0 | 9.0 | 8.0 | 9.0 | **8.4** |
| jail-quarantine | L1 | 8.5 | 8.5 | 8.0 | 9.0 | 8.0 | 8.5 | 8.5 | 8.5 | 8.0 | 8.5 | **8.4** |
| jail-rate | L2 | 9.0 | 8.5 | 8.5 | 8.5 | 8.5 | 8.0 | 8.0 | 8.0 | 8.0 | 8.5 | **8.4** |
| jail-task-contract | L1 | 8.5 | 8.5 | 8.0 | 8.0 | 8.0 | 8.5 | 8.0 | 9.0 | 8.0 | 9.0 | **8.4** |
| cpr-agenda-builder | L3 | 8.0 | 8.5 | 8.0 | 8.0 | 8.0 | 8.5 | 8.0 | 8.5 | 8.0 | 9.0 | **8.3** |
| jail-decide | L1 | 8.5 | 8.5 | 8.0 | 8.0 | 8.0 | 8.5 | 8.0 | 8.5 | 7.5 | 9.0 | **8.3** |
| jail-memory | L1 | 8.5 | 8.5 | 8.0 | 9.0 | 8.0 | 8.5 | 8.0 | 8.5 | 7.5 | 8.5 | **8.3** |
| jail-py-lab | PY | 7.5 | 8.5 | 9.0 | 8.0 | 8.0 | 8.5 | 9.0 | 8.0 | 9.0 | 7.0 | **8.3** |
| jail-py-prompt-tools | PY | 7.5 | 8.5 | 9.0 | 8.0 | 8.0 | 8.5 | 9.0 | 8.0 | 9.0 | 7.0 | **8.3** |
| jail-research | L1 | 9.0 | 8.5 | 8.0 | 8.5 | 8.0 | 8.5 | 7.5 | 9.0 | 7.5 | 8.5 | **8.3** |
| jail-skill-miner | L1 | 8.0 | 8.5 | 8.0 | 8.5 | 8.0 | 8.5 | 8.0 | 8.5 | 8.0 | 9.0 | **8.3** |
| rate-skill | L2 | 8.0 | 8.5 | 7.5 | 9.0 | 8.5 | 8.0 | 8.5 | 8.5 | 7.5 | 8.5 | **8.3** |
| business-model-canvas | L3 | 8.0 | 8.5 | 8.0 | 8.5 | 8.0 | 8.5 | 7.5 | 8.5 | 8.0 | 8.5 | **8.2** |
| jail-py-rate-tools | PY | 7.0 | 8.5 | 9.0 | 8.0 | 8.0 | 8.5 | 9.0 | 8.0 | 9.0 | 7.0 | **8.2** |
| jail-red-team | L1 | 8.5 | 8.5 | 8.0 | 8.0 | 8.0 | 8.5 | 7.5 | 8.5 | 7.5 | 9.0 | **8.2** |
| company-prospect-research | L2 | 8.5 | 8.5 | 7.5 | 9.0 | 8.0 | 8.0 | 7.0 | 8.0 | 7.5 | 8.5 | **8.1** |
| jail-exec-brief | L2 | 8.0 | 8.5 | 8.0 | 8.0 | 8.0 | 8.5 | 8.0 | 8.0 | 7.0 | 9.0 | **8.1** |
| pestle-analysis | L3 | 8.0 | 8.5 | 8.0 | 8.0 | 8.0 | 8.5 | 7.5 | 8.5 | 7.5 | 8.5 | **8.1** |
| swot-analysis | L3 | 8.0 | 8.5 | 8.0 | 8.0 | 8.0 | 8.5 | 7.5 | 8.5 | 7.5 | 8.5 | **8.1** |

Overall = arithmetic mean of the 10 categories (rate-skill rule 4). Compatibility: all 24 target every configured IDE (Antigravity, VS Code, Cursor) and CLI (Claude Code, Codex CLI, OpenCode, Gemini CLI) — cores are plaintext/relative-link portable; jail-py-* additionally require Python 3.8+ code execution.

## Fresh findings from this pass (not previously recorded)

1. **The #1 system risk is now routing, not quality.** 24 router descriptions share verb surface ("rate/score/verify/check/review/evaluate"). The collision set is exactly what `evals/kernel-trigger-evals.json`'s 12 near-misses test — and they are unrun. Until that run, every Execution Reliability score is capped in the low 8s on principle.
2. **Eval infrastructure lags eval content.** 40 kernel cases + jail-rate suites exist as JSON, but `scripts/run_evals.py` predates them (jail-prompt-oriented). A thin runner (or a jail-lab session using trigger pass-rate as the metric) is the cheapest path to evidence.
3. **Kernel has no worked examples** — a deliberate small-context tradeoff. Clarity holds at 8.5 across the kernel; the first skill to show recurring usage confusion should get a references/examples.md, on demand, not speculatively.
4. **jail-task-contract ↔ jail-prompt Phase 1** remains the closest boundary in the plugin (task-for-any-executor vs prompt-as-deliverable). Descriptions carve it and near-miss n5 tests it; watch it in real usage.
5. **Frameworks' Idempotency 7.5** is structural: live evidence varies run to run. The one-packet-per-run rule (skill-graph anti-pattern list) is the mitigation; a cached-packet convention could lift it later.

## Ranked recommendations

1. **Run the trigger evals** (all suites) — moves ER/MV plugin-wide; use jail-lab on itself (metric: near-miss pass rate). Effort: low. Impact: highest.
2. **jail-prompt lane-loaded refactor** (~21KB → ~12KB core target) — the single biggest token win. Effort: medium.
3. **Thin eval runner for the JSON suites** (repo scripts/, not skill content). Effort: low-medium.
4. **jail-exec-brief structure lint** (7 parts, answer-first, labels) as a future jail-py check. Effort: low. Impact: its 7.0 → 8.5.
5. **Hold the line on count.** 24 skills ≈ 3.7K standing tokens; wave 3 adds ~17 more. Enforce the roadmap's entry bar (miner pipeline + rate-skill ≥ 8.0) so growth stays paid-for.
