# Project Integrity OS

## Open Issues Register — TODO-0101 — v0.1

**Stato:** DRAFT — issues non bloccanti per il consolidamento decisionale
**Data:** 2026-08-06

---

# 1. Regola

Gli issue elencati non riaprono le decisioni approvate.

Devono essere risolti nei deliverable finali o assegnati esplicitamente a TODO-0102/TODO-0103.

---

# 2. OI-0101-001 — UUID concrete format

**Stato:** OPEN
**Destinazione:** TODO-0102
**Bloccante per schema logico:** no
**Bloccante per DDL:** sì

Definire UUID version, canonical lowercase representation e CHECK SQLite.

---

# 3. OI-0101-002 — Canonical JSON hashing

**Stato:** OPEN
**Destinazione:** Data Dictionary / TODO-0102
**Bloccante per schema logico:** no
**Bloccante per hash implementation:** sì

Definire canonical JSON serialization, Unicode normalization e numeric representation.

---

# 4. OI-0101-003 — Timestamp validation

**Stato:** OPEN
**Destinazione:** Portability Matrix / TODO-0102

Definire precisione, formato UTC, parser e CHECK applicativi.

---

# 5. OI-0101-004 — Partial unique indexes

**Stato:** OPEN
**Destinazione:** Constraint Catalog / TODO-0102

Casi:

- un active execution per task;
- un active attempt per execution;
- un current version pointer coerente;
- una effective baseline per scope;
- un final accepted report per owner e round.

---

# 6. OI-0101-005 — Migration bootstrap tra TODO-0102 e TODO-0103

**Stato:** OPEN
**Destinazione:** Implementation Wave Matrix

Definire come TODO-0102 crea un project database prima che il global registry di TODO-0103 sia implementato.

Vincolo:

```text
nessuna fake registry row
```

Soluzione candidata:

```text
controlled bootstrap actor binding
+
later registry reconciliation
```

---

# 7. OI-0101-006 — Event hash chain serialization version

**Stato:** OPEN
**Destinazione:** Data Dictionary

Definire i campi inclusi nel preimage e la version del formato.

---

# 8. OI-0101-007 — Decimal representation

**Stato:** OPEN
**Destinazione:** Portability Matrix

Scegliere integer scaled, decimal string o altra rappresentazione governata per SQLite.

---

# 9. OI-0101-008 — Large content storage threshold

**Stato:** OPEN
**Destinazione:** Data Dictionary

Definire quando content resta nel database e quando usa managed artifact storage.

---

# 10. OI-0101-009 — Control database physical path and backup

**Stato:** OPEN
**Destinazione:** TODO-0103 / TODO-0104

Non blocca lo schema logico.

---

# 11. OI-0101-010 — Import/export record minimal fields

**Stato:** OPEN
**Destinazione:** Entity Catalog / TODO-0104

Necessario per owner canonici di import/export report, ma non per il primo vertical slice.

---

# 12. OI-0101-011 — Report owner policy governance and versioning

**Stato:** OPEN
**Destinazione:** Entity Catalog / Data Dictionary / Constraint Catalog / Implementation Wave Matrix; enforcement fisico in TODO-0102 se necessario
**Bloccante per schema logico:** no
**Bloccante per schema fisico autorevole:** sì

Le decisioni consolidate definiscono già ownership autorevole dei report, tipi canonici di report owner e, per `CLOSURE_REPORT`, la allowlist:

```text
PROJECT
PHASE
WORK_ITEM
TASK
BASELINE
```

Questo issue non riapre tali decisioni e non introduce nuovi owner canonici.

Deve definire:

- rappresentazione e versionamento di `report_owner_policies`;
- stato della policy e regola di entrata in vigore;
- modalità con cui una versione sostituisce o supersede una precedente;
- vincolo per cui un owner type è ammesso soltanto dalla policy applicabile;
- governance necessaria per aggiungere o rimuovere un owner type;
- aggiornamenti richiesti a Entity Catalog, Data Dictionary e Constraint Catalog;
- impatto su migrazioni, integrity rules e test quando cambia la allowlist;
- modalità con cui Implementation Wave Matrix assegna enforcement fisico a TODO-0102 o a una task successiva.

`PRIVATE_CHILD` non viene aggiunto alla allowlist di `CLOSURE_REPORT`.

Una futura estensione degli owner canonici deve essere una modifica governata del modello e non una conseguenza automatica dello stato `CLOSED` di una entità.

---

# 13. Chiusura

Nessun issue aperto modifica:

- separazione task execution/attempt;
- root project entity;
- global binding strategy;
- report ownership;
- validation history;
- entity classification;
- transition authority.
