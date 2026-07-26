# Changelog — jail-baton

## 1.3.0 — 2026-07-25 (plugin 0.25.0)

- Added a fail-closed pre-emit gate: all 8 baton parts must carry content
  or an explicit `N/A — <reason>` marker before the baton is written, so
  a silently blank part can't slip through.
- Redact rule now names jail-py-toolkit's `secret-scan.py` as the check
  to run over the drafted baton text before emit, with a stated manual
  fallback for when the toolkit isn't available.
- New `references/example-baton.md`: a compact worked example with all
  8 parts filled, including one legitimate `N/A — <reason>` marker, for
  the pre-emit gate to match against.

## 1.2.0 — 2026-07-22 (plugin 0.24.0)

- **Renamed jail-baton → jail-handoff.** Same discipline (compact a session into a pick-up-and-continue handoff document); the name aligns with the suite's JAIL-HANDOFF block vocabulary. All cross-references updated; git history preserves the jail-baton lineage.

## 1.1.0 — 2026-07-22 (plugin 0.23.0)

- Proactive offer on context-pressure signals (offer the baton while state is sharp) + state-of-play formalized on the jail-orchestrate ledger shape (node/scope/status/artifact) so batons seed orchestrate resumes and vice versa.

## 1.0.0
- New kernel skill. Session-to-session handoff batons — compact the work's state, decisions-with-why, artifact references (never duplicates), next actions, and suggested skills so a fresh agent or smaller-context model continues without re-derivation. Secrets redacted per quarantine classes. Adapted from Matt Pocock's handoff (MIT), extended under JAIL rules; complements the in-run JAIL-HANDOFF block.
