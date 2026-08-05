# Project Integrity OS

## Convenzioni tecniche — v0.2

**Stato:** ACTIVE — baseline tecnica MVP
**Data:** 2026-08-05
**Task di origine:** TODO-0003
**Sostituisce:** `Project_Integrity_OS_Convenzioni_Tecniche_v0_1.md`
**Motivo della revisione:** completamento post-chiusura delle convenzioni di naming e delle future migrazioni, mantenendo invariata la baseline tecnica già verificata.
**Ambito:** codice, naming, dipendenze, test, errori, logging, migrazioni e verifiche.

---

## 1. Principi

Project Integrity OS segue un approccio `deterministic-first`.

Il frontend è responsabile di:

- presentazione;
- interazione;
- stato strettamente visuale;
- invocazione dei comandi Tauri;
- visualizzazione di risultati ed errori normalizzati.

Il core Rust è responsabile di:

- regole di dominio;
- contratti;
- validazione;
- transizioni autorevoli;
- errori applicativi;
- decisioni deterministiche.

Ogni modifica deve:

- avere un obiettivo circoscritto;
- evitare refactor non richiesti;
- modificare il minor numero ragionevole di file;
- preservare comportamento e dati già verificati;
- evitare funzionalità appartenenti a task future;
- distinguere sempre ciò che è dichiarato da ciò che è osservato;
- non introdurre dati, esiti o identificatori inventati.

---

## 2. Frontend

Prettier è la fonte unica della formattazione frontend.

Comandi standard:

- `npm run format`
- `npm run format:check`

Il lockfile npm non deve essere formattato manualmente.

ESLint usa Flat Config e deve:

- terminare con zero warning;
- applicare le regole TypeScript raccomandate;
- applicare le regole fondamentali degli Hooks React;
- escludere dipendenze e directory generate.

Comando standard:

- `npm run lint`

Il typecheck deve coprire codice applicativo e configurazioni Vite/Vitest.

Comando standard:

- `npm run typecheck`

Il typecheck:

- non emette JavaScript;
- non lascia file `*.tsbuildinfo` nella root;
- viene eseguito anche dallo script `build`.

La build standard è:

- `npm run build`

---

## 3. Test frontend

Il test runner standard è Vitest in modalità non interattiva.

Comando:

- `npm run test`

Un test valido deve verificare comportamento osservabile, come:

- stato iniziale;
- contenuto visibile;
- interazione;
- comando Tauri invocato;
- risultato o errore renderizzato.

Le API Tauri possono essere sostituite da mock, ma il test deve verificare nome e numero delle invocazioni rilevanti.

---

## 4. Rust

La baseline Rust richiede:

- `cargo fmt --manifest-path "src-tauri/Cargo.toml" --all -- --check`
- `cargo clippy --manifest-path "src-tauri/Cargo.toml" --all-targets --all-features -- -D warnings`
- `cargo test --manifest-path "src-tauri/Cargo.toml"`
- `cargo check --manifest-path "src-tauri/Cargo.toml"`

Rustfmt è la fonte unica della formattazione Rust.

Clippy deve essere eseguito su tutti i target e con tutti i warning trasformati in errori.

I test devono verificare contratti o comportamento reale, non soltanto compilazione o presenza di file.

---

## 5. Convenzioni di naming

### 5.1 Regola generale

I nomi devono essere:

- espliciti;
- stabili;
- coerenti con il linguaggio e con il dominio;
- privi di abbreviazioni ambigue;
- privi di numerazioni arbitrarie non documentate;
- indipendenti da dettagli temporanei dell'implementazione.

Non usare nomi generici come `data`, `item`, `thing`, `helper`, `utils`, `manager` o `misc` quando esiste un termine di dominio più preciso.

### 5.2 TypeScript e React

Usare:

- `PascalCase` per componenti React, tipi, interfacce e union type nominate;
- `camelCase` per funzioni, variabili, parametri, hook e proprietà;
- prefisso `use` per gli hook React;
- `SCREAMING_SNAKE_CASE` soltanto per costanti realmente globali e immutabili;
- suffisso `Props` per i tipi delle proprietà di un componente;
- suffisso `State` per stati espliciti e condivisi;
- suffisso `Result` per risultati strutturati;
- suffisso `Error` per tipi di errore;
- suffisso `Options` per configurazioni opzionali passate a una funzione.

I file devono seguire queste regole:

- componente React principale: `PascalCase.tsx`;
- test del componente o modulo: stesso nome con `.test.ts` o `.test.tsx`;
- hook: `useNomeEsplicito.ts`;
- configurazioni tool: naming previsto dal tool;
- moduli non React: nome coerente con l'export principale, evitando file generici accumulativi.

Un file non deve diventare un contenitore eterogeneo. Quando contiene responsabilità indipendenti, deve essere suddiviso per responsabilità reale e non per dimensione arbitraria.

### 5.3 Rust

Seguire le convenzioni idiomatiche Rust:

- `snake_case` per moduli, file, funzioni, metodi e variabili;
- `PascalCase` per struct, enum, trait e varianti di tipo;
- `SCREAMING_SNAKE_CASE` per costanti e statiche;
- nomi di modulo singolari quando rappresentano un concetto o servizio;
- nomi di errore terminanti in `Error`;
- codici errore serializzati in `SCREAMING_SNAKE_CASE`.

Le funzioni devono descrivere l'azione e l'oggetto, per esempio `load_project`, `validate_task_contract`, `build_report_summary`.

I booleani devono esprimere una condizione leggibile, per esempio `is_valid`, `has_evidence`, `can_transition`.

### 5.4 Test

Il nome di un test deve descrivere il comportamento osservato o il contratto protetto.

Forme raccomandate:

- `renders_<observable_result>`;
- `<function>_returns_<contract>`;
- `<operation>_rejects_<invalid_condition>`;
- `<transition>_is_blocked_when_<condition>`.

Evitare nomi come `test1`, `works`, `basic_test` o `should_work`.

### 5.5 Documenti e artefatti

I documenti baseline devono usare:

```text
Project_Integrity_OS_<Nome>_v<MAJOR>_<MINOR>.md
```

I documenti legati a una task devono includere l'identificatore della task:

```text
Project_Integrity_OS_<Tipo>_TODO-0003_v0_1.md
```

Le versioni già usate per decisioni o esecuzioni non devono essere sovrascritte. Una revisione sostanziale richiede:

1. nuova versione;
2. aggiornamento del Document Registry;
3. archiviazione della versione sostituita;
4. dichiarazione esplicita del documento sostituito.

### 5.6 Identificatori di dominio

Gli identificatori persistenti devono essere:

- stabili;
- univoci nel relativo ambito;
- non derivati da etichette modificabili;
- non riciclati dopo eliminazione o annullamento;
- verificabili tra prompt, report, evidenze e verifiche.

Gli esempi approvati restano:

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

La strategia definitiva di generazione verrà definita nella task che implementerà la persistenza. Questa baseline disciplina soltanto forma, stabilità e non riuso.

---

## 6. Errori applicativi

Gli errori Rust destinati al frontend devono essere serializzabili e contenere:

- `code`;
- `message`;
- `context` opzionale.

`code` deve essere stabile e serializzato in `SCREAMING_SNAKE_CASE`.

`message` deve essere sicuro da mostrare e non deve esporre:

- segreti;
- stack trace;
- percorsi locali non necessari;
- dettagli interni incontrollati.

`context` può contenere soltanto dati strutturati e sicuri.

Un errore tecnico interno può essere registrato nei log, ma il messaggio pubblico deve restare controllato.

---

## 7. Logging

Il logging Rust usa `tracing`.

Livelli minimi:

- `error`;
- `warn`;
- `info`;
- `debug`.

L'inizializzazione deve:

- essere centralizzata;
- essere tentata una sola volta;
- non generare panic se un subscriber è già installato;
- restituire un errore controllato;
- evitare segreti e payload non filtrati.

Il logging tecnico non costituisce automaticamente un audit log persistente.

I campi strutturati devono usare nomi stabili e non includere dati sensibili non necessari.

---

## 8. Dipendenze

Ogni dipendenza deve essere motivata indicando:

- nome e versione;
- ecosistema;
- runtime o sviluppo;
- scopo;
- necessità;
- alternativa senza dipendenza;
- file interessati;
- impatto su build e lockfile;
- verifica eseguita.

Regole:

- preferire dipendenze già presenti;
- distinguere runtime e sviluppo;
- evitare major update non richiesti;
- aggiornare i lockfile con il package manager;
- non modificare manualmente i lockfile;
- non introdurre una dipendenza per una funzione ottenibile chiaramente con la libreria standard, salvo motivazione osservabile.

---

## 9. Convenzioni per le future migrazioni

### 9.1 Ambito

TODO-0003 non introduce migrazioni SQL reali. Questa sezione stabilisce le regole che le task di persistenza dovranno rispettare.

### 9.2 Versionamento e naming

Ogni migrazione deve avere:

- identificatore monotono;
- nome descrittivo;
- file immutabile dopo l'applicazione in un ambiente condiviso;
- registrazione della versione dello schema;
- collegamento alla task che l'ha introdotta.

Formato raccomandato:

```text
NNNN_descrizione_in_snake_case.sql
```

Esempi:

```text
0001_create_projects.sql
0002_add_task_execution_status.sql
0003_create_evidence_indexes.sql
```

Non usare timestamp locali come unica fonte di ordinamento. La numerazione deve essere esplicita e verificata contro la sequenza esistente.

### 9.3 Immutabilità

Una migrazione già applicata o pubblicata non deve essere riscritta.

Una correzione richiede una nuova migrazione che:

- descriva il problema corretto;
- preservi la tracciabilità;
- non nasconda la sequenza storica;
- sia idempotente soltanto quando il comportamento idempotente è esplicitamente progettato e testato.

### 9.4 Transazioni

Le migrazioni devono essere transazionali quando il motore e le istruzioni coinvolte lo consentono.

Se una migrazione non può essere atomica, deve dichiarare:

- motivo;
- punti di fallimento;
- strategia di recupero;
- verifica dello stato parziale;
- procedura manuale eventualmente necessaria.

### 9.5 Migrazioni forward e rollback

La strategia predefinita è `forward-only` finché una task successiva non approva rollback automatici.

Per ogni migrazione devono essere documentati:

- precondizioni;
- trasformazione;
- postcondizioni;
- verifica;
- strategia di recupero.

Un rollback distruttivo non deve essere introdotto automaticamente. La perdita di dati richiede una decisione esplicita e registrata.

### 9.6 Compatibilità e dati

Le migrazioni devono:

- preservare i dati esistenti salvo approvazione esplicita;
- evitare dipendenza da `rowid`;
- mantenere tipi compatibili con la futura migrazione PostgreSQL quando previsto dai documenti di progetto;
- attivare e verificare le foreign key;
- separare evoluzione dello schema da importazioni o riparazioni dati quando le due operazioni hanno rischi differenti;
- non introdurre valori derivati non ricostruibili senza dichiararne la fonte.

### 9.7 Verifiche obbligatorie

Ogni migrazione reale dovrà includere almeno:

- test su database vuoto;
- test di aggiornamento dalla versione precedente;
- test di riapertura dopo la migrazione;
- verifica della versione schema;
- verifica delle foreign key;
- verifica di indici e vincoli introdotti;
- verifica di conservazione dei dati rilevanti;
- test del comportamento in caso di fallimento quando applicabile.

La task che implementerà SQLite definirà i comandi concreti e il formato definitivo del registro migrazioni.

---

## 10. Verifica standard

Gli script npm obbligatori sono:

- `format`;
- `format:check`;
- `lint`;
- `typecheck`;
- `test`;
- `build`;
- `rust:fmt:check`;
- `rust:clippy`;
- `rust:test`;
- `rust:check`;
- `verify:frontend`;
- `verify:rust`;
- `verify`.

Il comando aggregato è:

- `npm run verify`

Deve includere:

- `git diff --check` per le modifiche non staged;
- `git diff --cached --check` per le modifiche staged;
- tutte le verifiche frontend e Rust.

Prima della verifica finale, tutti i file intenzionalmente appartenenti alla task devono essere inseriti nello staging. I file locali estranei alla task non devono essere staged.

---

## 11. Line ending

La baseline corrente adotta una politica transitoria compatibile con Windows e Git Bash:

- non normalizzare in massa i file esistenti;
- non introdurre modifiche prive di contenuto dovute soltanto agli a capo;
- conservare `endOfLine: "auto"` in Prettier durante questa baseline;
- trattare gli avvisi `LF will be replaced by CRLF` come informativi;
- richiedere una task esplicita prima di introdurre o modificare `.gitattributes`;
- controllare sempre il contenuto effettivo tramite diff prima del commit.

La rappresentazione canonica definitiva degli a capo verrà stabilita insieme a una futura migrazione controllata, evitando modifiche massive non correlate.

---

## 12. Git e modalità browser

Prima di applicare modifiche devono essere osservati:

- `git status --short`;
- `git diff --stat`;
- `git diff --cached --stat`.

Le modifiche preesistenti devono essere identificate e preservate.

Sono vietati:

- reset distruttivi;
- pulizie distruttive;
- eliminazione di modifiche preesistenti;
- commit non autorizzati;
- push non autorizzati.

In modalità browser:

- l'utente esegue materialmente i comandi;
- l'output incollato costituisce evidenza;
- l'assistente prepara analisi, file completi, comandi e controlli;
- l'assistente non attribuisce all'utente azioni non osservate;
- una modifica non applicata non consuma un tentativo;
- il tentativo inizia con la prima modifica applicata;
- dopo tre tentativi ragionati l'esecuzione si ferma.

---

## 13. Scope escluso

Questa baseline non introduce:

- database;
- persistenza;
- migrazioni SQL reali;
- Git Inspector completo;
- Task Contract persistente;
- Prompt Generator;
- Report Importer;
- Rule Catalog UI;
- Reconciliation Engine;
- Controlled Process Runner completo;
- integrazione IA.

Le convenzioni per le migrazioni non autorizzano l'implementazione anticipata delle task di persistenza.

---

## 14. Conformità

Una modifica è conforme quando:

1. rispetta la separazione frontend/core;
2. usa naming coerente con questa baseline;
3. è formattata;
4. non produce warning;
5. supera typecheck e build;
6. include test reali quando applicabile;
7. supera i controlli Rust;
8. non lascia artefatti generati nella root;
9. documenta le dipendenze;
10. rispetta le convenzioni di migrazione quando applicabili;
11. supera `npm run verify`.
