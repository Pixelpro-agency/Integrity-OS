# Project Integrity OS

## Brief esecutivo — TODO-0101

### Definire lo schema dati minimo

**Versione del brief:** v0.1  
**Stato:** DRAFT — analisi amministrativa pronta per approvazione  
**Data:** 2026-08-05  
**Task:** TODO-0101  
**Priorità:** P0  
**Modalità prevista:** `BROWSER_OPERATOR_ASSISTED`  
**Tentativi massimi:** 3 tentativi ragionati, poi stop e report diagnostico  
**Commit policy durante l'esecuzione:** `FORBIDDEN`  
**Push policy durante l'esecuzione:** `FORBIDDEN`

---

# 1. Documenti autorevoli

TODO-0101 deve rispettare:

1. `Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md`
2. `Project_Integrity_OS_TODO_MVP_v0_8.md`
3. `Project_Integrity_OS_Prompt_Report_Rule_Catalog_Lifecycle_v0_1.md`
4. `Project_Integrity_OS_Convenzioni_Tecniche_v0_2.md`
5. `Project_Integrity_OS_Standard_Report_Sviluppo_v0_2.md`
6. `Project_Integrity_OS_Organizzazione_Documenti_v0_1.md`
7. il presente brief, dopo approvazione e passaggio ad `ACTIVE`

Gerarchia:

1. la specifica FROZEN governa obiettivi e vincoli;
2. la To-Do governa stato, dipendenze e ordine;
3. la baseline Prompt/Report/Rule Catalog/Lifecycle governa identificatori, tentativi e artefatti;
4. le convenzioni tecniche governano naming, tipi, migrazioni e verifiche;
5. lo Standard Report governa l'output dell'esecutore;
6. il presente brief governa il perimetro specifico di TODO-0101.

---

# 2. Stato e dipendenze

```text
TODO-0101 — Definire schema dati minimo
Dipendenza: TODO-0001 — soddisfatta
Stato del brief: DRAFT
```

Prerequisiti osservati:

```text
TODO-0001 — DONE
TODO-0002 — DONE
TODO-0003 — DONE
baseline tecnica — disponibile
baseline Prompt/Report/Rule Catalog/Lifecycle — disponibile
SQLite adapter — non implementato
```

Prima dell'esecuzione il brief deve essere approvato e la task portata a `READY`.

---

# 3. Obiettivo

Definire e documentare lo schema dati relazionale minimo del primo MVP.

Il risultato deve stabilire:

- entità;
- responsabilità;
- chiavi primarie e foreign key;
- relazioni e cardinalità;
- campi minimi;
- tipi logici;
- vocabolari chiusi;
- invarianti;
- vincoli di unicità;
- immutabilità;
- politica di cancellazione;
- uso dei payload JSON;
- compatibilità SQLite/PostgreSQL;
- assenza di dipendenza da `rowid`.

TODO-0101 produce una specifica dati, non un database eseguibile.

---

# 4. Output obbligatorio

Creare integralmente:

```text
docs/00-current/Project_Integrity_OS_Schema_Dati_Minimo_v0_1.md
```

Il documento deve contenere almeno:

1. scopo e principi;
2. tipi logici;
3. regole comuni;
4. entità e dizionario dati;
5. chiavi, relazioni e cardinalità;
6. diagramma ER testuale o Mermaid;
7. vocabolari chiusi;
8. invarianti trasversali;
9. immutabilità e cancellazione;
10. strategia relazionale più JSON;
11. mapping SQLite/PostgreSQL;
12. indici concettualmente necessari;
13. ordine futuro di creazione delle tabelle;
14. aspetti rinviati;
15. checklist di conformità.

Non creare SQL reale.

---

# 5. Decisioni strutturali vincolanti

## 5.1 Un database per progetto

Ogni progetto usa un database SQLite separato.

Nel database dedicato:

- `projects` contiene il record autorevole del progetto;
- deve esistere un solo progetto attivo;
- tutte le entità di dominio rilevanti contengono `project_id`;
- il futuro registro globale di TODO-0103 resta distinto e minimale.

## 5.2 Identificatori

Ogni entità persistente deve avere una chiave esplicita di tipo logico:

```text
UUID
```

Regole:

- generato dall'applicazione;
- stabile;
- non derivato da nomi modificabili;
- non riciclato;
- rappresentabile come `TEXT` canonico in SQLite;
- rappresentabile come `UUID` in PostgreSQL;
- nessuna dipendenza da `rowid`.

Gli ID leggibili come `PROJECT-001` o `REPORT-001` sono identificatori di dominio e non sostituiscono necessariamente la chiave UUID interna.

Quando entrambi servono:

```text
<entity>_id
display_id
```

La versione UUID concreta è rinviata a TODO-0102.

## 5.3 Isolamento per progetto

Ogni tabella di dominio deve includere:

```text
project_id UUID NOT NULL
```

Le relazioni devono impedire collegamenti tra progetti differenti tramite vincoli composti coerenti, non soltanto tramite una dichiarazione documentale.

## 5.4 `task_executions` rappresenta i tentativi

Nel primo schema:

```text
task_executions = persistenza dei tentativi del lifecycle
```

Ogni riga rappresenta un singolo tentativo.

Vincolo minimo:

```text
UNIQUE (project_id, task_id, attempt_number)
```

Il termine `attempt_id` dei Prompt Schema e Report Schema deve riferirsi in modo deterministico allo stesso record persistito in `task_executions`.

## 5.5 Relazionale più JSON

Usare tabelle relazionali per:

- identità;
- stato;
- relazioni;
- versioni;
- timestamp;
- vincoli;
- esiti sintetici.

Usare JSON versionato per:

- regole configurate;
- scope;
- prompt strutturato;
- report strutturato;
- dettagli delle evidenze;
- risultati di riconciliazione e verifica;
- payload eventi;
- metadati estensibili.

Mappatura logica:

```text
SQLite      → TEXT contenente JSON valido
PostgreSQL  → JSONB
```

Non salvare l'intero progetto in un unico JSON.

## 5.6 Testi originali immutabili

Conservare separatamente:

```text
prompt.rendered_text
report.raw_text
```

Dopo congelamento o importazione non devono essere sovrascritti.

## 5.7 Timestamp

Tipo logico:

```text
TIMESTAMP_UTC
```

Regole:

- UTC;
- precisione almeno al millisecondo;
- RFC 3339 in SQLite;
- `TIMESTAMPTZ` in PostgreSQL;
- nomi coerenti come `created_at`, `started_at`, `completed_at`, `observed_at`.

## 5.8 Eliminazione

Regola predefinita:

```text
ON DELETE RESTRICT
```

Nessun cascade distruttivo sullo storico operativo. Le entità storiche vengono chiuse o archiviate tramite stato e timestamp.

## 5.9 Immutabilità

Append-only o immutabili dopo finalizzazione:

- eventi;
- snapshot;
- report originali;
- prompt congelati;
- evidenze;
- approvazioni;
- eccezioni approvate;
- command run conclusi;
- baseline approvate.

Una rettifica crea un nuovo record o evento.

## 5.10 Eventi

`events` è un audit log append-only, non un event store puro. La fonte di verità operativa resta nelle tabelle relazionali.

---

# 6. Entità obbligatorie

## 6.1 `projects`

Responsabilità: identità del progetto, repository collegato, database, versione schema e disponibilità.

Campi minimi:

```text
project_id
display_id
name
repository_path
database_path
default_branch
schema_version
availability_status
created_at
updated_at
archived_at
```

## 6.2 `baselines`

Responsabilità: baseline storicizzata e approvabile.

Campi minimi:

```text
baseline_id
project_id
previous_baseline_id
status
commit_sha
branch_name
working_tree_status
fingerprint
summary_json
created_at
approved_at
approved_by
```

Una baseline approvata è immutabile.

## 6.3 `tasks`

Responsabilità: identità e stato corrente della task.

Campi minimi:

```text
task_id
project_id
display_id
title
objective
motivation
priority
status
max_attempts
commit_policy
push_policy
manual_validation_required
corrective_for_task_id
created_at
updated_at
completed_at
archived_at
```

Scope e criteri versionati appartengono al Task Contract.

## 6.4 `task_executions`

Responsabilità: rappresentare ogni tentativo e collegare task, prompt, snapshot, report ed esiti.

Campi minimi:

```text
task_execution_id
project_id
task_id
attempt_number
status
executor_type
external_session_id
prompt_id
initial_snapshot_id
consumed
started_at
completed_at
technical_outcome
closure_reason
created_at
```

## 6.5 `reports`

Responsabilità: conservare report originale e payload strutturato.

Campi minimi:

```text
report_id
project_id
task_execution_id
schema_version
prompt_id
declared_outcome
raw_text
structured_payload_json
parse_status
completeness_status
content_hash
received_at
created_at
```

## 6.6 `evidence`

Responsabilità: registrare fatti osservati con fonte e timestamp.

Campi minimi:

```text
evidence_id
project_id
task_id
task_execution_id
evidence_type
source_type
observed_at
payload_schema_version
payload_json
content_hash
repository_snapshot_id
command_run_id
created_at
```

## 6.7 `reconciliations`

Responsabilità: confrontare dichiarazioni ed evidenze.

Campi minimi:

```text
reconciliation_id
project_id
task_execution_id
report_id
status
payload_schema_version
result_json
started_at
completed_at
created_at
```

Valori iniziali:

```text
MATCH
MISMATCH
PARTIAL
NOT_APPLICABLE
UNKNOWN
MISSING_EVIDENCE
NOT_VERIFIABLE
```

Il documento finale deve scegliere il valore canonico tra le varianti storiche `PARTIAL` e `PARTIAL_MATCH`, documentando gli alias senza riscrivere le fonti.

## 6.8 `verifications`

Responsabilità: verifica tecnica, macroscopica e verifica della verifica.

Campi minimi:

```text
verification_id
project_id
task_execution_id
reconciliation_id
verification_type
status
scope_json
result_json
started_at
completed_at
created_at
```

Tipi minimi:

```text
TECHNICAL
MACRO
VERIFICATION_OF_VERIFICATION
FUNCTIONAL_VALIDATION
```

Stati minimi:

```text
PASSED
FAILED
NOT_RUN
BLOCKED
UNKNOWN
```

## 6.9 `approvals`

Responsabilità: decisioni umane collegate a task, tentativo o verifica.

Campi minimi:

```text
approval_id
project_id
task_id
task_execution_id
verification_id
approval_type
decision
approved_by
reason
approved_at
created_at
```

## 6.10 `exceptions`

Responsabilità: deroghe esplicite e governate.

Campi minimi:

```text
exception_id
project_id
task_id
task_execution_id
rule_id
status
reason
risk_accepted
expires_at
approved_by
approved_at
corrective_task_id
created_at
```

## 6.11 `bugs`

Responsabilità: bug collegati allo storico e alle correzioni.

Campi minimi:

```text
bug_id
project_id
display_id
title
symptom
severity
status
discovered_at
discovered_in_task_id
potentially_responsible_task_id
potentially_responsible_commit_sha
violated_requirement
missed_detection_reason
fix_task_id
regression_test_reference
residual_risk
future_areas_json
created_at
updated_at
closed_at
```

## 6.12 `events`

Responsabilità: audit append-only.

Campi minimi:

```text
event_id
project_id
aggregate_type
aggregate_id
aggregate_version
event_type
actor_type
actor_id
payload_schema_version
payload_json
occurred_at
created_at
```

Vincolo minimo:

```text
UNIQUE (project_id, aggregate_type, aggregate_id, aggregate_version)
```

## 6.13 `repository_snapshots`

Responsabilità: stato tecnico osservato del repository.

Campi minimi:

```text
repository_snapshot_id
project_id
task_id
task_execution_id
snapshot_type
commit_sha
branch_name
working_tree_status
state_schema_version
state_json
fingerprint
captured_at
created_at
```

## 6.14 `command_runs`

Responsabilità: comandi autorizzati del Controlled Process Runner.

Campi minimi:

```text
command_run_id
project_id
task_id
task_execution_id
command_id
category
program
arguments_json
working_directory
environment_json
timeout_ms
authorization_status
started_at
completed_at
exit_code
stdout_text
stderr_text
result_status
created_at
```

Non deve rappresentare una shell generica.

---

# 7. Tabelle di supporto richieste

## 7.1 `task_dependencies`

```text
project_id
task_id
depends_on_task_id
dependency_type
created_at
```

Vincoli: niente auto-dipendenza, niente duplicati, stesso progetto.

## 7.2 `task_contracts`

```text
task_contract_id
project_id
task_id
version
status
schema_version
contract_json
content_hash
created_at
frozen_at
```

TODO-0301 definirà comportamento e validazione completi.

## 7.3 `prompts`

```text
prompt_id
project_id
task_id
task_execution_id
task_contract_id
schema_version
prompt_version
structured_payload_json
rendered_text
content_hash
status
created_at
frozen_at
```

## 7.4 `artifacts`

```text
artifact_id
project_id
task_id
task_execution_id
report_id
artifact_type
declared_path
observed_path
media_type
content_hash
status
metadata_json
created_at
observed_at
```

## 7.5 `baseline_tasks`

```text
project_id
baseline_id
task_id
relation_type
created_at
```

## 7.6 `schema_migrations`

Tabella tecnica del database:

```text
version
name
checksum
introduced_by_task_id
applied_at
execution_time_ms
```

Non richiede `project_id` perché è scoped dal database fisico e deve esistere anche durante il bootstrap.

---

# 8. Tipi logici minimi

Definire almeno:

```text
UUID
DISPLAY_ID
TEXT
LONG_TEXT
BOOLEAN
INTEGER
NON_NEGATIVE_INTEGER
TIMESTAMP_UTC
ENUM_TEXT
SHA
CONTENT_HASH
LOCAL_PATH
JSON_DOCUMENT
SCHEMA_VERSION
DURATION_MS
```

Mapping concettuale minimo:

| Tipo logico | SQLite | PostgreSQL | Regole |
|---|---|---|---|
| UUID | TEXT | UUID | formato canonico |
| BOOLEAN | INTEGER 0/1 | BOOLEAN | solo valori validi |
| TIMESTAMP_UTC | TEXT RFC 3339 | TIMESTAMPTZ | UTC |
| JSON_DOCUMENT | TEXT JSON valido | JSONB | schema versionato |
| SHA | TEXT | TEXT | formato validato |
| CONTENT_HASH | TEXT | TEXT | algoritmo dichiarato |
| DURATION_MS | INTEGER | BIGINT | non negativo |

---

# 9. Relazioni minime

```text
projects 1 ── N baselines
projects 1 ── N tasks
tasks N ── N tasks tramite task_dependencies
tasks 1 ── N task_contracts
tasks 1 ── N task_executions
task_executions 1 ── N prompts
task_executions 1 ── N reports
task_executions 1 ── N evidence
task_executions 1 ── N reconciliations
task_executions 1 ── N verifications
task_executions 1 ── N command_runs
task_executions 1 ── N artifacts
projects 1 ── N bugs
projects 1 ── N events
projects 1 ── N repository_snapshots
baselines N ── N tasks tramite baseline_tasks
```

Chiarire inoltre:

- una riconciliazione usa un report e un insieme di evidenze;
- una verifica può dipendere da una riconciliazione;
- un'approvazione richiede un oggetto verificabile;
- un'eccezione può collegarsi a una task correttiva;
- un bug può essere scoperto dopo la chiusura della task originaria.

---

# 10. Vocabolari chiusi

Raccogliere in una sezione unica almeno:

- stati task;
- stati tentativo;
- policy commit e push;
- esiti dichiarati;
- stati test/verifica;
- stati riconciliazione;
- severità e stati bug;
- tipi snapshot;
- tipi verifica;
- decisioni approvazione;
- stati eccezione;
- tipi attore;
- categorie command run.

In caso di varianti terminologiche:

1. scegliere un valore canonico;
2. elencare gli alias storici importabili;
3. non modificare le fonti storiche;
4. rinviare la normalizzazione alla task implementativa.

---

# 11. Indici concettuali

Indicare almeno indici per:

- foreign key usate nelle ricerche;
- `tasks(project_id, status)`;
- `tasks(project_id, display_id)` univoco;
- `task_executions(project_id, task_id, attempt_number)` univoco;
- `reports(project_id, task_execution_id)`;
- `evidence(project_id, task_execution_id, evidence_type)`;
- `events(project_id, aggregate_type, aggregate_id, aggregate_version)` univoco;
- `repository_snapshots(project_id, captured_at)`;
- `command_runs(project_id, task_execution_id, started_at)`;
- `bugs(project_id, status, severity)`;
- `schema_migrations(version)` univoco.

---

# 12. Fuori scope

TODO-0101 non deve:

- aggiungere dipendenze;
- modificare `Cargo.toml`, `Cargo.lock`, `package.json` o `package-lock.json`;
- creare file `.sqlite`;
- creare SQL o migrazioni reali;
- implementare repository Rust o CRUD;
- implementare transazioni;
- implementare registro globale;
- implementare Task Contract, Rule Catalog o parser report;
- implementare snapshot Git, runner, riconciliazione o verifica;
- implementare state machine;
- modificare frontend o core Rust;
- introdurre API IA, PostgreSQL o Supabase;
- modificare la specifica FROZEN.

---

# 13. Scope

Write scope principale:

```text
docs/00-current/Project_Integrity_OS_Schema_Dati_Minimo_v0_1.md
docs/10-executions/TODO-0101/
```

Aggiornamenti di governance soltanto in preparazione o chiusura:

```text
docs/00-current/Project_Integrity_OS_TODO_MVP_<versione>.md
docs/00-current/Project_Integrity_OS_Document_Registry_<versione>.md
docs/20-history/todo/
docs/20-history/registry/
```

Read scope minimo:

```text
docs/00-current/
docs/10-executions/TODO-0002/
docs/10-executions/TODO-0003/
src-tauri/Cargo.toml
src-tauri/src/
package.json
```

Il codice è in sola lettura.

---

# 14. Verifiche obbligatorie

Verificare che:

- siano presenti le 14 entità obbligatorie;
- siano presenti le 6 tabelle di supporto;
- ogni entità rilevante abbia `project_id`;
- ogni tabella abbia chiave esplicita;
- foreign key e cardinalità siano definite;
- siano impediti collegamenti cross-project;
- `task_executions` rappresenti i tentativi;
- prompt e report originali siano immutabili;
- eventi e snapshot siano immutabili;
- la cancellazione sia restrittiva;
- esista mapping SQLite/PostgreSQL;
- non esista dipendenza da `rowid`;
- relazionale e JSON siano separati;
- gli aspetti rinviati siano dichiarati.

Comandi finali:

```bash
git diff --check
git diff --cached --check
npm run verify
```

Il report deve dimostrare che non sono stati modificati:

```text
src/
src-tauri/
package.json
package-lock.json
src-tauri/Cargo.toml
src-tauri/Cargo.lock
```

---

# 15. Criteri di accettazione

- `AC-0101-001`: documento principale presente nel percorso autorizzato.
- `AC-0101-002`: tutte le 14 entità obbligatorie definite.
- `AC-0101-003`: tabelle di supporto definite senza implementare task future.
- `AC-0101-004`: chiavi, foreign key, cardinalità e unicità documentate.
- `AC-0101-005`: isolamento per progetto garantito.
- `AC-0101-006`: tipi compatibili con SQLite e PostgreSQL.
- `AC-0101-007`: nessuna dipendenza da `rowid`.
- `AC-0101-008`: separazione tra relazionale, JSON e testi originali.
- `AC-0101-009`: immutabilità esplicita.
- `AC-0101-010`: cancellazione governata e non distruttiva.
- `AC-0101-011`: diagramma ER e dizionario dati coerenti.
- `AC-0101-012`: vocabolari chiusi e alias storici documentati.
- `AC-0101-013`: nessuna implementazione anticipata.
- `AC-0101-014`: verifiche finali con exit code `0`.
- `AC-0101-015`: report conforme allo Standard Report v0.2.

---

# 16. Condizioni di stop

Fermarsi e produrre report diagnostico quando:

- i documenti autorevoli sono inconciliabili;
- manca un riferimento indispensabile;
- servirebbe modificare la specifica FROZEN;
- servirebbe introdurre codice, dipendenze o SQL;
- una relazione richiede un'entità non motivabile;
- dopo tre tentativi restano criteri bloccanti;
- la verifica fallisce fuori dal perimetro documentale.

---

# 17. Report obbligatorio

Il report finale deve rispettare `Project_Integrity_OS_Standard_Report_Sviluppo_v0_2.md` e includere:

- task e tentativo;
- esito;
- sintesi;
- documenti letti;
- file verificati, creati, modificati, eliminati e rinominati;
- comandi e test;
- criteri di accettazione con ID;
- errori, limiti, deviazioni e aspetti non verificati;
- dipendenze;
- commit e push;
- artefatti;
- richieste di approvazione;
- output completo di `npm run verify`.

---

# 18. Decisioni rinviate

Rinviati a TODO-0102 o task dedicate:

- libreria SQLite;
- versione UUID concreta;
- SQL DDL;
- `WITHOUT ROWID`;
- PRAGMA e foreign key concrete;
- transazioni;
- migrazioni eseguibili;
- repository interface e CRUD;
- serializzazione Rust;
- validazione JSON;
- parser report e generatore prompt;
- state machine;
- query plan;
- backup e cifratura;
- PostgreSQL adapter.

---

# 19. Esito dell'analisi amministrativa

```text
TODO-0101 può passare da TODO ad ANALYZED.
```

Dopo approvazione del brief e creazione del prompt esecutivo:

```text
TODO-0101 può passare da ANALYZED a READY.
```

Nessuna modifica al codice o alle dipendenze è necessaria.
