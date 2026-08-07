# Project Integrity OS

## Ruoli, permessi, sensibilità e redazione — v0.3

**Stato:** DRAFT — modello consolidato, non ancora fonte autorevole
**Data:** 2026-08-06
**Task:** `TODO-0101`
**Decisioni:** `DEC-0101-017`, `DEC-0101-015`, `DEC-0101-018`, `DEC-0101-019`, `DEC-0101-020`
**Correzioni:** `C-0101-005`, `C-0101-006`, `C-0101-007`, `C-0101-009`
**Sostituisce:** `../history/decisions/Project_Integrity_OS_12_Ruoli_Permessi_Sensibilita_Redazione_v0_2_DRAFT.md`

---

# 1. Principio

```text
identity
≠ project binding
≠ membership
≠ role
≠ permission
≠ scope
≠ ownership
≠ approval
```

Modello:

```text
RBAC
+
hierarchical scope
+
policy conditions
+
classification
+
handling flags
+
separation of duties
+
DEFAULT DENY
```

---

# 2. Storage e scope

## Control database

Contiene:

```text
actors
actor_identities
actor_sessions
permissions
classification_levels
handling_flag_definitions
security catalog metadata
```

## Project database

Contiene:

```text
project_actor_bindings
project_memberships
roles
role_versions
role_permission_bindings
actor_role_assignments
delegations
delegation_permissions
access_policies
approval_policies
redaction_profiles
entity_classifications
entity_handling_flags
security_reviews
```

Non esistono FK cross-database.

---

# 3. Actors

Tipi:

```text
HUMAN
AI
SYSTEM
TOOL
EXTERNAL_SERVICE
MIGRATION_PROCESS
```

`actors` usa UUID globale.

Il `reference_code` globale è univoco nel global registry e non viene riciclato.

Identities e sessions appartengono all'actor globale.

---

# 4. Project actor bindings

```text
project_actor_binding_id
project_id
actor_id
actor_reference_code
actor_type_snapshot
display_name_snapshot
global_registry_version
actor_definition_hash
binding_status
bound_at
revoked_at
```

Il binding locale:

- rende possibile la FK nel project database;
- non duplica credenziali;
- conserva identità globale e snapshot minimo;
- viene rivalidato quando necessario.

Membership, owner, executor e approver puntano al binding locale.

---

# 5. Membership

```text
project_membership_id
project_id
project_actor_binding_id
membership_status
valid_from
valid_until
invited_by_actor_binding_id
activated_at
suspended_at
revoked_at
```

Stati:

```text
INVITED
ACTIVE
SUSPENDED
REVOKED
EXPIRED
```

---

# 6. Permissions globali

`permissions` è un catalogo globale.

Esempi:

```text
task.read
task.update
task.execute
decision.resolve
approval.grant
evidence.read_sensitive
redaction.perform
deletion.approve
baseline.approve
security.break_glass
```

Ogni definition possiede:

```text
permission_code
catalog_version
definition_hash
```

---

# 7. Roles locali

```text
roles
role_versions
role_permission_bindings
```

`roles` è project-local e una project entity.

Una role version può derivare da:

```text
role_template_code
role_template_catalog_version
role_template_definition_hash
```

`role_permission_bindings` conserva:

```text
role_version_id
permission_code
permission_catalog_version
permission_definition_hash
effect
constraints_json
created_at
```

Non usa FK cross-database.

Il core valida il binding.

---

# 8. Role assignments

```text
actor_role_assignment_id
project_id
project_actor_binding_id
role_version_id
scope_entity_id
inherit_to_descendants
valid_from
valid_until
assigned_by_actor_binding_id
status
created_at
```

Ogni scope root è una project entity.

Ownership non attribuisce automaticamente permission.

---

# 9. Delegations

```text
delegations
delegation_permissions
```

`delegations` non contiene una lista autorevole di permission.

Ogni permission delegata è una riga in `delegation_permissions` con code/version/hash.

La delega:

- non supera il grantor;
- non estende lo scope;
- non è trasferibile;
- è revocabile;
- scade;
- può avere numero massimo di usi;
- viene auditata.

---

# 10. Separation of duties

Livelli:

```text
NOT_REQUIRED
RECOMMENDED
REQUIRED
STRICT
```

Regole iniziali:

```text
executor != verifier
verifier != final approver
deletion requester != deletion approver
role assignment requester != approver
exception requester != exception approver
```

Un'IA non può approvare la propria esecuzione o estendere autonomamente il proprio scope.

---

# 11. Classificazione

Cataloghi globali:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
```

Handling flags:

```text
PERSONAL_DATA
CREDENTIAL
SECURITY_SENSITIVE
LEGAL_HOLD
THIRD_PARTY_CONFIDENTIAL
EXPORT_RESTRICTED
DELETION_RESTRICTED
AUDIT_REQUIRED
```

Nel project database:

```text
entity_classifications
field_classifications
entity_handling_flags
classification_changes
```

Ogni binding conserva code, catalog version e definition hash.

---

# 12. Access policy

Ordine:

```text
identity
→ session
→ project actor binding
→ membership
→ project
→ target
→ scope
→ role
→ permission binding
→ classification
→ handling flags
→ state
→ separation of duties
→ integrity
→ explicit deny
→ preventive approval
→ decision
```

Esiti:

```text
ALLOW
ALLOW_WITH_REDACTION
ALLOW_WITH_CONDITIONS
DENY
REQUIRE_APPROVAL
INDETERMINATE
```

Errore tecnico su azione protetta produce deny o indeterminate non permissivo.

---

# 13. Redaction

Redaction profile operativo è project-local e versionato.

Può derivare da template globale tramite code/version/hash.

Azioni:

```text
ALLOW
MASK
REMOVE
REPLACE_WITH_MARKER
TOKENIZE
HASH_ONLY
METADATA_ONLY
REFERENCE_ONLY
DENY_ENTITY
```

Copre:

- content;
- metadata;
- filename;
- logs;
- summary;
- cache;
- export;
- Context Package;
- provider esterno.

---

# 14. Session e Context Package

La session globale può indicare un active project.

Il project database conserva la delivery autorizzata.

Un `actor_session.context_package_version_id` è valido soltanto se:

- la package version appartiene all'active project;
- il recipient actor corrisponde;
- la delivery è autorizzata;
- l'hash consegnato corrisponde.

L'integrity engine verifica la coerenza.

---

# 15. Security review

```text
security_reviews
security_review_versions
security_review_findings
security_review_evidence
```

Una `SECURITY_REPORT` possiede come owner autorevole una `SECURITY_REVIEW`.

Questo elimina owner types non modellati.

---

# 16. AI

Una IA può:

- analizzare;
- proporre;
- eseguire entro scope;
- produrre report;
- generare finding;
- effettuare verifiche autorizzate.

Non può autonomamente:

- assegnarsi ruoli;
- estendere scope;
- approvare la propria esecuzione;
- ridurre classificazioni;
- modificare policy;
- disabilitare integrity rules;
- cancellare evidence;
- autorizzare purge;
- impersonare un approvatore umano.

---

# 17. Decisione consolidata

```text
DEC-0101-017
C-0101-005...009

Actors, identities, sessions
e cataloghi di sicurezza sono globali.

Il project database usa
project_actor_bindings e binding locali
code/version/hash.

Roles e policies operative sono
project-local e versionate.

Delegation permissions sono righe dedicate,
non liste JSON autorevoli.

Security reports sono owned
da security reviews modellate.
```
