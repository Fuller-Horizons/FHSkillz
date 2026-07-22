# FHSkillz skill catalog — purpose, output, and value (0.19.0)

*2026-07-19 · Value = single-rater judgment on the jail-rate anchors (9–10 exceptional · 8–8.9 excellent · 7–7.9 good), weighing frequency of use × impact per use × what the skill adds over an unaided capable model. This is a different axis than the build-quality matrix (docs/skill-matrix-0.18.0.md): a narrow, perfectly-built tool can score 8.2 there and 7.2 here.*

## L1 — Reasoning kernel

| Skill | Purpose / use case | Output | Value |
|---|---|---|:---:|
| **jail-prompt** 2.0.0 | Pre-flight for any AI task: triages stakes, kills bad-fit/flawed-premise work (STOP), engineers the rest into verifiable prompts | Engineered prompt block (or chain + manifest), or a STOP with next-step choices | **9.0** |
| **jail-task-contract** 1.0.0 | Turn an ambiguous request into an executable contract before work starts; guard scope after — material change = new contract | 14-field task contract + JAIL-HANDOFF; blocking questions when guessing would be costly | **8.5** |
| **jail-research** 1.0.0 | Gather evidence anyone can audit: answerable questions, tiered dated sources, contradictions weighed not averaged | Evidence packet (findings labeled Fact/Inference/Estimate/Unknown + numbered dated sources + gaps) | **8.5** |
| **jail-verify** 1.0.0 | Independently confirm finished work is done-done — artifacts from the current run, never an agent's say-so | PASS/FAIL/PASS-WITH-FLAGS verdict, per-check failing observations, ranked fixes | **9.0** |
| **jail-decide** 1.0.0 | Choose among options defensibly: criteria before options, do-nothing always priced, reversibility named | Decision package (options table, recommendation + confidence + change-conditions + next actions) | **8.5** |
| **jail-red-team** 1.0.0 | Attack a draft plan/claim before it ships: steelman first, three lenses, bias sweep on consequential calls | Ranked findings (severity × likelihood) each with fix/falsifier + PROCEED/RETHINK verdict | **8.3** |
| **jail-orchestrate** 1.0.0 | Run multiple agents as one system: earn delegation, fence scopes, verify nodes, merge by evidence | Integrated single result + dependency/resume ledger with artifact-verified nodes | **8.0** |
| **jail-approval-gate** 1.0.0 | Decide before acting what needs a human: never / per-action / batchable / auto — failing closed | Tiered action inventory + approval request blocks + authorization ledger | **8.4** |
| **jail-quarantine** 1.0.0 | Two gates: inbound data adopted only after review; protected data halts processing and fails closed | Quarantine report (adopted / needs-review / halts / injection attempts defused) | **8.4** |
| **jail-memory** 1.0.0 | Govern durable memory: six-check ingestion gate, update-don't-duplicate, supersede-don't-delete + postmortem ritual | Stored/refused entries with provenance + distilled postmortem lessons | **8.0** |
| **jail-lab** 1.0.0 | Improve anything measurable by experiment: one variable, bounded run, keep/discard vs best, audit ledger (autoresearch pattern, MIT) | Append-only experiment ledger + baseline→best report with keep rate and discard lessons | **8.6** |
| **jail-skill-miner** 1.0.0 | Mine codebases/histories for reusable disciplines; 4-box filter, dedup vs installed skills, stop for approval | Candidate table (evidence · discipline · failure prevented · NEW/EXTENDS/DUPLICATE · rank), then authored skills on approval | **7.5** |

**Why these values:** **jail-prompt** 9.0 — Fires on nearly every vague ask; prevents the most expensive failure (doing the wrong thing well); most distinctive skill in the suite · **jail-task-contract** 8.5 — Universal entry point; kills scope drift and endless-revision loops — the two costs every project pays · **jail-research** 8.5 — Feeds every downstream decision/framework; provenance discipline is exactly what unaided models skip · **jail-verify** 9.0 — Prevents the highest-severity failure in agentic work: confident false completion; verifier≠producer is rare and valuable · **jail-decide** 8.5 — Frequent in business use; the do-nothing pricing and change-conditions upgrade real decisions, not just documents · **jail-red-team** 8.3 — Models flatter by default; a disciplined adversarial pass is high leverage exactly where stakes are high · **jail-orchestrate** 8.0 — Critical in agentic contexts (false-success plague, duplicated work); value concentrated where subagents exist · **jail-approval-gate** 8.4 — Max-severity protection (irreversible/external actions); makes agent autonomy safe enough to actually use · **jail-quarantine** 8.4 — Prevents leaked secrets, poisoned CRMs, and injection obedience — low frequency, severe consequence · **jail-memory** 8.0 — Compounding value — every future session inherits clean memory instead of folklore; refusals are half the point · **jail-lab** 8.6 — Converts 'make it better' vibes into measured progress; applies to prompts, skills, code, content, funnels · **jail-skill-miner** 7.5 — Occasional use but leveraged — it is how the plugin grows without bloating; the dedup gate protects all 24

## L2 — Workflow

| Skill | Purpose / use case | Output | Value |
|---|---|---|:---:|
| **jail-rate** 2.0.0 | Rate anything 0.0–10.0 on a type-matched weighted rubric with cited empirical evidence; current → projected | Declared rubric + evidence-cited scorecard + ranked recommendations + dated sources + confidence | **8.8** |
| **jail-operationalize** 1.0.0 | Convert a recommendation into a runnable operating workflow a named owner could execute Monday | 13-field spec: trigger→inputs→actions→tool→owner→approval→output→evidence→metric→frequency→risk→next→completion standard | **8.7** |
| **jail-exec-brief** 1.0.0 | Compress complex/technical material into decision-ready executive communication; tech → business consequences | Seven-part brief: answer-first, facts labeled, risks priced, one recommendation, next actions | **7.8** |
| **jail-rate-skill** 2.1.0 | QA instrument for AI skills: 10-category matrix, untrusted-target rules, machine-validated record | Rating matrix + IDE/CLI compatibility + JSON record (validated, history-tracked) | **7.8** |
| **jail-prospect** 1.2.0 | Screen a US private company as a sell-side/consulting prospect from free sources only; never fabricates | One-page brief: Likelihood-to-Sell + Consulting-Opportunity (0–100), red flags, outreach hook, cited appendix | **8.2** |

**Why these values:** **jail-rate** 8.8 — Extremely broad trigger surface; evidence-before-score and the projection make it decision-grade, not vibes · **jail-operationalize** 8.7 — Directly attacks the 'analysis that stops at advice' failure — your most-rejected output class; very consulting-marketable · **jail-exec-brief** 7.8 — Frequent use and audience-critical, but closest to unaided-model behavior — the translation rules are the real delta · **jail-rate-skill** 7.8 — Narrow audience but load-bearing: it is the plugin's own quality gate and the wave-3 entry bar · **jail-prospect** 8.2 — Money-adjacent with a direct decision output; narrower audience than the kernel but high impact per use

## L3 — Frameworks

| Skill | Purpose / use case | Output | Value |
|---|---|---|:---:|
| **jail-pestle** 1.1.0 | Macro-environment analysis tied to a specific subject + decision — never a trend listicle | Six-dimension factor tables (trend/likelihood/magnitude/time/O-T/confidence) + interactions + tripwires | **7.5** |
| **jail-swot** 1.1.0 | Evidence-sorted SWOT (aspirations rejected, weather ≠ opportunity) converted into TOWS strategies | Prioritized SWOT matrix + TOWS combinations + vulnerabilities + recommended actions | **7.6** |
| **jail-bmc** 1.1.0 | Business Model Canvas where validated info and hypotheses never blur; riskiest assumptions get experiments | Nine labeled blocks + coherence findings + unit economics + sequenced validation experiments | **7.8** |
| **jail-cpr** 1.1.0 | Context·Purpose·Results meeting design; agenda reverse-engineered from testable Results | CPR + owned/timed/output-typed agenda + pre-work + action-item template | **8.0** |

**Why these values:** **jail-pestle** 7.5 — Solid consultant deliverable; value bounded by the framework's commodity nature — the evidence discipline is the differentiator · **jail-swot** 7.6 — The sorting traps + mandatory TOWS turn a box-filling exercise into strategy; frequent in advisory work · **jail-bmc** 7.8 — Best of the frameworks — the V/H discipline and experiment sequencing fix how BMCs actually get misused · **jail-cpr** 8.0 — Meetings are universal and mostly wasted; immediate payoff every single use; strong client-facing artifact

## JAIL-PY companions

| Skill | Purpose / use case | Output | Value |
|---|---|---|:---:|
| **jail-py-prompt-tools** 1.0.0 | Runnable enforcement for jail-prompt: secret scan, prompt/chain/truth lint, dry-run | Exit-coded verdicts with named findings (real checks, not self-assessment) | **7.5** |
| **jail-py-rate-tools** 1.0.0 | Runnable validation/persistence for ratings: record check, history + deltas, variance, structure lint | Exit-coded validation (tamper-proof: rejects a fudged overall) + rating-history.jsonl | **7.2** |
| **jail-py-lab** 1.0.0 | Runnable bookkeeping for jail-lab: measured entries, keep/discard verdicts, trajectory reports | Append-only JSONL ledger + report (baseline→best, keep rate, stop-condition status) | **7.8** |

**Why these values:** **jail-py-prompt-tools** 7.5 — Turns the flagship's rules from 'told to' into 'enforced'; value scoped to code-execution contexts · **jail-py-rate-tools** 7.2 — Narrowest scope in the suite, but it makes rating integrity mechanical — scores can't be quietly edited · **jail-py-lab** 7.8 — The difference between doing the lab discipline and skipping it; guards (direction lock, hypothesis required) enforced in code

**Suite mean value: 8.14** across 24 skills · spread 7.2–9.0. The kernel out-values the frameworks because its failures are severer and its disciplines are least replaceable by an unaided model; frameworks earn their place as evidence-disciplined versions of commodity formats; companions score on enforcement, bounded by needing code execution.