# FHSkillz skill catalog — purpose, output, and value (0.24.0)

*2026-07-22 · Value = single-rater judgment on the jail-rate anchors (9–10
exceptional · 8–8.9 excellent · 7–7.9 good), weighing frequency × impact per
use × what the skill adds over an unaided capable model. Different axis than
the build-quality matrix. Per the determinism rule, scores moved ONLY where
shipped capability changed the calculus — the evidence column names the
driver; renames alone do not move value. Routing claims are measured
(wave-3 baseline: 79/79 fire · 0/16 false-fire · variance 11/12 —
evals/results/2026-07-22-wave3-baseline/).*

**0.24.0 changes:** 4 renames (operationalize→**plan**, baton→**handoff**,
strategy-scan→**strategy**, exec-brief→**summarize**) · 1 merge
(jail-wayfind folded into **jail-plan** as its MAP lane) → 27→**26 skills** ·
content upgrades to research (dual output), memory (file system), cpr (DOCX/PDF).

## Layer 1 — Reasoning kernel

| Skill | Purpose / use case | Output | Was | Now | Evidence for the move |
|---|---|---|:---:|:---:|---|
| **jail-prompt** 2.0.0 | Pre-flight for any AI task: stakes triage, STOP on bad-fit/flawed premise, engineer the rest | Engineered prompt / chain + manifest / STOP | 9.0 | **9.0** | untouched |
| **jail-verify** 1.1.0 | Independent done-done check on artifacts, never say-so | PASS/FAIL/FLAGS + failing observations + fixes | 9.0 | **9.0** | untouched |
| **jail-research** 1.2.0 | Auditable research: tiered dated sources, contradictions weighed | **Synthesized answer (inline [n] cites) + evidence packet** | 8.7 | **8.8** | dual output (Perplexity-style): the answer is now directly usable AND fully traceable — usable as a deliverable, not just a feeder |
| **jail-plan** 1.0.0 | Turn intent into an executable plan — OPERATE (decision → owned 13-field workflow) or MAP (foggy multi-session work → decision-ticket map) | 13-field spec · or map index + cleared-way handoff | 8.7 | **8.7** | merger of jail-operationalize (OPERATE) + jail-wayfind (MAP); two lanes off one skill — carries operationalize's value, MAP adds coverage (verified k6, mp-t4, n7) |
| **jail-task-contract** 1.2.0 | Ambiguity → executable 14-field contract; scope guarded; grill mode | Contract + JAIL-HANDOFF; blocking questions when guessing is costly | 8.7 | **8.7** | untouched (kept standalone — the front door every skill refs) |
| **jail-decide** 1.1.0 | Defensible choices: criteria first, do-nothing priced, quantified lane | Decision package + confidence + change-conditions | 8.7 | **8.7** | untouched this wave |
| **jail-lab** 1.0.0 | Improve anything measurable: one variable, keep/discard vs best, ledger | Experiment ledger + baseline→best report | 8.6 | **8.6** | untouched |
| **jail-diagnose** 1.0.0 | Loop-first defect diagnosis; confirmed cause; mandatory regression case | Diagnosis report: loop · cause+evidence · fix · proof | 8.6 | **8.6** | untouched |
| **jail-council** 1.1.0 | Max-accuracy deliberation: blind answers, anonymized review, evidence-decided | Council answer + dissent register + audit appendix | 8.6 | **8.6** | untouched this wave |
| **jail-approval-gate** 1.1.0 | Tier every action before acting; standing profiles; fail closed | Tiered inventory + approval requests + ledger | 8.6 | **8.6** | untouched (kept standalone — safety gate must fire even unplanned) |
| **jail-quarantine** 1.1.0 | Adoption gate + sensitive halt + inline paste scan | Quarantine report | 8.6 | **8.6** | untouched this wave |
| **jail-red-team** 1.1.0 | Pressure-test before shipping; falsifier per finding; pre-mortem-lite | Ranked findings + falsifiers + verdict | 8.6 | **8.6** | untouched this wave |
| **jail-memory** 1.3.0 | Govern durable memory: six-check gate, supersede-don't-delete, postmortems | **Markdown memory system: MEMORY.md index + dated provenance-headed entry files** | 8.5 | **8.6** | file system elevated to first-class — concrete index + per-entry header schema (id/type/created/updated/source/status) makes memory portable and auditable on any platform |
| **jail-handoff** 1.2.0 | Session handoff: state with proof, decisions-with-why, secrets redacted | The handoff document | 8.5 | **8.5** | renamed from jail-baton (name aligns with JAIL-HANDOFF vocabulary); value unchanged |
| **jail-prototype** 1.1.0 | Throwaway prototypes answering named design questions | Verdict + evidence + spike-ledger entry | 8.3 | **8.3** | untouched this wave |
| **jail-skill-miner** 1.2.0 | Mine disciplines + the suite's self-maintenance loop | Candidate table → approved artifact sets | 8.2 | **8.2** | untouched this wave |

## Layer 2 — Workflow

| Skill | Purpose / use case | Output | Was | Now | Evidence for the move |
|---|---|---|:---:|:---:|---|
| **jail-rate** 2.0.0 | Rate anything **0.0–10.0**, type-matched weighted rubric, cited evidence | Rubric + evidence-cited scorecard + recommendations | 8.8 | **8.8** | scale + validator confirmed 0.0–10.0 at 0.1 increments this wave; content untouched |
| **jail-prospect** 1.3.0 | Free-source company screening: sell-side + vendor/competitor/partner vetting | Purpose-fit scored brief, fully cited | 8.5 | **8.5** | untouched this wave |
| **jail-rate-skill** 2.2.0 | QA instrument for AI skills; measured evidence outranks inspection | Rating matrix + validated JSON record | 8.4 | **8.4** | untouched this wave |
| **jail-summarize** 1.2.0 | Decision-forcing executive communication; tech → business consequences | Seven-part brief ending in the forced decision | 8.3 | **8.3** | renamed from jail-exec-brief (broader name); value unchanged |

## Layer 3 — Frameworks

| Skill | Purpose / use case | Output | Was | Now | Evidence for the move |
|---|---|---|:---:|:---:|---|
| **jail-cpr** 1.3.0 | Meetings, both halves: Results-first design + post-meeting debrief | **DOCX (default) or PDF document** — CPR/agenda or decisions/actions/audit | 8.5 | **8.6** | the deliverable is now a polished Word/PDF file (via docx/pdf skills), not chat text — a hand-out-ready artifact |
| **jail-strategy** 1.1.0 | SWOT→TOWS, PESTLE+tripwires, or full sweep — one evidence base | Classified tables + strategies/implications + tripwires | 8.3 | **8.3** | renamed from jail-strategy-scan (shorter name); value unchanged |
| **jail-bmc** 1.2.0 | Evidence-labeled Business Model Canvas + validation pipeline | Canvas + coherence findings + lab-shaped experiments | 8.2 | **8.2** | untouched this wave |

## JAIL-PY companions

| Skill | Purpose / use case | Output | Was | Now | Evidence for the move |
|---|---|---|:---:|:---:|---|
| **jail-py-lab** 1.1.0 | Runnable lab bookkeeping + wave-over-wave comparison | Ledger + trajectory + exit-coded regression check | 8.2 | **8.2** | untouched; ran the wave-3 ledger in anger again |
| **jail-py-toolkit** 1.0.0 | Prompt + rating machine checks, one install, release-wired | Exit-coded verdicts; 9 scripts | 8.0 | **8.0** | untouched |

**Suite mean value: 8.53** across 26 skills (was 8.50 across 27 at 0.23.0) ·
**18 of 26 at ≥ 8.5**. The merge removed a lane-duplication (two planning
skills → one two-lane jail-plan) without losing coverage; the three content
upgrades (research dual-output, memory file-system, cpr document-output) each
moved their skill on a real capability change, not a rename.

## The honest remainder (below 8.5, and why)

Eight skills sit at 8.0–8.4 after this wave: prototype 8.3 · summarize 8.3 ·
strategy 8.3 · rate-skill 8.4 · skill-miner 8.2 · bmc 8.2 · py-lab 8.2 ·
py-toolkit 8.0. The caps are structural, not build-quality:
occasional-by-nature triggers, commodity-format cores, code-execution
dependence, narrow audience. What would move them: recorded real-usage
frequency (jail-memory postmortems now capture it on the new file system),
live skill-miner cycles, and rate-skill becoming the enforced pre-release
gate. Inflating them without evidence would break the determinism rule the
catalog runs on.
