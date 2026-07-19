# Changelog — jail-py-prompt-tools

## 1.0.0
- New JAIL-PY companion skill. Receives jail-prompt's five machine checks unchanged (`secret-scan.py`, `prompt-lint.py`, `chain-lint.py`, `truth-lint.py`, `dry-run.py`) so the core skill can be instruction-only. Scripts are stdlib-only Python 3.8+ with stable exit codes.
