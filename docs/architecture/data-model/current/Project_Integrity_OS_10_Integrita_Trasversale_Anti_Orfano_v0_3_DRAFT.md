# Project Integrity OS

## Integrità trasversale e anti-orfano — v0.3

**Stato:** DRAFT — modello consolidato, non ancora fonte autorevole
**Data:** 2026-08-06
**Task:** `TODO-0101`
**Decisioni:** `DEC-0101-015`, `DEC-0101-019`, `DEC-0101-020`
**Correzioni:** `C-0101-004`, `C-0101-005`, `C-0101-006`, `C-0101-009`
**Sostituisce:** `../history/decisions/Project_Integrity_OS_10_Integrita_Trasversale_Anti_Orfano_v0_2_DRAFT.md`

---

# 1. Principio

Ogni entità citabile deve:

- avere identità stabile;
- appartenere a un perimetro definito;
- essere risolvibile;
- avere specializzazione coerente;
- non diventare orfana;
- non attraversare silenziosamente il confine del progetto.

---

# 2. Tre scope logici

```text
SYSTEM_CATALOG
GLOBAL_REGISTRY
PROJECT_DATABASE
```

Nell'MVP possono essere materializzati in due database fisici:

```text
control database
= system catalog + global registry + actors

project database
= dati governati di un singolo progetto
```

Non si usa `project_id NULL` per mescolare semantiche globali e locali.

---

# 3. Root project entity

```text
projects.project_id = project_entities.entity_id
project_entities.project_id = projects.project_id
project_entities.entity_type = PROJECT
```

Creazione atomica.

Regole:

```text
ROOT_PROJECT_ENTITY_EXISTS
ROOT_PROJECT_ENTITY_ID_MATCHES_PROJECT_ID
ROOT_PROJECT_ENTITY_TYPE_IS_PROJECT
ROOT_PROJECT_ENTITY_REFERENCE_CODE_MATCHES
ROOT_PROJECT_ENTITY_IS_UNIQUE
```

---

# 4. Project entities

```text
entity_id
project_id
entity_type
reference_code
record_state
created_at
archived_at
```

Ogni tipo è classificato deterministicamente nell'Entity Catalog.

Categorie:

```text
PROJECT_ROOT
PROJECT_ENTITY
PROJECT_CONFIGURATION
DERIVED_PROJECTION
EXTERNAL_REFERENCE
```

Una configurazione project-local citabile è sempre una `project_entity`.

Una configurazione non citabile e puramente privata è dichiarata esplicitamente come child non governato.

Non viene usata la formula ambigua “può essere project_entity”.

---

# 5. Entity versions

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

Una entity version corrisponde a una sola tabella versionata specializzata.

Una version frozen non viene aggiornata.

---

# 6. System catalog

Esempi:

```text
permissions
classification_levels
handling_flag_definitions
event_types
relationship_type_templates
role_templates
access_policy_templates
approval_policy_templates
redaction_profile_templates
transition_templates
integrity_rule_templates
```

Caratteristiche:

- nessun `project_id`;
- codici stabili;
- catalog version;
- definition hash;
- nessuno stato operativo del singolo progetto.

---

# 7. Global registry

Contiene:

- project registry;
- database locations;
- schema metadata globale;
- actors;
- actor identities;
- actor sessions;
- system catalog version metadata.

Le relazioni dal project database non usano FK cross-database.

---

# 8. Binding locali

Il project database usa record locali riproducibili.

## Actor

```text
project_actor_bindings
```

## Catalog definition

Ogni binding conserva almeno:

```text
definition_code
catalog_version
definition_hash
bound_at
```

Esempi dedicati:

```text
role_permission_bindings
entity_classification_bindings
entity_handling_flag_bindings
project_template_bindings
event type fields negli events
relationship_type_bindings
```

Il core valida il binding al momento della creazione.

L'integrity engine può riconfrontare code, version e hash.

---

# 9. Isolamento progetto

Le relazioni interne usano, dove necessario:

```text
(project_id, entity_id)
(project_id, entity_version_id)
```

Nell'MVP non sono ammesse FK dirette cross-project.

Le fonti esterne usano:

```text
external_references
import_records
repository_snapshots
artifacts
provenance
```

---

# 10. Relazioni

Le relazioni fondamentali usano tabelle dedicate.

`entity_links` collega soltanto `project_entities`.

Tipi supplementari:

```text
RELATED_TO
SIMILAR_TO
INFORMED_BY
REFERENCES
NAVIGATES_TO
HISTORICALLY_ASSOCIATED_WITH
```

I relationship type globali usano template code/version/hash.

Le regole locali applicabili usano `relationship_type_bindings`.

---

# 11. Integrity engine

```text
integrity_rules
integrity_rule_versions
integrity_profiles
integrity_profile_versions
integrity_profile_rule_bindings
integrity_runs
integrity_check_results
```

Le rules e profiles operative sono project-local e project entities.

Possono derivare da template globali congelando code, catalog version e hash.

Livelli:

```text
SCHEMA
RELATIONAL
TYPE
PROJECT_BOUNDARY
VERSION
TEMPORAL
WORKFLOW
TRACEABILITY
CONTENT
EVENT
AGGREGATE
SECURITY
```

Enforcement:

```text
ADVISORY
REQUIRED
BLOCKING
FATAL
```

---

# 12. Anti-orphan

Controlli:

- root project entity presente;
- una sola specializzazione;
- entity type coerente;
- version specialization coerente;
- no cross-project FK;
- no mutation frozen;
- no recycled reference code;
- no generic link verso entità inesistente;
- no relation fondamentale rappresentata solo da generic link;
- no global catalog row nel project entity catalog;
- no project configuration priva di project_id;
- no binding globale senza code/version/hash;
- no report senza owner valido;
- no baseline item irrisolvibile;
- no Context Package source irrisolvibile;
- no invalid event subject;
- no forbidden cycle.

---

# 13. Enforcement

Database:

- PK, FK, unique, check;
- same-project constraints;
- structural cardinalities;
- no self-link;
- one specialization;
- one report ownership;
- sequences.

Core:

- factory atomiche;
- transition rules;
- catalog validation;
- state changes;
- idempotency.

Integrity engine:

- semantic orphan;
- cycles;
- temporal overlap;
- catalog drift;
- pointer divergence;
- reconstruction;
- aggregate consistency.

Frontend:

- presentazione;
- drill-down;
- nessuna autorità finale.

---

# 14. Decisione consolidata

```text
DEC-0101-015
C-0101-004...009

Project root, project entities
e entity versions formano il catalogo
universale project-local.

System catalog, global registry
e project database sono scope distinti.

I riferimenti globali usano binding
con code, catalog version e hash.

Ogni entity type è classificato
deterministicamente.

Il database impedisce orfani strutturali.
Il core impedisce transizioni invalide.
L'integrity engine rileva orfani semantici.
```
