I haven't built anything yet. Two things need your input first.

**1. I couldn't check the spike ledger.** The project's docs (including `claude/spike-ledger.md`) aren't reachable from this session. The project read/search tools aren't loaded here, and the files aren't on disk. I can't rule out an earlier spike on this screen, so I'd need either the ledger pasted in or the project tools reconnected.

**2. "See how it feels" doesn't name a question yet.** A prototype needs one question it answers, or it's just a demo. Here's a proposed one:

> *Which of three batch-send layouts lets an owner review and send a batch with no mis-sends, in under 30 seconds?*

If that's close, I'd build a single-file HTML review page with:
- three genuinely different layouts (for example: a list-with-checkboxes, a summary-then-confirm step, and a per-recipient preview table) behind one switch
- sample recipients only, clearly labeled as sample data
- numbered review points and a "Copy my answers" button, so your verdict comes back as pasted text

It would be marked `proto-batch-send` with a "PROTOTYPE — wipe me" banner, and it would run by opening the file.

Tell me:
- Is the question above right, or what would you change?
- What is the batch-send screen for? Which product or workflow, and what is in a batch (emails, invoices, orders)? That decides the sample data and the fields shown.
- Do you have a spec or current screen I should match?

Once you say yes, I'll build it, lint it, and tell you which review channel to use.