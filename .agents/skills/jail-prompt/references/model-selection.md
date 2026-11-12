# Model selection for subagent steps

Load this when assigning models in a delegation set (delegation.md) or the
RUN SETTINGS of a reusable prompt. Model facts (IDs, aliases, prices, effort
defaults) live in one dated table: [models.md](models.md).

## Mode: quality-first (default) or cost-first

`orchestration.mode` sets what "good enough" means for every step.

**quality-first (the default).** The bar is the best output the strongest
model would give.
- The lead agent's merge and the final check run on a strong model (Opus 5.5
  or Fable 5.2), never lower. The check runs on a different strong model from
  the one that produced what it checks (e.g. merge on Opus 5.5, check on Fable
  5.2).
- A cheaper model may keep a step **only with measured proof** that it scores
  the same as the strong model on that step's test items (`agent.selected_by`,
  below). Without proof, the step starts one tier up from the table and
  escalates from there.
- Cheap-first escalation (rule 5 below) still applies, so you pay strong-model
  prices only where the cheap model is proven equal or the item needs it.

**cost-first (only when the user asks for it, e.g. a quick internal draft).**
Cheapest model that passes the step's SUCCESS TEST, as in the table. Say in the
reply that the run was cost-first.

## Measured model selection

For any prompt set that will be reused, run at volume, or shipped to a client,
pick each step's model by test, not by table:

1. Take 3–5 test items for the step (typical, hard, edge; prompt-testing.md).
2. Run the step's brief on 2–3 candidate models: the strong model plus the
   one or two cheaper ones you hope to use. Same brief, same effort, same items.
3. Grade blind (labels shuffled, a fresh grader on a strong model) against the
   step's SUCCESS TEST and QUALITY BAR, pass/fail per check.
4. Choose the highest score. A tie goes to the cheaper model. In quality-first
   mode a cheaper model must **tie the strong model**, not just pass.
   With **jail-py-toolkit**: `select-models.py --prompt brief.md --items items.jsonl --checks checks.txt --candidates haiku,sonnet,opus --grader claude-fable-5-2` runs steps 2-4 and prints the record (`--dry-run` first to see the call count). Fallback: run and grade by hand as above.
5. Record it on the step and save it with the prompt in the library, so the
   trial isn't repeated until the model, the brief or the inputs change:

```json
{"selected_by": {
  "date": "2026-11-12",
  "items": 4,
  "candidates": ["haiku", "sonnet", "opus"],
  "scores": {"haiku": "16/16", "sonnet": "16/16", "opus": "16/16"},
  "grader": "fresh opus agent, blind"
}}
```

Re-run the selection when a new model generation ships (e.g. Fable 5.1 → 5.2)
or the step's brief changes. No way to run trials in this session → keep
quality-first defaults and list "model selection not measured" as an Unknown.

## Picking the model per step

| Work in the step | Model | Effort | Escalate to |
|---|---|---|---|
| Extract, classify, scan, reformat to a fixed schema | Haiku | low | Sonnet (failed or Unknown items only) |
| Draft, analyze, compare, grade against a rubric | Sonnet | medium | Opus |
| Lead agent: plan, merge, final synthesis for a client | Opus 5.5 | medium (high if high-stakes) | Fable 5.2 if Opus fails the test set |
| Independent check | A different strong model from the producer (Opus 5.5 or Fable 5.2) | medium | — |
| Security-testing steps | Opus 5.5 (Fable blocks and reroutes them) | medium | — |

A cheap step must have a machine-checkable SUCCESS TEST, so a miss is caught
and escalated rather than shipped. For a prompt set that will be reused, try
each cheap step on 2–3 test items first; if the cheap model fails more than one
in five, start that step one tier up.

Fable version rule (5.2 by default, 5.1 only when 5.2 isn't served or a tested
prompt was validated on 5.1): [generation-settings.md](generation-settings.md);
model facts: [models.md](models.md).
