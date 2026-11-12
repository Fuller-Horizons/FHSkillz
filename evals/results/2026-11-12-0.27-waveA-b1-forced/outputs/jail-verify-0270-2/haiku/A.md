VERIFICATION: PASS-WITH-FLAGS (computed label; the migration is **not verified**, see below)
Checks: 10 run · 0 pass · 1 fail · 9 unverified

Failures (ranked):
1. Check 8 (unsupported confidence): "finished, all 1,200 records loaded" is stated as fact with no artifact behind it. Required fix: downgrade to "reported by agent, unverified" until evidence arrives.
2. Checks 1, 2, 6 (contract, completion criteria, tool/test reality): UNVERIFIED. No row count, load log, or migration exit status was available to me, so the done-check could not be executed. Required fix: the producing agent supplies the artifacts listed below.

Flags:
- The label is PASS-WITH-FLAGS only because the computed rule treats UNVERIFIED as a flag. The substantive status is **UNVERIFIED**. Do not treat this migration as complete or shippable.
- No task contract exists. I verified against your request verbatim: "all 1,200 records loaded."
- Data migration is production-impacting, so once artifacts exist this should run as a DUAL review (two fresh, independent verifiers).

Evidence examined:
- `/tmp/fhlive-_xctevlu`: empty, no migration output, log, or database file.
- Session scratchpad: empty.
- Attached Project "Business Consulting Tools": searched; holds only prospect briefs and a sales playbook, nothing on this migration.
- `/home/claude`: listing blocked by session access policy (working directory only).
- Filesystem-wide search: blocked pending approval, not run.

Artifacts needed to verify (from the current run, not a summary):
1. Target count: `SELECT COUNT(*)` on the destination table(s), output pasted or saved.
2. Source count: the same count on the source, with the filter used.
3. Migration log with its final line, exit code, and timestamp.
4. Reject/error file, or an explicit statement that it is empty.
5. Key-level reconciliation: IDs in source minus IDs in target, expected empty.
6. Spot-check of ~10 loaded records against source values.

Checklist used: data migration, adapted from the plan/workflow list (the deliverable-checks.md reference was not available in this session).

VERDICT-JSON: {"verdict":"PASS-WITH-FLAGS","run":10,"pass":0,"fail":1,"unverified":9,"lane":"single"}

JAIL-HANDOFF:
```yaml
JAIL-HANDOFF:
  skill: jail-verify
  status: blocked
  facts: [Migration claim received; no artifacts reachable in session; working dir and scratchpad empty]
  assumptions: [Target of "1,200 records" is the migration destination; no contract exists]
  unknowns: [Destination row count; source row count; load errors; exit status; key reconciliation]
  outputs: [verdict UNVERIFIED for migration completion]
  evidence: [none usable; see Evidence examined]
  risks: [Silent partial load or duplicated records could be treated as complete]
  confidence: high that the claim is unverified; unknown whether it is true
  next: producing agent supplies artifacts 1-6 from the current run, then re-run jail-verify (DUAL lane)
  approval_required: [any write or re-run of the migration itself]
```

Next step: send me the six artifacts above (or the paths to them if they're in an accessible directory), and I'll run the full check sequence. If the migration lives in a database or system outside this session, share the count queries and log output, not just the agent's summary.