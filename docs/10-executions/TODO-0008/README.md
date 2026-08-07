# TODO-0008 — Correzione metadati documenti architetturali

## Scopo

Questo pacchetto applica il punto 5/5 del piano di refactor documentale.

Interessa esclusivamente i 15 documenti decisionali correnti sotto:

`docs/architecture/data-model/current/`

## Modifiche consentite

Per tutti i 15 documenti:

- correggere il campo `Sostituisce`;
- puntare alla versione storica realmente presente sotto `../history/decisions/`;
- rimuovere dal nome storico il vecchio segmento `_TODO-0101`.

Nel solo documento 02:

- correggere il riferimento al documento 13 eliminando `_TODO-0101` dal nome.

## Vincolo

Il contenuto tecnico e decisionale non deve cambiare.

Il pacchetto è stato verificato con confronto riga per riga:

- 14 documenti: 1 sola riga modificata;
- documento 02: 2 sole righe modificate;
- nessun’altra differenza ammessa.

## Applicazione

Estrarre lo ZIP nella root del progetto e consentire la sovrascrittura dei 15 documenti.

Poi eseguire da Git Bash:

```bash
bash docs/10-executions/TODO-0008/APPLY_TODO-0008_GITBASH.sh
```

Lo script effettua soltanto verifiche locali. Non modifica Git e non elimina file.

## Dopo TODO-0008

Questo completa il quinto punto del ciclo documentale corrente.

Prima di procedere con il punto successivo occorre aggiornare:

- `Project_Integrity_OS_Piano_Modifiche_Documentazione_v0_2_CHECKLIST.md`
- `Project_Integrity_OS_Piano_Modifiche_Documentazione_v0_2_CHECKLIST.json`

marcando come completati i punti già applicati.
