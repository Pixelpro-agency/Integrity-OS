# Project Integrity OS
## Document Registry — v0.3

**Funzione:** indice autorevole dei documenti di progetto.  
**Regola:** la colonna `Autorevole` stabilisce se il documento deve essere usato per il lavoro corrente.

| ID | Categoria | Documento | Versione | Stato | Autorevole | Sostituisce | Task | Percorso previsto | Note |
|---|---|---|---|---|---|---|---|---|---|
| DOC-001 | Flussi | Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md | v0.2 | FROZEN | Sì | Project_Integrity_OS_Flussi_MVP_v0_1.md | Globale | docs/00-current/ | Specifica funzionale congelata |
| DOC-002 | To-Do | Project_Integrity_OS_TODO_MVP_v0_4.md | v0.4 | SUPERSEDED | No | Project_Integrity_OS_TODO_MVP_v0_3.md | Globale | docs/20-history/todo/ | Stato durante l’esecuzione di TODO-0002 |
| DOC-003 | Modalità | Project_Integrity_OS_Modalita_Esecuzione_v0_1.md | v0.1 | ACTIVE | Sì | — | Globale | docs/00-current/ | Browser, desktop/local, orchestratore/API |
| DOC-004 | Brief | Project_Integrity_OS_Brief_TODO-0002_v0_2_ACTIVE.md | v0.2 | SUPERSEDED | No | Project_Integrity_OS_Brief_TODO-0002_v0_1_SUPERSEDED.md | TODO-0002 | docs/10-executions/TODO-0002/superseded/ | Versione effettivamente utilizzata durante l’esecuzione |
| DOC-005 | Prompt | Project_Integrity_OS_Prompt_Esecutivo_Browser_TODO-0002.md | n.d. | FINAL | Sì, come storico della task | Project_Integrity_OS_Prompt_Esecutivo_TODO-0002.md | TODO-0002 | docs/10-executions/TODO-0002/instructions/ | Prompt realmente utilizzato |
| DOC-006 | Start Here | START_HERE_Browser_Project_Integrity_OS_TODO-0002.md | n.d. | FINAL | Sì, come storico della task | START_HERE_Project_Integrity_OS_TODO-0002.md | TODO-0002 | docs/10-executions/TODO-0002/instructions/ | Procedura realmente utilizzata |
| DOC-007 | Brief | Project_Integrity_OS_Brief_TODO-0002_v0_1_SUPERSEDED.md | v0.1 | SUPERSEDED | No | — | TODO-0002 | docs/10-executions/TODO-0002/superseded/ | Riferiva la To-Do v0.2 |
| DOC-008 | Prompt | Project_Integrity_OS_Prompt_Esecutivo_TODO-0002.md | n.d. | SUPERSEDED | No, nella modalità corrente | — | TODO-0002 | docs/10-executions/TODO-0002/superseded/ | Variante desktop/local |
| DOC-009 | Start Here | START_HERE_Project_Integrity_OS_TODO-0002.md | n.d. | SUPERSEDED | No, nella modalità corrente | — | TODO-0002 | docs/10-executions/TODO-0002/superseded/ | Avvio precedente |
| DOC-010 | Flussi | Project_Integrity_OS_Flussi_MVP_v0_1.md | v0.1 | SUPERSEDED | No | — | Globale | docs/20-history/flows/ | Prima versione dei flussi |
| DOC-011 | To-Do | Project_Integrity_OS_TODO_MVP_v0_1.md | v0.1 | SUPERSEDED | No | — | Globale | docs/20-history/todo/ | Storico |
| DOC-012 | To-Do | Project_Integrity_OS_TODO_MVP_v0_2.md | v0.2 | SUPERSEDED | No | v0.1 | Globale | docs/20-history/todo/ | Storico |
| DOC-013 | To-Do | Project_Integrity_OS_TODO_MVP_v0_3.md | v0.3 | SUPERSEDED | No | v0.2 | Globale | docs/20-history/todo/ | Storico |
| DOC-014 | Concetto | sistema_integrita_continuita_progetto_v0_1.md | v0.1 | SUPERSEDED | No | — | Globale | docs/20-history/concept/ | Evoluzione concettuale |
| DOC-015 | Concetto | sistema_integrita_continuita_progetto_v0_2.md | v0.2 | SUPERSEDED | No | v0.1 | Globale | docs/20-history/concept/ | Evoluzione concettuale |
| DOC-016 | Concetto | sistema_integrita_continuita_progetto_v0_3.md | v0.3 | SUPERSEDED | No | v0.2 | Globale | docs/20-history/concept/ | Evoluzione concettuale |
| DOC-017 | Concetto | sistema_integrita_continuita_progetto_v0_4.md | v0.4 | SUPERSEDED | No | v0.3 | Globale | docs/20-history/concept/ | Evoluzione concettuale |
| DOC-018 | Concetto | sistema_integrita_continuita_progetto_v0_5.md | v0.5 | SUPERSEDED | No | v0.4 | Globale | docs/20-history/concept/ | Evoluzione concettuale |
| DOC-019 | Concetto | sistema_integrita_continuita_progetto_v0_6.md | v0.6 | SUPERSEDED | No | v0.5 | Globale | docs/20-history/concept/ | Ultima versione concettuale prima dei flussi operativi |
| DOC-020 | To-Do | Project_Integrity_OS_TODO_MVP_v0_5.md | v0.5 | ACTIVE | Sì | Project_Integrity_OS_TODO_MVP_v0_4.md | Globale | docs/00-current/ | TODO-0002 chiusa; TODO-0003 non avviata |
| DOC-021 | Brief | Project_Integrity_OS_Brief_TODO-0002_v0_3_FINAL.md | v0.3 | FINAL | Sì, come fonte finale della task | Project_Integrity_OS_Brief_TODO-0002_v0_2_ACTIVE.md | TODO-0002 | docs/10-executions/TODO-0002/instructions/ | Brief finale di chiusura |
| DOC-022 | Report | Project_Integrity_OS_Report_Esecutivo_TODO-0002_v0_1.md | v0.1 | FINAL | Sì, come dichiarazione dell’esecutore | — | TODO-0002 | docs/10-executions/TODO-0002/reports/ | Report della chat esecutiva |
| DOC-023 | Verifica | Project_Integrity_OS_Verifica_Indipendente_TODO-0002_v0_1.md | v0.1 | FINAL | Sì | — | TODO-0002 | docs/10-executions/TODO-0002/reports/ | Verifica amministratore e controlli ripetibili |
| DOC-024 | Approvazione | Project_Integrity_OS_Approvazione_Umana_TODO-0002_v0_1.md | v0.1 | FINAL | Sì | — | TODO-0002 | docs/10-executions/TODO-0002/validation/approvals/ | Approvazione e autorizzazione commit |
| DOC-025 | Deviazione | Project_Integrity_OS_Deviazione_DEV-TODO-0002-001_v0_1.md | v0.1 | ACCEPTED | Sì | — | TODO-0002 | docs/10-executions/TODO-0002/validation/exceptions/ | Build installer temporanea, poi rimossa |
| DOC-026 | Organizzazione | Project_Integrity_OS_Organizzazione_Documenti_v0_1.md | v0.1 | ACTIVE | Sì, per l’organizzazione documentale | — | Globale | docs/00-current/ | Regole di classificazione, versionamento e archiviazione |
| DOC-027 | Script di chiusura | Project_Integrity_OS_Chiusura_TODO-0002_v0_1_EXECUTED.py | v0.1 | EXECUTED | Sì, come evidenza operativa | — | TODO-0002 | docs/10-executions/TODO-0002/instructions/closure/ | Script realmente eseguito per la chiusura documentale |
| DOC-028 | Istruzioni di chiusura | START_HERE_Chiusura_TODO-0002_v0_1_EXECUTED.md | v0.1 | EXECUTED | Sì, come storico operativo | — | TODO-0002 | docs/10-executions/TODO-0002/instructions/closure/ | Istruzioni realmente utilizzate per la chiusura |
| DOC-029 | Registro | Project_Integrity_OS_Document_Registry_v0_1.md | v0.1 | SUPERSEDED | No | — | Globale | docs/20-history/registry/ | Prima versione del registro documentale |
| DOC-030 | Registro | Project_Integrity_OS_Document_Registry_v0_2.md | v0.2 | SUPERSEDED | No | Project_Integrity_OS_Document_Registry_v0_1.md | Globale | docs/20-history/registry/ | Registro prodotto durante la chiusura di TODO-0002 |
| DOC-031 | Registro | Project_Integrity_OS_Document_Registry_v0_3.md | v0.3 | ACTIVE | Sì | Project_Integrity_OS_Document_Registry_v0_2.md | Globale | docs/00-current/ | Registro documentale corrente della baseline TODO-0002 |

---

## Regole di aggiornamento

Quando nasce una nuova versione:

1. aggiungere una nuova riga;
2. marcare la precedente `SUPERSEDED`;
3. aggiornare `Autorevole`;
4. indicare `Sostituisce`;
5. spostare il file nel percorso coerente;
6. non cancellare la riga storica.

Quando una task termina:

- prompt e brief restano legati alla task;
- report ed evidenze vengono aggiunti sotto la stessa cartella;
- il documento corrente non viene riscritto retroattivamente;
- eventuali correzioni generano una nuova versione.
