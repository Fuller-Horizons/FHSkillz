#!/usr/bin/env bash
# Repo pre-commit gate — install with:
#   ln -sf ../../scripts/pre-commit-hook.sh .git/hooks/pre-commit
# Validates every skill folder + marketplace sync before allowing a commit.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
python3 "$ROOT/scripts/validate-skills.py"
