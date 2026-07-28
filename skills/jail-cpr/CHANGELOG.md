# Changelog — cpr-agenda-builder

## 1.5.0 — 2026-07-27 (plugin 0.26.0)

- **New COMMIT lane.** A third lane for a personal or team commitment
  contract over a defined period (a quarter, a "tour," a fixed number of
  weeks) — no meeting, no agenda. Its own Purpose rule (identity-level why,
  not one sentence) and a Results rule tightened to self-contained testable
  (no outside-witness corroboration, no undefined qualifiers). DEBRIEF's
  Results-audit step now doubles as the period-end scorecard, accepting a
  self-report/check-in as valid input alongside transcripts.
- **New COMMIT output template**, alongside the existing DESIGN template —
  leads with an explicit **DEADLINE** (the period's real calendar end date,
  pinned in step 1 and checked by the closing verify gate), not folded
  into a Result or left as a fuzzy "in a few months."
- **New gotchas:** unverifiable corroboration, undefined qualifiers,
  DESIGN-machinery leaking into COMMIT, fuzzy deadline.

## 1.4.0 — 2026-07-25 (plugin 0.25.0)

- **Closing checks are now hard gates.** DESIGN step 5 (jail-verify) and DEBRIEF step 4 (Results audit) state FAIL-any-check gates — do not render the document until fixed or flagged inline.
- **Code-free fallback promoted to co-equal.** Deliverable section now leads with the no-docx/pdf Markdown fallback (full-fidelity, not degraded), stated before the DOCX/PDF bullets instead of trailing.
- **Gotchas moved to `references/gotchas.md`.** SKILL.md keeps a one-line pointer; content unchanged, offsets the line growth from the gate and deliverable edits.

## 1.3.0 — 2026-07-22 (plugin 0.24.0)

- **Document deliverable.** The meeting output is now a polished DOCX (default, via the docx skill) or PDF (on request, via the pdf skill) — title block, CPR/debrief sections as headings, agenda/action-items as tables — not just chat text. Cross-refs updated for jail-plan / jail-summarize renames.

## 1.2.0 — 2026-07-22 (plugin 0.23.0)

- DEBRIEF lane (the post-meeting half): decisions-vs-discussed-vs-deferred with provenance, owned actions (unowned flagged, never guessed), commitments, Results audit against the CPR, and routing (memory/operationalize/decide/next design). DESIGN <-> DEBRIEF close the loop.

## 1.1.0
- **Renamed** `cpr-agenda-builder` → `jail-cpr` (JAIL family naming). Folder, frontmatter, and every cross-reference updated; earlier changelog entries keep the historical name.

## 1.0.0
- New skill (JAIL frameworks pack, wave 1). Context-Purpose-Results meeting design — agendas reverse-engineered from testable Results, every item owned and output-bearing.
