# Project Integrity OS

## Condizioni complete delle transizioni — v0.2

**Stato:** DRAFT — modello consolidato, non ancora fonte autorevole
**Data:** 2026-08-06
**Task:** `TODO-0101`
**Decisioni:** `DEC-0101-018`, `DEC-0101-015`, `DEC-0101-017`, `DEC-0101-019`, `DEC-0101-020`
**Correzioni:** `C-0101-001`, `C-0101-005`, `C-0101-006`, `C-0101-007`, `C-0101-009`
**Sostituisce:** `../history/decisions/Project_Integrity_OS_13_Transizioni_Condizioni_Complete_v0_1_DRAFT.md`

---

# 1. Principio

```text
un campo di stato governato
non viene aggiornato direttamente
```

Flusso:

```text
named action
→ transition request
→ authorization
→ evaluation
→ atomic commit
→ event
→ effect execution
→ postcondition verification
```

---

# 2. Catalogo globale e definizioni locali

## System catalog

```text
transition_templates
```

Ogni template possiede code, catalog version e definition hash.

## Project database

```text
transition_definitions
transition_definition_versions
transition_requirements
transition_effects
transition_requests
transition_evaluations
transition_evaluation_results
transition_executions
transition_effect_results
transition_compensations
transition_recovery_runs
transition_policy_bindings
```

Una transition definition è project-local, una project entity e può derivare da un template globale tramite binding.

---

# 3. Versione della transizione

Conserva:

- action code;
- target entity type;
- source state;
- target state;
- required permission binding;
- role constraints;
- separation of duties;
- approval policy version;
- integrity profile version;
- concurrency strategy;
- idempotency;
- atomicity scope;
- requirements;
- effects;
- postconditions;
- compensation;
- effective period;
- content hash.

L'esecuzione conserva la versione esatta.

---

# 4. Requirement types

```text
ENTITY_STATE
RELATED_ENTITY_EXISTS
RELATED_ENTITY_STATE
REQUIRED_VERSION
REQUIRED_DOCUMENT
REQUIRED_CONTEXT_PACKAGE
REQUIRED_REQUIREMENT_COVERAGE
REQUIRED_TEST_RESULT
REQUIRED_VERIFICATION
REQUIRED_VALIDATION
REQUIRED_APPROVAL
REQUIRED_INTEGRITY_PROFILE
NO_BLOCKING_REGISTER_ITEM
NO_OPEN_CONFLICT
NO_BLOCKING_BUG
DEPENDENCY_SATISFIED
AUTHORIZATION
SEPARATION_OF_DUTIES
TEMPORAL
CONTENT_AVAILABLE
REPOSITORY_STATE
BASELINE_COMPATIBILITY
CUSTOM_DETERMINISTIC_RULE
```

Classi:

```text
INVARIANT
POLICY_REQUIRED
ADVISORY
```

Ogni requirement indica mandatory, derogable, blocking, evaluation method, failure code e remediation.

---

# 5. Request

```text
transition_request_id
project_id
reference_code
target_entity_id
target_entity_version_id
transition_definition_version_id
expected_current_state
requested_target_state
expected_aggregate_sequence
requested_by_actor_binding_id
actor_session_id
delegation_id
reason
payload_json
idempotency_key
correlation_id
expires_at
status
created_at
```

Il target è una project entity esatta.

---

# 6. Evaluation

Ogni evaluation congela:

- transition version;
- integrity profile version;
- access policy version;
- approval policy version;
- repository snapshot;
- state snapshot;
- baseline version;
- target hash;
- result hash.

Risultati:

```text
PASSED
FAILED
WARNING
BLOCKED
NOT_APPLICABLE
NOT_EVALUATED
TECHNICAL_FAILURE
OVERRIDDEN_BY_EXCEPTION
```

Esito:

```text
ELIGIBLE
ELIGIBLE_WITH_WARNINGS
ELIGIBLE_WITH_EXCEPTIONS
NOT_ELIGIBLE
BLOCKED
INDETERMINATE
TECHNICAL_FAILURE
```

---

# 7. Lifecycle operativo

```text
REQUESTED
AUTHORIZING
EVALUATING
READY_TO_COMMIT
COMMITTING
COMMITTED
VERIFYING_EFFECTS
COMPLETED
```

Altri esiti:

```text
DENIED
BLOCKED
CANCELLED
FAILED
PARTIALLY_EFFECTIVE
RECOVERY_REQUIRED
SUPERSEDED
```

---

# 8. Concorrenza e idempotenza

Prima del commit:

```text
expected state
expected aggregate sequence
target hash
session
permission
membership
exception
blocker
versions
```

Divergenza:

```text
CONCURRENT_MODIFICATION
```

Idempotency conflict quando stessa chiave usa payload differente.

---

# 9. Atomicità

Nella stessa transazione:

- recheck;
- state update;
- required relations;
- transition execution;
- event;
- aggregate sequence.

Gli effetti esterni usano journal e manifest.

---

# 10. Effects e recovery

Effect states:

```text
PENDING
RUNNING
COMPLETED
FAILED
TECHNICAL_FAILURE
COMPENSATED
UNRECOVERABLE
```

Compensation:

```text
DATABASE_ROLLBACK
COMPENSATING_TRANSITION
MANUAL_RECOVERY
IRREVERSIBLE
```

`transition_recovery_runs` è una project entity.

Un `RECOVERY_REPORT` possiede come owner autorevole un `TRANSITION_RECOVERY_RUN`.

---

# 11. Postconditions

Controlli:

- final state;
- event;
- sequences;
- mandatory relations;
- external effects;
- hashes;
- projections;
- integrity profile;
- aggregate consistency;
- report ownership;
- root project identity quando coinvolta.

Fallimento materiale produce finding e `RECOVERY_REQUIRED`.

---

# 12. Profili

## PROJECT_ACTIVATION_PROFILE

- root project entity;
- control registry binding;
- membership;
- owner;
- schema;
- policy iniziali;
- nessuna fatal violation;
- baseline o eccezione.

## TASK_READY_PROFILE

- gerarchia;
- objective e scope;
- Task Contract frozen;
- requirements e criteria;
- dependencies;
- decisions;
- nessun register item bloccante non risolto;
- Context Package generabile;
- executor assegnabile.

## ATTEMPT_START_PROFILE

- task ed execution valide;
- attempt policy;
- prompt frozen;
- Context Package frozen;
- snapshot;
- authorization;
- executor binding;
- nessun blocker critico.

## VERIFICATION_PASS_PROFILE

- report owned correttamente;
- reconciliation;
- evidence;
- test obbligatori;
- commit e baseline;
- conflict risolti;
- nessun finding bloccante non risolto;
- assumption critiche non smentite;
- integrity;
- verifier autorizzato;
- separation of duties.

## TASK_COMPLETION_PROFILE

- final attempt;
- verification passed;
- validation prevista;
- requirements verified;
- criteria passed;
- bug e finding gestiti;
- question risolte o non bloccanti;
- risks gestiti;
- decisioni attuate;
- documentazione;
- approval;
- versione verificata coerente;
- nessuna fatal violation.

---

# 13. Lifecycle canonici

## Project

```text
DRAFT
INITIALIZING
ACTIVE
SUSPENDED
CLOSING
CLOSED
ARCHIVED
PENDING_DELETION
TOMBSTONED
```

## Phase e work item

```text
DRAFT
PLANNED
READY
IN_PROGRESS
BLOCKED
IN_VERIFICATION
COMPLETED
DEFERRED
CANCELLED
ARCHIVED
```

## Task

```text
DRAFT
DEFINED
READY
IN_EXECUTION
BLOCKED
IN_VERIFICATION
COMPLETED
DEFERRED
CANCELLED
ARCHIVED
```

## Task execution

```text
PLANNED
READY
ACTIVE
PAUSED
BLOCKED
AWAITING_VERIFICATION
COMPLETED
FAILED
CANCELLED
SUPERSEDED
```

## Attempt

```text
PLANNED
READY
IN_PROGRESS
AWAITING_REPORT
REPORTED
RECONCILING
IN_VERIFICATION
VERIFIED_PASSED
VERIFIED_FAILED
TECHNICAL_FAILURE
ABORTED
CANCELLED
SUPERSEDED
```

## Verification

```text
DRAFT
PLANNED
READY
IN_PROGRESS
BLOCKED
PASSED
FAILED
INCONCLUSIVE
SUPERSEDED
REVOKED
```

## Baseline

```text
DRAFT
BUILDING
VALIDATING
READY_FOR_APPROVAL
APPROVED
EFFECTIVE
SUPERSEDED
REVOKED
ARCHIVED
```

---

# 14. Batch

```text
ALL_OR_NOTHING
BEST_EFFORT
SEQUENTIAL_STOP_ON_FAILURE
```

Il manifest contiene UUID, version, expected state, sequence e hash.

---

# 15. Decisione consolidata

```text
DEC-0101-018

Transition templates sono globali.
Transition definitions sono project-local.

Target, versioni, actors, permissions
e catalog bindings sono risolvibili
senza FK cross-database.

I profili richiedono assenza di blocker
applicabili, non assenza assoluta di finding.

Recovery run è una entity canonica
e può essere owner di recovery report.
```
