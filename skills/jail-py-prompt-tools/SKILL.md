---
name: jail-py-prompt-tools
metadata:
  version: 1.0.0
description: >-
  JAIL-PY machine checks for engineered prompts — runnable Python companions to
  the jail-prompt skill. Use when jail-prompt calls for a machine check, or when
  the user asks to scan pasted input or files for secrets/API keys, lint an
  engineered prompt block for a complete skeleton and machine-verifiable
  SUCCESS TEST, validate a chain manifest's handoffs (produces/requires),
  check truth-tagged claims (Known/Infer/Unknown with evidence ids), or dry-run
  a prompt's declared OUTPUT FORMAT against a mock output. Triggers: "scan for
  secrets", "lint this prompt", "validate the chain manifest", "check the
  claims file", "dry-run the output format". Requires code execution
  (Python 3.8+, stdlib only). Not for authoring prompts — that's jail-prompt.
---

# JAIL-PY-PROMPT-TOOLS

Runnable verification for [jail-prompt](../jail-prompt/SKILL.md)'s workflow.
jail-prompt is instruction-only; this companion holds all the code. Every
script is stdlib-only Python 3.8+, takes files (or stdin) as arguments, and
exits non-zero on failure so it drops into CI or a pre-commit hook.

## The five checks

| Script | Backs (jail-prompt) | What it does | Exit |
|---|---|---|---|
| `scripts/secret-scan.py` | Phase 2 — Secure? | Flags hardcoded secrets / high-entropy keys in supplied inputs or files (AWS, OpenAI, GitHub, Google, Slack, Stripe, JWT, PEM, secret-assignments, entropy). | 0 clean · 1 found · 2 IO |
| `scripts/prompt-lint.py` | Phase 3 — sanity-check | Lints the engineered-prompt block: required skeleton sections, a machine-verifiable SUCCESS TEST, a concrete OUTPUT FORMAT, and that any embedded ```json parses. | 0 pass · 1 errors · 2 IO |
| `scripts/chain-lint.py` | Phase 3 — chain assembly | Verifies a chain manifest's handoffs: every key a step `requires` is produced by an earlier step or declared `inputs`; warns on missing/weak per-step or chain-level `success_test` and unused keys. | 0 pass · 1 errors · 2 IO |
| `scripts/truth-lint.py` | Phase 3 — truth-tagging | Validates an epistemic claim block: `status` is Known/Infer/Unknown, `evidence_count` matches `source_ids`, and a `Known` claim has evidence or a `settled` basis. `--require-evidence` forces evidence ids when SOURCES declares retrieval. | 0 pass · 1 errors · 2 IO |
| `scripts/dry-run.py` | Phase 3 — dry run | Confirms the declared OUTPUT FORMAT (JSON schema / JSON example / markdown table) parses and that a `--mock` output conforms. | 0 ok · 1 mismatch · 2 IO |

## Usage

```bash
# Secure check on whatever the user pasted/attached
python3 scripts/secret-scan.py path/to/input.txt        # or: echo "..." | python3 scripts/secret-scan.py

# Lint the engineered prompt before presenting it
python3 scripts/prompt-lint.py prompt.txt               # add --strict to fail on warnings

# Verify a chain manifest's handoffs before running the chain
python3 scripts/chain-lint.py chain.json                # add --strict to fail on warnings

# Validate truth-tagged claims (factual/research output)
python3 scripts/truth-lint.py claims.json               # add --require-evidence when SOURCES declares retrieval

# Dry-run the OUTPUT FORMAT against a mock output
python3 scripts/dry-run.py prompt.txt --mock mock.json
```

## Workflow

1. Write the artifact under test (prompt block, chain manifest, claims JSON, or
   mock output) to a temp file in the workspace.
2. Run the matching script; read stdout for the specific findings.
3. Exit 0 → report the artifact passed. Non-zero → fix the named findings in
   the artifact and re-run once; surface anything still failing to the user
   rather than looping.

## Gotchas
- **Reference by relative path.** Call these as `scripts/<name>.py` from this
  skill's folder; absolute machine-specific paths break on other installs.
- **No third-party deps.** Everything is stdlib; if an import fails, the Python
  environment is broken — don't pip-install to "fix" it.
- **A pass is not an endorsement.** Exit 0 means structurally valid, not that
  the prompt is *good* — jail-prompt's judgment layers still apply.
- **secret-scan on generated output too.** If the engineered prompt embeds
  user-supplied context, scan the final prompt block, not just the raw input.
- **Where code can't run** (claude.ai without code execution), don't fake a
  run — fall back to jail-prompt's manual checklists and say so.
