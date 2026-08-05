# Project Integrity OS
## Brief esecutivo — TODO-0002
### Creare la struttura iniziale Tauri 2

**Ruolo della chat:** esecutore tecnico.  
**Documento funzionale autorevole:** `Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md`.  
**To-Do autorevole:** `Project_Integrity_OS_TODO_MVP_v0_2.md`.  
**Percorso previsto:** `C:\Users\Utente\Desktop\Project Integrity OS`.  
**Tentativi massimi:** 3 tentativi ragionati, poi stop e report diagnostico.

---

## 1. Obiettivo

Creare lo scheletro iniziale avviabile di Project Integrity OS usando:

- Tauri 2;
- React;
- TypeScript;
- Vite;
- core applicativo Rust;
- prima destinazione Windows.

La task deve produrre soltanto la fondazione tecnica. Non deve ancora implementare SQLite, Git Inspector, task lifecycle o logica di verifica.

---

## 2. Vincoli architetturali

1. Il frontend React non deve contenere logica di dominio.
2. L’accesso al sistema operativo deve passare dal core Rust.
3. Il frontend deve comunicare con Rust tramite un comando Tauri minimo e tipizzato.
4. Non installare plugin non necessari alla task.
5. Non introdurre API IA, orchestratori o dipendenze cloud.
6. Non creare un terminale generico nell’applicazione.
7. Non implementare commit o push automatici.
8. Non aggiungere SQLite in questa task: è oggetto di TODO-0102.
9. La struttura deve essere predisposta per moduli Rust separati, senza anticiparne implementazioni.
10. Non modificare o riscrivere la specifica funzionale congelata.

---

## 3. Pre-flight obbligatorio

Prima di creare il progetto, verificare e riportare:

- sistema operativo e shell usata;
- versione di Node.js;
- versione di npm;
- versione di Rust (`rustc`);
- versione di Cargo;
- disponibilità dei prerequisiti Windows richiesti da Tauri;
- esistenza o meno della cartella di destinazione.

In caso di prerequisito mancante:

- non improvvisare installazioni invasive;
- non proseguire con una struttura parziale spacciata per completa;
- indicare con precisione ciò che manca e la procedura necessaria;
- non usare comandi che chiudano o terminino la shell dell’utente.

---

## 4. Creazione del progetto

Usare lo scaffold ufficiale Tauri 2 con template React + TypeScript e package manager npm.

Nome applicazione visibile:

```text
Project Integrity OS
```

Nome tecnico/cartella:

```text
project-integrity-os
```

Bundle identifier provvisorio:

```text
com.projectintegrity.os
```

La cartella finale dell’applicazione deve trovarsi in:

```text
C:\Users\Utente\Desktop\Project Integrity OS
```

Se lo scaffold crea una cartella tecnica intermedia, sistemare la struttura senza perdere file e senza annidamenti inutili.

---

## 5. Struttura minima richiesta

La struttura deve distinguere chiaramente:

```text
Project Integrity OS/
├── src/                         # frontend React/TypeScript
├── src-tauri/                   # core Tauri/Rust
├── docs/
│   ├── Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md
│   └── Project_Integrity_OS_TODO_MVP_v0_2.md
├── package.json
├── tsconfig*.json
├── vite.config.*
└── README.md
```

Dentro `src-tauri/src/`, predisporre senza sovra-ingegnerizzare:

```text
src-tauri/src/
├── main.rs
├── lib.rs                       # se previsto dallo scaffold corrente
└── app/
    └── mod.rs
```

È accettabile adattare questa struttura alle convenzioni reali dello scaffold Tauri 2, purché:

- l’avvio rimanga quello ufficiale;
- esista un punto chiaro per il futuro core applicativo;
- non si creino moduli vuoti inutili in grande quantità.

---

## 6. Comunicazione frontend ↔ Rust

Implementare un solo comando dimostrativo, per esempio:

```text
get_app_info
```

Deve restituire dati strutturati, non una stringa generica, con almeno:

- nome applicazione;
- versione;
- stato del core;
- modalità operativa iniziale, per esempio `deterministic-first`.

Il frontend deve:

- invocare il comando;
- mostrare il risultato;
- gestire lo stato di caricamento;
- mostrare un errore leggibile se l’invocazione fallisce.

Non aggiungere una vera dashboard: basta una schermata iniziale sobria che dimostri il collegamento.

---

## 7. README iniziale

Il README deve contenere soltanto informazioni concrete:

- scopo tecnico dello scaffold;
- stack;
- prerequisiti;
- comandi di sviluppo;
- struttura essenziale;
- stato corrente: TODO-0002;
- elementi esplicitamente non ancora implementati.

Non descrivere come già funzionanti database, Git Inspector, verifiche o orchestrazione.

---

## 8. Verifiche obbligatorie

Eseguire, secondo i comandi disponibili nello scaffold:

1. installazione dipendenze;
2. controllo TypeScript/build frontend;
3. formattazione o controllo Rust appropriato;
4. `cargo check` sul core Tauri;
5. avvio in modalità sviluppo;
6. verifica che la finestra si apra;
7. verifica che il frontend riceva i dati dal comando Rust.

Se l’ambiente non permette una verifica visiva automatica, dichiararlo espressamente e fornire le evidenze disponibili senza inventare il risultato.

Non costruire ancora installer MSI/NSIS.

---

## 9. Git

Per questa task:

- inizializzare Git solo se il progetto non è già in un repository;
- non eseguire push senza autorizzazione esplicita dell’utente;
- non dichiarare un push se non è stato realmente verificato;
- se viene creato un commit, riportarne hash, branch e stato del working tree;
- se non viene creato un commit, dichiararlo chiaramente nel report.

---

## 10. Criteri di accettazione

TODO-0002 può essere proposta come completata solo se:

- lo scaffold Tauri 2 esiste nel percorso previsto;
- React + TypeScript + Vite sono configurati;
- il core Rust compila con `cargo check`;
- il frontend supera il controllo/build previsto;
- `npm run tauri dev` viene avviato con successo, salvo limite ambientale documentato;
- il comando frontend ↔ Rust restituisce dati strutturati;
- la UI gestisce caricamento ed errore;
- i due documenti approvati sono presenti in `docs/`;
- il README non dichiara funzioni inesistenti;
- non sono state introdotte funzioni fuori scope.

---

## 11. Regola dei tre tentativi

Sono consentiti massimo tre tentativi ragionati.

Un tentativo è una sequenza coerente di diagnosi, correzione e nuova verifica. Non contare come tentativi separati semplici comandi di ispezione.

Dopo il terzo tentativo fallito:

- fermarsi;
- non continuare a modificare file;
- produrre il report diagnostico completo;
- indicare il blocco reale e ciò che resta non verificato.

---

## 12. Report finale obbligatorio

Restituire esattamente queste sezioni:

```text
Esito:
Tentativi eseguiti:

Prerequisiti verificati:

File e cartelle creati:

File modificati:

Comandi eseguiti:

Esito completo dei controlli e test:

Verifica avvio Tauri:

Verifica comunicazione frontend-Rust:

Git:
- repository inizializzato:
- branch:
- commit creato:
- hash commit:
- push eseguito:
- working tree finale:

Funzioni volutamente non implementate:

Limiti e parti non verificate:

Conferma assenza di modifiche fuori scope:
```

Non omettere sezioni. Usare `nessuno` o `non eseguito` quando appropriato.
