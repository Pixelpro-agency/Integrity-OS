# Project Integrity OS

## Decision Log preliminare — TODO-0101 — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole
**Data:** 2026-08-05
**Task collegata:** `TODO-0101 — Definire schema dati minimo`
**Scopo:** registrare le decisioni approvate prima della revisione del brief e prima dell’inserimento nei documenti correnti

---

# 1. Regola del registro

Ogni decisione deve distinguere:

```text
PROPOSED
UNDER_REVIEW
APPROVED
REJECTED
SUPERSEDED
REVOKED
```

In questo documento sono riportate soltanto decisioni approvate durante la discussione preliminare.

Il documento non modifica ancora la repository e non sostituisce i documenti autorevoli correnti.

---

# 2. DEC-0101-001

## Titolo

Separazione tra `task_executions` e `attempts`.

## Stato

```text
APPROVED
```

## Decisione

`task_executions` e `attempts` sono entità differenti.

```text
task_execution
= ciclo esecutivo complessivo affidato a un esecutore,
  modalità o sessione

attempt
= singolo tentativo numerato e consumabile
```

Prompt, snapshot, report, evidenze, riconciliazioni e verifiche si collegano al tentativo.

## Motivazione

- evitare ambiguità tra esecuzione e tentativo;
- rappresentare più tentativi nella stessa sessione;
- preservare il lifecycle approvato;
- evitare future migrazioni concettuali.

---

# 3. DEC-0101-002

## Titolo

UUID tecnici e `reference_code` leggibili.

## Stato

```text
APPROVED
```

## Decisione

Ogni entità persistente usa una chiave UUID esplicita.

Le entità citabili in UI, documenti, prompt, report, evidenze ed export possiedono anche un `reference_code`.

Le foreign key usano UUID.

Il `reference_code`:

- è stabile;
- è univoco nel progetto;
- non è riciclato;
- non viene modificato;
- non sostituisce la chiave tecnica.

## Motivazione

Combinare robustezza tecnica e leggibilità umana.

---

# 4. DEC-0101-003

## Titolo

Catena completa e verificabile del ciclo di lavoro.

## Stato

```text
APPROVED
```

## Decisione

Il sistema deve conservare la catena:

```text
analisi
→ decisioni
→ documentazione
→ fase
→ To-Do
→ task
→ contratto
→ esecuzione
→ tentativo
→ prompt
→ report
→ comandi
→ test
→ evidenze
→ riconciliazioni
→ verifiche
→ collaudi
→ approvazioni
→ chiusura
→ baseline
```

Nessun passaggio importante deve restare soltanto nella memoria della chat o dell’utente.

---

# 5. DEC-0101-004

## Titolo

Entità di governance come dati di prima classe.

## Stato

```text
APPROVED
```

## Decisione

Devono essere entità persistenti:

- analisi;
- decisioni;
- documenti;
- versioni documentali;
- requisiti;
- criteri di accettazione;
- definizioni dei test;
- esecuzioni dei test;
- collaudi.

Lo schema viene definito in `TODO-0101`.

L’implementazione viene distribuita nelle task successive.

## Motivazione

Consentire tracciabilità, query deterministiche e controlli di completezza.

---

# 6. DEC-0101-005

## Titolo

Doppia conservazione dei documenti.

## Stato

```text
APPROVED
```

## Decisione

Ogni documento logico è rappresentato da `documents`.

Ogni revisione è rappresentata da `document_versions`.

Per i documenti testuali governati, ogni versione conserva:

- contenuto;
- hash;
- provenienza;
- percorso, se presente;
- versione;
- stato;
- collegamento alla versione sostituita.

Il repository resta la rappresentazione leggibile e Git-versionata.

Il database conserva lo snapshot immutabile della versione registrata.

I file binari vengono gestiti tramite `artifacts`, storage controllato, hash e metadati.

Le divergenze non vengono riconciliate automaticamente.

---

# 7. DEC-0101-006

## Titolo

Separazione tra fase, work item, task, esecuzione e tentativo.

## Stato

```text
APPROVED
```

## Decisione

Il sistema distingue:

```text
phases
work_items
tasks
task_executions
attempts
```

- `work_items` rappresenta le voci della To-Do;
- `tasks` rappresenta unità esecutive concrete;
- `task_executions` rappresenta l’affidamento a un esecutore o sessione;
- `attempts` rappresenta i tentativi numerati.

Ogni livello possiede stato, relazioni e dipendenze proprie.

Il completamento di un livello inferiore non completa automaticamente quello superiore.

---

# 8. DEC-0101-007

## Titolo

Contesto gerarchico dal macroscopico al microscopico.

## Stato

```text
APPROVED
```

## Decisione

Il contesto deve essere organizzato dal progetto al singolo fatto osservato.

Ogni livello:

- è consultabile separatamente;
- mantiene collegamenti con i livelli superiori e inferiori;
- può essere selezionato in modo mirato;
- non richiede di leggere documenti monolitici.

Le IA ricevono soltanto il contesto pertinente, senza perdere la possibilità di risalire alle fonti.

## Principio espresso

> Dal satellite al granello di sabbia.

---

# 9. DEC-0101-008

## Titolo

Context Package persistenti e riproducibili.

## Stato

```text
APPROVED
```

## Decisione

Project Integrity OS introduce Context Package:

- persistenti;
- versionati;
- validabili;
- congelabili;
- riproducibili;
- collegati a un’entità radice;
- collegati a un destinatario e uno scopo.

Ogni pacchetto contiene:

- manifest;
- fonti e versioni;
- hash;
- modalità di inclusione;
- esclusioni;
- livelli `CORE`, `SUPPORTING`, `DEEP_REFERENCE`;
- controllo di completezza;
- hash finale.

Un pacchetto `FROZEN` è immutabile.

Una variazione delle fonti può renderlo `STALE` per usi futuri, senza alterare il valore storico.

---

# 10. Principi approvati derivati

## 10.1 Completezza senza sovraccarico

Conservare tutto non significa mostrare tutto a ogni attore.

## 10.2 Fonte primaria e sintesi

La sintesi accelera la consultazione.

La fonte originale conserva la verità storica.

## 10.3 Collegamenti bidirezionali

Ogni elemento deve poter mostrare ciò da cui deriva e ciò che influenza.

## 10.4 Anti-orfano

Il sistema deve individuare entità e relazioni incomplete.

## 10.5 Immutabilità

Correzioni e aggiornamenti creano nuove versioni o eventi.

## 10.6 Ricostruzione temporale

Deve essere possibile ricostruire lo stato valido in un momento storico.

---

# 11. Decisioni ancora aperte

Le seguenti aree devono essere discusse prima di finalizzare lo schema e il brief:

```text
DEC-0101-009 — Provenienza e classificazione delle informazioni
DEC-0101-010 — Sintesi, copertura e obsolescenza
DEC-0101-011 — Requisiti, criteri e copertura dei test
DEC-0101-012 — Lifecycle delle decisioni
DEC-0101-013 — Open questions, assumptions, risks, findings e conflicts
DEC-0101-014 — Eventi e ricostruzione temporale
DEC-0101-015 — Regole anti-orfano e integrità trasversale
DEC-0101-016 — Cancellazione, archiviazione e rettifiche
DEC-0101-017 — Ruoli, permessi, sensibilità e redazione
DEC-0101-018 — Condizioni complete delle transizioni
DEC-0101-019 — Cardinalità definitive e tabelle associative
DEC-0101-020 — Confine tra schema minimo e implementazione progressiva
```

La numerazione è preliminare e potrà essere consolidata prima dell’inserimento nella repository.

---

# 12. Impatto sul brief precedente

Il brief `Project_Integrity_OS_Brief_TODO-0101_v0_1_DRAFT.md` non deve essere promosso ad `ACTIVE`.

Dovrà essere sostituito da una nuova versione dopo la conclusione del confronto.

La nuova versione dovrà recepire tutte le decisioni approvate e distinguere:

- vincoli già presenti nei documenti autorevoli;
- decisioni architetturali approvate;
- aspetti rinviati;
- scope implementativo;
- criteri di accettazione.

---

# 13. Prossimo checkpoint

Dopo la creazione di questi documenti:

```text
CONTINUIAMO
→ DEC-0101-009
→ ulteriori decisioni
→ nuovo checkpoint documentale
→ revisione complessiva
→ inserimento nei documenti del progetto
```

Nessuna modifica deve essere applicata ai documenti correnti della repository finché l’allineamento non è concluso.
