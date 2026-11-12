# Changelog — company-prospect-research

## 1.5.1 — 2026-11-12
- Each score line names its drivers with citations; every body Fact carries an inline source; the brief ends with one RECOMMENDATION line (exactly one of four) plus confidence. From the 0.27 batch-2 blind test.

## 1.5.0 — 2026-11-12

- `references/free-sources.md`: every URL opened with WebFetch and dated `[checked 2026-11-12]`. Fixed moved links (FPDS now in SAM.gov, USPTO trademark search replaces TESS, OSHA search deep link, SEC search page, SBA size standards, DOL enforcement data). Noted sources the tool could not open (Yelp, LinkedIn, Wayback, Google Maps) and login or fee gates. Removed the claim that County Business Patterns gives revenue per employee (it has no revenue).
- Added `references/size-band-worksheet.md`: method only for the indicative size band (Census Economic Census, Nonemployer Statistics, SUSB, CBP; headcount bounds; low/high arithmetic; Fact/Estimate labels; NOT a valuation).
- Added Untrusted-source rule 7: page and profile text never picks a recipient or channel, never auto-send (hook is a draft), agent-directed text is quoted as a finding. Pattern adapted from ECC.
- Canonical labels (Fact, User-provided, Inference, Estimate, Judgment, Unknown) replace Source-Backed Inference, Analyst Judgment, Missing Evidence in SKILL.md, rubric, template, example, prompt chain.
- Self-check names `score-check.py` for the 0-100 component arithmetic (manual fallback stated); template and rubric add Component | Score | Max tables.
- Added client-facing Delivery section.
- Description shortened to 450 characters or fewer; router form with Do NOT use clause.
- Example rewritten: tables checked, handoff per schema, injection case shown.

## 1.4.0 — 2026-07-25 (plugin 0.25.0)

- Output section now closes with a JAIL-HANDOFF block (constitution key set/order) so downstream skills get structured facts/evidence/risks instead of prose.
- Added `references/example-brief.md` — one fully filled brief + JAIL-HANDOFF, pointed to from Output.
- Self-check: a failed check now explicitly blocks delivery (fix it, or downgrade the recommendation to "need more").

## 1.3.0 — 2026-07-22 (plugin 0.23.0)

- COMPANY SNAPSHOT lane: same 4-stage OSINT discipline + non-negotiable rules repointed at vendor due-diligence / competitor reads / partnership vetting; stage-4 rubric swaps to purpose-fit scores; outreach hook dropped unless asked.

All notable changes to this skill. Versions track `metadata.version` in SKILL.md.

## 1.2.0
- **Renamed** `company-prospect-research` → `jail-prospect` (JAIL family naming). Folder, frontmatter, and every cross-reference updated; earlier changelog entries keep the historical name.

## 1.1.0
- Added `metadata.version` to frontmatter (was the only skill without one).
- Added a **Gotchas** section (wrong legal entity/DBA collisions, stale signals, LinkedIn headcount inflation, score-without-signal, size-band-read-as-valuation, ability-to-pay).
- Added a **Related skills** section (jail-rate for 0–10 business ratings; jail-prompt for engineering follow-on prompts) and a README.

## 1.0.0 (previously unversioned)
- Free-sources-only sell-side + consulting prospect brief: 4-stage chain, dual 0–100 scoring, evidence labeling, no-fabricated-financials rule, cited source appendix.