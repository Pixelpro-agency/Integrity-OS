# Project Integrity OS

## Registro degli elementi irrisolti — v0.3

**Stato:** DRAFT — modello consolidato, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task:** `TODO-0101`  
**Decisioni:** `DEC-0101-013`, `DEC-0101-015`, `DEC-0101-018`, `DEC-0101-019`  
**Correzioni:** `C-0101-003`, `C-0101-007`, `C-0101-009`  
**Sostituisce:** `Project_Integrity_OS_08_Registro_Elementi_Irrisolti_TODO-0101_v0_2_DRAFT.md`

---

# 1. Principio

Open question, assumption, risk, finding, conflict e bug sono tipi distinti con radice comune.

Una trasformazione non modifica silenziosamente il tipo originario.

```text
FINDING
→ GENERATED
→ BUG
```

Il finding resta un finding.

---

# 2. Catalogo

```text
OPEN_QUESTION
ASSUMPTION
RISK
FINDING
CONFLICT
BUG
```

---

# 3. Entità

```text
register_items
register_item_versions
register_item_links

open_questions
assumptions
risks
findings
conflicts
bugs
```

Ogni register item è una `project_entity`.

Ogni register item possiede esattamente una specializzazione coerente con il tipo.

---

# 4. Identità

```text
register_item_id
project_id
reference_code
register_item_type
current_version_id
lifecycle_status
owner_actor_binding_id
severity
priority
criticality
blocking
due_at
created_at
closed_at
archived_at
```

`current_version_id` viene aggiornato soltanto tramite transizione e deve appartenere allo stesso item.

---

# 5. Versioni

```text
register_item_version_id
project_id
register_item_id
version_number
title
description
rationale
resolution_summary
content_hash
version_status
created_by_actor_binding_id
created_at
frozen_at
supersedes_register_item_version_id
```

La creazione dell'item e della prima version avviene nella stessa transazione.

Una version frozen è immutabile.

---

# 6. Specializzazioni

## Open question

```text
question_type
answer_required_from_actor_binding_id
decision_deadline
answer_status
```

## Assumption

```text
assumption_basis
confidence_level
validation_required
invalidated_at
```

## Risk

```text
likelihood
impact
exposure
mitigation_strategy
acceptance_status
```

## Finding

```text
finding_type
observation_method
affected_scope_entity_id
disposition
```

## Conflict

```text
conflict_type
resolution_method
resolution_status
```

Le affermazioni confliggenti usano relazioni a provenance records o entity versions, non testo autorevole duplicato.

## Bug

```text
bug_type
reproduction_status
affected_component
introduced_in_entity_version_id
fixed_in_entity_version_id
regression_test_required
regression_test_status
disposition
```

---

# 7. Relazioni dedicate del bug

```text
bug_findings
bug_tasks
bug_requirements
bug_acceptance_criteria
bug_test_definitions
bug_test_runs
bug_evidence
bug_verifications
```

Le relazioni fondamentali puntano a identità o versioni esatte secondo la semantica.

`register_item_links` non le sostituisce.

---

# 8. Link supplementari

```text
DERIVED_FROM
GENERATED
DUPLICATES
CONTRADICTS
INVALIDATES
MITIGATES
RESOLVES
BLOCKS
AFFECTS
RELATED_TO
```

Niente self-link salvo tipo esplicitamente ammesso.

---

# 9. Lifecycle

Lifecycle comune:

```text
DRAFT
OPEN
TRIAGED
IN_PROGRESS
BLOCKED
READY_FOR_REVIEW
RESOLVED
CLOSED
DEFERRED
REJECTED
SUPERSEDED
REOPENED
ARCHIVED
```

Lifecycle specifici possono restringere o estendere il catalogo tramite transition definitions.

---

# 10. Blocking

Un item blocca una transizione quando:

```text
blocking = true
```

e la policy applicabile lo considera rilevante per target, stato e periodo.

Una eccezione valida produce:

```text
OVERRIDDEN_BY_EXCEPTION
```

non `PASSED`.

---

# 11. Regole

- type e specializzazione coerenti;
- una sola specializzazione;
- BUG presente nel catalogo;
- nessun cambio silenzioso di tipo;
- reference code non riciclato;
- version frozen immutabile;
- project boundary rispettato;
- owner tramite project actor binding;
- bug chiuso con verification e regression test quando richiesto.

---

# 12. Decisione consolidata

```text
DEC-0101-013

Register items è la radice comune per:

OPEN_QUESTION
ASSUMPTION
RISK
FINDING
CONFLICT
BUG.

Ogni item è una project entity,
possiede versioni e una sola specializzazione.

I riferimenti a versioni introdotte o corrette
usano entity_versions, non testo libero.
```
