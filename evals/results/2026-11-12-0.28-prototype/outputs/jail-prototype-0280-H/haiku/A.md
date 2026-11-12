**Answer so far: no, a strict 4-stage pipeline can't record a second quote after a "no." The prototype isn't finished, though, because the run that would confirm this was blocked.**

**What I tried**
- The harness is `proto-crm-requote-pipeline.py` in my scratchpad. It has two models and runs one scenario: create, contact, quote #1, "no", ask for quote #2, quote #2, "yes". Sample data only, nothing persisted.
- Running it needs shell approval, which wasn't granted, so I haven't executed it. I didn't retry.

**Hand trace (not run output)**
- **Model A, strict 4-stage (won/lost terminal):** steps 1–4 pass. Step 5, `won_lost → quoted`, is blocked, so the second quote can't be recorded. The lead is stuck in lost.
- **Model B, with a reopen move (`won_lost → quoted`):** the second quote is recorded and the deal can close as won. But `outcome` still reads `lost` while the stage is `quoted`, so the first loss is hidden unless it's logged as history.

**Ledger**
- Another session already wrote an inconclusive entry for this question in `claude/spike-ledger.md`. Its hand-trace agrees with mine: lost → quoted is rejected. I didn't add a duplicate line. A run that answers the question should add a superseding entry.

**Verdict:** `inconclusive`. The ship gate needs run output or a reviewer answer, and I have neither.

**To finish:** approve running the script (one command, which I can list for you), or run `python3 proto-crm-requote-pipeline.py` yourself and paste the output. If the output shows model A blocked and model B recording the re-quote, the verdict becomes "answered" with the model B fix. The CRM change would then need a decision on whether a re-quote reopens the same lead or opens a new one.