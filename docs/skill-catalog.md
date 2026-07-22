# FHSkillz skill catalog — purpose, output, and value (0.20.0)

*2026-07-19 · Value = single-rater judgment on the jail-rate anchors (9–10 exceptional · 8–8.9 excellent · 7–7.9 good), weighing frequency × impact per use × what the skill adds over an unaided capable model. Different axis than the build-quality matrix (docs/skill-matrix-0.18.0.md). Scores carried per the determinism rule for unchanged skills; jail-council added at 0.20.0.*

## Layer 1 — Reasoning kernel

| Skill | Purpose / use case | Output | Value |
|---|---|---|:---:|
| **jail-prompt** 2.0.0 | Pre-flight for any AI task: triages stakes, kills bad-fit/flawed-premise work (STOP), engineers the rest into verifiable prompts | Engineered prompt block (or chain + manifest), or a STOP with next-step choices | **9.0** |
| **jail-verify** 1.0.0 | Independently confirm finished work is done-done — artifacts from the current run, never an agent's say-so | PASS/FAIL/PASS-WITH-FLAGS verdict, per-check failing observations, ranked fixes | **9.0** |
| **jail-lab** 1.0.0 | Improve anything measurable by experiment: one variable, bounded run, keep/discard vs best, audit ledger (autoresearch pattern, MIT) | Append-only experiment ledger + baseline→best report with keep rate | **8.6** |
| **jail-task-contract** 1.0.0 | Turn an ambiguous request into an executable contract before work starts; guard scope after — material change = new contract | 14-field task contract + JAIL-HANDOFF; blocking questions when guessing is costly | **8.5** |
| **jail-research** 1.0.0 | Gather evidence anyone can audit: answerable questions, tiered dated sources, contradictions weighed not averaged | Evidence packet (labeled findings + numbered dated sources + honest gaps) | **8.5** |
| **jail-decide** 1.0.0 | Choose among options defensibly: criteria before options, do-nothing always priced, reversibility named | Decision package (options table, recommendation + confidence + change-conditions) | **8.5** |
| **jail-council** 1.0.0 | Maximum-accuracy deliberation on consequential/contested questions: blind multi-model answers, anonymized adversarial review, verification round, evidence-decided synthesis — cost disclosed, never gated; Tier-A cross-provider native in OpenCode CLI | Council answer + per-claim confidence + dissent register + audit appendix | **8.4** |
| **jail-approval-gate** 1.0.0 | Decide before acting what needs a human: never / per-action / batchable / auto — failing closed | Tiered action inventory + approval request blocks + authorization ledger | **8.4** |
| **jail-quarantine** 1.0.0 | Two gates: inbound data adopted only after review; protected data halts processing and fails closed | Quarantine report (adopted / needs-review / halts / injections defused) | **8.4** |
| **jail-red-team** 1.0.0 | Attack a draft plan/claim before it ships: steelman first, three lenses, bias sweep on consequential calls | Ranked findings (severity × likelihood) with fixes/falsifiers + verdict | **8.3** |
| **jail-orchestrate** 1.0.0 | Run multiple agents as one system: earn delegation, fence scopes, verify nodes, merge by evidence | Integrated single result + dependency/resume ledger with verified nodes | **8.0** |
| **jail-memory** 1.0.0 | Govern durable memory: six-check ingestion gate, update-don't-duplicate, supersede-don't-delete + postmortem ritual | Stored/refused entries with provenance + distilled postmortem lessons | **8.0** |
| **jail-skill-miner** 1.0.0 | Mine codebases/histories for reusable disciplines; 4-box filter, dedup vs installed skills, stop for approval | Candidate table (evidence · discipline · failure prevented · rank) → approved skills | **7.5** |

## Layer 2 — Workflow

| Skill | Purpose / use case | Output | Value |
|---|---|---|:---:|
| **jail-rate** 2.0.0 | Rate anything 0.0–10.0 on a type-matched weighted rubric with cited empirical evidence; current → projected | Declared rubric + evidence-cited scorecard + ranked recommendations + confidence | **8.8** |
| **jail-operationalize** 1.0.0 | Convert a recommendation into a runnable operating workflow a named owner could execute Monday | 13-field spec: trigger→…→metric→risk→testable completion standard | **8.7** |
| **jail-prospect** 1.2.0 | Screen a US private company as a sell-side/consulting prospect from free sources only; never fabricates | One-page brief: two 0–100 scores, red flags, outreach hook, cited appendix | **8.2** |
| **jail-exec-brief** 1.0.0 | Compress complex/technical material into decision-ready executive communication; tech → business consequences | Seven-part answer-first brief with facts/analysis labeled | **7.8** |
| **jail-rate-skill** 2.1.0 | QA instrument for AI skills: 10-category matrix, untrusted-target rules, machine-validated record | Rating matrix + IDE/CLI compatibility + validated JSON record | **7.8** |

## Layer 3 — Frameworks

| Skill | Purpose / use case | Output | Value |
|---|---|---|:---:|
| **jail-cpr** 1.1.0 | Context·Purpose·Results meeting design; agenda reverse-engineered from testable Results | CPR + owned/timed/output-typed agenda + pre-work + action template | **8.0** |
| **jail-bmc** 1.1.0 | Business Model Canvas where validated info and hypotheses never blur; riskiest assumptions get experiments | Nine labeled blocks + coherence findings + sequenced validation experiments | **7.8** |
| **jail-swot** 1.1.0 | Evidence-sorted SWOT (aspirations rejected, weather ≠ opportunity) converted into TOWS strategies | Prioritized matrix + TOWS + vulnerabilities + actions | **7.6** |
| **jail-pestle** 1.1.0 | Macro-environment analysis tied to a specific subject + decision — never a trend listicle | Six-dimension factor tables + interactions + early-warning tripwires | **7.5** |

## JAIL-PY companions

| Skill | Purpose / use case | Output | Value |
|---|---|---|:---:|
| **jail-py-lab** 1.0.0 | Runnable bookkeeping for jail-lab: measured entries, keep/discard verdicts enforced in code | Append-only JSONL ledger + trajectory report | **7.8** |
| **jail-py-prompt-tools** 1.0.0 | Runnable enforcement for jail-prompt: secret scan, prompt/chain/truth lint, dry-run | Exit-coded verdicts with named findings | **7.5** |
| **jail-py-rate-tools** 1.0.0 | Runnable validation/persistence for ratings — tamper-proof records, history deltas, variance | Exit-coded checks + rating-history.jsonl | **7.2** |

**Suite mean value: 8.15** across 25 skills · spread 7.2–9.0. The kernel out-values the frameworks because its failures are severer and its disciplines least replaceable by an unaided model; jail-council (8.4) is reserved for the calls that must be maximally right — proven in the live 0.20.0 smoke run, where anonymized review caught a real error inside a unanimous council. Frameworks are commodity formats made valuable by evidence discipline; companions score on enforcement, bounded by needing code execution.

## Addendum (0.21.0) — Matt Pocock adaptation wave (MIT, attributed)

| Skill | Purpose / use case | Output | Value |
|---|---|---|:---:|
| **jail-diagnose** 1.0.0 | Feedback-loop-first defect diagnosis — red-capable repro before hypotheses; confirmed cause; mandatory regression case | Diagnosis report: loop · minimized case · cause+evidence · fix · proof | **8.6** |
| **jail-baton** 1.0.0 | Session-to-session handoff — compact state, decisions-with-why, references, next actions, redacted | The baton document | **8.2** |
| **jail-prototype** 1.0.0 | Throwaway prototypes answering a named design question; answer graduates, code dies | Verdict + evidence + archived artifact pointer | **7.9** |
| **jail-wayfind** 1.0.0 | Decision-ticket maps through fog until the way to a named destination clears | The map + cleared-way handoff | **7.6** |

Deltas also shipped (1.1.0 bumps): grill mode + facts-vs-decisions → jail-task-contract · two-axis ∥ review + preflight → jail-verify · tracer-bullet slicing + expand–contract → jail-orchestrate · ADR entry shape → jail-memory · invocation economics → jail-skill-miner. Quality quick-ratings (band-anchored): diagnose 8.4 · prototype 8.2 · baton 8.2 · wayfind 8.1.
