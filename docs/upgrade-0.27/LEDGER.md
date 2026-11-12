# Upgrade 0.27 ledger

NODE F1 | STATUS: verified | ARTIFACT: docs/JAIL-CONSTITUTION.md (Canonical claim labels) + docs/schemas/jail-handoff.schema.json (valid JSON)
NODE F5 | STATUS: verified | ARTIFACT: scripts/project-hosts.py --check exit 0; test_project_hosts 6 OK; .agents/skills = 26 + README
NODE F4 | STATUS: verified | ARTIFACT: scripts/tests 15 OK; run-live-evals.py --dry-run plan printed (12 runs for 3 cases)
NODE F2 | STATUS: verified | ARTIFACT: jail-py-toolkit tests 42 OK; pii-scan exit 1 with no values printed; label-lint/handoff-lint/desc-check run on live skills
NODE FIX | STATUS: verified | ARTIFACT: evals/behavioral-0.27 36 cases, all assertions tagged [O]/[F], JSON valid
NODE F3 | STATUS: verified | ARTIFACT: hooks/tests 19 OK; quarantine block exit 2 without value; off mode exit 0; approval_gate emits ask JSON for git push
NODE A-verify | STATUS: verified | ARTIFACT: desc-check OK, handoff-lint OK, label-lint OK, 147 lines
