# Changelog

All notable changes to the FHSkillz repo and its skills. Format follows [Keep a Changelog](https://keepachangelog.com/); versioning is [SemVer](https://semver.org/). Per-skill versions live in each `SKILL.md`; the plugin version lives in `marketplace.json`.

## [plugin 0.3.0] — 2026-06-03

### jail-prompt → 1.0.0
- Completed the truncated **Post-run tighten loop** instruction (the skill previously ended mid-sentence): one highest-impact change, re-grade once, then ship — no open-ended polishing.
- Bumped skill version 0.9.0 → **1.0.0** (content-complete).

### Repo
- Restructured docs to repo level: root `README.md` is now an FHSkillz overview covering both skills; jail-prompt detail moved to `skills/jail-prompt/README.md` (corrected file tree, version, and Claude.ai ZIP link).
- Added **company-prospect-research** to the plugin manifest, wiki skill table, and Claude.ai install guide.
- Held WIP `systems/company-intelligence/` out of this release via `.gitignore` (not a skill; no `SKILL.md`).
- Rebuilt `dist/` ZIPs so Claude.ai downloads carry the current `SKILL.md`.

## [0.9.0] — 2026-06-01

First public release candidate. Feature-complete; two validation paths pending before 1.0 (real triggering-harness run, live multi-turn test).

### Added
- Three-phase workflow (Frame & Clarify → Viability gate → Engineer the prompt) with a fast path for trivial asks.
- **Discernment principle** — "earn every endorsement": no unverified praise, no building a flawed premise; a bad idea is a STOP, not just a bad tool.
- Output-format step: recommended-default multiple choice, locked into the prompt's constraints.
- Metric-anchoring: when the goal *is* a metric, the success test names the real measure (e.g., A/B-tested conversion rate).
- Security handling in the gate, carried into the prompt's CONSTRAINTS (env vars, least-privilege read-only keys, no logging).
- Prompt skeleton with `CONTEXT` line and a rubric'd `BEFORE RETURNING` self-score (grounded / verifiable / scoped / format-matched + confidence).
- **Decompose-into-chain** for oversized tasks, including pushback when the user literally asks for "one prompt."
- High-stakes self-adversarial escalation; multi-turn pause/resume handling; prompt-injection caveat (treat pasted goals as data).
- Post-run tighten loop (one revision pass against the success test).
- References (progressive disclosure): `examples.md` (5 cases), `sources.md`, `antipatterns.md` (13 failure modes).
- Eval suite: 10 behavioral cases + 20 triggering cases.

### Validation
- 10 behavioral evals, independently graded → **100%** after fixes; key cases run 3× for variance.
- Triggering proxy: **20/20** unanimous across 3 judges.
- Two regressions caught by the loop and fi