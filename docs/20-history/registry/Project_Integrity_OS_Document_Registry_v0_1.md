# Project Integrity OS
## Document Registry — v0.1

**Funzione:** indice autorevole dei documenti di progetto.  
**Regola:** la colonna `Autorevole` stabilisce se il documento deve essere usato per il lavoro corrente.

| ID | Categoria | Documento | Versione | Stato | Autorevole | Sostituisce | Task | Percorso previsto | Note |
|---|---|---|---|---|---|---|---|---|---|
| DOC-001 | Flussi | Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md | v0.2 | FROZEN | Sì | Project_Integrity_OS_Flussi_MVP_v0_1.md | Globale | docs/00-current/ | Specifica funzionale congelata |
| DOC-002 | To-Do | Project_Integrity_OS_TODO_MVP_v0_4.md | v0.4 | ACTIVE | Sì | Project_Integrity_OS_TODO_MVP_v0_3.md | Globale | docs/00-current/ | To-Do operativa corrente |
| DOC-003 | Modalità | Project_Integrity_OS_Modalita_Esecuzione_v0_1.md | v0.1 | ACTIVE | Sì | — | Globale | docs/00-current/ | Browser, desktop/local, orchestratore/API |
| DOC-004 | Brief | Project_Integrity_OS_Brief_TODO-0002_v0_2_ACTIVE.md | v0.2 | ACTIVE | Sì | Project_Integrity_OS_Brief_TODO-0002_v0_1_SUPERSEDED.md | TODO-0002 | docs/00-current/ | Deve riferirsi alla To-Do v0.4 |
| DOC-005 | Prompt | Project_Integrity_OS_Prompt_Esecutivo_Browser_TODO-0002.md | n.d. | ACTIVE | Sì, per TODO-0002 | Project_Integrity_OS_Prompt_Esecutivo_TODO-0002.md | TODO-0002 | docs/10-executions/TODO-0002/instructions/ | Modalità browser con operatore |
| DOC-006 | Start Here | START_HERE_Browser_Project_Integrity_OS_TODO-0002.md | n.d. | ACTIVE | Sì, per TODO-0002 | START_HERE_Project_Integrity_OS_TODO-0002.md | TODO-0002 | docs/10-executions/TODO-0002/instructions/ | Procedura di avvio browser |
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
