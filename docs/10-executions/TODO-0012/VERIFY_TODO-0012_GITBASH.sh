#!/usr/bin/env bash
set -euo pipefail

FILE="docs/architecture/data-model/current/Project_Integrity_OS_14_Cardinalita_Tabelle_Associative_v0_3_DRAFT.md"

[[ -f "$FILE" ]] || { echo "ERRORE: manca $FILE" >&2; exit 1; }

grep -q 'Cardinalità consolidate e tabelle associative' "$FILE"

if grep -q 'Cardinalità definitive e tabelle associative' "$FILE"; then
  echo "ERRORE: titolo precedente ancora presente." >&2
  exit 1
fi

echo "TODO-0012 APPLICATO E VERIFICATO LOCALMENTE."
echo "Titolo documento 14: Cardinalità consolidate e tabelle associative."
echo "Nessun’altra modifica prevista dal pacchetto."
echo "Nessuna operazione Git è stata eseguita."
