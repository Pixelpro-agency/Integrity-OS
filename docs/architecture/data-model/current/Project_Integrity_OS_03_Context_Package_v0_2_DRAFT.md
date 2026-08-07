# Project Integrity OS

## Context Package — specifica concettuale v0.2

**Stato:** DRAFT — modello consolidato, non ancora fonte autorevole
**Data:** 2026-08-06
**Task:** `TODO-0101`
**Decisioni:** `DEC-0101-008`, `DEC-0101-009`, `DEC-0101-010`, `DEC-0101-015`, `DEC-0101-017`, `DEC-0101-019`
**Sostituisce:** `../history/decisions/Project_Integrity_OS_03_Context_Package_v0_1_DRAFT.md`

---

# 1. Principio

Un Context Package è un manifest persistente, versionato, validabile, congelabile e riproducibile del contesto consegnato.

Non è:

- una query temporanea;
- un prompt libero;
- una lista dinamica non congelata;
- una copia indiscriminata dell'intero progetto;
- un contenitore che ignora autorizzazioni e classificazioni.

---

# 2. Entità

```text
context_packages
context_package_versions
context_package_items
context_package_exclusions
context_package_validations
context_package_deliveries
attempt_context_packages
```

## `context_packages`

Identità logica:

```text
context_package_id
project_id
reference_code
package_type
purpose
root_entity_id
current_version_id
record_state
created_at
archived_at
```

`root_entity_id` punta a `project_entities`.

## `context_package_versions`

Versione immutabile del manifest:

```text
context_package_version_id
project_id
context_package_id
version_number
version_status
target_role_code
target_actor_id
target_session_id
source_baseline_version_id
selection_policy_code
selection_policy_version
selection_policy_hash
redaction_profile_version_id
content_hash
estimated_tokens
estimated_bytes
freshness_status
validity_status
created_by_actor_id
created_at
validated_at
frozen_at
supersedes_context_package_version_id
```

Ogni versione citabile possiede una riga in `entity_versions`.

---

# 3. Item

```text
context_package_item_id
project_id
context_package_version_id
source_entity_id
source_entity_version_id
source_external_reference_id
source_content_hash
item_category
inclusion_mode
inclusion_reason
required
priority
context_level
sequence_number
content_snapshot
excerpt_locator_json
summary_version_id
classification_level_code
redaction_applied
created_at
```

Regole:

- per una fonte versionata interna, `source_entity_version_id` è obbligatorio;
- per una fonte interna immutabile non versionata, si usa `source_entity_id` e hash;
- per una fonte esterna si usa `source_external_reference_id`;
- una sola modalità di sorgente è valorizzata;
- ogni item conserva il contenuto effettivamente consegnato o il riferimento deterministico.

---

# 4. Modalità di inclusione

```text
FULL
EXCERPT
SUMMARY
REFERENCE_ONLY
METADATA_ONLY
```

## FULL

Contenuto integrale della versione.

## EXCERPT

Estratto con documento, versione, hash e locator.

## SUMMARY

Punta a una `summary_version` congelata e verificabile.

## REFERENCE_ONLY

Consegna identità, versione e metodo di accesso autorizzato.

## METADATA_ONLY

Consegna soltanto metadata strutturati autorizzati.

---

# 5. Livelli

```text
CORE
SUPPORTING
DEEP_REFERENCE
```

`CORE` contiene tutto ciò che è obbligatorio per l'attività.

`SUPPORTING` contiene materiale pertinente consultabile.

`DEEP_REFERENCE` conserva accesso tracciabile alle fonti storiche o dettagliate.

---

# 6. Tipi

```text
GOVERNANCE
ANALYSIS
EXECUTION
VERIFICATION
VALIDATION
APPROVAL
DIAGNOSTIC
REOPENING
EXPORT
RECOVERY
SECURITY_REVIEW
```

Ogni tipo possiede un profilo di completezza.

---

# 7. Stati

```text
DRAFT
VALIDATING
VALID
FROZEN
DELIVERED
STALE
SUPERSEDED
REVOKED
```

Una versione `FROZEN`:

- non cambia manifest;
- non cambia item;
- non cambia esclusioni;
- non cambia redazione;
- non cambia hash.

Una nuova esigenza produce una nuova versione.

---

# 8. Esclusioni

```text
context_package_exclusion_id
project_id
context_package_version_id
excluded_entity_id
excluded_entity_version_id
excluded_external_reference_id
exclusion_reason
materiality
impact_assessment
excluded_by_policy_code
excluded_by_actor_id
created_at
```

Motivazioni:

```text
NOT_RELEVANT
OUT_OF_SCOPE
SUPERSEDED
DUPLICATE
SENSITIVE
TOKEN_LIMIT
ROLE_RESTRICTED
HISTORICAL_ONLY
UNAVAILABLE
MANUALLY_EXCLUDED
```

Un item obbligatorio non può essere escluso senza blocco o eccezione approvata.

---

# 9. Validazione

`context_package_validations` conserva:

```text
context_package_validation_id
project_id
context_package_version_id
integrity_profile_version_id
access_policy_version_id
redaction_profile_version_id
completeness_status
authorization_status
freshness_status
validation_status
result_hash
validated_by_actor_id
validated_at
```

Esiti:

```text
COMPLETE
INCOMPLETE
CONFLICTING
STALE_SOURCE
UNAUTHORIZED_CONTENT
TECHNICAL_FAILURE
```

Una versione non diventa `FROZEN` per un attempt se il profilo obbligatorio non è soddisfatto.

---

# 10. Delivery

```text
context_package_delivery_id
project_id
context_package_version_id
recipient_actor_id
recipient_session_id
attempt_id
delivery_channel
provider_code
provider_policy_code
delivered_hash
delivered_at
delivery_status
```

Una delivery registra esattamente ciò che è stato consegnato.

La permission locale non implica automaticamente l'autorizzazione a inviare il contenuto a un provider esterno.

---

# 11. Attempt

```text
ATTEMPT N ── M CONTEXT_PACKAGE_VERSIONS
```

tramite:

```text
attempt_context_packages
```

Ruoli:

```text
PRIMARY_EXECUTION
SUPPORTING
DIAGNOSTIC
RECOVERY
VERIFICATION_HANDOFF
```

Minimo:

```text
ATTEMPT → READY
richiede un PRIMARY_EXECUTION package
VALID e FROZEN
```

Normalmente ogni nuovo attempt riceve una nuova package version.

---

# 12. Selezione

Ordine deterministico:

1. elementi obbligatori del profilo;
2. gerarchia e Task Contract;
3. decisioni efficaci;
4. requisiti, criteri e test;
5. dipendenze;
6. register item bloccanti;
7. baseline e repository snapshot;
8. fonti esplicitamente richieste;
9. ricerca governata;
10. proposte IA aggiuntive;
11. validazione finale.

L'IA non elimina fonti obbligatorie.

---

# 13. Sicurezza

La classificazione derivata è almeno pari alla massima classificazione materiale delle fonti, salvo redazione o declassificazione approvata.

Ogni item conserva:

- classification level;
- handling flags applicabili;
- redaction result;
- motivo dell'esclusione o riduzione;
- fonte e hash.

---

# 14. Decisione consolidata

```text
DEC-0101-008

Context Package è una identità logica
con versioni immutabili.

Ogni versione contiene manifest, item,
esclusioni, validazioni, redazioni,
fonti esatte e hash finale.

Gli item puntano a project_entities,
entity_versions o external references.

Una delivery conserva destinatario,
canale, provider, attempt e hash consegnato.

Un package frozen non viene aggiornato.
```
