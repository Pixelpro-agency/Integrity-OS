# Project Integrity OS

## Standard del report di sviluppo — v0.1

**Stato:** baseline report MVP
**Data:** 2026-08-05
**Task:** TODO-0003
**Principio:** il report collega le evidenze, ma non sostituisce la verifica.

## 1. Scopo

Ogni task di sviluppo deve produrre un report normalizzato che indichi:

- task e repository;
- modalità di esecuzione;
- scope;
- file modificati;
- dipendenze;
- comandi;
- verifiche;
- errori;
- tentativi;
- stato Git;
- limiti residui;
- raccomandazione finale.

## 2. Classificazione delle informazioni

### Dichiarato

Informazione comunicata dall'esecutore o dall'operatore, ma non dimostrata direttamente dall'evidenza disponibile.

### Osservato

Informazione sostenuta da output, diff, file, screenshot o altro artefatto verificabile.

### Non verificato

Informazione rilevante che non è stata controllata o per cui l'evidenza è insufficiente.

Una dichiarazione non può essere trasformata in osservazione senza evidenza.

## 3. Esiti dichiarati del report

Valori ammessi:

- `SUCCESS`;
- `PARTIAL_SUCCESS`;
- `FAILED`;
- `BLOCKED`;
- `TECHNICAL_FAILURE`.

`SUCCESS` non significa automaticamente task chiusa, collaudo approvato, commit autorizzato o push autorizzato.

## 4. Identificazione obbligatoria

Il report deve contenere:

- task ID;
- titolo;
- repository;
- branch;
- modalità di esecuzione;
- stato;
- data di inizio e fine;
- tentativi usati;
- limite dei tentativi.

I valori non disponibili devono essere dichiarati come tali e non inventati.

## 5. Scope e file

Il report deve distinguere:

- file verificati;
- file creati;
- file modificati;
- file eliminati;
- file rinominati;
- baseline locale preservata;
- file generati;
- deviazioni dallo scope.

Per ogni deviazione devono essere indicati motivo, impatto e approvazione eventualmente ricevuta.

## 6. Dipendenze

Per ogni dipendenza aggiunta o aggiornata indicare:

- nome;
- versione;
- ecosistema;
- runtime o sviluppo;
- scopo;
- necessità;
- alternativa;
- manifest;
- lockfile;
- verifica eseguita.

## 7. Comandi

Devono essere elencati soltanto i comandi realmente eseguiti.

Per ogni comando indicare:

- comando;
- scopo;
- risultato;
- exit code, se osservato;
- evidenza disponibile.

Un exit code non mostrato non deve essere inventato.

## 8. Verifiche

La baseline tecnica comprende:

- `git diff --check`;
- `npm run format:check`;
- `npm run lint`;
- `npm run typecheck`;
- `npm run test`;
- `npm run build`;
- `cargo fmt --manifest-path "src-tauri/Cargo.toml" --all -- --check`;
- `cargo clippy --manifest-path "src-tauri/Cargo.toml" --all-targets --all-features -- -D warnings`;
- `cargo test --manifest-path "src-tauri/Cargo.toml"`;
- `cargo check --manifest-path "src-tauri/Cargo.toml"`;
- `npm run verify`.

Per ogni controllo indicare applicabilità, esecuzione, esito, evidenza e limiti.

## 9. Criteri di accettazione, artefatti e approvazioni

Il report deve elencare ogni criterio di accettazione usando il relativo identificatore stabile.

Per ogni criterio indicare:

- identificatore;
- descrizione;
- esito dichiarato;
- esito osservato;
- evidenza;
- eventuale motivo di blocco.

Gli artefatti devono indicare:

- identificatore;
- tipo;
- percorso dichiarato;
- obbligatorietà;
- stato osservato;
- eventuale checksum disponibile.

Le richieste di approvazione devono essere elencate separatamente e non possono essere considerate approvate senza una decisione umana osservabile.

## 10. Tentativi

Non consumano un tentativo:

- analisi;
- lettura;
- preflight;
- preparazione della patch;
- patch rifiutata prima dell'applicazione;
- comandi read-only.

Un tentativo inizia con la prima modifica applicata con successo.

Una correzione resta nello stesso tentativo se mantiene strategia, architettura e scope.

Dopo tre tentativi ragionati la task deve fermarsi.

## 11. Errori

Ogni errore significativo deve indicare:

- step;
- comando o azione;
- errore;
- impatto;
- risoluzione;
- tentativo.

Gli errori risolti non devono essere omessi dal report.

## 12. Git

Il report deve indicare:

- working tree iniziale;
- working tree finale;
- modifiche staged;
- commit policy;
- commit creato;
- commit SHA;
- push policy;
- push eseguito;
- remote.

Valori ammessi per commit e push:

- `FORBIDDEN`;
- `OPTIONAL`;
- `REQUIRED`.

## 13. Verifica macroscopica

Devono essere distinti:

- test automatici;
- verifica tecnica;
- avvio applicativo;
- verifica visuale;
- flusso manuale;
- collaudo umano.

Una build superata non dimostra automaticamente correttezza visuale o comportamento live.

## 14. Template minimo

Il report finale deve contenere almeno:

1. Identificazione
2. Scope autorizzato
3. Stato finale
4. Dichiarato
5. Osservato
6. Non verificato
7. File verificati, creati, modificati, eliminati e rinominati
8. Baseline locale preservata
9. Dipendenze
10. Comandi eseguiti
11. Verifiche
12. Test introdotti
13. Criteri di accettazione
14. Artefatti
15. Richieste di approvazione
16. Errori incontrati
17. Tentativi
18. Stato Git
19. Deviazioni
20. Rischi e limiti
21. Raccomandazione

Raccomandazioni ammesse:

- `READY_FOR_VERIFICATION`;
- `READY_FOR_HUMAN_REVIEW`;
- `NEEDS_CORRECTION`;
- `BLOCKED`;
- `STOPPED_AFTER_ATTEMPT_LIMIT`.

La raccomandazione non modifica autonomamente lo stato autorevole della task.

## 15. Criteri di conformità

Il report è conforme quando:

1. identifica univocamente la task;
2. separa dichiarato, osservato e non verificato;
3. elenca tutti i file della task;
4. preserva la baseline locale;
5. documenta dipendenze e comandi;
6. non inventa risultati o exit code;
7. registra gli errori risolti;
8. registra commit e push;
9. descrive rischi e limiti;
10. registra criteri di accettazione, artefatti e richieste di approvazione;
11. non dichiara autonomamente la task chiusa.
