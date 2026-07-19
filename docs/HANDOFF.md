# Handoff: prompt-preflight skill

## What this is
A Claude skill ("prompt-preflight") that converts a vague desired result into either a STOP decision or an engineered, verifiable, token-efficient prompt — after a viability gate. Built from scratch in a Claude chat session; moving to Cowork to run the full test/eval loop (Cowork has subagents).

## Current file
`SKILL.md` (this folder) — the working skill. ~76 lines.

## Design decisions made (and why)
- **3 phases:** Frame & Clarify -> Viability gate -> Engineer the prompt. Collapsed from an earlier 4-phase draft for efficiency.
- **One batched clarify round**, not an open loop — avoids question fatigue.
- **Viability gate is the core** (right tool? / groundable? / effort vs payoff? / enhancement? / secure?). Includes a readiness gate: advance only when confident output will be efficient, secure, logical, premium — but never fake the confidence number; name and resolve blockers instead.
- **STOP path** offers a multiple-choice next step (reframe / non-AI approach / proceed with caveats / drop).
- **Karpathy principles folded in** (from andrej-karpathy-skills + llm-council review): state assumptions, surface 2+ interpretations on ambiguity, imperative->verifiable-goal framing, Simplicity First (no unrequested scope).
- **Output skeleton** (ROLE/OBJECTIVE/SUCCESS TEST/PROCESS/SOURCES/CONSTRAINTS/BEFORE RETURNING) for consistent premium output.
- **Worked example** included (PM-tool comparison) — examples teach behavior better than rules.
- **Did NOT embed llm-council** — it's multi-model infra, ~5x token cost, contradicts the efficiency premise. Optional "council check" escalation for high-stakes only was discussed, not yet added.

## Scoring (pre-validation baseline)
Weighted rubric, 10 categories. Overall ~7.5/10.0. Lowest: Validation 3.0 (no tests). After one live test + security fix: Validation ~5.5, Robustness ~7.5.

| Category | Weight | Score |
|---|---|---|
| Triggering/description | 15% | 7.5 |
| Clarity/actionability | 10% | 8.5 |
| Workflow structure | 12% | 8.5 |
| Token efficiency | 8% | 9.0 |
| Output-quality mechanisms | 12% | 8.0 |
| Examples | 8% | 7.5 |
| Robustness/edge cases | 10% | 7.5 (after fix) |
| Authority/verification | 10% | 7.5 |
| Validation/evidence | 10% | 5.5 (after 1 run) |
| Goal alignment | 5% | 8.5 |

## Validation status
- 1 live run completed (real task: self-hosting Portkey AI Gateway on Win11). Flow worked end-to-end; gate -> GO; produced a usable engineered prompt.
- That run surfaced + fixed one gap: Phase 2 now has an explicit **Secure?** check for credential/PII tasks.

## Next steps in Cowork
1. Read SKILL.md to get oriented.
2. Use the skill-creator skill's full loop (subagents available): write evals/evals.json with 3-5 varied prompts (include a STOP case and a fast-path/trivial case), run with-skill vs baseline in parallel, generate the eval viewer (`generate_review.py --static` for headless), review, iterate.
3. Target lifting Validation (#9) past 8 and confirming triggering reliability (#1).
4. Optionally run description optimization (run_loop.py) once the skill is stable.
5. Package with package_skill.py and present the .skill file.
