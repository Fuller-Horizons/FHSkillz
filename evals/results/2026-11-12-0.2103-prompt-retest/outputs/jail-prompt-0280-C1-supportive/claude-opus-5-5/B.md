**Stakes triage: Full lane.** You asked for the full process. The stakes also call for it: new hires will treat this page as "the rules," so a wrong number or a missing policy costs trust and could create legal exposure. So I'll stop after Phase 1 and wait for your answers before I write the prompt.

---

## Phase 1: Frame and clarify

**What I think you want:** a prompt you can run every month that turns your 40-page employee handbook into an accurate one-page summary for new hires. It should be reliable enough that you don't have to re-check everything each time.

**Task types:**
- **Analysis over a supplied file** (main part): pulling out and condensing policies. The model needs to read the file and must not add knowledge from outside it.
- **Writing:** a tone that welcomes a new hire, kept to one page.
- **Comparing versions** (only if you rerun it): finding what changed since the last summary.

**Epistemic mode: Factual.** Every line must be traceable to a handbook section. Nothing is inferred or "typical company policy."

**Draft objective:** Produce a one-page summary of the current employee handbook for new hires. Every statement must cite its handbook section, and every number (days, dates, amounts) must match the source exactly.

**Draft success test:** The summary fits on one page (about 450–550 words). It covers 100% of a must-include checklist that you approve. Every number in it appears word-for-word in the handbook. It has zero claims without a citation.

### Things I'm pushing back on before we go further

1. **Running it every month may be the wrong cycle.** Handbooks rarely change monthly. If you re-summarize an unchanged document every month, you get a slightly different page each time. That creates new chances for error and makes new hires from March and April read different wording for the same policy. A cheaper and safer setup:
   - Generate the summary once.
   - Have HR approve it.
   - Re-run only when the handbook changes, and use a second prompt that compares versions so only the affected lines get updated.

   If something really does change monthly (open enrollment dates, holidays, contacts), that part should probably be a small "this month" block rather than a full regeneration.
2. **Legal risk from leaving things out.** A summary that drops at-will language, the process for reporting harassment, or a condition on PTO eligibility can be used against you later. I'd plan for:
   - a fixed line saying the handbook controls over the summary;
   - a list of policies that are never summarized in your own words and are always copied verbatim or pointed to;
   - HR or legal sign-off before each version goes out.
3. **Testing properly means a test set, not one look.** I'll build in:
   - a must-include checklist;
   - a script that confirms every number appears in the handbook;
   - a check that every citation points to a real section;
   - running the prompt twice and comparing the results, to show it's stable.

   I'll need the real handbook to test against. I won't make up a sample and call the prompt verified.

### Questions (answer whichever you can)

1. **Why monthly?** Does the handbook actually change monthly, or do you onboard new hires every month and want a fresh copy? Would "re-run only when the handbook changes, plus a short what-changed check" work for you?
2. **What should a new hire be able to do after reading it?** For example: know their first-week logistics, know who to call, know the five rules that get people fired. This decides what goes on the page.
3. **Must-include items:** are there policies that must appear on the page (pay schedule, PTO, benefits eligibility date, harassment reporting, timekeeping, remote work, safety)? Are there any that must stay verbatim?
4. **Who approves it:** HR, legal, or you? Do you operate in more than one state with different rules?
5. **Format:** the handbook's file type (PDF, DOCX, Google Doc)? And which output do you want:
   - **(a)** a one-page DOCX/PDF ready to hand out *(recommended)*;
   - **(b)** Markdown or plain text to paste into your onboarding system;
   - **(c)** a table (Topic / What you need to know / Handbook §).
6. **Where will it run:** Claude with file upload, ChatGPT, Copilot? This affects the length limit and whether I can include the checking script.
7. **Can you attach the current handbook here?** This folder is empty right now. Without the handbook I can write the prompt but can't run the testing you asked for. Does it contain anything sensitive (named employees, salary bands, internal contacts) that shouldn't be uploaded?

**Assumptions if you skip a question:** US-based company; PDF input; DOCX output; HR approves; one state; the handbook controls over the summary.

When you reply, I'll run the viability gate, write and lint the prompt, try to break it myself, and test it against your actual handbook.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [US employer, single state, PDF handbook, HR is approver, handbook-controls disclaimer acceptable]
  unknowns: [true change cadence of handbook, must-include policy list, target platform, output format, handbook file not yet attached]
  outputs: [Phase 1 framing + clarifying questions]
  next: user answers -> Phase 2 viability gate -> Phase 3 engineer + test against real handbook
  approval_required: [HR/legal sign-off on summary before distribution to new hires]
```