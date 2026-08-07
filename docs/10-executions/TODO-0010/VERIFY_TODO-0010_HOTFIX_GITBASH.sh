#!/usr/bin/env bash
set -euo pipefail

CP="docs/10-executions/TODO-0101/02-checkpoint/TODO-0101_Checkpoint_Finale_Analisi_v0_11_DRAFT.md"
README="docs/10-executions/TODO-0101/README.md"
DLOG="docs/architecture/data-model/current/Project_Integrity_OS_Decision_Log_Data_Model_v0_9_DRAFT.md"
AUDIT="docs/10-executions/TODO-0101/03-verifica-documentale/TODO-0101_Audit_Documentale_v0_2_FINAL.md"
HIST_AUDIT="docs/10-executions/TODO-0101/90-history/TODO-0101_Audit_Documentale_v0_1_HISTORICAL.md"

for f in "$CP" "$README" "$DLOG" "$AUDIT" "$HIST_AUDIT"; do
  [[ -f "$f" ]] || { echo "ERRORE: manca $f" >&2; exit 1; }
done

grep -q 'Audit documentale TODO-0101 v0.2' "$CP"
grep -q 'TODO-0101_Audit_Documentale_v0_2_FINAL.md' "$CP"

grep -q 'TODO-0101 Audit Documentale v0.2' "$README"
grep -q '03-verifica-documentale/TODO-0101_Audit_Documentale_v0_2_FINAL.md' "$README"
grep -q 'TODO-0101_Checkpoint_Finale_Analisi_v0_11_DRAFT.md' "$README"

grep -q 'Audit documentale TODO-0101 v0.2' "$DLOG"
grep -q 'TODO-0101_Audit_Documentale_v0_2_FINAL.md' "$DLOG"

if grep -q 'Audit documentale TODO-0101 v0.1.*TODO-0101_Audit_Documentale_v0_2_FINAL.md' "$CP"; then
  echo "ERRORE: etichetta v0.1 residua nel checkpoint." >&2
  exit 1
fi

if grep -q 'Audit documentale TODO-0101 v0.1.*TODO-0101_Audit_Documentale_v0_2_FINAL.md' "$DLOG"; then
  echo "ERRORE: etichetta v0.1 residua nel Decision Log." >&2
  exit 1
fi

echo "TODO-0010 HOTFIX VERIFICATO."
echo "Checkpoint v0.11 -> Audit v0.2: OK"
echo "README TODO-0101 -> Audit v0.2: OK"
echo "Decision Log v0.9 -> Audit v0.2: OK"
echo "Audit v0.2 corrente: PRESENTE"
echo "Audit v0.1 storico: PRESENTE"
echo "Nessuna operazione Git è stata eseguita."
