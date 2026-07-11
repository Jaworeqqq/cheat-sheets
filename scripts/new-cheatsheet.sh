#!/usr/bin/env bash
# Tworzy nową ściągawkę z szablonu.
# Użycie: ./scripts/new-cheatsheet.sh <sciezka/docelowa/nazwa.md>
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE="$ROOT/_templates/cheatsheet-template.md"

if [[ $# -ne 1 ]]; then
  echo "Użycie: $0 <dzial/podkatalog/nazwa.md>" >&2
  exit 1
fi

DEST="$ROOT/$1"
if [[ -e "$DEST" ]]; then
  echo "Plik już istnieje: $DEST" >&2
  exit 1
fi

mkdir -p "$(dirname "$DEST")"
sed "s/YYYY-MM-DD/$(date +%F)/" "$TEMPLATE" > "$DEST"
echo "Utworzono: $DEST"
