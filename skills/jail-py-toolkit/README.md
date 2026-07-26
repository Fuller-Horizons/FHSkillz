# jail-py-toolkit

This skill runs real Python scripts that check your prompts, ratings, and skill folders for problems before you ship them.

Part of the **[FHSkillz](../../README.md)** collection. Version 1.1.0.

## What it does

jail-py-toolkit is nine small Python scripts, not instructions. Each one checks a single thing, like a hidden secret or a bad prompt shape. You run a script on a file. It prints what it found and returns an exit code — a number that says pass or fail, so a hook or a CI job (an automated check that runs before code ships) can read it without a human. Two other skills, jail-prompt and jail-rate-skill, call this toolkit to run their checks for real, instead of guessing.

This skill needs Python 3.8 or later on your machine. If Python is not there, jail-prompt and jail-rate-skill still work on their own. They just switch to a manual version of each check and say so in their output.

## Use it when

- You wrote a prompt and want to know if it has a real, testable success check before you spend a run on it.
- You have a draft file and want to scan it for secrets, like API keys, before you paste it anywhere.
- You just finished a new skill folder and want to check that SKILL.md is set up right before you commit it.

## Don't use it for

- Writing the prompt itself — use [`jail-prompt`](../jail-prompt/) instead.
- Producing a skill rating — use [`jail-rate-skill`](../jail-rate-skill/) instead.

## What you get

Each script prints a short pass-or-fail report and one line per problem it found. It also returns an exit code your commit hook or CI job can check.

## Example

**You ask:**

> I just finished drafting the invoice-parser skill. Before I commit it, run the jail-py-toolkit checks: scan invoice_config.py for secrets, lint my prompt draft, and validate the skill folder structure.

**It produces:**

```
Ran the three backing scripts against the drafted files, from inside the draft folder.

$ python3 "C:/Dev/FHSkillz/skills/jail-py-toolkit/scripts/secret-scan.py" invoice_config.py
secret-scan: 2 potential secret(s) found:

  invoice_config.py:7: Stripe secret key -> sk_live_51Hj…
  invoice_config.py:8: OpenAI/Anthropic key -> sk-abcdefghi…

Replace these with environment variables (e.g. os.environ['API_KEY']) and use a restricted, read-only credential before generating the prompt.
EXIT:1
...
Summary — fix before you commit:
- secret-scan.py: fail. Two hardcoded keys in invoice_config.py, line 7 (Stripe) and line 8 (OpenAI). Move both to environment variables before this ships.
- prompt-lint.py: pass. All five required sections are present, the SUCCESS TEST is machine-verifiable, and OUTPUT FORMAT shows a worked JSON example.
- validate-skill-structure.py: pass. SKILL.md has frontmatter name + description, and the folder name matches.

JAIL-HANDOFF checks: {"secret-scan.py": "fail", "prompt-lint.py": "pass", "validate-skill-structure.py": "pass"} (source: jail-py-toolkit).
```

## More

[`SKILL.md`](SKILL.md) — the full instructions · [skill graph](../../docs/skill-graph.md) — how skills route to each other
