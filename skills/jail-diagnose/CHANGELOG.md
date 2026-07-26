# Changelog — jail-diagnose

## 1.1.0 — 2026-07-25 (plugin 0.25.0)

- Added a Safety section after Phase 1: prefer non-prod/staging for repro, snapshot/back up state (or get explicit confirmation) before destructive steps, redact secrets/tokens/PII before quoting logs or instrumentation in the report.
- JAIL-HANDOFF's `evidence` payload now specified as three fields carried verbatim from the Output block (`loop:`, `proof: red→green`, `regression_case:`) so jail-verify/jail-memory can machine-check them instead of re-deriving from prose.
- Added `references/harness-templates.md` with a copy-paste procedure skeleton for each of the 8 Phase-1 loop types; linked one line from core Phase 1.

## 1.0.0
- New kernel skill. Feedback-loop-first diagnosis of hard defects — build a tight red-capable reproduction signal before any hypothesizing, minimize, instrument where hypotheses predict divergence, fix the confirmed cause, and ship a mandatory regression case. Adapted from Matt Pocock's diagnosing-bugs (MIT), generalized beyond code and bound to JAIL evidence rules.
