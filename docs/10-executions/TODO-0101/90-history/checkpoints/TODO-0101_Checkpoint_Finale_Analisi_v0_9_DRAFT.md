# Project Integrity OS

## Checkpoint Index — TODO-0101 — v0.9

**Data:** 2026-08-06  
**Stato:** DRAFT — checkpoint riallineato alla struttura documentale corrente  
**Branch autorevole:** `main`  
**Commit di integrazione osservato:** `382c96f1f93de4ef6003f92db209675ab36d3c3c`  
**Task:** `TODO-0101 — Definire schema dati minimo`  
**Stato task:** `IN_ANALYSIS`  
**Decisioni:** `DEC-0101-001` → `DEC-0101-020`  
**Correzioni:** `C-0101-001` → `C-0101-009`  
**Versione precedente:** [TODO-0101 Checkpoint Finale Analisi v0.8](../90-history/checkpoints/TODO-0101_Checkpoint_Finale_Analisi_v0_8_DRAFT.md)

---

# 1. Punto di ingresso

[README operativo TODO-0101](../README.md)

---

# 2. Documenti decisionali correnti

1. [01 — Principi di tracciabilità v0.2](../../../architecture/data-model/current/Project_Integrity_OS_01_Principi_Tracciabilita_Contesto_v0_2_DRAFT.md)
2. [02 — Modello gerarchico v0.2](../../../architecture/data-model/current/Project_Integrity_OS_02_Modello_Gerarchico_Contesto_v0_2_DRAFT.md)
3. [03 — Context Package v0.2](../../../architecture/data-model/current/Project_Integrity_OS_03_Context_Package_v0_2_DRAFT.md)
4. [04 — Provenienza v0.2](../../../architecture/data-model/current/Project_Integrity_OS_04_Provenienza_Informazioni_v0_2_DRAFT.md)
5. [05 — Sintesi e drill-down v0.2](../../../architecture/data-model/current/Project_Integrity_OS_05_Sintesi_Drill_Down_v0_2_DRAFT.md)
6. [06 — Requisiti e test v0.2](../../../architecture/data-model/current/Project_Integrity_OS_06_Requisiti_Test_Tracciabilita_v0_2_DRAFT.md)
7. [07 — Lifecycle decisioni v0.2](../../../architecture/data-model/current/Project_Integrity_OS_07_Lifecycle_Decisioni_v0_2_DRAFT.md)
8. [08 — Registro irrisolti v0.3](../../../architecture/data-model/current/Project_Integrity_OS_08_Registro_Elementi_Irrisolti_v0_3_DRAFT.md)
9. [09 — Eventi v0.2](../../../architecture/data-model/current/Project_Integrity_OS_09_Eventi_Ricostruzione_Temporale_v0_2_DRAFT.md)
10. [10 — Integrità anti-orfano v0.3](../../../architecture/data-model/current/Project_Integrity_OS_10_Integrita_Trasversale_Anti_Orfano_v0_3_DRAFT.md)
11. [11 — Conservazione v0.2](../../../architecture/data-model/current/Project_Integrity_OS_11_Conservazione_Rettifiche_Cancellazione_v0_2_DRAFT.md)
12. [12 — Ruoli e sicurezza v0.3](../../../architecture/data-model/current/Project_Integrity_OS_12_Ruoli_Permessi_Sensibilita_Redazione_v0_3_DRAFT.md)
13. [13 — Transizioni v0.2](../../../architecture/data-model/current/Project_Integrity_OS_13_Transizioni_Condizioni_Complete_v0_2_DRAFT.md)
14. [14 — Cardinalità v0.3](../../../architecture/data-model/current/Project_Integrity_OS_14_Cardinalita_Tabelle_Associative_v0_3_DRAFT.md)
15. [15 — Schema completo v0.3](../../../architecture/data-model/current/Project_Integrity_OS_15_Schema_Completo_Implementazione_Progressiva_v0_3_DRAFT.md)

---

# 3. Controllo e tracciabilità

- [Decision Log Data Model v0.8](../../../architecture/data-model/current/Project_Integrity_OS_Decision_Log_Data_Model_v0_8_DRAFT.md) — versione corrente al momento di questo checkpoint; il riallineamento del Decision Log è il punto documentale successivo.
- [Correction Set Data Model v0.2](../../../architecture/data-model/history/consolidation/Project_Integrity_OS_Correction_Set_Data_Model_v0_2_DRAFT.md)
- [Open Issues Data Model v0.1](../../../planning/Project_Integrity_OS_Open_Issues_Data_Model_v0_1_DRAFT.md)
- [Audit documentale TODO-0101 v0.1](../03-verifica-documentale/TODO-0101_Audit_Documentale_v0_1_FINAL.md) — audit storico della riorganizzazione precedente, da riclassificare in un punto successivo del piano.
- [To-Do MVP corrente v0.10](../../../00-current/Project_Integrity_OS_TODO_MVP_v0_10.md)

---

# 4. Stato consolidato

```text
Decisioni di analisi: CONSOLIDATE
Correction Set: APPLIED
Integrazione in main: OBSERVED
Baseline documentale corrente: RIALLINEAMENTO IN CORSO
Schema Architecture: NOT PRODUCED
Schema fisico autorevole: NOT APPROVED
Implementazione SQLite: BLOCKED
```

Il refactor documentale successivo a TODO-0101 non modifica le decisioni `DEC-0101-001` → `DEC-0101-020`. Questo checkpoint aggiorna esclusivamente la navigazione e il riferimento allo stato documentale corrente.

---

# 5. Prossimi deliverable

```text
1. Schema Architecture
2. Entity Catalog
3. Data Dictionary
4. Relationship Matrix
5. Constraint Catalog
6. State and Transition Catalog
7. Portability Matrix
8. Implementation Wave Matrix
9. Brief esecutivo finale
10. Approvazione e congelamento
```

---

# 6. Regola di ripresa

Riprendere da **Schema Architecture** dopo la conclusione del riallineamento documentale in corso.

Non riaprire le decisioni consolidate salvo conflitto dimostrato o nuova decisione esplicita.

Non avviare TODO-0102.
