#!/usr/bin/env bash
set -euo pipefail

OLD="docs/architecture/data-model/current/Project_Integrity_OS_Decision_Log_Data_Model_v0_8_DRAFT.md"
NEW="docs/architecture/data-model/current/Project_Integrity_OS_Decision_Log_Data_Model_v0_9_DRAFT.md"
HIST="docs/architecture/data-model/history/decision-log/Project_Integrity_OS_Decision_Log_Data_Model_v0_8_DRAFT.md"
ARCH_README="docs/architecture/data-model/README.md"
TODO_README="docs/10-executions/TODO-0101/README.md"

for f in "$NEW" "$HIST" "$ARCH_README" "$TODO_README"; do
  if [[ ! -f "$f" ]]; then
    echo "ERRORE: file richiesto mancante: $f" >&2
    exit 1
  fi
done

if [[ -f "$OLD" ]]; then
  rm "$OLD"
  echo "RIMOSSO DA CURRENT: $OLD"
fi

grep -q "Decision Log — TODO-0101 — v0.9" "$NEW"
grep -q "Project_Integrity_OS_Decision_Log_Data_Model_v0_9_DRAFT.md" "$ARCH_README"
grep -q "Project_Integrity_OS_Decision_Log_Data_Model_v0_9_DRAFT.md" "$TODO_README"

# Verifica che le 20 decisioni siano identiche.
old_decisions="$(grep '^DEC-0101-' "$HIST" || true)"
new_decisions="$(grep '^DEC-0101-' "$NEW" || true)"
if [[ "$old_decisions" != "$new_decisions" ]]; then
  echo "ERRORE: le decisioni DEC-0101 sono cambiate tra v0.8 e v0.9." >&2
  exit 1
fi

count="$(grep -c '^DEC-0101-' "$NEW" || true)"
if [[ "$count" -ne 20 ]]; then
  echo "ERRORE: attese 20 decisioni, trovate $count." >&2
  exit 1
fi

echo "TODO-0007 APPLICATO E VERIFICATO LOCALMENTE."
echo "Decision Log corrente: v0.9."
echo "Decision Log v0.8 conservato nello storico."
echo "20 decisioni DEC-0101 verificate come inalterate."
echo "Nessuna operazione Git è stata eseguita."
