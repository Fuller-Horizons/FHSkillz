# Changelog — jail-baton

## 1.1.0 — 2026-07-22 (plugin 0.23.0)

- Proactive offer on context-pressure signals (offer the baton while state is sharp) + state-of-play formalized on the jail-orchestrate ledger shape (node/scope/status/artifact) so batons seed orchestrate resumes and vice versa.

## 1.0.0
- New kernel skill. Session-to-session handoff batons — compact the work's state, decisions-with-why, artifact references (never duplicates), next actions, and suggested skills so a fresh agent or smaller-context model continues without re-derivation. Secrets redacted per quarantine classes. Adapted from Matt Pocock's handoff (MIT), extended under JAIL rules; complements the in-run JAIL-HANDOFF block.