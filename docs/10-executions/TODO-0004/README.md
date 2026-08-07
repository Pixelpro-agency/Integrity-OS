# Project Integrity OS — TODO-0004

## Titolo

`TODO-0004 — Ripristinare e normalizzare la baseline documentale corrente`

## Stato del pacchetto

```text
PACKAGE_PREPARED
REPOSITORY_NOT_YET_MODIFIED
```

Questo archivio contiene i file da aggiungere o sovrascrivere e le istruzioni necessarie per applicare il refactor alla root del progetto.

## Obiettivo

Rendere `docs/00-current/` una cartella priva di versioni superate e ripristinare la baseline autentica `Convenzioni Tecniche v0.2`.

## Modifiche comprese

- creazione di `docs/README.md`;
- ripristino di `docs/00-current/Project_Integrity_OS_Convenzioni_Tecniche_v0_2.md` dalla copia originale approvata;
- aggiornamento dei soli metadati iniziali di `Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md`;
- rimozione pianificata di quattro file non più correnti;
- nessuna modifica alla To-Do v0.9;
- nessuna modifica ai documenti architetturali;
- nessuna modifica agli archivi autentici di TODO-0002, TODO-0003 o TODO-0101;
- nessuna operazione Git automatica.

## File da eliminare dalla root del progetto

Consultare `DELETE_FILES.txt` oppure eseguire lo script opzionale `APPLY_TODO-0004_GITBASH.sh` dopo aver estratto il pacchetto.

## Applicazione manuale

1. creare una copia di sicurezza della cartella `docs`;
2. estrarre il contenuto dello ZIP nella root del progetto;
3. autorizzare la sovrascrittura del documento Prompt/Report esistente;
4. eliminare i quattro file elencati in `DELETE_FILES.txt`;
5. verificare che `docs/00-current/` contenga soltanto i sei file elencati in `docs/README.md`;
6. non eseguire `git add`, commit, push o merge finché il risultato non è stato controllato.

## Applicazione con Git Bash

Dopo l'estrazione nella root del progetto:

```bash
bash docs/10-executions/TODO-0004/APPLY_TODO-0004_GITBASH.sh
```

Lo script:

- verifica di trovarsi nella root corretta;
- elimina esclusivamente i quattro percorsi elencati;
- verifica la presenza dei nuovi file;
- verifica lo stato atteso di `00-current`;
- non esegue comandi Git.

## Fuori perimetro

Le correzioni di To-Do v0.9, checkpoint TODO-0101, Decision Log, metadati dei quindici documenti e nuovo audit documentale restano demandate alla task successiva.
