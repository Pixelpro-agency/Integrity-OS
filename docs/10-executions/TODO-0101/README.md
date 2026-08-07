# Project Integrity OS — TODO-0101

## Archivio dell’analisi e indice dei documenti collegati

**Task:** `TODO-0101 — Definire schema dati minimo`
**Stato:** `IN_ANALYSIS`
**Implementazione SQLite:** `NON INIZIATA`
**Decisioni consolidate:** `DEC-0101-001` → `DEC-0101-020`
**Brief esecutivo corrente:** `NON DISPONIBILE`
**TODO-0101 READY:** `NO`

---

## 1. Funzione di questa cartella

Questa cartella conserva la traccia storica e operativa dell’analisi svolta per TODO-0101.

Durante la task sono state prodotte decisioni che non appartengono soltanto alla singola esecuzione, ma arricchiscono l’architettura generale di Project Integrity OS. Per questo motivo i documenti decisionali non sono conservati qui come allegati della task: sono stati collocati nella documentazione globale del repository.

La separazione corretta è:

```text
docs/10-executions/TODO-0101/
→ storia, checkpoint, brief superato e audit della task

docs/architecture/data-model/
→ decisioni architetturali globali nate durante TODO-0101

docs/planning/
→ elementi aperti che dovranno alimentare Implementazioni e To-Do
```

TODO-0101 non ha ancora prodotto lo schema fisico definitivo, i cataloghi finali, le matrici richieste o un brief esecutivo approvato.

---

## 2. Documentazione globale collegata

### Architettura del modello dati

Percorso:

```text
docs/architecture/data-model/
```

Dalla posizione di questo README:

```text
../../architecture/data-model/README.md
```

La cartella contiene:

- il Decision Log corrente;
- i quindici documenti decisionali correnti;
- le versioni storiche delle decisioni;
- le versioni storiche del Decision Log;
- i Correction Set usati durante il consolidamento.

I documenti sotto `current/` restano `DRAFT`: costituiscono input consolidato, ma non autorizzano direttamente l’implementazione e non rappresentano ancora lo schema fisico autorevole.

### Elementi aperti di pianificazione

Percorso:

```text
docs/planning/Project_Integrity_OS_Open_Issues_Data_Model_v0_1_DRAFT.md
```

Dalla posizione di questo README:

```text
../../planning/Project_Integrity_OS_Open_Issues_Data_Model_v0_1_DRAFT.md
```

Questo registro è una fonte di lavoro. Gli elementi ancora aperti dovranno essere tradotti successivamente:

- nel file globale delle Implementazioni;
- nella To-Do operativa aggiornata;
- nei deliverable finali di architettura;
- nelle task esecutive successive.

Non deve essere interpretato come una To-Do definitiva già approvata.

---

## 3. Contenuto della cartella TODO-0101

### `01-brief-superato/`

Contiene:

- il brief originale completo;
- la vista che lo dichiara `SUPERSEDED`.

Entrambi i file sono storici.

```text
DO_NOT_EXECUTE
```

Non devono essere utilizzati per avviare un’implementazione SQLite.

### `02-checkpoint/`

Contiene il checkpoint corrente dell’analisi:

```text
TODO-0101_Checkpoint_Finale_Analisi_v0_12_DRAFT.md
```

È il documento principale per ricostruire il punto in cui il lavoro si è fermato e i deliverable ancora pendenti.

### `03-verifica-documentale/`

Contiene l’audit della riorganizzazione documentale.

Audit corrente:

- [TODO-0101 Audit Documentale v0.3](03-verifica-documentale/TODO-0101_Audit_Documentale_v0_3_FINAL.md)

L’audit dimostra e descrive il riordino eseguito, ma non è un deliverable funzionale o architetturale dello schema dati.

### `90-history/`

Contiene:

- i checkpoint precedenti;
- il README originale dello ZIP sorgente.

Questi documenti servono soltanto per ricostruzione storica, confronto e audit. Non devono essere usati come stato corrente della task.

---

## 4. Ordine di lettura

Per riprendere il lavoro su TODO-0101:

1. leggere `02-checkpoint/TODO-0101_Checkpoint_Finale_Analisi_v0_12_DRAFT.md`;
2. leggere `../../architecture/data-model/README.md`;
3. consultare `../../architecture/data-model/current/Project_Integrity_OS_Decision_Log_Data_Model_v0_9_DRAFT.md`;
4. leggere, secondo necessità, i documenti numerati `01` → `15` sotto `../../architecture/data-model/current/`;
5. consultare `../../planning/Project_Integrity_OS_Open_Issues_Data_Model_v0_1_DRAFT.md`;
6. leggere `01-brief-superato/TODO-0101_Brief_v0_1_SUPERSEDED.md` soltanto per comprendere perché il vecchio brief non è più eseguibile;
7. usare `90-history/` soltanto quando serve ricostruire l’evoluzione documentale.

---

## 5. Deliverable ancora necessari

Prima che TODO-0101 possa diventare `READY`, restano da produrre, verificare e approvare:

1. Schema Architecture;
2. Entity Catalog;
3. Data Dictionary;
4. Relationship Matrix;
5. Constraint Catalog;
6. State and Transition Catalog;
7. Portability Matrix;
8. Implementation Wave Matrix;
9. file globale delle Implementazioni aggiornato;
10. To-Do operativa aggiornata;
11. brief esecutivo finale;
12. baseline finale congelata e approvata.

Le decisioni già raccolte devono alimentare questi documenti, non essere copiate integralmente dentro Implementazioni o To-Do.

---

## 6. File di controllo presenti nella radice della task

### `FILE_MAP.csv`

Registra la tracciabilità dei 57 file provenienti dallo ZIP originale e dei documenti derivati creati durante il refactor.

Per ogni riga sono disponibili:

- tipo di origine;
- percorso sorgente, quando applicabile;
- percorso corrente nel repository;
- ruolo documentale;
- stato corrente o storico;
- `source_sha256`;
- `current_sha256`;
- `change_type`;
- riferimento di provenienza;
- nota interpretativa.

Il file non usa più una dichiarazione indiscriminata di preservazione byte per byte: ogni documento esplicita il proprio tipo di modifica.

### `manifest.json`

Descrive in forma strutturata:

- stato di TODO-0101;
- regole della riorganizzazione;
- collocazione dei documenti globali e dei documenti della task;
- tracciabilità dei 57 file originari;
- documenti derivati prodotti durante il refactor;
- hash sorgente e hash correnti;
- tipo di modifica applicata;
- file di controllo generati;
- ordine consigliato di lettura.

I percorsi registrati sono riferiti alla radice del repository.

### `MANIFEST_SHA256.txt`

Contiene i checksum dei documenti interessati dalla riorganizzazione e dei file di controllo, usando i percorsi reali sotto `docs/`.

Il file non contiene il checksum di se stesso.

### `SOURCE_ARCHIVE_SHA256.txt`

Registra il checksum dello ZIP sorgente originale:

```text
TODO-0101.zip
```

---

## 7. Regole operative

1. Non eseguire i brief presenti in `01-brief-superato/`.
2. Non considerare i documenti architetturali `DRAFT` come autorizzazione a implementare.
3. Non riportare dentro questa cartella copie duplicate dei documenti globali.
4. Usare il Decision Log come indice delle decisioni.
5. Trasformare gli open issue in Implementazioni, To-Do o deliverable finali prima di chiuderli.
6. Conservare le versioni storiche soltanto per ricostruzione e audit.
7. Aggiornare `FILE_MAP.csv`, `manifest.json` e `MANIFEST_SHA256.txt` quando cambiano collocazione, contenuto editoriale o lineage dei file mappati.
8. I file di controllo sono stati rigenerati al termine del ciclo documentale TODO-0004 → TODO-0012; da questo punto devono essere mantenuti sincronizzati con le modifiche future.

---

## 8. Blocco operativo corrente

```text
DO_NOT_EXECUTE
TODO-0101_READY: NO
IMPLEMENTATION_STARTED: NO
```

La task potrà diventare eseguibile soltanto dopo la produzione dei deliverable finali, l’aggiornamento di Implementazioni e To-Do, la riscrittura del brief e l’approvazione della nuova baseline.

---

## 9. Provenienza

Archivio sorgente: `TODO-0101.zip`
SHA-256 archivio sorgente: `7f944468ac180558b50940dda5b46681a5fe4c5a59e408b5e90a2cba90e0cc79`


---

## Collegamenti negli snapshot storici

> I collegamenti presenti nei documenti sotto `90-history` riflettono la struttura storica originaria e possono non essere risolvibili nel tree corrente.

Gli snapshot storici non vengono corretti retroattivamente. La verifica dei collegamenti operativi riguarda i documenti correnti.
