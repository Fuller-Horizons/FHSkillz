#!/usr/bin/env bash
# Pre-commit hook to validate all skills in the repository.
# To install, copy or symlink this file to .git/hooks/pre-commit and make it executable:
#   cp scripts/pre-commit-hook.sh .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit

echo "=== Running Skills Pre-commit Validation ==="
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if command -v python3 &>/dev/null; then
    python3 "$SCRIPT_DIR/validate-skills.py" "$SCRIPT_DIR/../"
elif command -v python &>/dev/null; then
    python "$SCRIPT_DIR/validate-skills.py" "$SCRIPT_DIR/../"
else
    echo "[!] Error: Python is required to run the skills validator." >&2
    exit 1
fi
