# jail-council

Get a second and third opinion from independent AI passes before you trust an answer that has to be right.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.2.0.

## What it does

You give it a question that has a real right answer, but people disagree on it. Three separate passes answer it alone first. That is a **blind** answer — written before anyone sees anyone else's. Then it strips off the names and has each pass grade the others side by side. That is **anonymized** review, so nobody just agrees with their own work. A last pass, the **chairman**, reads every answer and review and writes one final answer, picking the best-backed claim over the most popular one.

## Use it when

- Two people on your team disagree about something technical, and "just trust me" is not good enough.
- You are about to do something risky — force-push a shared branch, sign off on a fix, ship a change — and want real second eyes first.
- A skill like jail-verify or jail-decide already flagged the call as high-stakes and contested.

## Don't use it for

- Splitting different subtasks across models to save time — that is parallel work, not a check. Use [`jail-orchestrate`](../jail-orchestrate/) instead.
- Questions with no provable answer, like taste or opinion. Use [`jail-red-team`](../jail-red-team/) for opinions, or [`jail-decide`](../jail-decide/) to choose between options you already understand.

## What you get

A final answer with a confidence level and source for each claim, a list of any real disagreement left standing, and an audit trail showing who said what and how hard the panel checked it.

## Example

**You ask:**

> quick council: my teammate says it's fine to rebase our shared feature/checkout branch and force-push, since force-with-lease makes it safe. But two teammates already pulled it and built 4-5 commits each on top. Is that actually safe?

**It produces:**

```
COUNCIL ANSWER — Is it safe for Sam to rebase feature/checkout and force-push it,
given Mia and Priya already have 4-5 local commits each on the old base?
Tier: C (3 independent same-model sessions, single working session — not cross-provider)

FINAL ANSWER
  Not "totally fine" as stated, but not impossible either — it depends on what
  happens after the push, not just the push itself.
  - The push itself can be made reasonably safe with `--force-with-lease`: it stops
    Sam from silently overwriting a remote update he hasn't seen. [Fact — git-scm.com
    git-push docs, verified live, High confidence]
  - That flag does nothing for Mia's and Priya's own local commits already built on
    the pre-rebase history — those are not visible to the remote-ref check at all.
    [Fact — git-scm.com git-push docs, High confidence]
  - Safe path: pause new commits on the branch → Sam rebases and pushes with
    `--force-with-lease` → Mia and Priya each `git fetch` then replay their own
    commits onto the new tip (e.g. `git rebase --onto origin/feature/checkout
    <old-base-sha> <their-branch>`), resolving conflicts per person. [Inference,
    synthesized from Member 3 + verification]
...
JAIL-HANDOFF: state=complete; tier=C (declared, not inflated); next: jail-verify if
Sam wants an independent recheck of this synthesis before force-pushing a branch
three people are actively working on.
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
