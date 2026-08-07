# Project Integrity OS

## Brief esecutivo — TODO-0002

> **Nome documentale normalizzato.** L’artefatto originale, con il nome usato durante l’esecuzione, è conservato nel pacchetto, sotto `preserved-originals/20-history/original-artifacts/legacy-names/`.


### Creare la struttura iniziale Tauri 2

**Versione del brief:** v0.2
**Stato:** CORRENTE
**Data revisione:** 2026-08-05
**Task:** TODO-0002
**Modalità di esecuzione:** `BROWSER_OPERATOR_ASSISTED`
**Ruolo della chat:** guida esecutiva tecnica con operatore umano
**Percorso previsto:** `C:\Users\Utente\Desktop\Project Integrity OS`
**Tentativi massimi:** 3 tentativi ragionati, poi stop e report diagnostico

---

# 1. Documenti autorevoli

L’esecuzione deve rispettare i seguenti documenti:

1. `Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md`
2. `Project_Integrity_OS_TODO_MVP_v0_4.md`
3. `Project_Integrity_OS_Brief_TODO-0002_v0_2_SUPERSEDED.md`
4. `Project_Integrity_OS_Modalita_Esecuzione_v0_1.md`
5. `Project_Integrity_OS_Prompt_Esecutivo_Browser_TODO-0002_v0_1_FINAL.md`

Gerarchia da applicare in caso di dubbio o apparente conflitto:

1. la specifica FROZEN governa obiettivi, vincoli funzionali e non-obiettivi;
2. la To-Do v0.4 governa stato, dipendenze, priorità e ordine operativo;
3. questo brief governa scope tecnico, output e criteri di accettazione di TODO-0002;
4. il documento sulle modalità governa il modello operativo;
5. il prompt browser governa l’interazione a checkpoint con l’utente.

La specifica FROZEN non deve essere modificata durante TODO-0002.

Le versioni precedenti dei documenti possono essere conservate come storico, ma non devono essere trattate come fonti operative correnti.

---

# 2. Stato della task

TODO-0002 dipende da:

```text
TODO-0001 — Congelare la specifica del vertical slice
```

La dipendenza è soddisfatta.

Stato corrente:

```text
IN_PROGRESS
```

Modalità selezionata:

```text
BROWSER_OPERATOR_ASSISTED
```

In questa modalità:

* la chat non opera direttamente sul computer;
* l’utente esegue materialmente comandi e modifiche;
* la chat guida un passaggio per volta;
* ogni risultato viene valutato soltanto attraverso evidenze restituite dall’utente;
* dichiarazioni, output osservati e conferme manuali devono restare distinti.

---

# 3. Obiettivo

Creare lo scheletro iniziale avviabile di Project Integrity OS usando:

* Tauri 2;
* React;
* TypeScript;
* Vite;
* core applicativo Rust;
* prima destinazione Windows.

La task deve produrre soltanto la fondazione tecnica necessaria alle task successive.

Il risultato deve dimostrare:

1. che l’applicazione desktop può essere avviata in sviluppo;
2. che il frontend React viene caricato nella finestra Tauri;
3. che il frontend comunica con un comando Rust minimo e tipizzato;
4. che la struttura iniziale è pronta ad accogliere futuri moduli Rust senza implementarli anticipatamente;
5. che il repository contiene documentazione coerente con lo stato reale.

---

# 4. Funzioni fuori scope

TODO-0002 non deve implementare:

* SQLite;
* database per progetto;
* registro globale;
* Git Inspector;
* Repository Observer;
* baseline;
* Task Contract;
* task lifecycle;
* macchina a stati;
* snapshot;
* report parser;
* Evidence Collector;
* Reconciliation Engine;
* Verification Engine;
* Policy Engine;
* Controlled Process Runner;
* orchestratori;
* adapter delle modalità di esecuzione;
* API di modelli IA;
* analisi semantica automatica;
* funzioni cloud;
* collaborazione multiutente;
* commit automatici;
* push automatici;
* terminale generico;
* installer MSI o NSIS;
* TODO-0003 o task successive.

Non devono essere create implementazioni segnaposto che fingano il funzionamento di questi componenti.

Sono ammessi soltanto punti strutturali minimi necessari a predisporre il futuro core Rust.

---

# 5. Vincoli architetturali

1. Il frontend React non deve contenere logica di dominio.

2. L’accesso al sistema operativo deve passare dal core Rust.

3. Il frontend deve comunicare con Rust attraverso un comando Tauri minimo e tipizzato.

4. Non devono essere installati plugin Tauri non necessari alla task.

5. Non devono essere introdotte API IA, dipendenze cloud o orchestratori.

6. Non deve essere creato un terminale generico nell’applicazione.

7. Non devono essere implementati commit o push automatici.

8. SQLite non deve essere aggiunto in questa task.

9. La struttura Rust deve essere predisposta per moduli separati senza anticiparne le implementazioni.

10. Non devono essere creati numerosi moduli vuoti per rappresentare componenti futuri.

11. Il frontend non deve accedere direttamente al filesystem, al database o al sistema operativo.

12. La specifica funzionale congelata non deve essere modificata o riscritta.

13. Il README non deve descrivere come operative funzioni non ancora implementate.

14. L’applicazione deve restare aderente allo scaffold ufficiale Tauri 2.

---

# 6. Percorso di destinazione

La cartella finale dell’applicazione deve trovarsi in:

```text
C:\Users\Utente\Desktop\Project Integrity OS
```

Non deve essere presunto che la cartella:

* esista;
* sia vuota;
* sia già un repository Git;
* contenga materiale eliminabile.

Prima della creazione dello scaffold deve essere eseguito un controllo esplicito.

Se la cartella contiene materiale non riconosciuto:

* non sovrascrivere;
* non cancellare;
* non spostare automaticamente;
* elencare ciò che risulta presente;
* fermare i passaggi dipendenti;
* richiedere una decisione esplicita dell’utente.

Non eliminare la cartella per “ripartire da zero” senza autorizzazione esplicita.

---

# 7. Pre-flight obbligatorio

Prima di creare o modificare il progetto, verificare e riportare:

* versione di Windows;
* shell utilizzata;
* versione di Node.js;
* versione di npm;
* versione di Rust tramite `rustc`;
* versione di Cargo;
* disponibilità dei prerequisiti Windows richiesti da Tauri;
* disponibilità del compilatore Microsoft richiesto;
* disponibilità di WebView2, quando applicabile;
* esistenza della cartella di destinazione;
* contenuto della cartella di destinazione;
* eventuale presenza di un repository Git;
* eventuali file o cartelle preesistenti.

Non proseguire se manca un prerequisito indispensabile.

In caso di prerequisito mancante:

* non improvvisare installazioni invasive;
* non creare uno scaffold parziale presentandolo come completo;
* indicare chiaramente ciò che manca;
* indicare la procedura necessaria;
* attendere una decisione dell’utente prima di installazioni o modifiche di sistema.

---

# 8. Sicurezza dei comandi

Nei comandi destinati al terminale dell’utente non usare:

* `exit`;
* `exit 1`;
* `logout`;
* `kill $$`;
* `exec`;
* comandi equivalenti che possano chiudere la shell o terminare la sessione.

In caso di controllo fallito:

* mostrare chiaramente l’errore;
* non nascondere stderr;
* non chiudere la shell;
* non presentare il controllo come riuscito;
* impedire l’esecuzione dei passaggi dipendenti;
* usare verifiche non terminanti o catene sicure.

Non utilizzare comandi distruttivi o ricorsivi senza necessità, spiegazione e autorizzazione esplicita.

---

# 9. Creazione dello scaffold

Utilizzare lo scaffold ufficiale Tauri 2 con:

```text
Frontend: React
Linguaggio frontend: TypeScript
Build tool: Vite
Package manager: npm
Core: Rust
```

Nome visibile dell’applicazione:

```text
Project Integrity OS
```

Nome tecnico:

```text
project-integrity-os
```

Bundle identifier:

```text
com.projectintegrity.os
```

La struttura finale non deve contenere annidamenti inutili come:

```text
Project Integrity OS/
└── project-integrity-os/
```

Se lo scaffold crea una cartella tecnica intermedia, la struttura deve essere sistemata senza perdere file e senza sovrascrivere materiale preesistente.

L’avvio e la configurazione devono restare compatibili con le convenzioni reali dello scaffold Tauri 2 installato.

---

# 10. Struttura minima richiesta

La struttura finale deve distinguere chiaramente frontend, core Rust e documentazione.

Struttura minima indicativa:

```text
Project Integrity OS/
├── src/
├── src-tauri/
├── docs/
│   ├── Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md
│   ├── Project_Integrity_OS_TODO_MVP_v0_4.md
│   ├── Project_Integrity_OS_Brief_TODO-0002_v0_2_SUPERSEDED.md
│   ├── Project_Integrity_OS_Modalita_Esecuzione_v0_1.md
│   └── history/
│       └── Project_Integrity_OS_Brief_TODO-0002_PRECEDENTE.md
├── package.json
├── tsconfig*.json
├── vite.config.*
└── README.md
```

La cartella `history/` conserva documenti precedenti e non autorevoli.

I documenti correnti non devono essere collocati dentro `history/`.

Il prompt esecutivo browser può essere conservato nella documentazione operativa, ma non è un requisito tecnico per il funzionamento dello scaffold.

Dentro `src-tauri/src/` predisporre, senza sovra-ingegnerizzare:

```text
src-tauri/src/
├── main.rs
├── lib.rs
└── app/
    └── mod.rs
```

La struttura può essere adattata alle convenzioni effettive dello scaffold corrente, purché:

* l’avvio ufficiale resti funzionante;
* esista un punto chiaro per il futuro core applicativo;
* il comando dimostrativo non venga collocato nel frontend;
* non vengano creati moduli vuoti non necessari;
* non vengano anticipati componenti delle task successive.

Se lo scaffold corrente utilizza sia `main.rs` sia `lib.rs`, la registrazione dei comandi deve rispettare il flusso ufficiale generato.

---

# 11. Comando Rust minimo

Implementare un solo comando Tauri dimostrativo:

```text
get_app_info
```

Il comando deve:

* essere implementato nel core Rust;
* essere registrato correttamente nel builder Tauri;
* essere invocabile dal frontend;
* restituire una struttura serializzabile;
* non restituire una semplice stringa generica;
* non leggere database;
* non ispezionare repository;
* non accedere a servizi cloud;
* non contenere logica di dominio futura.

La risposta deve contenere almeno:

* nome dell’applicazione;
* versione dell’applicazione;
* stato del core;
* modalità operativa iniziale.

Valori semantici attesi:

```text
Nome applicazione: Project Integrity OS
Stato core: ready
Modalità: deterministic-first
```

La versione deve provenire da una fonte coerente con la configurazione reale del progetto e non essere duplicata inutilmente in più file quando può essere letta dalla configurazione applicativa.

Il tipo Rust restituito deve essere esplicito e serializzabile.

Il tipo TypeScript corrispondente deve rappresentare gli stessi campi.

---

# 12. Frontend iniziale

Il frontend deve invocare `get_app_info` tramite le API Tauri appropriate.

La schermata deve essere sobria e limitata alla dimostrazione del collegamento frontend-Rust.

Deve gestire chiaramente tre stati:

## 12.1 Caricamento

Durante l’invocazione deve essere mostrato uno stato di caricamento leggibile.

## 12.2 Risultato

Quando il comando restituisce correttamente i dati, la schermata deve mostrare almeno:

* nome dell’applicazione;
* versione;
* stato del core;
* modalità operativa.

## 12.3 Errore

Se l’invocazione fallisce, la schermata deve mostrare un errore leggibile.

L’errore non deve essere ignorato o lasciato soltanto nella console.

Non è richiesto provocare artificialmente un errore durante il collaudo, ma la relativa gestione deve essere presente e verificabile nel codice.

Il frontend non deve contenere:

* database mock;
* dati di task;
* repository simulati;
* verifiche simulate;
* dashboard operative;
* navigazione verso funzioni future;
* logica di dominio.

Sono consentiti soltanto componenti e stili necessari alla schermata iniziale.

---

# 13. README iniziale

Il README deve descrivere esclusivamente lo stato reale del repository.

Deve contenere almeno:

* scopo tecnico dello scaffold;
* stack utilizzato;
* prerequisiti;
* procedura di installazione delle dipendenze;
* comandi di sviluppo;
* comando di build o controllo frontend;
* comando di controllo Rust;
* comando di avvio Tauri;
* struttura essenziale;
* descrizione di `get_app_info`;
* stato corrente: TODO-0002;
* modalità di esecuzione utilizzata;
* funzioni esplicitamente non implementate.

Il README non deve dichiarare come già funzionanti:

* SQLite;
* registrazione progetti;
* Git Inspector;
* gestione task;
* snapshot;
* report;
* evidenze;
* riconciliazione;
* Verification Engine;
* orchestrazione;
* API IA;
* cloud;
* commit o push automatici.

---

# 14. Metodo di esecuzione

L’esecuzione deve procedere per checkpoint.

Per ogni checkpoint la chat deve:

1. indicare in una frase lo scopo;
2. fornire un solo blocco coerente di comandi oppure una sola modifica;
3. specificare il percorso completo dei file coinvolti;
4. fornire il contenuto completo quando un file deve essere creato o sostituito;
5. indicare quale output o contenuto deve essere restituito;
6. attendere la risposta dell’utente;
7. interpretare l’evidenza ricevuta;
8. distinguere dichiarazioni da output osservati;
9. passare al checkpoint successivo soltanto quando il precedente è sufficiente.

Non riversare l’intera procedura esecutiva in un unico messaggio.

Checkpoint previsti:

```text
A — Pre-flight
B — Scaffold
C — Documenti e struttura
D — Comando Rust
E — Frontend
F — README
G — Controlli e collaudo
H — Git
```

---

# 15. Evidenze richieste

Le evidenze utilizzabili comprendono:

* output completo del terminale;
* contenuto completo dei file;
* diff verificabile;
* elenco delle directory;
* output dei test;
* output di Git;
* hash;
* screenshot;
* conferma manuale esplicitamente identificata come tale.

La chat non deve dichiarare di aver:

* creato file;
* modificato file;
* eseguito comandi;
* verificato build;
* verificato test;
* aperto la finestra;
* verificato Git;
* verificato commit;
* verificato push;

senza un’evidenza ricevuta dall’utente.

Le formulazioni devono distinguere chiaramente:

```text
Dichiarato dall’utente
Osservato nell’output
Confermato manualmente
Non verificato
```

---

# 16. Verifiche obbligatorie

Eseguire separatamente, secondo i comandi disponibili nello scaffold:

1. installazione delle dipendenze;
2. controllo TypeScript o build frontend;
3. controllo della formattazione Rust appropriato;
4. controllo statico Rust appropriato;
5. `cargo check` sul core Tauri;
6. avvio tramite `npm run tauri dev`;
7. verifica dell’apertura della finestra;
8. verifica della comunicazione frontend-Rust;
9. controllo della presenza dei documenti obbligatori;
10. controllo del README;
11. controllo dell’assenza di funzioni fuori scope.

Gli output dei controlli devono essere conservati separatamente quando possibile.

Un controllo fallito non deve essere presentato come riuscito.

Non costruire installer MSI o NSIS.

---

# 17. Collaudo manuale

La verifica visuale deve essere registrata come conferma manuale dell’utente.

Richiedere la seguente risposta strutturata:

```text
Finestra aperta: sì/no
Nome mostrato:
Versione mostrata:
Stato core mostrato:
Modalità mostrata:
Errore visibile: sì/no
Problemi osservati:
```

La comunicazione frontend-Rust può essere considerata confermata manualmente soltanto se i dati mostrati corrispondono alla risposta strutturata di `get_app_info`.

Un output positivo di build non sostituisce il collaudo manuale della finestra quando questo è richiesto.

---

# 18. Git

Prima di inizializzare Git verificare se la cartella si trova già dentro un repository.

Politica della task:

```text
Inizializzazione Git: solo se necessario
Commit obbligatorio: no
Push obbligatorio: no
Push automatico: vietato
```

Git può essere inizializzato soltanto se:

* il progetto non è già in un repository;
* l’utente è informato;
* non vengono coinvolte cartelle superiori non previste.

Un eventuale commit richiede una decisione esplicita dell’utente.

Non eseguire push senza autorizzazione esplicita.

Se viene creato un commit, il report deve indicare:

* branch;
* hash;
* stato del working tree;
* file inclusi;
* eventuale remoto;
* eventuale push.

Se non viene creato un commit, il report deve dichiararlo chiaramente.

Se non viene eseguito un push, il report deve indicare:

```text
non eseguito
```

---

# 19. Regola dei tre tentativi

Sono consentiti massimo tre tentativi ragionati.

Un tentativo comprende:

1. diagnosi;
2. correzione coerente;
3. nuova verifica.

I semplici comandi di lettura o ispezione non costituiscono automaticamente un nuovo tentativo.

Ogni tentativo deve essere registrato mentalmente durante l’esecuzione e riportato nel report finale.

Dopo il terzo tentativo fallito:

* fermarsi;
* non continuare a modificare file;
* non proporre una quarta correzione;
* produrre il report diagnostico completo;
* identificare il blocco reale;
* indicare ciò che resta non verificato;
* classificare l’esito come fallito, bloccato o evidenza incompleta secondo le prove disponibili.

---

# 20. Criteri di accettazione

TODO-0002 può essere proposta per verifica indipendente soltanto se le evidenze mostrano che:

* lo scaffold Tauri 2 esiste nel percorso previsto;
* React è configurato;
* TypeScript è configurato;
* Vite è configurato;
* il core Rust è presente;
* il frontend supera il controllo o la build prevista;
* `cargo check` riesce;
* `npm run tauri dev` viene avviato con successo;
* la finestra desktop si apre;
* il frontend riceve dati strutturati da `get_app_info`;
* la UI mostra caricamento;
* la UI mostra il risultato;
* la UI contiene una gestione leggibile dell’errore;
* i documenti correnti sono presenti in `docs/`;
* le versioni storiche sono distinguibili dai documenti correnti;
* il README descrive lo stato reale;
* nessuna logica di dominio è presente nel frontend;
* non sono state introdotte funzioni fuori scope;
* lo stato Git è stato dichiarato e supportato dalle evidenze disponibili.

Se una prova obbligatoria manca, utilizzare:

```text
EVIDENZA INCOMPLETA
```

Non utilizzare la parola `successo` per convenienza.

La chat esecutiva non può impostare autonomamente TODO-0002 come `DONE`.

Può soltanto indicare se il risultato è proponibile per una verifica indipendente e una successiva approvazione umana.

---

# 21. Registro logico delle evidenze

Durante l’esecuzione mantenere un registro logico con:

```text
Checkpoint:
Comando o modifica richiesta:
Evidenza ricevuta:
Tipo di evidenza:
Esito:
Elementi non verificati:
Tentativo:
```

Nel report finale distinguere:

* dichiarazioni dell’utente;
* output osservati nella chat;
* conferme manuali;
* controlli non verificabili;
* parti non eseguite;
* discrepanze.

---

# 22. Report finale obbligatorio

Restituire esattamente le seguenti sezioni:

```text
Esito:
Modalità di esecuzione: BROWSER_OPERATOR_ASSISTED
Tentativi eseguiti:

Prerequisiti verificati:
- evidenza:
- elementi non verificati:

File e cartelle dichiarati creati:
- evidenza:

File dichiarati modificati:
- evidenza:

Comandi eseguiti dall’utente:
- output osservato:

Esito completo dei controlli e test:

Verifica avvio Tauri:
- tipo evidenza: output / conferma manuale / non verificato

Verifica comunicazione frontend-Rust:
- tipo evidenza: output / conferma manuale / non verificato

Git:
- repository inizializzato:
- branch:
- commit creato:
- hash commit:
- push eseguito:
- working tree finale:
- fonte delle informazioni:

Discrepanze tra dichiarazioni ed evidenze:

Funzioni volutamente non implementate:

Limiti e parti non verificate:

Conferma assenza di modifiche fuori scope:
- evidenza disponibile:

Conclusione:
- proponibile per verifica indipendente: sì/no
```

Non omettere sezioni.

Utilizzare, quando appropriato:

```text
nessuno
non eseguito
non osservato
non verificato
```

Dopo il report finale:

* fermarsi;
* non avviare TODO-0003;
* non modificare automaticamente lo stato della To-Do;
* attendere verifica indipendente e decisione umana.


---

# 23. Chiusura della task esecutiva

Il completamento tecnico locale di TODO-0002 non equivale automaticamente alla chiusura governata della task.

La chat può concludere soltanto uno dei seguenti esiti:

```text
PROCEDURA COMPLETATA — proponibile per verifica indipendente
EVIDENZA INCOMPLETA
BLOCKED
FAILED
```

La transizione finale a `DONE` richiede una successiva decisione di governance basata sulle evidenze raccolte.

TODO-0003 non deve essere avviata durante questa esecuzione.
