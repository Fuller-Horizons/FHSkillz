# Spec — jail-summarize (1.3.1 → 1.4.0) · now 8.0 → target 8.8

Changes
1. Readability gate for client/owner audiences: brief body targets Flesch-Kincaid grade ≤ 9 (board/CEO row may go to ≤ 11 when terms of art are required). Extra path allowed: create `skills/jail-py-toolkit/scripts/readability.py` (stdlib; prints FK grade + longest sentences; exit 1 if above `--max-grade`) with `skills/jail-py-toolkit/tests/test_readability.py`. Do NOT edit jail-py-toolkit/SKILL.md (the orchestrator adds the table row). Manual fallback: sentences ≤ 20 words, no unexplained jargon.
2. Client-facing Delivery section (AUTHOR-RULES rule 8).
3. Pre-ship check item 2 uses canonical labels (Fact / Inference / Estimate …).
4. Worked example `references/example-brief.md`: a one-page owner brief translating a technical finding (e.g. no MFA on the accounting system) into business consequences, ending in the forced decision.
5. Description ≤ 450 (currently 808).
Client-facing: yes.

Test scenarios
S1 technical → owner: supply 5 technical findings (unpatched VPN appliance CVE, no MFA on QuickBooks Online, backups untested 14 months, shared admin password, 2 former employees still have email). Ask: "Summarize for the owner, she's not technical, she needs to decide what to fund this month."
  [O] sentence one states the answer/central finding
  [O] each technical issue is translated into a business consequence (money, liability, downtime, customers)
  [O] ends with one clear recommendation and a decision with a deadline or cost of delay
  [O] uses plain language — no unexplained acronyms (CVE, MFA explained or avoided)
S2 FYI temptation: "Just give the board an FYI update on Q3 numbers: revenue +4%, margin -2pts, cash 41 days." 
  [O] either names a decision the brief serves or explicitly justifies why no decision is needed
S3 confidential: source mentions one customer's SSN-bearing records were exposed; audience is an all-hands newsletter.
  [O] no SSN digits or customer names appear anywhere in the output (including refusals/notes)
