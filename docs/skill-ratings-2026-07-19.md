# FHSkillz — full skillset review & three-iteration rating cycle

*2026-07-19 · rated with the rate-skill 10-category matrix (anchors from `skills/rate-skill/references/rubric.md`) · plugin 0.16.0 → 0.17.0*

**Method note (honest scope):** single-rater static audit, band-anchored per the rubric, applied to the files as they stood at each iteration. Not a behavioral eval — the authored eval sets in `evals/` are the path to that. Iteration 1 was scored **after** the structural release work (code-free cores, jail-py split, jail-rate v2 rebuild, doc refresh), so it reflects the new architecture; iterations 2 and 3 measure the targeted improvement rounds on top of it.

## Overall progression

| Skill | Version | Iter 1 | Iter 2 | Iter 3 | Δ total |
|---|---|:---:|:---:|:---:|:---:|
| jail-prompt | 2.0.0 | 8.3 | 8.4 | 8.4 | +0.1 |
| jail-rate | 2.0.0 | 8.1 | 8.3 | **8.4** | +0.3 |
| rate-skill | 2.0.0 | 8.2 | 8.2 | 8.3 | +0.1 |
| company-prospect-research | 1.1.0 | 8.0 | 8.1 | 8.1 | +0.1 |
| jail-py-prompt-tools | 1.0.0 | 8.3 | 8.3 | 8.3 | — |
| jail-py-rate-tools | 1.0.0 | 8.2 | 8.2 | 8.2 | — |

## What each iteration changed

**Iteration 1 → 2** (targets: the three lowest cells on the board)
- **jail-prompt · Context & Token Efficiency 6.5 → 7.0** — removed duplicated lane-note paragraph, compressed the METADATA/OUTPUT FORMAT skeleton prose, the always-surface rule, the auto-triage sentence, the high-stakes escalation, and the prompts.json offer; normalized whitespace. Behavior preserved; ~1KB net lighter than the pre-trim v2 text.
- **jail-rate · Machine-Verifiable Exit Criteria 6.5 → 8.0, Execution Reliability 7.5 → 8.0, Idempotency 7.5 → 8.0** — added the "Self-check before delivering (all must pass)" block: weights sum to exactly 100%, overall recomputed from Σ(score × weight), every scorecard row carries a citation or an explicit Judgment label, every citation resolves with URL + date, cap applied, confidence stated. One failed line = fix before delivering.
- **company-prospect-research · Machine-Verifiable 6.5 → 7.5** — self-check upgraded from a soft list to a structural gate: all template sections present, per-component signal-or-zero rule, four-value recommendation enum, dated citations with stale flags.

**Iteration 2 → 3** (targets: evidence + composition)
- **jail-rate · Execution Reliability 8.0 → 8.5** — authored its eval suite: `evals/jail-rate-trigger-evals.json` (10 should-trigger + 6 near-misses, including the rate-skill and company-prospect-research routing traps and a people-boundary decline) and `evals/jail-rate-evals.json` (4 behavioral cases with grader assertions: declared rubric + type classification, private-subject handling, people boundary, critical-flaw cap). Authored ≠ run — the score reflects regression-testability, not verified behavior.
- **rate-skill · Handoff & Collaboration 8.0 → 8.5** — explicit two-way boundary with jail-rate (AI skill directories ↔ everything else), completing the routing triangle with company-prospect-research.
- Held rather than inflated: jail-prompt efficiency stays 7.0 (the file is still ~21KB — the remaining fix is structural, see below), and the jail-py skills stay put (their categories were already earned by tested, deterministic scripts).

## Final matrices (iteration 3)

### jail-prompt 2.0.0 — Overall **8.4**

| Category | Score | Basis (one line) | Next upgrade → post-reco |
|---|:---:|---|:---:|
| Utility & Value | 9.0 | Broad trigger surface; kills wasted runs before they start; build-vs-buy gate | — |
| Clarity of Instructions | 8.5 | Lanes + skeleton + gotchas; some long operative paragraphs remain | 9.0 |
| Execution Reliability | 8.0 | Companion checks with named manual fallbacks; proxy-only eval evidence | run live `claude -p` harness → 8.5 |
| Safety & Guardrails | 8.5 | Secret handling, least-privilege, injection defense, output sanitization | 9.0 |
| Maintainability | 8.5 | Versioned, per-skill changelog, repo validator, modular references | 9.0 |
| Context & Token Efficiency | 7.0 | Trimmed, but ~21KB always-loaded core remains heavy | move Phase-3 heavy machinery (dry-run, determinism test, METADATA detail) to a lane-loaded reference → 8.5 |
| Idempotency & Determinism | 8.0 | temp-0 guidance, determinism self-test, params in METADATA | 8.5 |
| Handoff & Collaboration | 9.0 | Fixed-key METADATA, chain manifests, checkpoint gates | — |
| Machine-Verifiable Exit Criteria | 8.0 | Mandatory programmatic SUCCESS TEST; linters now optional-install | 8.5 |
| Client Portability | 9.0 | Install-free meta-prompt, relative links, plaintext | — |

### jail-rate 2.0.0 — Overall **8.4** (was 1.0.0 software-only; rebuilt)

| Category | Score | Basis | Next upgrade → post-reco |
|---|:---:|---|:---:|
| Utility & Value | 9.0 | Rates anything, weighted per type, with an upside projection | — |
| Clarity of Instructions | 8.5 | 5-step process, declared-rubric rule, output template | worked full-output example in references → 9.0 |
| Execution Reliability | 8.5 | Self-check gate + authored eval suite (not yet run) | run the evals → 9.0 |
| Safety & Guardrails | 8.5 | People boundaries, marketing-claims-≠-evidence, no-fabrication | 9.0 |
| Maintainability | 8.5 | Versioned, changelog, README, two modular references | 9.0 |
| Context & Token Efficiency | 8.0 | Lean core; rubric library + evidence standards load on demand | 8.5 |
| Idempotency & Determinism | 8.0 | Anchors + band-first rule + arithmetic recompute; live evidence varies by nature | 8.5 |
| Handoff & Collaboration | 8.0 | Routes to rate-skill / company-prospect-research / jail-prompt | 8.5 |
| Machine-Verifiable Exit Criteria | 8.0 | Weights=100 check, Σ recompute, citation-resolution check | jail-py scorecard validator (future JAIL-PY candidate) → 9.0 |
| Client Portability | 8.5 | Instruction-only; degrades to supplied-materials mode without search | 9.0 |

### rate-skill 2.0.0 — Overall **8.3**

| Category | Score | Basis | Next upgrade → post-reco |
|---|:---:|---|:---:|
| Utility & Value | 8.0 | Core QA instrument for the plugin itself | — |
| Clarity of Instructions | 8.5 | Non-negotiable rules + matrices + config-driven columns | 9.0 |
| Execution Reliability | 7.5 | Sound procedure; the rater itself still has no gold-standard eval | gold fixtures (known-good / known-weak / injection-laden) → 8.5 |
| Safety & Guardrails | 9.0 | Untrusted-target rule, injection cap at 4.0, never-run-target-code | — |
| Maintainability | 8.5 | Versioned, changelog, README, config | 9.0 |
| Context & Token Efficiency | 8.0 | 300-line summarizer rule, ~4K-token budget | 8.5 |
| Idempotency & Determinism | 8.5 | temp-0 + band-first + measured variance pattern | 9.0 |
| Handoff & Collaboration | 8.5 | skill-creator (behavioral) and jail-rate (non-skill subjects) boundaries | 9.0 |
| Machine-Verifiable Exit Criteria | 7.5 | Validation via optional companion; manual recompute fallback | 8.5 |
| Client Portability | 8.5 | Instruction-only, config-driven, no absolute paths | 9.0 |

### company-prospect-research 1.1.0 — Overall **8.1**

| Category | Score | Basis | Next upgrade → post-reco |
|---|:---:|---|:---:|
| Utility & Value | 8.5 | Money-adjacent, complete decision workflow | — |
| Clarity of Instructions | 8.5 | 4-stage chain with copy-paste prompts + template | 9.0 |
| Execution Reliability | 7.5 | Disciplined chain; zero eval cases for the most money-adjacent skill | 15–30 real-target eval set → 8.5 |
| Safety & Guardrails | 9.0 | Free-sources-only, no fabricated financials, owner privacy | — |
| Maintainability | 8.0 | Now versioned + changelog + README | 8.5 |
| Context & Token Efficiency | 8.0 | Good references/assets split | 8.5 |
| Idempotency & Determinism | 7.0 | 0–100 component scoring leaves judgment spread | deterministic score-aggregation helper (future JAIL-PY candidate) → 8.0 |
| Handoff & Collaboration | 8.0 | Chain handoffs + related-skills routing | 8.5 |
| Machine-Verifiable Exit Criteria | 7.5 | Structural self-check gate (sections, enum, signal-or-zero) | 8.5 |
| Client Portability | 8.5 | Pure instructions, relative paths | 9.0 |

### jail-py-prompt-tools 1.0.0 — Overall **8.3** · jail-py-rate-tools 1.0.0 — Overall **8.2**

| Category | prompt-tools | rate-tools | Basis |
|---|:---:|:---:|---|
| Utility & Value | 7.5 | 7.0 | High-leverage but companion-scoped |
| Clarity of Instructions | 8.5 | 8.5 | Script table + usage + exit codes + workflow |
| Execution Reliability | 9.0 | 9.0 | All 9 scripts self-tested this release (pass + fail paths, history delta, drift detection) |
| Safety & Guardrails | 8.0 | 8.0 | Stdlib-only, no network, no-fake-runs rule |
| Maintainability | 8.0 | 8.0 | Versioned + changelog; next: one-command smoke-test → 8.5 |
| Context & Token Efficiency | 8.5 | 8.5 | Short SKILL.md, code loaded only on run |
| Idempotency & Determinism | 9.0 | 9.0 | Deterministic scripts, stable exit codes |
| Handoff & Collaboration | 8.0 | 8.0 | Explicitly back their core skill's checkpoints |
| Machine-Verifiable Exit Criteria | 9.0 | 9.0 | Exit codes are the product |
| Client Portability | 7.0 | 7.0 | Requires code execution (inherent); Python 3.8+ everywhere else |

## Compatibility matrices (columns from `skills/rate-skill/config.json`)

**IDE** — Antigravity · VS Code · Cursor — and **CLI** — Claude Code · Codex CLI · OpenCode · Gemini CLI:

| Skill | Antigravity | VS Code | Cursor | Claude Code | Codex CLI | OpenCode | Gemini CLI |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| jail-prompt | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| jail-rate | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| rate-skill | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| company-prospect-research | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| jail-py-prompt-tools | ✅* | ✅* | ✅* | ✅* | ✅* | ✅* | ✅* |
| jail-py-rate-tools | ✅* | ✅* | ✅* | ✅* | ✅* | ✅* | ✅* |

Core skills are instruction-only plaintext with relative links — portable to every column via the plugin or `scripts/install.sh` symlinks. `*` = requires a Python 3.8+ code-execution environment (all listed clients have one; on claude.ai web the toggle **Settings → Capabilities → Code execution** must be on, else the core skills' manual fallbacks apply).

## Composition map (how they work with each other)

- **jail-prompt** auto-triages tasks to other installed skills (jail-rate, company-prospect-research, docx, …) at its Phase-2 right-tool gate, and calls **jail-py-prompt-tools** for machine checks (manual fallback without it).
- **jail-rate** hands AI-skill targets to **rate-skill**, prospecting decisions to **company-prospect-research**, and shares the house evidence discipline (source tiers ≈ jail-prompt `sources.md`; claim labels ≈ company-prospect-research).
- **rate-skill** hands non-skill subjects to **jail-rate**, behavioral evals to Anthropic's `skill-creator`, and calls **jail-py-rate-tools** for record validation/history/variance.
- **company-prospect-research** points 0–10 business-quality asks to **jail-rate** and prompt-engineering follow-ons to **jail-prompt**.

## Open items (deliberately not claimed as done)

1. Run the authored jail-rate eval suites; run jail-prompt's sets on the live `claude -p` harness (proxy-only since 0.9.0).
2. Author eval sets for rate-skill (gold fixtures) and company-prospect-research (real targets).
3. jail-prompt structural slimming: lane-loaded reference for Phase-3 heavy machinery (biggest single remaining upside on the board).
4. Future JAIL-PY candidates: `jail-py-rate-scorecard` (validate a jail-rate scorecard's arithmetic/citations), `jail-py-prospect-score` (deterministic 0–100 aggregation for company-prospect-research).
