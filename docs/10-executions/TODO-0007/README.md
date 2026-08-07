# TODO-0007 — Riallineare Decision Log Data Model

## Scopo

Questo pacchetto applica il punto 4/5 del piano di refactor documentale:

- crea `Project_Integrity_OS_Decision_Log_Data_Model_v0_9_DRAFT.md`;
- conserva la v0.8 byte per byte nello storico;
- corregge soltanto metadati, provenienza e collegamenti;
- mantiene inalterate le decisioni `DEC-0101-001` → `DEC-0101-020`;
- aggiorna gli indici correnti che devono puntare alla v0.9;
- non modifica il checkpoint TODO-0101 v0.9, perché esso fotografa correttamente lo stato precedente al presente riallineamento.

## File interessati

### Creati

- `docs/architecture/data-model/current/Project_Integrity_OS_Decision_Log_Data_Model_v0_9_DRAFT.md`
- `docs/architecture/data-model/history/decision-log/Project_Integrity_OS_Decision_Log_Data_Model_v0_8_DRAFT.md`

### Aggiornati

- `docs/architecture/data-model/README.md`
- `docs/10-executions/TODO-0101/README.md`

### Rimossi dalla posizione corrente

- `docs/architecture/data-model/current/Project_Integrity_OS_Decision_Log_Data_Model_v0_8_DRAFT.md`

## Modifiche nella v0.9

Sono consentite soltanto modifiche documentali:

1. versione `v0.8` → `v0.9`;
2. collegamento corretto alla versione precedente v0.8 nello storico;
3. aggiunta della provenienza globale delle decisioni;
4. collegamento corretto all'audit TODO-0101 nella struttura corrente.

Le venti decisioni e il relativo contenuto concettuale restano invariati.

## Applicazione

Estrarre lo ZIP nella root del progetto e poi, da Git Bash:

```bash
bash docs/10-executions/TODO-0007/APPLY_TODO-0007_GITBASH.sh
```

Lo script non esegue `git add`, commit, push o merge.

## Verifica attesa

Al termine:

- deve esistere soltanto la v0.9 nella cartella `current/`;
- la v0.8 deve esistere nello storico;
- `docs/architecture/data-model/README.md` deve puntare alla v0.9;
- `docs/10-executions/TODO-0101/README.md` deve puntare alla v0.9;
- le 20 decisioni devono essere identiche tra v0.8 e v0.9.
