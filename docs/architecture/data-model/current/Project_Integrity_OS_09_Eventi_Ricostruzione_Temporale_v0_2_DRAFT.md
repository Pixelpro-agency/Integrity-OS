# Project Integrity OS

## Eventi e ricostruzione temporale — v0.2

**Stato:** DRAFT — modello consolidato, non ancora fonte autorevole
**Data:** 2026-08-06
**Task:** `TODO-0101`
**Decisioni:** `DEC-0101-014`, `DEC-0101-015`, `DEC-0101-019`, `DEC-0101-020`
**Correzioni:** `C-0101-004`, `C-0101-006`
**Sostituisce:** `../history/decisions/Project_Integrity_OS_09_Eventi_Ricostruzione_Temporale_v0_1_DRAFT.md`

---

# 1. Modello ibrido

```text
domain tables
→ stato corrente autorevole

event journal append-only
→ storico dei cambiamenti materiali

entity versions
→ contenuto esatto

state snapshots
→ checkpoint tecnico

baselines
→ checkpoint governato
```

Non viene adottato event sourcing totale per l'MVP.

---

# 2. Entità

```text
events
event_subjects
state_snapshots
state_reconstructions
state_reconstruction_events
projection_checkpoints
```

Il catalogo dei tipi evento è un system catalog globale, non una entità futura del project database.

---

# 3. Events

```text
event_id
project_id
reference_code
project_sequence_number
aggregate_entity_id
aggregate_sequence_number
event_category
event_type_code
event_type_catalog_version
event_type_definition_hash
event_schema_version
payload_json
payload_hash
previous_event_hash
event_hash
actor_binding_id
information_kind
acquisition_method
correlation_id
causation_event_id
idempotency_key
attempt_id
task_execution_id
command_run_id
repository_snapshot_id
baseline_version_id
occurred_at
observed_at
recorded_at
effective_at
created_at
```

`aggregate_entity_id` punta a `project_entities`.

Il progetto usa la root project entity come aggregate.

---

# 4. Event type binding

Il project database non usa foreign key cross-database verso il system catalog.

Ogni evento conserva:

```text
event_type_code
event_type_catalog_version
event_type_definition_hash
```

Il core valida il code contro il catalogo globale al momento della creazione.

La tripla congelata rende l'evento riproducibile anche dopo un aggiornamento del catalogo.

---

# 5. Sequenze

Vincoli:

```text
UNIQUE(project_id, project_sequence_number)

UNIQUE(
  project_id,
  aggregate_entity_id,
  aggregate_sequence_number
)
```

Le sequence sono monotone e non riutilizzate.

I timestamp non sono l'ordine autorevole.

---

# 6. Subjects

```text
event_subject_id
project_id
event_id
subject_entity_id
subject_entity_version_id
subject_role
sequence_number
created_at
```

Ruoli:

```text
PRIMARY
AFFECTED
SOURCE
TARGET
CAUSE
RESULT
INVALIDATED
SUPERSEDED
```

L'aggregate primario è sempre presente anche tra i subject o è ricostruibile deterministicamente.

---

# 7. Payload e hash

Il payload è piccolo e strutturato.

Contenuti grandi restano in entità dedicate.

La hash chain usa una serializzazione canonica documentata nel Data Dictionary:

- encoding UTF-8;
- ordinamento deterministico delle chiavi;
- normalizzazione dei timestamp;
- algoritmo SHA-256;
- inclusione di sequence, type binding, payload hash e previous hash.

La serializzazione è versionata.

---

# 8. Correlation, causation e idempotenza

```text
correlation_id
causation_event_id
idempotency_key
```

Vincolo quando presente:

```text
UNIQUE(project_id, idempotency_key)
```

Stessa chiave e stesso payload restituiscono il risultato precedente.

Stessa chiave e payload differente producono conflict.

---

# 9. Atomicità

Nella stessa transazione:

```text
verifica aggregate sequence
aggiornamento stato
relazioni obbligatorie
transition execution
event
nuova aggregate sequence
```

Non devono esistere stato senza evento o evento di transizione senza stato.

---

# 10. Tempi

```text
occurred_at
observed_at
recorded_at
effective_at
```

Persistenza in UTC RFC 3339.

Il valore originale esterno può essere conservato in provenance o payload.

Gli eventi tardivi sono append in coda e conservano il tempo originario.

---

# 11. State snapshots

```text
state_snapshot_id
project_id
reference_code
root_entity_id
snapshot_type
as_of_project_sequence
as_of_recorded_at
as_of_effective_at
state_schema_version
state_json
state_hash
source_baseline_version_id
created_by_actor_binding_id
created_at
supersedes_state_snapshot_id
```

Gli snapshot sono immutabili.

---

# 12. Ricostruzioni

Modalità:

```text
AS_KNOWN_AT
AS_EFFECTIVE_AT
AS_BASELINED
```

`state_reconstructions` conserva:

- root entity;
- sequenza o tempo richiesto;
- snapshot base;
- intervallo eventi;
- algoritmo e versione;
- manifest degli eventi;
- result hash;
- integrity status.

Una ricostruzione incompleta non è autorevole.

---

# 13. Integrità

Controlli:

- sequence duplicata o mancante;
- aggregate sequence incoerente;
- hash chain interrotta;
- payload hash errato;
- event type binding non risolvibile;
- subject inesistente;
- cross-project relation;
- causation inesistente;
- timestamp incoerente;
- divergenza tra event e current state.

Esiti:

```text
EVENT_STREAM_VALID
EVENT_STREAM_INCOMPLETE
EVENT_STREAM_CONFLICTING
EVENT_STREAM_CORRUPTED
EVENT_STREAM_UNSUPPORTED
```

---

# 14. Decisione consolidata

```text
DEC-0101-014
C-0101-006

Events usano aggregate_entity_id
e subject project-local risolvibili.

I tipi evento globali vengono congelati
tramite code, catalog version e definition hash.

Non esistono foreign key cross-database.

La hash chain usa una serializzazione
canonica e versionata.
```
