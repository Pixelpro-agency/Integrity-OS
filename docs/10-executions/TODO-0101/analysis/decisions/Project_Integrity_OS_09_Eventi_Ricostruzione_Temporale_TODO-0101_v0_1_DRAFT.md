# Project Integrity OS

## Eventi e ricostruzione temporale — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task collegata:** `TODO-0101 — Definire schema dati minimo`  
**Decisione collegata:** `DEC-0101-014 — APPROVED`

---

# 1. Scopo

Project Integrity OS deve poter rispondere:

- qual è lo stato corrente;
- come è stato raggiunto;
- che cosa era noto in un momento;
- che cosa risultava efficace;
- quale versione era stata usata;
- quali eventi hanno generato una conseguenza;
- se lo storico è completo e integro.

---

# 2. Modello temporale ibrido

```text
tabelle di dominio
→ stato corrente autorevole

registro eventi append-only
→ storico dei cambiamenti materiali

versioni immutabili
→ contenuto esatto

state snapshot
→ checkpoint tecnico

baseline
→ checkpoint governato e approvato
```

Non viene adottato event sourcing totale come requisito dell’MVP.

---

# 3. Entità

```text
events
event_subjects
state_snapshots
state_reconstructions
```

Entità future:

```text
event_type_catalog
projection_checkpoints
event_delivery_records
security_access_events
```

---

# 4. Eventi

Un evento rappresenta un fatto significativo già avvenuto.

Esempi:

```text
task.created
task.status_changed
attempt.started
attempt.report_received
document.version_frozen
decision.version_approved
decision.became_effective
context_package.delivered
test_run.completed
verification.completed
risk.materialized
assumption.disproved
conflict.detected
baseline.approved
integrity.violation_detected
recovery.completed
```

Non ogni click della UI è un evento di dominio.

---

# 5. Struttura di `events`

Campi concettuali:

```text
event_id
project_id
reference_code
project_sequence_number
aggregate_type
aggregate_id
aggregate_sequence_number
event_category
event_type
event_schema_version
payload_json
payload_hash
previous_event_hash
event_hash
actor_type
actor_id
actor_session_id
information_kind
acquisition_method
correlation_id
causation_event_id
idempotency_key
attempt_id
task_execution_id
command_run_id
repository_snapshot_id
baseline_id
occurred_at
observed_at
recorded_at
effective_at
created_at
```

---

# 6. Sequenze

## Project sequence

Ordine totale degli eventi nel progetto.

```text
EVENT-000001
EVENT-000002
EVENT-000003
```

Deve essere monotona, univoca e non riutilizzata.

## Aggregate sequence

Ordine degli eventi di una singola entità.

Vincolo concettuale:

```text
UNIQUE(
  project_id,
  aggregate_type,
  aggregate_id,
  aggregate_sequence_number
)
```

L’ordine autorevole non si basa soltanto sui timestamp.

---

# 7. Aggregate e soggetti

L’aggregate è l’entità primaria modificata.

`event_subjects` collega le altre entità coinvolte.

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

Tutti i soggetti interni devono appartenere allo stesso progetto.

---

# 8. Categorie

```text
DOMAIN
WORKFLOW
GOVERNANCE
DOCUMENT
REPOSITORY
EXECUTION
VERIFICATION
INTEGRITY
RECOVERY
SECURITY
SYSTEM
IMPORT_EXPORT
```

I tipi di evento usano nomenclatura stabile e `event_schema_version`.

Gli eventi storici non vengono riscritti quando cambia lo schema del payload.

---

# 9. Payload

Il payload deve essere piccolo e strutturato.

Esempio:

```json
{
  "from_status": "READY",
  "to_status": "IN_EXECUTION",
  "transition_rule": "TASK_START_V1",
  "reason": "Contratto congelato e dipendenze soddisfatte"
}
```

Log, file, report e contenuti grandi restano in entità dedicate.

L’evento conserva riferimenti, versioni e hash.

---

# 10. Correlation e causation

`correlation_id` raggruppa eventi dello stesso flusso.

`causation_event_id` indica la causa diretta.

Esempio:

```text
decision.became_effective
→ context_package.marked_stale
→ task.created
```

---

# 11. Idempotenza

Le operazioni ripetute per retry, timeout o recovery non devono creare duplicati.

Si usa:

```text
idempotency_key
```

Vincolo concettuale:

```text
UNIQUE(project_id, idempotency_key)
```

quando presente.

---

# 12. Atomicità

La modifica dello stato corrente e l’inserimento dell’evento avvengono nella stessa transazione.

Non devono esistere:

```text
stato aggiornato senza evento
evento di transizione senza stato aggiornato
```

---

# 13. Immutabilità e hash chain

Gli eventi sono append-only.

Campi:

```text
payload_hash
previous_event_hash
event_hash
```

Una modifica o rimozione deve produrre:

```text
EVENT_HASH_CHAIN_BROKEN
```

Le correzioni producono nuovi eventi:

```text
event.corrected
event.reversed
event.superseded
```

---

# 14. Tempi distinti

```text
occurred_at
observed_at
recorded_at
effective_at
```

- `occurred_at`: quando il fatto è avvenuto;
- `observed_at`: quando è stato osservato;
- `recorded_at`: quando è entrato nel sistema;
- `effective_at`: quando ha iniziato a governare.

Gli eventi tardivi vengono aggiunti in coda e conservano il tempo originario.

---

# 15. Ricostruzioni

## `AS_KNOWN_AT`

Ricostruisce ciò che il sistema sapeva in un momento.

Usa soprattutto:

```text
recorded_at
project_sequence_number
```

## `AS_EFFECTIVE_AT`

Ricostruisce ciò che risultava valido o efficace.

Usa:

```text
effective_at
valid_from
valid_until
```

## `AS_BASELINED`

Ricostruisce lo stato della baseline approvata.

Una correzione tardiva può cambiare `AS_EFFECTIVE_AT`, ma non riscrive `AS_KNOWN_AT`.

---

# 16. Bitemporalità mirata

Le entità governate più sensibili devono poter registrare:

```text
recorded_at
valid_from
valid_until
```

In particolare:

- decisioni;
- requisiti;
- assumption;
- eccezioni;
- documenti;
- baseline;
- relazioni di governo.

---

# 17. Timestamp

Regole:

```text
persistenza in UTC
formato RFC 3339
timezone locale solo nella UI
valore originale esterno conservato quando necessario
incertezza temporale registrata
```

---

# 18. State snapshot

Campi:

```text
state_snapshot_id
project_id
reference_code
root_entity_type
root_entity_id
snapshot_type
as_of_project_sequence
as_of_recorded_at
as_of_effective_at
state_schema_version
state_json
state_hash
source_baseline_id
created_by
created_at
supersedes_snapshot_id
```

Tipi:

```text
PROJECT_STATE
PHASE_STATE
WORK_ITEM_STATE
TASK_STATE
ATTEMPT_STATE
PRE_EXECUTION
POST_EXECUTION
PRE_APPROVAL
POST_APPROVAL
RECOVERY_CHECKPOINT
EXPORT_CHECKPOINT
```

Gli snapshot sono immutabili.

---

# 19. Repository snapshot, state snapshot e baseline

Sono concetti distinti.

## Repository snapshot

Commit, branch, working tree, file e hash.

## State snapshot

Stato del dominio e delle relazioni.

## Baseline

Insieme governato e approvato che può includere entrambi più documenti, decisioni, requisiti e verifiche.

---

# 20. State reconstruction

Campi concettuali:

```text
state_reconstruction_id
project_id
reference_code
reconstruction_mode
root_entity_type
root_entity_id
requested_sequence
requested_time
base_snapshot_id
first_event_sequence
last_event_sequence
event_count
reconstruction_algorithm
algorithm_version
status
result_json
result_hash
integrity_status
created_by
created_at
```

Stati:

```text
PENDING
RUNNING
COMPLETED
COMPLETED_WITH_WARNINGS
FAILED
INCOMPLETE_HISTORY
INTEGRITY_FAILURE
```

Ogni ricostruzione conserva il manifest degli eventi applicati e ignorati.

---

# 21. Integrità del journal

Controlli minimi:

```text
sequenza duplicata
sequenza mancante
aggregate sequence incoerente
hash chain interrotta
payload hash errato
event type sconosciuto
schema version non supportata
subject inesistente
relazione cross-project
causation inesistente
timestamp incoerente
divergenza tra evento e stato corrente
```

Esiti:

```text
EVENT_STREAM_VALID
EVENT_STREAM_INCOMPLETE
EVENT_STREAM_CONFLICTING
EVENT_STREAM_CORRUPTED
EVENT_STREAM_UNSUPPORTED
```

Una ricostruzione incompleta non viene presentata come autorevole.

---

# 22. Recovery

Il recovery può:

- ricostruire proiezioni;
- ripristinare snapshot;
- riconciliare stato ed eventi;
- importare eventi mancanti;
- marcare dati irrecuperabili.

Produce nuovi eventi e non riscrive silenziosamente lo storico.

---

# 23. Proiezioni

Rollup e viste UI devono poter essere rigenerati.

Campi concettuali:

```text
last_processed_project_sequence
projection_version
projection_hash
```

Le proiezioni possono diventare stale.

---

# 24. Concorrenza

Le modifiche a un aggregate devono poter verificare:

```text
expected_aggregate_sequence
```

In caso di divergenza:

```text
CONCURRENT_MODIFICATION
```

L’operazione non sovrascrive il cambiamento precedente.

---

# 25. Regole vincolanti

```text
Lo stato corrente non sostituisce lo storico.

Il journal non sostituisce le tabelle di dominio.

Gli eventi sono append-only.

Transizione ed evento sono atomici.

L’ordine usa sequence number.

I tempi di occorrenza, osservazione,
registrazione ed efficacia sono distinti.

Gli eventi tardivi non vengono inseriti nel passato.

Le correzioni producono nuovi eventi.

Il journal usa una hash chain verificabile.

AS_KNOWN_AT e AS_EFFECTIVE_AT sono distinti.

Snapshot, repository snapshot e baseline sono distinti.

Le ricostruzioni incomplete non sono autorevoli.
```

---

# 26. Decisione approvata

```text
DEC-0101-014 — APPROVED

Project Integrity OS adotta tabelle di dominio,
event journal append-only, versioni immutabili,
state snapshot e baseline.

Gli eventi hanno sequenze, schema versionato,
provenienza, attore, correlazione, causazione,
idempotenza, timestamp distinti e hash chain.

Il sistema supporta ricostruzioni AS_KNOWN_AT,
AS_EFFECTIVE_AT e AS_BASELINED.

Non viene imposto event sourcing totale nell’MVP.
```
