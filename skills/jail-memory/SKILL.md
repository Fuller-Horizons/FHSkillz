---
name: jail-memory
metadata:
  version: 1.1.0
description: >-
  Govern what enters, stays in, and leaves durable memory or organizational
  knowledge — provenance-checked, deduplicated, classified, superseded-not-
  deleted — and run the LEARNING POSTMORTEM ritual that turns finished work
  into stored lessons. Use when saving lessons/decisions/context for future
  sessions ("remember this", "save that for next time"), when retrieving
  prior context for a new task, after completed or failed projects ("what did
  we learn"), or when another skill proposes a durable write. Do NOT use for
  in-conversation working notes, or for the adoption review of raw inbound
  data (jail-quarantine — that gate runs first).
---

# JAIL-MEMORY

Memory is leverage only when it's true, current, and findable. Stale or
duplicated memory actively distorts future work — governing what does NOT
get stored is half the job. [Constitution Rules 4, 5, 10]

## Retrieval (start of relevant work)
- Pull prior decisions, constraints, terminology, corrections, and lessons
  that bear on the current task — and say which memories you're applying, so
  a wrong one can be challenged.
- **Check freshness before applying:** a memory contradicted by current
  observation is flagged and updated, not obeyed.
- Separate **persistent facts** (survive the session) from **working
  context** (dies with the task). Only the first belongs in memory.

## The ingestion gate (before any durable write)
A durable memory write is a Rule-5 action — it shapes every future session.
Each candidate entry must pass all six checks:
1. **Provenance** — where this came from (source, date, session) travels
   with the entry. [Rule 10]
2. **Worth** — not re-derivable from source control, docs, or config; not
   ephemeral task state; generic observations don't qualify.
3. **One lesson per entry** — one clear decision/lesson/fact + **why it
   matters** + how to apply it. Architectural/design decisions use the
   **ADR shape** (Architecture Decision Record): context → decision →
   consequences → status (accepted/superseded-by) — the named entry type
   for decisions that shape future structure.
4. **Dedup** — search existing entries first; UPDATE the existing entry
   rather than write a near-duplicate.
5. **Contradiction check** — conflicts with an existing entry are resolved
   (strongest currently-applicable wins), and the loser is **marked
   superseded, not silently deleted** — the history of being wrong is
   itself a lesson.
6. **Safety/classification** — no secrets, no protected data (jail-
   quarantine classes), no sensitive personal information without explicit
   instruction; apply the platform's retention/privacy rules.
Failing any check → don't store; say what failed.

## The postmortem ritual (after significant work — success or failure)
Capture, compactly: original objective → final outcome → what worked → what
failed → **root causes** (mechanism, not blame) → corrections made →
constraints discovered → reusable methods → invalidated assumptions →
recommended skill/process changes → tests that should exist. Then push only
the entries that pass the ingestion gate — a postmortem is a filter, not a
transcript. Store failures with the same care as wins; disproven approaches
prevent repeat spend.

## Output
The stored/updated entries (or the refusal + reason per candidate), each
showing: entry · type (lesson/decision/fact/reference) · provenance · what
it superseded (if anything). Then the JAIL-HANDOFF block;
`approval_required` lists writes awaiting human sign-off where the platform
or stakes demand it.

## Related skills
Raw inbound data → **jail-quarantine** adopts it first; memory stores the
distilled lesson, not the raw feed. Approval mechanics →
**jail-approval-gate**. Postmortem findings that change a skill →
**jail-skill-miner** / skill edit. Contract for the next run retrieves from
here → **jail-task-contract**.

## Gotchas
- **Transcript hoarding.** Storing summaries of everything. Memory is for
  what changes future behavior; the transcript already exists.
- **Duplicate drift.** Five near-identical entries that disagree slightly.
  Update-don't-duplicate is check 4 for a reason.
- **Silent deletion.** Overwriting a superseded belief erases the lesson of
  having been wrong. Mark, don't vanish.
- **Provenance-free facts.** An unattributed memory can't be challenged or
  aged — it becomes permanent folklore. No provenance, no storage.
- **Blame-shaped postmortems.** "Agent X failed" stores nothing reusable.
  Root cause = the mechanism that would fail again.
