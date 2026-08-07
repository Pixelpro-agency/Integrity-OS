# Project Integrity OS

## Correction Set — TODO-0101 — v0.1

**Stato:** DRAFT — correzioni richieste e applicate ai documenti candidati
**Data:** 2026-08-06
**Ambito:** correzione delle incongruenze rilevate dopo `DEC-0101-001`–`DEC-0101-020`
**Sostituisce:** nessuna decisione; raffina e rende coerenti le decisioni già approvate

---

# 1. Scopo

Questo correction set risolve cinque incongruenze senza riaprire l'intera architettura.

```text
C-0101-001 — cardinalità strutturali vs condizioni di lifecycle
C-0101-002 — ownership autorevole dei report
C-0101-003 — BUG nel registro comune
C-0101-004 — identità root del progetto
C-0101-005 — cataloghi di sistema vs configurazioni di progetto
```

---

# 2. C-0101-001 — Cardinalità e lifecycle

## Problema

Alcune relazioni erano espresse come `1..N` anche negli stati nei quali i figli possono non essere ancora stati creati.

## Correzione

Il modello distingue formalmente:

```text
CARDINALITÀ STRUTTURALE
```

da:

```text
CARDINALITÀ MINIMA DI TRANSIZIONE
```

La cardinalità strutturale rappresenta ciò che può esistere in qualunque stato valido del record.

La cardinalità minima di transizione rappresenta ciò che deve esistere prima del passaggio verso uno stato specifico.

Esempio:

```text
TASK 1 ── 0..1 TASK_CONTRACT
```

Condizioni:

```text
TASK → DEFINED
richiede Task Contract con almeno una versione DRAFT

TASK → READY
richiede una Task Contract version FROZEN
```

La stessa regola viene applicata a Context Package, test run, verification, validation, decision options, baseline, summary, reconciliation, integrity run e transition execution.

---

# 3. C-0101-002 — Ownership dei report

## Problema

La relazione `ATTEMPT N ── M REPORTS` consentiva allo stesso execution report di essere il report autorevole di più attempt.

## Correzione

Ogni report possiede esattamente un owner autorevole.

```text
REPORT 1 ── 1 REPORT_OWNERSHIP
OWNER ENTITY 1 ── 0..N REPORTS
```

`report_ownerships` è una relazione fondamentale e dedicata.

Esempi:

```text
EXECUTION_REPORT → owning ATTEMPT
VERIFICATION_REPORT → owning VERIFICATION
VALIDATION_REPORT → owning VALIDATION
INTEGRITY_REPORT → owning INTEGRITY_RUN
RECOVERY_REPORT → owning RECOVERY_RUN o TRANSITION_RECOVERY_RUN
```

`report_subjects` conserva soltanto soggetti aggiuntivi e non modifica l'ownership.

Un execution report non può appartenere autorevolmente a più attempt.

---

# 4. C-0101-003 — BUG nel registro comune

## Problema

`bugs` era stato modellato come specializzazione di `register_items`, ma `BUG` mancava dal catalogo dei tipi.

## Correzione

Il catalogo canonico diventa:

```text
OPEN_QUESTION
ASSUMPTION
RISK
FINDING
CONFLICT
BUG
```

Ogni `BUG` possiede:

- un record `register_items`;
- almeno una `register_item_version`;
- un record 1:1 nella tabella specializzata `bugs`.

La trasformazione da finding a bug crea un nuovo register item collegato tramite una relazione esplicita; non modifica il tipo del finding originario.

---

# 5. C-0101-004 — Identità root del progetto

## Problema

Il progetto era citabile come target, ma non era definito come venisse rappresentato nel catalogo universale.

## Correzione

Ogni progetto possiede un root entity record.

```text
projects.project_id = project_entities.entity_id
project_entities.project_id = projects.project_id
project_entities.entity_type = PROJECT
```

La riga root:

- è unica per progetto;
- usa lo stesso UUID tecnico del progetto;
- usa lo stesso `reference_code`;
- rende il progetto citabile da decision target, approval subject, objective scope, event subject e relazioni governate;
- non introduce una FK circolare da `projects` verso `project_entities`.

Il core crea `projects` e la root entity nella stessa transazione.

Una integrity rule verifica l'esistenza e l'unicità della root entity.

---

# 6. C-0101-005 — Cataloghi globali e configurazioni locali

## Problema

Permessi, ruoli, transition definitions, classification levels e altri cataloghi erano talvolta globali e talvolta project-scoped.

## Correzione

Il modello distingue:

```text
SYSTEM CATALOG
```

da:

```text
PROJECT-LOCAL GOVERNED CONFIGURATION
```

## System catalog

Non possiede `project_id` e non è un `project_entity`.

Esempi:

```text
permissions
classification_levels
handling_flag_definitions
event_types
relationship_type_templates
role_templates
transition_templates
integrity_rule_templates
```

Usa codici stabili e versioni di prodotto.

## Configurazione locale

Possiede `project_id`, può essere citabile e viene versionata nel progetto.

Esempi:

```text
roles
role_versions
transition_definitions
transition_definition_versions
integrity_rules
integrity_rule_versions
access_policies
approval_policies
retention_policies
redaction_profiles
```

Può avere un riferimento opzionale al template globale da cui deriva.

La configurazione locale congelata resta riproducibile anche se il catalogo di sistema viene aggiornato.

## Attori

`actors` rappresenta identità globali o tecniche e non possiede `project_id`.

L'appartenenza al progetto è rappresentata da:

```text
project_memberships
```

I ruoli vengono assegnati nel perimetro del progetto tramite:

```text
actor_role_assignments
```

---

# 7. Documenti corretti

```text
08 — Registro Elementi Irrisolti v0.2
10 — Integrità Trasversale Anti-Orfano v0.2
12 — Ruoli Permessi Sensibilità Redazione v0.2
14 — Cardinalità Tabelle Associative v0.2
15 — Schema Completo Implementazione Progressiva v0.2
Decision Log v0.6
Checkpoint Index v0.6
README TODO-0101
```

---

# 8. Criteri di verifica

Il correction set è verificato quando:

- le versioni `v0_1` sostituite sono nello storico;
- le versioni `v0_2` sono i documenti correnti;
- il Decision Log corrente è `v0_6`;
- il checkpoint corrente è `v0_6`;
- non esistono link correnti verso `docs/00-current` per questi documenti;
- il progetto è esplicitamente una root entity;
- `BUG` è presente nel catalogo;
- ogni report ha un solo owner;
- i cataloghi globali sono separati dalle configurazioni locali;
- le cardinalità lifecycle-dependent sono condizioni di transizione;
- `git diff --check` termina senza errori.
