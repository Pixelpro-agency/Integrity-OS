# Project Integrity OS

## Modello gerarchico del contesto — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole  
**Data:** 2026-08-05  
**Ambito:** gerarchia di progetto, entità di governance e navigazione dal macroscopico al microscopico  
**Origine:** analisi preliminare di `TODO-0101`  
**Relazioni:** `DEC-0101-001`, `DEC-0101-002`, `DEC-0101-003`, `DEC-0101-004`, `DEC-0101-006`, `DEC-0101-007`

---

# 1. Obiettivo

Definire una gerarchia stabile che distingua pianificazione, unità di lavoro, esecuzione e tentativi.

Il modello deve impedire che termini diversi vengano usati come sinonimi e deve permettere di attraversare il progetto:

```text
dal progetto
fino al singolo comando, test o evidenza
```

e in senso inverso:

```text
dal singolo fatto osservato
fino all’obiettivo e alla decisione originaria
```

---

# 2. Gerarchia primaria

```text
PROJECT
└── PHASE
    └── WORK ITEM
        └── TASK
            └── TASK EXECUTION
                └── ATTEMPT
```

## 2.1 `project`

Rappresenta il progetto governato.

Responsabilità:

- identità;
- repository;
- database dedicato;
- configurazione;
- stato complessivo;
- baseline;
- documentazione;
- storico.

## 2.2 `phase`

Rappresenta un grande momento, dominio o blocco strategico.

Esempi:

```text
Fondazioni
Persistenza
Repository e baseline
Task Contract
Esecuzione
Verifica
Interfaccia
```

Una fase:

- appartiene a un progetto;
- contiene work item;
- possiede stato;
- può dipendere da altre fasi;
- non viene completata automaticamente da una singola task.

## 2.3 `work_item`

Rappresenta una voce della To-Do autorevole.

Esempi:

```text
TODO-0101
TODO-0102
TODO-0901
```

Il work item:

- appartiene a una fase;
- possiede priorità;
- possiede dipendenze di pianificazione;
- raccoglie una o più task concrete;
- rappresenta l’impegno governato del backlog;
- non coincide con una sessione esecutiva.

## 2.4 `task`

Rappresenta un’unità esecutiva concreta necessaria a realizzare un work item.

Esempio:

```text
TODO-0102 — Implementare SQLite adapter
```

può essere articolato in:

```text
TASK-0102-01 — Integrare la libreria SQLite
TASK-0102-02 — Implementare le migrazioni
TASK-0102-03 — Implementare apertura e riapertura
TASK-0102-04 — Implementare test di persistenza
```

La task possiede:

- obiettivo;
- motivazione;
- scope;
- contratto;
- requisiti;
- criteri di accettazione;
- test richiesti;
- dipendenze esecutive;
- policy;
- stato;
- relazioni con decisioni e documenti.

## 2.5 `task_execution`

Rappresenta un ciclo esecutivo concreto affidato a:

- una persona;
- una chat;
- un agente;
- un provider;
- una modalità operativa;
- una sessione.

La stessa task può avere più esecuzioni distinte.

Esempio:

```text
EXECUTION-0042
task: TASK-0102-03
executor_type: CHAT_ASSISTED
provider: Claude
mode: BROWSER_OPERATOR_ASSISTED
```

## 2.6 `attempt`

Rappresenta un singolo tentativo numerato e consumabile all’interno di una task execution.

Esempio:

```text
EXECUTION-0042
├── ATTEMPT-0001 — VERIFIED_FAILED
├── ATTEMPT-0002 — TECHNICAL_FAILURE
└── ATTEMPT-0003 — VERIFIED_PASSED
```

Ogni tentativo può avere:

- Context Package;
- prompt congelato;
- snapshot iniziale;
- report;
- command run;
- test run;
- evidenze;
- riconciliazione;
- verifiche;
- collaudo;
- approvazioni;
- eventi.

---

# 3. Decisione strutturale

`task_executions` e `attempts` sono entità differenti.

```text
task_execution
= ciclo esecutivo complessivo

attempt
= singolo tentativo numerato
```

Prompt Schema e Report Schema devono riferirsi al record `attempt`.

Non devono essere creati due concetti concorrenti chiamati `attempt_id`.

---

# 4. Gerarchia di governance parallela

La gerarchia primaria è attraversata da entità di governo:

```text
ANALYSES
DECISIONS
DOCUMENTS
DOCUMENT VERSIONS
REQUIREMENTS
ACCEPTANCE CRITERIA
TEST DEFINITIONS
TEST RUNS
REPORTS
EVIDENCE
RECONCILIATIONS
VERIFICATIONS
VALIDATIONS
APPROVALS
EXCEPTIONS
BUGS
BASELINES
EVENTS
RISKS
OPEN QUESTIONS
ASSUMPTIONS
FINDINGS
CONFLICTS
```

Queste entità non appartengono tutte esclusivamente a un singolo livello.

Esempi:

- una decisione può influenzare più fasi, work item o task;
- un requisito può essere implementato da più task;
- un test può proteggere più criteri;
- un bug può essere scoperto durante una task ma corretto da un’altra;
- una baseline include più task e documenti;
- un documento può governare più esecuzioni.

---

# 5. Navigazione discendente

Dal macroscopico al microscopico:

```text
project
→ phase
→ work_item
→ task
→ task_execution
→ attempt
→ test_run
→ command_run
→ stdout/stderr
→ evidence
```

Esempio:

```text
Project Integrity OS
→ Persistenza
→ TODO-0102
→ TASK-0102-04
→ EXECUTION-0045
→ ATTEMPT-0002
→ TEST-RUN-0031
→ CMD-0055
→ exit code 1
→ EVIDENCE-0094
```

---

# 6. Navigazione ascendente

Dal microscopico al macroscopico:

```text
riga di output
→ command_run
→ test_run
→ evidence
→ attempt
→ task_execution
→ task
→ work_item
→ phase
→ project
```

Il sistema deve permettere di risalire senza ricerca manuale nei file.

---

# 7. Relazioni principali

```text
projects 1 ── N phases
phases 1 ── N work_items
work_items 1 ── N tasks
tasks 1 ── N task_executions
task_executions 1 ── N attempts
```

Relazioni di pianificazione:

```text
work_items N ── N work_items
```

Relazioni esecutive:

```text
tasks N ── N tasks
```

Le due categorie non devono essere confuse.

---

# 8. Relazioni di tracciabilità

Esempi minimi:

```text
analysis DERIVES decision
decision AUTHORIZES task
decision AFFECTS document
document_version GOVERNS attempt
requirement IMPLEMENTED_BY task
acceptance_criterion SATISFIED_BY verification
test_definition VERIFIES requirement
test_run EXECUTES test_definition
evidence PRODUCED_BY command_run
reconciliation COMPARES report WITH evidence
verification USES evidence
validation VALIDATES task
approval APPROVES verification
bug DISCOVERED_DURING attempt
bug CORRECTED_BY task
baseline INCLUDES task
baseline REFERENCES document_version
```

---

# 9. Identità

Ogni entità persistente usa un UUID tecnico.

Le entità citabili usano anche `reference_code`.

Esempi:

```text
PHASE-0001
WORK-0101
TASK-0101-01
EXECUTION-0001
ATTEMPT-0001
DECISION-0001
DOCUMENT-0001
REQUIREMENT-0001
AC-0001
TEST-0001
TEST-RUN-0001
```

Le foreign key usano UUID.

---

# 10. Stati separati

## 10.1 Phase

```text
PLANNED
ACTIVE
COMPLETED
BLOCKED
ARCHIVED
```

## 10.2 Work item

```text
TODO
IN_ANALYSIS
ANALYZED
READY
IN_PROGRESS
IN_VERIFICATION
DONE
BLOCKED
CANCELLED
```

## 10.3 Task

```text
DRAFT
READY
IN_EXECUTION
EXECUTION_REPORTED
IN_VERIFICATION
AWAITING_APPROVAL
COMPLETED
FAILED
BLOCKED
CANCELLED
```

## 10.4 Task execution

Vocabolario da finalizzare in una decisione successiva.

Dovrà distinguere almeno:

```text
PLANNED
ACTIVE
CLOSED
BLOCKED
CANCELLED
```

## 10.5 Attempt

```text
DRAFT
READY
IN_PROGRESS
AWAITING_REPORT
COLLECTING_EVIDENCE
IN_RECONCILIATION
IN_VERIFICATION
VERIFIED_PASSED
VERIFIED_FAILED
TECHNICAL_FAILURE
BLOCKED
CANCELLED
```

I vocabolari restano DRAFT fino alla decisione canonica sugli stati.

---

# 11. Regole di non propagazione automatica

Un livello inferiore superato non completa automaticamente il superiore.

Esempi:

- un attempt superato non chiude automaticamente la task;
- una task completata non chiude automaticamente il work item;
- un work item completato non chiude automaticamente la fase;
- una verifica tecnica passata non sostituisce il collaudo richiesto;
- un’approvazione non cancella eccezioni o rischi residui.

Ogni aggregazione deve verificare le proprie condizioni.

---

# 12. Entità documentali

## 12.1 `documents`

Rappresenta il documento logico.

## 12.2 `document_versions`

Rappresenta revisioni immutabili.

Relazione:

```text
documents 1 ── N document_versions
```

Una versione può:

- sostituire una versione precedente;
- essere corrente;
- essere storica;
- governare esecuzioni;
- essere inclusa in baseline;
- essere usata in Context Package.

---

# 13. Requisiti e test

```text
requirements
→ acceptance_criteria
→ test_definitions
→ test_runs
→ evidence
→ verifications
```

Il sistema deve poter identificare:

- requisiti senza criteri;
- criteri senza test;
- test mai eseguiti;
- test eseguiti senza evidenze;
- test falliti ma ignorati;
- test obsoleti;
- test appartenenti a tentativi diversi.

---

# 14. Documentazione delle fasi

Ogni fase deve poter collegare:

- analisi;
- decisioni;
- documenti;
- work item;
- requisiti;
- rischi;
- milestone;
- baseline iniziale e finale;
- stato;
- eventi.

Il sistema ultimato deve permettere di aprire una fase e vedere:

```text
perché esiste
cosa comprende
quali decisioni la governano
quali work item contiene
quali task sono state eseguite
quali problemi sono emersi
quali prove sostengono la chiusura
```

---

# 15. Context Graph

La gerarchia non è un semplice albero.

Esistono collegamenti trasversali.

Il sistema deve quindi trattare la struttura come:

```text
gerarchia primaria
+
grafo di relazioni di governance
```

La gerarchia fornisce orientamento.

Il grafo fornisce tracciabilità.

---

# 16. Stato del documento

Questo modello è una bozza di checkpoint.

Restano da finalizzare:

- vocabolari canonici;
- cardinalità di alcune entità;
- lifecycle delle decisioni;
- modello di provenienza;
- elementi irrisolti;
- eventi;
- regole di cancellazione;
- permessi e redazione;
- condizioni complete di transizione.

Non deve essere ancora utilizzato come specifica implementativa definitiva.
