# jail-handoff

Session-to-session **handoff** documents — compact the work's state,
decisions-with-why, artifact references (never duplicates), next actions,
and suggested skills so a fresh agent or smaller-context model continues
without re-derivation. Secrets are redacted per jail-quarantine protected
classes. Offered proactively on context-pressure signals (long session,
approaching compaction), not only on request.

Renamed from `jail-baton` at plugin 0.24.0 (the relay-baton metaphor lives
on inside the skill; the name now matches the suite's JAIL-HANDOFF
vocabulary). Same discipline, same version lineage in git.

Boundaries: the in-run structured handoff between skills is the JAIL-HANDOFF
block (constitution), not this skill; durable cross-project lessons go to
jail-memory; a multi-agent resume ledger lives in jail-orchestrate (the
handoff points at it, never replaces it).
