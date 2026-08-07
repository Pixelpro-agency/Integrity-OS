#!/usr/bin/env bash
set -euo pipefail

DIR="docs/architecture/data-model/current"
HIST="docs/architecture/data-model/history/decisions"

files=(
"Project_Integrity_OS_01_Principi_Tracciabilita_Contesto_v0_2_DRAFT.md"
"Project_Integrity_OS_02_Modello_Gerarchico_Contesto_v0_2_DRAFT.md"
"Project_Integrity_OS_03_Context_Package_v0_2_DRAFT.md"
"Project_Integrity_OS_04_Provenienza_Informazioni_v0_2_DRAFT.md"
"Project_Integrity_OS_05_Sintesi_Drill_Down_v0_2_DRAFT.md"
"Project_Integrity_OS_06_Requisiti_Test_Tracciabilita_v0_2_DRAFT.md"
"Project_Integrity_OS_07_Lifecycle_Decisioni_v0_2_DRAFT.md"
"Project_Integrity_OS_08_Registro_Elementi_Irrisolti_v0_3_DRAFT.md"
"Project_Integrity_OS_09_Eventi_Ricostruzione_Temporale_v0_2_DRAFT.md"
"Project_Integrity_OS_10_Integrita_Trasversale_Anti_Orfano_v0_3_DRAFT.md"
"Project_Integrity_OS_11_Conservazione_Rettifiche_Cancellazione_v0_2_DRAFT.md"
"Project_Integrity_OS_12_Ruoli_Permessi_Sensibilita_Redazione_v0_3_DRAFT.md"
"Project_Integrity_OS_13_Transizioni_Condizioni_Complete_v0_2_DRAFT.md"
"Project_Integrity_OS_14_Cardinalita_Tabelle_Associative_v0_3_DRAFT.md"
"Project_Integrity_OS_15_Schema_Completo_Implementazione_Progressiva_v0_3_DRAFT.md"
)

for f in "${files[@]}"; do
  test -f "$DIR/$f" || { echo "ERRORE: manca $DIR/$f" >&2; exit 1; }

  line="$(grep -m1 '^\*\*Sostituisce:\*\*' "$DIR/$f" || true)"
  [[ -n "$line" ]] || { echo "ERRORE: Sostituisce mancante in $f" >&2; exit 1; }

  if grep -q '^\*\*Sostituisce:\*\* `Project_Integrity_OS_.*TODO-0101' "$DIR/$f"; then
    echo "ERRORE: vecchio riferimento TODO-0101 ancora presente nel campo Sostituisce di $f" >&2
    exit 1
  fi
done

if grep -q 'Project_Integrity_OS_13_Transizioni_Condizioni_Complete_TODO-0101_v0_2_DRAFT.md' \
  "$DIR/Project_Integrity_OS_02_Modello_Gerarchico_Contesto_v0_2_DRAFT.md"; then
  echo "ERRORE: vecchio riferimento al documento 13 ancora presente nel documento 02." >&2
  exit 1
fi

# Verifica che ogni target Sostituisce esista.
for f in "${files[@]}"; do
  target="$(grep -m1 '^\*\*Sostituisce:\*\*' "$DIR/$f" | sed -E 's/^\*\*Sostituisce:\*\* `([^`]+)`.*/\1/')"
  full="$DIR/$target"
  if [[ ! -f "$full" ]]; then
    echo "ERRORE: target Sostituisce non risolvibile per $f -> $target" >&2
    exit 1
  fi
done

echo "TODO-0008 APPLICATO E VERIFICATO LOCALMENTE."
echo "15 documenti architetturali verificati."
echo "Campi Sostituisce riallineati allo storico reale."
echo "Riferimento documento 02 -> documento 13 corretto."
echo "Nessuna operazione Git è stata eseguita."
