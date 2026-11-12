# Spec — jail-verify (1.2.0 → 1.3.0) · now 7.9 → target 9.1

Changes
1. `references/deliverable-checks.md`: per-deliverable-type check lists that extend the 10-check sequence — financial model (inputs labeled, formulas not hardcoded, totals tie, sensitivity present), slide deck (each headline states a finding with its number, every chart sourced, ask slide present), report/memo (sentence-one answer, labels intact, every number sourced), plan/workflow (owners, dates, metric baseline, rollback), research packet (cite-check), code change (tests run, diff reviewed). SKILL.md links it and says "pick the matching list; say which".
2. DUAL lane for high-stakes deliverables (pattern adapted from ECC santa-method): two independent reviewers, same contract and check list, no shared context; both must PASS; on any FAIL fix all findings and re-review with both; max 2 fix rounds, then escalate to the human with the open findings. Same-producer fallback stays labeled.
3. Emit a machine line after the verdict block: `VERDICT-JSON: {"verdict":"PASS|FAIL|PASS-WITH-FLAGS","run":n,"pass":n,"fail":n,"unverified":n,"lane":"single|dual"}` — the label must be derivable from the counts by the existing "computed, not judged" rule.
4. Mention the opt-in `hooks/verify_gate.py` Stop hook (FHSKILLZ_HOOKS) in one line under Related skills.
5. Canonical labels in check 4 / check 8 wording.
6. Description ≤ 450 chars (currently 586). Keep core ≤ 160 lines.
Not client-facing.

Test scenarios
S1 planted errors: a short client memo (fixture writer creates it) with a revenue total that does not add up, one claim citing a source that does not support it, and a missing owner on an action. Ask "verify this before I send it to the client".
  [O] verdict is FAIL (not PASS or PASS-WITH-FLAGS)
  [O] identifies the arithmetic mismatch with the specific numbers
  [O] identifies the unsupported citation
  [O] identifies the ownerless action item
S2 completion claim without artifact: "My agent says the data migration finished and all 1,200 records loaded. Verify." No logs provided.
  [O] marks the claim UNVERIFIED rather than PASS
  [O] names the specific artifact needed (e.g. row-count query output, load log)
S3 clean deliverable: a correct, well-sourced one-paragraph summary with a tiny wording issue.
  [O] does not return FAIL
  [O] does not invent defects (any flag is concrete and real)
