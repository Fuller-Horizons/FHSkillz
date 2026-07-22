# jail-py-toolkit

The JAIL suite's runnable check toolkit — nine stdlib-only Python scripts in
two families: **prompt checks** (secret scan, prompt lint, chain lint, truth
lint, output dry-run) backing `jail-prompt`, and **rating checks** (record
validation, history persistence with deltas, variance/drift, skill-structure
lint) backing `jail-rate-skill`. Stable exit codes on every script — built
for CI, pre-commit hooks, and the repo's release validator, which runs the
toolkit self-checks on every release.

Successor to `jail-py-prompt-tools 1.0.0` + `jail-py-rate-tools 1.0.0`,
merged at plugin 0.23.0: one install instead of two for the code-execution
half of the suite (fewer installs matters for the basic-user path), zero
script behavior changes in the merge.

Cores stay code-free per the repo rule; when code execution isn't available,
each backing skill's SKILL.md carries the manual fallback for every check.
