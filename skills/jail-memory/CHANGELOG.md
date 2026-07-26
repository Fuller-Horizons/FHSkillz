# Changelog — jail-memory

## 1.4.0 — 2026-07-25 (plugin 0.25.0)

- **SUCCESS-TEST** after the six-check gate: all 8 frontmatter keys present, `id` recomputed fresh as MEMORY.md's current max + 1 (never carried from memory/session), `type`/`status` in the real vocab — any failure names which check failed and refuses the write.
- **Check 6 (safety/classification)** now names jail-py-toolkit's `secret-scan.py` as the pre-write scan, with a stated manual fallback (scan by hand for keys, tokens, passwords, SSNs, named-individual PII).
- Moved the MEMORY.md index example and entry-frontmatter example to new `references/schema.md`; the core now carries one compact schema line + a link, cutting SKILL.md length while keeping the checks it gates fully inline.

## 1.3.0 — 2026-07-22 (plugin 0.24.0)

- **Markdown memory system, first-class.** Elevated the file store from fallback to THE system: a `memory/MEMORY.md` index (id·type·title·created·updated·status·file) plus one dated, provenance-headed `memory/<NNNN>-<slug>.md` per entry (YAML header: id/type/title/created/updated/source/status/supersedes). Supersede-don't-delete on disk; retrieval reads the index first.

## 1.2.0 — 2026-07-22 (plugin 0.23.0)

- File-ledger fallback when no platform memory exists: MEMORY.md index + topic files, same six-check gate, ADR shape, supersede markers; retrieval = read the index at task start; platform memory mirrors the file, which stays the auditable source.

## 1.1.0
- Delta adapted from Matt Pocock's skills repo (github.com/mattpocock/skills, MIT): ADR (Architecture Decision Record) named entry shape: context → decision → consequences → status.

## 1.0.0
- New skill (JAIL reasoning-kernel wave 1). Memory and knowledge governance — six-check ingestion gate, update-don't-duplicate, supersede-don't-delete, plus the learning-postmortem ritual.
