# Project Integrity OS

## Piano TODO di correzione documentale riallineato al refactor concluso — v0.6

**Report ID:** `RPT-DOC-AUDIT-PLAN-0006`  
**Data:** `2026-08-07T02:33:00+02:00`  
**Aggiornato:** `2026-08-07T03:16:00+02:00`  
**Repository:** `Pixelpro-agency/Integrity-OS`  
**Branch locale:** `review/documentation-audit-20260806`  
**Stato:** `COMPLETED_OPERATIONAL_SCOPE`  
**Sostituisce:** `RPT-DOC-AUDIT-PLAN-0005` / v0.5

> La v0.5 resta una fotografia storica del piano precedente e non viene riscritta retroattivamente.  
> La v0.6 recepisce le decisioni realmente adottate durante il refactor documentale concluso.

---

# 1. Stato autorevole del refactor documentale

- [x] Piano modifiche documentazione v0.4: `COMPLETED`
- [x] due cicli da 5 punti completati
- [x] `docs/README.md` adottato come indice umano principale
- [x] Document Registry v0.6/v0.7 eliminati
- [x] nessun Registry v0.8 creato
- [x] storico locale mantenuto nelle cartelle `90-history`
- [x] Audit corrente: v0.3 `FINAL`
- [x] Checkpoint TODO-0101 corrente: v0.12
- [x] Decision Log corrente: v0.9
- [x] FILE_MAP: 66 righe
- [x] manifest schema 2.1
- [x] MANIFEST_SHA256 verificato
- [x] link correnti non risolti: 0
- [x] SQLite non iniziata
- [x] TODO-0101 resta `IN_ANALYSIS`
- [x] TODO-0101 `READY`: NO

Tree finale verificato:

```text
Cartelle: 41
File: 147
Markdown: 113
Link Markdown esaminati: 189
Link correnti non risolti: 0
Link storici non risolti: 146
.original.txt: 0
```

---

# 2. Perché la v0.5 è superata

La v0.5 era costruita su una strategia successivamente sostituita:

- Document Registry v0.8;
- `docs/20-history/`;
- History Index;
- Project Timeline;
- Git come archivio storico quasi esclusivo;
- rimozione dal tree di molte versioni superseded;
- Prompt/Report Rule Catalog Lifecycle v0.2 come nuova baseline obbligatoria.

Il refactor effettivamente applicato ha invece scelto:

- `docs/README.md` come indice umano;
- `90-history` come storico locale;
- FILE_MAP + manifest + checksum per la tracciabilità;
- conservazione degli artefatti autentici;
- conservazione degli script `.sh`, `.py` e degli altri artefatti di esecuzione;
- Prompt/Report Rule Catalog Lifecycle v0.1 come baseline operativa MVP;
- nessuna riscrittura retroattiva degli snapshot storici;
- separazione netta fra correzione documentale e decisioni tecniche.

**Conclusione:** la v0.5 non deve più essere usata come piano operativo.

---

# 3. Decisioni documentali definitive

## [x] DEC-DOC-001 — Niente Document Registry v0.8

Registry v0.6 e v0.7 sono stati eliminati.

**Decisione:** non creare automaticamente un Registry v0.8.

**Sostituzione funzionale:** `docs/README.md`.

---

## [x] DEC-DOC-002 — Niente `docs/20-history` obbligatorio

La struttura finale usa cartelle `90-history` locali alle aree interessate.

**Decisione:** non creare `docs/20-history` come requisito della baseline corrente.

---

## [x] DEC-DOC-003 — Git non sostituisce lo storico locale

Git resta una garanzia di recupero.

**Decisione:** Git non è l’unico archivio storico autorevole e non giustifica la rimozione automatica degli snapshot conservati sotto `90-history`.

---

## [x] DEC-DOC-004 — Niente History Index / Project Timeline obbligatori

History Index e Project Timeline possono eventualmente essere progettati in futuro, ma non sono prerequisiti del refactor concluso.

**Decisione:** non crearli soltanto per soddisfare la vecchia v0.5.

---

## [x] DEC-DOC-005 — Prompt/Report Rule Catalog Lifecycle resta v0.1

File corrente:

`docs/00-current/Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md`

- [x] stato `ACTIVE — baseline operativa MVP`
- [x] task di origine `TODO-0003`
- [x] contenuto tecnico invariato

**Decisione:** non creare una v0.2 per inerzia del vecchio piano.

---

## [x] DEC-DOC-006 — Snapshot storici non riscritti

I 146 link storici non risolti sono ammessi e documentati.

**Regola:**

- documenti correnti → link relativi risolvibili;
- documenti storici → preservazione della struttura originaria, anche con link non più risolvibili.

---

## [x] DEC-DOC-007 — Artefatti di esecuzione conservati

Restano parte della tracciabilità:

- `.sh`;
- `.py`;
- `.json`;
- `.csv`;
- manifesti;
- report;
- file `DELETE_FILES.txt`;
- file di audit/verifica;
- template di tracciabilità.

---

## [x] DEC-DOC-008 — Tecnica e documentazione restano separate

Le decisioni su `PRIVATE_CHILD` e `CLOSURE_REPORT` sono temi architetturali.

**Decisione:** non applicarle come semplice correzione documentale.

---

# 4. Disposizione dei finding della v0.5

| Finding | Stato v0.6 | Decisione |
|---|---|---|
| `FND-001` | `RESOLVED_OR_OBSOLETE` | Il tree finale contiene artefatti non Markdown; resta solo un controllo opzionale contro il commit base. |
| `FND-002` | `RESOLVED` | Registry v0.6/v0.7 eliminati; niente Registry v0.8. |
| `FND-003` | `RESOLVED_BY_DIFFERENT_MODEL` | README task creati e struttura organizzata senza History Index/Timeline obbligatori. |
| `FND-004` | `CLOSED_AS_NON_BLOCKING_HISTORY` | Gli artefatti storici autentici non vengono riscritti solo per uniformare metadati. |
| `FND-005` | `RESOLVED` | Audit v0.1/v0.2 storici; Audit v0.3 FINAL corrente. |
| `FND-006` | `SPLIT` | Q-001/Q-002 superseded; Q-003/Q-004 trasferite al backlog architetturale. |

---

# 5. Disposizione delle ACT della v0.5

## Sicurezza / verifica

- [x] `ACT-001` → **KEEP_AS_GUARD**
  - resta solo la regola: nessuna operazione Git senza autorizzazione esplicita.

- [ ] `ACT-002` → **OPTIONAL_SAFETY_CHECK**
  - backup e quarantena possono essere verificati, ma non bloccano più la documentazione.

- [x] `ACT-003` → **REMOVE_FROM_ACTIVE_PLAN**
  - vecchio percorso e requisito `DOC-027` nel Registry non sono più applicabili.

- [x] `ACT-004` → **COMPLETED_OPTIONAL_VERIFY**
  - controllo facoltativo eseguito: il solo file non Markdown del commit base è stato ritrovato nel tree corrente con percorso/nome diverso e blob identico byte-per-byte.

## Registry / struttura

- [x] `ACT-005` → `SUPERSEDED`
- [x] `ACT-006` → `SUPERSEDED`
- [x] `ACT-007` → `SUPERSEDED`
- [x] `ACT-008` → `SUPERSEDED`

Motivo: non esiste più un Registry corrente da ricostruire.

- [x] `ACT-009` → `REMOVE_FROM_ACTIVE_PLAN`
- [x] `ACT-010` → `SUPERSEDED_BY_FINAL_STRUCTURE`
- [x] `ACT-011` → `COMPLETED_AS_IMPLEMENTED`
- [x] `ACT-012` → `SUPERSEDED`

Motivo: la struttura corrente è già consolidata tramite README, `90-history`, FILE_MAP e manifesti.

## Correzioni degli artefatti storici

- [x] `ACT-013` → `REMOVE_FROM_ACTIVE_PLAN`
- [x] `ACT-014` → `REMOVE_FROM_ACTIVE_PLAN`
- [x] `ACT-015` → `REMOVE_FROM_ACTIVE_PLAN`
- [x] `ACT-016` → `REMOVE_FROM_ACTIVE_PLAN`
- [x] `ACT-017` → `REMOVE_FROM_ACTIVE_PLAN`
- [x] `ACT-018` → `REMOVE_FROM_ACTIVE_PLAN`
- [x] `ACT-019` → `REMOVE_FROM_ACTIVE_PLAN`
- [x] `ACT-020` → `REMOVE_FROM_ACTIVE_PLAN`
- [x] `ACT-021` → `SUPERSEDED`
- [x] `ACT-022` → `SUPERSEDED`

Motivo: non riscrivere retroattivamente gli artefatti autentici e gli snapshot storici.

## Governance precedente

- [x] `ACT-023 / Q-001-D` → `SUPERSEDED`
  - Git non sostituisce lo storico locale.

- [x] `ACT-024 / Q-002-C` → `SUPERSEDED`
  - Prompt/Report v0.1 resta ACTIVE; niente v0.2 automatica.

## Temi architetturali

- [x] `ACT-025 / Q-003-C` → `RESOLVED_BY_EXISTING_DECISIONS`
  - `PRIVATE_CHILD` è già coperto dalle decisioni DEC-0101 esistenti; nessuna nuova DEC necessaria.

- [x] `ACT-026 / Q-004-C` → `REVIEW_COMPLETED_OPEN_ISSUE_REQUIRED`
  - gli owner canonici di `CLOSURE_REPORT` sono già decisi; resta da formalizzare governance/versionamento di `report_owner_policies` come open issue, non come nuova DEC.

Queste due voci non sono più correzioni documentali.

## Audit e gate

- [x] `ACT-027` → `COMPLETED_SUPERSEDED_BY_V0_3`
- [x] `ACT-028` → `COMPLETED_WITH_NEW_CRITERIA`
- [ ] `ACT-029` → `ACTIVE_FINAL_GATE`

---

# 6. Scope operativo residuo reale

Delle 29 ACT originarie restano soltanto quattro concetti utili.

## [x] GUARD-GIT-001 — Regola Git

- [x] Non eseguire commit, push, PR, merge o force-push senza autorizzazione esplicita dell’utente.

Questa è una regola di sicurezza, non una nuova task documentale.

---

## [x] VERIFY-BASE-001 — Controllo opzionale contro il commit base

Origine: `ACT-004`.

Scopo:

verificare che gli artefatti non Markdown del commit base siano rappresentati correttamente nel tree attuale.

Checklist:

- [x] inventariati i file non Markdown del commit base;
- [x] classificato il solo file base come apparentemente mancante nel vecchio percorso;
- [x] individuato il corrispondente file ricollocato nel tree corrente;
- [x] verificato blob Git identico: `0ee1ce669b5e067954d39928c128eebaba4a377c`;
- [x] verificato `IDENTICO_BYTE_PER_BYTE`;
- [x] nessun reintegro e nessuna sovrascrittura necessari.

**Stato:** `COMPLETED`  
**Blocking:** `NO`

Esito:

```text
File non Markdown nel commit base: 1
File realmente mancanti: 0
File differenti: 0
File ricollocati byte-identici: 1
File aggiunti successivamente: 34
Perdita di contenuto: NO
```

---

# 7. Backlog architetturale separato

## [x] ARCH-FOLLOWUP-001 — PRIVATE_CHILD

Origine: `ACT-025 / Q-003-C`.

Verifica conclusa:

- [x] `PRIVATE_CHILD` è già una classificazione canonica del modello;
- [x] la gerarchia stabilisce un solo parent autorevole per ogni figlio;
- [x] i child non citabili e puramente privati sono già distinti dalle project entity governate;
- [x] il cascade è ammesso soltanto per child privati, non governati e rigenerabili;
- [x] `CLOSURE_REPORT` non include `PRIVATE_CHILD` fra gli owner canonici;
- [x] nessuna nuova `DEC-0101-021` è necessaria per questo tema.

**Stato:** `RESOLVED_BY_EXISTING_DECISIONS`

Copertura principale: `DEC-0101-006`, `DEC-0101-015`, `DEC-0101-019`, `DEC-0101-020`.

Eventuale lavoro futuro: solo consolidamento editoriale della definizione, non nuova decisione architetturale.

---

## [x] ARCH-FOLLOWUP-002 — CLOSURE_REPORT allowlist

Origine: `ACT-026 / Q-004-C`.

Verifica conclusa:

- [x] owner canonici già definiti;
- [x] `CLOSURE_REPORT` limitato a `PROJECT / PHASE / WORK_ITEM / TASK / BASELINE`;
- [x] `report_owner_policies` definisce report type, allowed owner entity type e owner role;
- [x] ownership del report univoca;
- [x] owner type non modellati esclusi;
- [x] `PRIVATE_CHILD` escluso dalla allowlist corrente;
- [x] verificato il lifecycle delle decisioni prima di ipotizzare una nuova DEC;
- [x] stabilito che il gap residuo non riapre le decisioni già consolidate.

Gap residuo confermato:

- [ ] versionamento esplicito di `report_owner_policies`;
- [ ] stato e intervallo/entrata in vigore della policy;
- [ ] governance per l'estensione dei tipi owner;
- [ ] effetti obbligatori su cataloghi, vincoli, migrazioni e test.

**Stato:** `RESOLVED_AS_OPEN_ISSUE`

**Nuova DEC:** `NO`, salvo futuro conflitto dimostrato con le decisioni consolidate.

### Open issue registrato

- [x] `OI-0101-011 — Report owner policy governance and versioning`
- [x] registrato in `docs/planning/Project_Integrity_OS_Open_Issues_Data_Model_v0_1_DRAFT.md`
- [x] il registro resta v0.1 DRAFT e viene aggiornato in place;
- [x] nessun link corrente ha richiesto riallineamento perché filename e percorso del registro sono invariati;
- [x] l'issue non riapre `C-0101-002`, `C-0101-007` o le decisioni `DEC-0101-001` → `DEC-0101-020`.

Titolo: `Report owner policy governance and versioning`

Destinazione primaria:

- `Entity Catalog` — tipi owner canonici e classificazione;
- `Data Dictionary` — campi/versione/stato/validità della policy;
- `Constraint Catalog` — enforcement dell'allowlist e ownership valida;
- `Implementation Wave Matrix` — introduzione, migrazione e sequenza di enforcement.

Aspetti di DDL/migrazione fisica possono essere assegnati a `TODO-0102` dopo la chiusura e approvazione dei deliverable di `TODO-0101`.

**Nota:** il Decision Log usa ancora la formula più generica `CLOSURE_REPORT → entità chiusa`, mentre il documento di cardinalità specifica i cinque target ammessi. Il riallineamento va trattato nel lavoro architetturale, non come pulizia retroattiva indiscriminata.

---

# 7A. Ciclo operativo post-v0.6 — checkpoint 5/5

Regola operativa: fermarsi ogni 5 punti completati e aggiornare questo piano prima di proseguire.

- [x] **PUNTO 1/5 — VERIFY-BASE-001**: verifica non Markdown contro commit base completata; nessuna perdita di contenuto.
- [x] **PUNTO 2/5 — ARCH-FOLLOWUP-001 / PRIVATE_CHILD**: risolto tramite decisioni esistenti; nessuna nuova DEC.
- [x] **PUNTO 3/5 — ARCH-FOLLOWUP-002 / verifica copertura**: owner canonici e allowlist logica già presenti; gap di governance/versionamento confermato.
- [x] **PUNTO 4/5 — classificazione del gap CLOSURE_REPORT**: non creare una nuova DEC; trattare il residuo come open issue senza riaprire la report ownership consolidata.
- [x] **PUNTO 5/5 — destinazione del nuovo open issue**: risoluzione nei deliverable finali TODO-0101 (`Entity Catalog`, `Data Dictionary`, `Constraint Catalog`, `Implementation Wave Matrix`), con enforcement fisico eventualmente in TODO-0102.

**Checkpoint ciclo:** `COMPLETED_5_OF_5`

---

# 7B. Ciclo successivo — chiusura anticipata per esaurimento scope

- [x] **PUNTO 1/5 — registrazione OI-0101-011**: inserito formalmente nell'Open Issues Register v0.1 DRAFT.
- [x] verificata una sola occorrenza di `OI-0101-011`.
- [x] numerazione aggiornata: `# 12. OI-0101-011` e `# 13. Chiusura`.
- [x] nessuna nuova DEC creata.
- [x] nessun altro punto operativo residuo della v0.6.

**Checkpoint ciclo:** `COMPLETED_1_OF_5_SCOPE_EXHAUSTED`

La regola dei 5 punti resta valida, ma questo ciclo termina anticipatamente perché il piano v0.6 non contiene altri punti operativi residui. Non vengono inventate attività aggiuntive per raggiungere artificialmente 5/5.

---

# 8. Gate Git finale

## [x] GATE-DOC-001 — Autorizzazione operazione Git

Deriva da `ACT-029`, ma usa i criteri realmente adottati.

Criteri:

- [x] `docs/` contiene 41 cartelle
- [x] `docs/` contiene 147 file
- [x] Audit corrente: v0.3 FINAL
- [x] Checkpoint TODO-0101 corrente: v0.12
- [x] Decision Log corrente: v0.9
- [x] FILE_MAP rigenerato
- [x] manifest schema 2.1
- [x] MANIFEST_SHA256 verificato
- [x] link correnti non risolti: 0
- [x] link storici non risolti documentati
- [x] nessuna modifica tecnica involontaria alle 20 decisioni
- [x] Piano modifiche documentazione v0.4: COMPLETED
- [x] autorizzazione esplicita dell’utente alla fase Git manuale finale; il push sarà eseguito dall’utente sui comandi forniti

**Stato:** `AUTHORIZED_PENDING_FINAL_GIT_PRECHECK`

Il gate documentale è soddisfatto e l’utente ha autorizzato la fase Git manuale finale. Prima del push resta soltanto il controllo conclusivo dello stato del repository e dei file da includere.

---

# 9. Elementi da NON creare automaticamente

- [x] non creare `Project_Integrity_OS_Document_Registry_v0_8.md`
- [x] non creare `docs/20-history/` come requisito della baseline
- [x] non creare `Project_Integrity_OS_History_Index_v0_1.md` come prerequisito
- [x] non creare `Project_Integrity_OS_Project_Timeline_v0_1.md` come prerequisito
- [x] non creare `Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_2.md` solo per soddisfare il vecchio piano

---

# 10. Stato finale della v0.6

```text
Piano documentale strutturale: COMPLETED
Piano v0.6 — scope operativo: COMPLETED
Vecchio piano v0.5: SUPERSEDED
Finding documentali bloccanti residui: 0
Correzioni documentali strutturali residue: 0

Controllo commit-base non Markdown: COMPLETED
Follow-up architetturali da verificare: 0
Open issue architetturali da registrare: 0
OI-0101-011: REGISTERED_OPEN
Gate Git: AUTHORIZED_PENDING_FINAL_GIT_PRECHECK

TODO-0101: IN_ANALYSIS
TODO-0101 READY: NO
SQLite: NON INIZIATA
```

---

# 11. Prossimo passo corretto

Lo scope operativo del piano v0.6 è esaurito.

- [x] `VERIFY-BASE-001` completato;
- [x] `ARCH-FOLLOWUP-001` risolto tramite decisioni esistenti;
- [x] `ARCH-FOLLOWUP-002` trasferito correttamente a `OI-0101-011`;
- [x] `OI-0101-011` registrato formalmente;
- [x] nessuna nuova DEC necessaria;
- [x] nessuna ulteriore riorganizzazione documentale richiesta.

Prima del push eseguire soltanto il **final Git precheck** per verificare branch, working tree, file modificati e diff. Il push sarà eseguito manualmente dall'utente tramite i comandi forniti dopo tale controllo.

Dopo il push, il lavoro torna a `TODO-0101` e deve riprendere dai deliverable già previsti, a partire da **Schema Architecture**.

Non avviare TODO-0102 e non avviare SQLite.

La documentazione non deve essere nuovamente ristrutturata per soddisfare le assunzioni ormai superate della v0.5.
