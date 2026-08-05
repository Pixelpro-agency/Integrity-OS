# Project Integrity OS
## Flussi funzionali del primo MVP — v0.1

**Stato:** bozza operativa approvabile  
**Ambito:** primo vertical slice locale, single-user, un repository per progetto  
**Principio guida:** deterministic-first; l’intelligenza artificiale viene introdotta solo dove i controlli logici, strutturali o tecnici non sono sufficienti.

---

## FL-01 — Obiettivo del primo MVP

Il primo MVP deve dimostrare un comportamento completo e verificabile:

> collegare un repository, creare una task strutturata, registrare lo stato prima dell’esecuzione, importare il report dell’esecutore, osservare lo stato reale del repository, confrontare dichiarazioni ed evidenze e impedire la chiusura della task quando i dati non concordano.

Il primo MVP non deve ancora:

- modificare automaticamente il codice;
- orchestrare autonomamente più agenti;
- usare obbligatoriamente API di modelli IA;
- decidere semanticamente se una soluzione architetturale è corretta;
- eseguire commit o push senza un’azione esplicita dell’utente;
- sostituire Git, il terminale o gli strumenti di sviluppo.

Il risultato atteso è una prima prova concreta del principio:

> una task non è completata perché un esecutore lo dichiara; è completata solo quando report, evidenze, controlli e approvazione concordano.

---

## FL-02 — Principio deterministic-first

Project Integrity OS deve preferire sempre controlli deterministici, ripetibili e verificabili.

Esempi di controlli deterministici:

- lettura dello stato Git;
- elenco reale dei file modificati;
- confronto tra file dichiarati e file osservati;
- verifica del branch corrente;
- verifica dell’esistenza di commit;
- verifica della presenza del commit sul remoto;
- esecuzione di test autorizzati;
- controllo di codice di uscita, stdout e stderr;
- ricerca globale di stringhe o riferimenti residui;
- verifica della presenza di file obbligatori;
- controllo del working tree;
- verifica dello scope di modifica;
- verifica della completezza formale del report;
- verifica del numero di tentativi;
- controllo delle dipendenze tra task;
- controllo della transizione di stato consentita.

L’IA deve essere esclusa da ogni controllo che può essere risolto in modo affidabile tramite funzioni, query, regole, parser, Git o comandi autorizzati.

### FL-02.1 — Uso futuro dell’IA

L’IA potrà essere aggiunta in un secondo momento per attività semanticamente complesse, per esempio:

- rilevare conflitti concettuali con decisioni precedenti;
- valutare se un requisito è soddisfatto solo formalmente ma non sostanzialmente;
- individuare documentazione semanticamente contraddittoria;
- proporre collegamenti tra un bug e task storiche;
- stimare aree di regressione non evidenti;
- valutare se il perimetro della verifica è insufficiente;
- preparare un riepilogo ragionato per la revisione umana.

Anche in questi casi, l’IA produrrà una valutazione o una proposta, non una verità incontestabile.

---

## FL-03 — Replicazione del metodo di lavoro attuale

Il metodo di lavoro usato per progettare Project Integrity OS deve diventare parte del prodotto.

Il flusso generale è:

1. ragionamento e definizione macroscopica;
2. decisione esplicita;
3. registrazione della decisione;
4. creazione di un documento di riferimento;
5. creazione o aggiornamento della To-Do;
6. preparazione di una task esecutiva circoscritta;
7. esecuzione separata;
8. report obbligatorio;
9. verifica indipendente;
10. verifica macroscopica;
11. collaudo umano;
12. aggiornamento dello stato e della documentazione;
13. passaggio alla task successiva solo dopo chiusura valida.

### FL-03.1 — Separazione dei ruoli

Il sistema deve distinguere almeno questi ruoli logici:

- **governance/amministratore:** mantiene obiettivi, decisioni, scope e stato complessivo;
- **esecutore:** svolge una task circoscritta;
- **verificatore tecnico:** controlla dichiarazioni ed evidenze;
- **verificatore macroscopico:** controlla coerenza rispetto al progetto;
- **approvatore umano:** autorizza chiusura, deroghe e nuove baseline.

Nell’MVP i ruoli possono essere svolti dalla stessa persona in momenti diversi, ma devono restare distinti nel modello.

### FL-03.2 — Regola dei tentativi

Ogni esecuzione deve registrare il numero di tentativi.

Regola iniziale:

- massimo tre tentativi ragionati;
- dopo il terzo fallimento, stop obbligatorio;
- produzione di un report diagnostico;
- nessuna prosecuzione automatica;
- passaggio allo stato `FAILED` o `BLOCKED`.

### FL-03.3 — Report obbligatorio

Per una task con modifiche, il report deve poter richiedere almeno:

- esito;
- numero di tentativi;
- file verificati;
- file modificati;
- comandi eseguiti;
- test eseguiti;
- risultato completo dei test;
- errori residui;
- limiti o parti non verificate;
- stato del commit;
- stato del push;
- impatto sulla documentazione.

Il report è una dichiarazione dell’esecutore e non costituisce prova sufficiente.

---

## FL-04 — Creazione e registrazione di un progetto

L’utente crea un progetto in Project Integrity OS e collega un repository locale.

Il sistema registra:

- `project_id` UUID;
- nome del progetto;
- percorso del repository;
- percorso del database SQLite dedicato;
- branch osservato;
- remote configurati;
- commit corrente;
- data di creazione;
- versione dello schema;
- stato di disponibilità del repository.

### FL-04.1 — Database per progetto

Ogni progetto usa un database SQLite separato.

Il database non viene normalmente salvato dentro il repository Git.

Struttura prevista:

```text
Project Integrity OS Data/
└── <project-id>/
    ├── project.sqlite
    ├── backups/
    ├── evidence/
    ├── exports/
    └── project-link.json
```

### FL-04.2 — Registro globale minimo

L’applicazione mantiene un piccolo registro globale contenente soltanto:

- `project_id`;
- nome;
- percorso del repository;
- percorso del database;
- ultima apertura;
- versione dello schema;
- stato sintetico.

Il registro globale non contiene task, bug, evidenze o storico operativo.

---

## FL-05 — Baseline iniziale

Prima di creare task operative, il sistema acquisisce una baseline iniziale.

La baseline comprende almeno:

- commit corrente;
- branch;
- stato del working tree;
- elenco dei file tracciati rilevanti;
- hash o fingerprint dei file governati;
- documenti di progetto registrati;
- To-Do importata o creata;
- stato dichiarato del progetto;
- data e approvatore della baseline.

La baseline iniziale non viene approvata automaticamente da un’IA.

### FL-05.1 — Modifiche successive alla baseline

Ogni cambiamento osservato viene classificato come:

- autorizzato da una task;
- non associato a una task;
- modifica esterna;
- modifica ai documenti governati;
- potenziale divergenza;
- modifica ignorabile secondo policy esplicita.

---

## FL-06 — Creazione della task strutturata

Una task non è solo testo libero. Deve essere registrata come contratto operativo.

Campi minimi:

- identificatore;
- titolo;
- obiettivo;
- motivazione;
- stato;
- dipendenze;
- file o aree modificabili;
- aree in sola lettura;
- aree escluse;
- ricerche globali obbligatorie;
- output obbligatori;
- test richiesti;
- commit richiesto: sì/no;
- push richiesto: sì/no;
- collaudo manuale richiesto: sì/no;
- tentativi massimi;
- criteri di accettazione;
- riferimenti a documenti, requisiti e decisioni.

### FL-06.1 — Scope separati

Il sistema deve distinguere:

- **write scope:** ciò che l’esecutore può modificare;
- **read scope:** ciò che può leggere;
- **verification scope:** ciò che il sistema deve controllare;
- **macro scope:** parti del progetto che possono essere influenzate dalla task.

Regola fondamentale:

> lo scope di verifica può e spesso deve essere più ampio dello scope di modifica.

### FL-06.2 — Pacchetto esecutivo

Il sistema genera un pacchetto temporaneo con solo ciò che serve all’esecutore:

- obiettivo;
- contesto pertinente;
- file modificabili;
- vincoli;
- test;
- output;
- massimo numero di tentativi;
- formato del report;
- condizioni di stop.

Il pacchetto non espone l’intero metodo proprietario.

---

## FL-07 — Snapshot pre-esecuzione

Prima dell’avvio della task, il sistema registra uno snapshot tecnico:

- commit iniziale;
- branch;
- working tree;
- file modificati già presenti;
- file non tracciati;
- timestamp;
- eventuali anomalie;
- task attiva;
- tentativo corrente.

Lo snapshot serve come riferimento per distinguere le modifiche prodotte dalla task da quelle già esistenti.

Se il repository non è in uno stato compatibile con l’esecuzione, il sistema deve bloccare o richiedere una decisione esplicita.

---

## FL-08 — Esecuzione esterna

Nell’MVP l’esecuzione può avvenire:

- manualmente;
- in una chat separata;
- con Codex, Claude Code o altro strumento;
- nel terminale dell’utente;
- tramite un futuro orchestratore.

Project Integrity OS non deve dipendere dall’esecutore scelto.

Il sistema registra:

- data e ora di inizio;
- tipo di esecutore;
- identificatore della sessione, se disponibile;
- tentativo;
- pacchetto di contesto consegnato;
- stato `IN_EXECUTION`.

### FL-08.1 — Controlled Process Runner

Il software può eseguire soltanto controlli e comandi autorizzati.

Ogni operazione deve specificare:

- programma;
- argomenti;
- directory di lavoro;
- timeout;
- variabili d’ambiente consentite;
- output atteso;
- categoria del comando;
- autorizzazione richiesta.

Non deve essere presente, nell’MVP, un terminale generico incontrollato.

---

## FL-09 — Importazione del report

Al termine dell’esecuzione, l’utente importa o incolla il report.

Il sistema:

1. conserva il report originale;
2. prova a estrarre i campi strutturati;
3. segnala campi mancanti;
4. non modifica automaticamente lo stato in `COMPLETED`;
5. porta la task in `EXECUTION_REPORTED` o `EVIDENCE_INCOMPLETE`.

### FL-09.1 — Report incompleto

Esempi di errori:

- manca l’elenco dei file modificati;
- manca il numero dei tentativi;
- mancano i comandi;
- sono citati test senza esito completo;
- il commit è richiesto ma non dichiarato;
- il push è richiesto ma non dichiarato;
- non sono indicate limitazioni.

Il report può essere accettato come input anche se incompleto, ma non come prova di completamento.

---

## FL-10 — Raccolta automatica delle evidenze

Dopo il report, il sistema osserva direttamente il repository e raccoglie evidenze:

- `git status`;
- diff rispetto allo snapshot iniziale;
- file realmente modificati;
- file aggiunti, eliminati o rinominati;
- branch;
- commit nuovi;
- commit associabile alla task;
- presenza del commit sul remoto;
- working tree;
- risultati di ricerche obbligatorie;
- file obbligatori presenti o mancanti;
- test eseguiti dal Controlled Process Runner;
- stdout, stderr, durata e codice di uscita.

Le evidenze osservate hanno priorità sulle dichiarazioni del report.

---

## FL-11 — Riconciliazione report/evidenze

Il sistema confronta automaticamente ciò che l’esecutore ha dichiarato con ciò che è stato osservato.

Controlli minimi:

- file dichiarati vs file modificati reali;
- comandi dichiarati vs comandi registrati;
- test dichiarati vs test eseguiti;
- esito test dichiarato vs codice di uscita;
- commit dichiarato vs commit rilevato;
- push dichiarato vs commit sul remoto;
- working tree dichiarato vs stato reale;
- riferimenti rimossi dichiarati vs ricerca globale;
- output obbligatori dichiarati vs file realmente presenti.

Esiti possibili:

- `MATCH`;
- `PARTIAL_MATCH`;
- `MISMATCH`;
- `NOT_VERIFIABLE`;
- `MISSING_EVIDENCE`.

### FL-11.1 — Esempi di blocco

```text
Report: 3 file modificati
Repository: 4 file modificati
Esito: MISMATCH
```

```text
Report: push completato
Remoto: commit non presente
Esito: MISMATCH
```

```text
Report: tutti i riferimenti .mdx rimossi
Ricerca globale: 1 riferimento residuo
Esito: MISMATCH
```

---

## FL-12 — Verifica tecnica deterministica

La verifica tecnica controlla:

- rispetto dello scope;
- presenza degli output obbligatori;
- completezza del report;
- esecuzione dei test richiesti;
- esito dei test;
- stato Git;
- commit e push;
- ricerche obbligatorie;
- file residui;
- anomalie del working tree;
- massimo numero di tentativi;
- dipendenze della task;
- transizione di stato.

La task può passare oltre solo se tutte le condizioni obbligatorie sono soddisfatte oppure esiste una deroga esplicita.

---

## FL-13 — Verifica macroscopica deterministica iniziale

Nell’MVP la verifica macroscopica non usa ancora ragionamento IA.

Si limita a controlli strutturali e globali:

- ricerca nel repository oltre il write scope;
- ricerca nei documenti registrati;
- controllo di riferimenti residui;
- verifica di file fuori scope modificati;
- confronto con aree dichiarate invarianti;
- verifica che la documentazione obbligatoria sia stata aggiornata;
- controllo che task dipendenti non risultino incoerenti;
- controllo che non esistano bug bloccanti collegati;
- controllo che il collaudo richiesto sia ancora mancante;
- controllo che lo stato della milestone non venga aggiornato prematuramente.

Quando viene trovato un problema fuori scope:

- l’esecuzione locale può risultare riuscita;
- l’obiettivo complessivo resta non completato;
- la task entra in `OUT_OF_SCOPE_FINDINGS` o `PARTIALLY_COMPLETED`;
- serve una decisione umana;
- può essere esteso lo scope oppure creata una task correttiva.

---

## FL-14 — Verifica della verifica

Il sistema deve controllare anche la completezza della verifica svolta.

Controlli iniziali deterministici:

- tutti i controlli obbligatori sono stati eseguiti;
- nessun controllo richiesto è stato saltato;
- il verification scope coincide con quello previsto;
- le ricerche hanno coperto le cartelle richieste;
- i test sono quelli previsti dalla task;
- commit, branch e baseline usati sono quelli corretti;
- le evidenze appartengono al tentativo corrente;
- non sono state riutilizzate prove obsolete;
- le eccezioni sono registrate e ancora valide.

La verifica non può risultare positiva se il proprio perimetro è incompleto.

---

## FL-15 — Collaudo manuale

Quando richiesto, la task passa a `FUNCTIONAL_VALIDATION`.

Il collaudo umano registra:

- procedura seguita;
- ambiente;
- risultato atteso;
- risultato osservato;
- problemi trovati;
- allegati o note;
- esito;
- eventuale bug creato;
- approvatore.

Un test automatico positivo non sostituisce il collaudo funzionale quando quest’ultimo è richiesto.

---

## FL-16 — Approvazione e chiusura

La task può essere completata solo quando concordano:

- report;
- evidenze;
- verifica tecnica;
- verifica macroscopica;
- verifica della verifica;
- collaudo, se richiesto;
- approvazione umana.

La chiusura registra:

- stato finale;
- data;
- approvatore;
- commit associato;
- baseline di partenza;
- evidenze principali;
- deroghe;
- bug aperti;
- task correttive create.

### FL-16.1 — Deroghe

Una deroga deve specificare:

- regola superata;
- motivo;
- approvatore;
- durata o scadenza;
- rischio accettato;
- azione correttiva;
- task collegata.

La deroga non elimina l’incompletezza: la rende esplicita e governata.

---

## FL-17 — Aggiornamento della baseline

Dopo una chiusura valida, il sistema può proporre una nuova baseline.

La baseline viene pubblicata solo dopo approvazione umana.

Contiene:

- commit di riferimento;
- task incluse;
- bug noti;
- decisioni vigenti;
- milestone;
- stato sintetico;
- hash;
- data;
- approvatore.

La baseline precedente resta nello storico.

---

## FL-18 — Gestione dei bug

Un bug deve essere un’entità collegata allo storico.

Campi iniziali:

- identificatore;
- titolo;
- sintomo;
- severità;
- stato;
- data di scoperta;
- task durante cui è emerso;
- task o commit potenzialmente responsabile;
- requisito violato;
- ragione per cui non è stato rilevato;
- correzione;
- test di regressione;
- rischio residuo;
- aree future da controllare.

Una task già completata non viene riscritta retroattivamente come se non fosse mai stata chiusa.

Il sistema registra invece:

- task completata all’epoca;
- bug scoperto successivamente;
- relazione tra task, bug e correzione;
- eventuale nuova task correttiva;
- impatto sulla salute corrente.

---

## FL-19 — Stati della task

Stati principali:

```text
DRAFT
ANALYZED
READY
IN_EXECUTION
EXECUTION_REPORTED
EVIDENCE_COLLECTION
TECHNICAL_VERIFICATION
MACRO_VERIFICATION
FUNCTIONAL_VALIDATION
HUMAN_APPROVAL
COMPLETED
```

Stati alternativi:

```text
BLOCKED
FAILED
PARTIALLY_COMPLETED
OUT_OF_SCOPE_FINDINGS
EVIDENCE_INCOMPLETE
REGRESSION_DETECTED
EXCEPTION_REQUIRED
REOPENED
CANCELLED
```

Lo stato `COMPLETED` non può essere impostato direttamente dall’esecutore.

---

## FL-20 — Primo vertical slice funzionante

Il primo vertical slice deve includere soltanto il seguente flusso:

1. creazione del progetto;
2. collegamento del repository;
3. creazione del database dedicato;
4. acquisizione dello snapshot iniziale;
5. creazione di una task con campi minimi;
6. generazione del contratto esecutivo;
7. registrazione dell’avvio;
8. importazione del report;
9. scansione Git post-esecuzione;
10. confronto file dichiarati/file reali;
11. verifica di test richiesti;
12. verifica di commit;
13. verifica di push;
14. ricerca globale configurata;
15. blocco della chiusura in caso di discrepanza;
16. approvazione manuale;
17. chiusura e registrazione evento.

### FL-20.1 — Criteri di accettazione del vertical slice

Il vertical slice è accettato quando dimostra almeno questi casi:

1. report senza elenco file modificati → task non chiudibile;
2. file reale non dichiarato → mismatch;
3. test richiesto non eseguito → task non chiudibile;
4. commit richiesto assente → task non chiudibile;
5. push richiesto assente → task non chiudibile;
6. riferimento residuo trovato fuori dal write scope → obiettivo non completato;
7. tutti i controlli positivi → task approvabile;
8. deroga manuale → chiusura consentita ma incompleta e registrata;
9. database e storico sopravvivono alla riapertura dell’applicazione;
10. nessuna API IA necessaria per completare il flusso.

---

## FL-21 — Architettura logica del primo MVP

```text
Tauri 2
├── Frontend React + TypeScript + Vite
└── Core Rust
    ├── Project Core
    ├── Task Lifecycle
    ├── Baseline Manager
    ├── Event Store
    ├── Repository Observer
    ├── Git Inspector
    ├── Controlled Process Runner
    ├── Evidence Collector
    ├── Report Parser
    ├── Reconciliation Engine
    ├── Verification Engine
    ├── Policy Engine
    ├── SQLite Adapter
    └── Export/Backup
```

Il frontend non accede direttamente al database o al sistema operativo.

---

## FL-22 — Dati nel repository e dati nel software

### Nel repository

Rimangono soltanto contenuti specifici del progetto e utili alla sua comprensione:

- costituzione o descrizione del progetto;
- architettura vigente;
- requisiti;
- decisioni tecniche pubblicate;
- baseline leggibile;
- milestone;
- documentazione tecnica;
- eventuali specifiche di task che si decide di pubblicare;
- manifest minimo di collegamento.

### Nel database e nel motore proprietario

Rimangono:

- workflow;
- metodo operativo;
- regole di completamento;
- tentativi;
- report;
- evidenze;
- verifiche;
- verifica della verifica;
- deroghe;
- approvazioni;
- storico;
- bug;
- grafo semantico;
- pacchetti di contesto;
- log;
- risultati dei controlli;
- logica proprietaria di selezione e combinazione delle policy.

---

## FL-23 — Elementi esplicitamente rinviati

Non fanno parte del primo vertical slice:

- orchestrazione multi-agent;
- chiamate API a modelli IA;
- analisi semantica automatica;
- sincronizzazione cloud;
- PostgreSQL o Supabase;
- collaborazione multiutente;
- portale cliente;
- commit e push automatici;
- modifiche automatiche al codice;
- integrazione Jira o Linear;
- gestione di più organizzazioni;
- sistema di plugin pubblico;
- aggiornamenti automatici;
- firma dell’installer.

Questi elementi potranno essere introdotti solo dopo aver validato il nucleo deterministico.

---

## FL-24 — Regola conclusiva

Project Integrity OS deve essere progettato in modo che il progetto possa essere governato anche quando:

- l’IA cambia;
- la chat viene persa;
- l’esecutore è una persona;
- l’esecutore è un agente;
- l’orchestratore viene sostituito;
- il progetto viene riaperto mesi dopo;
- un bug viene scoperto dopo una task approvata.

La continuità deve risiedere nel modello, nello storico, nelle evidenze e nelle procedure del software, non nella memoria di una conversazione.
