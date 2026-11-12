I built the batch-send mock-up as a throwaway prototype. It's delivered as `proto-batch-send.html`, at `/tmp/claude-0/-tmp-fhlive-v22bdxi0/f6e2cd5c-0b82-4562-a94f-bd6ce5780a3a/scratchpad/proto-batch-send/proto-batch-send.html`.

**The question I named:** Does the three-state approval flow (ready / needs attention / approved) feel right for batch sends? You didn't name a question, and nothing in the project defines the batch-send screen, so I took this reading. Tell me if you meant something else.

**Three variants, switchable at the top:**
- **A · Matrix:** one table with checkboxes, a check column, and a send button showing the approved count.
- **B · One at a time:** a card per email with a progress bar. Keys a, s and b approve, skip and go back.
- **C · Lanes + gate:** three columns (Ready, Needs attention, Approved). Sending requires typing the approved count.

The data is six fictional companies with reserved example addresses. Two are blocked, so you can see how the flow handles a recipient that can't be approved. Approval state carries across the three variants, so you can compare them on the same batch.

**Surfaced state:** a panel below shows the counts, each recipient's status, and a log of every action. Nothing leaves the page. The send is simulated.

**Not verified:** I couldn't run the page in a browser or syntax-check the script here, because my shell commands were blocked for approval. Please open it and tell me if anything is broken.

**Next step:** Tell me which variant feels right, or what felt wrong about the others. I'll record the verdict in the spike ledger then, not before, because the answer is your reaction. I haven't written anything to the project yet.