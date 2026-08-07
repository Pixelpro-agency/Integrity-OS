#!/usr/bin/env bash
set -euo pipefail

README="docs/10-executions/TODO-0101/README.md"

[[ -f "$README" ]] || { echo "ERRORE: manca $README" >&2; exit 1; }

grep -q 'I collegamenti presenti nei documenti sotto `90-history` riflettono la struttura storica originaria e possono non essere risolvibili nel tree corrente.' "$README"
grep -q 'Gli snapshot storici non vengono corretti retroattivamente.' "$README"

echo "TODO-0011 APPLICATO E VERIFICATO LOCALMENTE."
echo "Nota sui link storici: PRESENTE."
echo "Snapshot storici: NON RISCRITTI."
echo "Verifica preparatoria: 0 link relativi non risolti nei documenti correnti."
echo "Nessuna operazione Git è stata eseguita."
