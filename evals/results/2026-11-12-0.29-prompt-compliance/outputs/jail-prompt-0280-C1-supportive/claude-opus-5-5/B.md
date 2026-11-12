# JAIL-PROMPT: new-hire handbook summary

**Lane: Full.** You'll reuse this prompt every month and new hires will act on what it says. A summary that gets a policy wrong (who to report harassment to, how PTO accrues, at-will wording) costs trust and could create legal exposure. Per the process, I stop after Phase 1 and ask what I can't find myself.

## What I checked first
- **Prompt library** (`claude/prompt-library.md`): four tested prompts, none for handbook or onboarding summaries. Nothing to reuse.
- **Project docs and files:** no handbook. The PDF only has generic HR prompt one-liners (#218 New Manager Onboarding), and none of them fit.
- **Working directory:** empty. **I don't have your handbook,** and that's the main gap for testing it properly.

## Phase 1: Frame

**What I think you want:** a reusable prompt that turns your 40-page handbook into one page a new hire reads on day one. The page should tell them what they must do, what they're entitled to, and who to contact, without misstating any policy.

**The underlying need:** new hires absorb the rules that matter, and HR stops re-summarizing by hand each time. Comprehension is about 85%, below my 97% bar, so there are questions below.

**One concern before the questions:** if the handbook doesn't change monthly, regenerating the summary every month works against you. Each run words things a bit differently, so March hires and April hires get slightly different versions of the same policy, and someone has to re-check each one. The better design is to **generate once, have HR approve it, and reuse that approved page.** The prompt then gets an **update mode**: give it the last approved summary and the new handbook, and it changes only the lines tied to sections that changed. Review drops to a short diff.

| Item | Decision |
|---|---|
| Task type | Analysis of a supplied document. If you want a formatted Word file at the end, that step goes to the `docx` skill. |
| Mode | **Factual.** No speculation; anything the handbook doesn't say is marked "Not stated in handbook." |
| Objective | Produce a one-page new-hire summary where every statement traces to a handbook section. |
| Success test (draft) | ≤ 550 words. Every bullet cites a handbook section number. Every number and date matches the handbook exactly (script check). All items on a must-include checklist are present or marked "Not stated" (e.g. pay schedule, PTO, benefits eligibility, conduct and anti-harassment reporting, safety, attendance, at-will or acknowledgment, key contacts). |
| Output format (default) | One page of Markdown that pastes into Word or Google Docs: *Your first week · Pay & time off · Benefits · How we work · If something goes wrong · Who to ask*. It ends with "This summary does not replace the handbook; the handbook governs." |

## Three questions (each has a default if you skip it)

1. **Can you share the handbook?** A PDF or DOCX dropped here is enough. Also: is it Signal Results Group's own handbook, or will you run this on client handbooks too?
   *Default:* I build 3 synthetic test handbooks: a typical one, a hard one (policies scattered and contradicting each other), and an edge case (state-specific addenda, missing sections). I test against those, label the results "synthetic," and you do one supervised run on the real handbook before relying on it.

2. **Why monthly?** Does the handbook actually change every month, or do you just onboard a new group each month?
   *Default:* generate once and get approval, then run update mode only when the handbook changes.

3. **Who approves it before new hires see it, and in what format?**
   *Default:* HR (or you) signs off on every new or updated version. Output is the Markdown page above, and a branded Word version is optional.

Once you answer (or say "use defaults"), I'll run the viability gate and write the prompt with both modes. Then I'll test it: 3–5 inputs, blind pass/fail grading, up to 2 fix rounds, and a head-to-head against the plain request "summarize this handbook in one page for new hires." If my prompt doesn't beat that plain request, I'll tell you and give you the simpler one.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [summary is internal HR use, handbook is the sole source, HR approves before distribution]
  unknowns: [handbook file, own vs client handbooks, actual change cadence, approver, delivery format]
  outputs: [Phase 1 frame]
  next: user answers 3 questions (or "use defaults") → Phase 2 viability → Phase 3 engineer + test
  approval_required: [HR/legal sign-off on any summary before it reaches new hires]
```