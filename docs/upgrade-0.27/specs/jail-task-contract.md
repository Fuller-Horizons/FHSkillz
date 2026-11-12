# Spec — jail-task-contract (1.3.0 → 1.4.0) · now 7.8 → target 9.0

Changes
1. Field 13 (Completion criteria) gains a structured acceptance-criterion format (pattern adapted from ECC intent-driven-development): `AC-NNN — scenario · trigger/action · expected result · must-not (prohibited side effect) · verification method (script | diff | named observation | human check, with why) · priority (required/nice)`. Quick Capture: 3–7 ACs; Full: add a risk row per security/data/migration/external dependency. Keep "the check must be able to FAIL".
2. New preset **ENGAGEMENT** (consulting scope) alongside RESEARCH/BUILD/ANALYSIS: deliverables with acceptance ACs · in-scope list · ≥5 explicit out-of-scope items each with why deferred · change-order triggers (what turns a request into a new contract) · decision rights (who approves deliverables) · client inputs required + due dates. Lives in `references/presets.md` with the other presets (move preset detail out of the core).
3. Business-rule boundary (from ECC): business rules, compliance duties, SLAs, pricing and retention policy are never inferred from code or files — they are User-provided or Unknown until an authoritative artifact states them.
4. Worked example `references/example-engagement-contract.md`: an ENGAGEMENT contract for a small-business sales-process diagnostic (all 14 fields, ACs, JAIL-HANDOFF).
5. Canonical labels; description ≤ 450 (currently 686); core ≤ 160 lines.
Client-facing: yes (ENGAGEMENT preset output is shared with clients).

Test scenarios
S1 engagement: "A landscaping company owner wants help 'fixing marketing'. Budget about $6k, wants results before spring. Draft the scope so we agree before I start."
  [O] contains an explicit out-of-scope list with at least 3 items
  [O] completion criteria are testable (each can fail), not "report delivered"
  [O] surfaces the vague goal ("fixing marketing") as an assumption or blocking question rather than silently defining it
  [O] lists inputs the client must provide
S2 scope drift: a running contract is pasted, then "also, can you rebuild their website while you're at it?"
  [O] treats the website rebuild as a new/child contract or change order, not a silent addition
  [O] states what changed (goal/deliverable) in one line
S3 trivial ask: "rename these 5 files to lowercase".
  [O] does not produce a full 14-field contract (proportionate response / just does it or says trivial)
