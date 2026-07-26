# jail-py-lab

This skill is the runnable bookkeeper for a jail-lab experiment loop: it logs every measured try to a file and tells you what to keep.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.2.0.

## What it does

You run [jail-lab](../jail-lab/SKILL.md)'s loop: try one change, measure it, keep it or throw it away. This skill is the code that does the measuring and record-keeping for you. It appends each try to a ledger (a plain text log, one line of JSON per entry, that you never edit by hand). It compares the new number to the best one so far and prints KEEP or DISCARD. A second script reads the whole ledger back and shows your trajectory. A third compares two ledgers, or two points in one ledger, so you can catch a regression before it ships.

## Use it when

- "I changed the trigger wording for a skill — log this experiment and tell me if it's better."
- "What's the best result so far in this lab?"
- "Compare this wave's ledger to last wave's and tell me if we regressed."
- "Wire up a metric command so I stop typing numbers in by hand."

## Don't use it for

- Deciding what to try next, or whether an idea is worth testing at all — that discipline lives in [`jail-lab`](../jail-lab/), which this skill only keeps the books for.
- A one-time score with no iteration — use [`jail-rate`](../jail-rate/) instead.
- A single before/after check with no ongoing ledger — use [`jail-verify`](../jail-verify/) instead.
- A session with no code execution — fall back to jail-lab's manual markdown ledger. This skill needs Python 3.8 or later; the core skills like jail-lab work fine without it.

## What you get

A ledger file that grows one line per experiment, a console line per run (`KEEP`, `DISCARD`, or `BASELINE`, with the metric and the new best), and, on request, a full trajectory report or a delta between two ledgers.

## Example

**You ask:**

> I'm tuning the trigger description for the handoff skill. Baseline pass rate is 0.81, higher is better. Log the baseline, then log two experiments I already measured: concrete trigger verbs got 0.87, a long synonym list got 0.83. Then show me the report.

**It produces:**

```
$ python3 lab-run.py --ledger "$LEDGER" --direction max --baseline --change "unmodified baseline description" --metric 0.81
[lab-run] #0 BASELINE •  metric=0.81  best=0.81  change='unmodified baseline description'
EXIT_CODE=0

$ python3 lab-run.py --ledger "$LEDGER" --direction max --change "added concrete trigger verbs (sign out, resume later)" --hypothesis "concrete verbs match real user phrasing better than abstract nouns" --metric 0.87 --evidence "evals/handoff-wave4.txt"
[lab-run] #1 KEEP ▲  metric=0.87  best=0.87  change='added concrete trigger verbs (sign out, resume later)'
EXIT_CODE=0

$ python3 lab-run.py --ledger "$LEDGER" --direction max --change "added long synonym list (pause, suspend, park, shelve)" --hypothesis "more synonyms should catch more phrasings" --metric 0.83
[lab-run] #2 DISCARD ▼  metric=0.83  best=0.87  change='added long synonym list (pause, suspend, park, shelve)'
[lab-run] revert this change — a regression never stays.
EXIT_CODE=1

$ python3 lab-report.py --ledger "$LEDGER"
JAIL-LAB REPORT — C:/Users/Jonathan R. Fuller/.claude/jobs/e61aab73/tmp/jail-py-lab-demo-ledger.jsonl
  direction: max  ·  experiments: 2  ·  entries: 3
  baseline:  0.81  (unmodified baseline description)
  best:      0.87
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
