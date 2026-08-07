#!/usr/bin/env bash
set -euo pipefail

if [[ ! -d "docs" ]]; then
  echo "ERRORE: eseguire lo script dalla root del progetto, dove esiste la cartella docs/." >&2
  exit 1
fi

NEW="docs/10-executions/TODO-0101/02-checkpoint/TODO-0101_Checkpoint_Finale_Analisi_v0_9_DRAFT.md"
OLD="docs/10-executions/TODO-0101/02-checkpoint/TODO-0101_Checkpoint_Finale_Analisi_v0_8_DRAFT.md"
HIST="docs/10-executions/TODO-0101/90-history/checkpoints/TODO-0101_Checkpoint_Finale_Analisi_v0_8_DRAFT.md"
README="docs/10-executions/TODO-0101/README.md"

for f in "$NEW" "$HIST" "$README"; do
  if [[ ! -f "$f" ]]; then
    echo "ERRORE: file richiesto assente: $f" >&2
    exit 1
  fi
done

# La copia storica deve coincidere con la v0.8 corrente prima della rimozione, se presente.
if [[ -f "$OLD" ]]; then
  OLD_HASH=$(sha256sum "$OLD" | awk '{print $1}')
  HIST_HASH=$(sha256sum "$HIST" | awk '{print $1}')
  if [[ "$OLD_HASH" != "$HIST_HASH" ]]; then
    echo "ERRORE: la copia storica della v0.8 non coincide byte per byte con il file corrente." >&2
    exit 1
  fi
  rm -- "$OLD"
  echo "RIMOSSO DA CURRENT: $OLD"
else
  echo "NOTA: v0.8 non presente in 02-checkpoint; verifico comunque lo storico."
fi

# Verifiche essenziali
[[ -f "$NEW" ]]
[[ -f "$HIST" ]]
[[ ! -f "$OLD" ]]
grep -q 'TODO-0101_Checkpoint_Finale_Analisi_v0_9_DRAFT.md' "$README"
if grep -q 'TODO-0101_Checkpoint_Finale_Analisi_v0_8_DRAFT.md' "$README"; then
  echo "ERRORE: il README di TODO-0101 contiene ancora un riferimento corrente alla v0.8." >&2
  exit 1
fi

required=(
  "docs/architecture/data-model/current/Project_Integrity_OS_01_Principi_Tracciabilita_Contesto_v0_2_DRAFT.md"
  "docs/architecture/data-model/current/Project_Integrity_OS_15_Schema_Completo_Implementazione_Progressiva_v0_3_DRAFT.md"
  "docs/architecture/data-model/current/Project_Integrity_OS_Decision_Log_Data_Model_v0_8_DRAFT.md"
  "docs/architecture/data-model/history/consolidation/Project_Integrity_OS_Correction_Set_Data_Model_v0_2_DRAFT.md"
  "docs/planning/Project_Integrity_OS_Open_Issues_Data_Model_v0_1_DRAFT.md"
  "docs/10-executions/TODO-0101/03-verifica-documentale/TODO-0101_Audit_Documentale_v0_1_FINAL.md"
  "docs/00-current/Project_Integrity_OS_TODO_MVP_v0_10.md"
)
for f in "${required[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "ERRORE: riferimento richiesto non trovato: $f" >&2
    exit 1
  fi
done

echo "TODO-0006 APPLICATO E VERIFICATO LOCALMENTE."
echo "Checkpoint TODO-0101 corrente: v0.9."
echo "Checkpoint v0.8 conservato nello storico."
echo "Nessuna operazione Git è stata eseguita."
