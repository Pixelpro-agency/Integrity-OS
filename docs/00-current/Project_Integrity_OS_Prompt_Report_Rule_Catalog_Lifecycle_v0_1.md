# Project Integrity OS
## Prompt Schema v1, Report Schema v1, Rule Catalog v1 e Lifecycle dei Tentativi

**Versione:** 0.1
**Stato:** ACTIVE — baseline operativa MVP
**Data:** 2026-08-05
**Task di origine:** `TODO-0003 — Definire convenzioni tecniche e qualità`
**Scopo:** definire la baseline operativa per configurare le regole delle task, generare prompt e report collegati ai tentativi, raccogliere evidenze, verificare gli esiti e prepararne la futura persistenza.

---

# 1. Obiettivo del documento

Questo documento definisce una prima base comune per:

- configurare le regole di una task tramite UI;
- generare un prompt esecutivo coerente;
- richiedere un report strutturato;
- collegare prompt e report allo stesso tentativo;
- verificare automaticamente la coerenza tra istruzioni, dichiarazioni ed evidenze;
- rappresentare gli esiti nella UI tramite stati, indicatori, dropdown e riepiloghi;
- preparare la futura persistenza in SQLite senza vincolare prematuramente lo schema SQL.

La struttura deve restare:

- deterministica;
- versionata;
- leggibile;
- validabile;
- esportabile in JSON;
- compatibile con una futura migrazione PostgreSQL;
- separata dalla presentazione grafica della UI.

---

# 2. Principio generale

Ogni task deve seguire questo flusso:

```text
Task
↓
Task Contract
↓
Rule Set configurato
↓
Prompt strutturato
↓
Prompt testuale congelato
↓
Tentativo
↓
Report originale
↓
Report strutturato
↓
Evidenze osservate
↓
Riconciliazione
↓
Verifica
↓
Approvazione o nuovo tentativo
```

Prompt e report non devono essere semplici testi indipendenti.

Devono essere due rappresentazioni collegate allo stesso tentativo e devono condividere identificatori stabili per:

- test;
- criteri di accettazione;
- regole;
- artefatti;
- comandi;
- file;
- commit;
- push;
- evidenze.

---

# 3. Rule Catalog v1

Il Rule Catalog è il catalogo delle regole configurabili nella UI.

Ogni regola deve indicare:

- identificatore stabile;
- nome leggibile;
- categoria;
- tipo di valore;
- valore predefinito;
- se è obbligatoria;
- se è bloccata;
- se è selezionabile;
- dove si applica;
- come viene validata;
- come alimenta prompt, report, verifica e UI.

Esempio:

```json
{
  "rule_id": "execution.max_attempts",
  "label": "Numero massimo di tentativi",
  "category": "EXECUTION",
  "value_type": "INTEGER",
  "required": true,
  "locked": false,
  "default_value": 3,
  "applies_to": [
    "PROMPT",
    "REPORT",
    "VERIFICATION",
    "UI"
  ],
  "validation": {
    "minimum": 1,
    "maximum": 10
  }
}
```

---

# 4. Tipologie di regole

## 4.1 Regole fisse e bloccate

Sono sempre attive e visibili nella UI ma non modificabili.

Esempi:

```text
Identificativo della task
Identificativo del tentativo
Numero del tentativo
Obiettivo della task
Scope consentito
Scope vietato
Elenco dei file verificati
Elenco dei file creati
Elenco dei file modificati
Elenco dei file eliminati
Elenco dei file rinominati
Comandi eseguiti
Test eseguiti
Errori incontrati
Limiti
Deviazioni
Aspetti non verificati
Stato commit
Stato push
Report finale obbligatorio
```

Anche quando una sezione non contiene elementi, deve essere presente:

```json
{
  "errors": [],
  "limitations": [],
  "deviations": [],
  "unverified_aspects": []
}
```

## 4.2 Regole selezionabili predefinite

Sono presenti nel catalogo e possono essere attivate, disattivate o configurate.

Esempi:

```text
Commit obbligatorio
Commit facoltativo
Commit vietato
SHA del commit obbligatorio
Push obbligatorio
Push facoltativo
Push vietato
Aggiornamento documentazione richiesto
File riepilogativo delle modifiche richiesto
Screenshot richiesti
Backup pre-modifica richiesto
Nessuna nuova dipendenza consentita
Artefatti aggiuntivi richiesti
Numero massimo di tentativi
```

## 4.3 Regole personalizzate

L'utente può aggiungere regole specifiche per la task.

Ogni regola personalizzata deve indicare almeno:

```json
{
  "rule_id": "custom.IMPL-001.001",
  "label": "Non modificare il frontend",
  "value_type": "BOOLEAN",
  "value": true,
  "applies_to": [
    "PROMPT",
    "VERIFICATION",
    "UI"
  ]
}
```

Le regole personalizzate devono essere versionate e collegate alla task.

---

# 5. Tipi di valore ammessi per le regole

Prima versione consigliata:

```text
BOOLEAN
INTEGER
TEXT
ENUM
FILE
DIRECTORY
PATH_PATTERN
COMMAND
STRING_LIST
OBJECT
```

Esempi UI:

```text
BOOLEAN       → checkbox
INTEGER       → campo numerico
TEXT          → campo di testo
ENUM          → radio button o select
FILE          → selettore file
DIRECTORY     → selettore cartella
STRING_LIST   → elenco modificabile
```

---

# 6. Policy commit e push

Commit e push non devono essere rappresentati da un semplice booleano.

Devono usare tre stati:

```text
FORBIDDEN
OPTIONAL
REQUIRED
```

Esempio:

```json
{
  "commit_policy": "REQUIRED",
  "push_policy": "FORBIDDEN"
}
```

## 6.1 Regola SHA commit

La presenza dello SHA dipende dalla policy commit:

```text
commit_policy = FORBIDDEN
→ commit non consentito
→ SHA non richiesto

commit_policy = OPTIONAL
→ se viene creato un commit, SHA obbligatorio

commit_policy = REQUIRED
→ commit obbligatorio
→ SHA obbligatorio
→ messaggio commit obbligatorio
```

Lo SHA deve essere verificato contro Git e non considerato valido solo perché dichiarato nel report.

## 6.2 Push

Esempi:

```text
push_policy = FORBIDDEN
→ push.performed deve essere false

push_policy = OPTIONAL
→ push può essere true o false
→ se true, remote e branch obbligatori

push_policy = REQUIRED
→ push.performed deve essere true
→ remote e branch obbligatori
→ verifica presenza commit sul remoto
```

---

# 7. File riepilogativo delle modifiche

La creazione di un file riepilogativo può essere una regola opzionale.

Esempio:

```json
{
  "rule_id": "artifacts.change_summary_file",
  "label": "Creare file riepilogativo delle modifiche",
  "enabled": true,
  "configuration": {
    "required_path": "docs/execution/IMPL-001-changes.md",
    "format": "MARKDOWN"
  }
}
```

Il prompt deve specificare:

- percorso;
- formato;
- sezioni obbligatorie;
- eventuale convenzione di naming.

Il report deve dichiarare:

```json
{
  "artifacts": [
    {
      "artifact_id": "ARTIFACT-001",
      "type": "CHANGE_SUMMARY",
      "declared_path": "docs/execution/IMPL-001-changes.md"
    }
  ]
}
```

Le evidenze devono verificare:

- esistenza;
- percorso;
- tipo;
- checksum;
- eventuale conformità minima del contenuto.

---

# 8. Binding delle regole

Ogni regola deve poter alimentare quattro livelli:

```text
Prompt
Report
Verifica
UI
```

Esempio:

```json
{
  "rule_id": "git.push_policy",
  "configured_value": "FORBIDDEN",
  "prompt_binding": {
    "instruction": "Non eseguire il push."
  },
  "report_binding": {
    "required_field": "version_control.push.performed"
  },
  "verification_binding": {
    "check": "PUSH_NOT_PERFORMED"
  },
  "ui_binding": {
    "success_label": "Push non eseguito",
    "failure_label": "Push eseguito senza autorizzazione"
  }
}
```

Questa è la base per evitare che la stessa regola venga riscritta manualmente in punti diversi.

---

# 9. Prompt Schema v1

## 9.1 Struttura base

```json
{
  "schema_version": "1.0",
  "prompt_id": "PROMPT-001",
  "project_id": "PROJECT-001",
  "task_id": "IMPL-001",
  "attempt_id": "ATTEMPT-001",
  "attempt_number": 1,
  "contract_version": 1,
  "prompt_version": 1,

  "task": {
    "title": "",
    "objective": "",
    "context": []
  },

  "scope": {
    "allowed": [],
    "forbidden": []
  },

  "requirements": [],

  "required_tests": [],

  "acceptance_criteria": [],

  "execution_policy": {
    "max_attempts": 3,
    "stop_conditions": [],
    "commit_policy": "OPTIONAL",
    "push_policy": "FORBIDDEN"
  },

  "report_requirements": {
    "schema_version": "1.0",
    "required_sections": [
      "OUTCOME",
      "ATTEMPT",
      "SUMMARY",
      "FILES",
      "COMMANDS",
      "TESTS",
      "ERRORS",
      "LIMITATIONS",
      "DEVIATIONS",
      "UNVERIFIED_ASPECTS",
      "COMMIT",
      "PUSH"
    ]
  },

  "selected_rules": [],

  "optional_sections": {},

  "rendered_text": ""
}
```

---

# 10. Campi obbligatori del Prompt Schema v1

Devono essere sempre presenti:

```text
schema_version
prompt_id
project_id
task_id
attempt_id
attempt_number
contract_version
prompt_version
task.title
task.objective
task.context
scope.allowed
scope.forbidden
requirements
required_tests
acceptance_criteria
execution_policy.max_attempts
execution_policy.stop_conditions
execution_policy.commit_policy
execution_policy.push_policy
report_requirements
selected_rules
rendered_text
```

Le liste possono essere vuote solo con una motivazione strutturata.

Esempio:

```json
{
  "required_tests": [],
  "tests_not_required_reason": "Task esclusivamente documentale"
}
```

---

# 11. Campi opzionali del Prompt Schema v1

Prima versione:

```json
{
  "relevant_files": [],
  "reference_documents": [],
  "suggested_commands": [],
  "required_artifacts": [],
  "environment_constraints": [],
  "dependency_policy": {},
  "documentation_requirements": [],
  "backup_requirements": [],
  "screenshot_requirements": [],
  "approval_requirements": [],
  "notes": []
}
```

I campi opzionali diventano obbligatori quando una regola attiva ne richiede la presenza.

---

# 12. Immutabilità del prompt

Il prompt può essere modificato durante la fase di preparazione.

Una volta avviato il tentativo:

- il prompt viene congelato;
- viene calcolato un hash;
- il testo reso non può essere sovrascritto;
- una modifica sostanziale richiede un nuovo prompt;
- una modifica dopo l'avvio richiede normalmente un nuovo tentativo;
- tutte le versioni precedenti restano auditabili.

---

# 13. Report Schema v1

## 13.1 Struttura base

```json
{
  "schema_version": "1.0",
  "report_id": "REPORT-001",
  "project_id": "PROJECT-001",
  "task_id": "IMPL-001",
  "attempt_id": "ATTEMPT-001",
  "attempt_number": 1,
  "prompt_id": "PROMPT-001",
  "prompt_version": 1,

  "declared_outcome": "SUCCESS",

  "summary": "",

  "files": {
    "verified": [],
    "created": [],
    "modified": [],
    "deleted": [],
    "renamed": []
  },

  "commands": [],

  "tests": [],

  "acceptance_criteria": [],

  "errors": [],

  "limitations": [],

  "deviations": [],

  "unverified_aspects": [],

  "version_control": {
    "commit": {
      "performed": false,
      "sha": null,
      "message": null
    },
    "push": {
      "performed": false,
      "remote": null,
      "branch": null
    }
  },

  "artifacts": [],

  "approval_requests": [],

  "raw_text": ""
}
```

---

# 14. Campi obbligatori del Report Schema v1

Devono essere sempre presenti:

```text
schema_version
report_id
project_id
task_id
attempt_id
attempt_number
prompt_id
prompt_version
declared_outcome
summary
files.verified
files.created
files.modified
files.deleted
files.renamed
commands
tests
acceptance_criteria
errors
limitations
deviations
unverified_aspects
version_control.commit
version_control.push
artifacts
approval_requests
raw_text
```

Una sezione vuota deve essere espressa con un array vuoto o un valore esplicito, non omessa.

---

# 15. Campi condizionati del report

Diventano obbligatori in base alle regole.

## Commit richiesto

```text
commit_policy = REQUIRED
→ commit.performed = true
→ commit.sha valorizzato
→ commit.message valorizzato
```

## Push richiesto

```text
push_policy = REQUIRED
→ push.performed = true
→ push.remote valorizzato
→ push.branch valorizzato
```

## File riepilogativo richiesto

```text
change_summary_file = true
→ artifacts contiene CHANGE_SUMMARY
→ declared_path valorizzato
→ evidenza di esistenza obbligatoria
```

## Screenshot richiesti

```text
screenshots_required = true
→ artifacts contiene almeno uno SCREENSHOT
```

## Documentazione richiesta

```text
documentation_update_required = true
→ file documentali dichiarati
→ verifica Git dei file
```

---

# 16. Valori chiusi

Gli stati devono usare vocabolari chiusi.

## Test e verifiche

```text
PASSED
FAILED
NOT_RUN
BLOCKED
UNKNOWN
```

## Riconciliazione

```text
MATCH
MISMATCH
PARTIAL
NOT_APPLICABLE
UNKNOWN
```

## Esito dichiarato

```text
SUCCESS
PARTIAL_SUCCESS
FAILED
BLOCKED
TECHNICAL_FAILURE
```

Le spiegazioni devono stare in campi separati.

Le emoji non devono essere salvate nel JSON.

---

# 17. Identificatori condivisi

Gli elementi devono usare ID stabili:

```text
PROJECT-001
IMPL-001
CONTRACT-001
ATTEMPT-001
PROMPT-001
REPORT-001
RULE-001
TEST-001
AC-001
CMD-001
ARTIFACT-001
EVIDENCE-001
RECON-001
VERIFY-001
APPROVAL-001
```

Esempio:

- il prompt richiede `TEST-001`;
- il report dichiara `TEST-001`;
- le evidenze registrano `TEST-001`;
- la riconciliazione confronta `TEST-001`;
- la verifica usa `TEST-001` per decidere il criterio collegato.

---

# 18. Regola dei tentativi

## 18.1 Quando il tentativo non è ancora iniziato

La creazione o modifica del prompt non consuma un tentativo.

Non consumano un tentativo:

- generazione del prompt;
- correzione del prompt;
- validazione fallita;
- campo obbligatorio mancante;
- dipendenza non soddisfatta;
- repository non disponibile;
- snapshot non riuscito;
- annullamento prima dell'avvio;
- errore nella generazione del prompt.

---

# 19. Condizioni per avviare un tentativo

Il tentativo può partire solo quando:

1. la task è valida;
2. il Task Contract è valido;
3. le regole obbligatorie sono compilate;
4. il prompt strutturato è valido;
5. il prompt testuale è stato generato;
6. il prompt è stato congelato;
7. il preflight è superato;
8. lo snapshot iniziale è stato acquisito;
9. esistono tentativi disponibili;
10. l'utente seleziona esplicitamente `Avvia tentativo`.

Evento formale:

```json
{
  "event_type": "ATTEMPT_STARTED",
  "attempt_id": "ATTEMPT-001",
  "attempt_number": 1,
  "prompt_id": "PROMPT-001",
  "prompt_hash": "...",
  "snapshot_id": "SNAPSHOT-001",
  "started_at": "..."
}
```

Da questo momento il tentativo è consumato.

---

# 20. Fallimento tecnico dopo l'avvio

Dopo `ATTEMPT_STARTED`, il tentativo è normalmente consumato anche in caso di:

- sessione interrotta;
- crash dell'esecutore;
- indisponibilità del provider;
- perdita del collegamento;
- mancata produzione del report.

Stato consigliato:

```json
{
  "status": "TECHNICAL_FAILURE",
  "consumed": true
}
```

Un'eccezione può rendere il fallimento non consumante solo tramite decisione umana registrata:

```json
{
  "exception_type": "NON_CONSUMING_TECHNICAL_FAILURE",
  "approved_by": "HUMAN",
  "reason": "Sessione mai effettivamente avviata"
}
```

---

# 21. Quando un tentativo è superato

L'esito dichiarato dall'esecutore non è sufficiente.

Il tentativo è superato solo se:

1. il report è ricevuto;
2. il report è valido;
3. tutti i campi obbligatori sono presenti;
4. le evidenze sono state raccolte;
5. i test obbligatori risultano superati;
6. i criteri di accettazione risultano superati;
7. non esistono modifiche fuori scope bloccanti;
8. commit e push rispettano le policy;
9. gli artefatti richiesti esistono;
10. non esistono deviazioni bloccanti;
11. non esistono mismatch bloccanti;
12. la verifica restituisce `PASSED`.

Esempio:

```json
{
  "verification_status": "PASSED"
}
```

Solo la verifica può determinare il superamento del tentativo.

---

# 22. Quando un tentativo fallisce

Il tentativo fallisce quando una condizione obbligatoria non è soddisfatta.

Esempi:

```text
test obbligatorio fallito
file fuori scope
push vietato ma eseguito
commit richiesto ma assente
SHA dichiarato diverso da quello osservato
artefatto obbligatorio assente
report incompleto
criterio di accettazione fallito
evidenze insufficienti
mismatch bloccante
```

Esempio:

```json
{
  "verification_status": "FAILED",
  "blocking_checks": [
    "PUSH_POLICY",
    "FILES_SCOPE"
  ]
}
```

---

# 23. Avvio di un nuovo tentativo

Un nuovo tentativo non deve partire automaticamente.

Prima devono essere soddisfatte queste condizioni:

1. il tentativo precedente è chiuso;
2. il report è stato acquisito oppure l'assenza è stata registrata;
3. la raccolta evidenze è conclusa;
4. la riconciliazione è conclusa;
5. la verifica ha prodotto un esito;
6. esistono tentativi residui;
7. è stata decisa la gestione delle modifiche residue;
8. è stato preparato un nuovo prompt;
9. il nuovo prompt è stato congelato;
10. è stato acquisito un nuovo snapshot;
11. l'utente seleziona `Avvia nuovo tentativo`.

---

# 24. Gestione delle modifiche residue

Prima del nuovo tentativo il sistema deve richiedere una decisione:

```text
RESTORE_PREVIOUS_SNAPSHOT
APPROVE_AS_NEW_BASELINE
KEEP_AS_PARTIAL_WORK
BLOCK_FOR_HUMAN_REVIEW
```

## RESTORE_PREVIOUS_SNAPSHOT

Ripristina lo stato precedente al tentativo.

## APPROVE_AS_NEW_BASELINE

Conserva le modifiche e le approva come nuova base.

## KEEP_AS_PARTIAL_WORK

Conserva le modifiche ma le considera lavoro parziale non approvato.

## BLOCK_FOR_HUMAN_REVIEW

Blocca la task finché un umano non decide.

---

# 25. Stati preliminari del tentativo

Prima versione consigliata:

```text
DRAFT
READY
IN_PROGRESS
AWAITING_REPORT
COLLECTING_EVIDENCE
IN_RECONCILIATION
IN_VERIFICATION
VERIFIED_PASSED
VERIFIED_FAILED
BLOCKED
TECHNICAL_FAILURE
CANCELLED
```

Stati terminali:

```text
VERIFIED_PASSED
VERIFIED_FAILED
BLOCKED
TECHNICAL_FAILURE
CANCELLED
```

La macchina a stati definitiva verrà implementata nella task dedicata, ma questa baseline deve guidare i futuri schemi.

---

# 26. Presentazione nella UI

La UI può mostrare le regole come:

```text
Regole fisse

[✓ bloccato] Identificativo task
[✓ bloccato] Numero tentativo
[✓ bloccato] Elenco file modificati
[✓ bloccato] Errori e limiti
```

```text
Regole configurabili

Commit:      REQUIRED
Push:        FORBIDDEN
Tentativi:   3
File riepilogo modifiche: SÌ
Screenshot:  NO
Nuove dipendenze: VIETATE
```

Riepilogo verifica:

```text
Obiettivo definito           PASSED
Scope rispettato             PASSED
Report completo              FAILED
Test obbligatori             PASSED
Commit conforme              PASSED
Push conforme                PASSED
Artefatti richiesti          PARTIAL
```

La UI traduce gli stati in:

- icone;
- check;
- colori;
- badge;
- dropdown;
- sezioni espandibili.

I dati restano però testuali e strutturati, senza emoji nel database.

---

# 27. Persistenza futura

La persistenza consigliata è ibrida.

## Tabelle relazionali

```text
projects
tasks
task_contracts
task_rules
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

## Payload JSON

Usati per:

- regole configurate;
- prompt strutturato;
- report strutturato;
- risultati variabili;
- export;
- compatibilità futura.

## Testi originali

Devono essere conservati separatamente:

```text
prompt.rendered_text
report.raw_text
```

Non è consigliato salvare l'intero progetto in un unico JSON.

---

# 28. Decisioni considerate approvate come baseline

La seguente direzione è sufficientemente solida per iniziare TODO-0003:

1. Rule Catalog versionato;
2. regole fisse, selezionabili e personalizzate;
3. Prompt Schema v1;
4. Report Schema v1;
5. policy commit e push a tre stati;
6. ID condivisi;
7. testo originale più dati strutturati;
8. tentativo collegato a prompt, report ed evidenze;
9. avvio esplicito del tentativo;
10. tentativo consumato dopo `ATTEMPT_STARTED`;
11. superamento deciso dalla verifica;
12. nuovo tentativo non automatico;
13. persistenza relazionale più JSON;
14. UI alimentata da stati strutturati;
15. nessuna emoji salvata come valore di dominio.

---

# 29. Aspetti non bloccanti rinviabili

I seguenti dettagli possono essere definiti durante o dopo TODO-0003 senza bloccarne l'avvio:

- elenco completo di tutte le regole disponibili;
- limiti numerici definitivi per `max_attempts`;
- struttura SQL finale;
- JSON Schema completo;
- nomenclatura definitiva di ogni stato;
- formato grafico finale della UI;
- parser del report testuale;
- riconciliazione completa;
- macchina a stati eseguibile;
- generatore automatico dei prompt;
- verifica Git completa;
- supporto a provider differenti.

---

# 30. Decisione finale sull'avvio di TODO-0003

Con questa baseline, TODO-0003 può iniziare.

La task dovrà implementare e documentare:

```text
formattazione
lint
test Rust
test TypeScript
naming
gestione errori
logging
convenzioni migrazioni
regola dei tre tentativi
formato report di sviluppo
comandi di verifica
```

Durante TODO-0003 non devono ancora essere implementati:

```text
database SQLite completo
schema SQL definitivo
generatore automatico prompt
importatore report
reconciliation engine
verifica automatica completa
UI definitiva delle regole
state machine definitiva
```

TODO-0003 dovrà però rispettare le decisioni di questo documento e non introdurre convenzioni incompatibili con esse.

---

# 31. Criterio di chiusura della baseline preliminare

La fase di discussione preliminare è considerata sufficiente quando:

- il documento è approvato;
- viene salvato nel repository;
- viene registrato nel Document Registry;
- il brief di TODO-0003 lo cita come riferimento;
- eventuali future modifiche passano tramite una nuova versione del documento.

A quel punto non sono necessarie altre discussioni architetturali bloccanti prima dell'esecuzione di TODO-0003.
