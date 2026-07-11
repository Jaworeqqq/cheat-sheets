#!/usr/bin/env bash
# Creates a new cheat sheet from the template.
# Usage: ./scripts/new-cheatsheet.sh <path/to/name.md>
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE="$ROOT/_templates/cheatsheet-template.md"

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <section/subdir/name.md>" >&2
  exit 1
fi

DEST="$ROOT/$1"
if [[ -e "$DEST" ]]; then
  echo "File already exists: $DEST" >&2
  exit 1
fi

mkdir -p "$(dirname "$DEST")"
sed "s/YYYY-MM-DD/$(date +%F)/" "$TEMPLATE" > "$DEST"
echo "Created: $DEST"
