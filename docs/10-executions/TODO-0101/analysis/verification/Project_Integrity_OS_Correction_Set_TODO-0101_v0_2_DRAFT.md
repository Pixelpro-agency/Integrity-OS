# Project Integrity OS

## Correction Set — TODO-0101 — v0.2

**Stato:** DRAFT — correzioni incorporate nei documenti candidati  
**Data:** 2026-08-06  
**Ambito:** consolidamento completo delle decisioni `DEC-0101-001` → `DEC-0101-020`  
**Sostituisce:** `Project_Integrity_OS_Correction_Set_TODO-0101_v0_1_DRAFT.md`

---

# 1. Correzioni

```text
C-0101-001 — cardinalità strutturali vs lifecycle
C-0101-002 — ownership autorevole dei report
C-0101-003 — BUG nel registro comune
C-0101-004 — root project entity
C-0101-005 — cataloghi globali vs configurazioni locali
C-0101-006 — riferimenti globali senza FK cross-database
C-0101-007 — owner type canonici dei report
C-0101-008 — storico completo dei validation result
C-0101-009 — classificazione deterministica delle entità
```

Le correzioni raffinano le decisioni approvate e non ne cambiano gli obiettivi.

---

# 2. C-0101-001 — Cardinalità

Le cardinalità strutturali ammettono tutti gli stati validi.

I minimi dipendenti dal lifecycle sono transition requirements.

---

# 3. C-0101-002 — Report ownership

Ogni report possiede esattamente un owner autorevole.

```text
REPORT 1 ── 1 REPORT_OWNERSHIP
```

`report_subjects` aggiunge contesto e non modifica ownership.

---

# 4. C-0101-003 — BUG

`BUG` è parte del catalogo di `register_item_type` e possiede specializzazione 1:1.

---

# 5. C-0101-004 — Project root

```text
projects.project_id = project_entities.entity_id
```

Il project e la root entity vengono creati atomicamente.

---

# 6. C-0101-005 — Scope globali e locali

Scope logici:

```text
SYSTEM_CATALOG
GLOBAL_REGISTRY
PROJECT_DATABASE
```

Non si usa `project_id NULL` per distinguerli.

---

# 7. C-0101-006 — Binding globali

L'MVP usa due database fisici:

```text
CONTROL DATABASE
PROJECT DATABASE
```

SQLite non fornisce FK autorevoli tra database separati.

Ogni riferimento globale conserva:

```text
definition_code
catalog_version
definition_hash
```

e, quando serve una FK locale, un binding project-local.

Esempi:

- project actor bindings;
- role permission bindings;
- classification bindings;
- handling flag bindings;
- project template bindings;
- event type binding fields.

---

# 8. C-0101-007 — Owner report canonici

Mapping iniziale:

```text
EXECUTION_REPORT    → ATTEMPT
VERIFICATION_REPORT → VERIFICATION
VALIDATION_REPORT   → VALIDATION
INTEGRITY_REPORT    → INTEGRITY_RUN
RECOVERY_REPORT     → TRANSITION_RECOVERY_RUN
SECURITY_REPORT     → SECURITY_REVIEW
IMPORT_REPORT       → IMPORT_RECORD
EXPORT_REPORT       → EXPORT_RECORD
CLOSURE_REPORT      → target entity closed
DIAGNOSTIC_REPORT   → allowed governed entity
```

`report_owner_policies` governa i tipi ammessi.

---

# 9. C-0101-008 — Validation history

Il modello adotta:

```text
VALIDATION
→ VALIDATION_STEP
→ VALIDATION_STEP_RUN
→ VALIDATION_RESULT
```

Ogni retry crea un nuovo run.

I risultati sono append-only.

Lo stato corrente è derivato dall'ultimo run valido.

---

# 10. C-0101-009 — Entity classification

Ogni entità viene classificata esattamente come:

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

Non si usa la formula “può essere project entity”.

---

# 11. Documenti prodotti

```text
01 v0.2
02 v0.2
03 v0.2
04 v0.2
05 v0.2
06 v0.2
07 v0.2
08 v0.3
09 v0.2
10 v0.3
11 v0.2
12 v0.3
13 v0.2
14 v0.3
15 v0.3
README TODO-0101
Decision Log v0.7
Checkpoint Index v0.7
Open Issues Register v0.1
Brief v0.1 SUPERSEDED
```

---

# 12. Criteri di verifica

Il set è applicato quando:

- le versioni sostituite sono nello storico;
- soltanto le versioni correnti sono negli indici;
- il brief v0.1 è sotto `instructions/superseded`;
- README punta ai file correnti;
- nessun link corrente punta a versioni superate;
- non esistono FK concettuali cross-database;
- actors usano project actor binding;
- global definitions usano code/version/hash;
- report ownership è univoca e tipizzata;
- validation history conserva retry e risultati;
- entity classification è deterministica;
- `git diff --check` termina con exit code 0.

---

# 13. Stato dopo applicazione

```text
DECISIONAL CONSOLIDATION: COMPLETE
SCHEMA ARCHITECTURE: NOT YET PRODUCED
ENTITY CATALOG: NOT YET PRODUCED
FINAL BRIEF: NOT YET PRODUCED
IMPLEMENTATION: BLOCKED
```
