# Project Integrity OS — Documentazione

## Scopo

Questa cartella è il punto di ingresso della documentazione del progetto.
La struttura separa le baseline correnti, gli archivi delle task, l'architettura in consolidamento e gli elementi di pianificazione.

## Ordine di lettura consigliato

1. `00-current/Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md`
2. `00-current/Project_Integrity_OS_Modalita_Esecuzione_v0_1.md`
3. `00-current/Project_Integrity_OS_Convenzioni_Tecniche_v0_2.md`
4. `00-current/Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md`
5. `00-current/Project_Integrity_OS_Standard_Report_Sviluppo_v0_2.md`
6. `00-current/Project_Integrity_OS_TODO_MVP_v0_10.md`
7. `architecture/data-model/README.md`, quando occorre consultare le decisioni sul modello dati
8. `planning/Project_Integrity_OS_Open_Issues_Data_Model_v0_1_DRAFT.md`, per gli elementi ancora da trasformare in implementazioni e task

## `00-current/`

Contiene esclusivamente documenti correnti, attivi o esplicitamente congelati come baseline.

Dopo il refactor TODO-0004 deve contenere:

- `Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md`
- `Project_Integrity_OS_Modalita_Esecuzione_v0_1.md`
- `Project_Integrity_OS_Convenzioni_Tecniche_v0_2.md`
- `Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md`
- `Project_Integrity_OS_Standard_Report_Sviluppo_v0_2.md`
- `Project_Integrity_OS_TODO_MVP_v0_10.md`

Non devono rimanere in questa cartella versioni `SUPERSEDED`, versioni precedenti della To-Do o registri documentali non più coerenti con il tree reale.

## `10-executions/`

Contiene gli archivi delle task eseguite, verificate, chiuse o rimaste in analisi.

- `TODO-0002/`: scaffold iniziale e relativo ciclo di esecuzione, verifica e chiusura.
- `TODO-0003/`: convenzioni tecniche e qualità, con correzione documentale post-chiusura.
- `TODO-0101/`: analisi dello schema dati minimo; la task resta `IN_ANALYSIS` e non autorizza ancora l'implementazione SQLite.
- `TODO-0004/`: ripristino e normalizzazione della baseline documentale corrente.
- `TODO-0005/`: riallineamento della To-Do corrente ai percorsi documentali reali.

Gli artefatti storici autentici non devono essere riscritti retroattivamente.

## `architecture/`

Contiene decisioni e progettazione globale del progetto.

`architecture/data-model/current/` raccoglie analisi consolidate ma ancora `DRAFT`: non costituisce da sola una baseline fisica approvata e non autorizza l'implementazione.

Le cartelle `history/` servono soltanto per ricostruzione, provenienza e audit.

## `planning/`

Contiene elementi aperti e sorgenti di pianificazione che devono alimentare i futuri file Implementazioni e To-Do.

## Regole documentali

- una sola versione corrente per ciascun documento dentro `00-current/`;
- nessun file `SUPERSEDED` dentro `00-current/`;
- i documenti storici restano negli archivi delle task o nelle cartelle `history/` già stabilite;
- i documenti architetturali `DRAFT` non devono essere presentati come implementazione approvata;
- la To-Do corrente resta il riferimento operativo per stato, priorità e prossime azioni;
- percorsi, manifesti e checksum devono essere rigenerati soltanto dopo il completamento del ciclo documentale che li modifica.

## Stato dopo TODO-0005

TODO-0005 riallinea la To-Do corrente e conserva la v0.9 come storico, ma non:
- modifica le decisioni architetturali;
- crea il checkpoint TODO-0101 v0.9;
- crea il Decision Log Data Model v0.9;
- avvia l'implementazione SQLite;
- porta TODO-0101 a `READY`.
