# Project Integrity OS

## Decision Log preliminare — TODO-0101 — v0.3

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
DEC-0101-006 — Phases, work_items, tasks, executions, attempts
DEC-0101-007 — Contesto dal macroscopico al microscopico
DEC-0101-008 — Context Package versionati e riproducibili
DEC-0101-009 — Provenienza multidimensionale
DEC-0101-010 — Sintesi, drill-down e obsolescenza
DEC-0101-011 — Requisiti, criteri e copertura dei test
DEC-0101-012 — Lifecycle multidimensionale delle decisioni
DEC-0101-013 — Registri degli elementi irrisolti
DEC-0101-014 — Eventi e ricostruzione temporale
DEC-0101-015 — Integrità trasversale e anti-orfano
```

---

# 2. Decisioni aggiunte nel checkpoint v0.3

## DEC-0101-012 — APPROVED

La decisione logica è distinta da versioni, alternative, input, target, risoluzioni, efficacia, attuazione e verifica.

```text
APPROVED
≠ EFFECTIVE
≠ IMPLEMENTED
≠ VERIFIED
```

## DEC-0101-013 — APPROVED

Open question, assumption, risk, finding e conflict condividono una identità comune, ma mantengono lifecycle e campi specializzati.

Gli elementi cambiano natura creando nuovi record collegati.

## DEC-0101-014 — APPROVED

Il modello temporale combina:

```text
stato corrente
+
event journal append-only
+
versioni immutabili
+
state snapshot
+
baseline
```

Supporta `AS_KNOWN_AT`, `AS_EFFECTIVE_AT` e `AS_BASELINED`.

## DEC-0101-015 — APPROVED

Il Context Graph usa `project_entities` e `entity_versions`.

Le relazioni generiche usano foreign key reali.

Le regole di integrità sono versionate, raggruppate in profili e valutate tramite run tracciabili.

---

# 3. Documenti inclusi

## Checkpoint iniziale

```text
Project_Integrity_OS_Principi_Tracciabilita_Contesto_v0_1_DRAFT.md
Project_Integrity_OS_Modello_Gerarchico_Contesto_v0_1_DRAFT.md
Project_Integrity_OS_Context_Package_v0_1_DRAFT.md
```

## Checkpoint v0.2

```text
Project_Integrity_OS_Provenienza_Informazioni_v0_1_DRAFT.md
Project_Integrity_OS_Sintesi_Drill_Down_v0_1_DRAFT.md
Project_Integrity_OS_Requisiti_Test_Tracciabilita_v0_1_DRAFT.md
```

## Checkpoint v0.3

```text
Project_Integrity_OS_Lifecycle_Decisioni_v0_1_DRAFT.md
Project_Integrity_OS_Registro_Elementi_Irrisolti_v0_1_DRAFT.md
Project_Integrity_OS_Eventi_Ricostruzione_Temporale_v0_1_DRAFT.md
Project_Integrity_OS_Integrita_Trasversale_Anti_Orfano_v0_1_DRAFT.md
```

---

# 4. Decisioni ancora aperte

```text
DEC-0101-016 — Cancellazione, archiviazione e rettifiche
DEC-0101-017 — Ruoli, permessi, sensibilità e redazione
DEC-0101-018 — Condizioni complete delle transizioni
DEC-0101-019 — Cardinalità definitive e tabelle associative
DEC-0101-020 — Confine tra schema completo e implementazione progressiva
```

La numerazione può essere estesa se emergono ulteriori decisioni necessarie.

---

# 5. Stato del brief

Il brief precedente non deve essere promosso ad `ACTIVE`.

Dopo la conclusione dell’allineamento dovrà essere riscritto integralmente sulla base delle decisioni approvate.

---

# 6. Stato operativo

```text
CHECKPOINT DOCUMENTALE v0.3 COMPLETATO
→ CONTINUIAMO
→ DEC-0101-016
```
