# Changelog — jail-py-toolkit

## 1.0.0 — 2026-07-22 (plugin 0.23.0)

Initial release as the merger of **jail-py-prompt-tools 1.0.0** (5 prompt
checks) and **jail-py-rate-tools 1.0.0** (4 rating checks), both retired
this release; script code carried over unchanged (git history holds
lineage).

- One toolkit, two check families, nine scripts, stable exit codes.
- New in the merge: the repo release validator (`scripts/validate-skills.py`)
  now runs the toolkit self-checks every release, so the checks fire on the
  release loop instead of only on request.
