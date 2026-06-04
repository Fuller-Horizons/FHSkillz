#!/usr/bin/env bash
# One-command jail-prompt eval harness — runs the suites through your local,
# authenticated `claude` CLI and prints pass/fail (results also written to
# evals/last-run.md).
#
# Requires: an installed + logged-in `claude` CLI (run `claude` once to log in)
#           and python3.
#
# Usage:
#   ./scripts/run-evals.sh                      # full suite (triggering + behavioral)
#   ./scripts/run-evals.sh --suite trigger      # triggering only (fast, 20 cases)
#   ./scripts/run-evals.sh --suite behavioral --runs 3   # behavioral, 3x for variance
#   ./scripts/run-evals.sh --model claude-sonnet-4-6 --limit 5
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

if ! command -v claude >/dev/null 2>&1; then
  echo "ERROR: no 'claude' CLI on PATH. Install Claude Code, then run 'claude' once to log in." >&2
  exit 1
fi
if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 is required." >&2
  exit 1
fi

exec python3 "$ROOT/scripts/run_evals.py" "$@"
