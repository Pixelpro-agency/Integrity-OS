# Project Integrity OS

## Ruoli, permessi, sensibilità e redazione — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole
**Data:** 2026-08-06
**Task collegata:** `TODO-0101 — Definire schema dati minimo`
**Decisione collegata:** `DEC-0101-017 — APPROVED`

---

# 1. Principio

```text
conservare tutto nel sistema
≠ rendere tutto visibile a tutti
```

Il sistema deve distinguere:

```text
identità
ruolo
permesso
scope
ownership
sensibilità
redazione
approvazione
sessione
delega
```

# 2. Modello

```text
RBAC
+
scope gerarchico
+
condizioni di policy
+
classificazione dei dati
+
separation of duties
+
DEFAULT DENY
```

Il frontend non è autorità di sicurezza. Ogni comando backend deve rivalutare l’autorizzazione.

# 3. Entità concettuali

```text
actors
actor_identities
actor_sessions

roles
role_versions
permissions
role_permissions
actor_role_assignments
delegations

access_policies
access_policy_versions
access_decisions

approval_policies
approval_policy_versions
approval_requirements

classification_levels
handling_flags
entity_classifications
field_classifications
classification_changes

redaction_profiles
redaction_profile_versions
redaction_rules

security_access_events
break_glass_requests
```

# 4. Attori

Tipi iniziali:

```text
HUMAN
AI
SYSTEM
TOOL
EXTERNAL_SERVICE
MIGRATION_PROCESS
```

Le identità tecniche conservano provider, identificatore esterno, modello o tool, versione, riferimento protetto alla credenziale, stato, verifica e revoca. I segreti non vengono salvati direttamente.

# 5. Sessioni

Ogni sessione operativa può registrare:

```text
actor
identity
session type
inizio e scadenza
authentication strength
origin
client information
parent session
Context Package
delegation
```

Le sessioni IA devono mantenere provider, modello, versione, Context Package, tool autorizzati, scope e scadenza.

# 6. Ruoli

Ruoli iniziali:

```text
PROJECT_OWNER
PROJECT_ADMINISTRATOR
ARCHITECT
ANALYST
DOCUMENT_AUTHOR
EXECUTOR
VERIFIER
VALIDATOR
APPROVER
AUDITOR
SECURITY_OFFICER
READ_ONLY
SYSTEM_OPERATOR
```

I ruoli sono versionati e collegati a permessi atomici.

# 7. Permessi

Categorie principali.

## Lettura

```text
VIEW_METADATA
VIEW_CONTENT
VIEW_SENSITIVE_CONTENT
VIEW_HISTORY
VIEW_PROVENANCE
VIEW_EVIDENCE
VIEW_SECURITY_AUDIT
```

## Modifica

```text
CREATE_DRAFT
UPDATE_DRAFT
LINK_ENTITY
UNLINK_ENTITY
CREATE_VERSION
SUBMIT_FOR_REVIEW
```

## Governo

```text
FREEZE_VERSION
APPROVE_VERSION
REJECT_VERSION
MAKE_DECISION_EFFECTIVE
REVOKE_DECISION
CREATE_EXCEPTION
APPROVE_EXCEPTION
```

## Esecuzione

```text
START_TASK_EXECUTION
START_ATTEMPT
DELIVER_CONTEXT_PACKAGE
RUN_COMMAND
RUN_TEST
SUBMIT_REPORT
```

## Verifica

```text
RECONCILE
VERIFY
VALIDATE
CLOSE_FINDING
CLOSE_BUG
```

## Sicurezza

```text
CLASSIFY_CONTENT
DECLASSIFY_CONTENT
REDACT_CONTENT
VIEW_REDACTED_ORIGINAL
PURGE_CONTENT
HARD_DELETE
RESTORE_CONTENT
EXPORT_CONTENT
```

## Amministrazione

```text
ASSIGN_ROLE
REVOKE_ROLE
MANAGE_POLICY
MANAGE_RETENTION
MANAGE_SECURITY
RECOVER_PROJECT
DELETE_PROJECT
```

# 8. Assegnazioni e scope

Ogni assegnazione registra attore, ruolo e versione, progetto, scope, eventuale ereditarietà verso i discendenti, intervallo temporale, assegnatore, motivazione e stato.

Gerarchia primaria:

```text
PROJECT
→ PHASE
→ WORK_ITEM
→ TASK
→ TASK_EXECUTION
→ ATTEMPT
```

L’eredità verso il basso non è implicita per ogni ruolo.

# 9. Ownership

L’owner è responsabile dell’elemento, ma non ottiene automaticamente il diritto di:

- approvarsi;
- eliminare evidenze;
- modificare versioni frozen;
- chiudere finding critici;
- assegnarsi ruoli;
- disattivare policy.

# 10. Separation of duties

Livelli:

```text
NOT_REQUIRED
RECOMMENDED
REQUIRED
STRICT
```

Regole iniziali possibili:

```text
executor != verifier
verifier != final approver
deletion requester != deletion approver
role assignment requester != approver
exception requester != exception approver
```

Le eccezioni devono essere governate.

# 11. IA e deleghe

Una IA non può autonomamente:

```text
assegnarsi permessi
estendere lo scope
approvare la propria esecuzione
chiudere eccezioni critiche
disattivare integrity rule
ridurre classificazioni
cancellare prove
modificare versioni frozen
autorizzare purge
modificare policy di sicurezza
```

Le deleghe sono limitate, scadibili, revocabili, non trasferibili, legate alla sessione e verificabili.

# 12. Classificazione

Due dimensioni separate.

## Confidentiality level

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
```

## Handling flags

```text
PERSONAL_DATA
CREDENTIAL
SECURITY_SENSITIVE
LEGAL_HOLD
THIRD_PARTY_CONFIDENTIAL
EXPORT_RESTRICTED
DELETION_RESTRICTED
AUDIT_REQUIRED
```

La classificazione può essere applicata a entità, versione, singolo campo o locator.

# 13. Ereditarietà della sensibilità

Regola:

```text
un contenuto derivato eredita
la classificazione più alta
delle fonti materiali
```

Una classificazione può essere ridotta soltanto tramite redazione verificata, anonimizzazione, versione sanitizzata o declassificazione approvata.

Una sintesi non diventa meno sensibile perché è più corta.

# 14. Policy di accesso

Le policy devono considerare:

```text
actor type
ruolo
permesso
scope
classificazione
handling flags
stato dell’entità
separation of duties
integrità
scadenza
approvazioni preventive
```

Ordine di valutazione:

```text
identità
→ sessione
→ progetto
→ target
→ scope
→ ruolo e permesso
→ classificazione
→ handling restrictions
→ stato
→ separation of duties
→ integrità
→ deny espliciti
→ approvazioni
→ ALLOW o DENY
```

Regole:

```text
explicit deny prevale
la policy più restrittiva prevale
nessuna policy applicabile → DENY
```

# 15. Access decision

Esiti:

```text
ALLOW
ALLOW_WITH_REDACTION
ALLOW_WITH_CONDITIONS
DENY
REQUIRE_APPROVAL
```

Ogni decisione materiale conserva attore, sessione, azione, target, versione, policy, assegnazioni di ruolo, classificazione, redaction profile, motivazioni, timestamp e scadenza.

# 16. Audit

Devono essere sempre registrati:

```text
accessi RESTRICTED
visualizzazione credenziali
export
declassificazione
redazione
purge
hard delete
assegnazione ruoli
approvazioni
break-glass
modifiche policy
accessi amministrativi
```

Gli accessi ordinari possono essere regolati dalla policy per evitare rumore.

# 17. Redazione dinamica e derivati sanitizzati

## Dynamic view redaction

La fonte resta immutata e la risposta viene filtrata.

## Sanitized derivative

Viene creata una nuova versione derivata:

```text
fonte originale
→ versione sanitizzata
```

La nuova versione conserva fonti, locator, policy, hash, attore e verifica.

# 18. Redaction profiles

Profili iniziali possibili:

```text
AI_EXECUTION_PROFILE
EXTERNAL_EXPORT_PROFILE
AUDITOR_PROFILE
PUBLIC_REPORT_PROFILE
SUPPORT_DIAGNOSTIC_PROFILE
```

Azioni:

```text
ALLOW
MASK
REMOVE
REPLACE_WITH_MARKER
TOKENIZE
HASH_ONLY
METADATA_ONLY
REFERENCE_ONLY
DENY_ENTITY
```

# 19. Context Package e provider esterni

Prima del congelamento e della consegna devono essere verificati:

```text
destinatario
sessione
ruolo
scope
classificazione
provider
modello
policy
redaction profile
handling flags
restrizioni di export
hash finale
```

Un contenuto può essere incluso come:

```text
FULL
EXCERPT
SUMMARY
REFERENCE_ONLY
METADATA_ONLY
REDACTED
DENIED
```

Il permesso di leggere localmente non implica il permesso di inviare dati a un provider esterno.

# 20. Export e declassificazione

Ogni export governato conserva request, access decision, redaction profile, manifest, classificazione, hash, destinatario, scopo, timestamp ed evento.

Tipi:

```text
FULL_EXPORT
SANITIZED_EXPORT
METADATA_EXPORT
REFERENCE_EXPORT
```

La declassificazione richiede motivazione, trasformazioni, contenuto rimosso, rischio residuo, approvazione, verifica e data di efficacia.

# 21. Approval policies

Una policy può richiedere:

```text
uno o più approvatori
ruoli specifici
separazione dal richiedente
ordine sequenziale
approvazioni parallele
scadenza
quorum
```

Esempi:

```text
PURGE_RESTRICTED_CONTENT
→ Security Officer + Project Owner

TASK_COMPLETION_NORMAL
→ Verifier

TASK_COMPLETION_CRITICAL
→ Verifier + Approver
```

# 22. Break-glass

L’accesso straordinario richiede motivo, scope ristretto, durata breve, attore, autorizzazione, notifica, audit completo e post-review obbligatoria.

Non consente di cancellare audit, alterare eventi o riscrivere versioni frozen.

# 23. MVP

Configurazione iniziale raccomandata:

```text
un actor umano locale
ruolo PROJECT_OWNER
actor separati per IA e tool
sessioni tracciate
deleghe limitate
classificazione INTERNAL di default
DEFAULT DENY per azioni critiche
```

Lo schema resta compatibile con uso multiutente.

# 24. Regole vincolanti

```text
Identità, ruolo, permesso, scope, ownership,
classificazione e approvazione sono distinti.

Il modello usa DEFAULT DENY.

I permessi sono atomici e governati.

Le assegnazioni hanno scope e scadenza.

Ownership non concede privilegi automatici.

Le IA non estendono autonomamente ruoli o scope.

Le azioni critiche rispettano separation of duties.

Le classificazioni si applicano a entità,
versioni e campi.

I derivati ereditano la classificazione più alta.

La declassificazione richiede approvazione.

La redazione non modifica l’originale.

Context Package ed export applicano policy e redazione.

Il backend rivaluta sempre le autorizzazioni.

Gli accessi sensibili producono audit ed eventi.
```

# 25. Decisione approvata

```text
DEC-0101-017 — APPROVED

Project Integrity OS usa RBAC, scope gerarchico,
condizioni di policy, classificazione e separation of duties.

Il default è DENY.

Attori, identità, sessioni, ruoli, permessi,
assegnazioni, deleghe e access decisions sono distinti.

La sensibilità usa livelli PUBLIC, INTERNAL,
CONFIDENTIAL e RESTRICTED, più handling flags.

Le IA operano tramite sessioni e deleghe limitate.

Context Package, export e provider esterni applicano
policy e redaction profile prima della consegna.

Il backend è l’autorità finale dell’accesso.
```
