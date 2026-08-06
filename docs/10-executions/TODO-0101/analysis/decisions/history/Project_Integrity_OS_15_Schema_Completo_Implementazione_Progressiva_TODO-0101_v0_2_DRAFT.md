# Project Integrity OS

## Schema completo e implementazione progressiva — v0.2

**Stato:** DRAFT — modello corretto e consolidato  
**Data:** 2026-08-06  
**Task:** `TODO-0101`  
**Decisione primaria:** `DEC-0101-020`  
**Correzioni applicate:** `C-0101-001`, `C-0101-004`, `C-0101-005`  
**Sostituisce:** `Project_Integrity_OS_15_Schema_Completo_Implementazione_Progressiva_TODO-0101_v0_1_DRAFT.md`

---

# 1. Principio

```text
schema logico completo
+
schema fisico progressivo
+
capacità attivate soltanto quando integre
```

Lo schema minimo non è il minor numero di tabelle.

È il più piccolo modello che conserva identità, relazioni, storia, verificabilità e portabilità.

---

# 2. Tre livelli distinti

```text
SCHEMA CANONICO COMPLETO
SCHEMA FISICO INSTALLATO
CAPACITÀ APPLICATIVA ATTIVA
```

Una tabella installata non rende automaticamente disponibile una funzione.

---

# 3. Livelli di definizione

```text
L0 — CONCEPTUAL
L1 — LOGICAL
L2 — PHYSICAL
L3 — RUNTIME
L4 — PRODUCT
```

`TODO-0101` completa L0 e L1.

`TODO-0102` materializza L2 e parte di L3.

---

# 4. Due perimetri di persistenza

Il modello distingue:

## System catalog / global registry

Contiene:

- versioni schema;
- database metadata;
- global project registry;
- actor identities quando materializzate globalmente;
- permission codes;
- classification levels;
- event types;
- relationship templates;
- role templates;
- transition templates;
- integrity rule templates.

Non usa `project_id` per simulare righe globali.

## Project database

Contiene:

- progetto e root project entity;
- entità di dominio;
- configurazioni project-local;
- workflow;
- eventi;
- evidence;
- versioni;
- baseline;
- policy locali.

Ogni entità governata project-local usa `project_id NOT NULL`.

---

# 5. Nessun placeholder incompatibile

Non vengono usati:

```text
generic_records
future_data_json
all_links_json
metadata_blob
nullable project_id per distinguere globale/locale
```

come sostituti di un modello già deciso.

JSON conserva dettagli estensibili, non relazioni autorevoli.

---

# 6. Cardinalità e lifecycle

Il Data Dictionary e la Relationship Matrix devono distinguere:

```text
structural_min
structural_max
transition_required_min
required_from_state
required_for_transition
```

Esempio:

```text
TASK → TASK_CONTRACT
structural: 0..1
required for TASK → DEFINED: 1 draft
required for TASK → READY: 1 frozen version
```

Non viene incorporato nel DDL un minimo che rende impossibile la creazione valida di un draft.

---

# 7. Wave 0 — Foundation

Elementi minimi:

```text
schema_migrations
database_metadata
projects
project_entities
entity_versions
system catalog version metadata
actor locale minimo
project_membership locale
```

La creazione progetto include atomicamente:

```text
projects row
+
root project_entities row
```

La wave distingue il database di progetto dal global project registry.

---

# 8. Wave 1 — Governed work management

Include:

```text
phases
work_items
tasks
objectives
requirements
acceptance criteria
Task Contract
documents
decisions
register items
BUG
dipendenze
transizioni
eventi
ruoli locali minimi
integrity profile minimo
```

Le configurazioni locali possono derivare da template globali, ma vengono congelate nel progetto.

---

# 9. Wave 2 — Governed execution

Include:

```text
task_executions
attempts
prompts
Context Package
reports
report_ownerships
report_subjects
repository_snapshots
command_runs
test_runs
```

Ogni report ha un solo owner autorevole fin dalla prima implementazione.

---

# 10. Wave 3 — Verification and closure

Include:

```text
evidence
reconciliations
verifications
validations
approvals
exceptions
bugs
findings
```

I minimi dipendenti dal lifecycle vengono applicati dal transition engine.

---

# 11. Wave 4 — Baseline and historical intelligence

Include:

```text
baselines
state_snapshots
state_reconstructions
summaries
summary claims
provenance completa
event journal avanzato
projection checkpoints
```

Le entità possono nascere in draft con cardinalità strutturali permissive, ma non avanzano senza completezza.

---

# 12. Wave 5 — Advanced integrity, security and retention

Include:

```text
integrity rules e profiles completi
project roles configurabili
policy avanzate
classification assignments
redaction
retention
deletion workflows
break-glass
security audit
```

I cataloghi globali necessari sono seed di sistema versionati.

Le configurazioni operative restano project-local.

---

# 13. Stati di maturità

```text
definition_status
storage_status
runtime_status
verification_status
activation_status
```

La capacità può essere `ENABLED` soltanto quando:

- modello completo;
- migration applicata;
- runtime implementato;
- transizioni presenti;
- eventi presenti;
- autorizzazioni presenti;
- integrity profile presente;
- test superati;
- recovery definito;
- UI coerente.

---

# 14. Tipi canonici

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
| HASH_SHA256 | TEXT esadecimale | CHAR(64)/TEXT |
| ENUM_CODE | TEXT + check/catalogo | TEXT + check/catalogo |
| DECIMAL | rappresentazione governata | NUMERIC |
| BINARY_SMALL | BLOB | BYTEA |

I cataloghi globali usano codici stabili.

Le configurazioni locali usano UUID e versioni.

---

# 15. Deliverable richiesti

TODO-0101 richiede:

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

La Relationship Matrix deve avere colonne separate per cardinalità strutturale e requisiti di transizione.

L'Entity Catalog deve classificare ogni entità come:

```text
SYSTEM_CATALOG
GLOBAL_REGISTRY
PROJECT_ROOT
PROJECT_ENTITY
PROJECT_CONFIGURATION
DERIVED_PROJECTION
EXTERNAL_REFERENCE
```

---

# 16. Criteri di chiusura

```text
progetto rappresentato come root entity;

cataloghi globali separati dalle configurazioni locali;

BUG presente nel register item catalog;

report ownership univoca;

cardinalità lifecycle-dependent fuori dal DDL strutturale;

project_id NOT NULL per entità project-local;

nessun uso di project_id NULL come discriminante globale;

mapping SQLite/PostgreSQL documentato;

brief precedente sostituito;

Decision Log e checkpoint aggiornati;

open issue bloccanti risolti.
```

---

# 17. Decisione consolidata

```text
DEC-0101-020 + C-0101-001 + C-0101-004 + C-0101-005

TODO-0101 definisce integralmente il modello logico.

TODO-0102 materializza lo schema per wave verticali.

System catalog, global registry e project database
sono perimetri distinti.

Le cardinalità strutturali non incorporano
obblighi dipendenti dal lifecycle.

Ogni capacità viene attivata soltanto
quando storage, runtime, verifica e recovery
sono completi.
```
