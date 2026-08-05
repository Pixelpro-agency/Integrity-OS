# Project Integrity OS

## Standard del report di sviluppo — v0.2

**Stato:** ACTIVE — baseline report MVP
**Data:** 2026-08-05
**Task di origine:** TODO-0003
**Sostituisce:** `Project_Integrity_OS_Standard_Report_Sviluppo_v0_1.md`
**Motivo della revisione:** allineamento esplicito della baseline dei controlli al comando aggregato realmente configurato, includendo il controllo delle modifiche staged.
**Principio:** il report collega le evidenze, ma non sostituisce la verifica.

---

## 1. Scopo

Ogni task di sviluppo deve produrre un report normalizzato che indichi:

- task e repository;
- modalità di esecuzione;
- scope;
- file verificati e modificati;
- dipendenze;
- comandi;
- verifiche;
- test;
- criteri di accettazione;
- artefatti;
- errori;
- tentativi;
- stato Git;
- limiti residui;
- richieste di approvazione;
- raccomandazione finale.

Il report originale dell'esecutore deve essere conservato immutabile. Una successiva normalizzazione o verifica non deve riscriverlo retroattivamente.

---

## 2. Classificazione delle informazioni

### Dichiarato

Informazione comunicata dall'esecutore o dall'operatore, ma non dimostrata direttamente dall'evidenza disponibile.

### Osservato

Informazione sostenuta da output, diff, file, screenshot o altro artefatto verificabile.

### Non verificato

Informazione rilevante che non è stata controllata o per cui l'evidenza è insufficiente.

Una dichiarazione non può essere trasformata in osservazione senza evidenza.

Una deduzione deve essere indicata come tale e collegata alle evidenze usate.

---

## 3. Esiti dichiarati del report

Valori ammessi:

- `SUCCESS`;
- `PARTIAL_SUCCESS`;
- `FAILED`;
- `BLOCKED`;
- `TECHNICAL_FAILURE`.

`SUCCESS` non significa automaticamente:

- task chiusa;
- verifica superata;
- collaudo approvato;
- commit autorizzato;
- push autorizzato.

---

## 4. Identificazione obbligatoria

Il report deve contenere:

- schema o versione del formato;
- report ID, quando disponibile;
- task ID;
- titolo;
- repository;
- branch;
- modalità di esecuzione;
- stato;
- data di inizio e fine;
- tentativo ID, quando disponibile;
- numero di tentativo;
- tentativi usati;
- limite dei tentativi;
- prompt utilizzato e relativa versione.

I valori non disponibili devono essere dichiarati come tali e non inventati.

---

## 5. Scope e file

Il report deve distinguere:

- file verificati;
- file creati;
- file modificati;
- file eliminati;
- file rinominati;
- baseline locale preservata;
- file generati;
- file fuori scope osservati;
- deviazioni dallo scope.

Per ogni deviazione devono essere indicati:

- motivo;
- impatto;
- rischio;
- risoluzione;
- approvazione eventualmente ricevuta.

Un file non osservato non deve essere attribuito automaticamente alla task.

---

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
- comando usato per l'aggiornamento;
- verifica eseguita.

I lockfile devono essere aggiornati tramite il package manager e non manualmente.

---

## 7. Comandi

Devono essere elencati soltanto i comandi realmente eseguiti.

Per ogni comando indicare:

- comando;
- scopo;
- directory di lavoro, quando rilevante;
- risultato;
- exit code, se osservato;
- stdout/stderr rilevante;
- evidenza disponibile.

Un exit code non mostrato non deve essere inventato.

Catene shell concluse senza stampa dell'exit code possono essere classificate come evidenza indiretta, purché il limite sia dichiarato.

---

## 8. Verifiche

La baseline tecnica comprende:

- `git diff --check` per modifiche non staged;
- `git diff --cached --check` per modifiche staged;
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

Per ogni controllo indicare:

- applicabilità;
- esecuzione;
- esito;
- exit code osservato;
- evidenza;
- limiti.

Quando `npm run verify` comprende controlli aggregati, il report deve elencare sia il comando aggregato sia i controlli coperti.

Il controllo staged deve essere eseguito dopo aver inserito nello staging tutti e soltanto i file intenzionalmente appartenenti alla task.

---

## 9. Test

Per ogni test indicare:

- identificatore stabile, quando previsto;
- nome;
- file;
- comportamento protetto;
- comando di esecuzione;
- esito;
- numero di test superati, falliti e ignorati quando osservabile;
- limite dell'evidenza.

Una compilazione riuscita non sostituisce un test reale.

---

## 10. Criteri di accettazione, artefatti e approvazioni

Il report deve elencare ogni criterio di accettazione usando il relativo identificatore stabile quando previsto dal Task Contract.

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

---

## 11. Tentativi

Non consumano un tentativo:

- analisi;
- lettura;
- preflight;
- preparazione di file o modifiche non ancora applicate;
- modifica rifiutata prima dell'applicazione;
- comandi read-only.

Un tentativo inizia con la prima modifica applicata con successo.

Una correzione resta nello stesso tentativo se mantiene strategia, architettura e scope.

Dopo tre tentativi ragionati la task deve fermarsi e produrre un report diagnostico.

Il report deve indicare esplicitamente:

- tentativi consumati;
- correzioni rimaste nello stesso tentativo;
- motivazione di eventuali eccezioni umane.

---

## 12. Errori

Ogni errore significativo deve indicare:

- step;
- comando o azione;
- errore;
- impatto;
- risoluzione;
- tentativo;
- evidenza disponibile.

Gli errori risolti non devono essere omessi dal report.

Un errore tecnico dopo l'avvio del tentativo è normalmente consumante, salvo decisione umana registrata.

---

## 13. Git

Il report deve indicare:

- working tree iniziale;
- working tree finale;
- modifiche staged;
- modifiche non staged;
- file non tracciati;
- branch;
- remote;
- commit policy;
- commit creato;
- commit SHA;
- messaggio commit;
- push policy;
- push eseguito;
- branch e remote del push;
- verifica della presenza remota, quando applicabile.

Valori ammessi per commit e push:

- `FORBIDDEN`;
- `OPTIONAL`;
- `REQUIRED`.

L'esecuzione materiale di commit o push deve essere distinta dall'autorizzazione a eseguirli.

---

## 14. Verifica macroscopica

Devono essere distinti:

- test automatici;
- verifica tecnica;
- avvio applicativo;
- verifica visuale;
- flusso manuale;
- collaudo umano;
- verifica del repository oltre il write scope.

Una build superata non dimostra automaticamente correttezza visuale o comportamento live.

---

## 15. Template minimo

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
12. Test introdotti o eseguiti
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

---

## 16. Report originale e normalizzazione

Il testo originale ricevuto dall'esecutore deve restare immutabile.

Una verifica successiva può produrre:

- report normalizzato;
- tabella di riconciliazione;
- verifica indipendente;
- nota post-chiusura.

Questi documenti devono essere collegati all'originale senza sostituirlo e devono dichiarare chiaramente quali informazioni sono state aggiunte, verificate o corrette.

---

## 17. Criteri di conformità

Il report è conforme quando:

1. identifica univocamente la task;
2. separa dichiarato, osservato e non verificato;
3. elenca tutti i file della task;
4. preserva la baseline locale;
5. documenta dipendenze e comandi;
6. comprende sia `git diff --check` sia `git diff --cached --check` quando applicabili;
7. non inventa risultati o exit code;
8. registra gli errori risolti;
9. registra autorizzazione ed esecuzione di commit e push come fatti distinti;
10. descrive rischi e limiti;
11. registra criteri di accettazione, artefatti e richieste di approvazione;
12. conserva immutabile il report originale;
13. non dichiara autonomamente la task chiusa.
