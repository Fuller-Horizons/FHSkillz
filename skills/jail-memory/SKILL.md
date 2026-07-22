---
name: jail-memory
metadata:
  version: 1.3.0
description: >-
  Govern what enters, stays in, and leaves durable memory or organizational
  knowledge — provenance-checked, deduplicated, classified, superseded-not-
  deleted — and run the LEARNING POSTMORTEM ritual that turns finished work
  into stored lessons. Implemented as a MARKDOWN MEMORY SYSTEM: a MEMORY.md
  index plus one dated, provenance-headed .md file per entry, written to the
  project workspace so it travels, diffs in git, and works on any platform.
  Use when saving lessons/decisions/context for future sessions ("remember
  this", "save that for next time"), when retrieving prior context for a new
  task, after completed or failed projects ("what did we learn"), or when
  another skill proposes a durable write. Do NOT use for in-conversation
  working notes, or for the adoption review of raw inbound data
  (jail-quarantine — that gate runs first).
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

## The memory file system (how it's stored, indexed, and headed)
Memory is a set of **Markdown files** in a `memory/` folder at the project
root — the auditable source of truth on every platform. A platform's own
memory feature, when present, *mirrors* these files; the files never stop
being the record.

**The index — `memory/MEMORY.md`.** One scannable table, newest first, one
row per entry so retrieval is a single glance:
```
| id | type | title | created | updated | status | file |
|----|------|-------|---------|---------|--------|------|
| M0007 | decision | Legacy IDs kept for integration parsing | 2026-07-22 | 2026-07-22 | active | 0007-legacy-ids.md |
| M0003 | lesson | Client dislikes Friday deploys | 2026-06-30 | 2026-07-22 | superseded-by M0007 | 0003-friday-deploys.md |
```

**Each entry — `memory/<NNNN>-<slug>.md`** — opens with a provenance header
block (YAML frontmatter) so every fact can be aged and challenged, then the
body:
```
---
id: M0007
type: decision            # lesson | decision | fact | reference | ADR
title: Legacy IDs kept for integration parsing
created: 2026-07-22
updated: 2026-07-22
source: session 2026-07-22 · migration project · Jonathan
status: active            # active | superseded-by <id>
supersedes: []            # ids this replaced
---
**Context →** …  **Decision →** …  **Consequences →** …   (ADR shape for
decisions; lessons use: what happened · why it matters · how to apply)
```

**Rules on the files:**
- Every write passes the six-check gate above before a file is created.
- **Supersede, don't delete:** the loser's `status` becomes
  `superseded-by <id>` and it stays on disk — the history of being wrong is
  a lesson. The index row updates to match.
- **Retrieval = read `MEMORY.md` first** at the start of relevant work; open
  an entry file only when its row bears on the task.
- `id` is monotonic (`M0001`…); the filename carries the same number so
  index and files sort together. Secrets/protected data never enter a file
  (the six-check safety gate).

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
