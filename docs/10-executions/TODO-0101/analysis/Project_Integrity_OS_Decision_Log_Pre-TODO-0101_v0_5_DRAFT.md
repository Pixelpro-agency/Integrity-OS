# Project Integrity OS

## Decision Log preliminare — TODO-0101 — v0.5

**Stato:** DRAFT — checkpoint conclusivo delle decisioni, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task collegata:** `TODO-0101 — Definire schema dati minimo`  
**Versioni precedenti:** conservate in `analysis/history/`

---

# 1. Decisioni approvate

```text
DEC-0101-001 — Separazione tra task_executions e attempts
DEC-0101-002 — UUID tecnici e reference_code
DEC-0101-003 — Catena completa del ciclo di lavoro
DEC-0101-004 — Entità di governance di prima classe
DEC-0101-005 — Doppia conservazione documentale
DEC-0101-006 — Gerarchia phases/work_items/tasks/executions/attempts
DEC-0101-007 — Contesto dal macroscopico al microscopico
DEC-0101-008 — Context Package versionati e riproducibili
DEC-0101-009 — Provenienza multidimensionale
DEC-0101-010 — Sintesi, drill-down e obsolescenza
DEC-0101-011 — Requisiti, criteri e copertura dei test
DEC-0101-012 — Lifecycle delle decisioni
DEC-0101-013 — Registri degli elementi irrisolti
DEC-0101-014 — Eventi e ricostruzione temporale
DEC-0101-015 — Integrità trasversale e anti-orfano
DEC-0101-016 — Conservazione, rettifiche e cancellazione
DEC-0101-017 — Ruoli, permessi, sensibilità e redazione
DEC-0101-018 — Condizioni complete delle transizioni
DEC-0101-019 — Cardinalità definitive e tabelle associative
DEC-0101-020 — Schema completo e implementazione progressiva
```

---

# 2. Decisioni aggiunte nel checkpoint v0.5

## DEC-0101-019 — APPROVED

Il modello usa:

```text
gerarchia stretta
+
project_entities
+
entity_versions
+
tabelle associative dedicate
+
entity_links limitata alle relazioni supplementari
```

Sono stati consolidati anche i modelli minimi di:

```text
reports
approvals
exceptions
baselines
bugs
verifications
validations
evidence
reconciliations
```

Le cardinalità strutturali appartengono al database.

Le cardinalità condizionali appartengono alle transizioni e agli integrity profile.

## DEC-0101-020 — APPROVED

Il progetto distingue:

```text
schema canonico completo
schema fisico installato
capacità applicativa attiva
```

TODO-0101 completa il modello concettuale e logico.

TODO-0102 materializza progressivamente SQLite e adapter.

Le capacità vengono attivate soltanto come vertical slice integre e verificate.

---

# 3. Stato della fase decisionale

Le decisioni pianificate da `DEC-0101-001` a `DEC-0101-020` sono tutte approvate.

Questo checkpoint conclude la raccolta decisionale preliminare.

Non conclude ancora TODO-0101.

Prima della riscrittura del brief sono ancora necessari:

```text
1. verifica incrociata delle 20 decisioni;
2. rilevamento di conflitti, duplicazioni e lacune;
3. consolidamento del catalogo finale delle entità;
4. verifica della copertura rispetto alla To-Do v0.8;
5. conferma che gli open issue residui siano non bloccanti;
6. riscrittura integrale del brief TODO-0101;
7. produzione dei deliverable logici approvati.
```

---

# 4. Documenti aggiunti nel checkpoint v0.5

```text
Project_Integrity_OS_Cardinalita_Tabelle_Associative_v0_1_DRAFT.md
Project_Integrity_OS_Schema_Completo_Implementazione_Progressiva_v0_1_DRAFT.md
```

I documenti e Decision Log dei checkpoint precedenti restano inclusi e storicizzati.

---

# 5. Brief

Il brief precedente:

```text
Project_Integrity_OS_Brief_TODO-0101_v0_1_DRAFT.md
```

non deve essere promosso.

Deve essere sostituito dopo la verifica complessiva.

---

# 6. Stato operativo

```text
CHECKPOINT DOCUMENTALE v0.5 COMPLETATO
→ FASE DECISIONALE PRELIMINARE COMPLETATA
→ PROSSIMO PASSO: VERIFICA COMPLESSIVA DEC-0101-001..020
```
