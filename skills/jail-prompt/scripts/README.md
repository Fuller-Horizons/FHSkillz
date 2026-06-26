# jail-prompt scripts

Bundled, stdlib-only helpers the skill invokes by relative path. No third-party
deps; run with any Python 3.8+. All exit non-zero on failure so they drop into
CI or a pre-commit hook.

| Script | Phase | What it does | Exit |
|---|---|---|---|
| `secret-scan.py` | Phase 2 — Secure? | Flags hardcoded secrets / high-entropy keys in supplied inputs or files (AWS, OpenAI, GitHub, Google, Slack, Stripe, JWT, PEM, secret-assignments, entropy). | 0 clean · 1 found · 2 IO |
| `prompt-lint.py` | Phase 3 — sanity-check | Lints the engineered-prompt block: required skeleton sections, a machine-verifiable SUCCESS TEST, a concrete OUTPUT FORMAT, and that any embedded ```json parses. | 0 pass · 1 errors · 2 IO |
| `dry-run.py` | Phase 3 — Dry Run Sandbox | Confirms the declared OUTPUT FORMAT (JSON schema / JSON example / markdown table) parses and that a `--mock` output conforms. | 0 ok · 1 mismatch · 2 IO |
| `chain-lint.py` | Phase 3 — chain assembly | Verifies a chain manifest's handoffs: every key a step `requires` is produced by an earlier step or declared `inputs`; warns on missing/weak per-step or chain-level `success_test` and unused keys. | 0 pass · 1 errors · 2 IO |
| `truth-lint.py` | Phase 3 — sanity-check | Validates an epistemic truth-tagged claim block: `status` is Known/Infer/Unknown, `evidence_count` matches `source_ids`, and a `Known` claim has evidence or a `settled` basis (`--require-evidence` forces evidence ids when SOURCES declares retrieval). | 0 pass · 1 errors · 2 IO |
| `validate-skills.py` | repo / maintenance | Validates skill folders (frontmatter, name match, manifest sync). | 0 ok · non-zero on problems |
| `pre-commit-hook.sh` | repo / maintenance | Runs validation before commit. | git hook |

## Usage

```bash
# Secure check on whatever the user pasted/attached
python3 scripts/secret-scan.py path/to/input.txt        # or: echo "..." | python3 scripts/secret-scan.py

# Lint the engineered prompt before presenting it
python3 scripts/prompt-lint.py prompt.txt               # add --strict to fail on warnings

# Dry-run the OUTPUT FORMAT against a mock output
python3 scripts/dry-run.py prompt.txt --mock scratch/mock.json

# Verify a chain manifest's handoffs before running the chain
python3 scripts/chain-lint.py chain.json                # add --strict to fail on warnings

# Validate truth-tagged claims (factual/research output)
python3 scripts/truth-lint.py claims.json               # add --require-evidence when SOURCES declares retrieval
```

Keep references to these **relative** (`scripts/<name>.py`) so they survive installation on any client.
