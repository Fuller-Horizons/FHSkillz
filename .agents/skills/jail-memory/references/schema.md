# Memory file schema — MEMORY.md index + entry frontmatter

Load this when writing or reviewing an entry — the compact schema line in
SKILL.md points here for the full shape.

## The index — `memory/MEMORY.md`

One scannable table, newest first, one row per entry so retrieval is a
single glance:
```
| id | type | title | created | updated | status | file |
|----|------|-------|---------|---------|--------|------|
| M0007 | decision | Legacy IDs kept for integration parsing | 2026-07-22 | 2026-07-22 | active | 0007-legacy-ids.md |
| M0003 | lesson | Client dislikes Friday deploys | 2026-06-30 | 2026-07-22 | superseded-by M0007 | 0003-friday-deploys.md |
```

## Each entry — `memory/<NNNN>-<slug>.md`

Opens with a provenance header block (YAML frontmatter) so every fact can
be aged and challenged, then the body:
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
