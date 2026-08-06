# Project Integrity OS

## Requisiti, criteri di accettazione e copertura dei test — v0.2

**Stato:** DRAFT — modello consolidato, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task:** `TODO-0101`  
**Decisioni:** `DEC-0101-004`, `DEC-0101-011`, `DEC-0101-015`, `DEC-0101-018`, `DEC-0101-019`  
**Correzioni:** `C-0101-001`, `C-0101-008`  
**Sostituisce:** `Project_Integrity_OS_06_Requisiti_Test_Tracciabilita_TODO-0101_v0_1_DRAFT.md`

---

# 1. Catena canonica

```text
OBJECTIVE
→ REQUIREMENT_VERSION
→ ACCEPTANCE_CRITERION_VERSION
→ TEST_DEFINITION_VERSION
→ TEST_RUN
→ TEST_RUN_RESULT
→ EVIDENCE
→ VERIFICATION
→ VALIDATION
→ APPROVAL
```

I concetti restano distinti.

```text
implemented ≠ verified
test declared ≠ test observed
verification ≠ validation
approval ≠ pass
```

---

# 2. Entità

```text
objectives
objective_requirements

requirements
requirement_versions
requirement_scopes
requirement_dependencies

acceptance_criteria
acceptance_criterion_versions
requirement_acceptance_criteria

test_definitions
test_definition_versions
acceptance_criterion_test_definitions

test_environments
test_runs
test_run_results
test_run_command_runs
test_run_evidence

verifications
verification_criteria
verification_results
verification_evidence

validations
validation_steps
validation_step_runs
validation_results
validation_evidence
```

---

# 3. Objectives

```text
objective_id
project_id
reference_code
root_scope_entity_id
title
description
priority
status
source_decision_version_id
created_at
archived_at
```

Un objective appartiene a un root scope project-local.

La relazione con requirements è N:M tramite `objective_requirements`.

---

# 4. Requirements

## Identità

```text
requirement_id
project_id
reference_code
current_version_id
record_state
criticality
created_at
archived_at
```

## Versione

```text
requirement_version_id
project_id
requirement_id
version_number
title
statement
requirement_type
priority
rationale
verification_method
authoring_status
content_hash
created_at
approved_at
frozen_at
supersedes_requirement_version_id
```

Tipi iniziali:

```text
FUNCTIONAL
NON_FUNCTIONAL
DATA
SECURITY
PERFORMANCE
RELIABILITY
USABILITY
COMPATIBILITY
COMPLIANCE
DOCUMENTATION
OPERATIONAL
```

Una versione approvata è immutabile.

---

# 5. Scope e dipendenze

`requirement_scopes` collega la requirement version a una o più project entity.

```text
requirement_version_id
scope_entity_id
scope_role
required
created_at
```

`requirement_dependencies` usa versioni esatte quando il vincolo è congelato.

Tipi:

```text
DEPENDS_ON
REFINES
CONFLICTS_WITH
DUPLICATES
SUPERSEDES
CONSTRAINS
```

---

# 6. Acceptance criteria

## Identità

```text
acceptance_criterion_id
project_id
reference_code
current_version_id
record_state
blocking
created_at
archived_at
```

## Versione

```text
acceptance_criterion_version_id
project_id
acceptance_criterion_id
version_number
title
description
expected_result
criterion_type
priority
verification_method
authoring_status
content_hash
created_at
approved_at
frozen_at
supersedes_acceptance_criterion_version_id
```

Tipi:

```text
AUTOMATED_TEST
MANUAL_VALIDATION
STATIC_CHECK
REPOSITORY_INSPECTION
DOCUMENT_REVIEW
DATA_INTEGRITY_CHECK
PERFORMANCE_THRESHOLD
SECURITY_CHECK
COMPOSITE
```

La relazione requirement-criterion è N:M e usa versioni esatte nei contratti congelati.

---

# 7. Test definitions

## Identità

```text
test_definition_id
project_id
reference_code
current_version_id
record_state
created_at
archived_at
```

## Versione

```text
test_definition_version_id
project_id
test_definition_id
version_number
title
description
test_type
procedure
expected_result
automation_status
command_template
working_directory_template
timeout_ms
environment_requirements_json
input_definition_json
output_expectations_json
authoring_status
content_hash
created_at
approved_at
frozen_at
supersedes_test_definition_version_id
```

Ogni test run punta a una `test_definition_version_id` esatta.

---

# 8. Copertura pianificata

`acceptance_criterion_test_definitions` registra:

```text
acceptance_criterion_version_id
test_definition_version_id
coverage_type
mandatory
minimum_required_runs
required_result
applicable_environment
scenario_type
created_at
```

Scenario:

```text
POSITIVE
NEGATIVE
BOUNDARY
FAILURE
RECOVERY
REGRESSION
```

La copertura pianificata non prova l'esecuzione.

---

# 9. Test runs

```text
test_run_id
project_id
reference_code
test_definition_version_id
attempt_id
repository_snapshot_id
test_environment_id
status
started_at
completed_at
duration_ms
exit_code
observed_result_json
stdout_hash
stderr_hash
executed_by_actor_binding_id
created_at
```

Stati:

```text
SCHEDULED
RUNNING
PASSED
FAILED
BLOCKED
NOT_RUN
CANCELLED
TECHNICAL_FAILURE
INCONCLUSIVE
```

`FAILED` e `TECHNICAL_FAILURE` sono distinti.

Un test run può usare più command run tramite:

```text
test_run_command_runs
```

Ruoli:

```text
SETUP
PRIMARY
SUPPORTING
TEARDOWN
DIAGNOSTIC
```

---

# 10. Test run results

```text
test_run_result_id
project_id
test_run_id
assertion_reference
expected_value_json
observed_value_json
status
difference_json
sequence_number
created_at
```

Stati:

```text
PASSED
FAILED
NOT_EVALUATED
INCONCLUSIVE
NOT_APPLICABLE
```

Una run conclusa richiede almeno un risultato conclusivo o una motivazione esplicita per un test senza asserzioni separate.

---

# 11. Evidence

I test run usano N:M evidence tramite `test_run_evidence`.

Ruoli:

```text
PRIMARY_RESULT
SUPPORTING_OUTPUT
FAILURE_DETAIL
ENVIRONMENT_PROOF
REGRESSION_PROOF
```

Un risultato dichiarato passato senza evidence obbligatoria resta incompleto.

---

# 12. Verification

Una verification possiede:

```text
verification_id
project_id
reference_code
primary_subject_entity_id
verification_type
status
created_at
completed_at
```

Relazioni:

```text
verification_subjects
verification_criteria
verification_results
verification_evidence
verification_reconciliations
```

Minimi di transizione:

```text
VERIFICATION → READY
richiede almeno un criterio

VERIFICATION → PASSED/FAILED
richiede risultati per tutti i criteri obbligatori
```

---

# 13. Validation

La validation funzionale resta distinta dalla verification tecnica.

```text
VALIDATION 1 ── 0..N VALIDATION_STEPS
VALIDATION_STEP 1 ── 0..N VALIDATION_STEP_RUNS
VALIDATION_STEP_RUN 1 ── 1..N VALIDATION_RESULTS
```

## `validation_steps`

Definisce procedura e atteso.

## `validation_step_runs`

Rappresenta ogni esecuzione o retry:

```text
validation_step_run_id
project_id
validation_step_id
run_number
environment_id
performed_by_actor_binding_id
status
started_at
completed_at
created_at
```

Vincolo:

```text
UNIQUE(validation_step_id, run_number)
```

## `validation_results`

Conserva risultati append-only del run.

Il risultato corrente di uno step è derivato dall'ultimo run concluso valido, non da un campo sovrascritto.

---

# 14. Planned e observed coverage

Planned coverage:

```text
quali test e validation sono richiesti
```

Observed coverage:

```text
quali run sono stati realmente eseguiti
con quali versioni, ambienti, risultati ed evidence
```

Stati:

```text
NOT_DEFINED
PLANNED
PARTIALLY_COVERED
FULLY_COVERED
EXECUTED
PARTIALLY_VERIFIED
VERIFIED
FAILED
BLOCKED
STALE
```

---

# 15. Obsolescenza

La copertura può diventare `STALE` quando cambia:

- requirement version;
- criterion version;
- test definition version;
- codice o repository snapshot;
- ambiente;
- baseline;
- decisione applicabile;
- dipendenza;
- policy.

Un test passato non resta automaticamente valido per una versione differente.

---

# 16. Bug e regressione

Catena:

```text
BUG
→ corrective TASK
→ REQUIREMENT_VERSION
→ ACCEPTANCE_CRITERION_VERSION
→ REGRESSION TEST_DEFINITION_VERSION
→ TEST_RUN
→ EVIDENCE
→ VERIFICATION
```

Un bug chiuso richiede regression test quando applicabile o eccezione approvata.

---

# 17. Blocco della chiusura

Una task non può completarsi quando:

- un requirement bloccante non è verified;
- un criterion bloccante è failed;
- un test obbligatorio non è eseguito;
- manca evidence obbligatoria;
- la copertura è stale;
- manca una validation obbligatoria;
- esiste un mismatch non risolto;
- la versione verificata differisce da quella candidata alla approval.

---

# 18. Decisione consolidata

```text
DEC-0101-011
C-0101-001
C-0101-008

Requirements, acceptance criteria
e test definitions possiedono
identità logiche e versioni immutabili.

Ogni test run punta a una versione esatta.

Command run e test run sono collegati N:M.

Validation steps, step runs e results
conservano tutti i retry e lo storico.

Planned coverage e observed coverage
restano distinte.
```
