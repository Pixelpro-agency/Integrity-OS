# Project Integrity OS

## Decision Log preliminare — TODO-0101 — v0.4

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole
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
```

# 2. Decisioni aggiunte nel checkpoint v0.4

## DEC-0101-016 — APPROVED

Archiviazione, ritiro, annullamento, sostituzione, rettifica, redazione, purge, hard delete, ripristino e tombstone restano operazioni distinte.

Gli hard delete sono limitati a draft mai utilizzati.

Le operazioni distruttive usano policy, assessment, manifest, approvazioni, journal ed integrity check.

## DEC-0101-017 — APPROVED

Il modello di sicurezza combina:

```text
RBAC
+
scope gerarchico
+
policy
+
classificazione
+
separation of duties
+
DEFAULT DENY
```

Le IA operano tramite sessioni e deleghe limitate.

Classificazione e redazione si applicano a entità, versioni, campi, Context Package ed export.

## DEC-0101-018 — APPROVED

Gli stati non vengono modificati direttamente.

Ogni passaggio usa una transizione nominata, versionata, autorizzata, valutata, atomica e registrata.

Gli effetti esterni sono journaled e verificati tramite postcondizioni.

# 3. Documenti del checkpoint v0.4

```text
Project_Integrity_OS_Conservazione_Rettifiche_Cancellazione_v0_1_DRAFT.md
Project_Integrity_OS_Ruoli_Permessi_Sensibilita_Redazione_v0_1_DRAFT.md
Project_Integrity_OS_Transizioni_Condizioni_Complete_v0_1_DRAFT.md
```

I documenti dei checkpoint precedenti restano inclusi.

# 4. Decisioni ancora aperte

```text
DEC-0101-019 — Cardinalità definitive e tabelle associative
DEC-0101-020 — Confine tra schema completo e implementazione progressiva
```

Restano inoltre da verificare esplicitamente prima della chiusura:

```text
modello definitivo dei report e dei sottotipi
modello delle approvals e delle exceptions
modello delle baselines
catalogo completo delle entità minime
coerenza finale con la To-Do v0.8
```

La numerazione potrà essere estesa se questi temi richiedono decisioni autonome.

# 5. Stato del brief

Il brief precedente non viene promosso.

Dopo il completamento delle decisioni architetturali dovrà essere riscritto integralmente.

# 6. Stato operativo

```text
CHECKPOINT DOCUMENTALE v0.4 COMPLETATO
→ CONTINUIAMO
→ DEC-0101-019
```
