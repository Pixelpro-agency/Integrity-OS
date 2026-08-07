# Project Integrity OS
## To-Do del primo MVP — v0.10

**Documento di riferimento:** [`Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md`](Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md)  
**Regola:** ogni voce indica i paragrafi funzionali a cui è collegata.  
**Stato corrente:** TODO-0001, TODO-0002, TODO-0003 e TODO-0004 completate; TODO-0101 è `IN_ANALYSIS`. Il consolidamento decisionale è documentato nell'area architetturale, mentre i deliverable finali restano da produrre prima di rendere la task `READY`.  
**Sostituisce:** `Project_Integrity_OS_TODO_MVP_v0_9.md`

---

## Legenda

Stati:

- `TODO`
- `IN_ANALYSIS`
- `READY`
- `IN_PROGRESS`
- `BLOCKED`
- `IN_VERIFICATION`
- `DONE`

Priorità:

- `P0` indispensabile al vertical slice;
- `P1` necessario all’MVP ma non al primo flusso end-to-end;
- `P2` utile dopo il primo collaudo;
- `DEFERRED` rinviato.

---

# EPIC 0 — Fondazioni e vincoli

## TODO-0001 — Congelare la specifica del vertical slice

**Riferimenti:** FL-01, FL-02, FL-20, FL-23, FL-24  
**Priorità:** P0  
**Stato:** DONE

Definire e approvare formalmente:

- obiettivo;
- non-obiettivi;
- criteri di accettazione;
- dipendenze;
- vincoli deterministic-first;
- assenza obbligatoria di API IA nel primo vertical slice.

**Done quando:**

- documento dei flussi approvato;
- To-Do approvata;
- nessun requisito ambiguo bloccante.

---

## TODO-0002 — Creare struttura iniziale del repository Project Integrity OS

**Riferimenti:** FL-21  
**Priorità:** P0  
**Dipende da:** TODO-0001 — soddisfatta  
**Stato:** DONE

**Avvio esecuzione:** 2026-08-04 23:51 Europe/Rome  
**Brief utilizzato:** [`TODO-0002_01_Brief_Esecuzione_v0_2_USED_THEN_SUPERSEDED.md`](../10-executions/TODO-0002/01-esecuzione-effettiva/TODO-0002_01_Brief_Esecuzione_v0_2_USED_THEN_SUPERSEDED.md)  
**Brief finale archiviato:** [`TODO-0002_08_Brief_Finale_Chiusura_v0_3_FINAL.md`](../10-executions/TODO-0002/04-chiusura-documentale/TODO-0002_08_Brief_Finale_Chiusura_v0_3_FINAL.md)  
**Modalità utilizzata:** `BROWSER_OPERATOR_ASSISTED`  
**Documento modalità:** [`Project_Integrity_OS_Modalita_Esecuzione_v0_1.md`](Project_Integrity_OS_Modalita_Esecuzione_v0_1.md)  
**Prompt utilizzato:** [`TODO-0002_02_Prompt_Browser_Operatore_v0_1_USED.md`](../10-executions/TODO-0002/01-esecuzione-effettiva/TODO-0002_02_Prompt_Browser_Operatore_v0_1_USED.md)  
**Chiusura:** 2026-08-05 02:15 Europe/Rome  
**Verifica indipendente:** SUPERATA  
**Approvazione umana:** APPROVATA  
**Deviazione accettata:** `DEV-TODO-0002-001`  
**Baseline Git:** autorizzata; commit locale da creare senza push  
**Archivio completo:** [`docs/10-executions/TODO-0002/`](../10-executions/TODO-0002/README.md)

Creare il progetto Tauri 2 con:

- frontend React;
- TypeScript;
- Vite;
- core Rust;
- struttura modulare iniziale;
- configurazione Windows.

**Done quando:**

- applicazione avviabile in sviluppo;
- finestra desktop funzionante;
- frontend comunica con un comando Rust minimo;
- nessuna logica di dominio nel frontend.

---

## TODO-0003 — Definire convenzioni tecniche e qualità

**Riferimenti funzionali:** FL-02, FL-03, FL-21  
**Riferimento operativo vincolante:** [`Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md`](Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md)  
**Priorità:** P0  
**Dipende da:** TODO-0002 — soddisfatta  
**Stato:** DONE

**Chiusura:** 2026-08-05 20:02 Europe/Rome  
**Modalità utilizzata:** `BROWSER_OPERATOR_ASSISTED`  
**Prompt utilizzato:** [`TODO-0003_Prompt_Browser_Operatore_v0_1_USED.md`](../10-executions/TODO-0003/01-esecuzione-effettiva/TODO-0003_Prompt_Browser_Operatore_v0_1_USED.md)  
**Report esecutivo:** [`TODO-0003_Report_Esecutore_v0_1_RAW_FINAL.md`](../10-executions/TODO-0003/02-risultato-esecutore/TODO-0003_Report_Esecutore_v0_1_RAW_FINAL.md)  
**Verifica indipendente:** SUPERATA  
**Approvazione umana:** APPROVATA  
**Tentativi utilizzati:** 1  
**Commit locale:** autorizzato  
**Commit di chiusura osservato:** `e33bab77c5032c0aefdbf18fb2cde1afd2a5ea9d`  
**Push incluso nell'approvazione:** NO  
**Push osservato:** eseguito manualmente dall'utente verso `origin/main`; il commit di chiusura risulta presente sul branch remoto `main`  
**Correzione documentale post-chiusura:** [`TODO-0003_Correzione_Documentale_Post_Chiusura_v0_1_FINAL.md`](../10-executions/TODO-0003/05-post-chiusura/TODO-0003_Correzione_Documentale_Post_Chiusura_v0_1_FINAL.md)  
**Convenzioni tecniche correnti:** [`Project_Integrity_OS_Convenzioni_Tecniche_v0_2.md`](Project_Integrity_OS_Convenzioni_Tecniche_v0_2.md)  
**Standard report corrente:** [`Project_Integrity_OS_Standard_Report_Sviluppo_v0_2.md`](Project_Integrity_OS_Standard_Report_Sviluppo_v0_2.md)  
**Archivio completo:** [`docs/10-executions/TODO-0003/`](../10-executions/TODO-0003/README.md)

**Chiarimento operativo approvato:** le policy Git `commit` e `push` utilizzano i valori `FORBIDDEN`, `OPTIONAL` e `REQUIRED`. Questa decisione precisa operativamente i precedenti campi sì/no senza modificare gli obiettivi del vertical slice.

Definire e rendere operative:

- formattazione;
- lint;
- test Rust;
- test TypeScript;
- naming;
- gestione strutturata degli errori;
- logging;
- convenzioni per le migrazioni;
- comandi standard di verifica;
- regola dei tentativi conforme al lifecycle approvato;
- formato obbligatorio dei report di sviluppo;
- collegamento concettuale tra Rule Catalog, prompt, report e verifica.

La task deve recepire, senza ancora implementare integralmente:

- Prompt Schema v1;
- Report Schema v1;
- Rule Catalog v1;
- lifecycle preliminare dei tentativi;
- distinzione tra dichiarazioni, evidenze, riconciliazione e verifica;
- futura persistenza relazionale più payload JSON.

**Fuori scope per TODO-0003:**

- schema SQL definitivo;
- adapter SQLite;
- generatore automatico dei prompt;
- importatore dei report;
- interfaccia definitiva del Rule Catalog;
- Reconciliation Engine;
- macchina a stati definitiva;
- verifica Git completa.

**Done quando:**

- comandi di controllo documentati;
- formattazione e lint configurati;
- test di esempio Rust e TypeScript passano;
- gestione errori e logging possiedono una baseline minima;
- convenzioni tecniche documentate;
- report standard di sviluppo approvato e coerente con il documento operativo;
- nessuna funzione appartenente alle task successive è stata implementata anticipatamente.

---

## TODO-0004 — Ripristinare e normalizzare la baseline documentale corrente

**Priorità:** P0  
**Dipende da:** TODO-0003 — soddisfatta  
**Stato:** DONE

**Scopo:** ripristinare la baseline documentale approvata, eliminare versioni superate da `docs/00-current/` e creare un punto di ingresso semplice alla documentazione.

**Risultati:**

- ripristinata `Project_Integrity_OS_Convenzioni_Tecniche_v0_2.md` dalla copia autentica;
- creato `docs/README.md`;
- riclassificato come baseline attiva il documento Prompt/Report/Rule Catalog/Lifecycle;
- rimossi da `00-current` Concetto v0.6 SUPERSEDED, Registry v0.6, Registry v0.7 e To-Do v0.8;
- nessuna decisione architetturale o funzione software modificata.

**Archivio:** [`docs/10-executions/TODO-0004/`](../10-executions/TODO-0004/README.md)

**Done quando:**

- `00-current` contiene una sola versione corrente per documento;
- Convenzioni Tecniche v0.2 è presente;
- nessun file `SUPERSEDED` resta in `00-current`;
- `docs/README.md` è il punto di ingresso della documentazione.

---

# EPIC 1 — Persistenza locale per progetto

## TODO-0101 — Definire schema dati minimo

**Riferimenti:** FL-04, FL-05, FL-06, FL-07, FL-09, FL-10, FL-16, FL-18, FL-19  
**Priorità:** P0  
**Dipende da:** TODO-0001 — soddisfatta  
**Baseline tecnica disponibile:** TODO-0003 — soddisfatta  
**Stato:** IN_ANALYSIS

**Avvio dell’analisi documentale:** 2026-08-06  
**Indice della task:** [`docs/10-executions/TODO-0101/README.md`](../10-executions/TODO-0101/README.md)  
**Documentazione architetturale:** [`docs/architecture/data-model/README.md`](../architecture/data-model/README.md)  
**Registro degli elementi aperti:** [`docs/planning/Project_Integrity_OS_Open_Issues_Data_Model_v0_1_DRAFT.md`](../planning/Project_Integrity_OS_Open_Issues_Data_Model_v0_1_DRAFT.md)  
**Decisioni consolidate:** `DEC-0101-001` → `DEC-0101-020`  
**Correzioni consolidate:** `C-0101-001` → `C-0101-009`  
**Commit di integrazione in main:** `382c96f1f93de4ef6003f92db209675ab36d3c3c`

Le decisioni e le analisi prodotte durante TODO-0101 sono conservate nella documentazione architetturale globale. La To-Do non ne duplica il contenuto e non le presenta come schema fisico già approvato.

La task non è ancora `READY` e non autorizza l’implementazione SQLite.

**Deliverable ancora obbligatori:**

1. Schema Architecture;
2. Entity Catalog;
3. Data Dictionary;
4. Relationship Matrix;
5. Constraint Catalog;
6. State and Transition Catalog;
7. Portability Matrix;
8. Implementation Wave Matrix;
9. brief esecutivo finale;
10. approvazione e congelamento della baseline.

**Prossima azione:** completare e verificare i deliverable finali, risolvere o assegnare esplicitamente gli open issue e produrre il brief esecutivo.

**Condizioni per `READY`:**

- deliverable finali completi e reciprocamente coerenti;
- entità, relazioni, cardinalità e vincoli definiti;
- separazione CONTROL/PROJECT DATABASE formalizzata nei deliverable;
- riferimenti globali senza FK cross-database definiti;
- tipi compatibili con una futura migrazione PostgreSQL;
- nessuna dipendenza da `rowid`;
- open issue risolti o assegnati esplicitamente a TODO-0102/TODO-0103;
- brief esecutivo approvato;
- passaggio a `READY` mediante decisione esplicita.

**Done quando:**

- la baseline dello schema dati è congelata e approvata;
- la task può essere eseguita senza decisioni architetturali mancanti;
- il passaggio a `READY` è registrato esplicitamente.

---

## TODO-0102 — Implementare SQLite adapter

**Riferimenti:** FL-04.1, FL-04.2, FL-21
**Priorità:** P0
**Dipende da:** TODO-0101
**Stato:** TODO

Implementare:

- creazione database per progetto;
- apertura;
- migrazioni versionate;
- transazioni;
- foreign key;
- repository interface;
- test di persistenza.

**Done quando:**

- database creato in area privata;
- schema migrato;
- chiusura/riapertura senza perdita dati;
- test automatici passano.

---

## TODO-0103 — Implementare registro globale minimo

**Riferimenti:** FL-04.2
**Priorità:** P0
**Dipende da:** TODO-0102
**Stato:** TODO

Campi:

- project_id;
- name;
- repository_path;
- database_path;
- last_opened_at;
- schema_version;
- availability_status.

**Done quando:**

- più progetti possono essere registrati;
- ogni progetto apre il proprio database;
- nessun dato operativo è duplicato nel registro globale.

---

## TODO-0104 — Backup ed export iniziale

**Riferimenti:** FL-04.1, FL-17, FL-22
**Priorità:** P1
**Dipende da:** TODO-0102
**Stato:** TODO

Implementare:

- backup manuale del database;
- checksum;
- export JSON canonico minimo;
- manifest del pacchetto.

**Done quando:**

- un progetto può essere esportato;
- backup validato;
- ripristino testato.

---

# EPIC 2 — Collegamento repository e baseline

## TODO-0201 — Registrare un repository locale

**Riferimenti:** FL-04
**Priorità:** P0
**Dipende da:** TODO-0103
**Stato:** TODO

Verificare:

- percorso esistente;
- presenza repository Git;
- branch;
- remote;
- commit corrente;
- permessi di lettura.

**Done quando:**

- repository valido registrato;
- repository non valido rifiutato con errore chiaro;
- nessuna modifica prodotta dal controllo.

---

## TODO-0202 — Implementare Git Inspector read-only

**Riferimenti:** FL-02, FL-07, FL-10, FL-11, FL-12
**Priorità:** P0
**Dipende da:** TODO-0201
**Stato:** TODO

Funzioni:

- status;
- branch;
- remote;
- commit HEAD;
- diff;
- file modificati;
- file non tracciati;
- file rinominati;
- verifica commit sul remoto.

**Done quando:**

- output strutturato;
- errori Git gestiti;
- test su repository fixture.

---

## TODO-0203 — Acquisire baseline iniziale

**Riferimenti:** FL-05, FL-05.1
**Priorità:** P0
**Dipende da:** TODO-0202
**Stato:** TODO

Registrare:

- commit;
- branch;
- working tree;
- fingerprint;
- documenti registrati;
- approvatore;
- timestamp.

**Done quando:**

- baseline salvata;
- baseline riapribile;
- modifiche successive distinguibili.

---

## TODO-0204 — Rilevare divergenze dalla baseline

**Riferimenti:** FL-05.1, FL-13, FL-17
**Priorità:** P1
**Dipende da:** TODO-0203
**Stato:** TODO

Classificare:

- autorizzata;
- non associata;
- esterna;
- governata;
- potenziale divergenza.

**Done quando:**

- ogni modifica rilevata riceve una classificazione;
- nessuna divergenza viene assorbita silenziosamente.

---

# EPIC 3 — Task contract e lifecycle

## TODO-0301 — Definire modello Task Contract

**Riferimenti:** FL-06, FL-06.1, FL-19
**Priorità:** P0
**Dipende da:** TODO-0101
**Stato:** TODO

Campi minimi:

- obiettivo;
- scope;
- test;
- output;
- commit/push;
- tentativi;
- criteri di accettazione;
- dipendenze.

**Done quando:**

- validazione campi;
- errori leggibili;
- serializzazione persistente.

---

## TODO-0302 — Implementare macchina a stati

**Riferimenti:** FL-03.2, FL-19
**Priorità:** P0
**Dipende da:** TODO-0301
**Stato:** TODO

Impedire transizioni non valide.

**Done quando:**

- `COMPLETED` non impostabile dall’esecutore;
- stati laterali supportati;
- transizioni registrate come eventi;
- test completi della state machine.

---

## TODO-0303 — Implementare dipendenze tra task

**Riferimenti:** FL-06, FL-12, FL-13
**Priorità:** P1
**Dipende da:** TODO-0302
**Stato:** TODO

**Done quando:**

- task bloccata se prerequisito non valido;
- dipendenze circolari rifiutate;
- stato di blocco spiegato.

---

## TODO-0304 — Generare pacchetto esecutivo

**Riferimenti:** FL-06.2, FL-08
**Priorità:** P0
**Dipende da:** TODO-0301
**Stato:** TODO

Generare documento temporaneo con:

- obiettivo;
- contesto;
- scope;
- test;
- report;
- tentativi;
- stop conditions.

**Done quando:**

- pacchetto esportabile/copiabile;
- metodo proprietario non esposto integralmente;
- versione e task_id presenti.

---

# EPIC 4 — Snapshot ed esecuzione

## TODO-0401 — Snapshot pre-esecuzione

**Riferimenti:** FL-07
**Priorità:** P0
**Dipende da:** TODO-0202, TODO-0302
**Stato:** TODO

**Done quando:**

- stato Git registrato prima del tentativo;
- anomalie rilevate;
- snapshot collegato a task e tentativo.

---

## TODO-0402 — Gestire tentativi

**Riferimenti:** FL-03.2, FL-08
**Priorità:** P0
**Dipende da:** TODO-0302
**Stato:** TODO

**Done quando:**

- tentativi numerati;
- massimo configurabile;
- quarto tentativo bloccato se massimo 3;
- report diagnostico richiesto dopo fallimento finale.

---

## TODO-0403 — Registrare esecuzione esterna manuale

**Riferimenti:** FL-08
**Priorità:** P0
**Dipende da:** TODO-0401, TODO-0402
**Stato:** TODO

Registrare:

- esecutore;
- sessione;
- inizio;
- fine;
- pacchetto usato;
- tentativo.

**Done quando:**

- il sistema non dipende dal provider;
- esecuzione manuale tracciata.

---

# EPIC 5 — Report ed evidenze

## TODO-0501 — Definire schema report obbligatorio

**Riferimenti:** FL-03.3, FL-09, FL-09.1
**Priorità:** P0
**Dipende da:** TODO-0301
**Stato:** TODO

**Done quando:**

- schema versionato;
- campi obbligatori per tipo di task;
- validazione;
- supporto report incompleto.

---

## TODO-0502 — Importare report testuale

**Riferimenti:** FL-09
**Priorità:** P0
**Dipende da:** TODO-0501
**Stato:** TODO

Nell’MVP:

- incolla testo;
- conserva originale;
- compilazione manuale assistita dei campi;
- parser semplice e deterministico.

**Done quando:**

- report originale immutabile;
- campi estratti modificabili con audit;
- campi mancanti segnalati.

---

## TODO-0503 — Raccogliere evidenze Git post-esecuzione

**Riferimenti:** FL-10
**Priorità:** P0
**Dipende da:** TODO-0202, TODO-0401
**Stato:** TODO

**Done quando:**

- diff rispetto allo snapshot;
- file reali;
- commit;
- push;
- working tree;
- evidenze persistite.

---

## TODO-0504 — Controlled Process Runner

**Riferimenti:** FL-08.1, FL-10, FL-12
**Priorità:** P0
**Dipende da:** TODO-0003
**Stato:** TODO

Supportare solo operazioni autorizzate:

- test configurati;
- ricerche;
- Git read-only;
- comandi di verifica.

**Done quando:**

- nessuna shell generica;
- timeout;
- cwd controllata;
- stdout/stderr;
- codice di uscita;
- audit completo.

---

## TODO-0505 — Ricerca globale configurata

**Riferimenti:** FL-02, FL-10, FL-13
**Priorità:** P0
**Dipende da:** TODO-0504
**Stato:** TODO

**Done quando:**

- pattern configurabili;
- include/exclude;
- risultati con file e riga;
- scope di ricerca registrato;
- riferimento residuo rilevabile fuori write scope.

---

# EPIC 6 — Riconciliazione e verifica

## TODO-0601 — Reconciliation Engine

**Riferimenti:** FL-11, FL-11.1
**Priorità:** P0
**Dipende da:** TODO-0502, TODO-0503
**Stato:** TODO

Confrontare:

- file;
- test;
- comandi;
- commit;
- push;
- riferimenti;
- output.

**Done quando:**

- esiti MATCH/PARTIAL_MATCH/MISMATCH/NOT_VERIFIABLE/MISSING_EVIDENCE;
- discrepanze spiegate;
- risultati persistiti.

---

## TODO-0602 — Verification Engine tecnico

**Riferimenti:** FL-12
**Priorità:** P0
**Dipende da:** TODO-0601, TODO-0504, TODO-0505
**Stato:** TODO

**Done quando:**

- policy obbligatorie applicate;
- task bloccata su errore;
- nessun uso IA;
- report di verifica generato.

---

## TODO-0603 — Verifica macroscopica deterministica

**Riferimenti:** FL-13
**Priorità:** P0
**Dipende da:** TODO-0602
**Stato:** TODO

Controllare:

- repository oltre write scope;
- documenti registrati;
- riferimenti residui;
- file fuori scope;
- aggiornamenti documentali;
- bug bloccanti;
- milestone.

**Done quando:**

- finding fuori scope registrato;
- successo locale distinto da completamento globale;
- decisione umana richiesta.

---

## TODO-0604 — Verifica della verifica

**Riferimenti:** FL-14
**Priorità:** P0
**Dipende da:** TODO-0602, TODO-0603
**Stato:** TODO

**Done quando:**

- controlli mancanti rilevati;
- scope incompleto rilevato;
- evidenze obsolete rifiutate;
- verifica positiva impossibile se incompleta.

---

# EPIC 7 — Collaudo, approvazione e chiusura

## TODO-0701 — Registrare collaudo manuale

**Riferimenti:** FL-15
**Priorità:** P1
**Dipende da:** TODO-0302
**Stato:** TODO

**Done quando:**

- procedura e risultati registrabili;
- bug creabile dal collaudo;
- esito collegato alla task.

---

## TODO-0702 — Approvazione umana

**Riferimenti:** FL-16
**Priorità:** P0
**Dipende da:** TODO-0604
**Stato:** TODO

**Done quando:**

- utente vede evidenze e discrepanze;
- approvazione firmata logicamente con utente e timestamp;
- chiusura impedita senza condizioni richieste.

---

## TODO-0703 — Gestire deroghe

**Riferimenti:** FL-16.1
**Priorità:** P1
**Dipende da:** TODO-0702
**Stato:** TODO

**Done quando:**

- motivo obbligatorio;
- approvatore;
- scadenza;
- rischio;
- task correttiva;
- deroga visibile nello stato finale.

---

## TODO-0704 — Chiudere task e registrare evento

**Riferimenti:** FL-16, FL-19
**Priorità:** P0
**Dipende da:** TODO-0702
**Stato:** TODO

**Done quando:**

- task chiusa solo da transizione valida;
- evento immutabile;
- commit/evidenze collegate;
- stato persistente dopo riavvio.

---

## TODO-0705 — Aggiornare baseline

**Riferimenti:** FL-17
**Priorità:** P1
**Dipende da:** TODO-0704
**Stato:** TODO

**Done quando:**

- nuova baseline proposta;
- approvazione umana;
- baseline precedente conservata;
- hash e commit registrati.

---

# EPIC 8 — Bug memory

## TODO-0801 — Modello Bug

**Riferimenti:** FL-18
**Priorità:** P1
**Dipende da:** TODO-0101
**Stato:** TODO

**Done quando:**

- bug collegabile a task, commit, requisito e collaudo;
- origine incerta rappresentabile;
- stato e severità.

---

## TODO-0802 — Creare bug da verifica o collaudo

**Riferimenti:** FL-13, FL-15, FL-18
**Priorità:** P1
**Dipende da:** TODO-0801, TODO-0603
**Stato:** TODO

**Done quando:**

- finding convertibile in bug;
- task storica non riscritta;
- task correttiva creabile.

---

## TODO-0803 — Registrare test di regressione

**Riferimenti:** FL-18
**Priorità:** P2
**Dipende da:** TODO-0802
**Stato:** TODO

**Done quando:**

- bug collegato al test;
- assenza del test segnalabile;
- protezione futura visibile.

---

# EPIC 9 — Interfaccia MVP

## TODO-0901 — Dashboard progetti

**Riferimenti:** FL-04, FL-04.2
**Priorità:** P0
**Dipende da:** TODO-0103
**Stato:** TODO

Mostrare:

- progetti;
- repository;
- stato;
- ultima apertura;
- disponibilità.

---

## TODO-0902 — Vista progetto

**Riferimenti:** FL-05, FL-19, FL-20
**Priorità:** P0
**Dipende da:** TODO-0203
**Stato:** TODO

Mostrare:

- baseline;
- task;
- stato repository;
- anomalie;
- prossima azione consentita.

---

## TODO-0903 — Editor Task Contract

**Riferimenti:** FL-06
**Priorità:** P0
**Dipende da:** TODO-0301
**Stato:** TODO

**Done quando:**

- campi strutturati;
- scope;
- test;
- commit/push;
- criteri;
- validazione.

---

## TODO-0904 — Vista esecuzione e report

**Riferimenti:** FL-08, FL-09, FL-10
**Priorità:** P0
**Dipende da:** TODO-0403, TODO-0502, TODO-0503
**Stato:** TODO

---

## TODO-0905 — Vista riconciliazione

**Riferimenti:** FL-11, FL-12, FL-13, FL-14
**Priorità:** P0
**Dipende da:** TODO-0604
**Stato:** TODO

Mostrare chiaramente:

- dichiarato;
- osservato;
- discrepanza;
- blocco;
- controllo non eseguito.

---

## TODO-0906 — Vista approvazione

**Riferimenti:** FL-15, FL-16, FL-16.1
**Priorità:** P0
**Dipende da:** TODO-0702
**Stato:** TODO

---

# EPIC 10 — Collaudo del vertical slice

## TODO-1001 — Preparare repository fixture

**Riferimenti:** FL-20.1
**Priorità:** P0
**Dipende da:** TODO-0202
**Stato:** TODO

Preparare scenari ripetibili:

- file non dichiarato;
- test non eseguito;
- commit assente;
- push assente;
- riferimento residuo;
- tutto corretto.

---

## TODO-1002 — Test end-to-end senza IA

**Riferimenti:** FL-02, FL-20, FL-20.1
**Priorità:** P0
**Dipende da:** TODO-0906, TODO-1001
**Stato:** TODO

**Done quando:**

- tutti i dieci criteri FL-20.1 verificati;
- nessuna API IA usata;
- dati persistono dopo riavvio;
- task non chiudibile in caso di mismatch.

---

## TODO-1003 — Collaudo su Tennis Decision UI

**Riferimenti:** FL-03, FL-20, FL-24
**Priorità:** P0
**Dipende da:** TODO-1002
**Stato:** TODO

Usare una task reale o simulata del progetto per verificare:

- report incompleto;
- `fileModificati` mancante;
- commit/push;
- riferimenti residui fuori scope;
- verifica della verifica.

**Done quando:**

- problemi reali rilevati;
- limiti documentati;
- decisione sulla fase successiva.

---

# EPIC 11 — Modalità di esecuzione e funzioni future

## TODO-1101 — Definire interfaccia comune ExecutionMode

**Riferimenti:** FL-08, FL-21, `Project_Integrity_OS_Modalita_Esecuzione_v0_1.md`
**Priorità:** P1 — dopo la prima base operativa
**Stato:** TODO

Definire un contratto indipendente dal provider per:

- capacità disponibili;
- Task Contract in ingresso;
- risultato normalizzato;
- evidenze;
- tentativi;
- errori;
- stato dell’esecuzione.

---

## TODO-1102 — Implementare Browser Operator Adapter

**Riferimenti:** FL-08, FL-09, FL-10, `Project_Integrity_OS_Modalita_Esecuzione_v0_1.md`
**Priorità:** P1 — dopo la prima base operativa
**Dipende da:** TODO-1101
**Stato:** TODO

Supportare:

- generazione del pacchetto per chat browser;
- guida a checkpoint;
- importazione output manuali;
- distinzione tra dichiarato e osservato;
- evidenze fornite dall’operatore;
- report normalizzato.

---

## TODO-1103 — Implementare Desktop/Local Adapter

**Riferimenti:** FL-08, FL-10, FL-21, `Project_Integrity_OS_Modalita_Esecuzione_v0_1.md`
**Priorità:** P1 — dopo la prima base operativa
**Dipende da:** TODO-1101
**Stato:** TODO

Supportare capacità locali effettivamente autorizzate:

- lettura file;
- modifica file;
- comandi controllati;
- osservazione output;
- ispezione Git;
- raccolta diretta delle evidenze.

---

## TODO-1104 — Implementare Orchestrator/API Adapter

**Riferimenti:** FL-02.1, FL-08, FL-23, `Project_Integrity_OS_Modalita_Esecuzione_v0_1.md`
**Priorità:** DEFERRED
**Dipende da:** TODO-1101
**Stato:** TODO

Integrare orchestratori e modelli tramite API senza spostare nel provider la fonte di verità del progetto.

---

## TODO-1105 — Analisi semantica con IA

**Riferimenti:** FL-02.1, FL-13, FL-14
**Priorità:** DEFERRED
**Stato:** TODO

---

## TODO-1106 — PostgreSQL/Supabase adapter

**Riferimenti:** FL-04.1, FL-23
**Priorità:** DEFERRED
**Stato:** TODO

---

## TODO-1107 — Collaborazione cloud

**Riferimenti:** FL-23
**Priorità:** DEFERRED
**Stato:** TODO

---

# Ordine operativo raccomandato

```text
TODO-0001
→ TODO-0002
→ TODO-0003
→ TODO-0101
→ TODO-0102
→ TODO-0103
→ TODO-0201
→ TODO-0202
→ TODO-0203
→ TODO-0301
→ TODO-0302
→ TODO-0304
→ TODO-0401
→ TODO-0402
→ TODO-0403
→ TODO-0501
→ TODO-0502
→ TODO-0503
→ TODO-0504
→ TODO-0505
→ TODO-0601
→ TODO-0602
→ TODO-0603
→ TODO-0604
→ TODO-0702
→ TODO-0704
→ TODO-0901 ... TODO-0906
→ TODO-1001
→ TODO-1002
→ TODO-1003
```

Le attività P1 e P2 vengono inserite dopo la prima dimostrazione end-to-end, salvo che emergano come prerequisiti reali durante lo sviluppo.


---

## Registro avanzamento

### TODO-0001 — Completata

- flussi approvati;
- perimetro deterministic-first congelato;
- funzioni IA escluse dal primo vertical slice;
- criteri FL-20.1 confermati;
- TODO-0002 autorizzata.

### TODO-0101 — In analisi

- consolidamento decisionale completato e integrato in `main`;
- venti decisioni e nove correzioni registrate;
- audit documentale globale eseguito;
- implementazione SQLite ancora bloccata;
- prossimo passo: produrre Schema Architecture e gli altri deliverable finali.

### Decisione modalità di esecuzione — Registrata

- definite tre modalità: browser con operatore, desktop/local-enabled, orchestratore/API;
- selezionata `BROWSER_OPERATOR_ASSISTED` per TODO-0002;
- il prompt desktop precedente resta una variante futura;
- le modalità condividono Task Contract, evidenze, verifiche e macchina a stati;
- l’adapter browser verrà implementato nel prodotto dopo la prima base operativa.
