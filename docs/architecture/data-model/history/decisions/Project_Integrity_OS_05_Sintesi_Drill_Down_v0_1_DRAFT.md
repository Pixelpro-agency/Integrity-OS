# Project Integrity OS

## Sintesi, drill-down, copertura e obsolescenza — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole
**Data:** 2026-08-06
**Task collegata:** `TODO-0101 — Definire schema dati minimo`
**Decisione collegata:** `DEC-0101-010 — APPROVED`
**Ambito:** viste sintetiche, navigazione progressiva, fonti, copertura, freschezza e validità

---

# 1. Scopo

Le sintesi servono a ridurre il carico cognitivo, migliorare la UI e permettere alle IA di leggere soltanto il contesto necessario.

Non devono:

- sostituire le fonti;
- nascondere omissioni;
- diventare documenti monolitici;
- apparire aggiornate quando le fonti sono cambiate;
- impedire l’accesso al dettaglio;
- perdere il collegamento al significato originale.

Principio:

> ogni sintesi è una vista compatta e navigabile di informazioni più dettagliate.

---

# 2. Drill-down tracciabile

Ogni valore sintetico deve poter essere aperto progressivamente:

```text
sintesi
→ dettaglio strutturato
→ contenuto originale
→ fonti
→ evidenze
```

Esempio UI:

```text
Tentativi: 3
```

Primo livello di dettaglio:

```text
ATTEMPT-0001 — VERIFIED_FAILED
ATTEMPT-0002 — TECHNICAL_FAILURE
ATTEMPT-0003 — VERIFIED_PASSED
```

Dettaglio del tentativo:

```text
Context Package
prompt
snapshot
report
comandi
test
errori
evidenze
riconciliazione
verifica
decisione finale
```

La sintesi non deve diventare un vicolo cieco.

---

# 3. Tipi di riduzione

```text
EXCERPT
STRUCTURED_EXTRACTION
SUMMARY
ROLLUP
CURRENT_STATE_SNAPSHOT
```

## 3.1 `EXCERPT`

Parte di una fonte estratta senza reinterpretazione sostanziale.

Deve registrare:

- fonte;
- versione;
- hash;
- sezione;
- locator;
- testo estratto.

## 3.2 `STRUCTURED_EXTRACTION`

Trasforma contenuto in campi strutturati.

Esempio:

```text
report
→ file modificati
→ comandi
→ test
→ commit
→ push
```

Deve registrare:

- parser;
- versione;
- locator;
- errori;
- ambiguità;
- campi non estratti.

## 3.3 `SUMMARY`

Riduce e riformula una o più fonti per uno scopo.

## 3.4 `ROLLUP`

Aggrega dati strutturati.

Esempio:

```text
12 task
8 completate
2 bloccate
2 attive
```

Deve essere principalmente deterministico.

## 3.5 `CURRENT_STATE_SNAPSHOT`

Vista dello stato corrente congelata perché usata in una decisione, un Context Package o una verifica.

---

# 4. Entità concettuali

```text
summaries
summary_sources
summary_coverage
summary_claims
summary_claim_sources
```

Potrà essere aggiunta:

```text
summary_profiles
```

per definire profili riutilizzabili.

---

# 5. `summaries`

Campi concettuali:

```text
summary_id
project_id
reference_code
summary_type
purpose
target_role
root_entity_type
root_entity_id
title
content_text
structured_content_json
generation_method
generator_actor_type
generator_actor_id
generator_version
summary_profile_id
status
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
supersedes_summary_id
```

---

# 6. Scopo

Ogni sintesi deve dichiarare perché esiste.

Vocabolario iniziale:

```text
EXECUTIVE_ORIENTATION
TASK_PREPARATION
ATTEMPT_HANDOFF
VERIFICATION_REVIEW
PROJECT_REOPENING
DIAGNOSTIC
APPROVAL_REVIEW
HISTORICAL_RECAP
```

Una sintesi per orientamento non sostituisce evidenze e output durante una verifica.

---

# 7. Fonti

Ogni fonte deve essere registrata tramite `summary_sources`.

Campi:

```text
summary_source_id
project_id
summary_id
source_entity_type
source_entity_id
source_version_id
source_reference_code
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

Le fonti contraddittorie non devono essere escluse silenziosamente.

---

# 8. Copertura

La sintesi deve indicare quali parti del problema copre.

Stati:

```text
FULL
PARTIAL
MINIMAL
NOT_COVERED
NOT_APPLICABLE
UNKNOWN
```

Dimensioni iniziali:

```text
OBJECTIVES
DECISIONS
DOCUMENTS
REQUIREMENTS
TASKS
ATTEMPTS
TESTS
EVIDENCE
BUGS
RISKS
EXCEPTIONS
TEMPORAL_RANGE
REPOSITORY_SCOPE
```

Esempio:

```text
task: FULL
bug: PARTIAL
decisioni: FULL
evidenze tecniche: MINIMAL
```

Una percentuale può essere usata soltanto quando è misurabile.

Esempio valido:

```text
8 requisiti coperti su 10 = 80%
```

Esempio non valido:

```text
87% del progetto
```

senza base deterministica.

---

# 9. Esclusioni

Ogni esclusione materiale deve essere visibile.

Campi:

```text
excluded_entity_type
excluded_entity_id
excluded_section
exclusion_reason
materiality
impact_note
```

Motivazioni:

```text
OUT_OF_SCOPE
NOT_RELEVANT
DUPLICATE
SUPERSEDED
SENSITIVE
TOKEN_LIMIT
UNAVAILABLE
UNVERIFIED
CONFLICTING
MANUALLY_EXCLUDED
```

Materialità:

```text
NON_MATERIAL
LOW
MEDIUM
HIGH
BLOCKING
```

Una sintesi con esclusioni `BLOCKING` non può essere considerata completa.

---

# 10. Freschezza e validità

Sono dimensioni differenti.

## 10.1 Freshness

```text
CURRENT
POTENTIALLY_STALE
STALE
UNKNOWN
```

## 10.2 Validity

```text
VALID
VALID_WITH_LIMITATIONS
INVALID
SUPERSEDED
REVOKED
```

Una sintesi storica può essere:

```text
freshness_status: STALE
validity_status: VALID
```

come prova del contesto consegnato in passato.

Non deve essere usata per descrivere lo stato corrente.

---

# 11. Cause di obsolescenza

Una sintesi deve essere rivalutata quando cambia:

- una fonte;
- una decisione;
- una baseline;
- una evidenza;
- un report;
- un bug materiale;
- lo stato di una task;
- la policy;
- il periodo temporale;
- un requisito;
- un test;
- una esclusione materiale.

La sintesi precedente non viene sovrascritta.

Si crea:

```text
SUMMARY-0002
supersedes SUMMARY-0001
```

---

# 12. Source set hash

Ogni sintesi deve registrare un hash deterministico delle fonti.

Deve includere almeno:

- identità;
- versioni;
- hash;
- locator;
- ordine rilevante;
- policy;
- esclusioni materiali.

Il `source_set_hash` serve a stabilire se due sintesi sono state costruite sullo stesso insieme di fonti.

---

# 13. Metodo di generazione

Vocabolario:

```text
HUMAN_AUTHORED
DETERMINISTIC_SYSTEM
AI_GENERATED
HYBRID
```

Una sintesi IA deve registrare:

- provider;
- modello;
- versione;
- sessione;
- Context Package;
- istruzione;
- fonti;
- stato di verifica.

La revisione umana non cancella l’origine IA.

---

# 14. Affermazioni materiali

Per sintesi importanti devono essere rappresentabili:

```text
summary_claims
summary_claim_sources
```

Campi concettuali:

```text
summary_claim_id
summary_id
claim_text
claim_type
importance
verification_status
sequence_number
```

Ogni claim materiale può collegarsi a:

- fonte;
- versione;
- locator;
- evidenza;
- verifica.

Non è necessario spezzare ogni frase.

È necessario per affermazioni:

- tecniche;
- decisionali;
- controverse;
- usate per approvazioni;
- usate per creare task.

---

# 15. Periodo temporale

Ogni sintesi deve dichiarare:

```text
covers_from
covers_until
as_of
```

Distinguiamo:

```text
HISTORICAL_SNAPSHOT
CURRENT_ORIENTATION
```

Una sintesi senza riferimento temporale può essere scambiata erroneamente per stato corrente.

---

# 16. Uso nei Context Package

Una sintesi può essere inclusa soltanto quando:

- lo scopo è compatibile;
- la copertura è sufficiente;
- non è `INVALID`;
- non è `STALE` per un uso corrente;
- le fonti sono risolvibili;
- le esclusioni sono visibili;
- la versione viene congelata.

Una sintesi non sostituisce automaticamente una fonte obbligatoria.

Esempio:

```text
Task Contract completo
```

non può essere sostituito da una sintesi, salvo policy esplicita.

---

# 17. Struttura gerarchica delle sintesi

Le sintesi devono evitare un nuovo documento monolitico.

Esempio:

```text
project summary
├── phase summaries
│   ├── work item summaries
│   │   └── task summaries
│   └── risk summaries
└── current-state rollup
```

Ogni livello mantiene il collegamento ai livelli inferiori.

---

# 18. Regole vincolanti

```text
Una sintesi non sostituisce le fonti.

Ogni sintesi ha uno scopo.

Ogni sintesi registra fonti, versioni e hash.

Ogni sintesi dichiara copertura ed esclusioni.

Ogni dato sintetico è navigabile fino al dato originale.

Una fonte modificata non aggiorna retroattivamente la sintesi.

Una sintesi obsoleta resta disponibile come storico.

Una sintesi IA conserva modello, Context Package e fonti.

Una approvazione non cancella l’origine IA.

Una sintesi con omissioni bloccanti non è completa.

Un Context Package non usa sintesi stale
per rappresentare lo stato corrente.

Le sintesi usate per decisioni e approvazioni
sono congelate.
```

---

# 19. Decisione approvata

```text
DEC-0101-010 — APPROVED

Project Integrity OS tratta excerpt, estrazioni,
sintesi, rollup e snapshot dello stato come artefatti
derivati, persistenti, versionati e verificabili.

Ogni sintesi conserva scopo, fonti, versioni,
hash, copertura, esclusioni, materialità,
periodo temporale, freschezza, validità,
metodo di generazione e versione sostituita.

Ogni sintesi è una vista compatta con drill-down
verso dettaglio, contenuto originale, fonti ed evidenze.
```

---

# 20. Aspetti da consolidare successivamente

- profili di sintesi;
- policy UI;
- regole di caching;
- indici;
- algoritmi di invalidazione;
- formato dei claim;
- gestione token budget;
- query materializzate;
- implementazione incrementale.
