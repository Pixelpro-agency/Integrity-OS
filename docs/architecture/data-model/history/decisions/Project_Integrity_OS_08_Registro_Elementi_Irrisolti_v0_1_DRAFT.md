# Project Integrity OS

## Registro di open question, assumption, risk, finding e conflict — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole
**Data:** 2026-08-06
**Task collegata:** `TODO-0101 — Definire schema dati minimo`
**Decisione collegata:** `DEC-0101-013 — APPROVED`

---

# 1. Principio

```text
ciò che non sappiamo
≠ ciò che supponiamo
≠ ciò che potrebbe accadere
≠ ciò che abbiamo rilevato
≠ ciò che risulta incompatibile
```

I cinque concetti devono condividere una vista comune, ma mantenere campi e lifecycle specializzati.

---

# 2. Modello ibrido

```text
register_items
├── open_questions
├── assumptions
├── risks
├── findings
└── conflicts
```

`register_items` contiene identità e metadati comuni.

Le tabelle specializzate conservano il significato specifico.

---

# 3. `register_items`

Campi concettuali:

```text
register_item_id
project_id
reference_code
item_type
title
summary
priority
severity
criticality
blocking
owner_actor_id
root_entity_type
root_entity_id
source_provenance_id
current_version
status_summary
opened_at
due_at
resolved_at
closed_at
archived_at
supersedes_register_item_id
created_by
created_at
updated_at
```

Tipi:

```text
OPEN_QUESTION
ASSUMPTION
RISK
FINDING
CONFLICT
```

Per gli elementi materiali è previsto `register_item_versions`.

---

# 4. Open questions

Rappresentano conoscenza mancante.

Entità:

```text
open_questions
question_answers
question_resolutions
```

Lifecycle:

```text
OPEN
UNDER_ANALYSIS
ANSWER_PROPOSED
ANSWERED
DEFERRED
BLOCKED
UNRESOLVABLE
SUPERSEDED
CLOSED
```

Una domanda `ANSWERED` può essere ancora `UNDER_REVIEW` dal punto di vista di governo.

Una domanda bloccante impedisce la transizione collegata finché non viene:

- risolta;
- differita tramite decisione;
- coperta da eccezione.

---

# 5. Assumptions

Rappresentano proposizioni temporaneamente accettate per procedere.

Entità:

```text
assumptions
assumption_validations
```

Campi specifici:

```text
statement
assumption_type
basis
confidence_level
impact_if_false
validation_method
validation_due_at
valid_from
valid_until
```

Lifecycle:

```text
DRAFT
ACTIVE
VALIDATING
CONFIRMED
PARTIALLY_CONFIRMED
DISPROVED
EXPIRED
REVOKED
SUPERSEDED
CLOSED
```

Una assumption deve indicare:

- chi l’ha accettata;
- scope;
- scadenza;
- metodo di validazione;
- impatto se falsa.

Una assumption smentita può rendere stale sintesi, Context Package, requisiti e verifiche.

---

# 6. Risks

Rappresentano eventi o condizioni future incerte.

Entità:

```text
risks
risk_assessments
risk_responses
risk_triggers
```

Formulazione raccomandata:

```text
A causa di [causa],
potrebbe verificarsi [evento incerto],
producendo [conseguenza].
```

Campi specifici:

```text
risk_nature
category
cause
uncertain_event
potential_consequence
probability_level
impact_level
exposure_level
proximity
trigger_description
response_strategy
contingency_plan
risk_owner_actor_id
review_due_at
```

Lifecycle:

```text
IDENTIFIED
UNDER_ASSESSMENT
ASSESSED
RESPONSE_PLANNED
MITIGATING
MONITORING
ACCEPTED
TRANSFERRED
AVOIDED
MATERIALIZED
EXPIRED
CLOSED
```

Un rischio materializzato resta nello storico e genera un nuovo elemento operativo.

---

# 7. Findings

Rappresentano elementi già emersi da analisi, osservazioni, test, verifiche o collaudi.

Entità:

```text
findings
finding_dispositions
```

Tipi:

```text
OBSERVATION
NONCONFORMITY
GAP
ANOMALY
DEFECT_CANDIDATE
POSITIVE_PRACTICE
IMPROVEMENT_OPPORTUNITY
SECURITY_FINDING
DATA_QUALITY_FINDING
DOCUMENTATION_FINDING
PROCESS_FINDING
INTEGRITY_VIOLATION
```

Lifecycle:

```text
OPEN
TRIAGED
CONFIRMED
DISMISSED
ACTION_REQUIRED
IN_REMEDIATION
RESOLVED
VERIFIED
ACCEPTED
SUPERSEDED
CLOSED
```

Disposizioni:

```text
CREATE_BUG
CREATE_TASK
CREATE_RISK
CREATE_QUESTION
CREATE_DECISION
ACCEPT
DISMISS
MONITOR
NO_ACTION_REQUIRED
```

Un finding materiale deve ricevere una disposizione.

---

# 8. Conflicts

Rappresentano incompatibilità tra almeno due parti.

Entità:

```text
conflicts
conflict_parties
conflict_resolutions
```

Tipi:

```text
SOURCE_CONFLICT
DECISION_CONFLICT
REQUIREMENT_CONFLICT
DOCUMENT_CONFLICT
EVIDENCE_CONFLICT
STATE_CONFLICT
SCOPE_CONFLICT
VERSION_CONFLICT
OWNERSHIP_CONFLICT
POLICY_CONFLICT
```

Lifecycle:

```text
OPEN
UNDER_ANALYSIS
CONFIRMED
RESOLUTION_PROPOSED
RESOLVED
ACCEPTED_BY_EXCEPTION
UNRESOLVABLE
SUPERSEDED
CLOSED
```

La risoluzione non cancella la parte risultata non prevalente.

---

# 9. Trasformazioni

Quando un elemento cambia natura, non viene rinominato o sovrascritto.

Si crea un nuovo elemento collegato.

Esempi:

```text
ASSUMPTION-001 DISPROVED
→ FINDING-004 derived_from ASSUMPTION-001

RISK-003 MATERIALIZED
→ BUG-017 materializes_from RISK-003
```

Relazioni iniziali:

```text
DERIVED_FROM
RAISES
ANSWERS
VALIDATES
DISPROVES
MATERIALIZES_AS
MITIGATED_BY
RESOLVED_BY
CONTRADICTS
BLOCKS
INVALIDATES
DUPLICATES
SUPERSEDES
RELATED_TO
CREATES
```

---

# 10. Severità, priorità, criticità e blocking

Sono dimensioni distinte.

## Severità

```text
INFO
LOW
MEDIUM
HIGH
CRITICAL
```

## Priorità

```text
LOW
NORMAL
HIGH
URGENT
```

## Criticità

```text
NON_CRITICAL
IMPORTANT
CRITICAL
SYSTEMIC
```

## Blocking

```text
true | false
```

---

# 11. Ownership e scadenze

Ogni elemento materiale deve avere un owner.

Timestamp possibili:

```text
due_at
review_due_at
valid_until
escalate_at
```

La scadenza produce eventi, escalation e possibili blocchi.

Non cancella l’elemento.

---

# 12. Impatto sulle transizioni

## Prima di `TASK READY`

Controllare:

- open question bloccanti;
- assumption critiche;
- rischi incompatibili;
- finding bloccanti;
- conflict di scope o decisione.

## Prima di `ATTEMPT IN_PROGRESS`

Includere nel Context Package gli elementi pertinenti.

## Prima di `VERIFICATION PASSED`

Non devono esistere conflict di evidenza irrisolti, finding bloccanti o assumption critiche smentite.

## Prima di `TASK COMPLETED`

Ogni elemento collegato deve essere risolto, accettato, trasferito, differito o coperto da eccezione.

---

# 13. Vista UI

La vista unificata è un rollup:

| Codice | Tipo | Titolo | Stato | Gravità | Bloccante | Owner |
|---|---|---|---|---|---|---|

Ogni riga apre il record specializzato, le fonti, le relazioni e lo storico.

---

# 14. Regole vincolanti

```text
Una open question non è una assumption.

Una assumption non è un fatto.

Un risk descrive un futuro incerto.

Un finding descrive qualcosa già emerso.

Un conflict richiede almeno due parti.

Gli elementi non cambiano tipo sovrascrivendosi.

Le trasformazioni creano nuovi elementi collegati.

Una assumption critica ha scadenza e validazione.

Un risk materializzato genera un elemento operativo.

Un finding materiale riceve una disposizione.

Un conflict non si risolve eliminando una fonte.

Gli elementi bloccanti governano le transizioni.

Ogni elemento resta navigabile verso fonti,
decisioni, task, verifiche ed esiti.
```

---

# 15. Decisione approvata

```text
DEC-0101-013 — APPROVED

Project Integrity OS distingue formalmente open question,
assumption, risk, finding e conflict.

Gli elementi condividono una identità comune tramite
register_items, ma mantengono lifecycle e campi specializzati.

Quando cambiano natura viene creato un nuovo elemento
collegato, preservando la catena storica.

Gli elementi bloccanti partecipano alle regole di transizione.
```
