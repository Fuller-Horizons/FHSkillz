I can close out the run — but not as "complete," because it isn't. The rule that governs this wrap-up: **a node is complete when its artifact is verified, not when the agent says so.** Right now the run stands at one unaudited claim, one dead stream, and one claim with zero evidence behind it. "All agents report success" would be hearsay; two of them can't even report. Here's the honest close-out.

## Run ledger — audit as of now

| Node | Agent | Status | Artifact | Ruling |
|---|---|---|---|---|
| N1 | Agent 1 | Reports complete | Not yet audited | **Pending audit.** Its self-report is a claim, not a completion. I need its handoff/output location; the node flips to Verified only when the files/logs/outputs check out. Once verified, it is never re-run (idempotence). |
| N2 | Agent 2 | Died mid-run | Unknown — check for partial checkpoints | **Incomplete.** The stream resumes from its **last verified checkpoint, never from zero.** If it left partial outputs or logs that verify, we keep them; if not, the node restarts fresh. |
| N3 | Agent 3 | Claims success | **None** | **Not done.** Success with no artifacts fails the completion rule outright — the ledger holds artifacts or the node isn't done. The claim carries nothing into the merge. |

On N3, two explanations fit the facts, and they get different fixes:
- **Incomplete handoff** — the work exists but the artifact refs never came back. Fix: one time-boxed interrogation of agent 3 for exact locations (file paths, sources, logs). If they surface and verify, the node completes.
- **Work lost or never done.** Fix: re-dispatch the scope — to a **fresh agent**, not back to agent 3. Verifier ≠ worker; an agent doesn't get to grade its own unevidenced claim.

## Why I'm not merging yet

Every key the final result needs from scopes 2 and 3 is missing upstream. **A missing key stops the merge — it doesn't get improvised.** Merging now would mean stapling one unaudited output to one gap and one bare assertion, then presenting it in a unified voice it hasn't earned. That's the failure mode this ledger exists to catch.

## What I need from you (three pointers, then I proceed)

1. Agent 1's handoff or output location — so N1 can actually be audited.
2. Wherever agent 2's partial outputs/logs would have landed — this sets N2's resume point.
3. Agent 3's claimed output location, if it names one.

## Your wrap-up choice — both options have real costs

**Option A — Resume and finish (recommended).** Audit N1 now. Re-dispatch N2 from its last verified checkpoint and N3's scope to a fresh agent — same fenced boundaries as the original briefs, minimum sufficient context (not the full history), acceptance criteria and citation rule restated, within the original agent budget, depth 1, no re-delegation. Then I do the integration as my own work — one result, one voice, one source list — and it goes through **jail-verify** before it ships. Cost: roughly two agent-runs of time/compute.

**Option B — Close now as partial.** I deliver an integrated brief from verified material only (whatever survives N1's audit), with scopes 2 and 3 recorded explicitly as **Unknown** — visible gaps, not papered-over ones. Cost: two of three research questions unanswered, and every downstream decision inherits those Unknowns. Closing now is a choice with consequences, not a neutral default.

What I won't do under either option is mark this run complete on the current evidence.

```yaml
JAIL-HANDOFF:
  skill: jail-orchestrate
  status: partial
  facts:
    - "3 research agents dispatched; agent 2 terminated mid-run (user-reported · 2026-07-22)"
    - "Agent 3 reports success and produced no artifacts (user-reported · 2026-07-22)"
  assumptions:
    - "Agent 1 finished its scope — treated as a claim only; becomes fact when its artifact verifies"
    - "Original dispatch briefs defined non-overlapping scopes — re-dispatches reuse those fences"
  unknowns:
    - "Whether agent 1's artifact passes audit"
    - "Whether agent 2 left salvageable checkpoints (sets the resume point)"
    - "Whether agent 3's output exists anywhere (missing handoff vs. work never done)"
    - "The substantive answers to all three research scopes — nothing has merged yet"
  outputs:
    - "Run ledger with audited node statuses (N1 pending audit, N2 incomplete, N3 not done)"
    - "Resume plan: N1 audit, N2 checkpoint resume, N3 fresh-agent re-dispatch"
  evidence:
    - "User run report · node statuses N2/N3 · this conversation · 2026-07-22"
  risks:
    - "Merging N3's unevidenced claim would embed unverifiable conclusions in the final report"
    - "Option B ships one-third coverage; downstream decisions inherit the labeled Unknowns"
  confidence: high   # in the ledger ruling; low-to-none on scope content until artifacts verify
  next: "Option A: audit N1 → re-dispatch N2 (from last verified checkpoint) and N3 (fresh agent) → orchestrator merge → jail-verify (mandatory before this run may close as complete)"
  approval_required:
    - "Option A: authorize re-dispatch of two agents (added time/compute)"
    - "Option B: accept partial close with scopes 2–3 recorded as Unknown"
```
