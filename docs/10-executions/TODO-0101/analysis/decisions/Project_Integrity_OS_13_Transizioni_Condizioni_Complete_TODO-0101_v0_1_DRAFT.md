# Project Integrity OS

## Condizioni complete delle transizioni — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task collegata:** `TODO-0101 — Definire schema dati minimo`  
**Decisione collegata:** `DEC-0101-018 — APPROVED`

---

# 1. Principio

```text
un campo di stato non si modifica direttamente
```

Ogni cambiamento avviene tramite:

```text
azione nominata
→ richiesta
→ autorizzazione
→ valutazione
→ commit atomico
→ evento
→ verifica degli effetti
```

# 2. Concetti

```text
stato
azione
transizione
condizione
effetto
eccezione
risultato
```

Questi concetti non devono essere compressi in un semplice aggiornamento di colonna.

# 3. Entità concettuali

```text
transition_definitions
transition_definition_versions
transition_requirements
transition_effects

transition_requests
transition_evaluations
transition_evaluation_results
transition_executions
transition_effect_results
```

Entità future:

```text
transition_compensations
transition_recovery_runs
transition_policy_bindings
```

# 4. Definizioni versionate

Ogni transizione conserva:

```text
action code
target entity type
source state
target state
required permission
role constraints
separation of duties
approval policy
integrity profile
concurrency strategy
idempotency
atomicity scope
preconditions
postconditions
effects
compensation
effective period
content hash
```

L’esecuzione storica conserva la versione esatta applicata.

# 5. Catalogo governato

Non viene adottata una macchina a stati completamente libera.

Il core conserva le invarianti fondamentali.

Le policy possono:

- aggiungere restrizioni;
- richiedere approvazioni;
- aggiungere test e controlli;
- vietare transizioni;
- restringere ruoli e scope.

Non possono rimuovere invarianti strutturali non derogabili.

# 6. Requisiti della transizione

Tipi iniziali:

```text
ENTITY_STATE
RELATED_ENTITY_EXISTS
RELATED_ENTITY_STATE
REQUIRED_VERSION
REQUIRED_DOCUMENT
REQUIRED_CONTEXT_PACKAGE
REQUIRED_REQUIREMENT_COVERAGE
REQUIRED_TEST_RESULT
REQUIRED_VERIFICATION
REQUIRED_VALIDATION
REQUIRED_APPROVAL
REQUIRED_INTEGRITY_PROFILE
NO_BLOCKING_REGISTER_ITEM
NO_OPEN_CONFLICT
NO_BLOCKING_BUG
DEPENDENCY_SATISFIED
AUTHORIZATION
SEPARATION_OF_DUTIES
TEMPORAL
CONTENT_AVAILABLE
REPOSITORY_STATE
BASELINE_COMPATIBILITY
CUSTOM_DETERMINISTIC_RULE
```

Ogni requisito indica:

```text
mandatory
derogable
blocking
evaluation method
failure code
failure message
remediation
```

# 7. Enforcement

Classi:

```text
INVARIANT
POLICY_REQUIRED
ADVISORY
```

Una eccezione può coprire soltanto regole dichiarate derogabili.

Un override resta distinto da `PASSED`.

# 8. Lifecycle operativo

```text
REQUESTED
AUTHORIZING
EVALUATING
READY_TO_COMMIT
COMMITTING
COMMITTED
VERIFYING_EFFECTS
COMPLETED
```

Esiti alternativi:

```text
DENIED
BLOCKED
CANCELLED
FAILED
PARTIALLY_EFFECTIVE
RECOVERY_REQUIRED
SUPERSEDED
```

# 9. Transition request

Ogni richiesta specifica:

```text
target entity
target version
transition version
expected current state
requested target state
expected aggregate sequence
actor
session
delegation
reason
payload
idempotency key
correlation id
scadenza
```

Il target non può essere definito tramite filtro ambiguo.

# 10. Valutazione

Ogni evaluation conserva:

```text
transition version
integrity profile version
access policy version
approval policy version
repository snapshot
state snapshot
baseline
result hash
```

Risultati dei singoli requisiti:

```text
PASSED
FAILED
WARNING
BLOCKED
NOT_APPLICABLE
NOT_EVALUATED
TECHNICAL_FAILURE
OVERRIDDEN_BY_EXCEPTION
```

Esito complessivo:

```text
ELIGIBLE
ELIGIBLE_WITH_WARNINGS
ELIGIBLE_WITH_EXCEPTIONS
NOT_ELIGIBLE
BLOCKED
INDETERMINATE
TECHNICAL_FAILURE
```

# 11. Validità temporale e concorrenza

Una valutazione può scadere.

Prima del commit vengono ricontrollati:

```text
stato
aggregate sequence
sessione
permessi
eccezioni
versioni
blocker
hash del target
```

Optimistic concurrency:

```text
expected_current_state
expected_aggregate_sequence
```

In caso di divergenza:

```text
CONCURRENT_MODIFICATION
```

# 12. Idempotenza

Ogni transizione materiale può usare una `idempotency_key`.

Stesso payload già completato:

```text
restituire risultato esistente
```

Stessa chiave con payload differente:

```text
IDEMPOTENCY_CONFLICT
```

Operazione incompleta:

```text
resume
recovery
oppure block
```

# 13. Atomicità interna

Nella stessa transazione devono essere eseguiti:

```text
verifica sequence
aggiornamento stato
relazioni obbligatorie
transition execution
evento
aggregate sequence
```

Non devono esistere stato senza evento o evento senza stato.

# 14. Effetti esterni

Per file, Git, provider, export, purge o processi esterni:

```text
database commit
→ effect manifest
→ execution
→ result
→ postcondition verification
```

Stati:

```text
PENDING
RUNNING
COMPLETED
FAILED
TECHNICAL_FAILURE
COMPENSATED
UNRECOVERABLE
```

Un effetto esterno fallito può produrre:

```text
PARTIALLY_EFFECTIVE
RECOVERY_REQUIRED
```

# 15. Compensazione

Strategie:

```text
DATABASE_ROLLBACK
COMPENSATING_TRANSITION
MANUAL_RECOVERY
IRREVERSIBLE
```

Le azioni irreversibili richiedono approvazione superiore e preview completa.

# 16. Postcondizioni

Dopo il commit devono essere controllati:

```text
stato finale
evento
aggregate sequence
relazioni obbligatorie
effetti esterni
hash
proiezioni
integrity profile post-transizione
coerenza aggregata
```

Un fallimento produce finding e `RECOVERY_REQUIRED`.

# 17. Effetti derivati

Le transizioni possono generare:

```text
eventi
task
finding
summary stale
Context Package stale
requisiti da rivalutare
baseline stale
approval revocate
notifiche
projection stale
open question
risk
integrity run
```

Gli effetti devono essere dichiarati nella versione della transizione.

# 18. Regole aggregate e riaperture

Una transizione superiore non forza silenziosamente gli stati inferiori.

Le riaperture avvengono tramite azioni dedicate:

```text
REOPEN_TASK
REOPEN_BUG
REOPEN_FINDING
REVOKE_APPROVAL
SUPERSEDE_BASELINE
```

La riapertura conserva motivo, fonte, attore e conseguenze.

# 19. Profili minimi

## PROJECT_ACTIVATION_PROFILE

```text
identità valida
source root o repository
policy iniziali
Project Owner
schema inizializzato
nessuna violazione fatal
baseline iniziale o eccezione
```

## TASK_READY_PROFILE

```text
gerarchia valida
obiettivo e scope
Task Contract frozen
requisiti e criteri
dipendenze
decisioni bloccanti
open question
assumption critiche
rischi
Context Package generabile
executor assegnabile
```

## ATTEMPT_START_PROFILE

```text
task valida
execution valida
numero tentativi
prompt frozen
Context Package VALID e FROZEN
snapshot iniziale
authorization snapshot
executor autorizzato
nessun blocco critico
```

## ATTEMPT_REPORT_PROFILE

```text
attempt corretto
report originale conservato
provenienza
campi obbligatori
nessuna mutazione
quarantena se invalido
```

## VERIFICATION_PASS_PROFILE

```text
report
reconciliation
evidence
test obbligatori
commit e baseline
conflict risolti
finding assenti
assumption non smentite
integrità
verifier autorizzato
separation of duties
```

## TASK_COMPLETION_PROFILE

```text
execution valida
attempt finale
verification PASSED
validation richiesta
requisiti VERIFIED
criteri PASSED
bug e finding gestiti
question risolte
rischi gestiti
decisioni attuate
documentazione
approval finale
versione verificata coerente
nessuna violazione fatal
```

## BASELINE_APPROVAL_PROFILE

```text
state snapshot
repository snapshot
document versions frozen
decisioni efficaci
requisiti e verifiche coerenti
Context Package e summary non stale
integrity run
nessun conflict bloccante
manifest e hash
approvatori autorizzati
separation of duties
```

# 20. Lifecycle principali

## Project

```text
DRAFT
INITIALIZING
ACTIVE
SUSPENDED
CLOSING
CLOSED
ARCHIVED
PENDING_DELETION
TOMBSTONED
```

## Phase e work item

```text
DRAFT
PLANNED
READY
IN_PROGRESS
BLOCKED
IN_VERIFICATION
COMPLETED
DEFERRED
CANCELLED
ARCHIVED
```

## Task

```text
DRAFT
DEFINED
READY
IN_EXECUTION
BLOCKED
IN_VERIFICATION
COMPLETED
DEFERRED
CANCELLED
ARCHIVED
```

## Task execution

```text
PLANNED
READY
ACTIVE
PAUSED
BLOCKED
AWAITING_VERIFICATION
COMPLETED
FAILED
CANCELLED
SUPERSEDED
```

## Attempt

```text
PLANNED
READY
IN_PROGRESS
AWAITING_REPORT
REPORTED
RECONCILING
IN_VERIFICATION
VERIFIED_PASSED
VERIFIED_FAILED
TECHNICAL_FAILURE
ABORTED
CANCELLED
SUPERSEDED
```

## Verification

```text
DRAFT
PLANNED
READY
IN_PROGRESS
BLOCKED
PASSED
FAILED
INCONCLUSIVE
SUPERSEDED
REVOKED
```

## Baseline

```text
DRAFT
BUILDING
VALIDATING
READY_FOR_APPROVAL
APPROVED
EFFECTIVE
SUPERSEDED
REVOKED
ARCHIVED
```

# 21. Tentativi

La policy dei tentativi appartiene alla `task_execution` o al contratto.

Campi:

```text
maximum_attempts
attempt_counting_policy
technical_failure_consumes_attempt
aborted_attempt_consumes_attempt
manual_override_policy
```

Devono essere distinti:

```text
attempt_number
consumed_attempt_number
```

Le deroghe sono esplicite.

# 22. Eccezioni

Una eccezione deve indicare:

```text
regola
transizione
target
scope
motivo
rischio
azioni compensative
approvatore
valid_from
valid_until
stato
```

Prima del commit si verifica che sia valida, non scaduta e applicabile.

L’esito resta:

```text
ELIGIBLE_WITH_EXCEPTIONS
```

# 23. Batch

Le transizioni multiple usano un manifest esatto di:

```text
UUID
versione
stato atteso
aggregate sequence
hash
```

Modalità:

```text
ALL_OR_NOTHING
BEST_EFFORT
SEQUENTIAL_STOP_ON_FAILURE
```

La modalità viene dichiarata prima dell’esecuzione.

# 24. UI

La UI deve distinguere:

```text
action available
action blocked
action requires approval
action available with exception
```

Il drill-down mostra:

```text
stato
transizione
condizioni
pass
fail
warning
eccezioni
autorizzazioni
effetti
```

Il core Rust resta l’autorità.

# 25. Regole vincolanti

```text
Gli stati non vengono modificati direttamente.

Ogni passaggio usa una transizione versionata.

La richiesta indica target, stato e sequence attesi.

Autorizzazione e condizioni precedono il commit.

La valutazione può diventare stale.

Stato, evento e relazioni obbligatorie sono atomici.

Gli effetti esterni sono journaled.

Un effetto parziale non è completato.

Le correzioni usano transizioni compensative.

Le eccezioni non trasformano fallimenti in pass.

Le transizioni aggregate non forzano gli inferiori.

Le riaperture sono azioni esplicite.

Ogni esecuzione conserva policy e versioni applicate.

Il frontend presenta; il core decide.
```

# 26. Decisione approvata

```text
DEC-0101-018 — APPROVED

Project Integrity OS vieta la modifica diretta
degli stati governati.

Ogni cambiamento usa transition definition e version,
requirements, request, evaluation, execution ed effects.

Le transizioni applicano autorizzazione, integrità,
concorrenza, idempotenza, atomicità, postcondizioni
e compensazione.

Gli effetti esterni sono journaled e verificati.

Le eccezioni restano visibili come override.

Riaperture, revoche e rettifiche sono nuove transizioni.

Il core Rust è l’autorità finale.
```
