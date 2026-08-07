# TODO-0010 — Riclassificare e rigenerare l’audit documentale TODO-0101

## Scopo

Applica `DOC-FIX-008`.

Operazioni:

- conserva byte per byte l’audit v0.1 nello storico;
- crea un nuovo audit v0.2 sul tree `docs/` risultante;
- conserva byte per byte il checkpoint v0.10 nello storico;
- crea il checkpoint v0.11 per riallineare il riferimento al nuovo audit v0.2;
- aggiorna il README di TODO-0101;
- aggiorna esclusivamente il collegamento all’audit nel Decision Log Data Model v0.9;
- non modifica alcuna decisione `DEC-0101-*`.

## Perché nasce anche checkpoint v0.11

Il checkpoint v0.10 puntava correttamente all’audit v0.1 quando fu creato. Poiché DOC-FIX-008 sposta v0.1 nello storico e rende v0.2 l’audit corrente, non viene riscritta retroattivamente v0.10: si crea v0.11.

## Applicazione

Estrarre lo ZIP nella root del progetto, quindi:

```bash
bash docs/10-executions/TODO-0010/APPLY_TODO-0010_GITBASH.sh
```

Nessuna operazione Git viene eseguita.

## Risultato atteso

- Audit TODO-0101 corrente: v0.2
- Audit v0.1: storico
- Checkpoint TODO-0101 corrente: v0.11
- Checkpoint v0.10: storico
- Decision Log corrente: v0.9
- TODO-0101: IN_ANALYSIS
