# Project Integrity OS
## Organizzazione dei documenti — v0.1

**Stato:** proposta operativa approvabile  
**Obiettivo:** conservare l’intera evoluzione del progetto senza confondere documenti correnti, storici, esecutivi ed evidenze.

---

## 1. Principio

Tutti i documenti devono essere conservati, ma non devono restare mescolati nella cartella principale.

Ogni file deve appartenere a una delle seguenti categorie:

1. **CURRENT** — fonte autorevole attuale;
2. **EXECUTION** — materiale operativo relativo a una task;
3. **EVIDENCE** — prove raccolte durante esecuzione, verifica e collaudo;
4. **HISTORY** — versioni precedenti e documenti superati;
5. **REGISTRY** — indice che dichiara quale documento è autorevole.

Una versione storica non viene cancellata. Viene spostata e marcata come superata.

---

## 2. Struttura consigliata

```text
Project Integrity OS/
├── docs/
│   ├── 00-current/
│   │   ├── Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md
│   │   ├── Project_Integrity_OS_TODO_MVP_v0_4.md
│   │   ├── Project_Integrity_OS_Modalita_Esecuzione_v0_1.md
│   │   ├── Project_Integrity_OS_Brief_TODO-0002_v0_2_ACTIVE.md
│   │   └── Project_Integrity_OS_Document_Registry_v0_1.md
│   │
│   ├── 10-executions/
│   │   └── TODO-0002/
│   │       ├── instructions/
│   │       │   ├── Project_Integrity_OS_Prompt_Esecutivo_Browser_TODO-0002.md
│   │       │   └── START_HERE_Browser_Project_Integrity_OS_TODO-0002.md
│   │       ├── superseded/
│   │       │   ├── Project_Integrity_OS_Brief_TODO-0002_v0_1_SUPERSEDED.md
│   │       │   ├── Project_Integrity_OS_Prompt_Esecutivo_TODO-0002.md
│   │       │   └── START_HERE_Project_Integrity_OS_TODO-0002.md
│   │       ├── evidence/
│   │       │   ├── preflight/
│   │       │   ├── commands/
│   │       │   ├── screenshots/
│   │       │   └── file-checks/
│   │       ├── reports/
│   │       └── validation/
│   │
│   └── 20-history/
│       ├── concept/
│       │   ├── sistema_integrita_continuita_progetto_v0_1.md
│       │   ├── sistema_integrita_continuita_progetto_v0_2.md
│       │   ├── sistema_integrita_continuita_progetto_v0_3.md
│       │   ├── sistema_integrita_continuita_progetto_v0_4.md
│       │   ├── sistema_integrita_continuita_progetto_v0_5.md
│       │   └── sistema_integrita_continuita_progetto_v0_6.md
│       ├── flows/
│       │   └── Project_Integrity_OS_Flussi_MVP_v0_1.md
│       └── todo/
│           ├── Project_Integrity_OS_TODO_MVP_v0_1.md
│           ├── Project_Integrity_OS_TODO_MVP_v0_2.md
│           └── Project_Integrity_OS_TODO_MVP_v0_3.md
│
├── src/
├── src-tauri/
├── package.json
└── README.md
```

Le cartelle `src/`, `src-tauri/` e i file applicativi nasceranno con lo scaffold. La struttura `docs/` può essere preparata prima.

---

## 3. Mappatura dei file attuali

### Documenti correnti

Spostare in `docs/00-current/`:

- `Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md`
- `Project_Integrity_OS_TODO_MVP_v0_4.md`
- `Project_Integrity_OS_Modalita_Esecuzione_v0_1.md`
- nuovo brief corretto, salvato come:
  - `Project_Integrity_OS_Brief_TODO-0002_v0_2_ACTIVE.md`
- `Project_Integrity_OS_Document_Registry_v0_1.md`

### Materiale operativo corrente di TODO-0002

Spostare in `docs/10-executions/TODO-0002/instructions/`:

- `Project_Integrity_OS_Prompt_Esecutivo_Browser_TODO-0002.md`
- `START_HERE_Browser_Project_Integrity_OS_TODO-0002.md`

### Materiale operativo superato di TODO-0002

Spostare in `docs/10-executions/TODO-0002/superseded/`:

- il vecchio brief, rinominato:
  - `Project_Integrity_OS_Brief_TODO-0002_v0_1_SUPERSEDED.md`
- `Project_Integrity_OS_Prompt_Esecutivo_TODO-0002.md`
- `START_HERE_Project_Integrity_OS_TODO-0002.md`

Il prompt desktop non viene cancellato: resta una variante storica e potenzialmente riutilizzabile, ma non è il prompt attivo della sessione corrente.

### Evoluzione concettuale

Spostare in `docs/20-history/concept/`:

- `sistema_integrita_continuita_progetto_v0_1.md`
- `sistema_integrita_continuita_progetto_v0_2.md`
- `sistema_integrita_continuita_progetto_v0_3.md`
- `sistema_integrita_continuita_progetto_v0_4.md`
- `sistema_integrita_continuita_progetto_v0_5.md`
- `sistema_integrita_continuita_progetto_v0_6.md`

### Flussi precedenti

Spostare in `docs/20-history/flows/`:

- `Project_Integrity_OS_Flussi_MVP_v0_1.md`

### To-Do precedenti

Spostare in `docs/20-history/todo/`:

- `Project_Integrity_OS_TODO_MVP_v0_1.md`
- `Project_Integrity_OS_TODO_MVP_v0_2.md`
- `Project_Integrity_OS_TODO_MVP_v0_3.md`

---

## 4. Regole di naming

### Stati consentiti

Usare questi suffissi quando servono:

- `_DRAFT`
- `_ACTIVE`
- `_FROZEN`
- `_SUPERSEDED`
- `_CANCELLED`

Esempio:

```text
Project_Integrity_OS_Brief_TODO-0002_v0_1_SUPERSEDED.md
Project_Integrity_OS_Brief_TODO-0002_v0_2_ACTIVE.md
```

### Regola di versione

Non sovrascrivere una versione già usata per una decisione o un’esecuzione.

Quando il contenuto cambia in modo sostanziale:

1. creare una nuova versione;
2. aggiornare il registro;
3. spostare la precedente nella cartella storica o `superseded`;
4. dichiarare esplicitamente quale versione sostituisce.

### Regola sui file senza versione

Evitare file operativi mutevoli senza versione.

Sono ammessi senza versione soltanto:

- `README.md`;
- eventuali indici generati;
- file applicativi che non rappresentano una baseline documentale.

---

## 5. Registro dei documenti

Il file `Project_Integrity_OS_Document_Registry_v0_1.md` deve indicare:

- categoria;
- versione;
- stato;
- percorso;
- autorevolezza;
- documento sostituito;
- task collegata;
- data;
- note.

Il registro risolve la domanda:

> Quale documento devo usare oggi?

Non deve essere necessario dedurlo dalla data del file o dalla posizione in Esplora file.

---

## 6. Materiale di esecuzione ed evidenze

Per ogni task creare una cartella dedicata:

```text
docs/10-executions/<TASK-ID>/
```

Struttura:

```text
instructions/
evidence/
reports/
validation/
superseded/
```

### `instructions/`

Contiene:

- brief attivo;
- prompt;
- START HERE;
- eventuali allegati destinati all’esecutore.

### `evidence/`

Contiene prove grezze:

- output di terminale;
- screenshot;
- risultati di test;
- elenchi file;
- diff;
- controlli Git;
- file prodotti per la verifica.

### `reports/`

Contiene:

- report dell’esecutore;
- report della verifica indipendente;
- report diagnostici dopo fallimenti.

### `validation/`

Contiene:

- collaudo manuale;
- approvazione;
- decisione di chiusura;
- eventuali deroghe.

### `superseded/`

Contiene istruzioni o brief sostituiti durante la stessa task.

---

## 7. Cartella History già esistente

La cartella `History` visibile nella cartella principale può essere:

- svuotata dopo aver spostato i file nella struttura `docs/20-history/`; oppure
- rinominata temporaneamente `_legacy_history_before_reorganization`.

La soluzione consigliata è usare soltanto `docs/20-history/` come posizione definitiva, evitando due archivi storici paralleli.

---

## 8. Protezione del metodo

Questa documentazione contiene parti del metodo proprietario di Project Integrity OS.

Finché il progetto è in sviluppo:

- il repository deve restare privato;
- i documenti interni non devono essere inclusi automaticamente nei pacchetti distribuiti;
- la futura build non deve copiare `docs/20-history/` nell’installer;
- gli export destinati a clienti devono distinguere dati del progetto e logica interna del metodo.

Conservare lo storico nel repository privato è utile per sviluppare e collaudare il prodotto su se stesso.

---

## 9. Uso futuro come primo flusso reale

Quando Project Integrity OS sarà operativo, questa struttura potrà essere importata come caso reale.

Il software dovrà poter ricostruire:

- evoluzione concettuale da v0.1 a v0.6;
- passaggio dai flussi v0.1 ai flussi FROZEN;
- evoluzione della To-Do;
- cambio della modalità da desktop a browser;
- sostituzione del brief;
- istruzioni usate per TODO-0002;
- evidenze e report prodotti;
- decisioni che hanno modificato lo stato operativo.

Questa struttura non è quindi un archivio casuale: è il primo dataset storico del prodotto.

---

## 10. Decisione operativa immediata

Prima del pre-flight di TODO-0002:

1. creare la struttura `docs/`;
2. spostare i file secondo la mappatura;
3. salvare il nuovo brief come `v0_2_ACTIVE`;
4. rinominare il vecchio brief come `v0_1_SUPERSEDED`;
5. inserire il registro documentale;
6. verificare che nessun documento corrente punti ancora alla To-Do v0.2;
7. procedere con il pre-flight soltanto dopo la normalizzazione.
