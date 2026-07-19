# Kernel + frameworks rating pass — wave 1 (plugin 0.18.0)

*2026-07-19 · rate-skill 10-category matrix, band-anchored per `skills/rate-skill/references/rubric.md` · single-rater static audit of the shipped files (iteration 1 for these skills). Not a behavioral eval — the authored suites in `evals/` are the path to that, and no score claims they ran.*

Categories: Utility & Value · Clarity of Instructions · Execution Reliability · Safety & Guardrails · Maintainability · Context & Token Efficiency · Idempotency & Determinism · Handoff & Collaboration · Machine-Verifiable Exit Criteria · Client Portability.

| Skill | Utility | Clarity | ExecRel | Safety | Maint | TokenEff | Idempot | Handoff | MachVer | Portab | **Overall** |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| jail-verify | 9.0 | 9.0 | 8.5 | 9.0 | 8.0 | 8.5 | 8.5 | 8.5 | 9.0 | 9.0 | **8.7** |
| jail-lab | 8.5 | 9.0 | 8.5 | 8.0 | 8.0 | 8.5 | 9.0 | 8.5 | 9.0 | 8.5 | **8.6** |
| jail-operationalize | 8.5 | 9.0 | 8.0 | 8.0 | 8.0 | 8.5 | 8.5 | 8.5 | 8.5 | 9.0 | **8.5** |
| jail-approval-gate | 8.5 | 9.0 | 8.0 | 9.0 | 8.0 | 8.5 | 8.5 | 8.5 | 8.0 | 9.0 | **8.5** |
| jail-task-contract | 8.5 | 8.5 | 8.0 | 8.0 | 8.0 | 8.5 | 8.0 | 9.0 | 8.0 | 9.0 | **8.4** |
| jail-orchestrate | 8.5 | 8.5 | 8.0 | 8.5 | 8.0 | 8.5 | 8.0 | 9.0 | 8.5 | 8.0 | **8.4** |
| jail-quarantine | 8.5 | 8.5 | 8.0 | 9.0 | 8.0 | 8.5 | 8.5 | 8.5 | 8.0 | 8.5 | **8.4** |
| jail-research | 9.0 | 8.5 | 8.0 | 8.5 | 8.0 | 8.5 | 7.5 | 9.0 | 7.5 | 8.5 | **8.3** |
| jail-decide | 8.5 | 8.5 | 8.0 | 8.0 | 8.0 | 8.5 | 8.0 | 8.5 | 7.5 | 9.0 | **8.3** |
| jail-memory | 8.5 | 8.5 | 8.0 | 9.0 | 8.0 | 8.5 | 8.0 | 8.5 | 7.5 | 8.5 | **8.3** |
| jail-skill-miner | 8.0 | 8.5 | 8.0 | 8.5 | 8.0 | 8.5 | 8.0 | 8.5 | 8.0 | 9.0 | **8.3** |
| jail-py-lab | 7.5 | 8.5 | 9.0 | 8.0 | 8.0 | 8.5 | 9.0 | 8.0 | 9.0 | 7.0 | **8.3** |
| cpr-agenda-builder | 8.0 | 8.5 | 8.0 | 8.0 | 8.0 | 8.5 | 8.0 | 8.5 | 8.0 | 9.0 | **8.3** |
| jail-red-team | 8.5 | 8.5 | 8.0 | 8.0 | 8.0 | 8.5 | 7.5 | 8.5 | 7.5 | 9.0 | **8.2** |
| business-model-canvas | 8.0 | 8.5 | 8.0 | 8.5 | 8.0 | 8.5 | 7.5 | 8.5 | 8.0 | 8.5 | **8.2** |
| jail-exec-brief | 8.0 | 8.5 | 8.0 | 8.0 | 8.0 | 8.5 | 8.0 | 8.0 | 7.0 | 9.0 | **8.1** |
| pestle-analysis | 8.0 | 8.5 | 8.0 | 8.0 | 8.0 | 8.5 | 7.5 | 8.5 | 7.5 | 8.5 | **8.1** |
| swot-analysis | 8.0 | 8.5 | 8.0 | 8.0 | 8.0 | 8.5 | 7.5 | 8.5 | 7.5 | 8.5 | **8.1** |

**Read of the board.** jail-verify (8.7) and jail-lab (8.6) lead — both are built around checks that can fail, which the rubric rewards. Nothing scores 9+ overall: these are well-built but **unproven** — Execution Reliability sits at 8.0–8.5 across the board because the eval suites are authored, not run. Frameworks sit ~8.1–8.3: thinner by design (they orchestrate the kernel rather than carry their own machinery).

**Standing upgrades (next iteration's targets)**
1. **Run the eval suites** (kernel-trigger, kernel-evals, jail-rate suites) — the single change that moves every ER/MV cell. Use jail-lab on itself: metric = trigger-eval pass rate.
2. **jail-exec-brief MV 7.0** — add a checkable structure lint (7 parts present, answer-first, labels intact) to a future jail-py companion.
3. **jail-research/frameworks Idempotency 7.5** — live evidence varies by nature; mitigate with packet caching rules (one packet per run, appended not re-searched).
4. **jail-py-lab Portability 7.0** — inherent (code execution); manual-ledger fallback in jail-lab already covers the gap.
5. Per-skill worked examples in `references/` where usage questions recur — deferred to keep wave-1 cores lean; add on demand, not speculatively.
