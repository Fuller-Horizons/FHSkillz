# Wave 2 scorecard — "all skills toward 8.5+" (0.23.0)

Date: 2026-07-22 · Program: [enhancement-metrics-contract.md](enhancement-metrics-contract.md) · Trigger evidence: [evals/results/2026-07-22-wave2-baseline/](../evals/results/2026-07-22-wave2-baseline/RUN.md)

## What shipped

- **19 skills enhanced** (new lanes, integration hooks, presets): task-contract, research, decide, council, approval-gate, quarantine, red-team, prospect, baton, orchestrate, memory, cpr, prototype, exec-brief, rate-skill, skill-miner, py-lab, bmc, wayfind.
- **2 consolidations** (29 → 27 skills): jail-swot + jail-pestle → **jail-strategy-scan** · jail-py-prompt-tools + jail-py-rate-tools → **jail-py-toolkit**. Legacy keywords route to successors (measured).
- **Release loop hardened:** validate-skills.py now runs the toolkit machine checks every release; py-lab's lab-compare.py is an exit-coded regression gate.
- **Suite compounding:** memory became the persistence hub (spike ledger, approval profiles, tripwires, ADRs); baton/orchestrate share one ledger shape; red-team falsifiers and bmc assumptions feed jail-lab.

## Ship-gate status

| Gate | Target | Measured | Status |
|---|---|---|---|
| Trigger fire rate (95 cases) | ≥ 95% | **100%** (79/79, post fix-loop; 98.7% pre-fix) | ✅ |
| False-fire rate | ≤ 5% | **0%** (0/16) | ✅ |
| Variance ×3 (collision set incl. flipped n8) | stable | **36/36 identical** | ✅ |
| Fix loop with regression case | required | 1 failure → description fix → blind re-judge, 4/4 neighbors held; wn1 kept as regression case | ✅ |
| Repo validator (now incl. machine checks) | pass | pass | ✅ |
| Behavioral assertions | 100% | authored (incl. 5 new wave-2 behavioral cases), **not yet run** | ⏳ Wave 2b |

## Value movement (the ask: everything over 8.5)

**Suite mean 8.15 → 8.50.** 18 of 27 skills now ≥ 8.5 (was 9 of 29 ≥ 8.5).
Every score move is evidence-named in [skill-catalog.md](skill-catalog.md);
untouched skills did not move (determinism rule).

**The honest remainder — 9 skills at 8.0–8.4:** strategy-scan 8.3 ·
prototype 8.3 · exec-brief 8.3 · rate-skill 8.4 · bmc 8.2 · py-lab 8.2 ·
skill-miner 8.2 · wayfind 8.0 · py-toolkit 8.0. Their caps are structural
(occasional-by-nature triggers, commodity-format cores, code-execution
dependence, narrow audience) — the catalog's closing section names what
evidence would move each. Scoring them 8.5 today would be theater; the
contract's north star is verified correctness, and that includes the
ratings themselves.

## 0.23.0 release contents

New skills (2) · retired skills (4, git history preserves lineage) ·
17 SKILL.md deltas + version bumps + per-skill changelogs · lab-compare.py ·
validator machine-check wiring · docs (constitution layer map, skill-graph,
catalog re-rate, this scorecard) · evals (wave2 suite, 3 retargeted cases,
accept-map, 2 evidence bundles, ledger #1–#2) · README/wiki count updates.

## Next (on your approval)

- **Wave 2b:** behavioral executor — run all authored assertion suites
  (kernel 8-case types + chains, council, mp, rate, prompt, wave-2's 5 new)
  with fresh-grader subagents, variance ×3 on flaky-prone cases.
- **Standing:** usage-frequency capture via jail-memory postmortems to
  evidence the remaining nine's next move.
