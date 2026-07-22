# Changelog — jail-baton

## 1.0.0
- New kernel skill. Session-to-session handoff batons — compact the work's state, decisions-with-why, artifact references (never duplicates), next actions, and suggested skills so a fresh agent or smaller-context model continues without re-derivation. Secrets redacted per quarantine classes. Adapted from Matt Pocock's handoff (MIT), extended under JAIL rules; complements the in-run JAIL-HANDOFF block.
