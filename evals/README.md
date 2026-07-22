# Evals — how to re-run the validation loop

This folder holds the plugin's test sets. Re-run the relevant set whenever you change a skill's `SKILL.md` or references, so improvements are evidence-backed rather than vibes.

## Files

**MP-adaptation wave** (0.21.0 — authored 2026-07-19): `mp-wave-evals.json` — 4 triggers, 4 routing near-misses, 4 behavioral cases (loop-refusal, throwaway enforcement, baton redaction, plan-not-do).

**jail-council** (0.20.0 — authored 2026-07-19): `jail-council-evals.json` — 4 triggers, 3 routing near-misses, 5 behavioral cases (tier honesty, anonymization, mandatory error-hunt, evidence-beats-votes, audit-appendix-or-theater). A live Tier-C run is recorded in docs/smoke-tests-0.19.0.md (0.20.0 addendum).

**Kernel + frameworks** (0.18.0 wave 1 — authored 2026-07-19, not yet run):
- `kernel-trigger-evals.json` — 17 should-trigger + 12 cross-routing near-misses (the kernel's collision set: verify vs rate vs red-team, decide vs rate, research vs prospect-research, memory refusing secrets).
- `kernel-evals.json` — 11 behavioral cases covering the 8 required types (normal, ambiguous, missing evidence, contradictory, routes-elsewhere, should-not-trigger, security, partial failure) + 3 integration chains (research→PESTLE→decide→brief · contract→orchestrate→verify · lab loop).

**jail-rate** (v2.0.0 universal rebuild — authored 2026-07-19, not yet run):
- `jail-rate-trigger-evals.json` — 10 should-trigger + 6 near-miss routing cases (jail-rate-skill / jail-prospect handoffs, people-boundary declines).
- `jail-rate-evals.json` — 4 behavioral cases with grader assertions (type classification + declared rubric, private-subject handling, people boundary, critical-flaw cap).

**jail-prompt:**
- `evals.json` — 11 behavioral cases (as of v1.2.0, repaired from a truncated file and extended with **Lite-lane** and **connector-routing** coverage). Each has a `prompt`, an `expected_output`, and (in the workspace copies) an `assertions` list the grader checks.
- `trigger_evals.json` — 20 triggering cases (10 should-trigger, 10 tricky near-misses) for description tuning.

> **Latest run:** see [`RESULTS.md`](RESULTS.md) — v1.2.0 proxy run scored **20/20 triggering** (two independent judges, unanimous) and **4/4 behavioral** cases (incl. both new behaviors), all assertions PASS.
>
> **Open validation item (carried since 0.9.0):** results so far are **subagent-proxy**, not the live `claude -p` harness, and the behavioral runs were single-turn. The live CLI harness run and a true multi-turn exercise still need an authenticated environment (see the triggering loop below). Don't upgrade "proxy" to "harness-verified" until that run lands.

## Behavioral loop (the main one)

The workflow uses the **skill-creator** skill. In Cowork (has subagents):

1. **Run** each case twice — once with the current skill, once with the previous version as baseline — saving outputs to a workspace laid out as `iteration-N/eval-<id>/<config>/run-<r>/outputs/`.
2. **Grade** with a *fresh, independent* subagent (it reads `agents/grader.md`) against the assertions — do not grade your own outputs; that conflict cost real accuracy here.
3. **Aggregate**: `python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name jail-prompt` → `benchmark.json` + `.md` (pass rate, time, tokens, mean ± stddev).
4. **Review**: `python eval-viewer/generate_review.py <workspace>/iteration-N --skill-name JAIL-PROMPT --benchmark .../benchmark.json --static viewer.html` (use `--static` in headless/Cowork).
5. **Improve → repeat.** Run key cases **3×** to measure variance — single runs hide flakiness (that's how the least-privilege regression was found).

## Triggering loop (pending real run)

`trigger_evals.json` feeds the description optimizer:

```
python -m scripts.run_loop --eval-set evals/trigger_evals.json \
  --skill-path . --model <session-model-id> --max-iterations 5 --verbose
```

This needs an authenticated `claude` CLI and a writable `.claude/commands/` — neither was available at build time, so 0.9.0 used a subagent **proxy** instead (3 independent judges voting per query). Replace the proxy result with a real run before tagging 1.0.

## What "good" looks like

- Behavioral: 100% of assertions pass, **with discriminating assertions** (some should be capable of failing — all-pass-always means the test isn't testing).
- Triggering: should-trigger ≥ ~0.9 trigger rate, near-misses ≤ ~0.1, on a held-out split.
