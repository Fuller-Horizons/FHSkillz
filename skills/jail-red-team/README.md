# jail-red-team

You give it a plan, and it attacks that plan on purpose, before it ships, so real flaws show up now instead of later.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.2.0.

## What it does

This skill argues against your plan on purpose. First it builds the strongest version of the plan — a **steelman** — because tearing down a weak paraphrase proves nothing. Then it attacks that strong version. For a routine draft it runs a quick 10-minute check. For a big, contested call it runs a full sweep: hidden assumptions, biased reasoning, missing stakeholders, shaky dependencies, and more. Every flaw comes with a **falsifier**: the cheapest test that would prove the flaw right or wrong.

## Use it when

- Someone says "poke holes in this" or "what am I missing" before a plan goes to leadership
- A decision is costly and only works if everyone plays along and nothing goes wrong
- jail-decide or jail-verify sends a contested call here for a real gut-check

## Don't use it for

- Checking that a finished deliverable is complete, not hunting for what could go wrong — use [`jail-verify`](../jail-verify/) instead.
- Re-picking between options once the findings are in — use [`jail-decide`](../jail-decide/).
- A plan whose premise is so broken it should not proceed at all — that's a stop condition for [`jail-prompt`](../jail-prompt/), not an attack for this skill.

## What you get

A ranked list of findings, each with its cause, its fix, and a falsifier. It closes with what survived the attack, plus one verdict: proceed, proceed with fixes, or rethink.

## Example

**You ask:**

> Before I take this to the exec meeting, red-team our Zendesk migration plan. Northwind runs support through Zendesk: 50 agents, $96,000/year. Our platform team built Nimbus, which has run IT's internal helpdesk since March. The plan: a hard cutover on Sept 5, all 50 agents at once, Zendesk turned off the same night. Marcus, our only Nimbus engineer, goes on vacation Sept 8–19, right after cutover. Three enterprise contracts name Zendesk's audit-log and CSAT features by name. Is this plan solid enough to green-light?

**It produces:**

```
LANE: FULL SWEEP — consequential (customer-facing system of record, three contracts with named feature requirements, no revert path once Zendesk seats are cut) and contested (Marcus is confident on engineering readiness; Priya is asking for an outside check before putting her name on it in front of execs). Ordinary-draft or three-lens treatment would under-serve stakes this high.

STEELMAN: Northwind is paying $96,000/year for a product it has already rebuilt in-house — Nimbus has carried IT's internal helpdesk for 200 employees since March without incident, so this isn't a from-scratch, unproven build. A single hard cutover avoids the alternative failure mode of running two ticketing systems in parallel: agents split across two queues, customer history forked across two systems, and a longer total exposure window rather than a shorter, sharper one. Recovering the full license cost in year one is a real, material saving for a support org this size, and doing it now — before renewal terms lock in for another year — is the cheapest time to make the move.

RED-TEAM FINDINGS (ranked by severity × likelihood)
1. Contract-compliance exposure — severity: critical · basis: the plan states three enterprise contracts (Voss Freight, Calloway Retail, Ardent Supply) name Zendesk's audit-log and CSAT features specifically, and nothing in the plan indicates anyone has checked whether those contracts require Zendesk by name or merely equivalent capability, or whether Nimbus reproduces those features at all.
   → fix: Legal and Priya review the three contracts' literal language against Nimbus's actual feature list before the cutover date is finalized; get written sign-off or a contract amendment if Nimbus falls short.
   → falsifier: pull the three contracts and check whether they say "must use Zendesk" or "must provide audit-log/CSAT capability," then check that capability against Nimbus's feature list.
     · falsifier-status: HANDOFF → owner: Priya + Legal; jail-lab spec: contract-language audit paired with a Nimbus feature-parity checklist, due before cutover date is locked.
2. Single engineer is both the builder and the only rollback path, and he leaves 3 days after cutover — severity: critical · basis: the plan states Marcus is "our only Nimbus engineer" and his pre-planned vacation runs Sept 8–19, starting just 3 days after the Sept 5 hard cutover — precisely the window when post-launch defects and edge cases in a 400,000-ticket migration tend to surface. No co-owner, on-call backup, or documented runbook is mentioned.
   → fix: pair a second engineer on the migration script and runbook now, or move the cutover date so it isn't sandwiched against Marcus's vacation — either 3+ weeks before Sept 8, or after Sept 19.
   → falsifier: re-read the plan for any mention of a second engineer, an on-call backup, or a written runbook someone else could execute.
     · falsifier-status: RUN-NOW → result: confirmed (the plan names no backup engineer and no runbook).
...
Survives the attack: the underlying economics and direction are sound — $96,000/year is real, recoverable spend, and Nimbus already carries production load for 200 internal users, so this is a maturity-and-sequencing problem, not a build-from-scratch gamble.

Verdict: RETHINK — findings 1 and 2 are both critical and unresolved; a contract-compliance gap with three named enterprise accounts and a single-engineer rollback hole during the highest-defect window are each individually enough to hold the cutover date, and they compound.
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
