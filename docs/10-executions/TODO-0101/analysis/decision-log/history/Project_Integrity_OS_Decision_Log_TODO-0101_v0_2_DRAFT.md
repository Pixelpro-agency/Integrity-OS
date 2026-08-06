# Project Integrity OS

## Decision Log preliminare — TODO-0101 — v0.2

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole  
**Data:** 2026-08-06  
**Task collegata:** `TODO-0101 — Definire schema dati minimo`  
**Sostituisce nel checkpoint:** `Project_Integrity_OS_Decision_Log_Pre-TODO-0101_v0_1_DRAFT.md`  
**Versione precedente conservata in:** `analysis/history/`

---

# 1. Decisioni approvate

## DEC-0101-001 — APPROVED

Separazione tra `task_executions` e `attempts`.

## DEC-0101-002 — APPROVED

UUID tecnici più `reference_code` leggibili.

## DEC-0101-003 — APPROVED

Catena completa e verificabile del ciclo di lavoro.

## DEC-0101-004 — APPROVED

Analisi, decisioni, documenti, requisiti, test e collaudi come entità persistenti di prima classe.

## DEC-0101-005 — APPROVED

Documenti conservati nel repository e come versioni immutabili nel database.

## DEC-0101-006 — APPROVED

Separazione tra `phases`, `work_items`, `tasks`, `task_executions` e `attempts`.

## DEC-0101-007 — APPROVED

Contesto gerarchico dal macroscopico al microscopico.

## DEC-0101-008 — APPROVED

Context Package persistenti, versionati, validabili, congelabili e riproducibili.

## DEC-0101-009 — APPROVED

Classificazione multidimensionale della provenienza delle informazioni.

Dimensioni:

```text
natura
acquisizione
attore
fonte
verifica
governo
confidenza
catena degli input
```

## DEC-0101-010 — APPROVED

Sintesi come artefatti derivati, versionati, verificabili e navigabili tramite drill-down.

Catena:

```text
sintesi
→ dettaglio strutturato
→ contenuto originale
→ fonti
→ evidenze
```

## DEC-0101-011 — APPROVED

Separazione formale tra obiettivi, requisiti, criteri, test definition, test run, risultati, evidenze, verifiche e collaudi.

La copertura pianificata è distinta dalla copertura osservata.

---

# 2. Principi derivati consolidati

```text
Conservare tutto non significa mostrare tutto.

Ogni sintesi mantiene accesso al dettaglio.

Ogni informazione conserva la provenienza.

Ogni risultato verificato conserva la prova.

Ogni test è collegato al requisito e al criterio.

Ogni dato storico resta immutabile o versionato.

Ogni livello è navigabile verso l’alto e verso il basso.
```

---

# 3. Documenti del checkpoint v0.2

## Documenti precedenti conservati

```text
Project_Integrity_OS_Principi_Tracciabilita_Contesto_v0_1_DRAFT.md
Project_Integrity_OS_Modello_Gerarchico_Contesto_v0_1_DRAFT.md
Project_Integrity_OS_Context_Package_v0_1_DRAFT.md
```

## Nuovi documenti

```text
Project_Integrity_OS_Provenienza_Informazioni_v0_1_DRAFT.md
Project_Integrity_OS_Sintesi_Drill_Down_v0_1_DRAFT.md
Project_Integrity_OS_Requisiti_Test_Tracciabilita_v0_1_DRAFT.md
```

---

# 4. Decisioni ancora aperte

```text
DEC-0101-012 — Lifecycle delle decisioni
DEC-0101-013 — Open questions, assumptions, risks, findings e conflicts
DEC-0101-014 — Eventi e ricostruzione temporale
DEC-0101-015 — Regole anti-orfano e integrità trasversale
DEC-0101-016 — Cancellazione, archiviazione e rettifiche
DEC-0101-017 — Ruoli, permessi, sensibilità e redazione
DEC-0101-018 — Condizioni complete delle transizioni
DEC-0101-019 — Cardinalità definitive e tabelle associative
DEC-0101-020 — Confine tra schema completo e implementazione progressiva
```

---

# 5. Stato del brief

Il brief:

```text
Project_Integrity_OS_Brief_TODO-0101_v0_1_DRAFT.md
```

non deve essere promosso ad `ACTIVE`.

Dovrà essere sostituito dopo il completamento dell’allineamento.

---

# 6. Prossimo punto

```text
DEC-0101-012
Lifecycle delle decisioni
```

Stato operativo:

```text
CHECKPOINT DOCUMENTALE COMPLETATO
→ CONTINUIAMO
```
