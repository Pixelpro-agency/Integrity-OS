# Project Integrity OS

## Conservazione, archiviazione, rettifiche e cancellazione — v0.2

**Stato:** DRAFT — modello consolidato, non ancora fonte autorevole
**Data:** 2026-08-06
**Task:** `TODO-0101`
**Decisioni:** `DEC-0101-016`, `DEC-0101-015`, `DEC-0101-017`, `DEC-0101-018`, `DEC-0101-019`, `DEC-0101-020`
**Sostituisce:** `../history/decisions/Project_Integrity_OS_11_Conservazione_Rettifiche_Cancellazione_v0_1_DRAFT.md`

---

# 1. Principio

```text
non più operativo
≠ da eliminare
```

Operazioni distinte:

```text
ARCHIVE
WITHDRAW
VOID
SUPERSEDE
CORRECT
REDACT
PURGE_CONTENT
HARD_DELETE
RESTORE
TOMBSTONE
```

---

# 2. Classi di conservazione

## A — Governed immutable records

Esempi:

- events;
- final decision resolutions;
- approvals;
- frozen entity versions;
- original reports;
- evidence;
- completed command/test runs;
- completed verifications;
- approved baselines;
- completed integrity runs.

Regola:

```text
nessun hard delete ordinario
```

## B — Governed operational entities

Esempi:

- projects;
- phases;
- work items;
- tasks;
- requirements;
- register items;
- policies.

Usano archive, logical removal, supersession e restore.

## C — Unused drafts

Hard delete ammesso soltanto se:

- mai frozen;
- mai approved;
- mai delivered;
- mai baselined;
- mai usato in attempt;
- non referenziato;
- senza evento materiale dipendente;
- policy permissiva;
- assessment completato.

## D — Regenerable content

Cache, projection, preview e temporary export possono essere rigenerati.

---

# 3. Record state

```text
ACTIVE
DRAFT
INACTIVE
ARCHIVED
WITHDRAWN
VOIDED
SUPERSEDED
REVOKED
QUARANTINED
PENDING_DELETION
CONTENT_PURGED
TOMBSTONED
```

Non ogni entity type ammette ogni stato.

---

# 4. Entità

```text
retention_policies
retention_policy_versions
deletion_requests
deletion_assessments
deletion_actions
record_tombstones
redaction_records
correction_records
archive_records
restoration_records
deletion_certificates
```

Retention policies operative sono project-local project entities.

Possono derivare da template globali tramite code, catalog version e definition hash.

---

# 5. Target

Ogni operazione punta a:

```text
target_entity_id
target_entity_version_id
target_field_path
```

Per risorse esterne usa `external_reference_id`.

Non usa generic type/id non vincolati.

---

# 6. Retention policy

```text
retention_policy_id
project_id
reference_code
current_version_id
template_code
template_catalog_version
template_definition_hash
record_state
created_at
archived_at
```

La version definisce:

```text
target_entity_type_code
classification_level_code
default_retention_mode
minimum_retention_duration
maximum_retention_duration
archive_allowed
hard_delete_allowed
content_purge_allowed
redaction_allowed
restoration_allowed
approval_policy_version_id
content_hash
```

Modalità:

```text
PERMANENT
PROJECT_LIFETIME
UNTIL_BASELINE_SUPERSEDED
UNTIL_TASK_CLOSED
TIME_LIMITED
UNTIL_EXPLICIT_REVIEW
REGENERABLE
EXTERNAL_POLICY
```

---

# 7. Deletion request

Lifecycle:

```text
DRAFT
SUBMITTED
UNDER_ASSESSMENT
CHANGES_REQUESTED
APPROVED
REJECTED
SCHEDULED
EXECUTING
COMPLETED
COMPLETED_WITH_WARNINGS
PARTIALLY_COMPLETED
FAILED
CANCELLED
```

Azioni:

```text
ARCHIVE
WITHDRAW
VOID
REDACT
PURGE_CONTENT
HARD_DELETE
ANONYMIZE
CRYPTO_ERASE
TOMBSTONE
```

La richiesta è una project entity.

---

# 8. Assessment

L'assessment conta e valuta:

- relazioni;
- versioni frozen;
- baseline;
- Context Package;
- summary;
- verification;
- approvals;
- events;
- backup/export;
- repository;
- storage esterni;
- classificazione;
- legal hold;
- ricostruibilità;
- recovery e reversibilità.

Una valutazione incompleta blocca l'azione.

---

# 9. Approval

Una deletion approval usa il modello generale:

```text
approval_requests
approval_request_subjects
approval_requirements
approvals
```

L'actor è riferito tramite project actor binding.

Requester e approver rispettano separation of duties.

---

# 10. Correzioni

`correction_records` conserva:

```text
correction_record_id
project_id
target_entity_id
target_entity_version_id
target_field_path
original_value_hash
corrected_value
correction_type
reason
source_provenance_record_id
approval_request_id
effective_from
recorded_at
created_at
```

Per contenuti frozen si crea una nuova entity version.

Gli eventi append-only non vengono modificati.

---

# 11. Redazione

`redaction_records` conserva:

- target e field path;
- original hash;
- reason;
- classification;
- redaction action;
- redaction marker;
- reversibility;
- access policy;
- approvazione;
- actor;
- timestamp.

Azioni:

```text
MASK
REMOVE_FROM_VIEW
REMOVE_FROM_EXPORT
REPLACE_WITH_MARKER
TOKENIZE
ANONYMIZE
ENCRYPT_AND_RESTRICT
PURGE_ORIGINAL
```

La redazione resta visibile.

---

# 12. Purge e tombstone

Dopo purge restano almeno:

- entity identity;
- project;
- reference code;
- type;
- original hash;
- size;
- reason;
- policy version;
- approval;
- timestamp;
- replacement;
- tombstone hash.

I reference code non vengono riciclati.

---

# 13. Propagazione

Una fonte corretta, redatta, purgata o invalidata può rendere:

```text
STALE
VALID_WITH_LIMITATIONS
INVALID
INCOMPLETE_SOURCE
REGENERATION_REQUIRED
EVIDENCE_NO_LONGER_AVAILABLE
HISTORICALLY_VERIFIED_CONTENT_PURGED
```

su:

- summary;
- Context Package;
- verification;
- reconstruction;
- baseline;
- projection;
- export;
- AI analysis.

Gli effetti producono eventi e integrity check.

---

# 14. Project deletion

Workflow:

```text
request
→ freeze writes
→ inventory
→ assessment
→ optional export
→ approval
→ purge by class
→ global registry tombstone
→ integrity verification
→ deletion certificate
```

Il control database conserva il tombstone globale.

Il project database conserva o esporta il manifest previsto dalla policy prima della rimozione.

Stati distinti:

```text
PRIMARY_STORAGE_PURGED
ALL_MANAGED_COPIES_PURGED
EXTERNAL_COPIES_UNKNOWN
```

---

# 15. Repository

```text
working tree removal
≠ Git history removal
≠ remote deletion
```

Stati:

```text
FILE_REMOVED_FROM_CURRENT_TREE
GIT_HISTORY_STILL_CONTAINS_CONTENT
GIT_HISTORY_REWRITTEN
REMOTE_HISTORY_STATUS_UNKNOWN
```

Non viene dichiarata eliminazione completa senza evidenza.

---

# 16. Decisione consolidata

```text
DEC-0101-016

Retention e deletion operano su
project_entities ed entity_versions.

Policy operative sono project-local
e possono derivare da template globali
tramite binding riproducibile.

Approval usa il modello generale.
Actor usa project actor binding.

Correzione, redazione, purge e delete
non riscrivono silenziosamente lo storico.
```
