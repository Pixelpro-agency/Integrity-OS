# Project Integrity OS

## Brief esecutivo — TODO-0101 — v0.1 — SUPERSEDED

**Stato:** `SUPERSEDED — DO_NOT_EXECUTE`
**Data di superamento:** 2026-08-06
**Task:** `TODO-0101 — Definire schema dati minimo`
**Versione originaria:** `v0.1 DRAFT`
**Motivo:** il brief precede `DEC-0101-001` → `DEC-0101-020` e i Correction Set `v0.1` e `v0.2`.

---

# 1. Avvertenza

```text
DO_NOT_EXECUTE
DO_NOT_PROMOTE_TO_ACTIVE
DO_NOT_USE_AS_SCHEMA SOURCE
```

Il file è conservato esclusivamente per tracciabilità storica.

Git conserva il contenuto originario e le modifiche precedenti.

---

# 2. Incompatibilità principali

La versione originaria:

- trattava `task_executions` come tentativi;
- non modellava `attempts`;
- usava `display_id` invece del `reference_code` canonico;
- collegava direttamente report, evidence e verification alla task execution;
- modellava bugs fuori dal registro comune;
- non usava project root entity;
- non usava `project_entities` ed `entity_versions`;
- non distingueva system catalog, global registry e project database;
- non definiva binding globali code/version/hash;
- non definiva report ownership;
- non definiva Context Package, summary, requirements e test come identità versionate complete;
- non conservava lo storico completo delle validation;
- conteneva cardinalità rigide incompatibili con i draft;
- richiedeva un documento monolitico prima del consolidamento dei deliverable.

---

# 3. Documenti sostitutivi

Il perimetro corrente è governato da:

- Decision Log v0.7;
- Correction Set v0.2;
- documenti decisionali 01–15 correnti;
- futuro Schema Architecture;
- futuro Entity Catalog;
- futuro Data Dictionary;
- futura Relationship Matrix;
- futuro Constraint Catalog;
- futuro State and Transition Catalog;
- futura Portability Matrix;
- futura Implementation Wave Matrix;
- futuro brief esecutivo riscritto.

---

# 4. Uso consentito

Il documento può essere usato soltanto per:

- ricostruire l'evoluzione;
- verificare perché alcune scelte sono state sostituite;
- confrontare il brief finale con la bozza iniziale.

Non può essere usato per:

- creare un prompt esecutivo;
- portare TODO-0101 a READY;
- implementare SQL;
- giudicare completezza del modello corrente.

---

# 5. Stato finale

```text
SUPERSEDED
HISTORICAL
NON_AUTHORITATIVE
NON_EXECUTABLE
```
