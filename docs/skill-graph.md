# FHSkillz skill graph — routing registry

The plugin's routing map: what each skill consumes/produces, which skills it
may invoke, and its risk posture. Invocation is by **name** (model-invoked;
no hard runtime dependency): a skill that references another gracefully
degrades to the named inline fallback when the target isn't installed.
Chains are **directed and acyclic** — a skill never invokes anything that
invokes it back in the same run; iteration happens only through jail-lab's
bounded loop or a human checkpoint. Handoffs use the JAIL-HANDOFF block
(docs/JAIL-CONSTITUTION.md); downstream skills consume the block, not prose.

## Layer 1 — Reasoning kernel

| Skill | Consumes | Produces | May invoke | Invoked by | Data sensitivity | Failure behavior |
|---|---|---|---|---|---|---|
| jail-task-contract | raw request | task contract | jail-prompt (prompt deliverables) | everything | low | blocking ambiguity → stop + ask |
| jail-research | contract / question | evidence packet | jail-orchestrate (parallel streams), jail-quarantine (inbound data) | jail-decide, frameworks, jail-rate | medium (external fetches) | unanswerable → Unknowns in packet |
| jail-verify | any deliverable + its contract | verdict + ranked fixes | — (terminal check; independence required) | everything | low | missing contract → verify vs request verbatim, flagged |
| jail-decide | evidence packet / analysis | decision package | jail-research (gaps), jail-red-team (contested) | frameworks, jail-operationalize | low | thin evidence → assumption-labeled or route back |
| jail-red-team | draft plan/claim/analysis | ranked findings + verdict | — | jail-decide, frameworks, jail-prompt (high-stakes) | low | nothing found → "holds" is valid |
| jail-orchestrate | parallelizable plan | integrated result + ledger | jail-research (per stream), jail-verify (merge) | jail-task-contract, jail-research | inherits streams' | node unverified → not complete; resume from ledger |
| jail-approval-gate | intended actions | tiered inventory + approvals | jail-quarantine (sensitive classes) | any acting skill | high | unclassified → PER-ACTION; no response → not approved |
| jail-quarantine | inbound/bulk/sensitive data | adopted data + halt report | jail-approval-gate | jail-research, jail-memory, extraction tasks | high | safe path unavailable → skip (fail closed) |
| jail-memory | lessons/decisions/context | governed memory entries | jail-approval-gate (durable writes) | jail-task-contract (retrieval), jail-cpr | medium | gate fails → don't store + say why |
| jail-lab | improvable artifact + metric | experiment ledger + best | jail-py-lab (bookkeeping) | jail-operationalize, skill iteration | low | no metric → refuse or route to jail-rate |
| jail-skill-miner | codebase/history | candidate table → skills | jail-rate-skill (QA), jail-approval-gate (author stop) | user | low | unverified citation → dropped |
| jail-prompt | vague goal | engineered prompt / STOP | jail-py-prompt-tools, any skill via auto-triage | jail-task-contract | low | flawed premise → STOP |

## Layer 2 — Workflow skills

| Skill | Consumes | Produces | May invoke | Invoked by |
|---|---|---|---|---|
| jail-operationalize | decision/recommendation | 13-field operating workflow | jail-verify (readiness), jail-lab (metric loop) | jail-decide, frameworks |
| jail-exec-brief | any complex material | decision-ready brief | — (voice layer) | frameworks, jail-decide, kernel chains |
| jail-rate | any ratable subject | 0–10 scorecard, cited | jail-research (evidence), jail-rate-skill / jail-prospect (handoffs) | jail-decide (option scoring) |
| jail-rate-skill | AI skill directory | 10-category matrix + record | jail-py-rate-tools, skill-creator (behavioral) | jail-skill-miner |
| jail-prospect | company name | prospect brief | — | jail-research (domain handoff) |

## Layer 3 — Domain packs

| Skill | Chain (in order; inline fallback per step) |
|---|---|
| jail-pestle | task-contract → research → classify 6 dims → red-team → decide → exec-brief → verify |
| jail-swot | task-contract → research → classify+sort rules → red-team → TOWS → decide → exec-brief → verify |
| jail-bmc | task-contract → research → 9 blocks → coherence pass → red-team → assumption-ranking/experiments → decide → exec-brief → verify |
| jail-cpr | task-contract → memory retrieval → CPR (exec-brief voice) → agenda-from-Results → verify |

Wave 3 (planned, not shipped): docs/ROADMAP-wave3-domain-packs.md.

## Anti-patterns the graph forbids
- **Circular invocation** — chains are DAGs; verify/red-team never invoke
  their producer in the same run.
- **Unbounded recursion** — jail-orchestrate depth cap (1 without explicit
  approval) is the only fan-out mechanism.
- **Duplicate research** — one evidence packet per run; downstream skills
  cite it rather than re-searching (gaps route back to jail-research, which
  appends).
- **Silent overrides** — a downstream skill disagreeing with an upstream
  verified finding surfaces the conflict (jail-research contradiction rule);
  it never quietly rewrites it.
- **Unstructured handoffs** — kernel skills end with JAIL-HANDOFF; a
  downstream skill missing a required key stops and asks, it doesn't
  improvise.
- **Approval laundering** — tiers travel through delegation
  (jail-approval-gate ∘ jail-orchestrate).
