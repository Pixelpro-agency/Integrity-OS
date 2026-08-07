# Project Integrity OS

## Integrità trasversale e anti-orfano — v0.2

**Stato:** DRAFT — modello corretto e consolidato
**Data:** 2026-08-06
**Task:** `TODO-0101`
**Decisione primaria:** `DEC-0101-015`
**Correzioni applicate:** `C-0101-004`, `C-0101-005`
**Sostituisce:** `Project_Integrity_OS_10_Integrita_Trasversale_Anti_Orfano_TODO-0101_v0_1_DRAFT.md`

---

# 1. Principio

Ogni entità citabile deve:

- avere una identità stabile;
- appartenere a un progetto;
- essere risolvibile;
- avere relazioni verificabili;
- non diventare orfana;
- non attraversare silenziosamente il confine del progetto.

I cataloghi tecnici globali sono distinti dalle entità governate di progetto.

---

# 2. Root identity del progetto

Ogni progetto è anche la root entity del proprio grafo.

```text
projects.project_id = project_entities.entity_id
project_entities.project_id = projects.project_id
project_entities.entity_type = PROJECT
```

Cardinalità:

```text
PROJECT 1 ── 1 ROOT PROJECT_ENTITY
PROJECT 1 ── 0..N OTHER PROJECT_ENTITIES
```

La riga root usa:

- lo stesso UUID del progetto;
- lo stesso `reference_code`;
- `entity_type = PROJECT`;
- stato coerente con il progetto.

`projects` non possiede una FK inversa obbligatoria verso `project_entities`.

Il core crea progetto e root entity nella stessa transazione.

Una integrity rule verifica:

```text
ROOT_PROJECT_ENTITY_EXISTS
ROOT_PROJECT_ENTITY_ID_MATCHES_PROJECT_ID
ROOT_PROJECT_ENTITY_TYPE_IS_PROJECT
ROOT_PROJECT_ENTITY_REFERENCE_CODE_MATCHES
ROOT_PROJECT_ENTITY_IS_UNIQUE
```

---

# 3. `project_entities`

Campi comuni:

```text
entity_id
project_id
entity_type
reference_code
record_state
created_at
archived_at
```

Ogni entità citabile project-local possiede una riga in `project_entities`.

La tabella specializzata condivide lo stesso UUID.

Esempio:

```text
project_entities.entity_id = tasks.task_id
```

Ogni `entity_type` deve corrispondere a una sola tabella specializzata.

---

# 4. `entity_versions`

Ogni versione citabile possiede:

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

La versione comune non sostituisce la tabella specializzata.

Una versione frozen:

- non viene aggiornata;
- non cambia owner;
- non cambia contenuto;
- non cambia hash;
- può essere soltanto superseded, revoked o invalidated tramite eventi e nuove versioni.

---

# 5. Confine tra cataloghi globali e progetto

## System catalog

I cataloghi globali:

- non possiedono `project_id`;
- non sono `project_entities`;
- usano codici stabili;
- sono versionati con la versione dell'applicazione o del catalogo;
- non possono contenere stato operativo di un singolo progetto.

Esempi:

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

## Project-local governed configuration

Le configurazioni operative applicate a un progetto:

- possiedono `project_id NOT NULL`;
- possono essere `project_entities`;
- sono versionate;
- possono derivare da un template globale;
- restano riproducibili anche dopo un aggiornamento del template.

Esempi:

```text
roles
transition_definitions
integrity_rules
access_policies
approval_policies
retention_policies
redaction_profiles
```

Non si usa `project_id NULL` per mescolare i due livelli nella stessa semantica.

---

# 6. Isolamento del progetto

Le relazioni project-local usano, dove necessario, FK composite:

```text
(project_id, entity_id)
```

Regola:

```text
source.project_id = target.project_id
```

Nell'MVP non sono ammesse FK dirette cross-project.

Le fonti esterne vengono modellate tramite:

```text
external_references
import_records
repository_snapshots
artifacts
hash
provenance
```

---

# 7. Relazioni fondamentali e generiche

Le relazioni fondamentali usano tabelle dedicate.

`entity_links` può collegare soltanto record già presenti in `project_entities`.

Campi minimi:

```text
entity_link_id
project_id
source_entity_id
source_entity_version_id
target_entity_id
target_entity_version_id
relationship_type_id
valid_from
valid_until
created_by_actor_id
created_at
```

`relationship_types` o i relativi template definiscono:

- source type ammessi;
- target type ammessi;
- direzionalità;
- transitività;
- simmetria;
- possibilità di ciclo;
- cardinalità;
- enforcement.

---

# 8. Integrity engine

Struttura:

```text
integrity_rules
integrity_rule_versions
integrity_profiles
integrity_profile_versions
integrity_profile_rule_bindings
integrity_runs
integrity_check_results
```

I template globali possono inizializzare le regole locali.

Ogni binding punta a versioni esatte.

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

# 9. Regole anti-orfano

Controlli minimi:

```text
project root entity presente;

specializzazione coerente con entity_type;

versione specializzata coerente con entity_versions;

nessuna FK project-local verso altro progetto;

nessuna versione frozen mutata;

nessun reference_code riciclato;

nessun link generico verso entità inesistente;

nessuna relazione fondamentale rappresentata
soltanto da entity_links;

nessun catalogo globale con stato operativo di progetto;

nessuna configurazione locale priva di project_id;

nessun ciclo vietato;

nessun evento senza aggregate e subject;

nessuna baseline con item irrisolvibili;

nessun Context Package con fonte irrisolvibile.
```

---

# 10. Enforcement

```text
database
→ FK, unique, check, project boundary e invarianti strutturali;

core Rust
→ creazione atomica, transizioni e regole di dominio;

integrity engine
→ cicli, orfani semantici, sovrapposizioni,
  divergenze e ricostruibilità;

frontend
→ presentazione e drill-down, mai autorità finale.
```

Le violazioni materiali producono finding:

```text
register_item_type = FINDING
finding_type = INTEGRITY_VIOLATION
```

---

# 11. Decisione consolidata

```text
DEC-0101-015 + C-0101-004 + C-0101-005

Ogni progetto possiede una root project entity
con lo stesso UUID tecnico.

project_entities cataloga tutte le entità citabili
project-local.

I cataloghi globali non usano project_id
e non sono project_entities.

Le configurazioni operative locali possiedono
project_id, versioni e relazioni verificabili.

Le relazioni fondamentali usano tabelle dedicate.

L'integrity engine verifica specializzazioni,
confini di progetto, versioni, temporalità,
traceability, eventi e sicurezza.
```
