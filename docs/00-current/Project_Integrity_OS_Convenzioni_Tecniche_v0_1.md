# Project Integrity OS

## Convenzioni tecniche — v0.1

**Stato:** baseline tecnica MVP
**Data:** 2026-08-05
**Task:** TODO-0003
**Ambito:** codice, dipendenze, test, errori, logging e verifiche.

## 1. Principi

Project Integrity OS segue un approccio deterministic-first.

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
- evitare funzionalità appartenenti a task future.

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

## 4. Rust

La baseline Rust richiede:

- `cargo fmt --manifest-path "src-tauri/Cargo.toml" --all -- --check`
- `cargo clippy --manifest-path "src-tauri/Cargo.toml" --all-targets --all-features -- -D warnings`
- `cargo test --manifest-path "src-tauri/Cargo.toml"`
- `cargo check --manifest-path "src-tauri/Cargo.toml"`

Rustfmt è la fonte unica della formattazione Rust.

Clippy deve essere eseguito su tutti i target e con tutti i warning trasformati in errori.

I test devono verificare contratti o comportamento reale, non soltanto compilazione o presenza di file.

## 5. Errori applicativi

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

## 6. Logging

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

## 7. Dipendenze

Ogni dipendenza deve essere motivata indicando:

- nome e versione;
- scopo;
- necessità;
- alternativa senza dipendenza;
- file interessati;
- impatto su build e lockfile.

Regole:

- preferire dipendenze già presenti;
- distinguere runtime e sviluppo;
- evitare major update non richiesti;
- aggiornare i lockfile con il package manager;
- non modificare manualmente i lockfile.

## 8. Verifica standard

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

## 9. Line ending

La baseline corrente adotta una politica transitoria compatibile con Windows e Git Bash:

- non normalizzare in massa i file esistenti;
- non introdurre modifiche prive di contenuto dovute soltanto agli a capo;
- conservare `endOfLine: "auto"` in Prettier durante questa baseline;
- trattare gli avvisi `LF will be replaced by CRLF` come informativi;
- richiedere una task esplicita prima di introdurre o modificare `.gitattributes`;
- controllare sempre il contenuto effettivo tramite diff prima del commit.

La rappresentazione canonica definitiva degli a capo verrà stabilita insieme a una futura migrazione controllata, evitando modifiche massive non correlate.

## 10. Git e modalità browser

Prima di applicare una patch devono essere osservati:

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
- una patch non applicata non consuma un tentativo;
- il tentativo inizia con la prima modifica applicata;
- dopo tre tentativi ragionati l'esecuzione si ferma.

## 11. Scope escluso

Questa baseline non introduce database, persistenza, migrazioni, Git inspector completo, Task Contract persistente, Prompt Generator, Report Importer, Rule Catalog UI, reconciliation engine, controlled runner completo o integrazione AI.

## 12. Conformità

Una modifica è conforme quando:

1. rispetta la separazione frontend/core;
2. è formattata;
3. non produce warning;
4. supera typecheck e build;
5. include test reali quando applicabile;
6. supera i controlli Rust;
7. non lascia artefatti generati nella root;
8. documenta le dipendenze;
9. supera `npm run verify`.
