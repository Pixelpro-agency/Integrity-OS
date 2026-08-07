# Project Integrity OS

## Lifecycle delle decisioni — v0.2

**Stato:** DRAFT — modello consolidato, non ancora fonte autorevole
**Data:** 2026-08-06
**Task:** `TODO-0101`
**Decisioni:** `DEC-0101-012`, `DEC-0101-015`, `DEC-0101-017`, `DEC-0101-018`, `DEC-0101-019`
**Sostituisce:** `../history/decisions/Project_Integrity_OS_07_Lifecycle_Decisioni_v0_1_DRAFT.md`

---

# 1. Principio

```text
decidere
≠ risolvere
≠ rendere efficace
≠ attuare
≠ verificare
```

Ogni dimensione possiede stato e storico propri.

---

# 2. Entità

```text
decisions
decision_versions
decision_options
decision_inputs
decision_targets
decision_conditions
decision_resolutions
decision_implementation_links
decision_effects
```

---

# 3. Decisione logica

```text
decision_id
project_id
reference_code
decision_type
owner_actor_binding_id
scope_entity_id
criticality
reversibility
current_version_id
effective_version_id
record_state
created_at
closed_at
archived_at
```

Regole:

- `current_version_id` appartiene alla stessa decisione;
- `effective_version_id` appartiene alla stessa decisione;
- al massimo una versione è effective nello stesso intervallo;
- i pointer sono aggiornati soltanto tramite transizione atomica;
- integrity scan rileva divergenze.

---

# 4. Versioni

```text
decision_version_id
project_id
decision_id
version_number
problem_statement
context
decision_statement
rationale
consequences
assumptions
constraints
implementation_notes
review_requirements
effective_from
effective_until
content_hash
authoring_status
created_by_actor_binding_id
created_at
proposed_at
frozen_at
supersedes_decision_version_id
```

Una resolution riguarda una versione frozen esatta.

Una versione risolta non viene modificata.

---

# 5. Opzioni

```text
decision_option_id
project_id
decision_version_id
reference_code
title
description
benefits
costs
risks
constraints
estimated_impact
rejection_reason
sequence_number
created_at
```

Non esiste un campo autorevole `selected`.

La scelta è determinata esclusivamente dalla final resolution.

Le opzioni respinte restano nello storico.

---

# 6. Input

`decision_inputs` collega la decision version a entity/version risolvibili.

Ruoli:

```text
PRIMARY_BASIS
SUPPORTING
CONTRADICTING
CONSTRAINT
RISK_INPUT
HISTORICAL_CONTEXT
```

Fonti contraddittorie restano visibili.

---

# 7. Target

`decision_targets` punta a:

```text
target_entity_id
target_entity_version_id
impact_type
required
created_at
```

Tipi di impatto:

```text
CREATES
MODIFIES
CONSTRAINS
AUTHORIZES
BLOCKS
INVALIDATES
SUPERSEDES
DEPRECATES
REQUIRES_REVIEW
```

Il progetto è target tramite la propria root project entity.

---

# 8. Condizioni

Le condizioni non vengono conservate soltanto in JSON libero.

```text
decision_condition_id
project_id
decision_version_id
condition_code
description
required
blocking
derogable
owner_actor_binding_id
due_at
verification_method
status
resolved_by_entity_id
created_at
completed_at
```

Una condition può generare task, finding, requirement o transition requirement.

---

# 9. Dimensioni del lifecycle

## Authoring

```text
DRAFT
PROPOSED
UNDER_REVIEW
CHANGES_REQUESTED
READY_FOR_RESOLUTION
RESOLVED
WITHDRAWN
```

## Resolution

```text
PENDING
APPROVED
REJECTED
WITHDRAWN
```

## Effectiveness

```text
NOT_EFFECTIVE
SCHEDULED
EFFECTIVE
SUPERSEDED
REVOKED
EXPIRED
```

## Implementation

```text
NOT_APPLICABLE
NOT_STARTED
IN_PROGRESS
PARTIALLY_IMPLEMENTED
IMPLEMENTED
BLOCKED
FAILED
```

## Verification

```text
NOT_REQUIRED
NOT_VERIFIED
PARTIALLY_VERIFIED
VERIFIED
VERIFICATION_FAILED
STALE
```

---

# 10. Resolution

```text
decision_resolution_id
project_id
decision_version_id
resolution_type
selected_decision_option_id
rationale
approval_request_id
resolved_by_actor_binding_id
resolved_at
effective_from
expires_at
created_at
```

Vincoli:

- `selected_decision_option_id` appartiene alla stessa version;
- required quando la decisione seleziona una opzione;
- nullable con `single_option_reason` o per rejection/withdrawal;
- una sola final resolution attiva per version.

---

# 11. Implementation

`decision_implementation_links` collega la decision version a entità project-local o versioni esatte.

```text
decision_version_id
implementation_entity_id
implementation_entity_version_id
implementation_role
required
status
created_at
completed_at
```

Effective non implica implemented.

Implemented non implica verified.

---

# 12. Effetti

Ogni effetto materiale viene registrato:

```text
decision_effect_id
project_id
decision_version_id
effect_type
affected_entity_id
affected_entity_version_id
effect_status
event_id
created_at
```

Effetti:

- summary stale;
- Context Package stale;
- requirement da rivalutare;
- test coverage stale;
- task creata;
- document version richiesta;
- conflict generato;
- baseline da sostituire.

---

# 13. Conflitti

Un conflitto viene rilevato quando decisioni effective:

- governano target sovrapposti;
- hanno intervalli sovrapposti;
- producono regole incompatibili;
- non hanno relazione di supersession o eccezione valida.

Il conflitto genera un register item di tipo `CONFLICT`.

---

# 14. Decision Log

Il Decision Log è una summary navigabile.

Non è la fonte primaria.

Deve aprire:

```text
decision
→ version
→ options
→ inputs
→ targets
→ conditions
→ resolution
→ effects
→ implementation
→ verification
```

---

# 15. Decisione consolidata

```text
DEC-0101-012

La selezione di una option appartiene
alla final resolution, non alla option.

Le condizioni sono entità governate,
non soltanto JSON.

Input, target, implementation ed effects
puntano a project_entities ed entity_versions.

Current ed effective version pointer
sono protetti da transizioni e integrity rules.
```
