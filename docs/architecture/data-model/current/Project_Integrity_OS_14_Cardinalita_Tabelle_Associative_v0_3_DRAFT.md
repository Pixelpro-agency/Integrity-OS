# Project Integrity OS

## Cardinalità consolidate e tabelle associative — v0.3

**Stato:** DRAFT — modello relazionale consolidato, non ancora fonte autorevole
**Data:** 2026-08-06
**Task:** `TODO-0101`
**Decisione primaria:** `DEC-0101-019`
**Correzioni:** `C-0101-001` → `C-0101-009`
**Sostituisce:** `../history/decisions/Project_Integrity_OS_14_Cardinalita_Tabelle_Associative_v0_2_DRAFT.md`

---

# 1. Regola fondamentale

```text
structural cardinality
≠ transition required minimum
```

Le cardinalità strutturali rappresentano tutti gli stati validi.

I minimi dipendenti dal lifecycle sono transition requirements.

---

# 2. Notazione

```text
1
0..1
1..N
0..N
N..M
```

---

# 3. Scope di persistenza

```text
SYSTEM_CATALOG
GLOBAL_REGISTRY
PROJECT_DATABASE
```

Nell'MVP:

```text
CONTROL DATABASE
= system catalog + global registry

PROJECT DATABASE
= un progetto
```

Nessuna FK cross-database.

I riferimenti globali usano code, catalog version, definition hash e binding locale.

---

# 4. Project root

```text
PROJECT 1 ── 1 ROOT PROJECT_ENTITY
PROJECT 1 ── 0..N OTHER PROJECT_ENTITIES
PROJECT_ENTITY 1 ── 1 SPECIALIZED DOMAIN RECORD
PROJECT_ENTITY 1 ── 0..N ENTITY_VERSIONS
```

---

# 5. Gerarchia

```text
PROJECT        1 ── 0..N PHASES
PHASE          1 ── 0..N WORK_ITEMS
WORK_ITEM      1 ── 0..N TASKS
TASK           1 ── 0..N TASK_EXECUTIONS
TASK_EXECUTION 1 ── 0..N ATTEMPTS
```

Dipendenze N:M dedicate.

---

# 6. Objectives, requirements, criteria, tests

```text
PROJECT_ENTITY 1 ── 0..N OBJECTIVES
OBJECTIVE N ── M REQUIREMENTS

REQUIREMENT 1 ── 1..N REQUIREMENT_VERSIONS
REQUIREMENT_VERSION N ── M PROJECT_ENTITIES
REQUIREMENT_VERSION N ── M ACCEPTANCE_CRITERION_VERSIONS

ACCEPTANCE_CRITERION 1 ── 1..N ACCEPTANCE_CRITERION_VERSIONS
ACCEPTANCE_CRITERION_VERSION N ── M TEST_DEFINITION_VERSIONS

TEST_DEFINITION 1 ── 1..N TEST_DEFINITION_VERSIONS
TEST_DEFINITION_VERSION 1 ── 0..N TEST_RUNS
TEST_RUN 1 ── 0..N TEST_RUN_RESULTS
TEST_RUN N ── M COMMAND_RUNS
```

---

# 7. Task Contract

```text
TASK 1 ── 0..1 TASK_CONTRACT
TASK_CONTRACT 1 ── 1..N TASK_CONTRACT_VERSIONS
```

Minimi:

```text
TASK → DEFINED
1 draft contract version

TASK → READY
1 frozen contract version
```

---

# 8. Attempt, prompt e Context Package

```text
TASK_EXECUTION 1 ── 0..N ATTEMPTS
PROMPT 1 ── 1..N PROMPT_VERSIONS
ATTEMPT N ── M PROMPT_VERSIONS
CONTEXT_PACKAGE 1 ── 1..N CONTEXT_PACKAGE_VERSIONS
CONTEXT_PACKAGE_VERSION 1 ── 0..N ITEMS
CONTEXT_PACKAGE_VERSION 1 ── 0..N EXCLUSIONS
ATTEMPT N ── M CONTEXT_PACKAGE_VERSIONS
```

Vincolo:

```text
UNIQUE(task_execution_id, attempt_number)
```

---

# 9. Repository e commands

```text
ATTEMPT N ── M REPOSITORY_SNAPSHOTS
BASELINE_VERSION N ── M REPOSITORY_SNAPSHOTS
VERIFICATION N ── M REPOSITORY_SNAPSHOTS

ATTEMPT 1 ── 0..N COMMAND_RUNS
TEST_RUN N ── M COMMAND_RUNS
```

---

# 10. Reports

```text
REPORT 1 ── 1..N REPORT_VERSIONS
REPORT 1 ── 1 REPORT_OWNERSHIP
PROJECT_ENTITY 1 ── 0..N OWNED REPORTS
REPORT N ── M PROJECT_ENTITIES tramite REPORT_SUBJECTS
```

`report_ownerships.report_id` è unique.

Owner canonici:

```text
EXECUTION_REPORT    → ATTEMPT
VERIFICATION_REPORT → VERIFICATION
VALIDATION_REPORT   → VALIDATION
INTEGRITY_REPORT    → INTEGRITY_RUN
RECOVERY_REPORT     → TRANSITION_RECOVERY_RUN
SECURITY_REPORT     → SECURITY_REVIEW
IMPORT_REPORT       → IMPORT_RECORD
EXPORT_REPORT       → EXPORT_RECORD
CLOSURE_REPORT      → PROJECT/PHASE/WORK_ITEM/TASK/BASELINE target
DIAGNOSTIC_REPORT   → una project entity ammessa dalla policy
```

`report_owner_policies` definisce report type, allowed owner entity type e owner role.

---

# 11. Evidence e reconciliation

```text
EVIDENCE 1 ── 0..N EVIDENCE_ARTIFACTS
EVIDENCE N ── M SOURCE ENTITIES

RECONCILIATION 1 ── 0..N INPUTS
RECONCILIATION 1 ── 0..N RESULTS
VERIFICATION N ── M RECONCILIATIONS
```

Minimi dipendono dal reconciliation type.

---

# 12. Verification e validation

```text
VERIFICATION 1 ── 1 PRIMARY SUBJECT
VERIFICATION 1 ── 0..N ADDITIONAL SUBJECTS
VERIFICATION 1 ── 0..N CRITERIA
VERIFICATION 1 ── 0..N RESULTS
VERIFICATION N ── M EVIDENCE

VALIDATION 1 ── 1 PRIMARY SUBJECT
VALIDATION 1 ── 0..N ADDITIONAL SUBJECTS
VALIDATION 1 ── 0..N STEPS
VALIDATION_STEP 1 ── 0..N STEP_RUNS
VALIDATION_STEP_RUN 1 ── 1..N RESULTS
VALIDATION N ── M ACCEPTANCE_CRITERION_VERSIONS
VALIDATION N ── M EVIDENCE
```

Nessun risultato storico viene sovrascritto.

---

# 13. Decisions

```text
DECISION 1 ── 1..N DECISION_VERSIONS
DECISION_VERSION 1 ── 0..N OPTIONS
DECISION_VERSION 1 ── 0..N INPUTS
DECISION_VERSION 1 ── 0..N TARGETS
DECISION_VERSION 1 ── 0..N CONDITIONS
DECISION_VERSION 1 ── 0..1 FINAL RESOLUTION
DECISION_VERSION 1 ── 0..N IMPLEMENTATION LINKS
DECISION_VERSION 1 ── 0..N EFFECTS
```

La option scelta è determinata dalla final resolution.

---

# 14. Register items

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

---

# 15. Approvals

```text
APPROVAL_REQUEST 1 ── 1 PRIMARY SUBJECT
APPROVAL_REQUEST 1 ── 0..N ADDITIONAL SUBJECTS
APPROVAL_REQUEST 1 ── 0..N REQUIREMENTS
APPROVAL_REQUEST 1 ── 0..N APPROVALS
PROJECT_ACTOR_BINDING 1 ── 0..N APPROVALS
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

---

# 17. Baselines

```text
PROJECT 1 ── 0..N BASELINES
BASELINE 1 ── 1..N BASELINE_VERSIONS
BASELINE_VERSION 1 ── 0..N BASELINE_ITEMS
BASELINE_VERSION 1 ── 0..N STATE_SNAPSHOTS
BASELINE_VERSION 1 ── 0..N REPOSITORY_SNAPSHOTS
BASELINE_VERSION 1 ── 0..1 ACTIVE APPROVAL_REQUEST
```

---

# 18. Documents e summaries

```text
DOCUMENT 1 ── 1..N DOCUMENT_VERSIONS
DOCUMENT_VERSION 1 ── 0..N ARTIFACTS
DOCUMENT N ── M DOCUMENTS

SUMMARY 1 ── 1..N SUMMARY_VERSIONS
SUMMARY_VERSION 1 ── 1..N SOURCES per stato VALID
SUMMARY_VERSION 1 ── 0..N COVERAGE
SUMMARY_VERSION 1 ── 0..N EXCLUSIONS
SUMMARY_VERSION 1 ── 0..N CLAIMS
SUMMARY_CLAIM 1 ── 1..N SOURCES per claim materiale
```

Le cardinalità `1..N` indicate come minimi di stato sono applicate dalle transizioni.

---

# 19. Events

```text
PROJECT 1 ── 0..N EVENTS
PROJECT_ENTITY 1 ── 0..N EVENTS come aggregate
EVENT 1 ── 1..N EVENT_SUBJECTS
```

Sequences unique per project e aggregate.

---

# 20. Security

```text
ACTOR N ── M PROJECTS tramite PROJECT_ACTOR_BINDINGS e MEMBERSHIPS
PROJECT 1 ── 0..N ROLES
ROLE 1 ── 1..N ROLE_VERSIONS
ROLE_VERSION 1 ── 0..N PERMISSION_BINDINGS
PROJECT_ACTOR_BINDING N ── M ROLE_VERSIONS
DELEGATION 1 ── 0..N DELEGATION_PERMISSIONS
```

Permission binding usa code/version/hash.

---

# 21. Transition e integrity

```text
TRANSITION_DEFINITION 1 ── 1..N VERSIONS
TRANSITION_VERSION 1 ── 0..N REQUIREMENTS
TRANSITION_VERSION 1 ── 0..N EFFECTS
TRANSITION_REQUEST 1 ── 0..N EVALUATIONS
TRANSITION_REQUEST 1 ── 0..1 SUCCESSFUL EXECUTION
TRANSITION_EXECUTION 1 ── 0..N EFFECT RESULTS
TRANSITION_EXECUTION 1 ── 0..N RECOVERY RUNS

INTEGRITY_RULE 1 ── 1..N RULE_VERSIONS
INTEGRITY_PROFILE 1 ── 1..N PROFILE_VERSIONS
PROFILE_VERSION N ── M RULE_VERSIONS
INTEGRITY_RUN 1 ── 0..N CHECK_RESULTS
```

---

# 22. Delete behavior

Default:

```text
ON DELETE RESTRICT
```

Cascade soltanto per child privati, non governati e rigenerabili.

---

# 23. Decisione consolidata

```text
DEC-0101-019
C-0101-001...009

Cardinalità strutturali e lifecycle
sono separati.

Report ownership è univoca
e usa owner entities canoniche.

Validation conserva step, run e results.

Cataloghi globali sono riferiti
senza foreign key cross-database.

Ogni relazione fondamentale
usa una tabella dedicata.
```
