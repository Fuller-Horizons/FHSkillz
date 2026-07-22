# FHSkillz skill catalog — purpose, output, and value (0.23.0)

*2026-07-22 · Value = single-rater judgment on the jail-rate anchors (9–10
exceptional · 8–8.9 excellent · 7–7.9 good), weighing frequency × impact per
use × what the skill adds over an unaided capable model. Different axis than
the build-quality matrix. Per the determinism rule, scores moved ONLY where
0.21.0–0.23.0 shipped capability changed the frequency/impact/irreplaceability
calculus — the evidence column names the driver; unchanged skills carry their
prior score. Routing claims are measured (wave-2 baseline: 79/79 fire · 0/16
false-fire · variance 36/36 — evals/results/2026-07-22-wave2-baseline/).*

## Layer 1 — Reasoning kernel

| Skill | Purpose / use case | Output | Was | Now | Evidence for the move |
|---|---|---|:---:|:---:|---|
| **jail-prompt** 2.0.0 | Pre-flight for any AI task: stakes triage, STOP on bad-fit/flawed premise, engineer the rest | Engineered prompt / chain + manifest / STOP | 9.0 | **9.0** | untouched (winners don't churn) |
| **jail-verify** 1.1.0 | Independent done-done check on artifacts, never say-so | PASS/FAIL/FLAGS + failing observations + fixes | 9.0 | **9.0** | untouched |
| **jail-task-contract** 1.2.0 | Ambiguity → executable 14-field contract; scope guarded after | Contract + JAIL-HANDOFF; blocking questions when guessing is costly | 8.5 | **8.7** | grill mode + facts-vs-decisions (0.21.0, never re-rated) + type presets (RESEARCH/BUILD/ANALYSIS) cut fill time |
| **jail-research** 1.1.0 | Auditable evidence packets: tiered dated sources, contradictions weighed | Evidence packet + honest gaps | 8.5 | **8.7** | claim-class → tier routing with freshness windows + live-search availability detection (volatile claims can't silently run on memory) |
| **jail-decide** 1.1.0 | Defensible choices: criteria first, do-nothing priced, reversibility named | Decision package + confidence + change-conditions | 8.5 | **8.7** | quantified lane (EV ranges, cost-of-delay) + council-escalation check; routing surface measured (wn1 fix + 4/4 regression holds) |
| **jail-lab** 1.0.0 | Improve anything measurable: one variable, keep/discard vs best, ledger | Experiment ledger + baseline→best report | 8.6 | **8.6** | untouched core |
| **jail-diagnose** 1.0.0 | Loop-first defect diagnosis; confirmed cause; mandatory regression case | Diagnosis report: loop · cause+evidence · fix · proof | 8.6 | **8.6** | untouched; its regression rule governed this wave's own fix loop |
| **jail-council** 1.1.0 | Max-accuracy deliberation: blind answers, anonymized review, evidence-decided synthesis | Council answer + dissent register + audit appendix | 8.4 | **8.6** | MINI-COUNCIL lane at ~half cost with invariants intact — everyday contested calls now affordable (routing verified w4) |
| **jail-approval-gate** 1.1.0 | Tier every action before acting; fail closed | Tiered inventory + approval requests + ledger | 8.4 | **8.6** | standing APPROVAL PROFILE persists tier maps across sessions (per-run ritual → durable infrastructure) |
| **jail-quarantine** 1.1.0 | Adoption gate + sensitive halt + inline paste scan | Quarantine report | 8.4 | **8.6** | INLINE SCAN lane (everyday pastes) + canonical PROTECTED-CLASS TABLE other skills cite (verified w8) |
| **jail-red-team** 1.1.0 | Pressure-test before shipping; falsifier per finding | Ranked findings + falsifiers + verdict | 8.3 | **8.6** | falsifier-first rule (findings became testable; runnable ones feed jail-lab) + PRE-MORTEM-LITE lane (verified w10) |
| **jail-orchestrate** 1.2.0 | Long or parallel work as one system: earned delegation, fenced scopes, verified ledger | Integrated result + resume ledger | 8.0 | **8.5** | SOLO lane brings the ledger to single-agent long work — the constant case (verified w5); ledger shape shared with baton |
| **jail-memory** 1.2.0 | Govern durable memory: six-check gate, supersede-don't-delete, postmortems | Stored/refused entries + distilled lessons | 8.0 | **8.5** | file-ledger fallback works on any platform (the cap was platform-dependence); now the suite's persistence hub — spike ledger, approval profiles, tripwires, ADRs all land here |
| **jail-baton** 1.1.0 | Session handoff: state with proof, decisions-with-why, redacted | The baton document | 8.2 | **8.5** | proactive offer on context pressure (fires when it matters most) + orchestrate-ledger shape (batons seed resumes) — verified wn2 |
| **jail-skill-miner** 1.2.0 | Mine disciplines + the suite's self-maintenance loop | Candidate table → approved artifact sets | 7.5 | **8.2** | continuous mode: eval failures & repeated corrections auto-nominate fixes; ready-to-commit output. Honest gap to 8.5: needs routine live cycles |
| **jail-prototype** 1.1.0 | Throwaway prototypes answering named design questions | Verdict + evidence + spike-ledger entry | 7.9 | **8.3** | SPIKE LEDGER (answered questions never rebuilt) + verdicts return as labeled decide/bmc evidence. Fog-to-build frequency still moderate |
| **jail-wayfind** 1.1.0 | Decision-ticket maps through fog | The map + cleared-way handoff | 7.6 | **8.0** | map-as-baton-spine (multi-session persistence) + ADR-at-resolution. Fog work is structurally occasional — honest ceiling |

## Layer 2 — Workflow

| Skill | Purpose / use case | Output | Was | Now | Evidence for the move |
|---|---|---|:---:|:---:|---|
| **jail-rate** 2.0.0 | Rate anything 0.0–10.0, type-matched weighted rubric, cited evidence | Rubric + evidence-cited scorecard + recommendations | 8.8 | **8.8** | untouched |
| **jail-operationalize** 1.0.0 | Recommendation → runnable owned workflow | 13-field spec with testable completion | 8.7 | **8.7** | untouched |
| **jail-prospect** 1.3.0 | Free-source company screening: sell-side/consulting + vendor/competitor/partner vetting | Purpose-fit scored brief, fully cited | 8.2 | **8.5** | COMPANY SNAPSHOT lane ≈ triples applicable asks on the same discipline (verified w9; near-miss n6/n2 still route correctly) |
| **jail-rate-skill** 2.2.0 | QA instrument for AI skills; measured evidence outranks inspection | Rating matrix + validated JSON record | 7.8 | **8.4** | Rule 10: consumes real eval results (this repo's baselines) — categories scored from measurement; the marketplace's pre-release gate. Audience stays narrow |
| **jail-exec-brief** 1.1.0 | Decision-forcing executive communication | Seven-part brief ending in the forced decision | 7.8 | **8.3** | decision-forcing mandate (no FYI briefs) + audience-calibration table — the parts a plain model won't do unprompted. Summarization edges stay commodity |

## Layer 3 — Frameworks

| Skill | Purpose / use case | Output | Was | Now | Evidence for the move |
|---|---|---|:---:|:---:|---|
| **jail-cpr** 1.2.0 | Meetings, both halves: Results-first design + post-meeting debrief | CPR + agenda · decisions/actions/Results-audit | 8.0 | **8.5** | DEBRIEF lane doubles the surface (verified w6, wn4, and flipped n8); design↔debrief close the loop |
| **jail-strategy-scan** 1.0.0 | SWOT→TOWS, PESTLE+tripwires, or full sweep — one evidence base | Classified tables + strategies/implications + tripwires | 7.6/7.5 | **8.3** | merger of jail-swot+jail-pestle: one research sweep serves both lanes + native interaction pass + tripwires→memory (verified w1–w3, k14/k15). Commodity-format ceiling honestly remains |
| **jail-bmc** 1.2.0 | Evidence-labeled Business Model Canvas + validation pipeline | Canvas + coherence findings + lab-shaped experiments | 7.8 | **8.2** | riskiest assumptions emit jail-lab specs; canvas-delta mode makes it a living document. Still a commodity format at core |

## JAIL-PY companions

| Skill | Purpose / use case | Output | Was | Now | Evidence for the move |
|---|---|---|:---:|:---:|---|
| **jail-py-lab** 1.1.0 | Runnable lab bookkeeping + wave-over-wave comparison | Ledger + trajectory + exit-coded regression check | 7.8 | **8.2** | lab-compare.py regression gates + it is the suite's own metrics engine (trigger-accuracy ledger, used in anger twice). Code-execution bound |
| **jail-py-toolkit** 1.0.0 | Prompt + rating machine checks, one install, release-wired | Exit-coded verdicts; 9 scripts | 7.5/7.2 | **8.0** | merger of the two py tool skills: one install for basic users; validate-skills.py runs its checks every release. Code-execution bound |

**Suite mean value: 8.50** across 27 skills (was 8.15 across 25 at 0.20.0) ·
spread 8.0–9.0 · **18 of 27 at ≥ 8.5**.

## The honest remainder (below 8.5, and why)

Nine skills sit at 8.0–8.4 after this wave. The residual caps are
structural, not build-quality: **occasional-by-nature frequency** (wayfind,
prototype, skill-miner — their triggers are rare events), **commodity-format
cores** (strategy-scan, bmc, exec-brief's summarization edge — the JAIL
discipline is the moat, the format is not), **code-execution dependence**
(py-lab, py-toolkit), and **narrow audience** (rate-skill). What would move
them: recorded real-usage frequency over the coming weeks (jail-memory
postmortems will capture it), live skill-miner cycles, and rate-skill
becoming the enforced pre-release gate. Inflating them today would violate
the determinism rule the catalog runs on.
