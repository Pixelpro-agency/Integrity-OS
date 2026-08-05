# Project Integrity OS
## Modalità di esecuzione — v0.1

**Stato:** decisione architetturale approvata  
**Data:** 2026-08-05  
**Ambito:** modalità con cui una task viene consegnata, eseguita e verificata  
**Principio:** il modello di progetto, la macchina a stati e i criteri di completamento non dipendono dallo strumento esecutore.

---

## 1. Decisione

Project Integrity OS dovrà supportare tre modalità di esecuzione selezionabili per progetto o per singola task:

1. **Browser con operatore umano**
2. **Desktop/local-enabled**
3. **Orchestratore con API**

La modalità cambia il modo in cui vengono eseguite le azioni e raccolte le evidenze. Non cambia:

- il Task Contract;
- lo scope autorizzato;
- la regola dei tentativi;
- il report obbligatorio;
- la raccolta delle evidenze;
- la verifica tecnica;
- la verifica macroscopica;
- la verifica della verifica;
- il collaudo;
- l’approvazione umana;
- la regola secondo cui l’esecutore non può dichiarare autonomamente la task completata.

---

## 2. Principio di indipendenza

Il core non deve dipendere da ChatGPT, da un’app desktop specifica, da un orchestratore o da un provider di modelli.

Architettura concettuale:

```text
Project Core
    ↓
Task Contract
    ↓
Execution Mode Interface
    ├── Browser Operator Adapter
    ├── Desktop/Local Adapter
    └── Orchestrator/API Adapter
    ↓
Evidence Collector
    ↓
Verification Engine
```

Ogni adapter deve rispettare lo stesso contratto di ingresso e produrre un risultato normalizzato.

---

## 3. Negoziazione delle capacità

Il software non deve identificare una modalità soltanto dal nome dello strumento. Deve registrare le capacità effettivamente disponibili nella sessione.

Esempi:

```text
can_read_files
can_write_files
can_run_commands
can_observe_command_output
can_inspect_git
can_create_commit
can_push
can_use_external_tools
can_call_models
requires_human_operator
```

Una modalità desktop senza permesso al terminale non deve essere trattata come equivalente a un esecutore locale completo.

Una chat browser non deve essere considerata capace di osservare il computer soltanto perché riceve istruzioni dall’utente.

---

# 4. Modalità A — Browser con operatore umano

## 4.1 Descrizione

L’IA viene usata attraverso un’interfaccia browser e non dispone di accesso diretto a:

- filesystem locale;
- terminale;
- processi;
- repository;
- stato Git;
- finestra dell’applicazione;
- file non allegati o non incollati.

L’utente svolge il ruolo di operatore materiale.

## 4.2 Flusso

```text
Software prepara il Task Contract
        ↓
utente lo porta nella chat browser
        ↓
chat produce un singolo passaggio operativo
        ↓
utente esegue il comando o modifica il file
        ↓
utente restituisce output o contenuto
        ↓
chat interpreta l’evidenza
        ↓
solo dopo autorizza il passaggio seguente
        ↓
report finale costruito dalle prove ricevute
        ↓
Project Integrity OS verifica direttamente ciò che può osservare
```

## 4.3 Regole obbligatorie

La chat browser deve:

- dichiarare di non avere accesso diretto al computer;
- non affermare di aver creato o verificato file senza prova;
- fornire istruzioni precise con percorso completo;
- fornire comandi sicuri e copiabili;
- procedere in piccoli blocchi;
- attendere l’output prima di proseguire;
- distinguere `dichiarato dall’utente` da `osservato nell’output`;
- non inventare l’esito di build, test, avvio, commit o push;
- compilare il report soltanto dalle evidenze ricevute;
- fermarsi dopo tre tentativi ragionati;
- non usare comandi che chiudano la shell o terminino la sessione;
- in caso di controllo fallito, mostrare l’errore e impedire i passaggi dipendenti.

## 4.4 Evidenze

Le evidenze iniziali possono essere:

- output copiato dal terminale;
- contenuto completo di file;
- screenshot;
- elenco directory;
- hash;
- output Git;
- output dei test;
- conferma manuale esplicitamente marcata come tale.

Nel futuro software, ove possibile, Project Integrity OS dovrà verificare localmente le dichiarazioni ricevute dalla chat browser.

## 4.5 Limite di fiducia

La chat browser guida e interpreta. Non è la fonte primaria della verità locale.

---

# 5. Modalità B — Desktop/local-enabled

## 5.1 Descrizione

L’esecutore opera in un ambiente desktop o locale dotato delle capacità effettivamente autorizzate, per esempio:

- lettura dei file;
- modifica dei file;
- esecuzione di comandi;
- osservazione dell’output;
- ispezione Git;
- accesso agli strumenti locali.

Il software non deve presumere che tutte queste capacità siano sempre disponibili. Deve rilevarle o richiederne conferma.

## 5.2 Flusso

```text
Project Integrity OS consegna Task Contract
        ↓
adapter locale applica permessi e scope
        ↓
esecutore legge/modifica/esegue
        ↓
azioni e output vengono registrati
        ↓
evidenze raccolte direttamente
        ↓
Verification Engine riconcilia report e realtà
```

## 5.3 Regole obbligatorie

- write scope ristretto;
- read/verification scope più ampio;
- comandi controllati;
- nessun terminale generico del prodotto nel primo MVP;
- nessun commit o push automatico senza autorizzazione;
- audit di file, comandi, output e tentativi;
- stop dopo il limite di tentativi;
- report finale obbligatorio;
- nessuna chiusura autonoma della task.

## 5.4 Vantaggio

Riduce il lavoro manuale e permette di osservare direttamente le evidenze locali.

---

# 6. Modalità C — Orchestratore con API

## 6.1 Descrizione

Project Integrity OS affida la task a un orchestratore capace di selezionare e coordinare modelli, agenti e strumenti tramite API.

Questa modalità viene introdotta dopo la validazione del nucleo deterministico.

## 6.2 Responsabilità dell’orchestratore

L’orchestratore può:

- selezionare modelli;
- assegnare ruoli;
- coordinare esecutore e revisore;
- parallelizzare attività autorizzate;
- usare strumenti;
- applicare budget;
- raccogliere output.

Non può:

- modificare obiettivi o decisioni approvate;
- ampliare autonomamente lo scope;
- cambiare i criteri di accettazione;
- segnare la task `COMPLETED`;
- sostituire le verifiche deterministiche;
- approvare deroghe critiche.

## 6.3 Dati da registrare

- provider;
- modello;
- versione/configurazione;
- orchestratore;
- agenti coinvolti;
- prompt e Context Package;
- tool call;
- costi;
- token;
- durata;
- tentativi;
- output;
- errori;
- evidenze;
- versioni delle policy applicate.

## 6.4 Principio economico

Le API devono essere usate soltanto quando il valore semantico o operativo giustifica il costo.

Tutto ciò che può essere verificato deterministicamente resta fuori dalle chiamate IA.

---

# 7. Contratto comune delle modalità

Ogni modalità riceve almeno:

```text
task_id
execution_id
attempt_number
baseline_id
repository_reference
objective
write_scope
read_scope
verification_scope
constraints
required_checks
required_tests
required_outputs
commit_policy
push_policy
stop_conditions
report_schema_version
```

Ogni modalità restituisce almeno:

```text
execution_status
attempts_used
executor_type
declared_files_checked
declared_files_modified
declared_commands
declared_tests
declared_commit
declared_push
limitations
raw_report
evidence_references
```

Le dichiarazioni restano separate dalle evidenze osservate.

---

# 8. Stati condivisi

Le tre modalità usano la stessa macchina a stati:

```text
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

Una differenza di modalità non autorizza scorciatoie.

---

# 9. Modalità selezionata per TODO-0002

Per l’esecuzione attuale è selezionata:

```text
BROWSER_OPERATOR_ASSISTED
```

Motivo:

- l’utente dispone attualmente della chat browser;
- la chat non può operare direttamente nelle cartelle locali;
- la chat non può eseguire direttamente il terminale;
- l’utente può eseguire i passaggi e restituire le evidenze;
- il flusso permette di avviare realmente il progetto senza attendere la modalità desktop.

Il prompt desktop già creato resta valido come variante futura, ma non deve essere usato per l’esecuzione corrente.

---

# 10. Sviluppo futuro nel prodotto

Dopo una base minima funzionante, il prodotto dovrà introdurre:

1. interfaccia comune `ExecutionMode`;
2. profilo di capacità;
3. Browser Operator Adapter;
4. Desktop/Local Adapter;
5. Orchestrator/API Adapter;
6. normalizzazione dei report;
7. normalizzazione delle evidenze;
8. confronto tra prestazioni, costi, errori e affidabilità delle modalità.

La modalità deve essere selezionabile nella creazione o nell’avvio della task.

---

# 11. Decisione conclusiva

> Project Integrity OS non dovrà scegliere un unico modo di lavorare con l’IA. Dovrà governare più modalità operative mantenendo invariati contratto, procedure, evidenze e criteri di chiusura. Nell’immediato lo sviluppo inizierà tramite chat browser e operatore umano; in futuro verranno supportate anche esecuzione desktop/local-enabled e orchestrazione tramite API.
