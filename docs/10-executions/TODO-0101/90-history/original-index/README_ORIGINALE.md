# Project Integrity OS — TODO-0101

## Indice operativo della task

**Task:** `TODO-0101 — Definire schema dati minimo`
**Stato:** `IN_ANALYSIS — CONSOLIDAMENTO DECISIONALE INTEGRATO, DELIVERABLE FINALI PENDENTI`
**Repository:** `Pixelpro-agency/Integrity-OS`
**Branch autorevole:** `main`
**Commit di integrazione:** `382c96f1f93de4ef6003f92db209675ab36d3c3c`
**Decisioni:** `DEC-0101-001` → `DEC-0101-020`
**Correction Set:** `C-0101-001` → `C-0101-009` — applicato
**Audit documentale:** completato il 2026-08-06

---

# 1. Blocco operativo

Il brief `v0.1` è superato.

```text
DO_NOT_EXECUTE
SUPERSEDED_PENDING_FINAL_REWRITE
```

Nessuna implementazione SQLite deve iniziare prima della produzione, verifica e approvazione dei deliverable finali di TODO-0101.

---

# 2. Documenti decisionali correnti

1. [Principi di tracciabilità e contesto v0.2](analysis/decisions/Project_Integrity_OS_01_Principi_Tracciabilita_Contesto_TODO-0101_v0_2_DRAFT.md)
2. [Modello gerarchico e contesto v0.2](analysis/decisions/Project_Integrity_OS_02_Modello_Gerarchico_Contesto_TODO-0101_v0_2_DRAFT.md)
3. [Context Package v0.2](analysis/decisions/Project_Integrity_OS_03_Context_Package_TODO-0101_v0_2_DRAFT.md)
4. [Provenienza v0.2](analysis/decisions/Project_Integrity_OS_04_Provenienza_Informazioni_TODO-0101_v0_2_DRAFT.md)
5. [Sintesi e drill-down v0.2](analysis/decisions/Project_Integrity_OS_05_Sintesi_Drill_Down_TODO-0101_v0_2_DRAFT.md)
6. [Requisiti e test v0.2](analysis/decisions/Project_Integrity_OS_06_Requisiti_Test_Tracciabilita_TODO-0101_v0_2_DRAFT.md)
7. [Lifecycle decisioni v0.2](analysis/decisions/Project_Integrity_OS_07_Lifecycle_Decisioni_TODO-0101_v0_2_DRAFT.md)
8. [Registro elementi irrisolti v0.3](analysis/decisions/Project_Integrity_OS_08_Registro_Elementi_Irrisolti_TODO-0101_v0_3_DRAFT.md)
9. [Eventi e temporalità v0.2](analysis/decisions/Project_Integrity_OS_09_Eventi_Ricostruzione_Temporale_TODO-0101_v0_2_DRAFT.md)
10. [Integrità anti-orfano v0.3](analysis/decisions/Project_Integrity_OS_10_Integrita_Trasversale_Anti_Orfano_TODO-0101_v0_3_DRAFT.md)
11. [Conservazione e cancellazione v0.2](analysis/decisions/Project_Integrity_OS_11_Conservazione_Rettifiche_Cancellazione_TODO-0101_v0_2_DRAFT.md)
12. [Ruoli e sicurezza v0.3](analysis/decisions/Project_Integrity_OS_12_Ruoli_Permessi_Sensibilita_Redazione_TODO-0101_v0_3_DRAFT.md)
13. [Transizioni v0.2](analysis/decisions/Project_Integrity_OS_13_Transizioni_Condizioni_Complete_TODO-0101_v0_2_DRAFT.md)
14. [Cardinalità e associazioni v0.3](analysis/decisions/Project_Integrity_OS_14_Cardinalita_Tabelle_Associative_TODO-0101_v0_3_DRAFT.md)
15. [Schema completo e implementazione progressiva v0.3](analysis/decisions/Project_Integrity_OS_15_Schema_Completo_Implementazione_Progressiva_TODO-0101_v0_3_DRAFT.md)

Questi documenti sono decisioni di analisi consolidate, ma restano `DRAFT` e non sono ancora lo schema fisico autorevole.

---

# 3. Controllo e tracciabilità

- [Decision Log v0.8](analysis/decision-log/Project_Integrity_OS_Decision_Log_TODO-0101_v0_8_DRAFT.md)
- [Checkpoint Index v0.8](analysis/checkpoints/Project_Integrity_OS_Checkpoint_Index_TODO-0101_v0_8_DRAFT.md)
- [Correction Set v0.2](analysis/verification/Project_Integrity_OS_Correction_Set_TODO-0101_v0_2_DRAFT.md)
- [Open Issues Register v0.1](analysis/verification/Project_Integrity_OS_Open_Issues_Register_TODO-0101_v0_1_DRAFT.md)
- [Audit documentale v0.1](analysis/verification/Project_Integrity_OS_Audit_Documentale_TODO-0101_v0_1.md)
- [Brief v0.1 superseded](instructions/superseded/Project_Integrity_OS_Brief_TODO-0101_v0_1_SUPERSEDED.md)

---

# 4. Modello consolidato

```text
three logical scopes
→ SYSTEM_CATALOG
→ GLOBAL_REGISTRY
→ PROJECT_DATABASE

two physical SQLite databases in MVP
→ CONTROL DATABASE
→ PROJECT DATABASE

global references
→ stable code
→ catalog version
→ definition hash
→ local binding

project traceability
→ project_entities
→ entity_versions
```

---

# 5. Stato dei passaggi

```text
Correction package application: COMPLETED
Merge into main: COMPLETED
Documentation audit: COMPLETED
Schema Architecture: PENDING
Entity Catalog: PENDING
Data Dictionary: PENDING
Relationship Matrix: PENDING
Constraint Catalog: PENDING
State and Transition Catalog: PENDING
Portability Matrix: PENDING
Implementation Wave Matrix: PENDING
Final executable brief: PENDING
TODO-0101 READY: NO
```

---

# 6. Prossimo passo

```text
1. produrre Schema Architecture;
2. produrre Entity Catalog;
3. produrre Data Dictionary;
4. produrre Relationship Matrix;
5. produrre Constraint Catalog;
6. produrre State and Transition Catalog;
7. produrre Portability Matrix;
8. produrre Implementation Wave Matrix;
9. riscrivere il brief esecutivo;
10. verificare e approvare i deliverable;
11. congelare la baseline;
12. portare TODO-0101 a READY.
```
