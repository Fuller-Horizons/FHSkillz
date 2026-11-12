I'm using the **Full lane**: you'll reuse this every month and new hires will read the result, so it has to be tested. Below is what I found, the problems I'd raise, and three questions before I write and test anything.

## Phase 1: Frame

**What I found:** The prompt library has 4 tested prompts. None of them summarises documents, so this is a new prompt. There's no handbook in the Project or the working folder.

**What I understand you want:** each month, the handbook goes in and a one-page summary for new hires comes out. The real goal is that a new hire knows what to do, what they're owed, and who to ask in their first weeks, without the summary ever contradicting the handbook. I'm about 90% sure of this, not 97%. The gap is the word "monthly" (see question 1).

- **Task type:** summarising a document you supply. No web search, and nothing comes from the model's memory.
- **Mode:** Factual. Every line has to trace back to a passage in the handbook.
- **Objective:** turn the handbook into a one-page summary a new hire can act on, where every statement can be traced to a handbook section.
- **Success test (draft):** the summary is 500 words or fewer, so it fits one printed page. Every number and date in it appears word for word in the handbook (checked by script). Every section cites the handbook section it came from. There's a final line saying "the handbook governs." Text placed in the handbook to trick the model ("ignore the above") is never followed.

**Missing-context check:** 6 of 11 items are missing. These are the three that matter:

| # | Item | Status |
|---|---|---|
| 1 | Reader and use | Found: new hires, first weeks |
| 3 | How we'll know it worked | **Missing:** who approves the summary? |
| 4 | Input format | **Missing:** PDF, Word, Google Doc? |
| 5 | Edge cases | Assumed: state-specific addenda, outdated sections, tables |
| 7 | House style | Missing: any existing onboarding template? |
| 11 | Where it runs | **Missing:** which AI tool and model? |

## Phase 2: Viability gate (provisional: GO, with two challenges)

1. **Right tool?** Yes. Pulling the essentials out of one long document you supply is a good job for AI. No other skill or tool does it better.
2. **Can it be grounded?** Yes, completely, as long as the prompt uses only the handbook.
3. **Challenge 1 (is it worth running monthly?):** If the handbook doesn't change every month, running AI every month gives you a slightly different summary each time. Someone then has to re-check each version, and errors can creep in over time. If the handbook is stable, the cheaper and safer approach is to create the summary once, have someone sign off on it, and reuse the approved page. AI would only run again when the handbook is revised. When it does, the prompt should take the **last approved summary plus the revised handbook** and change only what changed, so the review is a short diff instead of a full re-read.
4. **Challenge 2 (legal risk):** New hires may treat this page as policy. If it gets the PTO accrual, the at-will wording or a reporting channel wrong, that's a real HR and legal exposure. So the summary needs "the handbook governs" on it and a person must sign off before it goes out. That human check stays even after testing.
5. **Security:** I'll treat the handbook text as data, not as instructions. One test input will include a planted instruction to check this. If the handbook lists staff names or phone numbers, mask them in anything you share with me.

## Three questions (each has a default)

1. **What actually changes each month: the handbook, or just the group of new hires?**
   *Default:* the handbook is revised now and then. I'll build two modes: **Create** (from the handbook alone) and **Update** (last approved summary + revised handbook, change only what changed, list the changes). If only the new hires change, I'd suggest making the summary once and dropping the monthly run.

2. **Can you share the handbook, with private details masked?**
   *Default:* I'll test on 5 synthetic handbooks, clearly labelled as synthetic, with planted traps:
   - conflicting PTO figures
   - a state-specific addendum
   - an outdated section
   - a policy table
   - an "ignore the above" instruction

   You'd then re-run the test on the real handbook before relying on the prompt. Testing on your real handbook would make the results much more meaningful.

3. **Where will it run, and who signs off?**
   *Default:* the Claude app with the handbook uploaded as a PDF, run on Sonnet 5.5 at medium effort. You or HR approve it before it goes to new hires. The output is a 450–500 word page you paste into your onboarding template.

**What testing involves once you answer:**
- 5 handbooks: 3 to tune the prompt on, 2 held back to check the tuning generalises.
- Each run 3 times; a handbook passes only if all 3 runs pass. That's 15 runs of my prompt.
- 15 runs of your original one-line request, so we can see whether my version actually beats it.
- Graded blind (outputs unlabelled and shuffled) by a separate grader agent.
- At most 2 rounds of fixes.

This uses subagents, so your reply is also your approval to start them. Reply **"defaults"** to go ahead with all three defaults, or answer any of the questions.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [handbook revised occasionally, not monthly; runs in Claude app on Sonnet 5.5; HR/owner signs off; one page = 500 words or fewer]
  unknowns: [monthly trigger; handbook format and real content; sign-off owner; house template]
  outputs: [frame + provisional GO; engineered prompt pending answers]
  next: answers (or "defaults") → write Create/Update prompt → lint → 5-input test, pass^3, baseline vs plain request
  approval_required: [subagent test runs; HR/legal sign-off on every summary before distribution; saving to prompt library]
  tested: untested: awaiting inputs and approval to run the test set
```