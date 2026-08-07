#!/usr/bin/env bash
set -euo pipefail

OLD_AUDIT="docs/10-executions/TODO-0101/03-verifica-documentale/TODO-0101_Audit_Documentale_v0_1_FINAL.md"
NEW_AUDIT="docs/10-executions/TODO-0101/03-verifica-documentale/TODO-0101_Audit_Documentale_v0_2_FINAL.md"
HIST_AUDIT="docs/10-executions/TODO-0101/90-history/TODO-0101_Audit_Documentale_v0_1_HISTORICAL.md"

OLD_CP="docs/10-executions/TODO-0101/02-checkpoint/TODO-0101_Checkpoint_Finale_Analisi_v0_10_DRAFT.md"
NEW_CP="docs/10-executions/TODO-0101/02-checkpoint/TODO-0101_Checkpoint_Finale_Analisi_v0_11_DRAFT.md"
HIST_CP="docs/10-executions/TODO-0101/90-history/checkpoints/TODO-0101_Checkpoint_Finale_Analisi_v0_10_DRAFT.md"

README="docs/10-executions/TODO-0101/README.md"
DLOG="docs/architecture/data-model/current/Project_Integrity_OS_Decision_Log_Data_Model_v0_9_DRAFT.md"

for f in "$NEW_AUDIT" "$HIST_AUDIT" "$NEW_CP" "$HIST_CP" "$README" "$DLOG"; do
  [[ -f "$f" ]] || { echo "ERRORE: file richiesto mancante: $f" >&2; exit 1; }
done

[[ ! -f "$OLD_AUDIT" ]] || { rm "$OLD_AUDIT"; echo "RIMOSSO DA CURRENT: $OLD_AUDIT"; }
[[ ! -f "$OLD_CP" ]] || { rm "$OLD_CP"; echo "RIMOSSO DA CURRENT: $OLD_CP"; }

grep -q 'Audit documentale — TODO-0101 — v0.2' "$NEW_AUDIT"
grep -q 'Checkpoint Index — TODO-0101 — v0.11' "$NEW_CP"
grep -q 'TODO-0101_Audit_Documentale_v0_2_FINAL.md' "$NEW_CP"
grep -q 'TODO-0101_Audit_Documentale_v0_2_FINAL.md' "$README"
grep -q 'TODO-0101_Checkpoint_Finale_Analisi_v0_11_DRAFT.md' "$README"
grep -q 'TODO-0101_Audit_Documentale_v0_2_FINAL.md' "$DLOG"

echo "TODO-0010 APPLICATO E VERIFICATO LOCALMENTE."
echo "Audit TODO-0101 corrente: v0.2."
echo "Audit v0.1 conservato nello storico."
echo "Checkpoint TODO-0101 corrente: v0.11."
echo "Checkpoint v0.10 conservato nello storico."
echo "Decision Log v0.9 riallineato al nuovo audit."
echo "Nessuna operazione Git è stata eseguita."
