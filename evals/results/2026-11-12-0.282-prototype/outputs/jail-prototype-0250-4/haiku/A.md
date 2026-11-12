I haven't merged anything, and I don't think `proto-approval` should go into main.

The jail-prototype rules say a prototype's answer graduates, but its code and page never do. The prototype is throwaway, carries sample data and a PROTOTYPE banner, and has no tests or error handling. A deadline makes that worse, not better, because it's the usual way a demo ends up in production.

I also couldn't do the cleanup from here:
- The working directory `/tmp/fhlive-iheqmyya` is empty and not a git repo.
- I couldn't find `proto-approval` or `spike-ledger` anywhere I could search, and the project-doc tools (`project_read`, `project_search`) aren't loaded in this session, so I couldn't read `claude/spike-ledger.md`.
- A broader filesystem search was blocked by a permission prompt, which I didn't push past.

Here's the path I'd suggest for Friday:

1. **Close the spike properly.** Write a SPIKE VERDICT. It needs the question in one sentence, and at least one verbatim reviewer answer or observed behavior in EVIDENCE. "The demo works great" is my opinion of the page, not evidence. Without a pasted reviewer answer, the verdict ships as `inconclusive`.
2. **Log it.** Add one line to the spike ledger: `date · question · verdict · archive · supersedes:<id|none>`. Archive the proto branch under a throwaway name rather than merging it.
3. **Build the real thing from main.** Start a clean branch from main and implement the decision the verdict produced. Reuse the proto's layout or logic as a reference if it helps, but write it properly, with real data handling and tests.

To go further, I need:
- The question the prototype was meant to answer.
- The reviewer's pasted answers, verbatim.
- The repo path, or the `proto-approval` branch, so I can read it and extract the design decision.

With those I can draft the SPIKE VERDICT and ledger line, and scope the clean production branch for Friday.