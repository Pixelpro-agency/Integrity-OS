# Project Integrity OS

## Context Package — specifica concettuale v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole
**Data:** 2026-08-05
**Ambito:** selezione, congelamento, consegna e riproduzione del contesto
**Origine:** analisi preliminare di `TODO-0101`
**Decisione collegata:** `DEC-0101-008`

---

# 1. Problema

Project Integrity OS deve conservare l’intero contesto del progetto, ma non deve consegnarlo integralmente a ogni IA, persona o verificatore.

Un esecutore deve ricevere:

- ciò che gli serve;
- la versione corretta;
- lo scope pertinente;
- le decisioni applicabili;
- le condizioni di stop;
- i criteri da soddisfare.

Il sistema deve inoltre poter ricostruire esattamente:

- cosa è stato consegnato;
- a chi;
- quando;
- per quale attività;
- da quali fonti;
- con quali esclusioni;
- con quale hash.

---

# 2. Principio

Un Context Package è un’entità persistente, versionata, validabile e congelabile.

Non è:

- una ricerca temporanea;
- un prompt libero;
- un elenco dinamico di file;
- una copia indiscriminata dell’intero progetto.

È un manifest riproducibile del contesto consegnato.

---

# 3. Entità

```text
context_packages
context_package_items
context_package_exclusions
```

Potranno essere aggiunte in seguito entità per:

- policy di selezione;
- delivery;
- redaction;
- validation result;
- summary.

---

# 4. `context_packages`

Campi concettuali:

```text
context_package_id
project_id
reference_code
package_type
purpose
target_role
target_executor_type
root_entity_type
root_entity_id
source_baseline_id
generation_policy_version
selection_query_json
status
content_hash
estimated_tokens
estimated_bytes
redaction_profile
created_by
created_at
validated_at
frozen_at
delivered_at
supersedes_context_package_id
```

## 4.1 Entità radice

Ogni pacchetto parte da un oggetto preciso:

```text
PROJECT
PHASE
WORK_ITEM
TASK
TASK_EXECUTION
ATTEMPT
VERIFICATION
VALIDATION
BUG
DECISION
```

Non deve esistere un pacchetto generico privo di finalità.

---

# 5. `context_package_items`

Campi concettuali:

```text
context_package_item_id
project_id
context_package_id
source_entity_type
source_entity_id
source_version_id
source_reference_code
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
summary_id
sensitivity_level
redaction_applied
created_at
```

Ogni elemento incluso deve essere identificabile e verificabile.

---

# 6. Modalità di inclusione

```text
FULL
EXCERPT
SUMMARY
REFERENCE_ONLY
METADATA_ONLY
```

## 6.1 `FULL`

Contenuto integrale della versione.

Uso tipico:

- Task Contract;
- brief;
- prompt;
- criteri di accettazione;
- decisioni direttamente vincolanti.

## 6.2 `EXCERPT`

Estratto preciso.

Deve registrare:

- documento;
- versione;
- hash;
- sezione;
- intervallo o locator;
- testo estratto.

## 6.3 `SUMMARY`

Sintesi congelata e tracciabile.

Deve indicare:

- fonti;
- versioni;
- hash;
- copertura;
- esclusioni;
- stato di aggiornamento.

## 6.4 `REFERENCE_ONLY`

L’elemento viene segnalato senza consegnarne il contenuto.

## 6.5 `METADATA_ONLY`

Vengono consegnati soltanto dati strutturati come stato, versione, gravità o dipendenza.

---

# 7. Livelli di contesto

```text
CORE
SUPPORTING
DEEP_REFERENCE
```

## 7.1 `CORE`

Materiale da leggere immediatamente.

Deve contenere tutto ciò che è obbligatorio per l’attività.

## 7.2 `SUPPORTING`

Materiale pertinente consultabile durante il lavoro.

## 7.3 `DEEP_REFERENCE`

Fonti storiche, complete o dettagliate raggiungibili senza appesantire il contesto iniziale.

---

# 8. Tipi di pacchetto

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
```

## 8.1 `GOVERNANCE`

Per amministrazione e pianificazione.

Include:

- stato macroscopico;
- fase;
- work item;
- dipendenze;
- decisioni aperte;
- rischi;
- prossime azioni.

## 8.2 `ANALYSIS`

Per preparare analisi e brief.

Include:

- problema;
- fonti autorevoli;
- decisioni;
- ambiguità;
- dipendenze;
- domande aperte.

## 8.3 `EXECUTION`

Per l’esecutore.

Include:

- task;
- contratto;
- scope;
- requisiti;
- criteri;
- test;
- condizioni di stop;
- formato report.

## 8.4 `VERIFICATION`

Per il verificatore.

Include:

- contratto;
- prompt;
- report;
- snapshot;
- evidenze;
- command run;
- test run;
- criteri;
- eccezioni.

## 8.5 `VALIDATION`

Per il collaudo umano.

Include:

- funzione;
- ambiente;
- procedura;
- atteso;
- rischi;
- problemi noti.

## 8.6 `APPROVAL`

Per la decisione finale.

Include:

- verifiche;
- collaudi;
- eccezioni;
- bug;
- rischi residui;
- baseline;
- commit.

## 8.7 `DIAGNOSTIC`

Per analizzare fallimenti.

Include:

- attempt;
- errori;
- log;
- comandi;
- modifiche residue;
- finding;
- contesto tecnico pertinente.

## 8.8 `REOPENING`

Per riprendere il lavoro dopo tempo.

Include:

- stato corrente;
- baseline;
- decisioni vigenti;
- task aperte;
- bug bloccanti;
- documenti correnti;
- ultimo evento;
- prossima azione consentita.

## 8.9 `EXPORT`

Per produrre un pacchetto completo o parziale portabile.

---

# 9. Stati

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

## 9.1 `DRAFT`

La selezione può cambiare.

## 9.2 `VALIDATING`

Sono in corso controlli di completezza, permessi e coerenza.

## 9.3 `VALID`

I requisiti minimi risultano soddisfatti.

## 9.4 `FROZEN`

Manifest e contenuti diventano immutabili.

Viene calcolato l’hash finale.

## 9.5 `DELIVERED`

Il pacchetto è stato consegnato.

Devono essere registrati:

- destinatario;
- canale;
- timestamp;
- sessione o attempt;
- hash consegnato.

## 9.6 `STALE`

Una fonte corrente è cambiata.

Il pacchetto resta valido come prova storica, ma non deve essere riutilizzato automaticamente.

## 9.7 `SUPERSEDED`

Un nuovo pacchetto lo sostituisce.

## 9.8 `REVOKED`

Il pacchetto non può essere usato.

La revoca non lo cancella.

---

# 10. Selezione

La selezione primaria deve essere deterministica.

Ordine proposto:

```text
1. elementi obbligatori per tipo di pacchetto;
2. collegamenti strutturali diretti;
3. dipendenze dichiarate;
4. decisioni vigenti applicabili;
5. requisiti e criteri collegati;
6. bug, rischi e finding bloccanti;
7. fonti esplicitamente richieste;
8. ricerca per identificatori e categorie governate;
9. ricerca semantica come proposta aggiuntiva;
10. validazione finale.
```

L’IA può proporre integrazioni.

L’IA non può rimuovere fonti obbligatorie senza registrazione.

---

# 11. Priorità

```text
MANDATORY
HIGH
NORMAL
LOW
REFERENCE
```

In caso di limite:

1. `MANDATORY` non viene rimosso;
2. `HIGH` viene preservato;
3. `FULL` può diventare `EXCERPT`;
4. `NORMAL` può diventare `SUMMARY`;
5. `LOW` può diventare `REFERENCE_ONLY`;
6. ogni riduzione viene registrata.

Non sono ammesse omissioni silenziose.

---

# 12. Esclusioni

Ogni esclusione deve registrare:

```text
source_entity_type
source_entity_id
exclusion_reason
excluded_by_policy
excluded_by_actor
impact_assessment
created_at
```

Motivazioni iniziali:

```text
NOT_RELEVANT
OUT_OF_SCOPE
SUPERSEDED
DUPLICATE
SENSITIVE
TOKEN_LIMIT
ROLE_RESTRICTED
HISTORICAL_ONLY
MANUALLY_EXCLUDED
```

Un elemento obbligatorio non può essere escluso senza blocco o eccezione umana.

---

# 13. Completezza

Esiti proposti:

```text
COMPLETE
INCOMPLETE
CONFLICTING
STALE_SOURCE
UNAUTHORIZED_CONTENT
```

Controlli:

- presenza della task;
- contratto corretto;
- decisioni vincolanti;
- criteri di accettazione;
- test richiesti;
- bug bloccanti;
- baseline corretta;
- fonti autorevoli;
- sintesi aggiornate;
- conflitti;
- redazioni;
- isolamento del progetto.

Un pacchetto incompleto non può diventare `FROZEN` per un tentativo senza eccezione esplicita.

---

# 14. Immutabilità e riproduzione

Un Context Package `FROZEN` non viene aggiornato.

Esempio:

```text
ATTEMPT-0001
→ PACKAGE-0001
```

Se cambia una decisione:

```text
PACKAGE-0001 → STALE per usi futuri
PACKAGE-0002 → nuovo pacchetto
PACKAGE-0002 supersedes PACKAGE-0001
```

`PACKAGE-0001` resta la prova di ciò che fu consegnato.

---

# 15. Sicurezza e redazione

Ogni pacchetto deve supportare:

- classificazione della sensibilità;
- profilo di redazione;
- esclusione di segreti;
- esclusione di dati personali non necessari;
- autorizzazione per ruolo;
- registrazione delle riduzioni.

Il contenuto originale resta protetto nel sistema.

Il destinatario riceve soltanto ciò che è autorizzato.

---

# 16. Esempio

```text
PACKAGE-EXEC-0001
type: EXECUTION
root: TASK-0102-03
target: technical_executor
```

## CORE

```text
TASK-0102-03
CONTRACT-0102-03-v1
PROMPT-0102-03-v1
AC-0001 ... AC-0006
TEST-0001 ... TEST-0004
DECISION-0001
DECISION-0002
```

## SUPPORTING

```text
Schema dati minimo — estratto pertinente
Convenzioni tecniche — sezioni migrazioni e test
Baseline repository
Bug bloccanti
```

## DEEP_REFERENCE

```text
Specifiche FROZEN complete
Analisi storiche
Decisioni indirette
Esecuzioni correlate
```

---

# 17. Decisione approvata

```text
DEC-0101-008

Project Integrity OS introduce Context Package persistenti,
versionati, validabili e congelabili.

Ogni pacchetto possiede scopo, destinatario, entità radice,
tipo, policy, manifest, versioni e hash delle fonti,
modalità di inclusione, esclusioni, controllo di completezza
e hash finale.

I livelli sono CORE, SUPPORTING e DEEP_REFERENCE.

Un pacchetto FROZEN è immutabile.

La selezione primaria è deterministica.
L’IA può proporre integrazioni, ma non può rimuovere
silenziosamente fonti obbligatorie.
```

---

# 18. Aspetti ancora da decidere

- schema definitivo delle policy;
- ruoli e permessi;
- livelli di sensibilità;
- redaction profile;
- token budget;
- algoritmo di stima;
- formato degli excerpt locator;
- lifecycle delle summary;
- delivery channels;
- criteri esatti di revoca;
- implementazione nella To-Do.
