# Project Integrity OS

## Provenienza e classificazione delle informazioni — v0.2

**Stato:** DRAFT — modello consolidato, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task:** `TODO-0101`  
**Decisioni:** `DEC-0101-009`, `DEC-0101-015`, `DEC-0101-017`, `DEC-0101-019`  
**Sostituisce:** `Project_Integrity_OS_04_Provenienza_Informazioni_TODO-0101_v0_1_DRAFT.md`

---

# 1. Principio

Dichiarazioni, osservazioni, derivazioni, inferenze, decisioni, approvazioni e sintesi non sono equivalenti.

La provenienza è multidimensionale.

Non viene usato un singolo enum che mescola:

- natura;
- acquisizione;
- attore;
- verifica;
- governo;
- confidenza.

---

# 2. Dimensioni

## Natura

```text
SOURCE_ARTIFACT
DECLARATION
OBSERVATION
DERIVATION
INFERENCE
DECISION
APPROVAL
SUMMARY
```

## Acquisizione

```text
MANUAL_ENTRY
PASTED_TEXT
FILE_IMPORT
REPOSITORY_READ
TOOL_EXECUTION
API_IMPORT
SYSTEM_CALCULATION
AI_GENERATION
MIGRATION
RESTORE
```

## Attore

```text
HUMAN
AI
SYSTEM
TOOL
EXTERNAL_SERVICE
MIGRATION_PROCESS
UNKNOWN
```

## Verifica

```text
UNVERIFIED
PARTIALLY_VERIFIED
VERIFIED
RECONCILED
CONFLICTING
DISPUTED
NOT_VERIFIABLE
STALE
REJECTED
```

## Governo

```text
NONE
PROPOSED
UNDER_REVIEW
APPROVED
REJECTED
SUPERSEDED
REVOKED
EXPIRED
```

## Confidenza

```text
LOW
MEDIUM
HIGH
NOT_APPLICABLE
```

---

# 3. Entità

```text
provenance_records
provenance_inputs
provenance_external_sources
```

## `provenance_records`

```text
provenance_record_id
project_id
target_entity_id
target_entity_version_id
target_field_path
information_kind
acquisition_method
actor_type
actor_id
actor_session_id
source_entity_id
source_entity_version_id
source_external_reference_id
source_locator_json
content_hash
verification_status
governance_status
confidence_level
confidence_score
confidence_basis
method_name
method_version
occurred_at
observed_at
recorded_at
valid_from
valid_until
supersedes_provenance_record_id
created_at
```

Regole:

- target interno: `target_entity_id` punta a `project_entities`;
- target versionato: `target_entity_version_id` punta a `entity_versions`;
- fonte interna: entity/version;
- fonte esterna: `source_external_reference_id`;
- le alternative sono mutuamente esclusive dove richiesto;
- ogni relazione interna rispetta `project_id`.

---

# 4. Input

`provenance_inputs` collega derivazioni, inferenze e summary ai propri input.

```text
provenance_record_id
input_provenance_record_id
input_role
sequence_number
created_at
```

Derivazioni, inferenze e summary materiali richiedono almeno una fonte risolvibile.

---

# 5. Attori globali e binding locali

Gli actor sono globali.

Il project database non usa foreign key cross-database verso il control database.

Usa:

```text
project_actor_bindings
```

con:

```text
project_actor_binding_id
project_id
actor_id
actor_reference_code
actor_type_snapshot
global_registry_version
actor_definition_hash
binding_status
bound_at
```

Le entità project-local fanno riferimento al binding locale quando serve enforcement relazionale nel database di progetto.

L'actor UUID globale resta conservato.

---

# 6. Esempio: test

```text
report originale
→ SOURCE_ARTIFACT

"TEST-001 PASSED"
→ DECLARATION

exit code osservato
→ OBSERVATION

exit_code = 0 → PASSED
→ DERIVATION

dichiarazione e osservazione confrontate
→ RECONCILIATION

criterio valutato
→ VERIFICATION

chiusura autorizzata
→ APPROVAL
```

Nessun passaggio sovrascrive il precedente.

---

# 7. Correzioni

Una correzione crea un nuovo provenance record o una nuova versione.

Il record precedente resta disponibile.

Quando una fonte viene corretta o invalidata, le entità dipendenti possono diventare:

```text
STALE
VALID_WITH_LIMITATIONS
INVALID
REGENERATION_REQUIRED
```

---

# 8. Osservazioni

Una observation deve registrare:

- strumento;
- versione;
- scope;
- ambiente;
- timestamp;
- output o hash;
- actor/tool;
- eventuale command run.

Un'affermazione priva di osservazione resta una declaration.

---

# 9. Derivazioni e inferenze

Una derivation registra:

- input;
- regola;
- versione della regola;
- risultato;
- hash;
- timestamp.

Una inference registra:

- fonti;
- metodo;
- attore;
- incertezza;
- confidence;
- verifica ancora necessaria.

Non viene inventata precisione numerica non supportata.

---

# 10. Regole vincolanti

```text
imported ≠ verified
generated ≠ correct
declaration ≠ observation
approval ≠ verification
exception ≠ passed
correction ≠ overwrite
conflict ≠ deletion of one source
```

Ogni contenuto usato in una verification deve avere provenienza risolvibile.

---

# 11. Decisione consolidata

```text
DEC-0101-009

La provenienza è multidimensionale.

Target e fonti project-local usano
project_entities ed entity_versions.

Actors globali vengono collegati al progetto
tramite binding locali riproducibili,
senza foreign key cross-database.

Correzioni, conflitti e derivazioni
restano visibili e verificabili.
```
