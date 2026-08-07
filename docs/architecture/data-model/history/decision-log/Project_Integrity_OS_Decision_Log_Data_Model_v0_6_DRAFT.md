# Project Integrity OS

## Decision Log preliminare — TODO-0101 — v0.6

> **Vista storica normalizzata.** L’artefatto originale è conservato come `.original.txt`; sono corretti soltanto naming, metadati, delimitatori Markdown o collegamenti relativi.


**Stato:** DRAFT — consolidato dopo il correction set
**Data:** 2026-08-06
**Task:** `TODO-0101 — Definire schema dati minimo`
**Versione precedente:** [v0.5](Project_Integrity_OS_Decision_Log_TODO-0101_v0_5_DRAFT.md)

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
DEC-0101-009 — Provenienza
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

# 2. Correction Set

Documento:

[Project Integrity OS — Correction Set TODO-0101 v0.1](../../verification/history/Project_Integrity_OS_Correction_Set_TODO-0101_v0_1_DRAFT.md)

Correzioni:

```text
C-0101-001 — cardinalità strutturali vs lifecycle
C-0101-002 — ownership dei report
C-0101-003 — BUG nel registro comune
C-0101-004 — root project entity
C-0101-005 — cataloghi globali vs configurazioni locali
```

Le correzioni non annullano le decisioni precedenti.

Le raffinano e ne rimuovono le incompatibilità.

---

# 3. Documenti corretti

```text
08 Registro Elementi Irrisolti v0.2
10 Integrità Trasversale Anti-Orfano v0.2
12 Ruoli Permessi Sensibilità Redazione v0.2
14 Cardinalità Tabelle Associative v0.2
15 Schema Completo Implementazione Progressiva v0.2
```

Le rispettive versioni v0.1 sono conservate in `../decisions/history/`.

---

# 4. Risoluzioni consolidate

## BUG

```text
register_item_type include BUG
```

## Project root

```text
projects.project_id = root project_entities.entity_id
```

## Report ownership

```text
ogni report possiede esattamente un owner autorevole
```

## Cardinalità

```text
minimi dipendenti dal lifecycle
→ transition requirements
```

## Cataloghi

```text
system catalog senza project_id
project-local configuration con project_id NOT NULL
```

---

# 5. Stato della task

```text
FASE DECISIONALE: COMPLETA CON CORREZIONI
STRUTTURA DOCUMENTALE: CONSOLIDATA
SCHEMA ARCHITECTURE: DA PRODURRE
ENTITY CATALOG: DA PRODURRE
RELATIONSHIP MATRIX: DA PRODURRE
CONSTRAINT CATALOG: DA PRODURRE
BRIEF DEFINITIVO: BLOCCATO FINO AI DELIVERABLE
IMPLEMENTAZIONE: NON AVVIABILE
```

---

# 6. Prossimo passo

```text
1. verificare applicazione del correction set;
2. produrre Schema Architecture;
3. produrre Entity Catalog;
4. produrre Relationship Matrix;
5. produrre Constraint Catalog;
6. riscrivere il brief TODO-0101.
```
