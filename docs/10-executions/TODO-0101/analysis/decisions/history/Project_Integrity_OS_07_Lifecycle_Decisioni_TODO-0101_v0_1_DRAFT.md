# Project Integrity OS

## Lifecycle delle decisioni — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task collegata:** `TODO-0101 — Definire schema dati minimo`  
**Decisione collegata:** `DEC-0101-012 — APPROVED`

---

# 1. Scopo

Una decisione non deve essere ridotta a un codice e a uno stato generico.

Il sistema deve conservare:

- problema;
- contesto;
- alternative;
- fonti;
- versione esatta;
- motivazione;
- conseguenze;
- approvazione;
- periodo di efficacia;
- target influenzati;
- attività di attuazione;
- verifica dell’attuazione;
- sostituzioni, revoche e scadenze.

Principio:

```text
decidere
≠ rendere efficace
≠ attuare
≠ verificare
```

---

# 2. Entità concettuali

```text
decisions
decision_versions
decision_options
decision_inputs
decision_targets
decision_resolutions
decision_implementation_links
```

Entità future possibili:

```text
decision_reviews
decision_findings
decision_conformance_checks
```

---

# 3. Decisione logica e versioni

## `decisions`

Rappresenta l’identità stabile della questione decisionale.

Campi concettuali:

```text
decision_id
project_id
reference_code
decision_type
title
owner_actor_id
scope_level
criticality
reversibility
current_version_id
effective_version_id
created_at
closed_at
archived_at
```

## `decision_versions`

Ogni formulazione significativa è una versione immutabile.

Campi:

```text
decision_version_id
project_id
decision_id
version_number
problem_statement
context
decision_statement
rationale
consequences
assumptions
constraints
implementation_notes
review_requirements
effective_from
effective_until
content_hash
authoring_status
created_by
created_at
proposed_at
frozen_at
supersedes_decision_version_id
```

Una approvazione o un rifiuto deve riferirsi a una versione esatta.

Una versione già risolta non viene modificata.

---

# 4. Tipi di decisione

Vocabolario iniziale:

```text
ARCHITECTURAL
PRODUCT
DATA_MODEL
PROCESS
SECURITY
SCOPE
PRIORITY
DOCUMENTATION
OPERATIONAL
BASELINE
RELEASE
EXCEPTION_APPROVAL
CLOSURE
RECOVERY
```

---

# 5. Alternative

Le alternative devono essere registrate tramite `decision_options`.

Campi:

```text
decision_option_id
project_id
decision_version_id
reference_code
title
description
benefits
costs
risks
constraints
estimated_impact
selected
rejection_reason
sequence_number
created_at
```

Quando esiste una sola alternativa reale deve essere indicato il motivo.

Le opzioni respinte non vengono cancellate.

---

# 6. Input e fonti

`decision_inputs` collega la versione alle fonti che l’hanno originata o supportata.

Tipi di input:

```text
ANALYSIS
DOCUMENT_VERSION
REQUIREMENT
RISK
BUG
FINDING
OPEN_QUESTION
CONFLICT
EVIDENCE
VALIDATION
VERIFICATION
PREVIOUS_DECISION
USER_DIRECTION
```

Ruoli:

```text
PRIMARY_BASIS
SUPPORTING
CONTRADICTING
CONSTRAINT
RISK_INPUT
HISTORICAL_CONTEXT
```

Le fonti contraddittorie devono restare visibili.

---

# 7. Target e impatti

`decision_targets` registra gli elementi governati o modificati.

Target possibili:

```text
PROJECT
PHASE
WORK_ITEM
TASK
REQUIREMENT
DOCUMENT
DOCUMENT_VERSION
TEST_DEFINITION
POLICY
BASELINE
CONTEXT_PACKAGE
SCHEMA_ENTITY
```

Tipi di impatto:

```text
CREATES
MODIFIES
CONSTRAINS
AUTHORIZES
BLOCKS
INVALIDATES
SUPERSEDES
DEPRECATES
REQUIRES_REVIEW
```

Ogni impatto deve poter generare azioni, finding, eventi o stati `STALE`.

---

# 8. Dimensioni del lifecycle

## 8.1 Elaborazione e review

```text
DRAFT
PROPOSED
UNDER_REVIEW
CHANGES_REQUESTED
READY_FOR_RESOLUTION
RESOLVED
WITHDRAWN
```

## 8.2 Risoluzione

```text
PENDING
APPROVED
REJECTED
WITHDRAWN
```

La risoluzione è registrata tramite `decision_resolutions`.

Campi:

```text
decision_resolution_id
project_id
decision_id
decision_version_id
resolution_type
rationale
conditions_json
approval_policy_id
resolved_by_actor_id
resolved_at
effective_from
expires_at
created_at
```

## 8.3 Efficacia

```text
NOT_EFFECTIVE
SCHEDULED
EFFECTIVE
SUPERSEDED
REVOKED
EXPIRED
```

## 8.4 Attuazione

```text
NOT_APPLICABLE
NOT_STARTED
IN_PROGRESS
PARTIALLY_IMPLEMENTED
IMPLEMENTED
BLOCKED
FAILED
```

## 8.5 Verifica dell’attuazione

```text
NOT_REQUIRED
NOT_VERIFIED
PARTIALLY_VERIFIED
VERIFIED
VERIFICATION_FAILED
STALE
```

---

# 9. Attuazione

`decision_implementation_links` collega la decisione a:

- work item;
- task;
- modifiche documentali;
- migrazioni;
- configurazioni;
- baseline.

Campi:

```text
decision_implementation_link_id
project_id
decision_version_id
implementation_entity_type
implementation_entity_id
required
implementation_role
status
created_at
completed_at
```

Una decisione efficace non è automaticamente attuata.

Una decisione attuata non è automaticamente verificata.

---

# 10. Condizioni

Una risoluzione approvata può contenere condizioni.

Le condizioni non devono restare in testo libero dimenticato.

Devono diventare elementi:

- verificabili;
- assegnabili;
- dotati di scadenza;
- collegati a task o controlli;
- capaci di bloccare l’efficacia quando richiesto.

Non viene introdotto uno stato principale `APPROVED_WITH_CONDITIONS`.

Si usa:

```text
resolution_type: APPROVED
conditions_json: [...]
```

---

# 11. Sostituzione, revoca e scadenza

## Sostituzione

Una nuova decisione prende il posto della precedente:

```text
DECISION-002
supersedes DECISION-001
```

La decisione precedente resta nello storico.

Devono essere registrati:

- elementi modificati;
- parti ancora valide;
- documenti da aggiornare;
- Context Package da rendere stale;
- requisiti e test da rivalutare;
- baseline eventualmente da sostituire.

## Revoca

Annulla una decisione senza sostituzione diretta.

Richiede:

- motivo;
- conseguenze;
- rollback;
- rischi;
- elementi rimasti privi di governo.

## Scadenza

Le decisioni temporanee usano:

```text
effective_from
effective_until
review_due_at
```

Una decisione scaduta non resta efficace per dimenticanza.

---

# 12. Conflitti

Due decisioni efficaci non possono governare lo stesso ambito in modo incompatibile senza segnalazione.

Condizioni indicative:

```text
stesso target
+
periodi di efficacia sovrapposti
+
regole incompatibili
+
assenza di relazione SUPERSEDES
```

Risultato:

```text
DECISION_CONFLICT
```

Il conflitto deve generare un elemento governato e può bloccare le attività interessate.

---

# 13. Reversibilità

Vocabolario:

```text
REVERSIBLE
REVERSIBLE_WITH_COST
DIFFICULT_TO_REVERSE
IRREVERSIBLE
UNKNOWN
```

Le decisioni difficili o irreversibili richiedono un livello di review superiore.

---

# 14. Propagazione

Quando una decisione diventa efficace, il sistema deve poter:

- richiedere aggiornamenti documentali;
- creare task;
- invalidare sintesi;
- rendere stale Context Package;
- rivalutare requisiti e test;
- segnalare conflitti;
- bloccare attività incompatibili;
- richiedere una nuova baseline.

Nessuna propagazione deve avvenire silenziosamente.

---

# 15. Decision Log

Il Decision Log è una sintesi navigabile.

Deve consentire il drill-down verso:

```text
problema
alternative
versioni
fonti
risoluzioni
approvazioni
target
attuazioni
verifiche
storico
```

Non è la fonte primaria.

---

# 16. Regole vincolanti

```text
Una decisione logica è distinta dalle sue versioni.

Una risoluzione riguarda una versione esatta.

Una versione risolta è immutabile.

APPROVED non implica EFFECTIVE.

EFFECTIVE non implica IMPLEMENTED.

IMPLEMENTED non implica VERIFIED.

Le modifiche producono nuove versioni o nuove decisioni.

Le decisioni respinte e sostituite restano nello storico.

Ogni decisione conserva fonti, alternative,
motivazione, conseguenze e target.

Ogni impatto prodotto viene tracciato.

I conflitti vengono segnalati e governati.
```

---

# 17. Decisione approvata

```text
DEC-0101-012 — APPROVED

Project Integrity OS separa decisione logica, versioni,
alternative, input, target, risoluzione, efficacia,
attuazione e verifica dell’attuazione.

Ogni approvazione o rifiuto riguarda una versione
esatta e congelata.

Sostituzioni, revoche, scadenze, conflitti e conseguenze
restano registrati.

Il Decision Log è una vista sintetica con drill-down
verso tutte le fonti e gli esiti.
```
