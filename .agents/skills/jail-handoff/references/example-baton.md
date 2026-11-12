# Worked example — a passing baton

1. **Objective + contract state** — Migrate billing DB from Postgres 13→15
   with zero downtime. Contract: `docs/migration-contract.md` v2, "done" =
   all reads/writes on PG15, PG13 decommissioned.
2. **State of play** — Done: schema replicated, verified row-count parity
   (see `ops/migration-log.md#step4`). In-flight: cutover script written,
   stopped mid-dry-run at the connection-pool swap step. Not started:
   PG13 decommission.
3. **Decisions so far, with why** — Chose logical replication over
   pg_dump: needed near-zero downtime. Rejected blue/green proxy: client
   lacks budget for extra infra.
4. **Reference, don't duplicate** — Contract: `docs/migration-contract.md`.
   Cutover script: `ops/cutover.sh`. Ledger: `ops/migration-log.md`.
5. **Live constraints & gotchas** — Client's connection pooler drops idle
   connections after 60s (not documented anywhere) — cutover script must
   account for it or it silently fails.
6. **Next actions** — 1) Finish dry-run past the pool-swap step. 2) Run
   cutover in staging. 3) Schedule prod cutover window with client.
7. **Suggested skills** — jail-orchestrate to run the cutover as a tracked
   multi-step op.
8. **Approval state** — N/A — no approval pending; client pre-authorized
   the full migration in the signed contract.
