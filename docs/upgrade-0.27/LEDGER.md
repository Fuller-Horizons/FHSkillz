# Upgrade 0.27 ledger

NODE F1 | STATUS: verified | ARTIFACT: docs/JAIL-CONSTITUTION.md (Canonical claim labels) + docs/schemas/jail-handoff.schema.json (valid JSON)
NODE F5 | STATUS: verified | ARTIFACT: scripts/project-hosts.py --check exit 0; test_project_hosts 6 OK; .agents/skills = 26 + README
NODE F4 | STATUS: verified | ARTIFACT: scripts/tests 15 OK; run-live-evals.py --dry-run plan printed (12 runs for 3 cases)
NODE F2 | STATUS: verified | ARTIFACT: jail-py-toolkit tests 42 OK; pii-scan exit 1 with no values printed; label-lint/handoff-lint/desc-check run on live skills
