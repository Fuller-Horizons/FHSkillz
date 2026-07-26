# Changelog — business-model-canvas

## 1.3.0 — 2026-07-25 (plugin 0.25.0)

- Chain: every named call (jail-task-contract, jail-research, jail-red-team, jail-lab, jail-decide, jail-summarize, jail-verify) now carries an inline manual fallback so the skill degrades gracefully without its companions.
- Step 3: fail-closed labeling — VALIDATED requires a checkable evidence ref or the element defaults to HYPOTHESIS; the coherence pass (step 4) may not start until every element is labeled. Fixed output schema (`Block | Element | Label(V/H) | Evidence ref | Confidence`, blocks always in the same nine-block order) for run-to-run determinism.
- New pre-ship SUCCESS-TEST checklist gates the JAIL-HANDOFF (labels intact, coherence pass done, top 3–5 assumptions have experiments, no VALIDATED lacks an evidence ref), replacing the bare jail-verify mention.
- New `references/worked-canvas.md` — one filled example canvas (Ledgerly seed-investment decision) with the SUCCESS-TEST walked through against it.

## 1.2.0 — 2026-07-22 (plugin 0.23.0)

- Riskiest assumptions emitted in jail-lab spec shape (metric/one-variable/bounded/threshold) with direct lab handoff; KEEPs promote hypotheses on the next pass. Canvas-delta mode: diff-driven revisits (promote/demote labels, coherence only on touched blocks + dependents, re-ranked assumptions) — the canvas becomes a living document.

## 1.1.0
- **Renamed** `business-model-canvas` → `jail-bmc` (JAIL family naming). Folder, frontmatter, and every cross-reference updated; earlier changelog entries keep the historical name.

## 1.0.0
- New skill (JAIL frameworks pack, wave 1). Nine-block BMC where validated info and hypotheses never blur — coherence pass, unit economics, riskiest assumptions with experiments.
