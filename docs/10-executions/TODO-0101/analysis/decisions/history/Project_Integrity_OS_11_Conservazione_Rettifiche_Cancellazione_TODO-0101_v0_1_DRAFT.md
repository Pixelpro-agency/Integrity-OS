# Project Integrity OS

## Conservazione, archiviazione, rettifiche e cancellazione — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task collegata:** `TODO-0101 — Definire schema dati minimo`  
**Decisione collegata:** `DEC-0101-016 — APPROVED`

---

# 1. Principio

```text
un elemento non più utilizzabile
non è necessariamente un elemento da cancellare
```

Project Integrity OS distingue formalmente:

```text
ARCHIVE
WITHDRAW
VOID
SUPERSEDE
CORRECT
REDACT
PURGE_CONTENT
HARD_DELETE
RESTORE
TOMBSTONE
```

Queste operazioni hanno significati, autorizzazioni e conseguenze differenti.

# 2. Significato delle operazioni

## ARCHIVE

L’elemento esce dalle viste operative ma resta disponibile come storico. Non perde automaticamente validità retroattiva e mantiene relazioni, provenienza e reference code.

## WITHDRAW

Una proposta viene ritirata prima dell’approvazione o dell’attuazione. Restano registrati proponente, versione, motivo, momento e sostituzione eventuale.

## VOID

Un atto resta nello storico ma viene dichiarato non valido operativamente. È adatto, per esempio, a una approval registrata sul target errato.

## SUPERSEDE

Una nuova entità o versione sostituisce quella precedente. La precedente resta valida per ricostruire il passato.

## CORRECT

Una rettifica crea un nuovo record o una nuova versione collegata. Il valore originario non viene cancellato.

## REDACT

Una parte del contenuto viene nascosta, trasformata o esclusa dalla vista o dall’export. La redazione non deve fingere che il contenuto non sia mai esistito.

## PURGE_CONTENT

Il contenuto materiale viene rimosso fisicamente, ma resta un record minimale con identità, hash, motivo, policy, autorizzazione, timestamp e dipendenze storiche.

## HARD_DELETE

Il record viene eliminato fisicamente dal database. È ammesso soltanto in casi limitati e privi di valore storico.

## RESTORE

Un elemento archiviato, ritirato o quarantinato torna in uno stato operativo consentito tramite una nuova operazione tracciata.

## TOMBSTONE

Rimane un record minimale che preserva identità, project_id, reference_code, stato finale, hash precedente, motivo, autorizzazione e relazioni essenziali.

# 3. Classi di conservazione

## Classe A — Record governati immutabili

Esempi:

```text
events
decision resolutions
approvals
frozen document versions
frozen prompts
original reports
evidence
command run conclusi
test run conclusi
verifications concluse
baseline approvate
integrity run conclusi
```

Regola:

```text
nessun hard delete ordinario
```

Sono ammesse rettifica, annullamento logico, sostituzione, revoca, redazione, purge del contenuto e tombstone.

## Classe B — Entità operative governate

Esempi:

```text
projects
phases
work_items
tasks
requirements
bugs
risks
open questions
```

Sono ammesse archiviazione, cancellazione logica, ripristino e sostituzione. L’hard delete è consentito soltanto se il record è ancora draft, non referenziato e mai utilizzato.

## Classe C — Draft non utilizzati

Possono essere eliminati fisicamente quando:

- non sono referenziati;
- non hanno eventi materiali;
- non sono stati congelati;
- non sono stati consegnati;
- non sono inclusi in decisioni, baseline o verifiche;
- la policy lo consente.

## Classe D — Contenuti rigenerabili

Esempi:

```text
cache
projection
rollup
indice di ricerca
preview
temporary export
```

Possono essere eliminati e ricreati dalle fonti senza compromettere storico, prove o ricostruzioni.

# 4. Stati comuni

Vocabolario proposto per `project_entities.record_state`:

```text
ACTIVE
DRAFT
INACTIVE
ARCHIVED
WITHDRAWN
VOIDED
SUPERSEDED
REVOKED
QUARANTINED
PENDING_DELETION
CONTENT_PURGED
TOMBSTONED
```

Non tutte le entità possono assumere tutti gli stati. Le transizioni consentite devono essere governate dal tipo di entità e dalle regole di integrità.

# 5. Entità concettuali

```text
retention_policies
retention_policy_versions
deletion_requests
deletion_assessments
deletion_actions
record_tombstones
redaction_records
correction_records
archive_records
restoration_records
deletion_certificates
```

# 6. Retention policy

Ogni policy deve definire almeno:

```text
target_entity_type
data_classification
default_retention_mode
minimum_retention_duration
maximum_retention_duration
archive_allowed
hard_delete_allowed
content_purge_allowed
redaction_allowed
restoration_allowed
approval_policy
```

Modalità iniziali:

```text
PERMANENT
PROJECT_LIFETIME
UNTIL_BASELINE_SUPERSEDED
UNTIL_TASK_CLOSED
TIME_LIMITED
UNTIL_EXPLICIT_REVIEW
REGENERABLE
EXTERNAL_POLICY
```

Le policy sono versionate. Ogni operazione storica conserva la versione applicata.

# 7. Deletion request

Ogni rimozione significativa richiede una richiesta governata.

Lifecycle:

```text
DRAFT
SUBMITTED
UNDER_ASSESSMENT
CHANGES_REQUESTED
APPROVED
REJECTED
SCHEDULED
EXECUTING
COMPLETED
COMPLETED_WITH_WARNINGS
PARTIALLY_COMPLETED
FAILED
CANCELLED
```

Azioni richiedibili:

```text
ARCHIVE
WITHDRAW
VOID
REDACT
PURGE_CONTENT
HARD_DELETE
ANONYMIZE
CRYPTO_ERASE
TOMBSTONE
```

# 8. Valutazione d’impatto

Prima dell’approvazione devono essere controllati almeno:

- stato frozen;
- uso in attempt;
- inclusione in baseline;
- uso in decisioni e approval;
- dipendenze di verifiche;
- necessità per ricostruzioni storiche;
- uso in summary e Context Package;
- presenza di dati sensibili;
- alternative alla cancellazione;
- possibilità di redazione;
- impatto su hash e manifest;
- copie in backup, export, repository e storage esterni.

Una valutazione incompleta blocca l’operazione.

# 9. Hard delete

È ammesso soltanto quando tutte le condizioni sono vere:

```text
record DRAFT
mai frozen
mai approved
mai delivered
mai incluso in baseline
mai usato in attempt
nessun evento materiale dipendente
nessuna relazione governata
nessuna evidence o verification dipendente
nessun obbligo di retention
policy esplicitamente permissiva
assessment completato
autorizzazione presente
```

Altrimenti si usa:

```text
ARCHIVE
VOID
REDACT
PURGE_CONTENT
TOMBSTONE
```

# 10. Rettifiche

Le rettifiche non sovrascrivono il dato storico.

`correction_records` deve poter registrare:

```text
target_entity
target_version
target_field_path
original_value_hash
corrected_value
correction_type
reason
source_provenance
approvazione
effective_from
recorded_at
```

Tipi iniziali:

```text
FACTUAL_CORRECTION
METADATA_CORRECTION
LINK_CORRECTION
TEMPORAL_CORRECTION
CLASSIFICATION_CORRECTION
IDENTITY_CORRECTION
TRANSCRIPTION_CORRECTION
```

Per contenuti frozen si crea una nuova versione collegata tramite `supersedes`.

# 11. Eventi e rettifiche

Gli eventi append-only non vengono modificati. Le correzioni usano nuovi eventi:

```text
event.reversed
event.corrected
event.superseded
```

La hash chain resta integra.

# 12. Redazione

Tipi iniziali:

```text
MASK
REMOVE_FROM_VIEW
REMOVE_FROM_EXPORT
REPLACE_WITH_MARKER
TOKENIZE
ANONYMIZE
ENCRYPT_AND_RESTRICT
PURGE_ORIGINAL
```

La UI deve mostrare marker espliciti:

```text
[REDACTED]
[CONTENT PURGED — RECORD RETAINED]
```

La redazione può essere reversibile o irreversibile. Quella irreversibile richiede policy e approvazione superiori.

# 13. Purge e tombstone

Quando un contenuto viene purgato restano almeno:

```text
identità
project_id
reference_code
tipo
hash originale
dimensione
motivo
policy
approvatore
timestamp
replacement eventuale
tombstone hash
```

I `reference_code` non vengono riciclati.

# 14. Effetti sulle entità derivate

Quando una fonte viene corretta, redatta, purgata o invalidata devono essere rivalutati:

```text
summaries
Context Package
verifications
reconstructions
baselines
projections
search indexes
exports
analisi IA
```

Possibili stati:

```text
STALE
VALID_WITH_LIMITATIONS
INVALID
INCOMPLETE_SOURCE
REGENERATION_REQUIRED
```

Nessun effetto deve essere silenzioso.

# 15. Progetto, repository e copie esterne

La cancellazione del progetto segue un workflow separato:

```text
request
→ freeze scritture
→ inventory
→ assessment
→ approval
→ purge per classi
→ tombstone globale
→ integrity verification
→ deletion certificate
```

La rimozione dal working tree non implica la rimozione dalla storia Git.

Stati distinti:

```text
FILE_REMOVED_FROM_CURRENT_TREE
GIT_HISTORY_STILL_CONTAINS_CONTENT
GIT_HISTORY_REWRITTEN
REMOTE_HISTORY_STATUS_UNKNOWN
```

Non si deve dichiarare una eliminazione completa quando copie esterne o backup non sono verificabili.

# 16. Operazioni distruttive

Ogni operazione materiale richiede:

```text
scope esatto
manifest di UUID, versioni e hash
preview
dipendenze
policy
approvazione
idempotency key
journal delle azioni
condizioni di stop
recovery
integrity check finale
```

Esiti:

```text
COMPLETED
COMPLETED_WITH_WARNINGS
PARTIALLY_COMPLETED
FAILED
```

Un esito parziale non viene dichiarato completato.

# 17. Regole vincolanti

```text
Archiviazione, ritiro, annullamento, sostituzione,
rettifica, redazione e cancellazione sono distinti.

Le entità governate e congelate non vengono
hard-deleted nel normale workflow.

Le rettifiche producono nuovi record o versioni.

Gli eventi append-only non vengono modificati.

Gli hard delete sono limitati a draft mai utilizzati.

Ogni operazione distruttiva usa policy,
assessment, manifest, approvazione ed eventi.

Le cancellazioni complesse sono journaled e idempotenti.

Un purge conserva un tombstone quando necessario.

I reference_code non vengono riciclati.

Le fonti purgate propagano limitazioni
alle verifiche e ricostruzioni dipendenti.

La redazione resta sempre visibile come operazione.

La chiusura di una entità non equivale alla cancellazione.
```

# 18. Decisione approvata

```text
DEC-0101-016 — APPROVED

Project Integrity OS distingue archive, withdraw, void,
supersede, correct, redact, purge content, hard delete,
restore e tombstone.

Le entità sono soggette a policy di conservazione
versionate e differenziate.

Record governati, frozen, approvati o usati non vengono
hard-deleted nel normale workflow.

Le operazioni distruttive significative richiedono
manifest, assessment, autorizzazione, journal, eventi
e verifica finale.

Rettifiche e annullamenti non riscrivono lo storico.

Redazione e purge conservano metadati, hash
e tombstone quando necessario.

Gli effetti sulle entità derivate vengono propagati
e resi visibili.
```
