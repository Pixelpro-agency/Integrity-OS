# Project Integrity OS — TODO-0006

## Riallineare il checkpoint corrente di TODO-0101

**Stato:** `READY_TO_APPLY_LOCAL`  
**Tipo:** refactor documentale  
**Modifiche al codice:** nessuna  
**Operazioni Git:** nessuna

## Obiettivo

Creare `TODO-0101_Checkpoint_Finale_Analisi_v0_9_DRAFT.md` con collegamenti coerenti con il tree corrente, conservare la v0.8 byte per byte nello storico e aggiornare il README di TODO-0101 affinché punti al checkpoint v0.9.

## File aggiunti o aggiornati

- `docs/10-executions/TODO-0101/02-checkpoint/TODO-0101_Checkpoint_Finale_Analisi_v0_9_DRAFT.md`
- `docs/10-executions/TODO-0101/90-history/checkpoints/TODO-0101_Checkpoint_Finale_Analisi_v0_8_DRAFT.md`
- `docs/10-executions/TODO-0101/README.md`

## File da rimuovere

- `docs/10-executions/TODO-0101/02-checkpoint/TODO-0101_Checkpoint_Finale_Analisi_v0_8_DRAFT.md`

La v0.8 non viene eliminata dal patrimonio documentale: la copia nello storico è identica byte per byte.

## File di controllo TODO-0101

`FILE_MAP.csv`, `manifest.json` e `MANIFEST_SHA256.txt` **non vengono rigenerati in questo punto intermedio**. Il piano prevede la loro rigenerazione dopo il completamento delle correzioni documentali collegate, per evitare aggiornamenti ripetuti e subito obsoleti.

## Applicazione

Dalla root del progetto:

```bash
bash docs/10-executions/TODO-0006/APPLY_TODO-0006_GITBASH.sh
```

Lo script non esegue `git add`, commit, push o merge.
