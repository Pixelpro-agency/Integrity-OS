# Project Integrity OS

## Integrità trasversale e regole anti-orfano — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task collegata:** `TODO-0101 — Definire schema dati minimo`  
**Decisione collegata:** `DEC-0101-015 — APPROVED`

---

# 1. Scopo

Un record può esistere fisicamente ed essere comunque orfano semanticamente.

Esempi:

- report senza attempt;
- test run con versione errata;
- evidence non collegata a una verifica;
- approval senza versione esatta;
- relazione cross-project;
- Context Package con fonti non risolvibili;
- aggregate con parent incoerente.

---

# 2. Tipi di orfano

```text
RELATIONAL_ORPHAN
SEMANTIC_ORPHAN
WORKFLOW_ORPHAN
VERSION_ORPHAN
PROVENANCE_ORPHAN
PROJECT_BOUNDARY_VIOLATION
CONTENT_ORPHAN
TEMPORAL_ORPHAN
AGGREGATE_ORPHAN
```

---

# 3. Livelli di integrità

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
SECURITY_BOUNDARY
```

L’integrità trasversale comprende vincoli strutturali, semantici, temporali e di processo.

---

# 4. Catalogo universale delle entità governate

Per evitare riferimenti polimorfici non verificabili viene introdotto:

```text
project_entities
```

Campi concettuali:

```text
entity_id
project_id
entity_type
reference_code
record_state
created_at
archived_at
```

Vincoli:

```text
PRIMARY KEY(entity_id)
UNIQUE(project_id, entity_type, reference_code)
UNIQUE(entity_id, project_id)
```

Le tabelle specializzate condividono lo stesso UUID.

Esempio:

```text
project_entities.entity_id = tasks.task_id
```

Ogni tabella rilevante mantiene `project_id`.

Il nome non deve essere confuso con il registro globale dei progetti di `TODO-0103`.

---

# 5. Registro comune delle versioni

Viene introdotto:

```text
entity_versions
```

Campi comuni:

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

Le tabelle specializzate restano:

```text
document_versions
decision_versions
register_item_versions
test_definition_versions
requirement_versions
```

Context Package, approval, baseline e summary possono così referenziare versioni reali.

---

# 6. Relazioni

## Relazioni fondamentali

Usano tabelle dedicate.

Esempi:

```text
work_item_tasks
requirement_acceptance_criteria
acceptance_criterion_test_definitions
task_executions
attempts
test_run_evidence
decision_inputs
decision_targets
```

## Relazioni trasversali

Usano:

```text
entity_links
```

Campi:

```text
entity_link_id
project_id
source_entity_id
target_entity_id
relationship_type_id
source_entity_version_id
target_entity_version_id
valid_from
valid_until
created_by
created_at
```

Entrambi gli estremi sono foreign key reali verso `project_entities`.

---

# 7. Tipi di relazione governati

`relationship_types` impedisce stringhe libere.

Campi:

```text
relationship_type_id
code
source_entity_type
target_entity_type
inverse_code
cardinality
same_project_required
version_reference_required
acyclic
symmetric
active
created_at
```

Esempi:

```text
IMPLEMENTS
VERIFIES
DERIVES_FROM
PRODUCED_BY
SUPERSEDES
BLOCKS
DEPENDS_ON
APPROVED_BY
CORRECTED_BY
INCLUDED_IN_BASELINE
```

Le combinazioni di tipi non ammesse vengono respinte.

---

# 8. Regole di integrità

Entità:

```text
integrity_rules
integrity_rule_versions
integrity_profiles
integrity_profile_rules
```

## Livelli di applicazione

```text
ADVISORY
REQUIRED
BLOCKING
FATAL
```

Le definizioni sono versionate e congelabili.

Campi concettuali di una versione:

```text
description
enforcement_level
evaluation_method
rule_definition_json
error_code
remediation_guidance
content_hash
```

---

# 9. Profili

Esempi:

```text
TASK_READY_PROFILE
ATTEMPT_START_PROFILE
ATTEMPT_REPORT_PROFILE
VERIFICATION_PASS_PROFILE
TASK_COMPLETION_PROFILE
BASELINE_APPROVAL_PROFILE
CONTEXT_PACKAGE_FREEZE_PROFILE
PROJECT_EXPORT_PROFILE
```

Un profilo raccoglie le regole applicabili a una transizione o operazione.

La versione del profilo usata deve restare nello storico.

---

# 10. Esecuzione dei controlli

Entità:

```text
integrity_runs
integrity_check_results
```

Trigger:

```text
WRITE_TIME
TRANSITION
CHECKPOINT
BASELINE
STARTUP
RECOVERY
IMPORT
EXPORT
MANUAL_AUDIT
```

Stati dei risultati:

```text
PASSED
FAILED
WARNING
BLOCKED
NOT_APPLICABLE
NOT_EVALUATED
TECHNICAL_FAILURE
```

`TECHNICAL_FAILURE` non equivale a una violazione verificata.

---

# 11. Ripartizione delle responsabilità

```text
database
→ invarianti strutturali

core Rust
→ regole di dominio e transizioni

Integrity Engine
→ scansioni trasversali e ricostruzioni

frontend
→ presentazione
```

Il frontend non è autorità di integrità.

---

# 12. SQLite

Ogni connessione SQLite deve avere foreign key realmente abilitate.

Sono necessari:

- configurazione all’apertura;
- verifica;
- test;
- diagnosi in caso di mancata attivazione.

Default:

```text
constraint immediate
```

Le constraint differibili sono eccezioni governate per operazioni atomiche multi-record.

---

# 13. Confine del progetto

Nell’MVP:

```text
nessuna relazione diretta cross-project
```

I riferimenti esterni usano `external_reference` con snapshot, hash e disponibilità.

Non vengono mascherati come foreign key interne.

---

# 14. Integrità delle versioni

Regole minime:

```text
una versione appartiene a una entità;

supersedes non punta a se stessa;

la catena supersedes è aciclica;

una versione frozen è immutabile;

una approval punta alla versione esatta;

una baseline include versioni esatte;

una versione usata in un attempt non viene riscritta;

versioni efficaci incompatibili non si sovrappongono.
```

---

# 15. Integrità temporale

Regole:

```text
valid_from < valid_until
created_at <= frozen_at
started_at <= completed_at
nessun uso prima della creazione nella vista AS_KNOWN_AT
nessuna decisione efficace prima di effective_at
nessuna versione scaduta per nuove esecuzioni
```

Le correzioni retroattive devono restare visibili.

---

# 16. Integrità esecutiva

Esempi:

```text
attempt appartiene alla task_execution corretta;

Task Contract e Context Package appartengono
alla stessa task e allo stesso attempt;

report e prompt condividono l’attempt;

test run e command run condividono l’attempt;

repository snapshot appartiene allo stesso progetto;

approval punta alla verifica e alla versione esatta;

baseline include soltanto elementi ammessi dalla policy.
```

---

# 17. Integrità requisiti-test

```text
requisito approvato
→ criterio o eccezione;

criterio bloccante
→ metodo di verifica;

test definition
→ criterio;

test run
→ versione frozen;

PASSED
→ evidence richiesta;

requirement VERIFIED
→ copertura completa;

bug chiuso
→ regression test o deroga.
```

---

# 18. Integrità di provenienza e sintesi

```text
DERIVATION
→ almeno un input;

INFERENCE
→ fonti e incertezza;

SUMMARY
→ almeno una fonte;

summary claim materiale
→ fonte o non verificabilità esplicita;

summary CURRENT
→ source_set_hash coerente;

Context Package FROZEN
→ fonti risolvibili.
```

---

# 19. Cicli vietati

Devono essere rilevati in:

```text
parent hierarchy
supersedes
blocking dependencies
provenance derivations
event causation
decision supersession
requirement dependencies acicliche
task dependencies bloccanti
```

Esempio:

```text
TASK-A depends_on TASK-B
TASK-B depends_on TASK-A
→ DEPENDENCY_CYCLE
```

---

# 20. Stato aggregato

Un livello superiore non può risultare completato se elementi inferiori obbligatori sono incompleti.

Esempi:

```text
work item DONE con task BLOCKED
task COMPLETED con requisito FAILED
attempt VERIFIED senza report
baseline APPROVED con elemento non frozen
```

Esito:

```text
AGGREGATE_STATE_INCONSISTENT
```

---

# 21. Violazioni e finding

Un controllo produce sempre un risultato tecnico.

Una violazione materiale genera:

```text
FINDING
finding_type: INTEGRITY_VIOLATION
```

Regola:

```text
warning non materiale
→ check result

failed materiale
→ finding

blocking o fatal
→ finding obbligatorio + blocco
```

---

# 22. Eccezioni

Una eccezione:

- non cancella la violazione;
- non cambia `FAILED` in `PASSED`;
- può autorizzare una transizione;
- ha scope, motivazione, rischio, approvatore e scadenza;
- resta visibile;
- può essere revocata.

Le regole `FATAL` richiedono una policy straordinaria per essere derogate.

---

# 23. Riparazioni

Le riparazioni automatiche sono ammesse solo se:

- deterministiche;
- non ambigue;
- reversibili;
- limitate;
- registrate;
- seguite da un nuovo integrity run.

Le correzioni semantiche richiedono decisione, task, recovery o intervento umano.

---

# 24. Quarantena

Un import non valido non entra direttamente nel dominio autorevole.

Viene conservato come:

```text
SOURCE_ARTIFACT
+
import result
+
integrity finding
```

fino a validazione, correzione, eccezione o rifiuto.

---

# 25. UI

Stato categoriale:

```text
COMPLETE
COMPLETE_WITH_WARNINGS
INCOMPLETE
BLOCKED
CONFLICTING
INTEGRITY_FAILURE
NOT_EVALUATED
```

La percentuale non deve nascondere violazioni bloccanti.

Drill-down:

```text
profilo
→ regola
→ versione
→ entità
→ osservato
→ atteso
→ evidence
→ finding
→ eccezione
→ remediation
```

---

# 26. Regole vincolanti

```text
Ogni entità citabile ha identità in project_entities.

Le relazioni generiche usano foreign key reali.

Le relazioni fondamentali hanno tabelle dedicate.

I relationship type sono governati.

Ogni collegamento interno rispetta project_id.

Le versioni frozen sono immutabili.

Le catene e i cicli sono controllati.

Le transizioni usano profili versionati.

Un controllo non eseguito non è PASSED.

Una eccezione non cancella una violazione.

Una riparazione produce eventi e nuova verifica.

Gli import non validi restano in quarantena.

Lo stato aggregato non contraddice i livelli inferiori.
```

---

# 27. Decisione approvata

```text
DEC-0101-015 — APPROVED

Project Integrity OS introduce project_entities,
entity_versions, relazioni dedicate, entity_links,
relationship_types, integrity rules versionate,
profili, run e risultati.

L’integrità viene controllata a livello strutturale,
relazionale, semantico, temporale, di workflow,
tracciabilità, contenuto, eventi, aggregate e sicurezza.

Le violazioni materiali generano finding.

Le eccezioni non cancellano i fallimenti.

Le riparazioni sono registrate e verificate.

Gli import non validi restano in quarantena.
```
