#!/usr/bin/env bash
set -euo pipefail

ROOT="$(pwd)"

if [[ ! -d "$ROOT/docs/00-current" || ! -d "$ROOT/docs/10-executions" ]]; then
  echo "ERRORE: eseguire lo script dalla root del progetto, dove esiste la cartella docs/." >&2
  exit 1
fi

TO_DELETE=(
  "docs/00-current/Project_Integrity_OS_Concetto_Integrita_Continuita_v0_6_SUPERSEDED.md"
  "docs/00-current/Project_Integrity_OS_Document_Registry_v0_6.md"
  "docs/00-current/Project_Integrity_OS_Document_Registry_v0_7.md"
  "docs/00-current/Project_Integrity_OS_TODO_MVP_v0_8.md"
)

REQUIRED=(
  "docs/README.md"
  "docs/00-current/Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md"
  "docs/00-current/Project_Integrity_OS_Modalita_Esecuzione_v0_1.md"
  "docs/00-current/Project_Integrity_OS_Convenzioni_Tecniche_v0_2.md"
  "docs/00-current/Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md"
  "docs/00-current/Project_Integrity_OS_Standard_Report_Sviluppo_v0_2.md"
  "docs/00-current/Project_Integrity_OS_TODO_MVP_v0_9.md"
)

for path in "${REQUIRED[@]}"; do
  if [[ ! -f "$path" ]]; then
    echo "ERRORE: file richiesto mancante dopo l'estrazione: $path" >&2
    exit 1
  fi
done

for path in "${TO_DELETE[@]}"; do
  if [[ -f "$path" ]]; then
    rm -- "$path"
    echo "RIMOSSO: $path"
  else
    echo "GIÀ ASSENTE: $path"
  fi
done

if ! grep -Fq '**Stato:** ACTIVE — baseline tecnica MVP' \
  "docs/00-current/Project_Integrity_OS_Convenzioni_Tecniche_v0_2.md"; then
  echo "ERRORE: Convenzioni Tecniche v0.2 non presenta lo stato atteso." >&2
  exit 1
fi

if ! grep -Fq '**Stato:** ACTIVE — baseline operativa MVP' \
  "docs/00-current/Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md"; then
  echo "ERRORE: il documento Prompt/Report non presenta lo stato aggiornato." >&2
  exit 1
fi

mapfile -t CURRENT_FILES < <(find docs/00-current -maxdepth 1 -type f -printf '%f\n' | sort)
EXPECTED=(
  "Project_Integrity_OS_Convenzioni_Tecniche_v0_2.md"
  "Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md"
  "Project_Integrity_OS_Modalita_Esecuzione_v0_1.md"
  "Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md"
  "Project_Integrity_OS_Standard_Report_Sviluppo_v0_2.md"
  "Project_Integrity_OS_TODO_MVP_v0_9.md"
)

if [[ "${CURRENT_FILES[*]}" != "${EXPECTED[*]}" ]]; then
  echo "ERRORE: docs/00-current non corrisponde allo stato atteso." >&2
  printf 'File osservati:\n' >&2
  printf '  %s\n' "${CURRENT_FILES[@]}" >&2
  exit 1
fi

echo
echo "TODO-0004 APPLICATO E VERIFICATO LOCALMENTE."
echo "Nessuna operazione Git è stata eseguita."
