#!/usr/bin/env bash
# Usage: ./scripts/new-skill.sh my-skill-name
set -euo pipefail
NAME="${1:?Usage: new-skill.sh <skill-name>}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/skills/$NAME"
[ -d "$DIR" ] && { echo "Skill '$NAME' already exists."; exit 1; }
mkdir -p "$DIR"
cat > "$DIR/SKILL.md" <<EOF
---
name: $NAME
description: TODO — describe exactly when Claude should use this skill (triggers, inputs, task verbs).
---

# ${NAME//-/ }

## When to use
- TODO

## Instructions
1. TODO
EOF
echo "Created skills/$NAME/SKILL.md"
"$ROOT/scripts/sync-marketplace.sh"
echo "Registered in marketplace.json. Edit the description before committing."
