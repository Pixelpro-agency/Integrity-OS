# Project Integrity OS

## Cardinalità definitive e tabelle associative — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole
**Data:** 2026-08-06
**Task collegata:** `TODO-0101 — Definire schema dati minimo`
**Decisione collegata:** `DEC-0101-019 — APPROVED`

---

# 1. Scopo

Questo documento consolida il grafo relazionale del sistema:

- cardinalità;
- ownership;
- parent autorevoli;
- versioni;
- tabelle associative;
- relazioni molti-a-molti;
- uso limitato dei collegamenti generici;
- isolamento tra progetti;
- comportamento delle foreign key.

Principio:

```text
relazioni fondamentali esplicite
+
grafo trasversale controllato
+
foreign key reali
+
versioni esatte
+
nessun collegamento ambiguo
```

---

# 2. Regole generali

## 2.1 Appartenenza al progetto

Ogni entità di dominio rilevante conserva:

```text
project_id
```

Ogni relazione interna rispetta:

```text
source.project_id = target.project_id
```

Le foreign key trasversali importanti usano, dove necessario:

```text
(entity_id, project_id)
```

Nell’MVP non sono ammesse relazioni dirette cross-project.

Le fonti esterne vengono rappresentate tramite riferimenti esterni, snapshot e hash.

## 2.2 Identità

Ogni entità persistente usa una PK UUID esplicita.

Le associazioni pure possono usare una chiave primaria composita.

Le associazioni governate, dotate di lifecycle, validità, approvazione o provenienza, possiedono un UUID autonomo.

Nessuna tabella dipende semanticamente da SQLite `rowid`.

## 2.3 Cancellazione

Per entità governate il comportamento predefinito è:

```text
ON DELETE RESTRICT
```

`CASCADE` è ammesso soltanto per componenti privi di identità autonoma, non governati e interamente posseduti dal parent.

---

# 3. Catalogo universale

## `project_entities`

Ogni entità citabile ha una identità comune nel grafo.

```text
PROJECT 1 ── 1..N PROJECT_ENTITIES
PROJECT_ENTITY 1 ── 1 SPECIALIZED DOMAIN RECORD
```

Campi minimi:

```text
entity_id
project_id
entity_type
reference_code
record_state
created_at
archived_at
```

La tabella specializzata condivide lo stesso UUID.

Esempio:

```text
project_entities.entity_id = tasks.task_id
```

La corrispondenza tra `entity_type` e tabella specializzata viene protetta tramite:

- factory transazionale nel core;
- constraint e trigger mirati;
- integrity rule obbligatoria;
- test di consistenza.

## `entity_versions`

```text
PROJECT_ENTITY 1 ── 0..N ENTITY_VERSIONS
ENTITY_VERSION 1 ── 1 SPECIALIZED VERSION RECORD
```

Campi comuni:

```text
entity_version_id
project_id
entity_id
version_number
version_status
content_hash
created_at
frozen_at
supersedes_entity_version_id
```

Le tabelle specializzate continuano a contenere i propri campi semantici.

---

# 4. Gerarchia del lavoro

Gerarchia autorevole:

```text
PROJECT
→ PHASE
→ WORK_ITEM
→ TASK
→ TASK_EXECUTION
→ ATTEMPT
```

Cardinalità:

```text
PROJECT        1 ── 0..N PHASES
PHASE          1 ── 0..N WORK_ITEMS
WORK_ITEM      1 ── 0..N TASKS
TASK           1 ── 0..N TASK_EXECUTIONS
TASK_EXECUTION 1 ── 0..N ATTEMPTS
```

Ogni elemento inferiore possiede un solo parent autorevole.

Una task non appartiene contemporaneamente a più work item.

Uno spostamento di parent è una transizione governata e non un aggiornamento diretto della FK.

---

# 5. Dipendenze

Tabelle dedicate:

```text
phase_dependencies
work_item_dependencies
task_dependencies
```

Cardinalità:

```text
PHASE N ── M PHASE
WORK_ITEM N ── M WORK_ITEM
TASK N ── M TASK
```

Campi minimi:

```text
dependency_type
blocking
required_state
valid_from
valid_until
created_at
```

Vincoli:

- nessun self-link;
- stesso progetto;
- nessuna duplicazione attiva;
- cicli vietati per dipendenze bloccanti.

---

# 6. Obiettivi, requisiti e criteri

## Obiettivi

Ogni obiettivo ha un solo root scope autorevole:

```text
PROJECT
PHASE
WORK_ITEM
TASK
```

Un’entità può avere più obiettivi.

## Obiettivi e requisiti

```text
OBJECTIVE N ── M REQUIREMENT
```

Tabella:

```text
objective_requirements
```

Ruoli:

```text
PRIMARY
SUPPORTING
CONSTRAINT
DERIVED
```

## Scope dei requisiti

```text
REQUIREMENT N ── M PROJECT_ENTITY
```

Tabella:

```text
requirement_scopes
```

Ogni requisito deve possedere almeno uno scope prima di diventare `APPROVED`.

## Versioni

```text
REQUIREMENT 1 ── 1..N REQUIREMENT_VERSIONS
ACCEPTANCE_CRITERION 1 ── 1..N ACCEPTANCE_CRITERION_VERSIONS
```

## Requisiti e criteri

```text
REQUIREMENT N ── M ACCEPTANCE_CRITERION
```

Tabella:

```text
requirement_acceptance_criteria
```

Campi:

```text
coverage_role
required
blocking
created_at
```

---

# 7. Definizioni dei test

```text
TEST_DEFINITION 1 ── 1..N TEST_DEFINITION_VERSIONS
ACCEPTANCE_CRITERION N ── M TEST_DEFINITION
```

Tabella:

```text
acceptance_criterion_test_definitions
```

Campi:

```text
coverage_type
mandatory
minimum_required_runs
required_result
applicable_environment
```

Ogni `test_run` punta alla versione esatta:

```text
test_definition_version_id
```

---

# 8. Task Contract

Struttura:

```text
task_contracts
task_contract_versions
```

Cardinalità:

```text
TASK 1 ── 1 TASK_CONTRACT
TASK_CONTRACT 1 ── 1..N TASK_CONTRACT_VERSIONS
```

Una task draft può non avere ancora il contratto.

Per diventare `DEFINED` deve avere almeno una bozza.

Per diventare `READY` deve avere una versione `FROZEN`.

Associazioni della versione:

```text
task_contract_version_requirements
task_contract_version_acceptance_criteria
task_contract_version_test_definitions
task_contract_version_documents
task_contract_version_decisions
task_contract_version_constraints
```

Le associazioni puntano a versioni esatte quando il contenuto è versionato.

---

# 9. Execution e attempt

```text
TASK 1 ── 0..N TASK_EXECUTIONS
TASK_EXECUTION 1 ── 0..N ATTEMPTS
```

Regola predefinita:

```text
massimo una task_execution attiva per task
massimo un attempt attivo per task_execution
```

Vincoli:

```text
UNIQUE(task_execution_id, attempt_number)
```

e, quando valorizzato:

```text
UNIQUE(task_execution_id, consumed_attempt_number)
```

Il parallelismo richiede una policy o decisione esplicita.

---

# 10. Prompt e Context Package

## Prompt

```text
PROMPT 1 ── 1..N PROMPT_VERSIONS
ATTEMPT 1 ── 1 PRIMARY PROMPT_VERSION
ATTEMPT 1 ── 0..N SUPPLEMENTARY PROMPT_VERSIONS
```

Tabella:

```text
attempt_prompts
```

Ruoli:

```text
PRIMARY_EXECUTION
CORRECTION
CLARIFICATION
RECOVERY
VERIFICATION
```

## Context Package

```text
CONTEXT_PACKAGE 1 ── 1..N CONTEXT_PACKAGE_VERSIONS
CONTEXT_PACKAGE_VERSION 1 ── 1..N CONTEXT_PACKAGE_ITEMS
ATTEMPT 1 ── 1..N CONTEXT_PACKAGE_VERSIONS
```

Un attempt necessita di almeno un `PRIMARY_EXECUTION_PACKAGE` prima dell’avvio.

Quando l’item è versionato, `entity_version_id` è obbligatorio.

Per record immutabili sono sufficienti identità e hash.

---

# 11. Repository snapshot, command run e test run

## Repository snapshot

Associazioni dedicate:

```text
attempt_repository_snapshots
baseline_repository_snapshots
verification_repository_snapshots
```

Ruoli:

```text
PRE_EXECUTION
POST_EXECUTION
VERIFICATION
BASELINE
RECOVERY
DIAGNOSTIC
```

## Command run

```text
ATTEMPT 1 ── 0..N COMMAND_RUNS
COMMAND_RUN N ── 1 ATTEMPT
```

Un comando importato senza attempt resta un source artifact finché non viene classificato e associato.

## Comandi e test

```text
COMMAND_RUN N ── M TEST_RUN
```

Tabella:

```text
test_run_command_runs
```

Ruoli:

```text
SETUP
PRIMARY
ASSERTION
TEARDOWN
DIAGNOSTIC
RECOVERY
```

## Test run

```text
TEST_DEFINITION_VERSION 1 ── 0..N TEST_RUNS
ATTEMPT 1 ── 0..N TEST_RUNS
TEST_RUN 1 ── 1..N TEST_RUN_RESULTS
```

---

# 12. Reports

Struttura:

```text
reports
report_versions
report_subjects
attempt_reports
verification_reports
validation_reports
```

Tipi iniziali:

```text
EXECUTION_REPORT
VERIFICATION_REPORT
VALIDATION_REPORT
DIAGNOSTIC_REPORT
RECOVERY_REPORT
INTEGRITY_REPORT
IMPORT_REPORT
EXPORT_REPORT
SECURITY_REPORT
CLOSURE_REPORT
```

Cardinalità:

```text
REPORT 1 ── 1..N REPORT_VERSIONS
ATTEMPT N ── M REPORTS
VERIFICATION N ── M REPORTS
VALIDATION N ── M REPORTS
```

Un attempt può avere report intermedi e di correzione, ma prima della verifica conclusiva deve avere un solo final execution report attivo e accettato.

L’originale consegnato resta immutabile.

Una rettifica crea una nuova versione.

Ogni report possiede almeno un subject.

---

# 13. Evidence, reconciliation, verification e validation

## Evidence

Struttura:

```text
evidence
evidence_artifacts
evidence_sources
```

Relazioni operative dedicate:

```text
command_run_evidence
test_run_evidence
report_evidence
reconciliation_evidence
verification_evidence
validation_evidence
bug_evidence
integrity_check_evidence
```

La stessa evidence può sostenere più verifiche senza duplicazione.

## Reconciliation

```text
RECONCILIATION 1 ── 2..N INPUTS
RECONCILIATION 1 ── 1..N RESULTS
VERIFICATION N ── M RECONCILIATIONS
```

Struttura:

```text
reconciliations
reconciliation_inputs
reconciliation_results
verification_reconciliations
```

## Verification

```text
VERIFICATION 1 ── 1 PRIMARY SUBJECT
VERIFICATION 1 ── 0..N ADDITIONAL SUBJECTS
VERIFICATION 1 ── 1..N CRITERIA
VERIFICATION 1 ── 1..N RESULTS
VERIFICATION N ── M EVIDENCE
VERIFICATION N ── M RECONCILIATIONS
```

## Validation

```text
VALIDATION 1 ── 1 PRIMARY SUBJECT
VALIDATION 1 ── 1..N STEPS
VALIDATION_STEP 1 ── 1 RESULT
VALIDATION N ── M ACCEPTANCE_CRITERIA
VALIDATION N ── M EVIDENCE
```

---

# 14. Decisions

Struttura:

```text
decisions
decision_versions
decision_options
decision_inputs
decision_targets
decision_resolutions
decision_implementation_links
```

Cardinalità:

```text
DECISION 1 ── 1..N DECISION_VERSIONS
DECISION_VERSION 1 ── 1..N OPTIONS
DECISION_VERSION 1 ── 1..N INPUTS
DECISION_VERSION 1 ── 1..N TARGETS
DECISION_VERSION 1 ── 0..1 FINAL RESOLUTION
DECISION_VERSION 1 ── 0..N IMPLEMENTATION LINKS
```

Una versione draft può temporaneamente non avere opzioni.

Prima della risoluzione deve avere almeno una opzione oppure una motivazione di opzione unica.

---

# 15. Register items e bugs

Struttura comune:

```text
register_items
register_item_versions
register_item_links
```

Specializzazioni:

```text
open_questions
assumptions
risks
findings
conflicts
bugs
```

Cardinalità:

```text
REGISTER_ITEM 1 ── 1 SPECIALIZED RECORD
REGISTER_ITEM 1 ── 1..N REGISTER_ITEM_VERSIONS
```

`bugs` è una specializzazione 1:1 di `register_items`.

Relazioni dedicate:

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

Un bug può generare più task correttive.

Una task può risolvere più bug correlati tramite collegamenti espliciti.

---

# 16. Approvals

Struttura:

```text
approval_requests
approval_request_subjects
approval_requirements
approvals
```

Cardinalità:

```text
APPROVAL_REQUEST 1 ── 1 PRIMARY SUBJECT
APPROVAL_REQUEST 1 ── 0..N ADDITIONAL SUBJECTS
APPROVAL_REQUEST 1 ── 1..N REQUIREMENTS
APPROVAL_REQUEST 1 ── 0..N APPROVALS
ACTOR 1 ── 0..N APPROVALS
```

Tipi iniziali:

```text
DECISION_RESOLUTION
VERSION_APPROVAL
TRANSITION_APPROVAL
TASK_COMPLETION
BASELINE_APPROVAL
EXCEPTION_APPROVAL
DELETION_APPROVAL
DECLASSIFICATION_APPROVAL
BREAK_GLASS_APPROVAL
PROJECT_CLOSURE
```

Ogni approval è l’atto di un singolo approvatore.

Esiti:

```text
APPROVED
REJECTED
ABSTAINED
CHANGES_REQUESTED
REVOKED
EXPIRED
```

---

# 17. Exceptions

Struttura:

```text
exceptions
exception_versions
exception_targets
exception_rule_overrides
exception_conditions
exception_uses
```

Cardinalità:

```text
EXCEPTION 1 ── 1..N EXCEPTION_VERSIONS
EXCEPTION_VERSION 1 ── 1..N TARGETS
EXCEPTION_VERSION 1 ── 1..N RULE OVERRIDES
EXCEPTION_VERSION 1 ── 0..N CONDITIONS
EXCEPTION_VERSION 1 ── 0..N USES
```

Tipi:

```text
INTEGRITY_RULE_EXCEPTION
TRANSITION_EXCEPTION
SECURITY_EXCEPTION
RETENTION_EXCEPTION
SCOPE_EXCEPTION
TEST_EXCEPTION
SEPARATION_OF_DUTIES_EXCEPTION
```

Ogni uso viene registrato.

Una exception non modifica permanentemente la regola derogata.

---

# 18. Baselines

Struttura:

```text
baselines
baseline_versions
baseline_items
baseline_state_snapshots
baseline_repository_snapshots
baseline_approval_requests
```

Tipi:

```text
INITIAL
WORKING
MILESTONE
TASK_CLOSURE
PHASE_CLOSURE
RELEASE
FINAL
RECOVERY
```

Cardinalità:

```text
PROJECT 1 ── 0..N BASELINES
BASELINE 1 ── 1..N BASELINE_VERSIONS
BASELINE_VERSION 1 ── 1..N BASELINE_ITEMS
BASELINE_VERSION 1 ── 1..N STATE_SNAPSHOTS
BASELINE_VERSION 1 ── 0..N REPOSITORY_SNAPSHOTS
BASELINE_VERSION 1 ── 0..1 ACTIVE APPROVAL REQUEST
```

Ogni versione possiede almeno:

- manifest;
- state snapshot;
- hash completo.

`baseline_items` punta a identità e, quando applicabile, versioni esatte.

Regola predefinita:

```text
massimo una baseline EFFECTIVE
per progetto, tipo e scope
nello stesso intervallo temporale
```

---

# 19. Documents, summaries e provenance

## Documents

```text
DOCUMENT 1 ── 1..N DOCUMENT_VERSIONS
DOCUMENT_VERSION 1 ── 0..N ARTIFACTS
DOCUMENT N ── M DOCUMENTS
```

Relazioni:

```text
SUPERSEDES
DERIVED_FROM
REFERENCES
IMPLEMENTS
SUMMARIZES
ATTACHES
```

## Summaries

Struttura definitiva:

```text
summaries
summary_versions
summary_sources
summary_coverage
summary_exclusions
summary_claims
summary_claim_sources
```

Cardinalità:

```text
SUMMARY 1 ── 1..N SUMMARY_VERSIONS
SUMMARY_VERSION 1 ── 1..N SOURCES
SUMMARY_VERSION 1 ── 1..N COVERAGE RECORDS
SUMMARY_VERSION 1 ── 0..N EXCLUSIONS
SUMMARY_VERSION 1 ── 0..N CLAIMS
SUMMARY_CLAIM 1 ── 1..N CLAIM SOURCES
```

## Provenance

```text
PROJECT_ENTITY 1 ── 0..N PROVENANCE_RECORDS come target
PROJECT_ENTITY 1 ── 0..N PROVENANCE_RECORDS come source
PROVENANCE_RECORD 1 ── 0..N PROVENANCE_INPUTS
```

Le derivazioni e inferenze richiedono input.

Le catene di derivazione devono essere acicliche.

---

# 20. Events, sicurezza, transizioni e integrità

## Events

```text
PROJECT 1 ── 0..N EVENTS
PROJECT_ENTITY 1 ── 0..N EVENTS come aggregate
EVENT 1 ── 1..N EVENT_SUBJECTS
```

Vincoli:

```text
UNIQUE(project_id, project_sequence_number)
UNIQUE(project_id, aggregate_entity_id, aggregate_sequence_number)
```

## Sicurezza

```text
ACTOR 1 ── 0..N IDENTITIES
ACTOR 1 ── 0..N SESSIONS
ACTOR N ── M ROLES tramite ACTOR_ROLE_ASSIGNMENTS
ROLE 1 ── 1..N ROLE_VERSIONS
ROLE_VERSION N ── M PERMISSIONS
```

## Transition engine

```text
TRANSITION_DEFINITION 1 ── 1..N VERSIONS
TRANSITION_VERSION 1 ── 1..N REQUIREMENTS
TRANSITION_VERSION 1 ── 0..N EFFECTS
TRANSITION_REQUEST 1 ── 0..N EVALUATIONS
TRANSITION_REQUEST 1 ── 0..1 SUCCESSFUL EXECUTION
TRANSITION_EXECUTION 1 ── 0..N EFFECT RESULTS
```

## Integrity engine

```text
INTEGRITY_RULE 1 ── 1..N RULE_VERSIONS
INTEGRITY_PROFILE 1 ── 1..N PROFILE_VERSIONS
PROFILE_VERSION N ── M RULE_VERSIONS
INTEGRITY_RUN N ── 1 PROFILE_VERSION
INTEGRITY_RUN 1 ── 1..N CHECK_RESULTS
```

---

# 21. `entity_links`

`entity_links` è limitata alle relazioni trasversali supplementari.

Può rappresentare:

```text
RELATED_TO
SIMILAR_TO
INFORMED_BY
REFERENCES
NAVIGATES_TO
HISTORICALLY_ASSOCIATED_WITH
```

Non può sostituire:

```text
task → work item
attempt → task execution
requirement → criterion
criterion → test definition
attempt → report
test run → evidence
approval → request
baseline → items
```

I tipi di relazione sono governati da `relationship_types`.

---

# 22. Vincoli immediati e condizionali

## Database

Applica invarianti sempre valide:

- foreign key;
- unicità;
- isolamento progetto;
- parent;
- sequence;
- no self-link;
- una sola specializzazione;
- una sola risoluzione finale;
- formati e tipi.

## Transition requirements

Applicano cardinalità minime dipendenti dal lifecycle:

- report finale;
- evidence;
- criteri;
- test;
- fonti;
- approvazioni;
- assenza di blocker.

## Integrity scans

Controllano:

- cicli;
- orfani semantici;
- sovrapposizioni temporali;
- incompletezze storiche;
- contenuti esterni mancanti;
- divergenze tra stato e relazioni.

---

# 23. Copertura della To-Do v0.8

Le entità minime richieste restano esplicite:

```text
projects
baselines
tasks
task_executions
reports
evidence
reconciliations
verifications
approvals
exceptions
bugs
events
repository_snapshots
command_runs
```

Nessuna viene assorbita in un grafo generico privo di semantica.

---

# 24. Decisione approvata

```text
DEC-0101-019 — APPROVED

Project Integrity OS usa una gerarchia stretta
per project, phase, work item, task,
task execution e attempt.

project_entities fornisce l’identità universale.

entity_versions fornisce l’identità comune
delle versioni immutabili.

Le relazioni fondamentali usano tabelle dedicate.

entity_links è limitata ai collegamenti
trasversali supplementari.

Le associazioni pure possono usare PK composite.

Le associazioni governate possiedono UUID autonomi.

Ogni collegamento interno rispetta project_id.

Le cardinalità strutturali sono protette dal database.

Le cardinalità condizionali sono protette
da transizioni e integrity profile.

Il default delle foreign key governate
è ON DELETE RESTRICT.

Nessuna struttura dipende da rowid.
```
