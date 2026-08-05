# Project Integrity OS
## Modello informativo preliminare per Task, Prompt, Tentativi, Report, Evidenze e Verifica

**Versione:** 0.1
**Stato:** SUPERSEDED — analisi preliminare consolidata dal documento operativo successivo
**Documento autorevole successivo:** `Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md`
**Data:** 2026-08-05
**Scopo:** fissare le decisioni emerse prima dell'avvio di `TODO-0003 — Definire convenzioni tecniche e qualità`.

---

# 1. Perché questo documento esiste

Prima di implementare le convenzioni tecniche previste da TODO-0003 è necessario chiarire come Project Integrity OS dovrà rappresentare e collegare:

- la task;
- il relativo contratto;
- il prompt esecutivo;
- i tentativi;
- il report dell'esecutore;
- le evidenze raccolte dal sistema;
- la riconciliazione tra dichiarazioni e realtà;
- la verifica tecnica;
- l'eventuale approvazione umana.

Prompt e report non devono essere progettati come semplici testi indipendenti. Devono essere due parti collegate dello stesso flusso operativo e devono poter essere confrontati in modo deterministico.

Il modello deve inoltre essere:

- leggibile dagli esseri umani;
- interpretabile dal core Rust;
- validabile automaticamente;
- persistibile in SQLite;
- esportabile in JSON;
- visualizzabile facilmente nella UI React;
- compatibile con versionamento, audit e futura migrazione PostgreSQL.

---

# 2. Decisione architetturale principale

Ogni task deve poter essere rappresentata come un documento JSON canonico composto da:

```text
Task
└── Task Contract
    └── Tentativi
        ├── Prompt esecutivo
        ├── Report dell'esecutore
        ├── Evidenze osservate
        ├── Riconciliazione
        └── Verifica
```

Il JSON è il formato canonico di rappresentazione, validazione, scambio ed esportazione.

Il database non deve però contenere l'intero progetto come un unico JSON gigantesco. La persistenza consigliata è ibrida:

- tabelle relazionali per identità, relazioni, stati, versioni e vincoli;
- payload JSON versionati per i contenuti strutturati e variabili;
- testo originale separato per prompt e report;
- artefatti e output estesi conservati tramite riferimenti dedicati.

---

# 3. Oggetti principali del dominio

## 3.1 Project

Rappresenta il progetto governato.

Campi minimi concettuali:

```json
{
  "project_id": "PROJECT-001",
  "name": "Project Integrity OS"
}
```

## 3.2 Task

Rappresenta l'unità di lavoro da governare.

Campi minimi concettuali:

```json
{
  "task_id": "IMPL-001",
  "project_id": "PROJECT-001",
  "title": "Implementare adapter SQLite",
  "status": "READY"
}
```

La task non deve essere soltanto un testo. Deve possedere un contratto strutturato e versionato.

## 3.3 Task Contract

Definisce ciò che deve essere fatto e con quali vincoli.

Contenuti previsti:

- obiettivo;
- contesto;
- scope consentito;
- scope vietato;
- requisiti;
- test obbligatori;
- criteri di accettazione;
- output richiesti;
- dipendenze;
- numero massimo di tentativi;
- regole su commit e push;
- condizioni di stop;
- limiti espliciti;
- formato richiesto del report.

Esempio:

```json
{
  "contract_id": "CONTRACT-001",
  "task_id": "IMPL-001",
  "version": 1,
  "objective": "Implementare la persistenza SQLite",
  "max_attempts": 3,
  "commit_allowed": true,
  "push_allowed": false,
  "scope": {
    "allowed": [
      "src-tauri/src/persistence/",
      "src-tauri/migrations/",
      "src-tauri/Cargo.toml"
    ],
    "forbidden": [
      "src/",
      "src-tauri/src/git_inspector/"
    ]
  },
  "required_tests": [],
  "acceptance_criteria": [],
  "stop_conditions": []
}
```

---

# 4. Il tentativo come contenitore operativo

Prompt e report non devono avere contatori di tentativi indipendenti.

Il tentativo appartiene all'esecuzione della task e contiene tutti gli elementi relativi a quella specifica esecuzione:

```json
{
  "attempt_id": "ATTEMPT-001",
  "task_id": "IMPL-001",
  "attempt_number": 1,
  "status": "IN_VERIFICATION",
  "prompt": {},
  "report": {},
  "evidence": [],
  "reconciliation": {},
  "verification": {}
}
```

La relazione corretta è:

```text
Task IMPL-001
├── Tentativo 1
│   ├── Prompt 1
│   ├── Report 1
│   ├── Evidenze 1
│   └── Verifica 1
│
└── Tentativo 2
    ├── Prompt 2
    ├── Report 2
    ├── Evidenze 2
    └── Verifica 2
```

Il sistema può calcolare automaticamente:

- tentativi utilizzati;
- tentativi residui;
- ultimo tentativo;
- stato dell'ultima verifica;
- superamento del limite massimo.

Questi valori derivati non devono necessariamente essere persistiti.

---

# 5. Modello del prompt

Il prompt deve esistere in due forme.

## 5.1 Forma strutturata

Contiene i dati che il sistema può validare e confrontare.

Esempio:

```json
{
  "prompt_id": "PROMPT-001",
  "attempt_id": "ATTEMPT-001",
  "schema_version": "1.0",
  "prompt_version": 1,
  "structured": {
    "objective": "Implementare adapter SQLite",
    "context": [],
    "allowed_scope": [],
    "forbidden_scope": [],
    "requirements": [],
    "required_tests": [
      {
        "test_id": "TEST-001",
        "description": "Creazione di un database nuovo",
        "required": true
      }
    ],
    "acceptance_criteria": [
      {
        "criterion_id": "AC-001",
        "description": "Il database viene creato correttamente",
        "required": true
      }
    ],
    "outputs_required": [],
    "max_attempts": 3,
    "commit_allowed": true,
    "push_allowed": false,
    "stop_conditions": [],
    "report_schema_version": "1.0"
  }
}
```

## 5.2 Forma testuale resa

Contiene il testo completo e immutabile consegnato all'esecutore:

```json
{
  "rendered_text": "Testo completo del prompt esecutivo..."
}
```

Il testo reso è necessario per dimostrare esattamente quali istruzioni sono state fornite.

## 5.3 Principio di immutabilità

Quando il prompt viene consegnato e il tentativo inizia, il prompt deve diventare immutabile.

Una correzione successiva non deve sovrascrivere silenziosamente il prompt già utilizzato.

Regola preliminare consigliata:

- prima dell'avvio del tentativo: è ammessa una nuova versione del prompt;
- dopo l'avvio: una modifica sostanziale richiede un nuovo tentativo e un nuovo prompt;
- tutte le versioni devono rimanere auditabili.

---

# 6. Modello del report

Anche il report deve esistere in due forme.

## 6.1 Testo originale

Il testo esatto restituito dall'esecutore deve essere conservato senza modifiche:

```json
{
  "report_id": "REPORT-001",
  "attempt_id": "ATTEMPT-001",
  "raw_text": "Esito: successo\nTentativi: 1\nFile modificati..."
}
```

Il testo originale rappresenta ciò che l'esecutore ha dichiarato.

## 6.2 Forma strutturata

Il report strutturato deve contenere campi confrontabili automaticamente:

```json
{
  "schema_version": "1.0",
  "revision": 1,
  "structured": {
    "declared_outcome": "SUCCESS",
    "summary": "Implementato adapter SQLite.",
    "files": {
      "verified": [],
      "created": [],
      "modified": [],
      "deleted": []
    },
    "commands": [
      {
        "command_id": "CMD-001",
        "command": "cargo test",
        "declared_exit_code": 0,
        "declared_status": "PASSED"
      }
    ],
    "tests": [
      {
        "test_id": "TEST-001",
        "declared_status": "PASSED",
        "notes": null
      }
    ],
    "errors": [],
    "deviations": [],
    "limitations": [],
    "artifacts": [],
    "commit": {
      "created": true,
      "sha": "abc123"
    },
    "push": {
      "performed": false
    },
    "approval_requests": []
  }
}
```

## 6.3 Revisioni

Il report originale non deve essere corretto sovrascrivendolo.

Eventuali integrazioni devono creare una revisione collegata alla precedente:

```json
{
  "report_id": "REPORT-001",
  "revision": 2,
  "supersedes_revision": 1
}
```

Ogni revisione precedente deve rimanere disponibile.

---

# 7. Dichiarazioni, evidenze e verità verificata

Il report non è una prova. Contiene dichiarazioni dell'esecutore.

Le evidenze contengono ciò che Project Integrity OS osserva realmente.

Esempio:

```text
REPORT
“Ho modificato tre file.”

EVIDENCE
Git rileva quattro file modificati.

RECONCILIATION
Un file rilevato non è stato dichiarato.

VERIFICATION
Esito non superato oppure richiesta di chiarimento.
```

Questa separazione è obbligatoria.

## 7.1 Report

Contiene:

- esito dichiarato;
- file dichiarati;
- test dichiarati;
- comandi dichiarati;
- commit e push dichiarati;
- errori e limiti dichiarati.

## 7.2 Evidence

Contiene dati osservati:

```json
{
  "evidence_id": "EVIDENCE-001",
  "attempt_id": "ATTEMPT-001",
  "type": "GIT_SNAPSHOT",
  "observed": {
    "created_files": [],
    "modified_files": [],
    "deleted_files": [],
    "head_commit": "abc123",
    "remote_contains_commit": false
  }
}
```

Altri tipi di evidenza potranno includere:

- output di test;
- exit code;
- stdout e stderr;
- stato Git;
- diff;
- file realmente presenti;
- checksum;
- artefatti;
- risultati di ricerche configurate.

## 7.3 Reconciliation

Confronta dichiarazioni ed evidenze:

```json
{
  "reconciliation_id": "RECON-001",
  "attempt_id": "ATTEMPT-001",
  "status": "MISMATCH",
  "checks": [
    {
      "check_id": "FILES_MATCH",
      "status": "FAILED",
      "missing_from_report": [
        "src-tauri/src/persistence/mod.rs"
      ]
    },
    {
      "check_id": "TESTS_MATCH",
      "status": "PASSED"
    }
  ]
}
```

## 7.4 Verification

Determina l'esito tecnico sulla base dei criteri e delle evidenze:

```json
{
  "verification_id": "VERIFY-001",
  "attempt_id": "ATTEMPT-001",
  "status": "FAILED",
  "criteria": [
    {
      "criterion_id": "AC-001",
      "status": "PASSED",
      "evidence_ids": [
        "EVIDENCE-001"
      ]
    }
  ]
}
```

L'esecutore non deve poter impostare autonomamente la task come completata.

Deve rimanere possibile avere:

```text
executor_outcome = SUCCESS
verification_outcome = FAILED
task_status = NEEDS_REWORK
```

---

# 8. Identificatori condivisi

Gli elementi correlati devono possedere identificatori stabili.

Esempi:

```text
PROJECT-001
IMPL-001
CONTRACT-001
ATTEMPT-001
PROMPT-001
REPORT-001
TEST-001
AC-001
CMD-001
EVIDENCE-001
RECON-001
VERIFY-001
APPROVAL-001
```

Gli stessi identificatori devono essere riutilizzati nelle diverse fasi.

Esempio:

- il prompt richiede `TEST-001`;
- il report dichiara il risultato di `TEST-001`;
- l'evidenza registra il risultato osservato di `TEST-001`;
- la riconciliazione confronta i due risultati;
- la verifica collega `TEST-001` al criterio di accettazione pertinente.

In questo modo il sistema non deve interpretare frasi simili o ambigue.

---

# 9. Vocabolari chiusi

I campi utilizzati per i controlli devono preferire valori chiusi e versionati.

Esempio per test e verifiche:

```json
[
  "PASSED",
  "FAILED",
  "NOT_RUN",
  "BLOCKED",
  "UNKNOWN"
]
```

Esempio per riconciliazione:

```json
[
  "MATCH",
  "MISMATCH",
  "PARTIAL",
  "NOT_APPLICABLE",
  "UNKNOWN"
]
```

Le spiegazioni restano disponibili in campi testuali separati.

Non devono essere salvate emoji come valori di dominio.

La UI potrà rappresentare:

```text
PASSED         → check verde
FAILED         → croce rossa
BLOCKED        → simbolo di blocco
WARNING/PARTIAL→ avviso giallo
UNKNOWN        → indicatore neutro
```

---

# 10. Uso nella UI

La UI React non deve analizzare il testo libero di prompt e report.

Il core Rust deve restituire dati già strutturati e validati.

Una task potrà essere mostrata come:

```text
IMPL-001 — Implementare adapter SQLite

✓ Obiettivo definito
✓ Scope rispettato
✗ Report file incompleto
✓ Test obbligatori superati
✓ Commit creato
✓ Push non effettuato
! Verifica limitata a Windows
```

Possibili sezioni espandibili:

```text
Prompt
Report dichiarato
Evidenze Git
Comandi e test
Differenze rilevate
Verifica finale
Approvazione
```

La presentazione grafica deve dipendere dagli stati strutturati, non da simboli conservati nel database.

---

# 11. Persistenza ibrida consigliata

Il database relazionale deve conservare almeno le identità e le relazioni:

```text
projects
tasks
task_contracts
task_executions
attempts
prompts
reports
evidence
reconciliations
verifications
approvals
command_runs
artifacts
events
```

Esempio concettuale:

```text
prompts
- prompt_id
- task_id
- attempt_id
- schema_version
- prompt_version
- structured_payload_json
- rendered_text
- created_at
- frozen_at
```

```text
reports
- report_id
- task_id
- attempt_id
- schema_version
- revision
- structured_payload_json
- raw_text
- received_at
```

I dati JSON non sostituiscono:

- chiavi primarie;
- chiavi esterne;
- vincoli;
- stati;
- cronologia;
- versioni;
- relazioni;
- audit.

Quando richiesto dalla UI o da un export, il core potrà assemblare un oggetto canonico completo.

---

# 12. Esempio di oggetto canonico aggregato

```json
{
  "schema_version": "1.0",
  "project_id": "PROJECT-001",
  "task_id": "IMPL-001",
  "task": {
    "title": "Implementare adapter SQLite",
    "status": "IN_VERIFICATION"
  },
  "contract": {
    "contract_id": "CONTRACT-001",
    "version": 1,
    "objective": "Implementare la persistenza SQLite",
    "max_attempts": 3,
    "commit_allowed": true,
    "push_allowed": false,
    "scope": {
      "allowed": [],
      "forbidden": []
    },
    "required_tests": [],
    "acceptance_criteria": [],
    "stop_conditions": []
  },
  "attempts": [
    {
      "attempt_id": "ATTEMPT-001",
      "attempt_number": 1,
      "status": "COMPLETED",
      "prompt": {
        "prompt_id": "PROMPT-001",
        "version": 1,
        "structured": {},
        "rendered_text": ""
      },
      "report": {
        "report_id": "REPORT-001",
        "revision": 1,
        "raw_text": "",
        "structured": {}
      },
      "evidence": [],
      "reconciliation": {
        "status": "MISMATCH",
        "checks": []
      },
      "verification": {
        "status": "FAILED",
        "criteria": []
      }
    }
  ],
  "summary": {
    "attempts_used": 1,
    "attempts_remaining": 2,
    "latest_verification": "FAILED"
  }
}
```

La sezione `summary` è preferibilmente derivata e può essere generata al momento anziché persistita.

---

# 13. Relazione con TODO-0003

TODO-0003 comprende due aree differenti.

## 13.1 Baseline tecnica

Può introdurre:

- formattazione;
- lint;
- test Rust;
- test TypeScript;
- naming del codice;
- gestione strutturata degli errori;
- logging;
- convenzioni per migrazioni;
- comandi di verifica.

## 13.2 Baseline operativa

Deve definire:

- struttura minima del prompt;
- struttura minima del report;
- regola dei tre tentativi;
- condizioni di stop;
- formato obbligatorio dei report esecutivi;
- distinzione tra dichiarazioni ed evidenze;
- requisiti di versionamento e immutabilità.

Il presente documento è una base preliminare per evitare che la parte operativa venga definita senza considerare la futura persistenza e riconciliazione.

---

# 14. Decisioni considerate già solide

Le seguenti decisioni possono essere assunte come direzione progettuale:

1. usare JSON come rappresentazione canonica;
2. collegare prompt e report a uno specifico tentativo;
3. conservare sia testo originale sia dati strutturati;
4. separare dichiarazioni, evidenze, riconciliazione e verifica;
5. assegnare ID stabili a test, criteri e oggetti;
6. usare vocabolari chiusi per gli stati;
7. non salvare emoji come dati;
8. adottare persistenza ibrida relazionale più JSON;
9. rendere immutabili prompt utilizzati e report originali;
10. generare per la UI un oggetto aggregato già validato dal core Rust.

---

# 15. Decisioni ancora da approvare prima dell'esecuzione completa di TODO-0003

Prima di congelare il formato operativo servono decisioni esplicite su:

## 15.1 Campi obbligatori del prompt

Definire esattamente:

- sezioni sempre obbligatorie;
- sezioni opzionali;
- campi generati dal sistema;
- campi compilati manualmente;
- campi modificabili;
- momento di congelamento.

## 15.2 Campi obbligatori del report

Definire esattamente:

- sezioni obbligatorie;
- differenza tra file verificati, creati, modificati ed eliminati;
- forma dei comandi;
- forma dei risultati dei test;
- errori;
- deviazioni;
- limiti;
- artefatti;
- richieste di approvazione;
- commit e push.

## 15.3 Semantica del tentativo

Definire:

- quando un tentativo inizia;
- quando viene considerato consumato;
- quali correzioni sono ammesse senza creare un nuovo tentativo;
- quando una modifica del prompt obbliga a un nuovo tentativo;
- trattamento dei fallimenti tecnici esterni;
- comportamento dopo il terzo tentativo.

## 15.4 Stati e autorità

Definire:

- stati della task;
- stati del tentativo;
- stati del report;
- stati della riconciliazione;
- stati della verifica;
- chi può impostare ogni stato;
- quali transizioni sono vietate;
- quando è richiesta approvazione umana.

## 15.5 Validazione e compatibilità

Definire:

- uso futuro di JSON Schema;
- gestione delle versioni;
- regole di compatibilità;
- campi sconosciuti;
- migrazione dei payload precedenti;
- distinzione tra errore di schema e incompletezza ammessa.

---

# 16. Raccomandazione operativa

Non è consigliabile iniziare l'intera TODO-0003 trattando il formato di prompt e report come già definitivo.

È invece consigliabile:

```text
1. approvare la direzione contenuta in questo documento;
2. svolgere una discussione finale e circoscritta sui cinque gruppi di decisioni aperte;
3. congelare Prompt Schema v1 e Report Schema v1;
4. aggiornare il brief esecutivo di TODO-0003;
5. eseguire TODO-0003;
6. affrontare successivamente lo schema dati relazionale in TODO-0101.
```

La parte tecnica di TODO-0003 potrebbe essere sviluppata indipendentemente, ma procedere prima di avere approvato il contratto minimo di prompt e report rischierebbe di dividere la task e produrre documentazione da correggere subito dopo.

---

# 17. Criterio di uscita dalla fase di discussione

La fase preliminare può essere considerata conclusa quando sono approvati:

- Prompt Schema v1;
- Report Schema v1;
- regole del tentativo;
- vocabolari degli stati;
- regole di immutabilità e versionamento;
- distinzione dichiarazioni/evidenze;
- modello di collegamento al futuro database.

A quel punto TODO-0003 può iniziare senza un rischio significativo di ripensamento strutturale.

---

# 18. Stato del documento

Questo documento:

- non implementa ancora il database;
- non costituisce ancora uno schema SQL;
- non implementa il generatore di prompt;
- non implementa l'importatore dei report;
- non implementa la riconciliazione;
- non sostituisce le task future dedicate a queste funzioni;
- fornisce la base decisionale necessaria per eseguire correttamente TODO-0003 e progettare successivamente TODO-0101.
