# Project Integrity OS

## Sintesi, drill-down, copertura e obsolescenza — v0.2

**Stato:** DRAFT — modello consolidato, non ancora fonte autorevole
**Data:** 2026-08-06
**Task:** `TODO-0101`
**Decisioni:** `DEC-0101-010`, `DEC-0101-015`, `DEC-0101-016`, `DEC-0101-019`
**Sostituisce:** `../history/decisions/Project_Integrity_OS_05_Sintesi_Drill_Down_v0_1_DRAFT.md`

---

# 1. Principio

Excerpt, estrazioni, summary, rollup e current-state snapshot sono artefatti derivati persistenti, versionati e verificabili.

Non sostituiscono le fonti.

Ogni valore sintetico permette:

```text
sintesi
→ dettaglio strutturato
→ versione originale
→ fonti
→ evidence
→ provenance
```

---

# 2. Tipi

```text
EXCERPT
STRUCTURED_EXTRACTION
SUMMARY
ROLLUP
CURRENT_STATE_SNAPSHOT
```

---

# 3. Entità

```text
summaries
summary_versions
summary_sources
summary_coverage
summary_exclusions
summary_claims
summary_claim_sources
summary_validations
```

## `summaries`

Identità logica:

```text
summary_id
project_id
reference_code
summary_type
purpose
root_entity_id
current_version_id
record_state
created_at
archived_at
```

## `summary_versions`

```text
summary_version_id
project_id
summary_id
version_number
title
content_text
structured_content_json
generation_method
generator_actor_id
generator_session_id
generator_version
summary_profile_code
summary_profile_version
summary_profile_hash
verification_status
governance_status
content_hash
source_set_hash
coverage_status
freshness_status
validity_status
covers_from
covers_until
as_of
created_at
verified_at
approved_at
frozen_at
stale_at
supersedes_summary_version_id
```

Ogni versione citabile possiede una riga in `entity_versions`.

---

# 4. Fonti

```text
summary_source_id
project_id
summary_version_id
source_entity_id
source_entity_version_id
source_external_reference_id
source_content_hash
source_role
source_locator_json
included_scope
sequence_number
created_at
```

Ruoli:

```text
PRIMARY
SUPPORTING
CONTRADICTING
CONTEXTUAL
HISTORICAL
```

Le fonti contraddittorie non vengono escluse silenziosamente.

---

# 5. Copertura

```text
summary_coverage_id
project_id
summary_version_id
coverage_dimension
coverage_status
covered_count
total_count
coverage_basis
created_at
```

Stati:

```text
FULL
PARTIAL
MINIMAL
NOT_COVERED
NOT_APPLICABLE
UNKNOWN
```

Una percentuale è ammessa soltanto con numeratore, denominatore e base deterministica.

---

# 6. Esclusioni

```text
summary_exclusion_id
project_id
summary_version_id
excluded_entity_id
excluded_entity_version_id
excluded_section
exclusion_reason
materiality
impact_note
created_at
```

Materialità:

```text
NON_MATERIAL
LOW
MEDIUM
HIGH
BLOCKING
```

Una summary con esclusioni bloccanti non è completa.

---

# 7. Claim

```text
summary_claim_id
project_id
summary_version_id
claim_text
claim_type
importance
verification_status
sequence_number
```

Ogni claim materiale usa una o più `summary_claim_sources`.

Sono materiali almeno i claim:

- tecnici;
- decisionali;
- controversi;
- usati per approval;
- usati per creare task;
- usati per dichiarare completamento.

---

# 8. Freshness e validity

Freshness:

```text
CURRENT
POTENTIALLY_STALE
STALE
UNKNOWN
```

Validity:

```text
VALID
VALID_WITH_LIMITATIONS
INVALID
SUPERSEDED
REVOKED
```

Una versione storica può essere:

```text
freshness = STALE
validity = VALID
```

come prova di ciò che era noto o consegnato.

---

# 9. Source set hash

Il `source_set_hash` include almeno:

- source entity/version;
- content hash;
- locator;
- ruolo;
- ordine rilevante;
- profilo;
- esclusioni materiali.

Serve a verificare se due summary sono state generate dallo stesso insieme di fonti.

---

# 10. Generazione

```text
HUMAN_AUTHORED
DETERMINISTIC_SYSTEM
AI_GENERATED
HYBRID
```

Una summary IA registra:

- actor e session;
- provider e modello;
- Context Package version;
- istruzione;
- fonti;
- verifica.

La revisione umana non cancella l'origine IA.

---

# 11. Invalidazione

Una summary viene rivalutata quando cambia una fonte materiale, una decisione, una baseline, una evidence, un requisito, un test, una policy o una esclusione.

La versione precedente non viene sovrascritta.

```text
SUMMARY_VERSION-0002
supersedes
SUMMARY_VERSION-0001
```

---

# 12. Context Package

Una summary può essere inclusa quando:

- lo scopo è compatibile;
- la copertura è sufficiente;
- non è invalid;
- non è stale per un uso corrente;
- le fonti sono risolvibili;
- le esclusioni sono visibili;
- la versione è congelata.

Non sostituisce automaticamente fonti obbligatorie.

---

# 13. Regole vincolanti

```text
summary identity ≠ summary version
summary ≠ source
stale historical summary ≠ invalid history
source change ≠ retroactive rewrite
approval ≠ removal of AI provenance
rollup ≠ unverifiable percentage
```

---

# 14. Decisione consolidata

```text
DEC-0101-010

Ogni summary possiede identità logica
e versioni immutabili.

Fonti, copertura, esclusioni e claim
appartengono alla versione.

Ogni sintesi mantiene drill-down
verso fonti, evidence e provenance.

Una nuova fonte o una nuova esclusione
produce invalidazione o nuova versione,
non sovrascrittura.
```
