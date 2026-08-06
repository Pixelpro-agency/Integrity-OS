# Project Integrity OS

## Principi di tracciabilità e gestione del contesto — v0.2

**Stato:** DRAFT — modello consolidato, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task:** `TODO-0101 — Definire schema dati minimo`  
**Decisioni:** `DEC-0101-003`, `DEC-0101-004`, `DEC-0101-005`, `DEC-0101-007`, `DEC-0101-008`, `DEC-0101-009`, `DEC-0101-010`, `DEC-0101-015`  
**Correzioni:** `C-0101-003` → `C-0101-009`  
**Sostituisce:** `Project_Integrity_OS_01_Principi_Tracciabilita_Contesto_TODO-0101_v0_1_DRAFT.md`

---

# 1. Scopo

Project Integrity OS deve impedire che la conoscenza necessaria a governare un progetto rimanga affidata:

- alla memoria di una chat o di una persona;
- a documenti monolitici e non versionati;
- a relazioni implicite;
- a dichiarazioni trattate come fatti;
- alla posizione corrente di un file;
- alla disponibilità di uno specifico modello IA;
- a operazioni che non lasciano storico verificabile.

Principio guida:

> Dal satellite al granello di sabbia, ogni elemento rilevante deve essere identificabile, versionabile, collegabile, verificabile e recuperabile.

La completezza non richiede di mostrare tutto contemporaneamente. Richiede di preservare tutto ciò che è materialmente rilevante e di distribuire soltanto il contesto autorizzato e necessario.

---

# 2. Catena completa

La catena canonica è:

```text
analisi
→ decisione
→ documentazione
→ fase
→ work item
→ task
→ Task Contract
→ task execution
→ attempt
→ prompt
→ report
→ command run e test run
→ evidence
→ reconciliation
→ verification
→ validation
→ approval
→ closure
→ baseline successiva
```

Ogni passaggio materiale deve essere rappresentato da entità o relazioni esplicite.

Da qualunque nodo deve essere possibile:

1. risalire alle fonti;
2. individuare la decisione che lo governa;
3. conoscere la versione utilizzata;
4. vedere attività, risultati ed evidenze;
5. distinguere dichiarato, osservato, derivato e verificato;
6. ricostruire stato corrente e storico;
7. identificare eccezioni, limiti e blocker.

---

# 3. Gerarchia primaria

```text
PROJECT
└── PHASE
    └── WORK_ITEM
        └── TASK
            └── TASK_EXECUTION
                └── ATTEMPT
```

I livelli non sono sinonimi.

Il completamento di un livello inferiore non completa automaticamente quello superiore.

Le cardinalità strutturali ammettono la creazione progressiva:

```text
PROJECT        1 ── 0..N PHASES
PHASE          1 ── 0..N WORK_ITEMS
WORK_ITEM      1 ── 0..N TASKS
TASK           1 ── 0..N TASK_EXECUTIONS
TASK_EXECUTION 1 ── 0..N ATTEMPTS
```

I minimi richiesti da uno stato o da una transizione appartengono al Transition Engine, non alla cardinalità strutturale.

---

# 4. Identità

Le entità persistenti usano UUID espliciti.

Le entità citabili usano anche un `reference_code` stabile e leggibile.

```text
UUID tecnico
+
reference_code di dominio
```

Regole:

- le foreign key usano UUID;
- il `reference_code` non è riciclato;
- per le entità project-local è univoco nel progetto;
- per le entità globali la regola di unicità è definita dal relativo catalogo;
- nessun modello dipende da SQLite `rowid`.

---

# 5. Catalogo universale e confini

Ogni entità citabile project-local possiede una riga in:

```text
project_entities
```

Ogni versione citabile project-local possiede una riga in:

```text
entity_versions
```

Eccezioni esplicite:

- system catalog;
- global project registry;
- actors, identities e sessioni globali;
- fonti esterne non importate come entità di progetto.

Questi elementi non usano `project_id NULL` per simulare un doppio significato. Appartengono a un perimetro distinto e vengono riferiti tramite codici stabili, versioni e hash o tramite binding locali.

---

# 6. Documentazione come dato di prima classe

Sono entità persistenti almeno:

- analisi;
- decisioni e relative versioni;
- documenti e versioni;
- obiettivi;
- requisiti e versioni;
- criteri di accettazione e versioni;
- test definition e versioni;
- report e versioni;
- summary e versioni;
- Context Package e versioni;
- baseline e versioni;
- policy e definizioni versionate.

Il Markdown è una rappresentazione leggibile e versionabile nel repository.

Il database conserva identità, stato, versione, hash, provenienza e relazioni.

Una versione usata da decisioni, attempt, verifiche, approvazioni o baseline non viene sovrascritta.

---

# 7. Provenienza multidimensionale

La provenienza non usa un unico enum.

Ogni informazione materiale può registrare:

```text
information_kind
acquisition_method
actor_type
verification_status
governance_status
confidence_level
sources
inputs
timestamps
hash
```

Nature iniziali:

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

Metodi di acquisizione iniziali:

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

Un dato importato o generato non è automaticamente verificato.

---

# 8. Fonte primaria, derivati e sintesi

La fonte originale conserva la verità storica osservata.

Excerpt, estrazioni, summary, rollup e current-state snapshot sono artefatti derivati e versionati.

Ogni derivato conserva:

- fonti e versioni esatte;
- hash delle fonti;
- scopo;
- copertura;
- esclusioni;
- periodo temporale;
- freshness;
- validity;
- metodo di generazione;
- drill-down verso le fonti.

Una fonte modificata non aggiorna retroattivamente il derivato.

---

# 9. Context Package

Il Context Package è:

```text
persistente
versionato
validabile
congelabile
riproducibile
autorizzato
```

Livelli:

```text
CORE
SUPPORTING
DEEP_REFERENCE
```

Modalità di inclusione:

```text
FULL
EXCERPT
SUMMARY
REFERENCE_ONLY
METADATA_ONLY
```

Un package frozen è immutabile.

La selezione primaria è deterministica. L'IA può proporre integrazioni, ma non può rimuovere silenziosamente fonti obbligatorie.

---

# 10. Collegamenti e drill-down

Le relazioni fondamentali usano tabelle dedicate.

`entity_links` serve soltanto per relazioni supplementari e di navigazione.

Ogni sintesi e relazione deve consentire il percorso:

```text
sintesi
→ dettaglio strutturato
→ record o versione
→ fonte
→ evidence
→ provenance
```

Il sistema deve rilevare:

- orfani;
- relazioni cross-project;
- requisiti senza criteri;
- criteri senza test;
- verifiche senza evidence;
- report senza owner;
- Context Package con fonti irrisolvibili;
- baseline con item irrisolvibili;
- versioni frozen mutate;
- cataloghi globali trattati come entità locali.

---

# 11. Completezza prima delle transizioni

Nessuno stato governato viene modificato direttamente.

Esempi:

```text
TASK → READY
richiede Task Contract frozen,
scope, requisiti, criteri,
dipendenze e assenza di blocker applicabili

ATTEMPT → READY
richiede prompt frozen,
Context Package frozen,
snapshot e autorizzazione

VERIFICATION → PASSED
richiede criteri valutati,
evidence sufficiente,
reconciliation e integrità

TASK → COMPLETED
richiede verification,
validation e approval previste
```

Elementi mancanti producono blocco, warning governato o eccezione esplicita.

---

# 12. Immutabilità, correzione e cancellazione

Non vengono riscritti retroattivamente:

- eventi;
- versioni frozen;
- prompt frozen;
- report originali;
- evidence;
- command run e test run conclusi;
- approvazioni;
- baseline approvate;
- transition execution concluse.

Una correzione produce una nuova versione, un nuovo record o un nuovo evento collegato.

`ON DELETE RESTRICT` è il comportamento predefinito.

Hard delete è limitato a draft mai utilizzati e non referenziati.

---

# 13. Sicurezza e minimizzazione

Conservare tutto non significa distribuire tutto.

Il sistema applica:

```text
DEFAULT DENY
RBAC
scope gerarchico
policy conditions
classificazione
handling flags
separation of duties
redazione
```

Ogni Context Package, export e accesso sensibile conserva la decisione di autorizzazione.

La permission locale non implica automaticamente l'autorizzazione a inviare dati a un provider IA esterno.

---

# 14. Ricostruzione temporale

Il modello usa:

```text
stato corrente autorevole
+
event journal append-only
+
versioni immutabili
+
state snapshot
+
baseline
```

Viste temporali:

```text
AS_KNOWN_AT
AS_EFFECTIVE_AT
AS_BASELINED
```

L'ordine autorevole usa sequence number, non soltanto timestamp.

---

# 15. Decisione consolidata

```text
DEC-0101-003...010
DEC-0101-014...020
C-0101-003...009

Project Integrity OS conserva un grafo di contesto
governato, versionato, verificabile e ricostruibile.

Le entità project-local usano project_entities
ed entity_versions.

Cataloghi globali, global registry e actors globali
restano fuori dal database di progetto e vengono
riferiti tramite binding locali riproducibili.

Cardinalità strutturali e minimi di transizione
restano distinti.

Nessuna sintesi, dichiarazione o approvazione
sostituisce fonti, evidence e verifiche.
```
