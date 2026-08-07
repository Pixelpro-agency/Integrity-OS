#!/usr/bin/env bash
set -euo pipefail

ROOT="$(pwd)"
TARGET="docs/00-current/Project_Integrity_OS_TODO_MVP_v0_9.md"
NEW="docs/00-current/Project_Integrity_OS_TODO_MVP_v0_10.md"
HISTORY="docs/10-executions/TODO-0005/90-history/Project_Integrity_OS_TODO_MVP_v0_9_SUPERSEDED.md"

for required in "$NEW" "$HISTORY" "docs/README.md"; do
  if [[ ! -f "$required" ]]; then
    echo "ERRORE: file richiesto assente: $required" >&2
    exit 1
  fi
done

if [[ -f "$TARGET" ]]; then
  rm -- "$TARGET"
  echo "RIMOSSO: $TARGET"
else
  echo "GIÀ ASSENTE: $TARGET"
fi

if [[ -f "$TARGET" ]]; then
  echo "ERRORE: la To-Do v0.9 è ancora in 00-current" >&2
  exit 1
fi

if [[ ! -f "$NEW" ]]; then
  echo "ERRORE: la To-Do v0.10 non è presente" >&2
  exit 1
fi

echo "TODO-0005 APPLICATO E VERIFICATO LOCALMENTE."
echo "Nessuna operazione Git è stata eseguita."
