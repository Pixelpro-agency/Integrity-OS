# Project Integrity OS

## Requisiti, criteri di accettazione e copertura dei test — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task collegata:** `TODO-0101 — Definire schema dati minimo`  
**Decisione collegata:** `DEC-0101-011 — APPROVED`  
**Ambito:** obiettivi, requisiti, criteri, test, evidenze, collaudi e tracciabilità

---

# 1. Scopo

Project Integrity OS deve impedire che:

- gli obiettivi restino vaghi;
- le task siano prive di criteri misurabili;
- esistano test senza requisito;
- un requisito venga dichiarato soddisfatto senza prova;
- un test eseguito non sia pertinente;
- una task venga chiusa con controlli mancanti;
- un bug venga corretto senza protezione di regressione.

Catena minima:

```text
obiettivo
→ requisito
→ criterio di accettazione
→ definizione del test
→ esecuzione del test
→ risultato
→ evidenza
→ verifica
→ collaudo
→ approvazione
```

---

# 2. Concetti distinti

## 2.1 Obiettivo

Descrive il risultato generale desiderato.

## 2.2 Requisito

Descrive una condizione che deve essere soddisfatta.

## 2.3 Criterio di accettazione

Definisce come stabilire se un requisito è soddisfatto.

## 2.4 Definizione del test

Descrive procedura, input, ambiente e risultato atteso.

## 2.5 Test run

Rappresenta una specifica esecuzione del test.

## 2.6 Risultato del test

Confronta valore atteso e osservato.

## 2.7 Evidenza

Conserva il materiale osservato.

## 2.8 Verifica

Determina se test ed evidenze soddisfano il criterio.

## 2.9 Collaudo

Conferma il comportamento funzionale quando richiesto.

## 2.10 Approvazione

Autorizza una decisione o chiusura.

Questi concetti non devono essere compressi in:

```text
passed = true
```

---

# 3. Entità concettuali

```text
objectives
requirements
acceptance_criteria
test_definitions
test_runs
test_run_results
validations
validation_steps
validation_results
```

Relazioni:

```text
objective_requirements
requirement_dependencies
requirement_acceptance_criteria
acceptance_criterion_test_definitions
test_run_evidence
verification_acceptance_criteria
validation_acceptance_criteria
```

---

# 4. Objectives

Gli obiettivi possono appartenere a:

```text
PROJECT
PHASE
WORK_ITEM
TASK
```

Campi:

```text
objective_id
project_id
reference_code
owner_entity_type
owner_entity_id
title
description
priority
status
source_decision_id
source_document_version_id
created_at
updated_at
archived_at
```

Un obiettivo può generare più requisiti.

---

# 5. Requirements

Campi concettuali:

```text
requirement_id
project_id
reference_code
title
statement
requirement_type
priority
status
source_type
source_entity_id
rationale
verification_method
criticality
created_at
updated_at
approved_at
supersedes_requirement_id
```

## 5.1 Tipi

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

## 5.2 Stati

```text
DRAFT
PROPOSED
APPROVED
IN_IMPLEMENTATION
IMPLEMENTED
IN_VERIFICATION
VERIFIED
PARTIALLY_SATISFIED
FAILED
DEFERRED
SUPERSEDED
REJECTED
```

`IMPLEMENTED` non significa `VERIFIED`.

---

# 6. Origine del requisito

Fonti:

```text
ANALYSIS
DECISION
DOCUMENT_VERSION
USER_NEED
BUG
RISK
REGULATION
WORK_ITEM
TASK
VALIDATION_FINDING
VERIFICATION_FINDING
```

Un requisito senza origine risolvibile deve risultare incompleto.

---

# 7. Atomicità e qualità

Un requisito deve essere sufficientemente specifico da essere verificabile.

Esempio non valido:

```text
Il database deve essere robusto.
```

Esempi atomici:

```text
Le foreign key sono abilitate per ogni connessione.

Una migrazione fallita non lascia lo schema parzialmente applicato.

La riapertura conserva i record confermati.
```

Il sistema deve poter segnalare:

```text
AMBIGUOUS
COMPOUND
NOT_TESTABLE
CONFLICTING
```

Un requisito con questi problemi non deve diventare `APPROVED` senza revisione.

---

# 8. Relazioni tra requisiti

```text
DEPENDS_ON
REFINES
CONFLICTS_WITH
DUPLICATES
SUPERSEDES
CONSTRAINS
```

Una dipendenza obbligatoria fallita impedisce di dichiarare soddisfatto il requisito dipendente.

---

# 9. Acceptance criteria

Campi:

```text
acceptance_criterion_id
project_id
reference_code
title
description
expected_result
criterion_type
priority
blocking
status
verification_method
created_at
updated_at
approved_at
supersedes_acceptance_criterion_id
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

Stati:

```text
DRAFT
APPROVED
READY_FOR_VERIFICATION
PASSED
FAILED
PARTIALLY_PASSED
BLOCKED
NOT_RUN
NOT_APPLICABLE
SUPERSEDED
```

L’esecutore non imposta direttamente il criterio a `PASSED`.

---

# 10. Relazione requisiti-criteri

```text
requirements N ── N acceptance_criteria
```

La relazione registra:

```text
requirement_id
acceptance_criterion_id
coverage_role
required
created_at
```

Ruoli:

```text
PRIMARY
SUPPORTING
REGRESSION
NEGATIVE_CASE
BOUNDARY_CASE
```

---

# 11. Test definitions

Campi:

```text
test_definition_id
project_id
reference_code
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
status
version
content_hash
created_at
approved_at
frozen_at
supersedes_test_definition_id
```

Tipi:

```text
UNIT
INTEGRATION
CONTRACT
MIGRATION
PERSISTENCE
REGRESSION
END_TO_END
STATIC_ANALYSIS
BUILD
MANUAL
SMOKE
SECURITY
PERFORMANCE
RECOVERY
```

Automazione:

```text
AUTOMATED
MANUAL
HYBRID
NOT_AUTOMATABLE
```

Una definizione usata in un tentativo viene congelata.

---

# 12. Copertura criteri-test

```text
acceptance_criteria N ── N test_definitions
```

Campi:

```text
acceptance_criterion_id
test_definition_id
coverage_type
mandatory
minimum_required_runs
required_result
applicable_environment
created_at
```

Tipi:

```text
DIRECT
INDIRECT
REGRESSION
NEGATIVE
BOUNDARY
MANUAL_CONFIRMATION
```

Il collegamento deve essere esplicito, non dedotto soltanto dalla somiglianza testuale.

---

# 13. Planned coverage e observed coverage

Devono restare distinte.

## Planned coverage

Quali test devono essere eseguiti.

## Observed coverage

Quali test sono stati realmente eseguiti.

Esempio:

```text
REQ-001

planned:
- TEST-001
- TEST-002

observed:
- TEST-001 PASSED
- TEST-002 NOT_RUN
```

Risultato:

```text
coverage = INCOMPLETE
```

---

# 14. Stati di copertura

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

Un requisito è `VERIFIED` soltanto quando la copertura obbligatoria è stata realmente eseguita e verificata.

---

# 15. Tipi di scenario

Per requisiti critici devono essere rappresentabili:

```text
POSITIVE
NEGATIVE
BOUNDARY
FAILURE
RECOVERY
REGRESSION
```

Non tutti sono sempre obbligatori.

L’assenza deve essere motivata quando il rischio è elevato.

---

# 16. Test runs

Campi:

```text
test_run_id
project_id
reference_code
test_definition_id
test_definition_version
attempt_id
task_execution_id
command_run_id
repository_snapshot_id
environment_id
status
started_at
completed_at
duration_ms
exit_code
observed_result_json
stdout_hash
stderr_hash
executed_by_actor_type
executed_by_actor_id
verified_against_commit
verified_against_baseline
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

---

# 17. Test run results

Un test run può contenere più asserzioni.

Campi:

```text
test_run_result_id
project_id
test_run_id
assertion_reference
expected_value_json
observed_value_json
status
difference_json
evidence_id
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

Vista sintetica:

```text
9/10 asserzioni superate
```

Drill-down:

```text
asserzione per asserzione
→ risultato
→ differenza
→ evidenza
```

---

# 18. Evidenze

```text
test_runs N ── N evidence
```

Ruoli:

```text
PRIMARY_RESULT
SUPPORTING_OUTPUT
FAILURE_DETAIL
ENVIRONMENT_PROOF
REGRESSION_PROOF
```

Un test `PASSED` senza l’evidenza obbligatoria deve risultare incompleto.

---

# 19. Ambiente e riproducibilità

Ogni run deve collegare un ambiente o fingerprint che includa almeno:

```text
operating_system
architecture
toolchain_versions
dependency_versions
database_version
schema_version
commit_sha
branch
working_tree_status
configuration_profile
```

Può esistere:

```text
test_environments
```

per evitare duplicazioni.

---

# 20. Dichiarato e osservato

Applicazione di `DEC-0101-009`:

```text
report dichiara TEST-001 PASSED
→ DECLARATION

runner esegue TEST-001
→ OBSERVATION

exit code produce PASSED
→ DERIVATION

dichiarazione e osservazione concordano
→ RECONCILIATION MATCH

criterio soddisfatto
→ VERIFICATION PASSED
```

---

# 21. Test esterni

Un test eseguito esternamente può essere importato come:

```text
SOURCE_ARTIFACT
o
DECLARATION
```

Non diventa automaticamente verificato.

Devono essere controllati:

- autenticità;
- commit;
- ambiente;
- output;
- identità del test;
- tentativo;
- risultato.

---

# 22. Collaudi

Entità:

```text
validations
validation_steps
validation_results
```

Ogni collaudo registra:

```text
validation_id
project_id
reference_code
task_id
attempt_id
environment
procedure
expected_result
observed_result
status
performed_by
performed_at
evidence
bugs_created
limitations
```

Il collaudo può coprire criteri tramite una relazione esplicita.

---

# 23. Regressione

Catena:

```text
bug
→ corrective_task
→ requirement
→ acceptance_criterion
→ regression_test_definition
→ regression_test_run
→ evidence
```

Un bug non dovrebbe essere chiuso senza test di regressione quando applicabile, salvo deroga.

---

# 24. Obsolescenza

La copertura può diventare `STALE` quando cambia:

- requisito;
- criterio;
- test definition;
- codice;
- dipendenza;
- ambiente;
- baseline;
- decisione applicabile.

Un test passato non resta automaticamente valido per una versione differente.

---

# 25. Matrice di tracciabilità

Vista sintetica:

| Requisito | Criterio | Test previsto | Ultimo run | Evidenza | Verifica | Stato |
|---|---|---|---|---|---|---|
| REQ-001 | AC-001 | TEST-001 | PASSED | EVIDENCE-001 | PASSED | VERIFIED |
| REQ-002 | AC-002 | TEST-002 | NOT_RUN | — | BLOCKED | INCOMPLETE |

Ogni cella deve aprire il dato originale.

La matrice è una sintesi navigabile, non la fonte primaria.

---

# 26. Blocco della chiusura

Una task non può essere completata quando:

```text
esiste un requisito bloccante non verificato;
esiste un criterio bloccante fallito;
un test obbligatorio non è stato eseguito;
un test è inconcludente;
manca evidenza;
la copertura è stale;
manca un collaudo obbligatorio;
esiste un mismatch non risolto;
la versione verificata non coincide con quella approvata.
```

Sono possibili:

- correzione;
- nuovo tentativo;
- revisione approvata del criterio;
- deroga esplicita;
- decisione umana registrata.

---

# 27. Regole vincolanti

```text
Un obiettivo non sostituisce un requisito.

Un requisito IMPLEMENTED non è VERIFIED.

Un criterio è osservabile e collegato a un requisito.

Una test definition è distinta da un test run.

Un test dichiarato non è un test osservato.

Un exit code positivo non dimostra da solo
che sia stato eseguito il test corretto.

Ogni run indica commit, ambiente e versione.

Ogni risultato apre l’evidenza originale.

La copertura passata può diventare STALE.

Una task non è COMPLETED se un requisito
bloccante non è VERIFIED.

Un bug corretto richiede un test di regressione
o una deroga esplicita.
```

---

# 28. Decisione approvata

```text
DEC-0101-011 — APPROVED

Project Integrity OS distingue formalmente obiettivi,
requisiti, criteri, definizioni dei test, test run,
risultati, evidenze, verifiche e collaudi.

La copertura pianificata è distinta da quella osservata.

Ogni test run registra versione, attempt, commit,
ambiente, comando, output, exit code, durata,
risultati ed evidenze.

Un requisito implementato non è automaticamente verificato.

Una task non può essere completata se requisiti
o criteri bloccanti non risultano verificati,
salvo deroga esplicita.

Ogni sintesi di copertura è navigabile fino
al dato e alla prova originali.
```

---

# 29. Aspetti da consolidare successivamente

- cardinalità finali;
- vocabolari definitivi;
- soglie;
- ambienti;
- test parameterization;
- flaky tests;
- retry policy;
- prestazioni;
- retention degli output;
- implementazione incrementale.
