I haven't loaded anything yet, because this request goes against how this skill works. Here is what I can do instead.

**Why I stopped**
- **The scorecard layout question is already answered.** The ledger has it as B: headline plus 3 tiles, with the "This week…" insight under the tiles. I don't need to prototype it again.
- **The prototype can't be promoted.** The skill's rule is that the answer graduates and the code does not. The file is named `proto-weekly-scorecard`, and the ship gate requires zero files under production paths. It also uses fictional sample data (Harbor Point Heating & Air). Loading real customers into it would put client-confidential data in a throwaway file.
- **Sending to clients is an outside action.** That needs your explicit approval of the exact recipients and content, so I won't do it on my own.

**What I'd do instead**
1. Build a new production scorecard from the validated layout decision (B). It would have a proper name, no `proto-` prefix, and a data source that is separate from the layout.
2. Load the real customer list into that build, after a data check. I'd confirm which fields it holds, whether it contains personal or sensitive data, and who is allowed to see each client's figures.
3. Render one scorecard per client and check each against its source data before anything goes out. A wrong number in a client-facing report is the main risk of a Monday deadline.
4. Prepare the send as a batch for your approval. It would list recipients, content, and what can't be undone, and nothing would be sent until you approve.

**What I need from you**
- Where the customer list lives, and which metrics each client's scorecard should show.
- Where the real numbers come from (a CRM, a spreadsheet, or something else), since the prototype only had sample data.
- How the scorecards reach clients: one file each, a shared link, or an email. And are all clients meant to receive one?

Once I have those, I'll build the production version. I'll hold the send for your approval, which should keep Monday realistic. I haven't added a ledger line, since no new spike was run.