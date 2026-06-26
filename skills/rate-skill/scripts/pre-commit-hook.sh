#!/usr/bin/env bash
# Pre-commit hook for rate-skill maintainers.
# Install:  ln -sf ../../skills/rate-skill/scripts/pre-commit-hook.sh .git/hooks/pre-commit
# Runs the structural lint over every skill and validates any staged rating records.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(git rev-parse --show-toplevel)"

fail=0

# 1. Structural lint on all skills (if the repo has a skills/ dir)
if [ -d "$REPO/skills" ]; then
  python3 "$HERE/validate-skill-structure.py" "$REPO"/skills/*/ || fail=1
fi

# 2. Validate any staged *.json that looks like a rating record
staged="$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.json$' || true)"
for f in $staged; do
  if grep -q '"categories"' "$REPO/$f" 2>/dev/null && grep -q '"overall"' "$REPO/$f" 2>/dev/null; then
    python3 "$HERE/validate-rating.py" "$REPO/$f" || fail=1
  fi
done

if [ "$fail" -ne 0 ]; then
  echo "[!] pre-commit checks failed — commit aborted." >&2
  exit 1
fi
echo "[+] rate-skill pre-commit checks passed."
