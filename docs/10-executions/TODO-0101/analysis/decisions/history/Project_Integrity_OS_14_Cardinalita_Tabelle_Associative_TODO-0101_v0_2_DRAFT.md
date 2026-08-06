# Project Integrity OS

## Cardinalità definitive e tabelle associative — v0.2

**Stato:** DRAFT — modello relazionale corretto e consolidato  
**Data:** 2026-08-06  
**Task:** `TODO-0101`  
**Decisione primaria:** `DEC-0101-019`  
**Correzioni applicate:** `C-0101-001` → `C-0101-005`  
**Sostituisce:** `Project_Integrity_OS_14_Cardinalita_Tabelle_Associative_TODO-0101_v0_1_DRAFT.md`

---

# 1. Regola fondamentale

Il documento distingue:

```text
CARDINALITÀ STRUTTURALE
```

da:

```text
MINIMO RICHIESTO DA UNA TRANSIZIONE
```

Le cardinalità strutturali devono essere valide in tutti gli stati ammessi.

Le quantità minime dipendenti dal lifecycle vengono applicate da transition requirements e integrity profiles.

---

# 2. Notazione

```text
1       esattamente uno
0..1    zero oppure uno
1..N    uno o più
0..N    zero o più
N..M    molti-a-molti
```

---

# 3. Project root e catalogo universale

```text
PROJECT 1 ── 1 ROOT PROJECT_ENTITY
PROJECT 1 ── 0..N OTHER PROJECT_ENTITIES
PROJECT_ENTITY 1 ── 1 SPECIALIZED DOMAIN RECORD
PROJECT_ENTITY 1 ── 0..N ENTITY_VERSIONS
```

Per la root:

```text
projects.project_id = project_entities.entity_id
project_entities.project_id = projects.project_id
entity_type = PROJECT
```

Per le altre entità:

```text
project_entities.entity_id = specialized_table.primary_key
```

Le entità citabili project-local usano `project_entities`.

I cataloghi globali non vi appartengono.

---

# 4. Cataloghi globali e configurazioni locali

## Globali

```text
permissions
classification_levels
handling_flag_definitions
event_types
relationship_type_templates
role_templates
transition_templates
integrity_rule_templates
```

Non possiedono `project_id`.

## Project-local

```text
roles
transition_definitions
integrity_rules
access_policies
approval_policies
retention_policies
redaction_profiles
```

Possiedono `project_id NOT NULL` e versioni locali.

Un record locale può riferirsi a un template globale.

---

# 5. Gerarchia del lavoro

Cardinalità strutturali:

```text
PROJECT        1 ── 0..N PHASES
PHASE          1 ── 0..N WORK_ITEMS
WORK_ITEM      1 ── 0..N TASKS
TASK           1 ── 0..N TASK_EXECUTIONS
TASK_EXECUTION 1 ── 0..N ATTEMPTS
```

Ogni figlio possiede un solo parent autorevole.

Il parallelismo di execution e attempt è regolato da policy e partial uniqueness.

Dipendenze:

```text
PHASE N ── M PHASE
WORK_ITEM N ── M WORK_ITEM
TASK N ── M TASK
```

Le dipendenze bloccanti devono essere acicliche.

---

# 6. Obiettivi, requisiti, criteri e test

```text
PROJECT_ENTITY 1 ── 0..N OBJECTIVES come root scope
OBJECTIVE N ── M REQUIREMENTS
REQUIREMENT N ── M PROJECT_ENTITIES tramite REQUIREMENT_SCOPES
REQUIREMENT 1 ── 1..N REQUIREMENT_VERSIONS
REQUIREMENT N ── M ACCEPTANCE_CRITERIA
ACCEPTANCE_CRITERION 1 ── 1..N ACCEPTANCE_CRITERION_VERSIONS
ACCEPTANCE_CRITERION N ── M TEST_DEFINITIONS
TEST_DEFINITION 1 ── 1..N TEST_DEFINITION_VERSIONS
```

Minimi di transizione:

```text
REQUIREMENT → APPROVED
richiede almeno uno scope

ACCEPTANCE_CRITERION → APPROVED
richiede almeno un requirement o una motivazione standalone

TASK → READY
richiede i criteri e le test definition obbligatorie
```

---

# 7. Task Contract

Cardinalità strutturale:

```text
TASK 1 ── 0..1 TASK_CONTRACT
TASK_CONTRACT 1 ── 1..N TASK_CONTRACT_VERSIONS
```

Condizioni:

```text
TASK → DEFINED
richiede Task Contract con versione DRAFT

TASK → READY
richiede Task Contract version FROZEN
```

Associazioni versionate:

```text
task_contract_version_requirements
task_contract_version_acceptance_criteria
task_contract_version_test_definitions
task_contract_version_documents
task_contract_version_decisions
task_contract_version_constraints
```

---

# 8. Attempt, prompt e Context Package

```text
TASK_EXECUTION 1 ── 0..N ATTEMPTS
PROMPT 1 ── 1..N PROMPT_VERSIONS
ATTEMPT N ── M PROMPT_VERSIONS tramite ATTEMPT_PROMPTS
CONTEXT_PACKAGE 1 ── 1..N CONTEXT_PACKAGE_VERSIONS
CONTEXT_PACKAGE_VERSION 1 ── 0..N CONTEXT_PACKAGE_ITEMS
ATTEMPT N ── M CONTEXT_PACKAGE_VERSIONS
```

Vincoli:

```text
UNIQUE(task_execution_id, attempt_number)
```

Minimi:

```text
ATTEMPT → READY
richiede un PRIMARY prompt frozen
e un PRIMARY_EXECUTION_PACKAGE frozen

CONTEXT_PACKAGE_VERSION → VALID
richiede almeno un item o una motivazione EMPTY_PACKAGE_APPROVED
```

---

# 9. Repository snapshot, command run e test run

```text
ATTEMPT N ── M REPOSITORY_SNAPSHOTS
BASELINE_VERSION N ── M REPOSITORY_SNAPSHOTS
VERIFICATION N ── M REPOSITORY_SNAPSHOTS

ATTEMPT 1 ── 0..N COMMAND_RUNS
COMMAND_RUN N ── M TEST_RUNS
TEST_DEFINITION_VERSION 1 ── 0..N TEST_RUNS
ATTEMPT 1 ── 0..N TEST_RUNS
TEST_RUN 1 ── 0..N TEST_RUN_RESULTS
```

Minimi:

```text
TEST_RUN → COMPLETED
richiede almeno un risultato conclusivo

ATTEMPT → IN_VERIFICATION
richiede snapshot e run previsti dal Task Contract
```

---

# 10. Ownership dei report

Struttura:

```text
reports
report_versions
report_ownerships
report_subjects
```

Cardinalità:

```text
REPORT 1 ── 1..N REPORT_VERSIONS
REPORT 1 ── 1 REPORT_OWNERSHIP
PROJECT_ENTITY 1 ── 0..N OWNED REPORTS
REPORT N ── M PROJECT_ENTITIES tramite REPORT_SUBJECTS
```

`report_ownerships.report_id` è unico.

Owner ammessi per tipo:

```text
EXECUTION_REPORT   → ATTEMPT
VERIFICATION_REPORT → VERIFICATION
VALIDATION_REPORT  → VALIDATION
INTEGRITY_REPORT   → INTEGRITY_RUN
RECOVERY_REPORT    → RECOVERY RUN
SECURITY_REPORT    → SECURITY OPERATION o ACCESS REVIEW
CLOSURE_REPORT     → TASK, PHASE, WORK_ITEM o PROJECT CLOSURE
```

`report_subjects` aggiunge contesto ma non cambia owner.

Un execution report non può essere owner-linked a più attempt.

Minimo:

```text
ATTEMPT → REPORTED
richiede un FINAL_EXECUTION_REPORT accettato
```

---

# 11. Evidence e reconciliation

```text
EVIDENCE 1 ── 0..N EVIDENCE_ARTIFACTS
EVIDENCE N ── M SOURCE ENTITIES
RECONCILIATION 1 ── 0..N INPUTS
RECONCILIATION 1 ── 0..N RESULTS
VERIFICATION N ── M RECONCILIATIONS
```

Minimi per tipo:

```text
COMPARISON_RECONCILIATION → READY
richiede almeno 2 input

NORMALIZATION_RECONCILIATION → READY
richiede almeno 1 input

RECONCILIATION → COMPLETED
richiede almeno 1 risultato
```

---

# 12. Verification e validation

```text
VERIFICATION 1 ── 1 PRIMARY SUBJECT
VERIFICATION 1 ── 0..N ADDITIONAL SUBJECTS
VERIFICATION 1 ── 0..N CRITERIA
VERIFICATION 1 ── 0..N RESULTS
VERIFICATION N ── M EVIDENCE
VERIFICATION N ── M RECONCILIATIONS

VALIDATION 1 ── 1 PRIMARY SUBJECT
VALIDATION 1 ── 0..N ADDITIONAL SUBJECTS
VALIDATION 1 ── 0..N STEPS
VALIDATION_STEP 1 ── 0..1 CURRENT RESULT
VALIDATION N ── M ACCEPTANCE_CRITERIA
VALIDATION N ── M EVIDENCE
```

Minimi:

```text
VERIFICATION → READY
richiede almeno un criterio

VERIFICATION → PASSED/FAILED
richiede risultati per tutti i criteri obbligatori

VALIDATION → READY
richiede almeno uno step

VALIDATION → PASSED/FAILED
richiede un risultato per ogni step obbligatorio
```

---

# 13. Decisions

```text
DECISION 1 ── 1..N DECISION_VERSIONS
DECISION_VERSION 1 ── 0..N OPTIONS
DECISION_VERSION 1 ── 0..N INPUTS
DECISION_VERSION 1 ── 0..N TARGETS
DECISION_VERSION 1 ── 0..1 FINAL RESOLUTION
DECISION_VERSION 1 ── 0..N IMPLEMENTATION LINKS
```

Minimi:

```text
DECISION_VERSION → READY_FOR_RESOLUTION
richiede almeno una option
oppure single_option_reason

DECISION_VERSION → RESOLVED
richiede target, input sufficiente e una final resolution
```

---

# 14. Register items e BUG

```text
REGISTER_ITEM 1 ── 1..N REGISTER_ITEM_VERSIONS
REGISTER_ITEM 1 ── 1 SPECIALIZED RECORD
```

Tipi:

```text
OPEN_QUESTION
ASSUMPTION
RISK
FINDING
CONFLICT
BUG
```

Relazioni dedicate del bug:

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

---

# 15. Approvals

```text
APPROVAL_REQUEST 1 ── 1 PRIMARY SUBJECT
APPROVAL_REQUEST 1 ── 0..N ADDITIONAL SUBJECTS
APPROVAL_REQUEST 1 ── 0..N REQUIREMENTS
APPROVAL_REQUEST 1 ── 0..N APPROVALS
ACTOR 1 ── 0..N APPROVALS
```

Minimi:

```text
APPROVAL_REQUEST → SUBMITTED
richiede i requirement calcolati dalla policy

APPROVAL_REQUEST → APPROVED
richiede quorum e separation of duties soddisfatti
```

---

# 16. Exceptions

```text
EXCEPTION 1 ── 1..N EXCEPTION_VERSIONS
EXCEPTION_VERSION 1 ── 0..N TARGETS
EXCEPTION_VERSION 1 ── 0..N RULE_OVERRIDES
EXCEPTION_VERSION 1 ── 0..N CONDITIONS
EXCEPTION_VERSION 1 ── 0..N USES
```

Minimo:

```text
EXCEPTION_VERSION → SUBMITTED
richiede almeno un target e una regola derogabile

EXCEPTION_VERSION → ACTIVE
richiede approval, intervallo e condizioni
```

---

# 17. Baselines

```text
PROJECT 1 ── 0..N BASELINES
BASELINE 1 ── 1..N BASELINE_VERSIONS
BASELINE_VERSION 1 ── 0..N BASELINE_ITEMS
BASELINE_VERSION 1 ── 0..N STATE_SNAPSHOTS
BASELINE_VERSION 1 ── 0..N REPOSITORY_SNAPSHOTS
BASELINE_VERSION 1 ── 0..1 ACTIVE APPROVAL REQUEST
```

Minimi:

```text
BASELINE_VERSION → VALIDATING
richiede manifest congelato

BASELINE_VERSION → READY_FOR_APPROVAL
richiede almeno uno state snapshot,
hash completo e item richiesti dal profilo

repository snapshot obbligatorio
quando il profilo lo richiede
```

---

# 18. Documents e summaries

```text
DOCUMENT 1 ── 1..N DOCUMENT_VERSIONS
DOCUMENT_VERSION 1 ── 0..N ARTIFACTS
DOCUMENT N ── M DOCUMENTS

SUMMARY 1 ── 1..N SUMMARY_VERSIONS
SUMMARY_VERSION 1 ── 0..N SOURCES
SUMMARY_VERSION 1 ── 0..N COVERAGE RECORDS
SUMMARY_VERSION 1 ── 0..N EXCLUSIONS
SUMMARY_VERSION 1 ── 0..N CLAIMS
SUMMARY_CLAIM 1 ── 0..N CLAIM SOURCES
```

Minimi:

```text
SUMMARY_VERSION → VALID
richiede almeno una source,
coverage esplicita e source per ogni claim materiale
```

---

# 19. Events e temporalità

```text
PROJECT 1 ── 0..N EVENTS
PROJECT_ENTITY 1 ── 0..N EVENTS come aggregate
EVENT 1 ── 1..N EVENT_SUBJECTS
PROJECT 1 ── 0..N STATE_SNAPSHOTS
PROJECT 1 ── 0..N STATE_RECONSTRUCTIONS
```

Vincoli:

```text
UNIQUE(project_id, project_sequence_number)

UNIQUE(
  project_id,
  aggregate_entity_id,
  aggregate_sequence_number
)
```

Ogni evento ha un aggregate primario e almeno un subject.

---

# 20. Sicurezza

```text
ACTOR N ── M PROJECTS tramite PROJECT_MEMBERSHIPS
ACTOR 1 ── 0..N IDENTITIES
ACTOR 1 ── 0..N SESSIONS
PROJECT 1 ── 0..N ROLES
ROLE 1 ── 1..N ROLE_VERSIONS
ROLE_VERSION N ── M GLOBAL PERMISSIONS
ACTOR N ── M ROLE_VERSIONS tramite ACTOR_ROLE_ASSIGNMENTS
```

`actor_role_assignments` possiede un solo scope root project-local.

---

# 21. Transition engine e integrity engine

```text
TRANSITION_DEFINITION 1 ── 1..N VERSIONS
TRANSITION_VERSION 1 ── 0..N REQUIREMENTS
TRANSITION_VERSION 1 ── 0..N EFFECTS
TRANSITION_REQUEST 1 ── 0..N EVALUATIONS
TRANSITION_REQUEST 1 ── 0..1 SUCCESSFUL EXECUTION
TRANSITION_EXECUTION 1 ── 0..N EFFECT RESULTS

INTEGRITY_RULE 1 ── 1..N RULE_VERSIONS
INTEGRITY_PROFILE 1 ── 1..N PROFILE_VERSIONS
PROFILE_VERSION N ── M RULE_VERSIONS
INTEGRITY_RUN 1 ── 0..N CHECK_RESULTS
```

Minimi:

```text
TRANSITION_VERSION → ACTIVE
richiede regole e profilo sufficienti

INTEGRITY_RUN → COMPLETED
richiede un risultato per ogni check pianificato
```

---

# 22. Enforcement

## Database

- PK;
- FK;
- same-project FK;
- unique;
- check;
- parent;
- no self-link;
- una sola specialization;
- una sola report ownership;
- sequence.

## Transition requirements

- minimi dipendenti dallo stato;
- report finale;
- criteria;
- results;
- item;
- source;
- approval;
- snapshot;
- assenza di blocker.

## Integrity scans

- cicli;
- orfani;
- sovrapposizioni temporali;
- divergenze;
- cataloghi mal classificati;
- root project entity mancante;
- report con ownership invalida.

---

# 23. Decisione consolidata

```text
DEC-0101-019 + C-0101-001...005

Le cardinalità strutturali rappresentano
tutti gli stati validi del record.

I minimi dipendenti dal lifecycle sono
transition requirements.

Ogni report possiede un solo owner autorevole.

BUG è una specializzazione del registro comune.

Il progetto possiede una root project entity.

I cataloghi globali sono separati
dalle configurazioni project-local.

Le relazioni fondamentali usano tabelle dedicate
e ogni relazione interna rispetta project_id.
```
