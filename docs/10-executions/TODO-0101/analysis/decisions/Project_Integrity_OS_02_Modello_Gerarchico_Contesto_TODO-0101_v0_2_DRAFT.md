# Project Integrity OS

## Modello gerarchico del contesto — v0.2

**Stato:** DRAFT — modello consolidato, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task:** `TODO-0101`  
**Decisioni:** `DEC-0101-001`, `DEC-0101-002`, `DEC-0101-003`, `DEC-0101-004`, `DEC-0101-006`, `DEC-0101-007`, `DEC-0101-015`, `DEC-0101-019`  
**Sostituisce:** `Project_Integrity_OS_02_Modello_Gerarchico_Contesto_TODO-0101_v0_1_DRAFT.md`

---

# 1. Obiettivo

Definire una gerarchia stabile che separi:

- pianificazione;
- unità di lavoro;
- affidamento esecutivo;
- tentativi;
- risultati tecnici;
- governo e verifica.

Il sistema deve consentire la navigazione:

```text
PROJECT → singolo fatto osservato
```

e:

```text
singolo fatto osservato → PROJECT
```

---

# 2. Gerarchia primaria

```text
PROJECT
└── PHASE
    └── WORK_ITEM
        └── TASK
            └── TASK_EXECUTION
                └── ATTEMPT
```

## Project

Rappresenta il progetto governato e la root del proprio grafo.

```text
projects.project_id = project_entities.entity_id
```

## Phase

Rappresenta un dominio o momento strategico.

## Work item

Rappresenta una voce autorevole della To-Do.

## Task

Rappresenta un'unità esecutiva concreta con Task Contract, requisiti, criteri e test previsti.

## Task execution

Rappresenta un ciclo esecutivo affidato a un esecutore, provider, modalità o sessione.

## Attempt

Rappresenta un singolo tentativo numerato e governato all'interno della task execution.

---

# 3. Cardinalità strutturali

```text
PROJECT        1 ── 0..N PHASES
PHASE          1 ── 0..N WORK_ITEMS
WORK_ITEM      1 ── 0..N TASKS
TASK           1 ── 0..N TASK_EXECUTIONS
TASK_EXECUTION 1 ── 0..N ATTEMPTS
```

Ogni figlio possiede un solo parent autorevole.

I minimi richiesti per avanzare di stato sono definiti dal Transition Engine.

Esempio:

```text
TASK 1 ── 0..1 TASK_CONTRACT

TASK → DEFINED
richiede una versione DRAFT

TASK → READY
richiede una versione FROZEN
```

---

# 4. Task execution e attempt

```text
task_execution
= ciclo esecutivo complessivo

attempt
= tentativo singolo numerato
```

Vincoli:

```text
UNIQUE(task_execution_id, attempt_number)
```

Devono essere distinti:

```text
attempt_number
consumed_attempt_number
```

La policy dei tentativi appartiene alla task execution o alla Task Contract version.

Prompt, Context Package, report, command run, test run, evidence e verifiche fanno riferimento all'attempt quando rappresentano il lavoro di un tentativo.

---

# 5. Dipendenze

Relazioni dedicate:

```text
phase_dependencies
work_item_dependencies
task_dependencies
```

Cardinalità:

```text
PHASE     N ── M PHASE
WORK_ITEM N ── M WORK_ITEM
TASK      N ── M TASK
```

Regole:

- niente auto-dipendenza;
- stesso progetto;
- nessun ciclo per le dipendenze dichiarate bloccanti;
- tipo, motivazione e periodo di validità espliciti;
- una dipendenza soddisfatta non completa automaticamente il dipendente.

---

# 6. Governance trasversale

La gerarchia è attraversata da entità di governo:

```text
ANALYSES
DECISIONS
DOCUMENTS
OBJECTIVES
REQUIREMENTS
ACCEPTANCE_CRITERIA
TEST_DEFINITIONS
REPORTS
EVIDENCE
RECONCILIATIONS
VERIFICATIONS
VALIDATIONS
APPROVALS
EXCEPTIONS
REGISTER_ITEMS
BASELINES
EVENTS
CONTEXT_PACKAGES
SUMMARIES
```

Queste entità possono riguardare più livelli.

Le relazioni fondamentali usano tabelle dedicate.

Le relazioni supplementari usano `entity_links`.

---

# 7. Navigazione discendente

Esempio:

```text
PROJECT
→ PHASE
→ WORK_ITEM
→ TASK
→ TASK_EXECUTION
→ ATTEMPT
→ TEST_RUN
→ COMMAND_RUN
→ TEST_RUN_RESULT
→ EVIDENCE
```

Ogni passaggio deve usare UUID e relazioni risolvibili.

---

# 8. Navigazione ascendente

Esempio:

```text
EVIDENCE
→ TEST_RUN_RESULT
→ TEST_RUN
→ ATTEMPT
→ TASK_EXECUTION
→ TASK
→ WORK_ITEM
→ PHASE
→ PROJECT
```

Una evidence può avere più relazioni di supporto, ma deve mantenere la provenienza e il contesto di produzione.

---

# 9. Identità condivisa

Ogni entità citabile project-local usa:

```text
project_entities.entity_id
```

La tabella specializzata condivide lo stesso UUID.

Ogni versione citabile usa:

```text
entity_versions.entity_version_id
```

Il `entity_type` deve corrispondere a una sola specializzazione.

La classificazione di ogni entità è deterministica e viene registrata nell'Entity Catalog.

---

# 10. Stati canonici

I lifecycle completi appartengono al documento:

```text
Project_Integrity_OS_13_Transizioni_Condizioni_Complete_TODO-0101_v0_2_DRAFT.md
```

Questo documento non definisce vocabolari concorrenti.

Principio:

```text
stato corrente
≠ evento
≠ risultato di verifica
≠ risultato di approval
```

Il completamento non si propaga automaticamente.

---

# 11. Requisiti e test

Catena canonica:

```text
OBJECTIVE
→ REQUIREMENT
→ ACCEPTANCE_CRITERION
→ TEST_DEFINITION_VERSION
→ TEST_RUN
→ TEST_RUN_RESULT
→ EVIDENCE
→ VERIFICATION
→ VALIDATION
→ APPROVAL
```

Un test definition non verifica direttamente un requisito.

Definisce un controllo associato a uno o più acceptance criterion.

La verification determina se criteri, risultati ed evidence soddisfano il requisito.

---

# 12. Report

Ogni report possiede:

```text
una identità logica
una o più versioni
esattamente un owner autorevole
zero o più subject aggiuntivi
```

L'owner è una project entity ammessa dalla policy del tipo di report.

`report_subjects` non modifica l'ownership.

---

# 13. Regole aggregate

- un attempt superato non completa automaticamente la task;
- una task completata non completa automaticamente il work item;
- un work item completato non completa automaticamente la phase;
- una verification tecnica non sostituisce una validation richiesta;
- una approval non trasforma un risultato failed in passed;
- una eccezione non nasconde il requisito derogato;
- una baseline approvata non rende automaticamente correnti tutte le entità incluse.

Ogni aggregazione usa una transizione esplicita.

---

# 14. Decisione consolidata

```text
DEC-0101-001
DEC-0101-006
DEC-0101-007
DEC-0101-015
DEC-0101-019

La gerarchia primaria è:

project
→ phase
→ work item
→ task
→ task execution
→ attempt.

Le cardinalità strutturali ammettono zero figli.

I minimi dipendenti dal lifecycle appartengono
alle transizioni.

La gerarchia fornisce orientamento.
Il grafo di governance fornisce tracciabilità.
```
