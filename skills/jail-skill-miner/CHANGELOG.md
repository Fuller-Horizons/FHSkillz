# Changelog — jail-skill-miner

## 1.3.0 — 2026-07-25 (plugin 0.25.0)

- Stage 3 gets a fenced STAGE-3 REPORT SCHEMA fixing the exact pipe column order, plus a fail-closed drop rule: unopened citations and unticked 4-boxes move to a `DROPPED (unverified)` list and can never appear as candidates — so unverified evidence can't be laundered into a recommendation.
- Budget & determinism block: hard caps (<=25 files opened, <=12 candidates, exactly 3 recommended, <=1200-token report) and a stated `rank = universality(1-5) x severity(1-5)` formula with alphabetical tiebreak, so two runs over the same source emit the same ordered table.
- Both gates made checkable: Stage 3 must end with the literal `STATUS: AWAITING-SELECTION` under a no-writes-until-selection rule (ambiguous reply → re-ask, never infer); Stage 4 emits the artifact set only when three boxes PASS, else prints `NOT-READY: <missing>` (jail-py-toolkit `validate-skill-structure.py` checks the set, manual fallback stated).
- Behavioral cases added at `evals/behavioral-0.25/jail-skill-miner.json` covering unverified-citation drop, feature-not-discipline drop, and schema column order.
- README version line corrected (said 1.0.0 while frontmatter was 1.2.0).

## 1.2.0 — 2026-07-22 (plugin 0.23.0)

- Continuous mode — the suite's self-maintenance loop: failed eval cases, corrections repeated across >=2 sessions, and postmortem recommendations auto-nominate fixes/deltas (intake changes, the 4-box/dedup/approval gate doesn't); approved fixes emit ready-to-commit artifact sets.

## 1.1.0
- Delta adapted from Matt Pocock's skills repo (github.com/mattpocock/skills, MIT): invocation-economics authoring rules (context load vs cognitive load, one-trigger-per-branch pruning, router cure).

## 1.0.0
- New skill (JAIL reasoning-kernel wave 1). Mines codebases and histories for plugin-worthy disciplines, filters features out, dedupes against installed skills, and stops for approval before authoring.