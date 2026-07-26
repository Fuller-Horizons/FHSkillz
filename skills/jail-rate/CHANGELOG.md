# Changelog — jail-rate

All notable changes to this skill. Versions track `metadata.version` in SKILL.md.

## 2.1.0 — 2026-07-25 (plugin 0.25.0)

- Moved the 8-bullet Gotchas list to `references/gotchas.md`; SKILL.md keeps a one-line pointer (token efficiency, largest core in the suite).
- Added a terminal `JAIL-HANDOFF` envelope (docs/JAIL-CONSTITUTION.md format) stating the artifact produced (scorecard/rubric), confidence, and named next-skill options (jail-rate-skill, jail-prospect, jail-council on contested dimensions).
- Added a determinism rule to Self-check: generate at temperature 0.0; identical subject + identical evidence must reproduce identical scores, and a divergent re-run means re-examine the evidence, not average it.

## 2.0.0
- **Universal rating engine (was: software-only).** Rates any subject — software, codebases, hardware, people (professional/public roles only), ideas, programs, services, businesses, content, and derived types — instead of only software products.
- **Subject-type awareness.** Step 1 classifies the subject; the rubric must match the type. Hands off AI-skill targets to `rate-skill` and prospecting decisions to `company-prospect-research`.
- **Per-type weighted rubric library** (`references/rubric-library.md`): 8 built-in rubrics with default weights, per-dimension evidence sources, and rationale — plus a meta-procedure for deriving a declared rubric for unlisted types. The rubric is always output before the scores.
- **Empirical evidence requirement** (`references/evidence-standards.md`): live research by default; tiered sources; every citation carries URL + date accessed; claims labeled Fact / Inference / Judgment; ≥2 independent sources per dimension targeted; marketing claims are not evidence; per-dimension → overall confidence rules; private-subject handling.
- **People boundaries.** Professional/public-role evaluation from public verifiable evidence only; no personal lives, protected attributes, rumor, or "character" scores.
- Kept from 1.0.0: calibration anchors, anti-inflation rules, critical-flaw cap (≤4.0), weighted overall, ranked impact×effort recommendations, current → projected rating.

## 1.0.0
- New skill: software-product rating across five weighted dimensions (quality 25 / features 20 / usability 20 / security 20 / marketability 15) with calibration bands, critical-flaw cap, and projected post-improvement scores.
