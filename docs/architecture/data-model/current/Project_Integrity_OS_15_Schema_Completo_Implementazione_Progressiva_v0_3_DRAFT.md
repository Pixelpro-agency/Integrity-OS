# Project Integrity OS

## Schema completo e implementazione progressiva — v0.3

**Stato:** DRAFT — modello consolidato, non ancora fonte autorevole
**Data:** 2026-08-06
**Task:** `TODO-0101`
**Decisione primaria:** `DEC-0101-020`
**Correzioni:** `C-0101-001`, `C-0101-004` → `C-0101-009`
**Sostituisce:** `../history/decisions/Project_Integrity_OS_15_Schema_Completo_Implementazione_Progressiva_v0_2_DRAFT.md`

---

# 1. Principio

```text
complete canonical schema
+
progressive physical schema
+
capabilities enabled only when integral
```

Lo schema minimo non è il minor numero di tabelle.

È il più piccolo modello capace di preservare identità, relazioni, storia, verificabilità e portabilità.

---

# 2. Livelli

```text
L0 — CONCEPTUAL
L1 — LOGICAL
L2 — PHYSICAL
L3 — RUNTIME
L4 — PRODUCT
```

`TODO-0101` completa L0 e L1.

`TODO-0102` materializza le prime wave L2 e runtime minimo.

`TODO-0103` materializza il global project registry.

---

# 3. Tre scope logici e due database MVP

## SYSTEM_CATALOG

Definizioni globali versionate:

- permissions;
- classification levels;
- handling flags;
- event types;
- relationship templates;
- role templates;
- policy templates;
- transition templates;
- integrity rule templates.

## GLOBAL_REGISTRY

- projects registry;
- database locations;
- schema metadata globale;
- actors;
- identities;
- sessions;
- system catalog version metadata.

## PROJECT_DATABASE

- progetto e root entity;
- dominio;
- workflow;
- configurazioni locali;
- events;
- evidence;
- versions;
- baselines;
- policies.

Materializzazione MVP:

```text
CONTROL DATABASE
= SYSTEM_CATALOG + GLOBAL_REGISTRY

ONE PROJECT DATABASE PER PROJECT
= PROJECT_DATABASE
```

---

# 4. Relazioni tra database

SQLite non fornisce FK autorevoli tra database separati.

Pertanto i riferimenti globali usano:

```text
stable code
catalog version
definition hash
local binding
```

Actors usano `project_actor_bindings`.

Permissions usano `role_permission_bindings`.

Classification e handling flag usano binding locali.

Template derivations conservano code/version/hash.

Il core valida i binding.

L'integrity engine rileva drift.

---

# 5. Nessun placeholder incompatibile

Non vengono usati come sostituti del modello:

```text
generic_records
future_data_json
all_links_json
metadata_blob
nullable project_id per distinguere global/local
```

JSON conserva dettagli estensibili, non identità e relazioni fondamentali.

---

# 6. Cardinalità

Data Dictionary e Relationship Matrix distinguono:

```text
structural_min
structural_max
transition_required_min
required_from_state
required_for_transition
enforcement_layer
```

---

# 7. Wave 0 — Control and project foundation

## TODO-0102 project database foundation

```text
schema_migrations
database_metadata
projects
project_entities
entity_versions
project_actor_bindings
project_memberships
events minimi
integrity metadata minimo
```

Creazione atomica:

```text
project
+
root project entity
+
initial actor binding
+
owner membership
```

## TODO-0103 control database

```text
global_project_registry
actors
actor_identities
actor_sessions
system_catalog_versions
minimum system catalog seed
```

TODO-0102 può usare una fixture o binding bootstrap controllato finché TODO-0103 non è disponibile, senza fingere che il registry sia già implementato.

---

# 8. Wave 1 — Governed work

```text
phases
work_items
tasks
objectives
requirements + versions
acceptance criteria + versions
Task Contract + versions
documents + versions
decisions + versions
register items + versions
dependencies
transition definitions minime
roles locali minimi
integrity profile minimo
```

---

# 9. Wave 2 — Governed execution

```text
task_executions
attempts
prompts + versions
Context Package + versions
reports + versions
report ownership
report subjects
repository snapshots
command runs
test definitions + versions
test runs
```

---

# 10. Wave 3 — Verification and closure

```text
evidence
reconciliations
verifications
validations
validation step runs
validation results
approval requests
approvals
exceptions
bugs
findings
transition recovery runs
```

---

# 11. Wave 4 — Baseline and history

```text
baselines + versions
state snapshots
state reconstructions
summaries + versions
summary claims
provenance completa
event journal avanzato
projection checkpoints
```

---

# 12. Wave 5 — Advanced governance

```text
integrity rules e profiles completi
configurable roles
advanced policies
classification assignments
redaction
retention
deletion workflows
break-glass
security reviews
security audit
import/export records
```

---

# 13. Maturity dimensions

```text
definition_status
storage_status
runtime_status
verification_status
activation_status
```

Una capability diventa `ENABLED` soltanto quando:

- logical model completo;
- migration applicata;
- runtime implementato;
- transitions presenti;
- events presenti;
- authorization presente;
- integrity profile presente;
- test passati;
- recovery definito;
- UI coerente quando prevista.

---

# 14. Canonical types

| Tipo canonico | SQLite | PostgreSQL |
|---|---|---|
| UUID | TEXT canonico | UUID |
| REFERENCE_CODE | TEXT | TEXT/VARCHAR |
| BOOLEAN | INTEGER CHECK 0/1 | BOOLEAN |
| INT32 | INTEGER con range | INTEGER |
| INT64 | INTEGER | BIGINT |
| SEQUENCE | INTEGER | BIGINT |
| TIMESTAMP_UTC | TEXT RFC 3339 UTC | TIMESTAMPTZ |
| DATE | TEXT ISO 8601 | DATE |
| JSON | TEXT validato | JSONB |
| HASH_SHA256 | TEXT hex | CHAR(64)/TEXT |
| ENUM_CODE | TEXT + catalog/check | TEXT + catalog/check |
| DECIMAL | rappresentazione governata | NUMERIC |
| BINARY_SMALL | BLOB | BYTEA |

---

# 15. Entity classification

Ogni entità viene classificata esattamente come una delle seguenti:

```text
SYSTEM_CATALOG
GLOBAL_REGISTRY
PROJECT_ROOT
PROJECT_ENTITY
PROJECT_CONFIGURATION
DERIVED_PROJECTION
EXTERNAL_REFERENCE
PRIVATE_CHILD
```

Nessuna classificazione “opzionale”.

---

# 16. Deliverable TODO-0101

```text
Schema Architecture
Entity Catalog
Data Dictionary
Relationship Matrix
Constraint Catalog
State and Transition Catalog
Portability Matrix
Implementation Wave Matrix
Coverage Check
Open Issues Register
```

Il presente set completa il consolidamento preliminare, non sostituisce tali deliverable.

---

# 17. Criteri di chiusura

- root project entity;
- cataloghi globali separati;
- global binding strategy definita;
- actors storage definito;
- BUG nel registro;
- report ownership univoca;
- owner report canonici;
- validation history completo;
- lifecycle minimum fuori dal DDL strutturale;
- project_id NOT NULL per project-local;
- mapping SQLite/PostgreSQL;
- brief precedente superseded;
- storico documentale corretto;
- nessun blocker aperto.

---

# 18. Decisione consolidata

```text
DEC-0101-020
C-0101-001...009

TODO-0101 definisce il modello logico completo.

L'MVP usa due database fisici:
control database e project database.

I tre scope logici restano distinti.

I riferimenti globali usano binding
code/version/hash, non FK cross-database.

TODO-0102 e TODO-0103 materializzano
wave diverse senza introdurre righe finte.

Una capability è attiva soltanto
quando storage, runtime, verification
e recovery sono completi.
```
