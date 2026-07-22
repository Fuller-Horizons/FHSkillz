---
name: jail-py-lab
metadata:
  version: 1.1.0
description: >-
  JAIL-PY machine bookkeeping for jail-lab experiment loops — runnable Python
  that appends measured experiments to an append-only JSONL ledger, computes
  keep/discard verdicts against the best-so-far, reports the trajectory, and
  compares ledgers or spans (A/B, wave-over-wave regression checks). Use when
  jail-lab is running and code execution is available: "log this experiment",
  "what's the best so far", "summarize the lab ledger", "compare this run to
  the last one", or to wire a metric command so measurement is automatic.
  Requires code execution (Python 3.8+, stdlib only). Not for deciding WHAT
  to try — that's jail-lab's discipline.
---

# JAIL-PY-LAB

The runnable half of [jail-lab](../jail-lab/SKILL.md): mechanical, honest
bookkeeping for experiment loops. Pattern adapted from Andrej Karpathy's
[autoresearch](https://github.com/karpathy/autoresearch) (MIT). Stdlib-only
Python 3.8+; stable exit codes.

## The three tools

| Script | What it does | Exit |
|---|---|---|
| `scripts/lab-run.py` | Appends one experiment to the JSONL ledger: takes the change + hypothesis, gets the metric (from `--metric VALUE` or by running `--metric-cmd` and parsing the last number of its output), compares against best-so-far per the declared direction, records KEEP/DISCARD. `--baseline` records experiment #0. | 0 keep/baseline · 1 discard · 2 error |
| `scripts/lab-report.py` | Reads the ledger: baseline → best trajectory, keep rate, kept-changes list, last entries, and stop-condition status (consecutive discards). | 0 ok · 2 error |
| `scripts/lab-compare.py` | Delta between two ledgers (`--against`: this wave vs last wave) or across a span of one ledger (`--from-id/--to-id`): best-vs-best with absolute + percent delta, keep rates, kept changes. Exit code IS the regression check — wire it into a release gate. | 0 improved-or-equal · 1 regressed · 2 error |

This toolkit is also the FHSkillz suite's own metrics engine: the repo's
trigger-accuracy ledger (`evals/results/trigger-accuracy-ledger.jsonl`) is
a jail-py-lab ledger, and release baselines compare wave-over-wave with
`lab-compare.py`.

## Usage (plain language → flags)

```bash
# "Start the lab: measuring eval pass rate, higher is better, currently 0.72"
python3 scripts/lab-run.py --ledger lab-ledger.jsonl --direction max \
  --baseline --change "unmodified baseline" --metric 0.72

# "I tightened the description; I think triggering improves. New score: 0.78"
python3 scripts/lab-run.py --ledger lab-ledger.jsonl --direction max \
  --change "tightened trigger description" \
  --hypothesis "more concrete verbs -> better routing" \
  --metric 0.78 --evidence evals/run-14.txt

# Automatic measurement: run a command, last number in its output = metric
python3 scripts/lab-run.py --ledger lab-ledger.jsonl --direction min \
  --change "cache prompt prefix" --hypothesis "fewer tokens/query" \
  --metric-cmd "python3 bench.py --quiet"

# "Where are we?"
python3 scripts/lab-report.py --ledger lab-ledger.jsonl
```

## Ledger format (append-only JSONL — never edit past lines)
`{"id", "ts", "change", "hypothesis", "metric", "direction", "verdict",
"best_after", "evidence"}` — one experiment per line; the file is the audit
log jail-lab requires. Discards stay forever; they're data.

## Gotchas
- **Editing the ledger.** Fixing history invalidates the audit trail. Wrong
  entry? Append a correction entry that supersedes it.
- **Direction flip mid-run.** `--direction` must match the lab declaration
  every call; the script refuses a ledger whose direction disagrees.
- **Metric-cmd noise.** The parser takes the LAST number in stdout — keep
  the command's output clean or print the metric last.
- **Verdicts overridden by hand.** If you keep a DISCARD anyway, the ledger
  and reality have diverged — jail-lab's discipline is broken, and the
  report will say so.
- **Where code can't run**, don't fake entries — use jail-lab's manual
  markdown ledger and say so.
