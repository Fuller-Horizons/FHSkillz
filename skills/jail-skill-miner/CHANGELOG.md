# Changelog — jail-skill-miner

## 1.2.0 — 2026-07-22 (plugin 0.23.0)

- Continuous mode — the suite's self-maintenance loop: failed eval cases, corrections repeated across >=2 sessions, and postmortem recommendations auto-nominate fixes/deltas (intake changes, the 4-box/dedup/approval gate doesn't); approved fixes emit ready-to-commit artifact sets.

## 1.1.0
- Delta adapted from Matt Pocock's skills repo (github.com/mattpocock/skills, MIT): invocation-economics authoring rules (context load vs cognitive load, one-trigger-per-branch pruning, router cure).

## 1.0.0
- New skill (JAIL reasoning-kernel wave 1). Mines codebases and histories for plugin-worthy disciplines, filters features out, dedupes against installed skills, and stops for approval before authoring.