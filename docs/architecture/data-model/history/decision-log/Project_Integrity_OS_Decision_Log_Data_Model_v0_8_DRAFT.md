# Project Integrity OS

## Decision Log — TODO-0101 — v0.8

**Stato:** DRAFT — decisioni di analisi consolidate, schema finale non ancora approvato
**Data:** 2026-08-06
**Task:** `TODO-0101 — Definire schema dati minimo`
**Versione precedente:** `history/Project_Integrity_OS_Decision_Log_TODO-0101_v0_7_DRAFT.md`
**Commit di integrazione:** `382c96f1f93de4ef6003f92db209675ab36d3c3c`

---

# 1. Perimetro di approvazione

Le decisioni `DEC-0101-001` → `DEC-0101-020` sono approvate come **decisioni di analisi e consolidamento concettuale**.

Non costituiscono ancora:

- schema fisico SQLite approvato;
- Data Dictionary autorevole;
- migrazione SQL;
- autorizzazione a implementare TODO-0102;
- chiusura di TODO-0101.

```text
APPROVED AS ANALYSIS DECISIONS
NOT YET APPROVED AS AUTHORITATIVE PHYSICAL SCHEMA
```

---

# 2. Decisioni consolidate

```text
DEC-0101-001 — Separazione task_executions / attempts
DEC-0101-002 — UUID e reference_code
DEC-0101-003 — Catena completa del ciclo di lavoro
DEC-0101-004 — Entità di governance di prima classe
DEC-0101-005 — Doppia conservazione documentale
DEC-0101-006 — Gerarchia del lavoro
DEC-0101-007 — Contesto macro→micro
DEC-0101-008 — Context Package
DEC-0101-009 — Provenienza multidimensionale
DEC-0101-010 — Sintesi e drill-down
DEC-0101-011 — Requisiti, criteri e test
DEC-0101-012 — Lifecycle delle decisioni
DEC-0101-013 — Registro elementi irrisolti
DEC-0101-014 — Eventi e ricostruzione temporale
DEC-0101-015 — Integrità e anti-orfano
DEC-0101-016 — Conservazione e cancellazione
DEC-0101-017 — Ruoli, sicurezza e redazione
DEC-0101-018 — Transizioni
DEC-0101-019 — Cardinalità e associazioni
DEC-0101-020 — Schema completo e implementazione progressiva
```

---

# 3. Correction Set consolidato

```text
C-0101-001 — cardinalità strutturali vs minimi di lifecycle
C-0101-002 — ownership autorevole dei report
C-0101-003 — BUG nel registro comune
C-0101-004 — identità della root project entity
C-0101-005 — cataloghi globali vs configurazioni locali
C-0101-006 — riferimenti globali senza FK cross-database
C-0101-007 — tipi canonici di report owner
C-0101-008 — storico completo dei validation result
C-0101-009 — classificazione deterministica delle entità
```

---

# 4. Architettura logica consolidata

## 4.1 Scope

```text
SYSTEM_CATALOG
GLOBAL_REGISTRY
PROJECT_DATABASE
```

## 4.2 Store fisici MVP

```text
CONTROL DATABASE
→ SYSTEM_CATALOG
→ GLOBAL_REGISTRY
→ actors globali

PROJECT DATABASE
→ project root
→ project entities
→ governance e tracciabilità del singolo progetto
```

## 4.3 Riferimenti globali

Nessuna foreign key SQLite attraversa database differenti.

I binding usano:

```text
stable code
catalog version
definition hash
local binding
```

## 4.4 Attori

- identità globale nel CONTROL DATABASE;
- binding dell’attore nel PROJECT DATABASE;
- ruoli, permessi e scope assegnati tramite entità di progetto.

## 4.5 Report owner canonici

```text
EXECUTION_REPORT     → ATTEMPT
VERIFICATION_REPORT  → VERIFICATION
VALIDATION_REPORT    → VALIDATION
INTEGRITY_REPORT     → INTEGRITY_RUN
RECOVERY_REPORT      → TRANSITION_RECOVERY_RUN
SECURITY_REPORT      → SECURITY_REVIEW
IMPORT_REPORT        → IMPORT_RECORD
EXPORT_REPORT        → EXPORT_RECORD
CLOSURE_REPORT       → entità chiusa
DIAGNOSTIC_REPORT    → entità governata di progetto
```

## 4.6 Validation history

```text
VALIDATION
→ VALIDATION_STEP
→ VALIDATION_STEP_RUN
→ VALIDATION_RESULT
```

Un retry crea un nuovo run. I risultati sono append-only.

## 4.7 Classificazione delle entità

```text
SYSTEM_CATALOG
GLOBAL_REGISTRY
PROJECT_ROOT
PROJECT_ENTITY
PROJECT_CONFIGURATION
DERIVED_PROJECTION
EXTERNAL_REFERENCE
PRIVATE_CHILD
```

---

# 5. Open issue non bloccanti per il consolidamento

Restano aperti:

- formato concreto UUID;
- canonical JSON hashing;
- validazione timestamp;
- partial unique index;
- bootstrap TODO-0102/TODO-0103;
- versione della serializzazione dell’event hash;
- rappresentazione dei decimali;
- soglia dei contenuti grandi;
- path e backup del CONTROL DATABASE;
- campi minimi import/export.

Devono essere risolti nei deliverable finali o assegnati esplicitamente alle task successive.

---

# 6. Audit documentale

L’audit del 2026-08-06 ha:

- normalizzato naming e versioni documentali;
- preservato gli originali storici;
- corretto link e code fence rappresentativi;
- aggiornato To-Do, Registry, README e Checkpoint;
- confermato che non risultano file Markdown vuoti, byte NUL o marker di conflitto.

Riferimento:

[Audit documentale v0.1](../verification/Project_Integrity_OS_Audit_Documentale_TODO-0101_v0_1.md)

---

# 7. Prossima decisione consentita

```text
produrre Schema Architecture
```

Non è consentito avviare implementazione SQLite prima della chiusura documentale di TODO-0101.
