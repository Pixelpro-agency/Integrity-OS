# Architettura del modello dati — documenti nati durante TODO-0101

## Funzione

Questa cartella raccoglie le decisioni architetturali nate durante l’analisi di TODO-0101 ma pertinenti all’intero Project Integrity OS.

Le decisioni definiscono, tra gli altri temi:

- tracciabilità e contesto;
- gerarchia Project, Work Item, Task Execution e Attempt;
- Context Package;
- provenienza delle informazioni;
- requisiti, criteri e test;
- lifecycle delle decisioni;
- elementi irrisolti;
- eventi e ricostruzione temporale;
- integrità anti-orfano;
- conservazione, rettifiche e cancellazione;
- ruoli, permessi e redazione;
- transizioni;
- cardinalità e tabelle associative;
- strategia tra schema completo e implementazione progressiva.

## Stato

I documenti nella cartella `current/` sono `DRAFT`: costituiscono input consolidato, ma non sono ancora lo schema fisico autorevole.

## Ordine di lettura

1. `current/Project_Integrity_OS_Decision_Log_Data_Model_v0_9_DRAFT.md`
2. documenti numerati `01` → `15` in `current/`
3. `../../planning/Project_Integrity_OS_Open_Issues_Data_Model_v0_1_DRAFT.md`
4. materiali in `history/` solo quando serve ricostruire l’evoluzione

## Uso futuro

Questi documenti dovranno alimentare:

- Schema Architecture;
- Entity Catalog;
- Data Dictionary;
- Relationship Matrix;
- Constraint Catalog;
- State and Transition Catalog;
- Portability Matrix;
- Implementation Wave Matrix;
- file globale delle Implementazioni;
- To-Do operativa aggiornata;
- brief esecutivo finale di TODO-0101.

Non devono essere copiati integralmente nei futuri file Implementazioni e To-Do: quei file dovranno tradurre le decisioni rispettivamente in sequenza costruttiva e task operative.
