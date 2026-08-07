# Project Integrity OS

## Ruoli, permessi, sensibilità e redazione — v0.2

**Stato:** DRAFT — modello corretto e consolidato
**Data:** 2026-08-06
**Task:** `TODO-0101`
**Decisione primaria:** `DEC-0101-017`
**Correzione applicata:** `C-0101-005`
**Sostituisce:** `Project_Integrity_OS_12_Ruoli_Permessi_Sensibilita_Redazione_TODO-0101_v0_1_DRAFT.md`

---

# 1. Principio

```text
identità globale
≠ appartenenza al progetto
≠ ruolo
≠ permesso
≠ scope
≠ ownership
≠ approvazione
```

Il modello usa:

```text
RBAC
+
scope gerarchico
+
condizioni di policy
+
classificazione
+
separation of duties
+
DEFAULT DENY
```

---

# 2. Livelli di scope

## Identità globale

```text
actors
actor_identities
actor_sessions
```

Queste entità identificano persone, IA, tool e servizi.

`actors` non possiede `project_id`.

Tipi:

```text
HUMAN
AI
SYSTEM
TOOL
EXTERNAL_SERVICE
MIGRATION_PROCESS
```

## Appartenenza al progetto

```text
project_memberships
```

Cardinalità:

```text
ACTOR N ── M PROJECT tramite PROJECT_MEMBERSHIPS
```

Ogni membership registra:

```text
project_membership_id
project_id
actor_id
membership_status
valid_from
valid_until
invited_by_actor_id
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

## Assegnazione dei ruoli

```text
actor_role_assignments
```

Ogni assegnazione è project-local e possiede:

```text
project_id NOT NULL
actor_id
role_version_id
scope_entity_id
inherit_to_descendants
valid_from
valid_until
assigned_by_actor_id
status
```

---

# 3. Cataloghi globali

## Permissions

`permissions` è un catalogo globale stabile.

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

Il catalogo non possiede `project_id`.

## Classification levels

Catalogo globale:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
```

## Handling flags

Catalogo globale:

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

## Templates

Possono essere globali:

```text
role_templates
access_policy_templates
approval_policy_templates
redaction_profile_templates
```

I template non contengono assegnazioni operative di un progetto.

---

# 4. Configurazioni project-local

## Roles

```text
roles
role_versions
role_permissions
```

`roles.project_id` è obbligatorio.

Un ruolo locale può riferirsi a un `role_template_id`.

Ruoli iniziali:

```text
PROJECT_OWNER
PROJECT_ADMINISTRATOR
ARCHITECT
ANALYST
DOCUMENT_AUTHOR
EXECUTOR
VERIFIER
VALIDATOR
APPROVER
AUDITOR
SECURITY_OFFICER
READ_ONLY
SYSTEM_OPERATOR
```

Il ruolo locale conserva la versione esatta dei permission code applicati.

## Policies

Sono project-local e versionate:

```text
access_policies
approval_policies
redaction_profiles
retention_policies
```

Possono derivare da template globali.

---

# 5. Attori e sessioni

## `actors`

Campi:

```text
actor_id
reference_code
actor_type
display_name
status
trust_level
created_at
disabled_at
archived_at
```

## `actor_identities`

```text
actor_identity_id
actor_id
identity_type
provider
external_identifier
model_or_tool_name
model_or_tool_version
credential_reference
status
verified_at
revoked_at
```

I segreti non vengono memorizzati in chiaro.

## `actor_sessions`

```text
actor_session_id
actor_id
actor_identity_id
active_project_id
session_type
started_at
expires_at
ended_at
status
authentication_strength
origin
context_package_version_id
delegation_id
```

`active_project_id` identifica il contesto operativo, ma non attribuisce membership o permessi.

---

# 6. Delega

```text
delegations
```

Ogni delega specifica:

```text
project_id
grantor_actor_id
grantee_actor_id
grantee_session_id
scope_entity_id
allowed_permissions
valid_from
valid_until
maximum_uses
constraints
status
```

La delega:

- non supera i permessi del grantor;
- non estende lo scope del grantor;
- non è trasferibile;
- è revocabile;
- scade;
- viene tracciata.

---

# 7. Separazione dei ruoli

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
verifier != final_approver
deletion_requester != deletion_approver
role_assignment_requester != role_assignment_approver
exception_requester != exception_approver
```

Una eccezione non può derogare regole dichiarate non derogabili.

---

# 8. IA

Una IA può:

- analizzare;
- proporre;
- eseguire entro lo scope;
- produrre report;
- generare finding;
- effettuare verifiche tecniche autorizzate.

Non può autonomamente:

```text
assegnarsi ruoli;
estendere lo scope;
approvare la propria esecuzione;
ridurre classificazioni;
modificare policy;
disabilitare integrity rule;
cancellare evidence;
autorizzare purge;
impersonare un approvatore umano.
```

Le operazioni tool conservano:

```text
initiated_by
executed_by
on_behalf_of
authorized_by
```

---

# 9. Classificazione

Le classificazioni operative sono project-local:

```text
entity_classifications
field_classifications
classification_changes
```

Esse riferiscono codici globali di livello e handling flag.

Regola di ereditarietà:

```text
derived_classification
=
massima classificazione materiale delle fonti
```

Una riduzione richiede redazione, anonimizzazione o declassificazione approvata.

---

# 10. Access policy

Ordine di valutazione:

```text
identità
→ sessione
→ membership
→ progetto
→ target
→ scope
→ ruolo
→ permesso
→ classificazione
→ handling restrictions
→ stato
→ separation of duties
→ integrità
→ deny espliciti
→ approval preventive
→ ALLOW o DENY
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

Regole:

```text
DEFAULT DENY
explicit deny prevale
errore tecnico su azione protetta → DENY
```

---

# 11. Redazione

Redazione dinamica:

```text
fonte immutata
→ vista filtrata
```

Derivato sanitizzato:

```text
fonte
→ nuova versione sanitizzata
→ source link
→ redaction manifest
→ hash
→ verifica
```

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

La redazione deve coprire anche:

- metadata;
- filename;
- log;
- summary;
- cache;
- export;
- Context Package;
- provider esterno.

---

# 12. Audit e break-glass

Devono essere registrati:

- accessi RESTRICTED;
- export;
- declassificazione;
- purge;
- hard delete;
- assegnazione ruoli;
- modifiche policy;
- break-glass;
- accessi amministrativi.

Il break-glass richiede:

```text
motivo
scope limitato
durata
autorizzazione
audit completo
post-review
```

Non consente di eliminare audit, modificare eventi o riscrivere versioni frozen.

---

# 13. MVP

Configurazione iniziale:

```text
un actor umano locale;
un system actor;
project membership ACTIVE;
ruolo locale PROJECT_OWNER;
actor separati per IA e tool;
sessioni tracciate;
deleghe limitate;
INTERNAL come default di classificazione;
DEFAULT DENY per azioni critiche.
```

Nessun bypass universale viene hardcoded.

---

# 14. Decisione consolidata

```text
DEC-0101-017 + C-0101-005

actors, identities e sessions sono globali.

L'appartenenza al progetto usa project_memberships.

permissions, classification levels, handling flags
e template sono cataloghi globali.

roles, assignments, policies, classificazioni
e redaction profiles operativi sono project-local.

Ogni autorizzazione include sempre project_id,
membership, scope, stato, sensibilità e policy.

Il backend e il core Rust sono l'autorità finale.
```
