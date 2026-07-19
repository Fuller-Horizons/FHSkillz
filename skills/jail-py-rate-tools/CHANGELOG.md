# Changelog — jail-py-rate-tools

## 1.0.0
- New JAIL-PY companion skill. Receives rate-skill's four tools unchanged (`validate-rating.py`, `save-rating.py`, `variance-check.py`, `validate-skill-structure.py`) so the core skill can be instruction-only. Stdlib-only Python 3.8+ with stable exit codes; history via `${CLAUDE_PLUGIN_DATA}` with `~/.rate-skill/` fallback.
