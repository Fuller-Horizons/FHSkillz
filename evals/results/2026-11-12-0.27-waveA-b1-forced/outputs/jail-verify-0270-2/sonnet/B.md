VERIFICATION: **UNVERIFIED** (computed: PASS-WITH-FLAGS is not earned, and the claim cannot be confirmed)
Checks: 10 run · 0 pass · 0 fail · 10 unverified

I can't confirm that the migration loaded 1,200 records. The working directory (`/tmp/fhlive-iffj_lfj`) is empty. It has no migration logs, source data, target database, scripts or contract. The only evidence is your agent's statement, and under jail-verify that is hearsay.

**Failures (ranked):** none observed. Nothing could be checked, so nothing could fail.

**What's unverified, and the observation that would settle each:**
1. **Contract compliance.** No contract was supplied. I'm using your request verbatim: "all 1,200 records loaded." Still missing is the source of the 1,200, the target, and which fields and tables count.
2. **Completion criteria.** I need the source count and the target count from the current state, via `SELECT COUNT(*)` or the equivalent. Those two numbers should be 1,200 and 1,200.
3. **Internal consistency.** The loaded, rejected and skipped counts from the migration log should sum to 1,200. I need the log.
4. **Grounding.** Does the "1,200" come from a real source count or from the agent's assumption? I need the source file's row count.
5. **Schema.** Do the loaded rows have the required columns, correct types and keys? I need a schema diff or sample rows.
6. **Tool reality.** I need the run's exit code and log. A job can exit 0 and still skip rows.
7. **Edge cases.** I'd check for duplicates, which would make 1,200 rows loaded fewer than 1,200 distinct records, along with nulls, truncated fields, encoding errors and rolled-back batches.
8. **Unsupported confidence.** "All 1,200" is an absolute claim with no artifact behind it.
9. **Security and privacy.** Check that the logs and target don't expose credentials or PII.
10. **Implementation readiness.** A rollback or backup of the pre-migration state needs to exist. I can't tell whether it does.

**Flags:**
- This pass would be same-producer verification if I were running the agent's work. The agent's output hasn't reached me at all, so I haven't verified it.
- If the agent reported this from a different session or environment, its artifacts live somewhere I can't see.

**Evidence examined:** the working directory listing and a glob for migration, load, import, log, db, sqlite and csv files. Both came back empty.

**What I need from you (any one of these moves it forward):**
- Where the migration ran, such as a path, a DB connection (read-only is fine), or the log file.
- The source file or table holding the 1,200 records.
- Or the agent's raw tool output (counts, log, exit code), pasted in.

With those I'll run the count reconciliation, a duplicate and null check, and a sample-row comparison against the source.

```
JAIL-HANDOFF
status: blocked: no artifacts available
verdict: UNVERIFIED (0/10 checks passable)
next: user supplies the migration log, source count and target access, then re-run /fh-skillz:jail-verify
do-not-ship: treat the migration as NOT confirmed
```