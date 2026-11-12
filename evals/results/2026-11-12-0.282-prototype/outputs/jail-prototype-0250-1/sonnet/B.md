I can't build this yet. The prototype skill won't start without a named question, and I couldn't check the spike ledger.

**Ledger check:** I can't read `claude/spike-ledger.md` from this session. It lives in the project, I have no project-read tool here, and it isn't on disk. So I can't say whether a batch-send question already has a recorded verdict. If you paste the batch-send entries, or tell me there are none, I'll go from there.

**The question:** "Build something and see how it feels" doesn't tell us what we're looking for, and a page with no question can't produce evidence. Here are three candidate questions for a batch-send screen. Pick one, or give me your own.

1. **Look/feel (my suggestion):** Which of three layouts lets a sender confirm who is getting what, and catch mistakes, in 30 seconds before hitting send? The three variants would be a recipient table, a grouped-by-message card view, and a step-by-step review wizard.
2. **Logic/state:** Does the send flow handle the hard cases correctly? Those are partial failures, duplicate recipients, a cancel mid-send, and retrying only the failed ones.
3. **Feasibility:** Can the screen send a batch of N items and show live progress without blocking the UI?

Three things I need from you:
- Which question, or your own wording.
- What batch-send means here: emails, invoices, proposals, or something else.
- Whether you have a look in mind. Otherwise I'll use Signal Results Group's look if you have one, or a neutral direction.

Once you say yes, I'll build one self-contained HTML review page. It will have three different layouts behind a switch, numbered review points, and a "Copy my answers" button. It will use sample data only. The timebox is one session and one feedback round.