**VERIFICATION: UNVERIFIED. The migration claim is not confirmed.**

Checks: 10 run · 0 pass · 0 fail · 10 unverified

Under the rubric, a label derived from these counts would read PASS-WITH-FLAGS. That label would overstate what was checked, so don't read it as a pass. Nothing was confirmed.

**Failures (ranked):** none. Nothing was observed to fail, because no artifact was available to check.

**Why every check is unverified:**
- **No task contract.** I have no stated source count, target, key field, or definition of "loaded." I'm verifying against your request verbatim: "all 1,200 records loaded."
- **No artifacts.** The working directory is empty. The scratchpad is empty. A project search for migration, load, or record-count material returned only unrelated docs (the prospect briefs and a prompt-book PDF).
- **The claim is success-by-relay.** "My agent says" is hearsay until the agent's output shows up.

**Flags:**
- If the migration was run by the same agent that reports it, this is same-producer verification. I have no independent evidence either way.
- "Loaded" can mean rows inserted, not rows correct. A count match alone would not prove the data is right.

**Evidence examined:** working directory `/tmp/fhlive-1f4kbrjc` (empty); scratchpad (empty); project search "data migration 1,200 records loaded" (no migration material).

**To verify, send me:**
1. The source of the 1,200 records and the target (table, file, or system). I can run the checks myself if I have access, or you can paste the outputs.
2. The count from the target and from the source, taken after the run.
3. Key reconciliation: the set of source IDs missing from the target, extra IDs in the target, and duplicate IDs.
4. The load log: exit code, rejected or errored rows, and timestamps.
5. A sample of 10–20 rows compared field by field against the source.

With those, I'll re-run the verdict. A PASS needs the counts, the key diff, and the log in hand. If the target shows 1,200 rows but any key is missing, duplicated, or rejected, it's a FAIL.

```yaml
JAIL-HANDOFF:
  skill: jail-verify
  status: unverified
  facts: [No migration artifacts present in session; project search found no migration material]
  assumptions: [Target of "1,200 records loaded" is the migration's destination; no contract, verified against request verbatim]
  unknowns: [Source record count; target count; key reconciliation; load log and exit code; field-level accuracy]
  outputs: [verdict UNVERIFIED]
  evidence: [working dir empty; scratchpad empty; project search negative]
  risks: [Same-producer verification if agent self-reports; count match may not mean correct data]
  confidence: none
  next: producing agent or user supplies the artifacts listed above, then re-run jail-verify
  approval_required: [any write or re-run of the migration]
```