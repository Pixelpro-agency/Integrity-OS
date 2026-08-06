# Project Integrity OS

## Provenienza e classificazione delle informazioni — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task collegata:** `TODO-0101 — Definire schema dati minimo`  
**Decisione collegata:** `DEC-0101-009 — APPROVED`  
**Ambito:** origine, natura, acquisizione, verifica, governo e catena di derivazione delle informazioni

---

# 1. Scopo

Project Integrity OS deve impedire che dichiarazioni, osservazioni, risultati calcolati, inferenze, decisioni e approvazioni vengano trattati come informazioni equivalenti.

Una frase come:

```text
“Il test è passato”
```

può rappresentare:

- una dichiarazione dell’esecutore;
- un campo estratto da un report;
- un fatto osservato da un command run;
- una derivazione prodotta dall’exit code;
- un’inferenza di un’IA;
- un risultato riconciliato;
- una verifica;
- un’approvazione umana.

Ogni passaggio deve essere conservato separatamente e collegato agli altri.

---

# 2. Decisione fondamentale

Non deve essere usato un unico enum che mescola:

- natura dell’informazione;
- metodo di acquisizione;
- identità dell’attore;
- stato di verifica;
- stato di governo;
- attendibilità;
- provenienza tecnica.

La provenienza è multidimensionale.

Ogni informazione rilevante deve poter registrare:

```text
natura informativa
+
metodo di acquisizione
+
attore
+
fonte
+
stato di verifica
+
stato di governo
+
confidenza quando applicabile
+
catena di derivazione
```

---

# 3. Natura informativa

Vocabolario minimo:

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

## 3.1 `SOURCE_ARTIFACT`

Materiale originale acquisito.

Esempi:

- report originale;
- documento;
- file;
- screenshot;
- output;
- log;
- archivio;
- risposta di un servizio esterno.

## 3.2 `DECLARATION`

Affermazione prodotta da un attore.

Esempi:

- “ho modificato tre file”;
- “il test è passato”;
- “il push è stato completato”.

Una dichiarazione non è automaticamente verificata.

## 3.3 `OBSERVATION`

Fatto registrato direttamente tramite un’osservazione.

Esempi:

- exit code osservato;
- file presente;
- commit rilevato;
- hash calcolato;
- working tree osservato.

Ogni osservazione deve indicare:

- strumento;
- scope;
- timestamp;
- output;
- ambiente o contesto.

## 3.4 `DERIVATION`

Risultato prodotto deterministicamente da input e regola.

Esempio:

```text
exit_code = 0
→ status = PASSED
```

Ogni derivazione deve registrare:

- input;
- regola;
- versione della regola;
- metodo;
- risultato;
- timestamp.

## 3.5 `INFERENCE`

Conclusione ragionata ma non direttamente dimostrata.

Esempio:

```text
Il fallimento potrebbe derivare da una foreign key non attivata.
```

Un’inferenza deve restare distinguibile da un fatto e deve indicare:

- fonti;
- metodo;
- attore;
- livello di confidenza;
- incertezza;
- verifiche ancora necessarie.

## 3.6 `DECISION`

Scelta di governo.

Esempi:

- adottare un modello dati;
- bloccare una task;
- accettare un rischio;
- sostituire una baseline.

## 3.7 `APPROVAL`

Atto formale con cui un attore autorizzato approva:

- documento;
- decisione;
- verifica;
- deroga;
- collaudo;
- chiusura.

L’approvazione non sostituisce la verifica tecnica.

## 3.8 `SUMMARY`

Vista ridotta e derivata da una o più fonti.

La sintesi non sostituisce le fonti originarie.

---

# 4. Metodo di acquisizione

Vocabolario iniziale:

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

Il metodo descrive come l’informazione entra nel sistema.

Non ne determina la correttezza.

Esempi:

```text
Report incollato
→ PASTED_TEXT

Output del Controlled Process Runner
→ TOOL_EXECUTION

Documento letto dalla repository
→ REPOSITORY_READ

Risultato del Reconciliation Engine
→ SYSTEM_CALCULATION

Sintesi prodotta da un modello
→ AI_GENERATION
```

---

# 5. Tipo di attore

Vocabolario minimo:

```text
HUMAN
AI
SYSTEM
TOOL
EXTERNAL_SERVICE
MIGRATION_PROCESS
UNKNOWN
```

Quando applicabile devono essere registrati:

```text
actor_id
actor_reference
provider
model_or_tool
version
session_id
```

L’origine `AI` non è sufficiente da sola.

Devono essere conservati anche:

- modello;
- provider;
- sessione;
- Context Package;
- fonti;
- stato di verifica;
- eventuale approvazione umana.

---

# 6. Stato di verifica

Vocabolario iniziale:

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

## Regole

- `UNVERIFIED`: registrato ma non controllato;
- `PARTIALLY_VERIFIED`: controllo incompleto;
- `VERIFIED`: verificato secondo scope e procedura definiti;
- `RECONCILED`: confrontato con altre fonti e coerente;
- `CONFLICTING`: incompatibile con una o più fonti;
- `DISPUTED`: contestato formalmente;
- `NOT_VERIFIABLE`: non controllabile con le fonti disponibili;
- `STALE`: non più aggiornato rispetto al contesto;
- `REJECTED`: rifiutato per lo scopo corrente.

Il sistema non deve scegliere silenziosamente tra fonti in conflitto.

---

# 7. Stato di governo

Vocabolario iniziale:

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

Lo stato di governo è distinto dallo stato di verifica.

Esempio:

```text
una deroga APPROVED
può riferirsi a una verifica FAILED
```

L’approvazione governa l’eccezione, non trasforma il fallimento in successo.

---

# 8. Confidenza

La confidenza viene usata solo per:

- inferenze;
- classificazioni probabilistiche;
- associazioni non deterministiche;
- analisi IA;
- risultati con incertezza reale.

Campi concettuali:

```text
confidence_level
confidence_score
confidence_basis
uncertainty_notes
```

Vocabolario iniziale:

```text
LOW
MEDIUM
HIGH
NOT_APPLICABLE
```

Non deve essere inventata una precisione numerica non supportata.

Per un exit code osservato:

```text
confidence_level = NOT_APPLICABLE
```

---

# 9. Provenance Envelope

Ogni informazione importante deve poter essere accompagnata da una struttura equivalente a:

```json
{
  "information_kind": "DECLARATION",
  "acquisition_method": "FILE_IMPORT",
  "actor_type": "AI",
  "verification_status": "UNVERIFIED",
  "governance_status": "NONE",
  "confidence_level": "NOT_APPLICABLE",
  "source_entity_type": "REPORT",
  "source_entity_id": "...",
  "source_version_id": "...",
  "source_locator": {
    "json_path": "$.tests[0].status"
  },
  "recorded_at": "...",
  "content_hash": "..."
}
```

Il record descrive:

> una dichiarazione estratta da un report importato, non ancora verificata.

---

# 10. Entità concettuali

```text
provenance_records
provenance_inputs
```

## 10.1 `provenance_records`

Campi concettuali:

```text
provenance_record_id
project_id
target_entity_type
target_entity_id
target_field_path
information_kind
acquisition_method
actor_type
actor_id
source_entity_type
source_entity_id
source_version_id
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
superseded_by_provenance_id
created_at
```

## 10.2 `provenance_inputs`

Collega una derivazione o inferenza ai suoi input.

Campi:

```text
provenance_record_id
input_provenance_record_id
input_role
sequence_number
created_at
```

Esempio:

```text
EVIDENCE-001
+
EVIDENCE-002
+
RULE-V3
→ RECONCILIATION-001
```

---

# 11. Provenienza a livello di record e campo

La provenienza deve poter riguardare:

- l’intera entità;
- un singolo campo;
- una specifica affermazione;
- un estratto;
- un risultato strutturato.

Campi:

```text
target_entity_type
target_entity_id
target_field_path
```

Esempio:

```text
target_entity_type: REPORT
target_field_path: $.version_control.commit.sha
```

Questo permette di distinguere nello stesso report:

- testo originale;
- campi dichiarati;
- campi estratti;
- campi normalizzati;
- correzioni;
- dati aggiunti manualmente.

---

# 12. Catena esempio: test

```text
Report originale
→ SOURCE_ARTIFACT

“TEST-001 PASSED”
→ DECLARATION

Test realmente eseguito
→ OBSERVATION

exit_code = 0 → PASSED
→ DERIVATION

dichiarato PASSED + osservato PASSED
→ RECONCILIATION MATCH

criterio soddisfatto
→ VERIFICATION PASSED

chiusura autorizzata
→ APPROVAL
```

Nessun passaggio sovrascrive il precedente.

---

# 13. Correzioni e conflitti

Una correzione produce un nuovo record.

Esempio:

```text
DECLARATION-001
commit_sha = abc123

DECLARATION-002
commit_sha = def456
supersedes DECLARATION-001
```

Devono restare disponibili:

- valore precedente;
- valore corretto;
- autore della correzione;
- motivo;
- fonte;
- verifiche che avevano usato il valore errato.

Quando due fonti confliggono:

```text
Report: push = true
Remoto: commit assente
```

il sistema conserva entrambe e produce:

```text
reconciliation = MISMATCH
verification_status = CONFLICTING
```

---

# 14. Regole vincolanti

```text
Un dato importato non è automaticamente verificato.

Un contenuto generato non è automaticamente corretto.

Una dichiarazione non è una osservazione.

Una osservazione deve indicare strumento, scope e timestamp.

Una derivazione deve indicare input, regola e versione.

Una inferenza deve indicare fonti, metodo e incertezza.

Una approvazione non trasforma un fallimento tecnico in successo.

Una fonte in conflitto non viene cancellata.

Una correzione produce un nuovo record collegato.

Ogni contenuto usato in una verifica deve avere
provenienza risolvibile.

Le relazioni di provenienza devono rispettare project_id.
```

---

# 15. Decisione approvata

```text
DEC-0101-009 — APPROVED

Project Integrity OS adotta una classificazione
multidimensionale della provenienza.

Ogni informazione rilevante registra natura, acquisizione,
attore, fonte, verifica, governo, confidenza quando applicabile,
timestamp, hash e catena degli input.

Dichiarazioni, osservazioni, derivazioni, inferenze,
decisioni, approvazioni, sintesi e fonti originali
restano concetti distinti.

Le correzioni e i conflitti vengono conservati
senza riscrivere retroattivamente lo storico.
```

---

# 16. Aspetti da consolidare successivamente

- tipi definitivi degli actor;
- locator canonici;
- vocabolari finali;
- cardinalità;
- policy di retention;
- indicizzazione;
- rappresentazione SQL;
- integrazione con eventi e verifiche;
- regole di importazione da fonti esterne.
