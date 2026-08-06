# Project Integrity OS

## Piano TODO di correzione documentale dopo audit di secondo livello — v0.5

**Report ID:** `RPT-DOC-AUDIT-PLAN-0005`
**Data:** `2026-08-06T17:33:00+02:00`
**Repository:** `Pixelpro-agency/Integrity-OS`
**Branch locale:** `review/documentation-audit-20260806`
**Branch remoto:** `origin/review/documentation-audit-20260806`
**Commit base dell’audit:** `382c96f1f93de4ef6003f92db209675ab36d3c3c`
**Checkpoint pubblicato:** `2f3c7f9`
**Stato Git:** `CHECKPOINT_PUSHED_WORKTREE_UNCOMMITTED`
**Stato complessivo:** `BLOCKED_NOT_COMMITTABLE`
**Sostituisce:** `RPT-DOC-AUDIT-PLAN-0004`

> Questo Markdown e il JSON omonimo sono generati dalla stessa struttura dati. I codici `FND-*`, `PHASE-*`, `ACT-*`, `Q-*` e `FILE-*` identificano gli stessi elementi nei due formati.

---

## [SEC-000] Revisione v0.5

**Revisione:** `REV-005`
**Stato:** `ACTIVE_WORKING_PLAN`

Registrazione del checkpoint documentale 2f3c7f9 già pubblicato sul branch review/documentation-audit-20260806 e riallineamento della sequenza operativa: la prossima task è completare ACT-002, ACT-003 e ACT-004 senza creare ulteriori commit.

### Modifiche introdotte

- Registrato il checkpoint 2f3c7f9 contenente esclusivamente i due file del piano nella root del progetto.
- Registrata l’esistenza del branch remoto origin/review/documentation-audit-20260806.
- Confermato che non è stata creata alcuna pull request e non è stato eseguito alcun merge in main.
- Rimossa la contraddizione secondo cui HEAD doveva restare al commit base dopo il checkpoint già eseguito.
- ACT-001 trasformata in guardia attiva contro ulteriori commit e push non autorizzati.
- ACT-002 indicata come prima azione operativa da completare.
- ACT-003 e ACT-004 raggruppate nel primo blocco di reintegro degli artefatti non Markdown.
- Aggiornati gate di commit, stato Git e prossimo passo operativo.
- Rigenerato il Markdown senza trailing whitespace e senza righe vuote eccedenti a fine file.

---

## [SEC-000A] Checkpoint Git registrato

**ID:** `CHECKPOINT-DOC-AUDIT-0001`
**Stato:** `COMMITTED_AND_PUSHED`
**Branch:** `review/documentation-audit-20260806`
**Branch remoto:** `origin/review/documentation-audit-20260806`
**Commit breve:** `2f3c7f9`
**Commit completo:** `NOT_RECORDED_IN_AVAILABLE_OUTPUT`
**Messaggio:** `docs(audit): add documentation correction plan v0.4`
**File inclusi:** `2`

- `Project_Integrity_OS_Piano_TODO_Correzione_Documentale.md`
- `Project_Integrity_OS_Piano_TODO_Correzione_Documentale.json`

**Pull request creata:** `NO`
**Merge in main:** `NO`

Checkpoint di continuità e trasferimento del piano. Non costituisce approvazione del tree documentale, superamento dell’audit o autorizzazione al merge.

---

## [SEC-001] Come leggere il report

| Prefisso | Significato |
|---|---|
| `FND-*` | finding globale |
| `PHASE-*` | fase del piano |
| `ACT-*` | azione TODO |
| `Q-*` | decisione/domanda umana |
| `FILE-*` | file Markdown controllato individualmente |

Ogni azione contiene campi operativi separati:

- **Togliere:** file, percorsi o contenuti che non devono restare nella forma attuale.
- **Aggiungere:** nuovi file, metadati, cartelle o relazioni.
- **Sostituire:** contenuti o versioni da rimpiazzare.
- **Reintegrare:** artefatti del commit base persi durante la normalizzazione.
- **Decisioni applicate:** decisioni di governance già approvate che l’azione deve rispettare.

---

## [SEC-002] Esito dell’audit di secondo livello

- Markdown esaminati: **108**
- `PASS`: **76**
- `REVIEW`: **18**
- `FAIL`: **14**

**Decisione:** il checkpoint del piano è stato pubblicato, ma non sono autorizzati ulteriori commit, pull request o merge finché il gate finale non è superato.

**Decisioni già risolte:** `Q-001-D`, `Q-002-C`, `Q-003-C`, `Q-004-C`.

**Questioni ancora aperte:** nessuna.

---

## [SEC-003] Finding globali

### [FND-001] Artefatti non Markdown eliminati dal tree docs

**Severità:** `BLOCKER`

Il pacchetto è stato costruito da un archivio contenente solo file Markdown e poi ha sostituito l'intera cartella docs. Questo elimina almeno lo script docs/10-executions/TODO-0002/instructions/closure/Project_Integrity_OS_Chiusura_TODO-0002_v0_1_EXECUTED.py.

**Azioni collegate:** `ACT-003`, `ACT-004`

### [FND-002] Document Registry v0.7 non affidabile

**Severità:** `BLOCKER`

Il registro cambia identificatori DOC storici, omette documenti, usa 51 valori di stato non controllati e compila solo in minima parte la catena Sostituisce.

**Azioni collegate:** `ACT-005`, `ACT-006`, `ACT-007`, `ACT-008`

### [FND-003] Struttura reale delle task diversa dalla baseline organizzativa

**Severità:** `HIGH`

Mancano README per TODO-0002 e TODO-0003; il materiale superseded di TODO-0101 è collocato sotto instructions; manca una politica applicata uniformemente che mantenga il tree essenziale e rinvii la storia a Git.

**Azioni collegate:** `ACT-010`, `ACT-011`, `ACT-012`

### [FND-004] Metadati interni incoerenti con filename e ruolo

**Severità:** `HIGH`

Più file dichiarano FINAL, EXECUTED o SUPERSEDED nel nome ma non nel contenuto; un brief SUPERSEDED dichiara internamente CORRENTE; il report TODO-0003 non ha identità documentale completa.

**Azioni collegate:** `ACT-013`, `ACT-014`, `ACT-015`, `ACT-016`, `ACT-017`, `ACT-018`, `ACT-019`, `ACT-020`

### [FND-005] Audit Documentale v0.1 invalidato dai finding successivi

**Severità:** `BLOCKER`

L'audit v0.1 si dichiara FINAL ma non rileva la cancellazione del file Python, i difetti del Registry, le contraddizioni di stato e le divergenze strutturali.

**Azioni collegate:** `ACT-027`

### [FND-006] Decisioni di governance risolte, applicazione ancora necessaria

**Severità:** `RESOLVED_PENDING_IMPLEMENTATION`

Q-001-D, Q-002-C, Q-003-C e Q-004-C sono state approvate. Non restano domande di governance aperte; ACT-023, ACT-024, ACT-025 e ACT-026 devono ancora applicare integralmente le decisioni al tree documentale.

**Azioni collegate:** `ACT-023`, `ACT-024`, `ACT-025`, `ACT-026`

---

## [SEC-004] Ordine obbligatorio delle fasi

### [PHASE-00] Congelamento e protezione

Azioni: `ACT-001`, `ACT-002`

### [PHASE-01] Reintegro completo del tree docs

Azioni: `ACT-003`, `ACT-004`

### [PHASE-02] Ricostruzione del Document Registry

Azioni: `ACT-005`, `ACT-006`, `ACT-007`, `ACT-008`

### [PHASE-03] Correzione della governance corrente, archivio storico Git e nuova baseline documentale globale

Azioni: `ACT-009`, `ACT-010`, `ACT-011`, `ACT-023`, `ACT-024`, `ACT-012`

### [PHASE-04] Correzione dei documenti storici e delle identità

Azioni: `ACT-013`, `ACT-014`, `ACT-015`, `ACT-016`, `ACT-017`, `ACT-018`, `ACT-019`, `ACT-020`, `ACT-021`, `ACT-022`

### [PHASE-05] Applicazione delle decisioni Q-003-C e Q-004-C

Azioni: `ACT-025`, `ACT-026`

### [PHASE-06] Nuovo audit e gate di commit

Azioni: `ACT-027`, `ACT-028`, `ACT-029`

---

## [SEC-005] Lista TODO operativa completa

### [ACT-001] Congelare ulteriori commit e push dopo il checkpoint documentale

- **Fase:** `PHASE-00`
- **Stato:** `ACTIVE_GUARD`
- **Tipo operazione:** `FREEZE_AFTER_RECORDED_CHECKPOINT`
- **Dipende da:** nessuna
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** nessuna

#### Togliere
- Nulla.

#### Aggiungere
- Nulla.

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Registrare come eccezione già eseguita il checkpoint 2f3c7f9 sul branch review/documentation-audit-20260806.
- [ ] Non creare ulteriori commit o push durante ACT-002...ACT-028 senza una nuova autorizzazione esplicita dell’utente.
- [ ] Non aprire pull request prima del superamento di ACT-028 e del gate ACT-029.
- [ ] Non integrare il branch in main finché ACT-029 non è PASS e l’utente non autorizza esplicitamente il merge.
- [ ] Non eseguire force-push sul branch di revisione o su main.

#### Criteri di completamento
- [ ] Il checkpoint 2f3c7f9 resta pubblicato sul branch remoto di revisione.
- [ ] Il checkpoint contiene esclusivamente i due file del piano documentale.
- [ ] Nessuna pull request è aperta come conseguenza automatica del checkpoint.
- [ ] main non viene modificato o integrato.
- [ ] Non vengono creati ulteriori commit o push prima di una nuova autorizzazione esplicita.

### [ACT-002] Conservare backup e quarantena esistenti

- **Fase:** `PHASE-00`
- **Stato:** `NEXT`
- **Tipo operazione:** `PRESERVE`
- **Dipende da:** `ACT-001`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** nessuna

#### Togliere
- Nulla.

#### Aggiungere
- Nulla.

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Verificare che esista /c/Users/Utente/Desktop/Project_Integrity_OS_document_backups/docs_before_documentation_audit_382c96f.tar.gz.
- [ ] Verificare che il backup sia leggibile senza estrarlo sopra il working tree.
- [ ] Calcolare e registrare lo SHA-256 del backup.
- [ ] Verificare che esista /c/Users/Utente/Desktop/Project_Integrity_OS_quarantine/outside_docs_20260806_152544.
- [ ] Verificare che la quarantena sia leggibile.
- [ ] Non cancellare, spostare o modificare backup e quarantena.
- [ ] Registrare nel report finale percorsi, esistenza, leggibilità e SHA-256 del backup.

#### Criteri di completamento
- [ ] Backup e quarantena esistono e sono leggibili.
- [ ] Lo SHA-256 del backup è registrato nel report finale.
- [ ] Nessun contenuto del backup o della quarantena è stato modificato.

### [ACT-003] Reintegrare lo script di chiusura TODO-0002

- **Fase:** `PHASE-01`
- **Stato:** `QUEUED_AFTER_ACT-002`
- **Tipo operazione:** `REINTEGRATE`
- **Dipende da:** `ACT-002`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** nessuna

#### Togliere
- Nulla.

#### Aggiungere
- Nulla.

#### Sostituire
- Nulla.

#### Reintegrare
- **Sorgente:** `382c96f1f93de4ef6003f92db209675ab36d3c3c:docs/10-executions/TODO-0002/instructions/closure/Project_Integrity_OS_Chiusura_TODO-0002_v0_1_EXECUTED.py`
  - **Destinazione:** `docs/10-executions/TODO-0002/instructions/closure/Project_Integrity_OS_Chiusura_TODO-0002_v0_1_EXECUTED.py`

#### Procedura esatta
- [ ] Recuperare il file esatto dal commit base, senza riscriverlo.
- [ ] Usare il commit base 382c96f1f93de4ef6003f92db209675ab36d3c3c come sorgente autorevole.
- [ ] Verificare che il blob reintegrato sia byte-identico alla versione del commit base.
- [ ] Non sovrascrivere una copia locale differente senza creare un finding separato.
- [ ] Registrare il file nel nuovo Document Registry con l’ID storico DOC-027 durante ACT-006.
- [ ] Non creare commit o push al termine di ACT-003.

#### Criteri di completamento
- [ ] Il file Python è presente nel tree.
- [ ] SHA del file coincide con la versione del commit base.
- [ ] DOC-027 è presente nel Registry.

### [ACT-004] Inventariare e reintegrare tutti i file non Markdown sotto docs

- **Fase:** `PHASE-01`
- **Stato:** `QUEUED_AFTER_ACT-003`
- **Tipo operazione:** `REINTEGRATE`
- **Dipende da:** `ACT-003`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** nessuna

#### Togliere
- Nulla.

#### Aggiungere
- Un inventario completo di tutti i file docs non terminanti in .md nel commit base.

#### Sostituire
- Nulla.

#### Reintegrare
- **Sorgente:** `382c96f1f93de4ef6003f92db209675ab36d3c3c:docs/** (file non Markdown)`
  - **Destinazione:** `stesso percorso relativo nel branch di revisione`

#### Procedura esatta
- [ ] Confrontare `git ls-tree -r --name-only 382c96f1f93de4ef6003f92db209675ab36d3c3c docs` con il tree corrente.
- [ ] Filtrare tutti i percorsi che non terminano in `.md`.
- [ ] Classificare ogni artefatto come PRESENTE_IDENTICO, MANCANTE oppure PRESENTE_DIFFERENTE.
- [ ] Reintegrare soltanto gli artefatti MANCANTI nello stesso percorso relativo.
- [ ] Non sostituire file PRESENTE_DIFFERENTE senza un finding separato e una decisione esplicita.
- [ ] Verificare hash o identità dei blob reintegrati rispetto al commit base.
- [ ] Produrre un inventario completo degli artefatti non Markdown e un report finale.
- [ ] Non creare commit o push al termine di ACT-004.

#### Criteri di completamento
- [ ] Tutti i file non Markdown del commit base sono inventariati.
- [ ] Nessun file non Markdown presente nel commit base manca nel tree corretto.
- [ ] Ogni file reintegrato coincide con il blob del commit base.
- [ ] Nessun file differente è stato sovrascritto automaticamente.
- [ ] Il report distingue file identici, mancanti, reintegrati e differenti.

### [ACT-005] Rimuovere il Registry v0.7 dalla posizione corrente

- **Fase:** `PHASE-02`
- **Stato:** `TODO`
- **Tipo operazione:** `MOVE_AND_INVALIDATE`
- **Dipende da:** `ACT-004`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** nessuna

#### Togliere
- docs/00-current/Project_Integrity_OS_Document_Registry_v0_7.md

#### Aggiungere
- docs/20-history/registry/Project_Integrity_OS_Document_Registry_v0_7_INVALIDATED.md

#### Sostituire
- **Da:** `Project_Integrity_OS_Document_Registry_v0_7.md`
  - **A:** `Project_Integrity_OS_Document_Registry_v0_7_INVALIDATED.md`
  - **Modifica:** Aggiungere intestazione INVALIDATED senza alterare il corpo storico oltre alla nota di invalidazione.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Togliere v0.7 da docs/00-current.
- [ ] Conservarla nello storico come versione invalidata.
- [ ] Dichiarare che non deve essere usata come fonte autorevole.

#### Criteri di completamento
- [ ] Nessun Registry v0.7 resta in 00-current.

### [ACT-006] Creare Document Registry v0.8 con ID stabili

- **Fase:** `PHASE-02`
- **Stato:** `TODO`
- **Tipo operazione:** `ADD`
- **Dipende da:** `ACT-005`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`, `Q-002-C`

#### Togliere
- Nulla.

#### Aggiungere
- docs/00-current/Project_Integrity_OS_Document_Registry_v0_8.md

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Mantenere gli ID DOC-001...DOC-048 già assegnati ai documenti originari.
- [ ] Non assegnare un nuovo DOC-ID a un file solo perché è stato rinominato o spostato.
- [ ] Aggiungere nuovi ID solo ai documenti realmente nuovi dopo DOC-048.
- [ ] Registrare anche file non Markdown autorevoli, incluso DOC-027.
- [ ] Registrare nel tree corrente solo documenti e artefatti ancora necessari.
- [ ] Per i documenti superati rimossi dal tree, rinviare all'History Index con percorso storico e commit SHA completo.
- [ ] Registrare la v0.1 Prompt/Report/Rule Catalog come documento storico legato a TODO-0003.
- [ ] Registrare la nuova v0.2 Prompt/Report/Rule Catalog come baseline globale corrente e non retroattiva.
- [ ] Usare percorsi reali, non percorsi previsti.

#### Criteri di completamento
- [ ] Tutti i documenti e artefatti governati sono registrati una sola volta.
- [ ] Gli ID storici restano invariati.
- [ ] DOC-027 e DOC-028 sono presenti.
- [ ] La v0.1 e la v0.2 Prompt/Report/Rule Catalog hanno portata e stato distinti.

### [ACT-007] Normalizzare gli stati ammessi nel Registry

- **Fase:** `PHASE-02`
- **Stato:** `TODO`
- **Tipo operazione:** `REPLACE_CONTENT`
- **Dipende da:** `ACT-006`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** nessuna

#### Togliere
- I 51 valori di stato liberi o narrativi presenti nel Registry v0.7.

#### Aggiungere
- Vocabolario controllato: DRAFT, ACTIVE, FROZEN, FINAL, SUPERSEDED, INVALIDATED, CANCELLED, EXECUTED, ACCEPTED.

#### Sostituire
- **Da:** `Colonna Stato del Registry v0.7`
  - **A:** `Colonna Stato del Registry v0.8`
  - **Modifica:** Sostituire frasi narrative con uno stato canonico; spostare spiegazioni nella colonna Note.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Ogni riga deve avere un solo stato canonico.
- [ ] Le note possono spiegare autorevolezza, autenticità storica o limitazioni.
- [ ] Non usare titoli o frasi del corpo come stato.

#### Criteri di completamento
- [ ] Il Registry usa soltanto gli stati canonici.

### [ACT-008] Ricostruire tutte le catene Sostituisce

- **Fase:** `PHASE-02`
- **Stato:** `TODO`
- **Tipo operazione:** `REPLACE_CONTENT`
- **Dipende da:** `ACT-007`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** nessuna

#### Togliere
- Valori vuoti di Sostituisce dove esiste una versione precedente.

#### Aggiungere
- Relazioni esplicite tra ogni versione e la versione immediatamente precedente.

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Per ogni famiglia versionata, collegare v0.2→v0.1, v0.3→v0.2 e così via.
- [ ] Per rinomine senza cambio sostanziale, conservare lo stesso DOC-ID e registrare il nome precedente nelle note.
- [ ] Per file senza predecessore reale usare `—`.

#### Criteri di completamento
- [ ] Ogni documento versionato ha una catena completa.
- [ ] Nessuna versione corrente appare scollegata dal proprio storico.

### [ACT-009] Sostituire Errata Documentale v0.1

- **Fase:** `PHASE-03`
- **Stato:** `TODO`
- **Tipo operazione:** `MOVE_AND_REPLACE`
- **Dipende da:** `ACT-008`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`, `Q-002-C`, `Q-003-C`, `Q-004-C`

#### Togliere
- docs/00-current/Project_Integrity_OS_Errata_Documentale_v0_1.md

#### Aggiungere
- docs/20-history/errata/Project_Integrity_OS_Errata_Documentale_v0_1_SUPERSEDED.md
- docs/00-current/Project_Integrity_OS_Errata_Documentale_v0_2.md

#### Sostituire
- **Da:** `Errata v0.1`
  - **A:** `Errata v0.2`
  - **Modifica:** Aggiungere FND-001...FND-006 e collegare ogni errata agli ACT e FILE coinvolti.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Rimuovere Errata v0.1 dal tree corrente dopo averla catalogata nell'History Index con il commit che la conserva.
- [ ] Creare Errata v0.2 come documento corrente.
- [ ] Dichiarare che l'audit v0.1 è invalidato.
- [ ] Registrare Q-001-D, Q-002-C, Q-003-C e Q-004-C come decisioni approvate.
- [ ] Indicare che PRIVATE_CHILD è una categoria tecnica canonica separata e non globalmente referenziabile.
- [ ] Indicare che CLOSURE_REPORT usa un'allowlist autorevole e versionata.
- [ ] Indicare che la baseline Prompt/Report/Rule Catalog v0.1 non è retroattivamente globale.
- [ ] Indicare che la nuova v0.2 vale soltanto dalla sua approvazione in avanti.
- [ ] Non creare una copia .original.txt della v0.1.

#### Criteri di completamento
- [ ] Errata v0.2 copre tutti i finding del secondo livello.

### [ACT-010] Sostituire Organizzazione Documenti v0.2 con v0.3

- **Fase:** `PHASE-03`
- **Stato:** `TODO`
- **Tipo operazione:** `REPLACE_AND_INDEX_HISTORY`
- **Dipende da:** `ACT-009`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`, `Q-002-C`, `Q-003-C`, `Q-004-C`

#### Togliere
- docs/00-current/Project_Integrity_OS_Organizzazione_Documenti_v0_2.md
- La previsione di cartelle originals/ o copie .original.txt nel tree corrente.

#### Aggiungere
- docs/00-current/Project_Integrity_OS_Organizzazione_Documenti_v0_3.md
- Regola Q-001-D: Git come archivio storico autorevole.
- Regola Q-002-C: nuova baseline globale non retroattiva per prompt, report, decisioni, checkpoint, correzioni e verifiche.
- Regola Q-003-C: PRIVATE_CHILD come categoria tecnica canonica separata, privata e dipendente dal genitore.
- Regola Q-004-C: allowlist autorevole e versionata per i proprietari di CLOSURE_REPORT.
- Regola: un solo documento corrente per famiglia in docs/00-current/.
- Regola: i documenti superati già committati vengono catalogati nell'History Index e rimossi dal tree.
- Regola: artefatti mai committati e non necessari restano fuori dalla repository con manifest SHA-256.

#### Sostituire
- **Da:** `Struttura task descritta in v0.2`
  - **A:** `Struttura task canonica in v0.3`
  - **Modifica:** Allineare README, instructions, evidence, reports, decisions, verification e validation; eliminare la conservazione permanente delle versioni superseded nel tree quando sono recuperabili da Git.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Catalogare Organizzazione Documenti v0.2 nell'History Index con il commit SHA che la conserva.
- [ ] Rimuovere v0.2 dal tree corrente senza duplicarla in 20-history.
- [ ] Creare v0.3 come unica versione corrente.
- [ ] Definire che l'inventario copre tutti i file sotto docs, non soltanto i Markdown.
- [ ] Definire che README principale, History Index e Project Timeline sono i punti di accesso alla ricostruzione storica.
- [ ] Integrare la baseline globale Q-002-C senza attribuirle validità retroattiva.
- [ ] Definire che il set documentale di una task è proporzionato a complessità, rischio, numero di decisioni e necessità di verifica.
- [ ] Distinguere esplicitamente categorie governate e globalmente referenziabili dalla categoria tecnica PRIVATE_CHILD.
- [ ] Definire che le allowlist di dominio, inclusa quella di CLOSURE_REPORT, sono autorevoli, versionate e modificabili solo tramite decisione approvata.

#### Criteri di completamento
- [ ] La struttura descritta coincide con il tree reale finale.
- [ ] Nessuna copia .original.txt è richiesta.
- [ ] La politica Git/History Index è esplicita e univoca.

### [ACT-011] Aggiungere README di task e collegamenti storici nel README principale

- **Fase:** `PHASE-03`
- **Stato:** `TODO`
- **Tipo operazione:** `ADD_AND_UPDATE`
- **Dipende da:** `ACT-010`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`, `Q-002-C`

#### Togliere
- Nulla.

#### Aggiungere
- docs/10-executions/TODO-0002/README.md
- docs/10-executions/TODO-0003/README.md
- Sezione `Cronologia e documentazione storica` nel README.md principale.

#### Sostituire
- **Da:** `README.md principale privo di accesso alla storia documentale`
  - **A:** `README.md con link a History Index e Project Timeline`
  - **Modifica:** Aggiungere una sezione breve senza duplicare l'elenco completo dei documenti storici.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Ogni README di task deve indicare task, stato finale, documenti ancora presenti, report, verifica, approvazione e commit di riferimento.
- [ ] I README di task devono usare link relativi verificabili.
- [ ] Il README principale deve collegare `docs/00-current/Project_Integrity_OS_History_Index_v0_1.md`.
- [ ] Il README principale deve collegare `docs/00-current/Project_Integrity_OS_Project_Timeline_v0_1.md`.
- [ ] Il README principale deve collegare la baseline globale `Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_2.md`.
- [ ] Il README principale non deve contenere l'intero catalogo storico.
- [ ] I README delle nuove task devono indicare quali moduli documentali della baseline v0.2 sono stati attivati e quali non erano necessari.

#### Criteri di completamento
- [ ] TODO-0002 e TODO-0003 hanno un indice locale completo.
- [ ] Il README principale consente di raggiungere History Index e Project Timeline.

### [ACT-012] Catalogare e rimuovere dal tree il materiale superseded di TODO-0101

- **Fase:** `PHASE-03`
- **Stato:** `TODO`
- **Tipo operazione:** `INDEX_HISTORY_AND_REMOVE`
- **Dipende da:** `ACT-024`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`

#### Togliere
- docs/10-executions/TODO-0101/instructions/superseded/
- Qualsiasi seconda copia Markdown della stessa identità/versione già recuperabile dal commit base.

#### Aggiungere
- Voci nell'History Index per ogni file rimosso, con commit SHA completo e percorso storico.
- Riferimento sintetico nel README di TODO-0101 alla storia recuperabile tramite Git.

#### Sostituire
- **Da:** `Link a instructions/superseded`
  - **A:** `Link all'History Index o al commit SHA pertinente`
  - **Modifica:** Aggiornare README, checkpoint, Registry e documenti correnti.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Inventariare tutti i file della cartella superseded prima della rimozione.
- [ ] Verificare che ciascun file esista nel commit base o in un altro commit stabile.
- [ ] Aggiungere una voce distinta nell'History Index per ogni file.
- [ ] Rimuovere la cartella superseded dal tree corrente dopo la verifica.
- [ ] Non creare una nuova cartella superseded in un altro percorso.

#### Criteri di completamento
- [ ] La cartella superseded di TODO-0101 non resta nel tree.
- [ ] Ogni file rimosso è catalogato e recuperabile tramite Git.
- [ ] Nessun link corrente punta alla cartella rimossa.

### [ACT-013] Correggere il prompt browser finale TODO-0002

- **Fase:** `PHASE-04`
- **Stato:** `TODO`
- **Tipo operazione:** `REPLACE_GOVERNED_FILE`
- **Dipende da:** `ACT-012`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`

#### Togliere
- Riferimenti legacy non mappati.
- Qualsiasi wrapper o copia `.original.txt` introdotta soltanto per duplicare la versione già presente in Git.

#### Aggiungere
- Metadati espliciti Task, Versione, Stato FINAL, autenticità storica e commit che conserva la versione precedente.

#### Sostituire
- **Da:** `Riferimenti legacy non mappati`
  - **A:** `Riferimenti canonici o note storiche con commit SHA`
  - **Modifica:** Il file governato viene corretto; la versione precedente resta recuperabile da Git.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Mantenere il prompt finale realmente utilizzato come artefatto della task.
- [ ] Correggere soltanto identità, metadati e riferimenti documentali.
- [ ] Registrare nell'History Index il percorso e il commit della versione precedente.
- [ ] Non creare wrapper, sidecar o copie originali duplicate.

#### Criteri di completamento
- [ ] Filename, metadati e riferimenti sono coerenti.
- [ ] La versione precedente è recuperabile tramite Git.

### [ACT-014] Correggere Start Here browser finale TODO-0002

- **Fase:** `PHASE-04`
- **Stato:** `TODO`
- **Tipo operazione:** `REPLACE_GOVERNED_FILE`
- **Dipende da:** `ACT-013`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`

#### Togliere
- Riferimento non risolto a Project_Integrity_OS_Brief_TODO-0002.md.
- Eventuali copie originali duplicate nel tree.

#### Aggiungere
- Riferimento al brief realmente utilizzato.
- Metadati Versione v0.1 e Stato FINAL.
- Nota con commit SHA che conserva la versione precedente.

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Mantenere il documento perché descrive la procedura realmente usata.
- [ ] Correggere il riferimento al brief senza creare un alias fittizio.
- [ ] Catalogare la versione precedente nell'History Index.

#### Criteri di completamento
- [ ] Nessun riferimento a file inesistente resta senza spiegazione.
- [ ] La storia precedente è recuperabile tramite Git.

### [ACT-015] Correggere Start Here chiusura TODO-0002

- **Fase:** `PHASE-04`
- **Stato:** `TODO`
- **Tipo operazione:** `REPLACE_CONTENT`
- **Dipende da:** `ACT-014`, `ACT-003`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** nessuna

#### Togliere
- Riferimento ambiguo a close_todo_0002.py.

#### Aggiungere
- Riferimento esatto a Project_Integrity_OS_Chiusura_TODO-0002_v0_1_EXECUTED.py.
- Metadato Stato EXECUTED.

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Indicare che `close_todo_0002.py` era eventualmente il nome operativo precedente, se dimostrabile.
- [ ] Non inventare alias se non supportato: in assenza di evidenza, dichiarare il mismatch come errata.

#### Criteri di completamento
- [ ] Il documento punta all'artefatto realmente presente e registrato.

### [ACT-016] Catalogare e rimuovere il Brief TODO-0002 v0.1 superseded

- **Fase:** `PHASE-04`
- **Stato:** `TODO`
- **Tipo operazione:** `INDEX_HISTORY_AND_REMOVE`
- **Dipende da:** `ACT-015`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`

#### Togliere
- docs/10-executions/TODO-0002/superseded/Project_Integrity_OS_Brief_TODO-0002_v0_1_SUPERSEDED.md

#### Aggiungere
- Voce History Index con nome, percorso nel commit, SHA completo, stato SUPERSEDED e documento sostitutivo.

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Verificare che il file sia presente in un commit stabile.
- [ ] Catalogarlo nell'History Index.
- [ ] Rimuoverlo dal tree corrente.
- [ ] Non riscrivere il contenuto e non creare una copia .original.txt.

#### Criteri di completamento
- [ ] Il file non è nel tree ed è recuperabile dal commit indicato.

### [ACT-017] Catalogare e rimuovere il Brief TODO-0002 v0.2 superseded

- **Fase:** `PHASE-04`
- **Stato:** `TODO`
- **Tipo operazione:** `INDEX_HISTORY_AND_REMOVE`
- **Dipende da:** `ACT-016`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`

#### Togliere
- docs/10-executions/TODO-0002/superseded/Project_Integrity_OS_Brief_TODO-0002_v0_2_SUPERSEDED.md

#### Aggiungere
- Voce History Index che spiega che il documento era CORRENTE durante l'esecuzione e oggi è SUPERSEDED.
- Commit SHA completo e percorso storico.

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Non correggere retroattivamente lo stato CORRENTE nel file storico.
- [ ] Spiegare la differenza temporale nell'History Index.
- [ ] Rimuovere il file dal tree corrente dopo la verifica Git.

#### Criteri di completamento
- [ ] La contraddizione temporale è spiegata nell'History Index.
- [ ] Il file non è duplicato nel tree.

### [ACT-018] Catalogare e rimuovere prompt e Start Here desktop superseded di TODO-0002

- **Fase:** `PHASE-04`
- **Stato:** `TODO`
- **Tipo operazione:** `INDEX_HISTORY_AND_REMOVE`
- **Dipende da:** `ACT-017`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`

#### Togliere
- docs/10-executions/TODO-0002/superseded/Project_Integrity_OS_Prompt_Esecutivo_Desktop_TODO-0002_v0_1_SUPERSEDED.md
- docs/10-executions/TODO-0002/superseded/Project_Integrity_OS_Start_Here_Desktop_TODO-0002_v0_1_SUPERSEDED.md

#### Aggiungere
- Due voci separate nell'History Index con commit SHA e motivo: varianti desktop non usate nella sessione browser.

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Verificare la presenza dei due file nel commit storico.
- [ ] Catalogarli separatamente.
- [ ] Rimuoverli dal tree corrente.

#### Criteri di completamento
- [ ] Entrambi i file sono recuperabili tramite Git e non restano nel tree.

### [ACT-019] Aggiungere identità documentale al report TODO-0003

- **Fase:** `PHASE-04`
- **Stato:** `TODO`
- **Tipo operazione:** `REPLACE_GOVERNED_FILE`
- **Dipende da:** `ACT-018`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`

#### Togliere
- Qualsiasi wrapper o copia originale duplicata del report già conservato in Git.

#### Aggiungere
- H1 `# Project Integrity OS`.
- H2 `## Report esecutivo — TODO-0003 — v0.1`.
- Metadati Task, Versione, Stato FINAL, tipo Report originale/raw.

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Mantenere il report perché è un artefatto finale della task.
- [ ] Aggiungere H1, H2 e metadati senza modificare il corpo delle dichiarazioni dell'esecutore.
- [ ] Catalogare nell'History Index la versione precedente con commit SHA completo.
- [ ] Non creare wrapper o copie .original.txt.

#### Criteri di completamento
- [ ] Il report è identificabile senza alterare le dichiarazioni originali.

### [ACT-020] Catalogare e rimuovere i sei documenti concettuali storici superseded

- **Fase:** `PHASE-04`
- **Stato:** `TODO`
- **Tipo operazione:** `INDEX_HISTORY_AND_REMOVE`
- **Dipende da:** `ACT-019`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`

#### Togliere
- docs/20-history/concept/Project_Integrity_OS_Concetto_Integrita_Continuita_v0_1_SUPERSEDED.md
- docs/20-history/concept/Project_Integrity_OS_Concetto_Integrita_Continuita_v0_2_SUPERSEDED.md
- docs/20-history/concept/Project_Integrity_OS_Concetto_Integrita_Continuita_v0_3_SUPERSEDED.md
- docs/20-history/concept/Project_Integrity_OS_Concetto_Integrita_Continuita_v0_4_SUPERSEDED.md
- docs/20-history/concept/Project_Integrity_OS_Concetto_Integrita_Continuita_v0_5_SUPERSEDED.md
- docs/20-history/concept/Project_Integrity_OS_Concetto_Integrita_Continuita_v0_6_SUPERSEDED.md

#### Aggiungere
- Sei voci ordinate nell'History Index, ciascuna con nome legacy, versione, percorso storico, commit SHA e successore.

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Verificare per ogni versione il commit che la conserva.
- [ ] Catalogare le versioni in ordine v0.1...v0.6.
- [ ] Rimuovere i sei file dal tree corrente.
- [ ] Non creare wrapper, sidecar o copie .original.txt.

#### Criteri di completamento
- [ ] Le sei versioni sono recuperabili tramite Git.
- [ ] Nessuna versione concettuale superseded resta nel tree corrente.

### [ACT-021] Correggere il riferimento history/history nel Decision Log v0.7

- **Fase:** `PHASE-04`
- **Stato:** `TODO`
- **Tipo operazione:** `REPLACE_CONTENT`
- **Dipende da:** `ACT-020`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** nessuna

#### Togliere
- Versione precedente: history/Project_Integrity_OS_Decision_Log_TODO-0101_v0_6_DRAFT.md

#### Aggiungere
- Versione precedente: Project_Integrity_OS_Decision_Log_TODO-0101_v0_6_DRAFT.md

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Correggere solo il riferimento relativo.
- [ ] Non modificare le decisioni contenute nello snapshot storico.

#### Criteri di completamento
- [ ] Il link relativo risolve al file v0.6 nella stessa cartella history.

### [ACT-022] Rimuovere la doppia identità Markdown del brief TODO-0101 v0.1

- **Fase:** `PHASE-04`
- **Stato:** `TODO`
- **Tipo operazione:** `INDEX_HISTORY_AND_REMOVE_DUPLICATE`
- **Dipende da:** `ACT-021`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`

#### Togliere
- docs/10-executions/TODO-0101/instructions/superseded/history/Project_Integrity_OS_Brief_TODO-0101_v0_1_DRAFT_ORIGINAL.md
- Qualsiasi copia `.original.txt` equivalente.

#### Aggiungere
- Voce History Index con commit SHA e percorso originario del brief.

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Verificare il commit che conserva l'originale.
- [ ] Catalogare l'originale nell'History Index.
- [ ] Rimuovere la doppia identità dal tree.
- [ ] Mantenere nel tree soltanto l'eventuale documento corrente realmente necessario.

#### Criteri di completamento
- [ ] Esiste una sola identità governata attiva per il Brief TODO-0101 v0.1.
- [ ] L'originale è recuperabile tramite Git.

### [ACT-023] Applicare Q-001-D: Git come archivio storico autorevole

- **Fase:** `PHASE-03`
- **Stato:** `TODO`
- **Tipo operazione:** `IMPLEMENT_APPROVED_DECISION`
- **Dipende da:** `ACT-011`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`

#### Togliere
- Copie `.original.txt` previste o già introdotte come duplicati di file presenti in Git.
- Wrapper creati esclusivamente per conservare una seconda copia di documenti storici già committati.
- Versioni SUPERSEDED, bozze e checkpoint non più necessari al lavoro corrente, dopo catalogazione nell'History Index.
- Pacchetti ZIP, backup, output temporanei e bozze mai approvate dal tree della repository.

#### Aggiungere
- docs/00-current/Project_Integrity_OS_History_Index_v0_1.md
- docs/00-current/Project_Integrity_OS_Project_Timeline_v0_1.md
- Sezione `Cronologia e documentazione storica` nel README.md principale.
- Per ogni documento rimosso: nome, percorso storico, commit SHA completo, task, stato storico, documento sostitutivo e motivo della rimozione.
- Per ogni milestone: sequenza, data, evento, task, documenti principali e commit SHA completo.

#### Sostituire
- **Da:** `Conservazione delle versioni superate nel tree corrente`
  - **A:** `Catalogazione storica tramite Git e History Index`
  - **Modifica:** Il contenuto storico resta recuperabile dal commit SHA; il tree contiene solo documenti correnti, artefatti finali di task ed evidenze necessarie.
- **Da:** `README principale come eventuale catalogo completo`
  - **A:** `README principale come punto di accesso sintetico`
  - **Modifica:** Il dettaglio completo resta nell'History Index e nella Project Timeline.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Creare l'History Index con SHA completi, non abbreviati.
- [ ] Registrare per ogni documento storico rimosso il percorso esatto nel commit che lo conserva.
- [ ] Creare la Project Timeline come sequenza cronologica di task, decisioni e milestone.
- [ ] Aggiornare il README principale con due link relativi, senza duplicare le tabelle storiche.
- [ ] Mantenere nel tree solo documenti correnti, brief e prompt realmente usati quando ancora necessari come artefatti finali, report originali, verifiche, decisioni approvate, evidenze e approvazioni.
- [ ] Rimuovere dal tree documenti superati già presenti in Git dopo averli catalogati.
- [ ] Conservare fuori dalla repository gli artefatti mai committati e non necessari, accompagnati da manifest SHA-256.
- [ ] Non riscrivere i commit storici citati; evitare force-push su main.
- [ ] I tag milestone possono essere aggiunti successivamente, ma non sostituiscono il commit SHA completo.

#### Criteri di completamento
- [ ] History Index presente e completo.
- [ ] Project Timeline presente e completa per i commit già esistenti.
- [ ] README principale collega entrambi i documenti.
- [ ] Nessun duplicato .original.txt resta nel tree.
- [ ] Ogni documento storico rimosso è recuperabile con `git show <SHA>:<percorso>`.
- [ ] Il tree corrente contiene soltanto documentazione utile al progetto attuale o necessaria come evidenza finale.

### [ACT-024] Applicare Q-002-C e creare la baseline globale Prompt/Report/Rule Catalog v0.2

- **Fase:** `PHASE-03`
- **Stato:** `TODO`
- **Tipo operazione:** `IMPLEMENT_APPROVED_DECISION`
- **Dipende da:** `ACT-023`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-001-D`, `Q-002-C`

#### Togliere
- docs/00-current/Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md
- Qualsiasi dichiarazione che renda retroattivamente globale la v0.1.
- Qualsiasi regola che imponga a ogni task futura di produrre sempre lo stesso numero di documenti.

#### Aggiungere
- docs/00-current/Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_2.md
- Voce History Index per la v0.1 con ambito storico TODO-0003 e commit SHA completo.
- Voce Project Timeline per l'approvazione della nuova baseline globale v0.2.
- Riferimento alla v0.2 nel README principale.
- Riferimento alla v0.2 nel Document Registry v0.8.
- Riferimento alla v0.2 in Organizzazione Documenti v0.3.
- Riferimento alla v0.2 nella To-Do corrente.

#### Sostituire
- **Da:** `Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md`
  - **A:** `Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_2.md`
  - **Modifica:** La v0.1 resta storica e riferita a TODO-0003; la v0.2 diventa baseline globale corrente solo dalla sua approvazione in avanti.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Verificare il commit stabile che conserva la v0.1.
- [ ] Catalogare la v0.1 nell'History Index con nome, percorso, SHA completo, ambito TODO-0003, stato SUPERSEDED e successore v0.2.
- [ ] Rimuovere la v0.1 da docs/00-current senza riscriverla retroattivamente.
- [ ] Creare integralmente la v0.2 come nuova baseline globale non retroattiva.
- [ ] Dichiarare nella v0.2 che il metodo deriva dall'esperienza documentale consolidata durante TODO-0101.
- [ ] Definire moduli documentali distinti: task contract/brief, prompt, analisi, decision log, decisioni individuali, checkpoint, correction set, report, evidenze, verifica, validazione e gate.
- [ ] Definire che non tutti i moduli sono obbligatori per ogni task.
- [ ] Definire criteri deterministici per attivare i moduli: complessità, rischio, numero di decisioni, impatto trasversale, necessità di checkpoint e verifica.
- [ ] Definire identificatori stabili per decisioni, correzioni, finding, criteri, evidenze e verifiche.
- [ ] Definire collegamenti obbligatori tra i documenti prodotti.
- [ ] Definire versionamento, stato canonico, documento sostituito e data di validità.
- [ ] Definire la distinzione tra decisione approvata e documento ancora DRAFT.
- [ ] Definire l'obbligo di registrare ogni nuovo documento nel Document Registry.
- [ ] Definire l'obbligo di aggiornare History Index e Project Timeline quando un documento viene sostituito o una milestone viene approvata.
- [ ] Definire un gate prima del commit e un audit finale del tree completo.
- [ ] Aggiornare README principale, To-Do corrente, Organizzazione Documenti e Registry con la nuova baseline.

#### Criteri di completamento
- [ ] La v0.1 resta recuperabile tramite Git e non è descritta come globale retroattiva.
- [ ] La v0.2 è l'unica baseline globale corrente della famiglia.
- [ ] La v0.2 dichiara una data o un commit di entrata in vigore.
- [ ] La v0.2 formalizza il metodo TODO-0101 senza imporre sempre venti documenti.
- [ ] Ogni modulo ha scopo, trigger di attivazione, identificatore e relazione con gli altri moduli.
- [ ] Registry, To-Do, Organizzazione Documenti, History Index, Project Timeline e README sono coerenti con Q-002-C.

### [ACT-025] Applicare Q-003-C: PRIVATE_CHILD come categoria tecnica canonica separata

- **Fase:** `PHASE-05`
- **Stato:** `TODO`
- **Tipo operazione:** `IMPLEMENT_APPROVED_DECISION`
- **Dipende da:** `ACT-024`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-003-C`

#### Togliere
- Qualsiasi elenco che presenti PRIVATE_CHILD sullo stesso piano delle categorie governate e globalmente referenziabili.
- Qualsiasi regola che permetta a PRIVATE_CHILD di entrare nel Global Registry.
- Qualsiasi regola che permetta riferimenti globali arbitrari verso PRIVATE_CHILD.
- Qualsiasi lifecycle autonomo implicito per PRIVATE_CHILD.
- Qualsiasi possibilità per PRIVATE_CHILD di possedere CLOSURE_REPORT.

#### Aggiungere
- Definizione canonica di PRIVATE_CHILD come categoria tecnica privata.
- Regola: ogni PRIVATE_CHILD appartiene obbligatoriamente a un solo genitore.
- Regola: PRIVATE_CHILD non può esistere senza il proprio genitore.
- Regola: PRIVATE_CHILD non può cambiare genitore liberamente.
- Regola: PRIVATE_CHILD non viene registrato nel Global Registry.
- Regola: PRIVATE_CHILD non può essere destinazione di riferimenti globali.
- Regola: l'eventuale identificatore è tecnico e locale al contesto del genitore.
- Regola: PRIVATE_CHILD non possiede normalmente un lifecycle autonomo.
- Regola: cancellazione o archiviazione del genitore comporta gestione coordinata dei figli privati.
- Regola: eventuali eccezioni richiedono una decisione architetturale esplicita.

#### Sostituire
- **Da:** `Documento decisionale 10 e documenti che elencano le categorie canoniche`
  - **A:** `Classificazione a due livelli coerente con Q-003-C`
  - **Modifica:** Separare le categorie governate e globalmente referenziabili dalla categoria tecnica canonica PRIVATE_CHILD.
- **Da:** `Formulazione generica `PRIVATE_CHILD è una categoria canonica``
  - **A:** ``PRIVATE_CHILD è una categoria tecnica canonica, privata, non globalmente referenziabile e dipendente dal genitore``
  - **Modifica:** Eliminare ogni ambiguità sul ruolo e sulla visibilità.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Aggiornare `Project_Integrity_OS_10_Integrita_Trasversale_Anti_Orfano_TODO-0101_v0_3_DRAFT.md`.
- [ ] Aggiornare il Correction Set di TODO-0101.
- [ ] Aggiornare il Decision Log corrente di TODO-0101.
- [ ] Aggiornare tutti i documenti che presentano l'elenco canonico delle categorie.
- [ ] Aggiornare la futura baseline Prompt/Report/Rule Catalog v0.2 se contiene regole sulle categorie di entità.
- [ ] Registrare Q-003-C nel Document Registry, nella Project Timeline e nei README pertinenti.
- [ ] Definire un vincolo deterministico che impedisca PRIVATE_CHILD orfani.
- [ ] Definire che un riferimento globale verso PRIVATE_CHILD è invalido.
- [ ] Definire che l'identificatore locale di PRIVATE_CHILD non deve essere esposto come identità pubblica del progetto.
- [ ] Aggiornare il futuro Entity Catalog e Constraint Catalog quando saranno prodotti.
- [ ] Aggiungere test futuri per: figlio senza genitore, cambio genitore non autorizzato, riferimento globale vietato e rimozione coordinata.

#### Criteri di completamento
- [ ] Tutti gli elenchi di categorie distinguono chiaramente categorie governate e PRIVATE_CHILD.
- [ ] PRIVATE_CHILD non appare nel Global Registry.
- [ ] PRIVATE_CHILD non è globalmente referenziabile.
- [ ] PRIVATE_CHILD appartiene a un solo genitore e non può restare orfano.
- [ ] PRIVATE_CHILD non possiede CLOSURE_REPORT.
- [ ] Correction Set, Decision Log e documento decisionale 10 sono coerenti.

### [ACT-026] Applicare Q-004-C: allowlist versionata per CLOSURE_REPORT

- **Fase:** `PHASE-05`
- **Stato:** `TODO`
- **Tipo operazione:** `IMPLEMENT_APPROVED_DECISION`
- **Dipende da:** `ACT-025`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** `Q-004-C`

#### Togliere
- La regola generica secondo cui qualunque entità con stato CLOSED può possedere CLOSURE_REPORT.
- La lista dei cinque owner type trattata come vincolo architetturale immutabile e sparso nel codice.
- Qualsiasi accettazione di owner_type arbitrari o stringhe libere.
- Qualsiasi possibilità per PRIVATE_CHILD di possedere CLOSURE_REPORT.

#### Aggiungere
- Allowlist autorevole e versionata dei tipi proprietari ammessi per CLOSURE_REPORT.
- Versione iniziale MVP: PROJECT, PHASE, WORK_ITEM, TASK e BASELINE.
- Regola: lo stato CLOSED non abilita automaticamente CLOSURE_REPORT.
- Regola: un owner type è valido soltanto se presente nell'allowlist attiva.
- Regola: PRIVATE_CHILD è sempre escluso dall'allowlist.
- Regola: l'aggiunta di un nuovo owner type richiede una decisione architetturale approvata.
- Regola: ogni estensione aggiorna cataloghi, lifecycle, vincoli, documentazione, migrazioni e test.
- Regola: l'allowlist possiede versione, stato e data o commit di entrata in vigore.

#### Sostituire
- **Da:** `Documento decisionale 14, Correction Set e Decision Log`
  - **A:** `Regola unica coerente con Q-004-C`
  - **Modifica:** Definire owner_type tramite allowlist autorevole e versionata, con cinque valori iniziali e procedura controllata di estensione.
- **Da:** `Controllo tramite stringa libera o elenco duplicato in più punti`
  - **A:** `Unica fonte autorevole della allowlist`
  - **Modifica:** Il codice e i vincoli devono dipendere dalla stessa definizione canonica.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Aggiornare `Project_Integrity_OS_14_Cardinalita_Tabelle_Associative_TODO-0101_v0_3_DRAFT.md`.
- [ ] Aggiornare il Correction Set di TODO-0101.
- [ ] Aggiornare il Decision Log corrente di TODO-0101.
- [ ] Registrare Q-004-C nel Document Registry, nella Project Timeline e nei README pertinenti.
- [ ] Definire l'allowlist iniziale con PROJECT, PHASE, WORK_ITEM, TASK e BASELINE.
- [ ] Definire che PRIVATE_CHILD non può essere aggiunto all'allowlist.
- [ ] Definire che una nuova entità non entra automaticamente nell'allowlist quando acquisisce lo stato CLOSED.
- [ ] Definire la procedura di estensione: decisione approvata, lifecycle, criteri di chiusura, evidenze, aggiornamento cataloghi e vincoli, eventuale migrazione e test.
- [ ] Aggiornare il futuro Entity Catalog e Constraint Catalog quando saranno prodotti.
- [ ] Aggiungere test futuri per owner type consentito, owner type vietato, stringa arbitraria, versione allowlist e tentativo PRIVATE_CHILD.

#### Criteri di completamento
- [ ] Esiste una sola regola autorevole per CLOSURE_REPORT.
- [ ] L'allowlist iniziale contiene soltanto PROJECT, PHASE, WORK_ITEM, TASK e BASELINE.
- [ ] PRIVATE_CHILD è escluso.
- [ ] Owner type arbitrari vengono rifiutati.
- [ ] Ogni estensione richiede una decisione approvata e aggiornamenti coordinati.
- [ ] Documento decisionale 14, Correction Set e Decision Log sono coerenti.

### [ACT-027] Invalidare Audit Documentale v0.1 e creare v0.2

- **Fase:** `PHASE-06`
- **Stato:** `TODO`
- **Tipo operazione:** `MOVE_AND_REPLACE`
- **Dipende da:** `ACT-026`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** nessuna

#### Togliere
- docs/10-executions/TODO-0101/analysis/verification/Project_Integrity_OS_Audit_Documentale_TODO-0101_v0_1.md

#### Aggiungere
- docs/10-executions/TODO-0101/analysis/verification/history/Project_Integrity_OS_Audit_Documentale_TODO-0101_v0_1_INVALIDATED.md
- docs/10-executions/TODO-0101/analysis/verification/Project_Integrity_OS_Audit_Documentale_TODO-0101_v0_2_DRAFT.md

#### Sostituire
- **Da:** `Conclusione FINAL della v0.1`
  - **A:** `Nota INVALIDATED`
  - **Modifica:** La v0.2 deve includere controllo Markdown e non Markdown, Registry, link, metadati e decisioni risolte.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Conservare la v0.1 come prova dell'audit incompleto.
- [ ] Creare Audit Documentale v0.2 soltanto dopo l'applicazione di Q-001-D, Q-002-C, Q-003-C e Q-004-C.
- [ ] Verificare esplicitamente la portata non retroattiva della baseline Prompt/Report/Rule Catalog v0.2.
- [ ] Verificare la separazione tra categorie governate e PRIVATE_CHILD.
- [ ] Verificare l'allowlist versionata di CLOSURE_REPORT.
- [ ] La v0.2 potrà diventare FINAL solo dopo ACT-028.

#### Criteri di completamento
- [ ] L'audit corrente non contiene conclusioni smentite dai finding.

### [ACT-028] Rieseguire il controllo completo del tree docs

- **Fase:** `PHASE-06`
- **Stato:** `TODO`
- **Tipo operazione:** `VERIFY`
- **Dipende da:** `ACT-027`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** nessuna

#### Togliere
- Nulla.

#### Aggiungere
- Report finale con inventario di tutti i file sotto docs, non solo .md.

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Controllare UTF-8, NUL, marker Git, code fence, link, nome/versione/stato, duplicati e hash.
- [ ] Confrontare tutti i file del commit base con il tree finale.
- [ ] Verificare che ogni documento governato presente nel tree sia nel Registry.
- [ ] Verificare che ogni documento storico rimosso sia nell'History Index con commit SHA completo e percorso recuperabile.
- [ ] Verificare che la Project Timeline copra i commit e le milestone già consolidate.
- [ ] Verificare che README principale e README di task abbiano link relativi validi.
- [ ] Verificare che non esistano copie .original.txt o wrapper duplicativi non autorizzati.
- [ ] Verificare che la v0.1 Prompt/Report/Rule Catalog sia storica e legata a TODO-0003.
- [ ] Verificare che la v0.2 Prompt/Report/Rule Catalog sia globale soltanto dalla sua entrata in vigore.
- [ ] Verificare che le nuove task usino moduli proporzionati e non un numero fisso di documenti.
- [ ] Verificare che i nuovi documenti logici siano registrati in Registry, History Index, Project Timeline e README pertinenti.
- [ ] Verificare che PRIVATE_CHILD sia categoria tecnica separata, privata, dipendente dal genitore e non globalmente referenziabile.
- [ ] Verificare che PRIVATE_CHILD non sia nel Global Registry e non possa possedere CLOSURE_REPORT.
- [ ] Verificare che CLOSURE_REPORT accetti soltanto owner type presenti nell'allowlist attiva.
- [ ] Verificare che l'allowlist iniziale contenga PROJECT, PHASE, WORK_ITEM, TASK e BASELINE.
- [ ] Verificare che l'estensione dell'allowlist richieda decisione approvata, aggiornamento di cataloghi, vincoli, migrazioni e test.
- [ ] Verificare che ogni ID DOC sia unico e stabile.
- [ ] Verificare che tutti i link relativi risolvano.

#### Criteri di completamento
- [ ] Zero FAIL.
- [ ] Zero decisioni aperte.
- [ ] Zero file mancanti rispetto al commit base salvo rimozioni catalogate nell'History Index o esplicitamente approvate.
- [ ] Zero documenti storici rimossi senza SHA e percorso di recupero.
- [ ] PRIVATE_CHILD è coerente in tutti i documenti.
- [ ] L'allowlist CLOSURE_REPORT è coerente in tutti i documenti.
- [ ] Audit v0.2 può essere promosso a FINAL.

### [ACT-029] Autorizzare il commit soltanto dopo esito completo

- **Fase:** `PHASE-06`
- **Stato:** `TODO`
- **Tipo operazione:** `GATE`
- **Dipende da:** `ACT-028`
- **Bloccata da domande:** nessuna
- **Decisioni applicate:** nessuna

#### Togliere
- Nulla.

#### Aggiungere
- Nulla.

#### Sostituire
- Nulla.

#### Reintegrare
- Nulla.

#### Procedura esatta
- [ ] Eseguire git diff --check e controllo scope.
- [ ] Produrre elenco esatto dei file aggiunti, spostati, sostituiti e reintegrati.
- [ ] Chiedere autorizzazione esplicita prima del commit.
- [ ] Non eseguire push senza autorizzazione separata.

#### Criteri di completamento
- [ ] Tutti gli ACT precedenti sono DONE.
- [ ] Audit v0.2 è FINAL.
- [ ] Working tree contiene solo modifiche documentali approvate.

---

## [SEC-006] Decisioni di governance

### [Q-001] Come conservare la storia mantenendo il progetto pulito e ordinato?

**Stato:** `RESOLVED`
**Decisione:** `Q-001-D`

#### Cosa significa in parole semplici

La cronologia completa non deve essere mantenuta duplicando nel tree corrente ogni versione superata. Git conserva già il contenuto dei file nei commit. Il tree operativo deve contenere soltanto documenti correnti, artefatti finali delle task ed evidenze necessarie.

#### Perché è importante

- Il progetto deve restare leggibile e ordinato durante lo sviluppo.
- Le versioni superate devono restare recuperabili senza occupare il tree corrente.
- Il README principale deve offrire un accesso semplice alla storia senza trasformarsi in un registro enorme.
- La ricostruzione step by step deve basarsi su commit SHA completi, History Index e Project Timeline.

#### Esempio concreto

Una To-Do v0.5 ormai sostituita può essere rimossa dal tree corrente se esiste nel commit `bb4c31bdd58f67432c27d491c92467b6a57a6e52`. L'History Index conserva nome, percorso, stato storico e SHA; il file può essere recuperato con `git show <SHA>:<percorso>`.

#### Opzioni

**Q-001-A — Originali dentro il repository come .original.txt** — `NOT_SELECTED`

Ogni originale byte-identico viene salvato in una cartella `originals/`; il Markdown governato contiene metadati corretti e punta all'originale.

- Vantaggi: Repository autosufficiente; Audit byte-per-byte possibile offline.
- Svantaggi: Più file; Tree documentale più pesante.

**Q-001-B — Originali soltanto nel pacchetto esterno** — `NOT_SELECTED`

Nel repository restano solo i Markdown governati; gli originali sono conservati in ZIP/backup esterno con hash.

- Vantaggi: Repository più pulito.
- Svantaggi: Il repository da solo non contiene tutta la prova storica; Rischio di perdere il pacchetto esterno.

**Q-001-C — Originali Markdown immutati più sidecar di metadati** — `NOT_SELECTED`

Gli originali `.md` restano esattamente come furono usati; un file separato `.metadata.json` o un Registry descrive nome canonico, stato attuale, alias e correzioni.

- Vantaggi: Nessuna riscrittura storica; Meno duplicazione del contenuto.
- Svantaggi: Il singolo Markdown può continuare a mostrare un titolo storico sbagliato; Serve consultare anche i metadati.

**Q-001-D — Git come archivio storico autorevole e tree corrente essenziale** — `APPROVED`

Le versioni superate già committate vengono rimosse dal tree corrente e registrate nell'History Index con commit SHA completo e percorso storico. Il README principale collega History Index e Project Timeline. Non vengono create copie `.original.txt`.

- Vantaggi: Repository pulita e facilmente navigabile; Storia completa recuperabile tramite Git; Nessuna duplicazione degli originali; Base adatta a una futura visualizzazione step by step.
- Svantaggi: La ricostruzione completa richiede la cronologia Git; I commit SHA citati non devono essere riscritti; Gli artefatti mai committati richiedono un archivio esterno con manifest.

#### Decisione approvata: `Q-001-D`

Q-001-D — Git come archivio storico autorevole. Il tree corrente contiene soltanto documenti operativi, autorevoli o necessari come evidenza finale. Le versioni superate già presenti in Git vengono rimosse dal tree senza duplicarle e vengono registrate nell'History Index con nome, percorso, commit SHA completo, task, stato storico, documento sostitutivo e motivo della rimozione. Il README principale collega History Index e Project Timeline. Gli artefatti mai committati e non necessari restano fuori dalla repository con manifest SHA-256. I commit citati non devono essere riscritti.

#### Regole applicative

- Un solo documento corrente per famiglia in docs/00-current/.
- Nessuna copia `.original.txt` per file già conservati in Git.
- I documenti SUPERSEDED non necessari vengono rimossi dal tree dopo la catalogazione.
- Gli artefatti finali di task e le evidenze necessarie possono restare nel tree.
- Ogni documento storico rimosso deve avere commit SHA completo e percorso recuperabile.
- Il README principale contiene solo collegamenti sintetici a History Index e Project Timeline.
- I file mai committati e non necessari vengono conservati fuori dalla repository con manifest SHA-256.
- Niente force-push o riscrittura dei commit storici referenziati.

**Azioni di implementazione:** `ACT-006`, `ACT-009`, `ACT-010`, `ACT-011`, `ACT-012`, `ACT-013`, `ACT-014`, `ACT-016`, `ACT-017`, `ACT-018`, `ACT-019`, `ACT-020`, `ACT-022`, `ACT-023`, `ACT-028`

### [Q-002] Come rendere globale il metodo documentale senza modificare retroattivamente la baseline v0.1?

**Stato:** `RESOLVED`
**Decisione:** `Q-002-C`

#### Cosa significa in parole semplici

La v0.1 resta autentica e riferita a TODO-0003. Non viene riscritta facendo finta che fosse già una regola globale. Una nuova v0.2 raccoglie e formalizza, da questo momento in avanti, il metodo modulare sperimentato durante TODO-0101.

#### Perché è importante

- La storia di TODO-0003 deve restare autentica.
- Le nuove task devono avere una regola documentale comune e non ambigua.
- Il metodo di TODO-0101 ha dimostrato l'utilità di separare analisi, decisioni, checkpoint, correzioni e verifica.
- Una task semplice non deve essere costretta a produrre venti documenti.
- Ogni nuovo documento logico deve essere registrato e collegato al resto del progetto.

#### Esempio concreto

TODO-0101 ha richiesto numerosi documenti perché conteneva molte decisioni architetturali collegate. Una task semplice potrà usare solo brief, prompt, report e verifica. Una task complessa potrà aggiungere Decision Log, decisioni individuali, checkpoint e Correction Set. La logica è comune; il numero di file dipende dalla necessità reale.

#### Opzioni

**Q-002-A — Solo TODO-0003** — `NOT_SELECTED`

Il documento resta storico; per le task successive serve un nuovo standard.

- Vantaggi: Nessuna estensione retroattiva.
- Svantaggi: Manca oggi uno standard globale successivo.

**Q-002-B — TODO-0003 e tutte le task successive** — `NOT_SELECTED`

La v0.1 resta vincolante globalmente finché non viene sostituita.

- Vantaggi: Regola unica immediata.
- Svantaggi: Estende la portata oltre ciò che il testo originario dichiara.

**Q-002-C — Principi globali, dettagli TODO-0003; creare una v0.2 globale** — `APPROVED`

La v0.1 resta autentica per TODO-0003; i principi riutilizzabili confluiscono in una nuova versione globale esplicitamente approvata.

- Vantaggi: Nessuna falsificazione; Baseline futura chiara.
- Svantaggi: Richiede scrivere e approvare un nuovo documento.

#### Decisione approvata: `Q-002-C`

Q-002-C — Nuova baseline globale non retroattiva. Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md resta un documento storico legato a TODO-0003. La nuova v0.2 diventa la baseline globale corrente dalla propria approvazione in avanti. La v0.2 formalizza il metodo modulare sperimentato durante TODO-0101, ma non impone un numero fisso di documenti: ogni task attiva soltanto i moduli richiesti da complessità, rischio, decisioni e verifica.

#### Regole applicative

- La v0.1 non viene riscritta né resa retroattivamente globale.
- La v0.1 viene catalogata nell'History Index con ambito TODO-0003 e commit SHA completo.
- La v0.2 è una nuova versione integrale e autorevole.
- La v0.2 entra in vigore soltanto dalla propria approvazione o commit.
- Il metodo distingue almeno brief/task contract, prompt, analisi, decisioni, checkpoint, correzioni, report, evidenze, verifica, validazione e gate.
- Non tutti i moduli sono obbligatori per ogni task.
- L'attivazione dei moduli dipende da complessità, rischio, impatto trasversale, numero di decisioni e necessità di verifica.
- Decisioni, correzioni e finding usano identificatori stabili.
- Ogni documento dichiara versione, stato, predecessore, task e relazioni.
- Le decisioni approvate sono distinte dai documenti ancora DRAFT.
- Ogni nuovo documento logico viene registrato nel Document Registry.
- History Index e Project Timeline vengono aggiornati quando documenti o milestone cambiano.
- README principale e README di task collegano la baseline e i documenti pertinenti.
- Prima del commit sono obbligatori gate e audit finale del tree completo.

**Azioni di implementazione:** `ACT-006`, `ACT-009`, `ACT-010`, `ACT-011`, `ACT-024`, `ACT-027`, `ACT-028`

### [Q-003] Qual è il ruolo canonico di PRIVATE_CHILD?

**Stato:** `RESOLVED`
**Decisione:** `Q-003-C`

#### Cosa significa in parole semplici

PRIVATE_CHILD resta nel modello, ma non è una normale entità governata e globalmente referenziabile. È una categoria tecnica canonica che vive esclusivamente dentro un solo genitore e non possiede identità pubblica autonoma.

#### Perché è importante

- Impedisce di confondere una chiave tecnica locale con un'identità di dominio globale.
- Evita figli orfani e riferimenti esterni verso record che dovrebbero restare privati.
- Mantiene la classificazione consolidata senza equiparare PRIVATE_CHILD alle entità principali.
- Chiarisce lifecycle, cancellazione, visibilità e responsabilità del genitore.
- Esclude esplicitamente PRIVATE_CHILD da CLOSURE_REPORT e dal Global Registry.

#### Esempio concreto

Una condizione interna di una TASK può avere una chiave primaria tecnica, ma non deve essere cercata o referenziata globalmente come una TASK autonoma. Se la TASK viene eliminata o archiviata, anche la condizione deve essere gestita in modo coordinato con il genitore.

#### Opzioni

**Q-003-A — Inserirla come settima categoria canonica** — `NOT_SELECTED`

Tutti i documenti elencano PRIVATE_CHILD insieme alle altre categorie.

- Vantaggi: Coerenza con C-0101-009; Classificazione completa.
- Svantaggi: Può sembrare equivalente alle entità governate principali.

**Q-003-B — Escluderla dalle categorie canoniche** — `NOT_SELECTED`

PRIVATE_CHILD resta un dettaglio implementativo non governato come categoria.

- Vantaggi: Elenco principale più semplice.
- Svantaggi: Conflitto con la classificazione consolidata già registrata.

**Q-003-C — Categoria tecnica separata dalle categorie governate** — `APPROVED`

Il modello dichiara sei categorie governate più PRIVATE_CHILD come categoria tecnica non referenziabile globalmente.

- Vantaggi: Evita ambiguità; Preserva la classificazione consolidata.
- Svantaggi: Richiede distinguere due livelli di classificazione.

#### Decisione approvata: `Q-003-C`

Q-003-C — PRIVATE_CHILD è una categoria tecnica canonica separata dalle categorie governate e globalmente referenziabili. Ogni PRIVATE_CHILD appartiene a un solo genitore, non può esistere senza di esso, non entra nel Global Registry, non è destinazione di riferimenti globali, non possiede normalmente un lifecycle autonomo e non può possedere CLOSURE_REPORT. L'eventuale identificatore è tecnico e locale.

#### Regole applicative

- PRIVATE_CHILD appartiene obbligatoriamente a un solo genitore.
- PRIVATE_CHILD non può esistere senza il genitore.
- PRIVATE_CHILD non può cambiare genitore liberamente.
- PRIVATE_CHILD non è registrato nel Global Registry.
- PRIVATE_CHILD non può essere destinazione di riferimenti globali.
- L'eventuale ID di PRIVATE_CHILD è tecnico e locale.
- PRIVATE_CHILD non possiede normalmente un lifecycle autonomo.
- Cancellazione o archiviazione del genitore comporta gestione coordinata dei figli privati.
- PRIVATE_CHILD non può possedere CLOSURE_REPORT.
- Ogni eccezione richiede una decisione architetturale esplicita.

**Azioni di implementazione:** `ACT-009`, `ACT-010`, `ACT-025`, `ACT-027`, `ACT-028`

### [Q-004] Come viene governata l'ownership di CLOSURE_REPORT?

**Stato:** `RESOLVED`
**Decisione:** `Q-004-C`

#### Cosa significa in parole semplici

CLOSURE_REPORT non può appartenere a qualunque record con stato CLOSED e non deve dipendere da stringhe libere. Una sola allowlist autorevole e versionata stabilisce i tipi proprietari ammessi.

#### Perché è importante

- Impedisce report di chiusura per entità prive di un vero lifecycle formale.
- Mantiene il primo MVP deterministico con cinque owner type approvati.
- Evita elenchi duplicati e divergenti nel codice e nei documenti.
- Permette estensioni future senza rendere arbitrario owner_type.
- Collega ogni estensione a lifecycle, evidenze, vincoli, migrazioni e test.

#### Esempio concreto

Nel primo MVP TASK può possedere CLOSURE_REPORT perché è presente nell'allowlist. PRIVATE_CHILD non può possederlo. Una futura RELEASE potrà essere aggiunta solo dopo una decisione approvata che definisca lifecycle, criteri di chiusura, evidenze e aggiornamenti tecnici.

#### Opzioni

**Q-004-A — Qualunque entità governata che supporta CLOSED** — `NOT_SELECTED`

La regola dipende dalla capacità lifecycle dell'entità, non da una lista fissa.

- Vantaggi: Flessibile; Coerente con un transition engine.
- Svantaggi: Richiede un catalogo affidabile delle entità chiudibili.

**Q-004-B — Solo PROJECT, PHASE, WORK_ITEM, TASK e BASELINE** — `NOT_SELECTED`

Il database usa una allowlist fissa di cinque owner type.

- Vantaggi: Semplice e deterministico nel MVP.
- Svantaggi: Potrebbe richiedere migrazioni per nuovi owner type.

**Q-004-C — Allowlist versionata nel catalogo** — `APPROVED`

Il MVP parte dai cinque tipi elencati, ma la regola autorevole è una allowlist catalogata e versionata, estendibile tramite decisione.

- Vantaggi: Deterministico oggi; Estendibile senza ambiguità.
- Svantaggi: Richiede un oggetto di configurazione/catalogo in più.

#### Decisione approvata: `Q-004-C`

Q-004-C — CLOSURE_REPORT usa un'allowlist autorevole, controllata e versionata dei tipi proprietari ammessi. L'allowlist iniziale del MVP contiene PROJECT, PHASE, WORK_ITEM, TASK e BASELINE. Lo stato CLOSED non è sufficiente per entrare automaticamente nell'allowlist. PRIVATE_CHILD è escluso. Ogni estensione richiede una decisione architetturale approvata e l'aggiornamento coordinato di lifecycle, cataloghi, vincoli, documentazione, eventuali migrazioni e test.

#### Regole applicative

- CLOSURE_REPORT può appartenere soltanto a un tipo presente nell'allowlist attiva.
- L'allowlist iniziale contiene PROJECT, PHASE, WORK_ITEM, TASK e BASELINE.
- Avere lo stato CLOSED non abilita automaticamente CLOSURE_REPORT.
- PRIVATE_CHILD è escluso dall'allowlist.
- owner_type arbitrari o stringhe libere sono vietati.
- L'allowlist è autorevole, versionata e possiede una data o un commit di entrata in vigore.
- L'aggiunta di un nuovo owner type richiede una decisione architetturale approvata.
- Ogni estensione aggiorna lifecycle, criteri di chiusura, evidenze, cataloghi, vincoli, documentazione, eventuali migrazioni e test.
- Il codice e la documentazione devono dipendere dalla stessa definizione canonica.

**Azioni di implementazione:** `ACT-009`, `ACT-010`, `ACT-026`, `ACT-027`, `ACT-028`

---

## [SEC-007] Controllo individuale dei 108 Markdown

| ID | Percorso | Esito | Azioni | Decisioni | Domande aperte | Finding |
|---|---|---|---|---|---|---|
| `FILE-001` | `00-current/Project_Integrity_OS_Convenzioni_Tecniche_v0_2.md` | **PASS** | — | — | — | Documento corrente coerente con nome, posizione, versione e stato dichiarato. |
| `FILE-002` | `00-current/Project_Integrity_OS_Document_Registry_v0_7.md` | **FAIL** | ACT-005, ACT-006, ACT-007, ACT-008 | — | — | Il registro non è affidabile: cambia identificatori DOC stabili dopo le rinomine, omette DOC-027 (`.py`), usa come stato frasi estratte dal corpo e lascia quasi sempre `Sostituisce` vuoto. |
| `FILE-003` | `00-current/Project_Integrity_OS_Errata_Documentale_v0_1.md` | **FAIL** | ACT-009 | — | — | L'errata attiva non contiene i finding del controllo di secondo livello e rimanda a originali esterni al repository senza collocazione persistente nel tree. |
| `FILE-004` | `00-current/Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md` | **PASS** | — | — | — | Documento corrente coerente con nome, posizione, versione e stato dichiarato. |
| `FILE-005` | `00-current/Project_Integrity_OS_Modalita_Esecuzione_v0_1.md` | **PASS** | — | — | — | Documento corrente coerente con nome, posizione, versione e stato dichiarato. |
| `FILE-006` | `00-current/Project_Integrity_OS_Organizzazione_Documenti_v0_2.md` | **FAIL** | ACT-010 | — | — | La struttura dichiarata non coincide con il tree: README assenti per TODO-0002/TODO-0003; `superseded/` di TODO-0101 è sotto `instructions/`; la policy sugli originali non è applicata uniformemente. |
| `FILE-007` | `00-current/Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md` | **REVIEW** | ACT-024 | Q-001-D, Q-002-C | — | Q-002-C ha risolto la portata: la v0.1 resta storica e riferita a TODO-0003. ACT-024 deve catalogarla tramite Git, rimuoverla da 00-current e sostituirla con una nuova v0.2 globale non retroattiva. |
| `FILE-008` | `00-current/Project_Integrity_OS_Standard_Report_Sviluppo_v0_2.md` | **PASS** | — | — | — | Documento corrente coerente con nome, posizione, versione e stato dichiarato. |
| `FILE-009` | `00-current/Project_Integrity_OS_TODO_MVP_v0_9.md` | **PASS** | — | — | — | Documento corrente coerente con nome, posizione, versione e stato dichiarato. |
| `FILE-010` | `10-executions/TODO-0002/instructions/Project_Integrity_OS_Brief_TODO-0002_v0_3_FINAL.md` | **REVIEW** | ACT-023 | Q-001-D | — | Contenuto e stato FINAL sono coerenti, ma l'originale byte-identico è dichiarato soltanto nel pacchetto esterno, non nel repository. |
| `FILE-011` | `10-executions/TODO-0002/instructions/Project_Integrity_OS_Prompt_Esecutivo_Browser_TODO-0002_v0_1_FINAL.md` | **FAIL** | ACT-013 | Q-001-D | — | Il filename dichiara FINAL senza metadato interno FINAL; sono presenti riferimenti legacy non mappati e l'originale è soltanto esterno. |
| `FILE-012` | `10-executions/TODO-0002/instructions/Project_Integrity_OS_Start_Here_Browser_TODO-0002_v0_1_FINAL.md` | **FAIL** | ACT-014 | Q-001-D | — | Il filename dichiara FINAL senza metadato interno FINAL; la procedura cita `Project_Integrity_OS_Brief_TODO-0002.md`, file oggi inesistente, senza mappatura. |
| `FILE-013` | `10-executions/TODO-0002/instructions/closure/Project_Integrity_OS_Start_Here_Chiusura_TODO-0002_v0_1_EXECUTED.md` | **FAIL** | ACT-015 | — | — | Il filename dichiara EXECUTED senza metadato interno EXECUTED; cita `close_todo_0002.py`, mentre l'artefatto realmente registrato ha un altro nome. |
| `FILE-014` | `10-executions/TODO-0002/reports/Project_Integrity_OS_Report_Esecutivo_TODO-0002_v0_1.md` | **PASS** | — | — | — | Documento di task coerente con nome, cartella, versione e ruolo storico o operativo. |
| `FILE-015` | `10-executions/TODO-0002/reports/Project_Integrity_OS_Verifica_Indipendente_TODO-0002_v0_1.md` | **PASS** | — | — | — | Documento di task coerente con nome, cartella, versione e ruolo storico o operativo. |
| `FILE-016` | `10-executions/TODO-0002/superseded/Project_Integrity_OS_Brief_TODO-0002_v0_1_SUPERSEDED.md` | **FAIL** | ACT-016 | Q-001-D | — | Il filename dichiara SUPERSEDED senza metadato interno SUPERSEDED. |
| `FILE-017` | `10-executions/TODO-0002/superseded/Project_Integrity_OS_Brief_TODO-0002_v0_2_SUPERSEDED.md` | **FAIL** | ACT-017 | Q-001-D | — | Contraddizione diretta: il filename dichiara SUPERSEDED, ma il contenuto dichiara `Stato: CORRENTE`. |
| `FILE-018` | `10-executions/TODO-0002/superseded/Project_Integrity_OS_Prompt_Esecutivo_Desktop_TODO-0002_v0_1_SUPERSEDED.md` | **FAIL** | ACT-018 | Q-001-D | — | Il filename dichiara SUPERSEDED senza metadato interno; la vista normalizzata lascia riferimenti legacy non risolti. |
| `FILE-019` | `10-executions/TODO-0002/superseded/Project_Integrity_OS_Start_Here_Desktop_TODO-0002_v0_1_SUPERSEDED.md` | **FAIL** | ACT-018 | Q-001-D | — | Il filename dichiara SUPERSEDED senza metadato interno e l'identità documentale è incompleta. |
| `FILE-020` | `10-executions/TODO-0002/validation/approvals/Project_Integrity_OS_Approvazione_Umana_TODO-0002_v0_1.md` | **PASS** | — | — | — | Documento di task coerente con nome, cartella, versione e ruolo storico o operativo. |
| `FILE-021` | `10-executions/TODO-0002/validation/exceptions/Project_Integrity_OS_Deviazione_DEV-TODO-0002-001_v0_1.md` | **PASS** | — | — | — | Documento di task coerente con nome, cartella, versione e ruolo storico o operativo. |
| `FILE-022` | `10-executions/TODO-0003/instructions/Project_Integrity_OS_Prompt_Esecutivo_Browser_TODO-0003_v0_1.md` | **PASS** | — | — | — | Documento di task coerente con nome, cartella, versione e ruolo storico o operativo. |
| `FILE-023` | `10-executions/TODO-0003/reports/Project_Integrity_OS_Report_Esecutivo_TODO-0003_v0_1.md` | **FAIL** | ACT-019 | Q-001-D | — | Mancano titolo H1 e metadati minimi di identità/versione/stato; il file inizia direttamente con `## ESITO DICHIARATO`. |
| `FILE-024` | `10-executions/TODO-0003/reports/Project_Integrity_OS_Verifica_Indipendente_TODO-0003_v0_1.md` | **PASS** | — | — | — | Documento di task coerente con nome, cartella, versione e ruolo storico o operativo. |
| `FILE-025` | `10-executions/TODO-0003/validation/approvals/Project_Integrity_OS_Approvazione_Umana_TODO-0003_v0_1.md` | **PASS** | — | — | — | Documento di task coerente con nome, cartella, versione e ruolo storico o operativo. |
| `FILE-026` | `10-executions/TODO-0003/validation/notes/Project_Integrity_OS_Nota_Post_Chiusura_TODO-0003_v0_1.md` | **PASS** | — | — | — | Documento di task coerente con nome, cartella, versione e ruolo storico o operativo. |
| `FILE-027` | `10-executions/TODO-0101/README.md` | **REVIEW** | ACT-027 | — | — | Dichiara `main` come branch autorevole, mentre la normalizzazione documentale è ancora non committata sul branch review. Occorre distinguere baseline 382c96f e audit pending. |
| `FILE-028` | `10-executions/TODO-0101/analysis/checkpoints/Project_Integrity_OS_Checkpoint_Index_TODO-0101_v0_8_DRAFT.md` | **REVIEW** | ACT-027 | — | — | Dichiara checkpoint successivo all'audit documentale; l'audit v0.1 deve invece essere superseded e il tree di audit non è ancora integrato. |
| `FILE-029` | `10-executions/TODO-0101/analysis/checkpoints/history/Project_Integrity_OS_Checkpoint_Index_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-030` | `10-executions/TODO-0101/analysis/checkpoints/history/Project_Integrity_OS_Checkpoint_Index_TODO-0101_v0_3_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-031` | `10-executions/TODO-0101/analysis/checkpoints/history/Project_Integrity_OS_Checkpoint_Index_TODO-0101_v0_4_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-032` | `10-executions/TODO-0101/analysis/checkpoints/history/Project_Integrity_OS_Checkpoint_Index_TODO-0101_v0_5_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-033` | `10-executions/TODO-0101/analysis/checkpoints/history/Project_Integrity_OS_Checkpoint_Index_TODO-0101_v0_6_DRAFT.md` | **REVIEW** | — | Q-001-D | — | La vista storica normalizzata è leggibile, ma l'originale dichiarato come `.original.txt` non è nel repository. Serve una scelta di conservazione persistente. |
| `FILE-034` | `10-executions/TODO-0101/analysis/checkpoints/history/Project_Integrity_OS_Checkpoint_Index_TODO-0101_v0_7_DRAFT.md` | **REVIEW** | — | Q-001-D | — | La vista storica normalizzata è leggibile, ma l'originale dichiarato come `.original.txt` non è nel repository. Serve una scelta di conservazione persistente. |
| `FILE-035` | `10-executions/TODO-0101/analysis/decision-log/Project_Integrity_OS_Decision_Log_TODO-0101_v0_8_DRAFT.md` | **REVIEW** | ACT-027 | — | — | La separazione tra decisioni di analisi e schema fisico non approvato è corretta, ma il documento incorpora come completato un audit che non è valido. |
| `FILE-036` | `10-executions/TODO-0101/analysis/decision-log/history/Project_Integrity_OS_Decision_Log_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-037` | `10-executions/TODO-0101/analysis/decision-log/history/Project_Integrity_OS_Decision_Log_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-038` | `10-executions/TODO-0101/analysis/decision-log/history/Project_Integrity_OS_Decision_Log_TODO-0101_v0_3_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-039` | `10-executions/TODO-0101/analysis/decision-log/history/Project_Integrity_OS_Decision_Log_TODO-0101_v0_4_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-040` | `10-executions/TODO-0101/analysis/decision-log/history/Project_Integrity_OS_Decision_Log_TODO-0101_v0_5_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-041` | `10-executions/TODO-0101/analysis/decision-log/history/Project_Integrity_OS_Decision_Log_TODO-0101_v0_6_DRAFT.md` | **REVIEW** | — | Q-001-D | — | La vista storica normalizzata è leggibile, ma l'originale dichiarato come `.original.txt` non è nel repository. Serve una scelta di conservazione persistente. |
| `FILE-042` | `10-executions/TODO-0101/analysis/decision-log/history/Project_Integrity_OS_Decision_Log_TODO-0101_v0_7_DRAFT.md` | **FAIL** | ACT-021 | Q-001-D | — | Il campo `Versione precedente` usa `history/...` pur essendo già dentro `history/`, generando concettualmente `history/history/...`. |
| `FILE-043` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_01_Principi_Tracciabilita_Contesto_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | — | — | Documento decisionale ordinato e coerente con la catena di versione; nessun conflitto certo rilevato. |
| `FILE-044` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_02_Modello_Gerarchico_Contesto_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | — | — | Documento decisionale ordinato e coerente con la catena di versione; nessun conflitto certo rilevato. |
| `FILE-045` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_03_Context_Package_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | — | — | Documento decisionale ordinato e coerente con la catena di versione; nessun conflitto certo rilevato. |
| `FILE-046` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_04_Provenienza_Informazioni_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | — | — | Documento decisionale ordinato e coerente con la catena di versione; nessun conflitto certo rilevato. |
| `FILE-047` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_05_Sintesi_Drill_Down_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | — | — | Documento decisionale ordinato e coerente con la catena di versione; nessun conflitto certo rilevato. |
| `FILE-048` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_06_Requisiti_Test_Tracciabilita_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | — | — | Documento decisionale ordinato e coerente con la catena di versione; nessun conflitto certo rilevato. |
| `FILE-049` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_07_Lifecycle_Decisioni_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | — | — | Documento decisionale ordinato e coerente con la catena di versione; nessun conflitto certo rilevato. |
| `FILE-050` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_08_Registro_Elementi_Irrisolti_TODO-0101_v0_3_DRAFT.md` | **PASS** | — | — | — | Documento decisionale ordinato e coerente con la catena di versione; nessun conflitto certo rilevato. |
| `FILE-051` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_09_Eventi_Ricostruzione_Temporale_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | — | — | Documento decisionale ordinato e coerente con la catena di versione; nessun conflitto certo rilevato. |
| `FILE-052` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_10_Integrita_Trasversale_Anti_Orfano_TODO-0101_v0_3_DRAFT.md` | **REVIEW** | ACT-025 | Q-003-C | — | Q-003-C ha risolto la classificazione: PRIVATE_CHILD deve essere descritto come categoria tecnica canonica separata, privata, dipendente dal genitore e non globalmente referenziabile. ACT-025 deve aggiornare questo documento, Correction Set e Decision Log. |
| `FILE-053` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_11_Conservazione_Rettifiche_Cancellazione_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | — | — | Documento decisionale ordinato e coerente con la catena di versione; nessun conflitto certo rilevato. |
| `FILE-054` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_12_Ruoli_Permessi_Sensibilita_Redazione_TODO-0101_v0_3_DRAFT.md` | **PASS** | — | — | — | Documento decisionale ordinato e coerente con la catena di versione; nessun conflitto certo rilevato. |
| `FILE-055` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_13_Transizioni_Condizioni_Complete_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | — | — | Documento decisionale ordinato e coerente con la catena di versione; nessun conflitto certo rilevato. |
| `FILE-056` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_14_Cardinalita_Tabelle_Associative_TODO-0101_v0_3_DRAFT.md` | **REVIEW** | ACT-026 | Q-004-C | — | Q-004-C ha risolto l'ownership: CLOSURE_REPORT deve usare una allowlist autorevole e versionata, inizialmente limitata a PROJECT, PHASE, WORK_ITEM, TASK e BASELINE. ACT-026 deve aggiornare questo documento, Correction Set e Decision Log. |
| `FILE-057` | `10-executions/TODO-0101/analysis/decisions/Project_Integrity_OS_15_Schema_Completo_Implementazione_Progressiva_TODO-0101_v0_3_DRAFT.md` | **PASS** | — | — | — | Documento decisionale ordinato e coerente con la catena di versione; nessun conflitto certo rilevato. |
| `FILE-058` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_01_Principi_Tracciabilita_Contesto_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-059` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_02_Modello_Gerarchico_Contesto_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-060` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_03_Context_Package_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-061` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_04_Provenienza_Informazioni_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-062` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_05_Sintesi_Drill_Down_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-063` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_06_Requisiti_Test_Tracciabilita_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-064` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_07_Lifecycle_Decisioni_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-065` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_08_Registro_Elementi_Irrisolti_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-066` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_08_Registro_Elementi_Irrisolti_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-067` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_09_Eventi_Ricostruzione_Temporale_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-068` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_10_Integrita_Trasversale_Anti_Orfano_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-069` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_10_Integrita_Trasversale_Anti_Orfano_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-070` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_11_Conservazione_Rettifiche_Cancellazione_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-071` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_12_Ruoli_Permessi_Sensibilita_Redazione_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-072` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_12_Ruoli_Permessi_Sensibilita_Redazione_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-073` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_13_Transizioni_Condizioni_Complete_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-074` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_14_Cardinalita_Tabelle_Associative_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-075` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_14_Cardinalita_Tabelle_Associative_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-076` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_15_Schema_Completo_Implementazione_Progressiva_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-077` | `10-executions/TODO-0101/analysis/decisions/history/Project_Integrity_OS_15_Schema_Completo_Implementazione_Progressiva_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-078` | `10-executions/TODO-0101/analysis/verification/Project_Integrity_OS_Audit_Documentale_TODO-0101_v0_1.md` | **FAIL** | ACT-027 | — | — | La conclusione FINAL non è sostenibile: non rileva la cancellazione dell'artefatto `.py`, i difetti del Registry, le contraddizioni di stato e le divergenze strutturali. |
| `FILE-079` | `10-executions/TODO-0101/analysis/verification/Project_Integrity_OS_Correction_Set_TODO-0101_v0_2_DRAFT.md` | **PASS** | — | — | — | Documento di analisi ordinato e coerente con la relativa famiglia e versione. |
| `FILE-080` | `10-executions/TODO-0101/analysis/verification/Project_Integrity_OS_Open_Issues_Register_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | — | — | Documento di analisi ordinato e coerente con la relativa famiglia e versione. |
| `FILE-081` | `10-executions/TODO-0101/analysis/verification/history/Project_Integrity_OS_Correction_Set_TODO-0101_v0_1_DRAFT.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-082` | `10-executions/TODO-0101/instructions/superseded/Project_Integrity_OS_Brief_TODO-0101_v0_1_SUPERSEDED.md` | **REVIEW** | ACT-012, ACT-022 | Q-001-D | — | È correttamente non eseguibile, ma descrive come corrente Decision Log v0.7; ora esiste v0.8. Va definito se resta snapshot o se serve un wrapper successivo. |
| `FILE-083` | `10-executions/TODO-0101/instructions/superseded/history/Project_Integrity_OS_Brief_TODO-0101_v0_1_DRAFT_ORIGINAL.md` | **FAIL** | ACT-012, ACT-022 | Q-001-D | — | Duplica nel tree la stessa identità/versione v0.1 del brief superseded e contraddice la policy che colloca gli originali fuori dai Markdown correnti. |
| `FILE-084` | `20-history/analysis/Project_Integrity_OS_Modello_Informativo_Pre-TODO-0003_v0_1.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-085` | `20-history/concept/Project_Integrity_OS_Concetto_Integrita_Continuita_v0_1_SUPERSEDED.md` | **REVIEW** | ACT-020 | Q-001-D | — | Nome ordinabile e versione corretta, ma manca il metadato interno esplicito `Stato: SUPERSEDED`; l'originale legacy è soltanto nel pacchetto esterno. |
| `FILE-086` | `20-history/concept/Project_Integrity_OS_Concetto_Integrita_Continuita_v0_2_SUPERSEDED.md` | **REVIEW** | ACT-020 | Q-001-D | — | Nome ordinabile e versione corretta, ma manca il metadato interno esplicito `Stato: SUPERSEDED`; l'originale legacy è soltanto nel pacchetto esterno. |
| `FILE-087` | `20-history/concept/Project_Integrity_OS_Concetto_Integrita_Continuita_v0_3_SUPERSEDED.md` | **REVIEW** | ACT-020 | Q-001-D | — | Nome ordinabile e versione corretta, ma manca il metadato interno esplicito `Stato: SUPERSEDED`; l'originale legacy è soltanto nel pacchetto esterno. |
| `FILE-088` | `20-history/concept/Project_Integrity_OS_Concetto_Integrita_Continuita_v0_4_SUPERSEDED.md` | **REVIEW** | ACT-020 | Q-001-D | — | Nome ordinabile e versione corretta, ma manca il metadato interno esplicito `Stato: SUPERSEDED`; l'originale legacy è soltanto nel pacchetto esterno. |
| `FILE-089` | `20-history/concept/Project_Integrity_OS_Concetto_Integrita_Continuita_v0_5_SUPERSEDED.md` | **REVIEW** | ACT-020 | Q-001-D | — | Nome ordinabile e versione corretta, ma manca il metadato interno esplicito `Stato: SUPERSEDED`; l'originale legacy è soltanto nel pacchetto esterno. |
| `FILE-090` | `20-history/concept/Project_Integrity_OS_Concetto_Integrita_Continuita_v0_6_SUPERSEDED.md` | **REVIEW** | ACT-020 | Q-001-D | — | Nome ordinabile e versione corretta, ma manca il metadato interno esplicito `Stato: SUPERSEDED`; l'originale legacy è soltanto nel pacchetto esterno. |
| `FILE-091` | `20-history/document-organization/Project_Integrity_OS_Organizzazione_Documenti_v0_1.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-092` | `20-history/flows/Project_Integrity_OS_Flussi_MVP_v0_1.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-093` | `20-history/registry/Project_Integrity_OS_Document_Registry_v0_1.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-094` | `20-history/registry/Project_Integrity_OS_Document_Registry_v0_2.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-095` | `20-history/registry/Project_Integrity_OS_Document_Registry_v0_3.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-096` | `20-history/registry/Project_Integrity_OS_Document_Registry_v0_4.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-097` | `20-history/registry/Project_Integrity_OS_Document_Registry_v0_5.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-098` | `20-history/registry/Project_Integrity_OS_Document_Registry_v0_6.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-099` | `20-history/report-standards/Project_Integrity_OS_Standard_Report_Sviluppo_v0_1.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-100` | `20-history/technical-conventions/Project_Integrity_OS_Convenzioni_Tecniche_v0_1.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-101` | `20-history/todo/Project_Integrity_OS_TODO_MVP_v0_1.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-102` | `20-history/todo/Project_Integrity_OS_TODO_MVP_v0_2.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-103` | `20-history/todo/Project_Integrity_OS_TODO_MVP_v0_3.md` | **REVIEW** | — | Q-001-D | — | La vista storica normalizzata è leggibile, ma l'originale dichiarato come `.original.txt` non è nel repository. Serve una scelta di conservazione persistente. |
| `FILE-104` | `20-history/todo/Project_Integrity_OS_TODO_MVP_v0_4.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-105` | `20-history/todo/Project_Integrity_OS_TODO_MVP_v0_5.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-106` | `20-history/todo/Project_Integrity_OS_TODO_MVP_v0_6.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-107` | `20-history/todo/Project_Integrity_OS_TODO_MVP_v0_7.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |
| `FILE-108` | `20-history/todo/Project_Integrity_OS_TODO_MVP_v0_8.md` | **PASS** | — | Q-001-D | — | Snapshot storico coerente con nome, posizione e versione; nessuna incongruenza attiva rilevata. |

---

## [SEC-008] Gate di commit

### [GATE-001] Stato

- **Ulteriori commit consentiti:** NO
- **Eccezione già registrata:** `2f3c7f9`
- **Motivo:** Il checkpoint 2f3c7f9 è già stato pubblicato esclusivamente per conservare il piano v0.4. Non autorizza ulteriori commit, pull request o merge. Le azioni ACT-002...ACT-028 non sono ancora completate.

Un nuovo commit, una pull request o un merge potranno essere valutati soltanto quando:

- [ ] ACT-002 completata con verifica e SHA-256 del backup
- [ ] ACT-003 completata con reintegro byte-identico di DOC-027
- [ ] ACT-004 completata con inventario di tutti gli artefatti non Markdown
- [ ] Q-001-D applicata integralmente
- [ ] Q-002-C applicata integralmente
- [ ] Q-003-C applicata integralmente
- [ ] Q-004-C applicata integralmente
- [ ] ACT-005...ACT-028 completate
- [ ] History Index e Project Timeline verificati
- [ ] Baseline Prompt/Report/Rule Catalog v0.2 verificata
- [ ] PRIVATE_CHILD coerente in tutti i documenti e cataloghi
- [ ] Allowlist CLOSURE_REPORT coerente e versionata
- [ ] Audit v0.2 FINAL
- [ ] zero FAIL
- [ ] zero questioni aperte
- [ ] autorizzazione esplicita dell’utente a un nuovo commit o merge

---

## [SEC-009] Stato delle decisioni e dell’esecuzione

1. `Q-001-D` — approvata e incorporata nel piano.
2. `Q-002-C` — approvata e incorporata nel piano.
3. `Q-003-C` — approvata e incorporata nel piano.
4. `Q-004-C` — approvata e incorporata nel piano.
5. Non restano domande di governance aperte.
6. Il checkpoint `2f3c7f9` è pubblicato sul branch di revisione e contiene soltanto i due file del piano.
7. Il checkpoint non autorizza una pull request, un merge o ulteriori commit.
8. La prossima esecuzione deve completare `ACT-002`, `ACT-003` e `ACT-004`.

---

## [SEC-010] Prossima task

**ID:** `NEXT-002`
**Titolo:** Completare ACT-002, ACT-003 e ACT-004
**Stato:** `READY`
**Azioni:** `ACT-002`, `ACT-003`, `ACT-004`

Verificare backup e quarantena, registrare lo SHA-256 del backup, inventariare tutti gli artefatti non Markdown del commit base e reintegrare esclusivamente quelli mancanti senza sovrascrivere file differenti.

### Ordine operativo

1. Verificare esistenza e leggibilità di backup e quarantena.
2. Calcolare e registrare lo SHA-256 del backup.
3. Reintegrare byte-identico lo script Python DOC-027 dal commit base.
4. Inventariare tutti i file sotto docs che non terminano in .md nel commit base.
5. Classificare ogni file come identico, mancante o differente.
6. Reintegrare soltanto i file mancanti.
7. Produrre un report finale senza commit e senza push.

### Campi obbligatori del report finale

- commit base controllato
- SHA-256 del backup
- numero totale di file non Markdown
- file presenti e identici
- file mancanti
- file reintegrati
- file presenti ma differenti
- hash o blob dei file reintegrati
- file sovrascritti
- commit
- push
- limiti o elementi non verificati

### Operazioni vietate durante questa task

- modificare il Document Registry
- correggere i Markdown del secondo livello
- rimuovere documenti superseded
- creare History Index o Project Timeline
- aprire pull request
- creare nuovi commit
- eseguire push
- fare merge in main
