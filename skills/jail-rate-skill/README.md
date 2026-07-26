# jail-rate-skill

This skill reads another AI skill and gives it a score you can trust and repeat.

Part of the **[FHSkillz](../../README.md)** collection. Version 2.3.0.

## What it does

You point it at a skill folder — the files that make up one AI skill, like a recipe card with extra notes attached. It reads the main file, `SKILL.md`, plus any support files. Then it scores the skill on 10 fixed categories, like safety and clarity, using the same yardstick every time. Each score comes with one concrete fix and a new score if you make that fix.

## Use it when

- You want to know if a skill is ready to ship.
- You are comparing two skills that do the same job and need a fair pick.
- You want proof a skill's scores don't drift each time you run it.
- You are rating every skill in a repo and want one sorted list at the end.

## Don't use it for

- Running a skill on live test prompts to see if it actually works — use Anthropic's `skill-creator` for that instead.
- Rating anything that is not an AI skill, like a business, a tool, or a person — use [`jail-rate`](../jail-rate/) instead.

## What you get

You get a full 10-category score table, two charts showing which editors and tools the skill works with, and a data file a computer can check and save for you.

## Example

**You ask:**

> Rate skills/jail-task-contract for me — I want to know if it's solid enough to keep as our default gate before every task, or if there are real gaps to patch first.

**It produces:**

```
### 1. Skill Rating Matrix

| Category | Rating<br>(0-10) | Rationale | Recommendation | Post Reco. Rating |
| :--- | :---: | :--- | :--- | :---: |
| **Utility & Value** | 8.3 | Layer-1 kernel skill invoked before nearly all non-trivial work (skill-graph.md: "Invoked by: everything"); trigger baseline confirms it fires correctly on a realistic scope-alignment prompt. No usage-frequency telemetry exists, so value is well-evidenced but not fully measured. | Log contract-emission events (skill + timestamp) to a local ledger so usage frequency becomes measured, not inferred. | 9.0 |
| **Clarity of Instructions** | 7.4 | Two distinct triage lanes (default vs. grill mode) and three type presets (RESEARCH/BUILD/ANALYSIS) give clear on-ramps; the 14-field order and SHIP-GATE checklist are unambiguous. But the file never shows one complete worked example of a filled contract. | Add a compact worked example (~15 lines, one sample 14-field contract) inline or in `references/example-contract.md`. | 8.8 |
| **Execution Reliability** | 5.8 | SHIP-GATE is a real, explicit fail-closed rule, and `behavioral-0.25` case 1 targets it directly — but per the repo's own baseline caveat that suite is "authored but not yet a trustworthy gate." No schema-validation script or config-saving exists; the gate is entirely model-self-enforced today. | Promote the behavioral-0.25 suite from authored to graded (producer/grader run + recorded pass rate); add a script that mechanically checks for the literal token "UNKNOWN" before a contract counts as shipped. | 8.0 |
| **Safety & Guardrails** | 8.0 | Concrete guardrails: secrets/PII named by class only, never pasted raw (field 5); field-14 actions wait on recorded human "approved"; an unlisted irreversible/external/durable/spend action found mid-run forces STOP+amend+re-approve. Eval case 2 directly targets the credential-by-class rule. No stated defense for third-party content pasted into the user's own request. | Add one line treating pasted third-party content in field 7 (Inputs available) as data, never instruction, mirroring jail-rate-skill's own injection-handling rule. | 8.8 |
| **Maintainability** | 7.2 | `metadata.version: 1.3.0` present; `CHANGELOG.md` ties each version to a plugin release and names its eval suite — genuinely well kept. No content-specific automated validator exists beyond the repo-wide structural linter, which checks frontmatter/name only, not the SHIP-GATE or field rules. | Wire this skill's SHIP-GATE and determinism claims into a CI/pre-commit check that re-runs `evals/behavioral-0.25/jail-task-contract.json` on any SKILL.md edit. | 8.5 |
| **Context & Token Efficiency** | 9.0 | Single ~125-line `SKILL.md`, no references to load, fully self-contained. Explicit numeric budgets: ≤2 rounds × ≤5 questions, ≤1200-word transcript, ≤1 line per field except 9/11/13 — the field-length cap is itself eval-tested (behavioral-0.25 case 3). | Add a word-counter check in jail-py-toolkit to enforce the 1200-word/1-line caps mechanically instead of by model self-report. | 9.4 |
...
| **Overall Rating** | **7.6** | Arithmetic mean of the 10 scores above, rounded to one decimal. | Apply all recommendations above. | **8.8** |
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
