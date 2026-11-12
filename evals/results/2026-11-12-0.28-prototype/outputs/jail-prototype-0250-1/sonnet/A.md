I checked the spike ledger, and it has no entry for the batch-send screen. The only entry is the weekly scorecard layout, which is a different question. I haven't built anything yet. The skill says a prototype needs a named question, and "mock something up and see how it feels" doesn't have one.

The project docs also don't describe the batch-send screen. I don't know what it sends, to whom, or what the user is trying to do on it. Here are some candidate questions, depending on your answers.

**Recommended (look question, three layouts):**
> *Which of three batch-send layouts lets someone confirm who is about to receive what, and catch a wrong recipient or message, before pressing Send?*

The three variants would differ in information structure, not colour:
- **A. Single review list.** One table of recipients with the message preview per row, and a Send All button at the bottom.
- **B. Group and preview.** Recipients grouped by message template, with one preview per group and a per-group send.
- **C. Stepped flow.** Pick recipients, then review the message, then confirm with a summary of counts and exceptions.

**Alternatives, if the real worry is different:**
- **Logic question:** what should happen when some sends fail, such as retry, partial-success state or undo?
- **Feasibility question:** can the screen handle a large batch without feeling stuck?

**I need from you:**
1. Is the recommended question the one you want answered, or should I use an alternative?
2. What does the batch send out (prospect outreach emails, client scorecards, invoices) and to roughly how many people at a time?
3. Should it follow the Signal Results look, or should I use a neutral direction? I'll use sample data only, with no real client or prospect records.

I'll use the default timebox of one session and one feedback round. Once you say yes, I'll build `proto-batch-send.html` as a single file, marked "PROTOTYPE — wipe me", with numbered review points and a Copy my answers button. Your pasted answers become the evidence for the verdict.