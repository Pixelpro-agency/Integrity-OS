# TODO-0013 — Rigenerazione finale metadati v2

Questa versione sostituisce il primo pacchetto TODO-0013, che usava un hash precalcolato dell'Audit v0.2 non coincidente con la variante effettivamente presente nel repository locale.

## Correzione

Lo script:

1. preserva l'Audit v0.2 locale nello storico;
2. preserva il Checkpoint v0.11 locale nello storico;
3. crea Audit v0.3 con metriche ricalcolate sul tree effettivo;
4. crea Checkpoint v0.12;
5. riallinea README TODO-0101 e Decision Log v0.9;
6. rigenera FILE_MAP.csv;
7. rigenera manifest.json;
8. rigenera MANIFEST_SHA256.txt;
9. calcola `current_sha256` direttamente dai file locali;
10. verifica la preservazione byte-per-byte dei file sorgente che devono essere immutati.

## Applicazione

Estrarre lo ZIP nella root del progetto, quindi:

```bash
bash docs/10-executions/TODO-0013/APPLY_TODO-0013_V2_GITBASH.sh
```

Non esegue operazioni Git.
