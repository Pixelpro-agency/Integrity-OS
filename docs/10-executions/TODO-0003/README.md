# Project Integrity OS — TODO-0003

## Archivio organizzato della task

**Task:** `TODO-0003 — Definire convenzioni tecniche e qualità`  
**Stato finale:** `DONE`  
**Modalità realmente usata:** `BROWSER_OPERATOR_ASSISTED`  
**Tentativi utilizzati:** `1`  
**Esito dichiarato dall’esecutore:** `SUCCESS`  
**Verifica indipendente:** `PASSED`  
**Approvazione umana:** `APPROVED`  
**Commit di chiusura osservato:** `e33bab77c5032c0aefdbf18fb2cde1afd2a5ea9d`  
**Push autorizzato all’assistente:** `NO`  
**Push successivamente eseguito dall’utente:** osservato su `origin/main`  
**Correzione documentale post-chiusura:** `COMPLETED`

---

## 1. Scopo di questo pacchetto

Questo archivio riorganizza i cinque artefatti autentici di TODO-0003 senza riscriverne retroattivamente il contenuto.

I documenti originali sono stati:

- conservati integralmente;
- copiati byte per byte;
- rinominati secondo la funzione reale;
- collocati nell’ordine cronologico e logico di lettura;
- descritti in `manifest.json` e `FILE_MAP.csv`;
- protetti da checksum SHA-256.

La riorganizzazione non modifica decisioni, risultati, date, dichiarazioni o prove storiche.

---

## 2. Ordine obbligatorio di lettura

### 1. `01-esecuzione-effettiva/`

Contiene il prompt realmente consegnato alla chat esecutiva.

Leggerlo per ricostruire:

- obiettivo e scope della task;
- modalità browser con operatore umano;
- vincoli tecnici e documentali;
- controlli e output richiesti.

**Avvertenza:** è un prompt storico. Non deve essere rieseguito né riutilizzato direttamente come modello per una task futura, perché contiene precondizioni, allegati e riferimenti validi nello stato del progetto del 5 agosto 2026.

### 2. `02-risultato-esecutore/`

Contiene il report originale/raw restituito dall’esecutore al termine del tentativo.

Deve essere letto come dichiarazione dell’esecutore. Il valore `SUCCESS` significa che il lavoro veniva proposto per la verifica indipendente; non significa che la task fosse già `DONE`.

### 3. `03-verifica-indipendente/`

Contiene i controlli tecnici osservati, le correzioni richieste durante la verifica e l’esito `PASSED`.

Questo documento è autorevole per:

- esito di `npm run verify`;
- test frontend e Rust osservati;
- confronto tra report e working tree;
- rispetto dello scope;
- raccomandazione `READY_FOR_HUMAN_REVIEW`.

### 4. `04-approvazione-umana/`

Contiene la decisione umana che autorizza:

- chiusura documentale;
- aggiornamento di To-Do e Document Registry;
- archiviazione delle versioni sostituite;
- creazione del commit locale.

Non autorizza l’assistente a eseguire il push.

### 5. `05-post-chiusura/`

Contiene la correzione documentale successiva alla chiusura ed è una lettura obbligatoria per interpretare correttamente l’intero pacchetto.

Chiarisce che:

- la task resta `DONE`;
- non è stato modificato codice nella correzione;
- il prompt rimane autentico ma non riutilizzabile automaticamente;
- il report resta il testo originale/raw;
- Convenzioni tecniche v0.1 e Standard report v0.1 sono stati sostituiti dalle versioni v0.2;
- il commit locale era autorizzato;
- il push non era autorizzato all’assistente;
- il push è stato poi eseguito materialmente dall’utente.

---

## 3. Flusso reale della task

```text
Prompt realmente usato
        ↓
Tentativo 1
        ↓
Report originale dell’esecutore: SUCCESS
        ↓
Verifica indipendente: PASSED
        ↓
Approvazione umana: APPROVED
        ↓
Commit locale di chiusura
        ↓
Push eseguito dall’utente
        ↓
Correzione documentale post-chiusura
        ↓
Stato finale: DONE
```

Le seguenti condizioni non sono equivalenti:

```text
SUCCESS del report
≠ PASSED della verifica
≠ APPROVED dell’utente
≠ DONE della task
```

---

## 4. Struttura dell’archivio

```text
TODO-0003_ORGANIZZATO/
├── README.md
├── FILE_MAP.csv
├── manifest.json
├── MANIFEST_SHA256.txt
├── SOURCE_ARCHIVE_SHA256.txt
├── 01-esecuzione-effettiva/
├── 02-risultato-esecutore/
├── 03-verifica-indipendente/
├── 04-approvazione-umana/
└── 05-post-chiusura/
```

Non sono state create cartelle storiche vuote: nel pacchetto originario non erano presenti brief sostituiti, prompt alternativi o varianti non utilizzate.

---

## 5. Documenti globali collegati ma non duplicati

TODO-0003 ha prodotto o aggiornato baseline globali che non vengono duplicate in questo archivio della task:

```text
Project_Integrity_OS_Convenzioni_Tecniche_v0_1.md
Project_Integrity_OS_Convenzioni_Tecniche_v0_2.md
Project_Integrity_OS_Standard_Report_Sviluppo_v0_1.md
Project_Integrity_OS_Standard_Report_Sviluppo_v0_2.md
Project_Integrity_OS_TODO_MVP_v0_7.md
Project_Integrity_OS_TODO_MVP_v0_8.md
Project_Integrity_OS_Document_Registry_v0_5.md
Project_Integrity_OS_Document_Registry_v0_6.md
```

Le versioni v0.2 delle convenzioni tecniche e dello standard report costituiscono l’interpretazione corrente successiva alla correzione post-chiusura. I relativi file globali devono essere conservati nella documentazione generale del progetto, non copiati dentro ogni archivio di task.

---

## 6. File di controllo

### `FILE_MAP.csv`

Mappa per ogni artefatto:

- posizione originale;
- posizione normalizzata;
- ruolo;
- stato;
- utilizzo reale;
- sicurezza di riuso o riesecuzione;
- checksum.

### `manifest.json`

Descrive la task e i documenti in forma strutturata, predisposta per una futura importazione in Project Integrity OS.

### `MANIFEST_SHA256.txt`

Contiene il checksum SHA-256 di tutti i file presenti nel pacchetto organizzato, escluso il file stesso.

### `SOURCE_ARCHIVE_SHA256.txt`

Registra il checksum dello ZIP sorgente usato per creare questa versione organizzata.

---

## 7. Regole per l’uso futuro

1. Non eseguire nuovamente il prompt.
2. Non correggere retroattivamente il report originale.
3. Non usare il report come prova sufficiente.
4. Leggere sempre verifica, approvazione e correzione post-chiusura.
5. Non confondere autorizzazione al commit con autorizzazione al push.
6. Non duplicare dentro la task le baseline globali del progetto.
7. Usare `manifest.json` per una futura importazione automatica.
8. Verificare i checksum prima di usare il pacchetto come fonte storica.

---

## 8. Provenienza

Archivio sorgente: `TODO-0003.zip`  
SHA-256 archivio sorgente: `2356519e2fe854a8d0293dba53f1cdd2af2b3bdf705a0b70b58e267d3676a134`
