# Project Integrity OS

## Registro degli elementi irrisolti — v0.2

**Stato:** DRAFT — modello corretto e consolidato  
**Data:** 2026-08-06  
**Task:** `TODO-0101`  
**Decisione primaria:** `DEC-0101-013`  
**Correzione applicata:** `C-0101-003`  
**Sostituisce:** `Project_Integrity_OS_08_Registro_Elementi_Irrisolti_TODO-0101_v0_1_DRAFT.md`

---

# 1. Principio

Domande aperte, assunzioni, rischi, finding, conflitti e bug sono elementi distinti.

Non vengono trasformati modificando silenziosamente il tipo del record originario.

```text
un fatto osservato
può generare un nuovo elemento governato
collegato alla propria origine
```

---

# 2. Catalogo canonico

`register_item_type` ammette:

```text
OPEN_QUESTION
ASSUMPTION
RISK
FINDING
CONFLICT
BUG
```

`BUG` è formalmente parte del registro comune.

---

# 3. Struttura

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

## `register_items`

Contiene i campi condivisi:

```text
register_item_id
project_id
reference_code
register_item_type
current_version_id
lifecycle_status
owner_actor_id
severity
priority
criticality
blocking
due_at
created_at
closed_at
archived_at
```

Ogni record possiede una sola specializzazione coerente con `register_item_type`.

## `register_item_versions`

Conserva il contenuto versionato:

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
created_at
frozen_at
supersedes_version_id
```

Le versioni citate da baseline, decisioni, verifiche o Context Package sono immutabili.

---

# 4. Cardinalità strutturali

```text
PROJECT 1 ── 0..N REGISTER_ITEMS
REGISTER_ITEM 1 ── 1..N REGISTER_ITEM_VERSIONS
REGISTER_ITEM 1 ── 1 SPECIALIZED REGISTER RECORD
REGISTER_ITEM N ── M REGISTER_ITEM tramite REGISTER_ITEM_LINKS
```

Il record logico e la prima versione vengono creati nella stessa transazione.

---

# 5. Specializzazioni

## Open question

Campi specifici:

```text
question_type
answer_required_from
decision_deadline
answer_status
```

## Assumption

```text
assumption_basis
confidence
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
affected_scope
disposition
```

## Conflict

```text
conflict_type
conflicting_claims
resolution_method
resolution_status
```

## Bug

```text
bug_type
reproduction_status
affected_component
introduced_in_version
fixed_in_version
regression_test_required
regression_test_status
disposition
```

Un bug chiuso richiede una verifica e, quando applicabile, un test di regressione.

---

# 6. Relazioni e trasformazioni

Tipi iniziali di `register_item_links`:

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

Esempio corretto:

```text
FINDING-001
→ GENERATED
→ BUG-001
```

Il finding resta un finding.

Il bug è un nuovo register item con identità e lifecycle propri.

---

# 7. Collegamenti dedicati del bug

Le relazioni fondamentali usano tabelle dedicate:

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

`register_item_links` non sostituisce queste relazioni autorevoli.

---

# 8. Lifecycle

Lifecycle comune minimo:

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

Le specializzazioni possono restringere o estendere gli stati.

Esempio bug:

```text
OPEN
→ TRIAGED
→ CONFIRMED
→ IN_REMEDIATION
→ READY_FOR_VERIFICATION
→ VERIFIED
→ CLOSED
```

---

# 9. Blocking

Un register item può impedire una transizione soltanto quando:

```text
blocking = true
```

e la policy applicabile lo considera rilevante per il target.

La chiusura del figlio non chiude automaticamente il parent.

Una eccezione valida può derogare una regola derogabile, ma il record resta visibile come elemento coperto da eccezione.

---

# 10. Regole di integrità

```text
register_item_type coerente con la specializzazione;

una sola specializzazione per register item;

BUG presente nel catalogo;

nessun cambio silenzioso di tipo;

reference_code non riciclato;

versione frozen immutabile;

project_id coerente in ogni relazione;

nessun self-link salvo tipo esplicitamente ammesso;

relazioni fondamentali rappresentate da tabelle dedicate;

bug chiuso con verifica e regression test quando richiesto.
```

---

# 11. Decisione consolidata

```text
DEC-0101-013 + C-0101-003

Project Integrity OS usa register_items come radice
comune per:

OPEN_QUESTION
ASSUMPTION
RISK
FINDING
CONFLICT
BUG.

Ogni tipo possiede una specializzazione 1:1.

Le trasformazioni generano nuovi elementi collegati
e non riscrivono il tipo dell'origine.

I bug condividono ownership, priorità, severità,
blocking, versioni e storico con il registro comune,
mantenendo campi e lifecycle specifici.
```
