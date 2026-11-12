# Upgrade 0.27 — task contract (jail-task-contract, 14 fields)

1. **Objective** — Raise FHSkillz quality to the most defensible, accurate, premium level, proven by measured tests, using cheaper models for most of the work.
2. **Stakeholder** — Jonathan Fuller (owner, Fuller Horizons); consumes the skills for consulting and agentic work.
3. **Required outcome** — Every changed skill beats its 0.26.0 version on blind live A/B tests and on re-rating; no skill regresses on any check class.
4. **Deliverables** — Branch `upgrade/0.27-wave-a` (patch + zip); `docs/upgrade-0.27/` (contract, specs, ledger, results); updated evals; new toolkit scripts, hooks, live runner.
5. **Constraints** — Code-free core SKILL.md (runnable code only in `jail-py-*`, `scripts/`, `hooks/`); stdlib-only Python 3.8+; descriptions ≤ 450 chars with ≥1 negative trigger; SKILL.md core ≤ 160 lines; ECC-derived patterns carry the line `Pattern adapted from ECC (github.com/affaan-m/ECC, MIT, © 2026 Affaan Mustafa)`; no text copied from CC-BY-SA or Apache-2.0 ECC skills; hooks are opt-in (off by default).
6. **Non-goals** — No new skills in this wave; no ECC plugin install; no wave-B skills before the checkpoint; no push to GitHub from this session (no push access).
7. **Inputs available** — FHSkillz 0.26.0 (commit a8c00d4), ECC 2.2.3 (commit d2ef268, MIT), existing evals + ledgers, authenticated `claude` CLI 2.1.322.
8. **Inputs missing** — Push access (owner opens the PR).
9. **Assumptions** — `--setting-sources project --plugin-dir <ver>` isolates versions (verified 2026-11-12 with a probe skill); Sonnet/Haiku aliases resolve to the 5.5 family.
10. **Dependencies** — Foundation (F1–F5) must pass unit tests before any skill authoring.
11. **Material risks** — Trigger-routing regression from shortened descriptions (mitigated: full trigger suite gate, 100% fire / 0% false-fire); grader bias (mitigated: dual blind graders + Opus calibration sample); live-test cost (mitigated: per-skill cap).
12. **Success criteria** — Behavioral pass rate (new) ≥ 95% and > baseline per skill; trigger gate 100/0; re-rate variance ≤ ±0.2; `python3 scripts/validate-skills.py` exit 0; all toolkit unit tests pass.
13. **Completion criteria** — `docs/upgrade-0.27/LEDGER.md` shows `NODE … STATUS: verified` with an artifact for every wave-A node; `results/` holds raw live outputs, grades, and the A/B key; the checks in 12 rerun green from a clean checkout of the branch.
14. **Approval-required actions** — Opening the PR / merging (owner); enabling hooks on a real machine (owner); live-test spend (approved 2026-11-12, "proceed").
