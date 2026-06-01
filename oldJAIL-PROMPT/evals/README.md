# Evals — how to re-run the validation loop

This folder holds the test sets used to validate JAIL-PROMPT. Re-run them whenever you change `SKILL.md` or the references, so improvements are evidence-backed rather than vibes.

## Files

- `evals.json` — 10 behavioral cases. Each has a `prompt`, an `expected_output`, and (in the workspace copies) an `assertions` list the grader checks.
- `trigger_evals.json` — 20 triggering cases (10 should-trigger, 10 tricky near-misses) for description tuning.

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
