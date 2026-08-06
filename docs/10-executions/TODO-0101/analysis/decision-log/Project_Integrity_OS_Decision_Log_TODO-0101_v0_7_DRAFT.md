# Project Integrity OS

## Decision Log preliminare — TODO-0101 — v0.7

**Stato:** DRAFT — consolidato dopo Correction Set v0.2  
**Data:** 2026-08-06  
**Task:** `TODO-0101 — Definire schema dati minimo`  
**Versione precedente:** `history/Project_Integrity_OS_Decision_Log_TODO-0101_v0_6_DRAFT.md`

---

# 1. Decisioni approvate

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

# 2. Correction Set v0.2

```text
C-0101-001 — structural cardinality vs lifecycle minimum
C-0101-002 — authoritative report ownership
C-0101-003 — BUG in common register
C-0101-004 — project root identity
C-0101-005 — global catalog vs local configuration
C-0101-006 — global binding without cross-database FK
C-0101-007 — canonical report owner types
C-0101-008 — complete validation result history
C-0101-009 — deterministic entity classification
```

---

# 3. Risoluzioni consolidate

## Persistence scopes

```text
SYSTEM_CATALOG
GLOBAL_REGISTRY
PROJECT_DATABASE
```

MVP physical stores:

```text
CONTROL DATABASE
PROJECT DATABASE
```

## Global references

```text
stable code
catalog version
definition hash
local binding
```

## Actor references

```text
global actor
→ project_actor_binding
→ membership / role / ownership / approval
```

## Report ownership

```text
one report
→ one authoritative owner
```

## Validation history

```text
validation
→ step
→ step run
→ results
```

## Entity classification

Ogni entity type ha una categoria esatta.

---

# 4. Stato documentale

```text
DECISIONAL PHASE: COMPLETE WITH CORRECTIONS
CURRENT DECISION DOCUMENTS: CONSOLIDATED
HISTORY: TO BE MATERIALIZED BY APPLY SCRIPT
SCHEMA ARCHITECTURE: TO PRODUCE
ENTITY CATALOG: TO PRODUCE
DATA DICTIONARY: TO PRODUCE
FINAL BRIEF: BLOCKED
IMPLEMENTATION: BLOCKED
```

---

# 5. Prossimo passo

```text
apply correction package
→ verify links and history
→ Schema Architecture
→ Entity Catalog
→ Data Dictionary
→ Relationship Matrix
→ Constraint Catalog
→ State and Transition Catalog
→ Portability Matrix
→ Implementation Wave Matrix
→ final brief
```
