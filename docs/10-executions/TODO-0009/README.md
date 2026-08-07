# TODO-0009 — Riallineare checkpoint TODO-0101 al Decision Log v0.9

## Scopo

Questo pacchetto risolve `FOLLOWUP-001` del piano documentale.

Il checkpoint TODO-0101 v0.9 era corretto al momento della sua creazione, quando il Decision Log corrente era v0.8. Dopo TODO-0007 il Decision Log v0.9 è diventato corrente e la v0.8 è stata spostata nello storico.

Per non riscrivere retroattivamente il checkpoint v0.9, viene creata una nuova versione:

`TODO-0101_Checkpoint_Finale_Analisi_v0_10_DRAFT.md`

## Modifiche

- conserva checkpoint v0.9 byte per byte nello storico;
- crea checkpoint v0.10;
- aggiorna il riferimento al Decision Log corrente da v0.8 a v0.9;
- aggiorna la versione precedente da checkpoint v0.8 a checkpoint v0.9;
- aggiorna la data del nuovo checkpoint;
- aggiorna `docs/10-executions/TODO-0101/README.md` affinché indichi v0.10 come checkpoint corrente;
- non modifica le decisioni architetturali;
- non modifica gli archivi di TODO-0006.

## Applicazione

Estrarre lo ZIP nella root del progetto, quindi eseguire:

```bash
bash docs/10-executions/TODO-0009/APPLY_TODO-0009_GITBASH.sh
```

Lo script non esegue alcuna operazione Git.

## Risultato atteso

- checkpoint corrente: v0.10;
- checkpoint v0.9: storico;
- Decision Log corrente referenziato: v0.9;
- TODO-0101: ancora `IN_ANALYSIS`;
- implementazione SQLite: non iniziata.
