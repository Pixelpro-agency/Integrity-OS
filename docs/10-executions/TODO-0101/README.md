# Project Integrity OS — TODO-0101

## Indice operativo della task

**Task:** `TODO-0101 — Definire schema dati minimo`  
**Stato:** `DRAFT — CONSOLIDAMENTO IN CORSO`  
**Repository:** `Pixelpro-agency/Integrity-OS`  
**Branch di lavoro:** `review/todo-0101-schema-20260806-023458`  
**Ultimo correction set:** `C-0101-001` → `C-0101-005`

---

# 1. Avvertenza operativa

Il brief presente in `instructions/Project_Integrity_OS_Brief_TODO-0101_v0_1_DRAFT.md` è una versione preliminare.

```text
DO_NOT_EXECUTE
SUPERSEDED_PENDING_REWRITE
```

Non deve essere usato come prompt esecutivo finché non sono completati:

- consolidamento delle decisioni;
- Schema Architecture;
- Entity Catalog;
- Data Dictionary;
- Relationship Matrix;
- Constraint Catalog;
- State and Transition Catalog;
- Portability Matrix;
- Implementation Wave Matrix;
- riscrittura del brief.

---

# 2. Documenti correnti

## Decisioni e modelli

1. [Principi di tracciabilità e contesto](analysis/decisions/Project_Integrity_OS_01_Principi_Tracciabilita_Contesto_TODO-0101_v0_1_DRAFT.md)
2. [Modello gerarchico e contesto](analysis/decisions/Project_Integrity_OS_02_Modello_Gerarchico_Contesto_TODO-0101_v0_1_DRAFT.md)
3. [Context Package](analysis/decisions/Project_Integrity_OS_03_Context_Package_TODO-0101_v0_1_DRAFT.md)
4. [Provenienza delle informazioni](analysis/decisions/Project_Integrity_OS_04_Provenienza_Informazioni_TODO-0101_v0_1_DRAFT.md)
5. [Sintesi e drill-down](analysis/decisions/Project_Integrity_OS_05_Sintesi_Drill_Down_TODO-0101_v0_1_DRAFT.md)
6. [Requisiti, test e tracciabilità](analysis/decisions/Project_Integrity_OS_06_Requisiti_Test_Tracciabilita_TODO-0101_v0_1_DRAFT.md)
7. [Lifecycle delle decisioni](analysis/decisions/Project_Integrity_OS_07_Lifecycle_Decisioni_TODO-0101_v0_1_DRAFT.md)
8. [Registro degli elementi irrisolti — v0.2](analysis/decisions/Project_Integrity_OS_08_Registro_Elementi_Irrisolti_TODO-0101_v0_2_DRAFT.md)
9. [Eventi e ricostruzione temporale](analysis/decisions/Project_Integrity_OS_09_Eventi_Ricostruzione_Temporale_TODO-0101_v0_1_DRAFT.md)
10. [Integrità trasversale e anti-orfano — v0.2](analysis/decisions/Project_Integrity_OS_10_Integrita_Trasversale_Anti_Orfano_TODO-0101_v0_2_DRAFT.md)
11. [Conservazione, rettifiche e cancellazione](analysis/decisions/Project_Integrity_OS_11_Conservazione_Rettifiche_Cancellazione_TODO-0101_v0_1_DRAFT.md)
12. [Ruoli, permessi, sensibilità e redazione — v0.2](analysis/decisions/Project_Integrity_OS_12_Ruoli_Permessi_Sensibilita_Redazione_TODO-0101_v0_2_DRAFT.md)
13. [Transizioni e condizioni complete](analysis/decisions/Project_Integrity_OS_13_Transizioni_Condizioni_Complete_TODO-0101_v0_1_DRAFT.md)
14. [Cardinalità e tabelle associative — v0.2](analysis/decisions/Project_Integrity_OS_14_Cardinalita_Tabelle_Associative_TODO-0101_v0_2_DRAFT.md)
15. [Schema completo e implementazione progressiva — v0.2](analysis/decisions/Project_Integrity_OS_15_Schema_Completo_Implementazione_Progressiva_TODO-0101_v0_2_DRAFT.md)

## Controllo e tracciabilità

- [Correction Set v0.1](analysis/verification/Project_Integrity_OS_Correction_Set_TODO-0101_v0_1_DRAFT.md)
- [Decision Log v0.6](analysis/decision-log/Project_Integrity_OS_Decision_Log_TODO-0101_v0_6_DRAFT.md)
- [Checkpoint Index v0.6](analysis/checkpoints/Project_Integrity_OS_Checkpoint_Index_TODO-0101_v0_6_DRAFT.md)

---

# 3. Storico previsto dopo l'applicazione

```text
analysis/decisions/history/
├── Project_Integrity_OS_08_..._v0_1_DRAFT.md
├── Project_Integrity_OS_10_..._v0_1_DRAFT.md
├── Project_Integrity_OS_12_..._v0_1_DRAFT.md
├── Project_Integrity_OS_14_..._v0_1_DRAFT.md
└── Project_Integrity_OS_15_..._v0_1_DRAFT.md

analysis/decision-log/history/
└── Project_Integrity_OS_Decision_Log_TODO-0101_v0_1...v0_5_DRAFT.md

analysis/checkpoints/history/
└── Project_Integrity_OS_Checkpoint_Index_TODO-0101_v0_2...v0_5_DRAFT.md
```

---

# 4. Prossimo passo

Dopo l'applicazione e la verifica del correction set:

```text
1. aggiornare il Findings Register;
2. produrre Schema Architecture;
3. produrre Entity Catalog;
4. produrre Relationship Matrix;
5. produrre Constraint Catalog;
6. riscrivere il brief TODO-0101.
```

Nessuna implementazione SQLite deve iniziare prima della chiusura documentale di `TODO-0101`.
