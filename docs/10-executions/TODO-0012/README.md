# TODO-0012 — Correggere titolo sulle cardinalità

## Scopo

Applica `DOC-REC-003`.

File interessato:

`docs/architecture/data-model/current/Project_Integrity_OS_14_Cardinalita_Tabelle_Associative_v0_3_DRAFT.md`

## Modifica

Da:

`Cardinalità definitive e tabelle associative`

A:

`Cardinalità consolidate e tabelle associative`

## Vincolo

Nessun’altra parte del documento deve cambiare.

La verifica automatica del pacchetto ha confermato:

- una sola riga rimossa;
- una sola riga aggiunta;
- contenuto tecnico invariato.

## Applicazione

Estrarre lo ZIP nella root del progetto consentendo la sovrascrittura del documento 14, quindi eseguire:

```bash
bash docs/10-executions/TODO-0012/VERIFY_TODO-0012_GITBASH.sh
```

Lo script non esegue operazioni Git.
