# jail-prototype 1.2.0 vs 2.0.0 — INVALID run (2026-11-12)

Scored (two blind Sonnet graders): old 2/8 cases vs new 3/8, but **the run is contaminated and not used for any decision.**

Cause: `--allowedTools` only pre-approves tools; it does not remove them. Every run could use the session's claude.ai Project, which holds the real `claude/spike-ledger.md` (with today's scorecard verdict) and real prospect briefs.
- Case 0250-3 ("mock up scorecard options"): all four outputs found the real ledger entry and correctly reported the recorded verdict instead of planning a build, so all 5 assertions failed for both versions.
- Case 0250-2: runs searched the Project ledger instead of the entry given in the prompt, and reported "not found".

Fix: `run-live-evals.py --disallowed-tools` (default `Projects`), verified with a probe run ("NO-PROJECTS"). Clean re-run: `2026-11-12-0.282-prototype`.

Caveat for earlier runs: every live run before this fix could also read the Project. Both arms were equally exposed, so A/B verdicts stand, but cases touching saved prompts, briefs or ledgers may have been helped by real data.
