# Summarizer guide — staying within budget on large targets

Rating a skill must not blow the context window. When a target skill's files are
large, summarize instead of reading them whole.

## The 300-line rule
- Any single reference/script file **> 300 lines**: do not read it in full. Read
  the first ~80 and last ~40 lines, plus headings, then summarize its purpose,
  inputs/outputs, and anything rating-relevant (guardrails, determinism, exit
  checks) in 3–6 lines.
- `SKILL.md` itself is always read in full — it's the contract under review.
- Prefer `grep` for targeted evidence (e.g. `temperature`, `injection`, `schema`,
  `assert`, `file:///`) over linear reads.

## Token budget
- Aim to keep total input for one rating under ~4,000 tokens of target material.
- For batch mode, summarize each skill independently; never hold more than one
  target's full contents in context at once.

## What to capture from a summarized file
For each large file, record only what changes a category score:
- scripts → does it validate / assert / enforce anything? (Execution Reliability,
  Machine-Verifiable Exit Criteria)
- references → does it define determinism, safety, or portability conventions?
- anything with `file:///` absolute paths → Client Portability penalty.

If summarization means you couldn't verify a claim, score the relevant category
conservatively and note the unread evidence in the rationale.
