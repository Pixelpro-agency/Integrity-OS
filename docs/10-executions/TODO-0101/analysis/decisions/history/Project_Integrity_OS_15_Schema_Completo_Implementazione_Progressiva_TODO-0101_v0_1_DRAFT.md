# Project Integrity OS

## Schema completo e implementazione progressiva — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task collegata:** `TODO-0101 — Definire schema dati minimo`  
**Decisione collegata:** `DEC-0101-020 — APPROVED`

---

# 1. Significato di schema minimo

Schema minimo non significa:

```text
il minor numero possibile di tabelle
```

Significa:

```text
il più piccolo modello capace di preservare
identità, significato, relazioni, storia,
verificabilità e futura evoluzione
```

La scelta approvata è:

```text
schema logico completo ora
+
implementazione fisica progressiva
+
attivazione per capacità verticali complete
```

---

# 2. Distinzioni

## Schema canonico completo

Rappresenta il modello target approvato:

- entità;
- colonne;
- tipi;
- chiavi;
- cardinalità;
- vincoli;
- versioni;
- lifecycle;
- relazioni;
- regole di integrità.

## Schema fisico installato

Rappresenta le tabelle, migration e indici realmente presenti in una specifica versione del database.

Può essere un sottoinsieme del modello canonico.

## Capacità applicativa attiva

Rappresenta ciò che il prodotto può realmente utilizzare in modo governato, verificato e sicuro.

La presenza di una tabella non rende automaticamente disponibile una funzione.

---

# 3. Livelli di maturità

```text
L0 — CONCEPTUAL
L1 — LOGICAL
L2 — PHYSICAL
L3 — RUNTIME
L4 — PRODUCT
```

## L0

Significato, responsabilità, confini e lifecycle.

## L1

Tabelle logiche, colonne, tipi, PK, FK, cardinalità, associazioni, indici e regole.

`TODO-0101` deve completare questo livello.

## L2

DDL SQLite, migration, mapping fisico, indici, trigger e ordine di installazione.

Responsabilità principale di `TODO-0102`.

## L3

Adapter Rust, repository, servizi, transazioni, transition engine, integrity engine, recovery e test.

## L4

UI, dashboard, azioni, drill-down e workflow completo.

---

# 4. Confine di TODO-0101

`TODO-0101` deve produrre uno schema logico completo.

Deve documentare:

```text
catalogo entità
catalogo versioni
dizionario colonne
PK e FK
cardinalità
tabelle associative
unique e check
vincoli temporali
strategie anti-orfano
ownership
lifecycle
mapping SQLite/PostgreSQL
moduli
dipendenze
wave di implementazione
criteri di completezza
```

Non deve necessariamente produrre:

- database SQLite funzionante;
- migration Rust;
- adapter;
- repository;
- UI;
- test runtime.

---

# 5. Stato documentale delle entità

Ogni entità approvata deve comparire nel modello canonico con uno stato di implementazione:

```text
DEFINED
PLANNED_FOR_FOUNDATION
PLANNED_FOR_CAPABILITY
DEFERRED_IMPLEMENTATION
```

Questo stato non sostituisce il lifecycle dell’entità.

Nessuna entità approvata può sparire dallo schema senza una decisione esplicita.

---

# 6. Nessuna tabella vuota

Non vengono create subito tutte le tabelle canoniche.

Una tabella viene materializzata quando entra in una capacità concreta e verificabile.

Si evitano:

- migration enormi;
- vincoli non testati;
- schema fisicamente pieno ma funzionalmente vuoto;
- manutenzione prematura.

---

# 7. Nessuno schema provvisorio incompatibile

L’implementazione progressiva non autorizza:

```text
tasks_v1_temp
generic_records
future_data_json
all_links_json
metadata_blob
```

come sostituti del modello già deciso.

Ogni tabella introdotta deve:

- usare il nome canonico;
- usare UUID espliciti;
- mantenere `project_id`;
- non dipendere da `rowid`;
- essere compatibile con il modello target;
- evolvere tramite migration additive.

---

# 8. Capacità verticali

Le capacità devono essere semanticamente complete.

Esempio non ammesso:

```text
creare tasks
e aggiungere eventi, transizioni e integrità in futuro
```

Esempio corretto:

```text
GOVERNED_TASK_MANAGEMENT

tasks
+
Task Contract minimo
+
transizioni
+
eventi
+
actor autorizzato
+
integrity profile
+
test
```

Nessuna capacità di scrittura viene attivata senza le protezioni necessarie.

---

# 9. Wave di implementazione

## Wave 0 — Database foundation

Obiettivo:

```text
aprire, identificare, versionare e migrare
correttamente il database
```

Elementi:

```text
schema_migrations
database_metadata
projects
project_entities
entity_versions
actor locale o system actor minimo
```

Abilita:

- creazione database;
- identificazione progetto;
- schema version;
- compatibilità;
- supporto a `TODO-0103`;
- informazioni tecniche UI.

## Wave 1 — Governed work management

Include:

```text
projects
phases
work_items
tasks
objectives
Task Contract
documents
decisions
requirements
transizioni
eventi
actor/session
integrity profile
dipendenze
```

## Wave 2 — Governed execution

Include:

```text
task_executions
attempts
prompts
Context Package
reports
repository_snapshots
command_runs
test_runs
```

Protegge fin dall’inizio:

- tentativi numerati;
- massimo tentativi;
- prompt frozen;
- Context Package frozen;
- report originale;
- snapshot;
- eventi;
- provenance essenziale.

## Wave 3 — Verification and closure

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

## Wave 4 — Baseline and historical intelligence

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

## Wave 5 — Advanced integrity, security and retention

Materializza pienamente:

```text
integrity rules e profiles
role e permission catalog
classification
redaction
retention
deletion workflows
break-glass
security audit
```

Le wave precedenti mantengono comunque protezioni minime.

---

# 10. Protezioni minime progressive

## Sicurezza iniziale

```text
un actor umano locale
un system actor
sessione locale
Project Owner
scope progetto
default deny sulle azioni critiche
```

## Transizioni iniziali

Le prime transizioni possono essere definite nel core Rust e tramite un catalogo ristretto.

Non è ammesso iniziare con aggiornamenti diretti dello stato.

## Eventi iniziali

Il primo workflow scrivibile deve già produrre eventi materiali.

Le ricostruzioni e projection avanzate possono evolvere successivamente.

---

# 11. Stati di maturità delle capacità

Ogni capacità usa dimensioni separate:

```text
definition_status
storage_status
runtime_status
verification_status
activation_status
```

## Definition

```text
NOT_DEFINED
PARTIALLY_DEFINED
COMPLETE
SUPERSEDED
```

## Storage

```text
NOT_INSTALLED
MIGRATED
MIGRATION_FAILED
```

## Runtime

```text
NOT_IMPLEMENTED
PARTIALLY_IMPLEMENTED
IMPLEMENTED
DEGRADED
```

## Verification

```text
NOT_VERIFIED
PARTIALLY_VERIFIED
VERIFIED
FAILED
STALE
```

## Activation

```text
DISABLED
ENABLED
BLOCKED
SUSPENDED
```

Esempio:

```text
definition_status: COMPLETE
storage_status: MIGRATED
runtime_status: IMPLEMENTED
verification_status: NOT_VERIFIED
activation_status: DISABLED
```

---

# 12. Tabelle tecniche di fondazione

## `schema_migrations`

Campi concettuali:

```text
migration_id
version
name
checksum
applied_at
application_version
execution_duration_ms
migration_batch
```

Una migration applicata è immutabile.

## `database_metadata`

Campi:

```text
database_id
database_kind
project_id nullable
schema_version
compatibility_version
created_at
last_migrated_at
created_by_application_version
```

Tipi di database:

```text
PROJECT_DATABASE
GLOBAL_PROJECT_REGISTRY
TEST_DATABASE
TEMPORARY_DATABASE
```

## `schema_capabilities`

Potrà registrare gli stati distinti di storage, runtime, verifica e attivazione.

Non usa un singolo booleano `ready`.

---

# 13. Tipi canonici e portabilità

| Tipo canonico | SQLite | PostgreSQL |
|---|---|---|
| `UUID` | `TEXT` canonico | `UUID` |
| `REFERENCE_CODE` | `TEXT` | `TEXT` / `VARCHAR` |
| `BOOLEAN` | `INTEGER CHECK 0/1` | `BOOLEAN` |
| `INT32` | `INTEGER` con range | `INTEGER` |
| `INT64` | `INTEGER` | `BIGINT` |
| `SEQUENCE` | `INTEGER` | `BIGINT` |
| `TIMESTAMP_UTC` | `TEXT` RFC 3339 UTC | `TIMESTAMPTZ` |
| `DATE` | `TEXT` ISO 8601 | `DATE` |
| `JSON` | `TEXT` validato | `JSONB` |
| `HASH_SHA256` | `TEXT` esadecimale | `CHAR(64)` / `TEXT` |
| `ENUM_CODE` | `TEXT` + check/catalogo | `TEXT` + check/catalogo |
| `DECIMAL` | rappresentazione governata | `NUMERIC` |
| `BINARY_SMALL` | `BLOB` | `BYTEA` |

Gli artifact grandi restano in managed storage.

La scelta concreta della versione UUID appartiene a `TODO-0102`.

---

# 14. Enum, cataloghi e JSON

## Enum

Per valori stabili e chiusi:

```text
TEXT + CHECK
```

Per valori estensibili o governati:

```text
catalog table + foreign key
```

Non si assume come fondamento un enum PostgreSQL nativo.

## JSON

È ammesso per:

```text
event payload
rule definition
manifest
provider metadata
observed result
environment fingerprint
redaction details
```

Non sostituisce:

```text
task list
approval list
requirements
evidence links
relationship graph
```

## EAV

Non viene adottato un modello EAV per il dominio principale.

`project_entities` non sostituisce le tabelle specializzate.

---

# 15. Nullability e default

Una colonna è nullable soltanto quando l’assenza ha significato di dominio.

Non vengono aggiunte colonne nullable per ipotetici usi futuri.

I default non devono nascondere dati obbligatori.

Non sono ammessi default come:

```text
verification_status = VERIFIED
actor_id = system
```

se non corrispondono a un fatto reale.

---

# 16. Indici

TODO-0101 documenta gli indici necessari almeno per:

- PK e unique;
- foreign key frequenti;
- `project_id`;
- `reference_code`;
- parent gerarchici;
- stati;
- sequence;
- intervalli temporali;
- versioni correnti;
- event journal;
- attempts;
- task aperte;
- blocker.

Gli indici avanzati vengono aggiunti sulla base di query e misurazioni reali.

---

# 17. Migration

Regole:

```text
migration applicata immutabile
versione e checksum
ordine deterministico
runner idempotente
failure non marcata come applicata
transazione quando possibile
assessment per migration distruttive
integrity profile dopo la migration
```

Per modifiche SQLite complesse:

```text
create new table
→ copy
→ validate
→ swap
→ verify
```

---

# 18. Compatibilità

L’applicazione deve conoscere:

```text
minimum_supported_schema_version
maximum_supported_schema_version
```

Database più vecchio:

- migration autorizzata;
- oppure blocco controllato.

Database più nuovo:

```text
READ_ONLY_COMPATIBILITY_MODE
UPGRADE_APPLICATION_REQUIRED
OPEN_BLOCKED
```

La scelta runtime definitiva appartiene a `TODO-0102`.

---

# 19. Attivazione delle capacità

Una capacità può diventare `ENABLED` soltanto quando sono presenti:

```text
schema logico completo
migration applicata
core implementato
transizioni
eventi
autorizzazioni minime
integrity profile
test superati
recovery
UI coerente
```

Una migration riuscita non è sufficiente.

Le feature incomplete restano:

```text
DISABLED
READ_ONLY
DIAGNOSTIC_ONLY
EXPERIMENTAL
```

e non vengono presentate come complete.

---

# 20. Completezza dello schema logico

Ogni entità approvata deve possedere:

```text
responsabilità
tabella logica
PK
project ownership
reference code quando richiesto
colonne
tipi canonici
nullability
versionamento
relazioni
cardinalità
FK
unique
check
lifecycle
retention
integrity rules
modulo
wave di implementazione
```

Un semplice elenco di tabelle non è sufficiente.

---

# 21. Deliverable di TODO-0101

Per la chiusura sono richiesti almeno:

## Schema Architecture

Moduli, ownership, cataloghi, versionamento, temporalità, sicurezza e progressione.

## Entity Catalog

Significato, modulo, identità, versionamento, lifecycle e wave di ogni entità.

## Data Dictionary

Colonne, tipi canonici, mapping SQLite/PostgreSQL, nullability, default, vincoli e descrizioni.

## Relationship Matrix

Source, target, cardinalità, tabella, ownership, versione, delete behavior e regole sui cicli.

## Constraint Catalog

PK, FK, unique, check, invarianti, cardinalità condizionali, transition e integrity rules.

## State and Transition Catalog

Stati, azioni, condizioni ed effetti delle entità governate.

## Portability Matrix

Mapping canonico, SQLite e PostgreSQL.

## Implementation Wave Matrix

Capacità, tabelle, dipendenze, protezioni, criteri di attivazione e task future.

## Coverage Check

Verifica esplicita delle entità richieste dalla To-Do v0.8.

## Open Issues Register

Ogni punto residuo deve essere non bloccante, assegnato e collegato a una task futura.

---

# 22. Fuori scope di TODO-0101

Non è richiesto completare:

```text
migration SQLite eseguibili
adapter Rust
repository e service layer
UI completa
performance tuning
runtime multiutente
provider IA reali
deletion workflow operativo
event replay completo
motore policy generalizzato
deployment PostgreSQL
```

Il modello logico non deve però impedirli.

---

# 23. Criteri di chiusura

TODO-0101 può chiudere soltanto quando:

```text
tutte le decisioni sono consolidate
tutte le entità minime sono presenti
ogni tabella usa PK esplicita
nessuna struttura dipende da rowid
le relazioni fondamentali sono documentate
le cardinalità sono definite
project_id è presente dove richiesto
le versioni immutabili sono modellate
i tipi hanno mapping SQLite/PostgreSQL
le regole anti-orfano sono documentate
le wave sono definite
non esistono incompatibilità note
le questioni bloccanti sono risolte
il brief precedente è sostituito
il documento finale è verificato
contro il Decision Log
```

---

# 24. Decisione approvata

```text
DEC-0101-020 — APPROVED

Project Integrity OS distingue:

schema canonico completo
schema fisico installato
capacità applicativa attiva.

TODO-0101 completa il modello concettuale e logico.

TODO-0102 materializza progressivamente
lo schema SQLite e l’adapter.

Le capacità vengono implementate tramite vertical slice
semanticamente complete.

Nessuna capacità di scrittura viene attivata
senza transizioni, eventi, autorizzazioni,
integrità, test e recovery.

Il modello logico include tutte le entità approvate,
anche quando l’implementazione è differita.

Non vengono usati placeholder JSON, EAV
o tabelle temporanee incompatibili.

Ogni capacità mantiene stati distinti
di definizione, storage, runtime,
verifica e attivazione.
```
