#!/usr/bin/env bash
set -euo pipefail

OLD="docs/10-executions/TODO-0101/02-checkpoint/TODO-0101_Checkpoint_Finale_Analisi_v0_9_DRAFT.md"
NEW="docs/10-executions/TODO-0101/02-checkpoint/TODO-0101_Checkpoint_Finale_Analisi_v0_10_DRAFT.md"
HIST="docs/10-executions/TODO-0101/90-history/checkpoints/TODO-0101_Checkpoint_Finale_Analisi_v0_9_DRAFT.md"
README="docs/10-executions/TODO-0101/README.md"
DLOG="docs/architecture/data-model/current/Project_Integrity_OS_Decision_Log_Data_Model_v0_9_DRAFT.md"

for f in "$NEW" "$HIST" "$README" "$DLOG"; do
  [[ -f "$f" ]] || { echo "ERRORE: file richiesto mancante: $f" >&2; exit 1; }
done

if [[ -f "$OLD" ]]; then
  rm "$OLD"
  echo "RIMOSSO DA CURRENT: $OLD"
fi

grep -q 'Checkpoint Index — TODO-0101 — v0.10' "$NEW"
grep -q 'Project_Integrity_OS_Decision_Log_Data_Model_v0_9_DRAFT.md' "$NEW"
grep -q 'TODO-0101_Checkpoint_Finale_Analisi_v0_9_DRAFT.md' "$NEW"
grep -q 'TODO-0101_Checkpoint_Finale_Analisi_v0_10_DRAFT.md' "$README"

if grep -q 'Project_Integrity_OS_Decision_Log_Data_Model_v0_8_DRAFT.md' "$NEW"; then
  echo "ERRORE: il nuovo checkpoint contiene ancora il riferimento al Decision Log v0.8." >&2
  exit 1
fi

echo "TODO-0009 APPLICATO E VERIFICATO LOCALMENTE."
echo "Checkpoint TODO-0101 corrente: v0.10."
echo "Checkpoint v0.9 conservato nello storico."
echo "Decision Log corrente referenziato: v0.9."
echo "Nessuna operazione Git è stata eseguita."
