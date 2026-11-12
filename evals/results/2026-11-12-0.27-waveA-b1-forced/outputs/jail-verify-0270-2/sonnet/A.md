VERIFICATION: FAIL-CLOSED, which maps to PASS-WITH-FLAGS. Nothing can be confirmed, so the claim stays UNVERIFIED.
Checks: 10 run · 0 pass · 0 fail · 10 unverified

I did not run the checks. The working directory (`/tmp/fhlive-l3p786pl`) is empty. It has no migration logs, source or target data, row counts, exit codes or task contract. All I have is the agent's statement, and under this skill's rules a claim without its artifact is not evidence. This is success-by-relay: hearsay, not a pass.

Reading the counts above: no check failed outright, so the computed label is PASS-WITH-FLAGS. Read that as "not verified, do not rely on it." It is not a pass.

**What would verify the claim.** Any of these would let me run the checks:
1. **Source count.** The row count and a key list or checksum from the source, taken now. Does "1,200" actually match the source?
2. **Target count.** `SELECT COUNT(*)` on the destination table(s), run from the current state. It must equal 1,200 exactly.
3. **Key reconciliation.** Source IDs minus target IDs, and target IDs minus source IDs. Both must be empty, with no duplicates and no orphans.
4. **Field-level sample.** At least 20–30 random records compared field by field, plus the edge cases: nulls, special characters, dates, and truncated text.
5. **Migration log.** The job's own log with exit code, rejected or skipped rows, and error or warning counts. A "finished" run can still skip rows.
6. **Constraints and integrity.** Foreign keys, NOT NULL and unique constraints hold, and any transformed fields have correct types.
7. **Rollback.** A backup or snapshot of the pre-migration state exists, and the rollback path is named (check 10).

**Flags:**
- "All 1,200 loaded" could mean attempted, inserted, or committed. Only a target-side count settles it.
- The contract is missing. Without it I'd verify against your original request. If 1,200 came from the agent and not the source, that number itself is unverified.
- This is a data migration, which is high stakes. Use the DUAL lane once artifacts exist, with two independent reviewers who share no context.

Evidence examined: working directory listing only (empty). No citations, logs or data were opened.
Checklist used: none selected. The closest fit is "code change / plan-workflow", and a data-migration checklist would be needed.

VERDICT-JSON: {"verdict":"PASS-WITH-FLAGS","run":10,"pass":0,"fail":0,"unverified":10,"lane":"single"}

JAIL-HANDOFF
- status: UNVERIFIED, blocked on artifacts
- next: you, to supply the source and target access (DB connection, exports, or the migration log). Then re-invoke jail-verify, DUAL lane. If the counts or keys don't reconcile, route to jail-diagnose.
- do not: tell anyone the migration is complete until then.

If you point me at where the data lives (a path, a DB I can query, or the agent's log output), I'll run the reconciliation now.