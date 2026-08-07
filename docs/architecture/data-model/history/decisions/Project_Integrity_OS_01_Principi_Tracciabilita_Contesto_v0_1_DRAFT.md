# Project Integrity OS

## Principi di tracciabilità e gestione del contesto — v0.1

**Stato:** DRAFT — checkpoint decisionale, non ancora fonte autorevole
**Data:** 2026-08-05
**Ambito:** principi generali di continuità, tracciabilità, organizzazione e distribuzione del contesto
**Origine:** analisi preliminare di `TODO-0101 — Definire schema dati minimo`
**Relazioni:** `DEC-0101-003`, `DEC-0101-004`, `DEC-0101-005`, `DEC-0101-007`, `DEC-0101-008`

---

# 1. Scopo

Project Integrity OS deve impedire che la conoscenza necessaria a governare un progetto rimanga affidata:

- alla memoria di una chat;
- alla memoria di una persona;
- a documenti monolitici difficili da consultare;
- a testi privi di versione;
- a relazioni implicite;
- a dichiarazioni non verificate;
- alla posizione corrente di un file;
- alla disponibilità di uno specifico modello IA;
- a una sequenza di lavoro che non lascia traccia.

Il sistema deve conservare il progetto dal livello più macroscopico al singolo fatto osservato.

Principio guida:

> Dal satellite al granello di sabbia, tutto deve essere conservato, diviso, etichettato, catalogato, collegato e recuperabile.

La completezza non richiede di mostrare tutto contemporaneamente. Richiede che ogni elemento sia preservato e che il sistema possa selezionare soltanto il contesto utile a una determinata attività.

---

# 2. Principio di tracciabilità completa

Ogni elemento rilevante deve poter essere seguito:

```text
origine
→ analisi
→ decisione
→ documentazione
→ fase
→ voce della To-Do
→ task
→ contratto
→ esecuzione
→ tentativo
→ prompt
→ report
→ comandi e test
→ evidenze
→ riconciliazione
→ verifica
→ collaudo
→ approvazione
→ chiusura
→ baseline successiva
```

La catena non deve contenere passaggi importanti lasciati soltanto nel testo libero.

Da qualunque elemento deve essere possibile:

1. risalire alle sue fonti;
2. identificare il motivo per cui esiste;
3. sapere quale decisione lo autorizza;
4. individuare i documenti che lo governano;
5. vedere le attività che lo hanno prodotto o modificato;
6. consultare le prove che lo verificano;
7. ricostruire gli eventi successivi;
8. conoscere lo stato corrente senza cancellare lo storico.

---

# 3. Principio di separazione dei livelli

Il sistema deve distinguere almeno:

```text
project
phase
work_item
task
task_execution
attempt
```

Questi livelli non sono sinonimi.

- `project` rappresenta l’intero sistema governato;
- `phase` rappresenta un grande momento o dominio del progetto;
- `work_item` rappresenta una voce della To-Do autorevole;
- `task` rappresenta un’unità esecutiva concreta;
- `task_execution` rappresenta l’affidamento concreto a un esecutore, modalità o sessione;
- `attempt` rappresenta un singolo tentativo numerato e consumabile.

Il completamento di un livello inferiore non completa automaticamente quello superiore.

---

# 4. Principio di granularità controllata

Le informazioni devono essere conservate in unità sufficientemente piccole da poter essere:

- selezionate;
- filtrate;
- versionate;
- collegate;
- validate;
- riutilizzate;
- escluse motivatamente;
- consegnate a un’IA senza rumore superfluo.

Non devono essere concentrate indiscriminatamente in un unico documento o in un unico payload JSON.

La granularità non deve però frammentare il significato. Ogni unità deve mantenere:

- identità;
- tipo;
- progetto;
- versione;
- stato;
- origine;
- relazioni;
- timestamp;
- autore o attore;
- hash quando applicabile.

---

# 5. Principio di identità doppia

Le entità persistenti usano:

```text
UUID tecnico
+
reference_code leggibile e stabile
```

L’UUID:

- è la chiave tecnica;
- è usato dalle foreign key;
- non dipende da un formato editoriale;
- è compatibile con una futura migrazione PostgreSQL.

Il `reference_code`:

- è usato in UI, documenti, prompt, report, evidenze ed export;
- è stabile;
- non è riciclato;
- è univoco nel progetto;
- non viene usato come foreign key tecnica.

Esempi:

```text
TASK-0001
ATTEMPT-0001
REPORT-0001
EVIDENCE-0001
DECISION-0001
DOCUMENT-0001
```

---

# 6. Principio di documentazione come dato di prima classe

Analisi, decisioni, documenti, requisiti, criteri di accettazione, definizioni dei test, esecuzioni dei test e collaudi sono entità persistenti.

Non devono esistere soltanto come testo disperso nei file.

Il sistema deve poter rispondere in modo deterministico a domande come:

- quale analisi ha originato questa decisione?
- quale decisione ha autorizzato questa task?
- quale versione documentale governava il tentativo?
- quali requisiti sono coperti da quali test?
- quale evidenza sostiene una verifica?
- quale collaudo era richiesto?
- chi ha approvato la chiusura?
- quali eccezioni erano valide in quel momento?

---

# 7. Principio di doppia conservazione documentale

I documenti testuali governati devono restare disponibili:

1. come file leggibili e versionabili nel repository;
2. come versioni immutabili registrate nel database.

Ogni versione documentale deve conservare almeno:

- identità del documento logico;
- identità della versione;
- numero o etichetta di versione;
- stato;
- contenuto testuale;
- hash;
- percorso della fonte, se presente;
- commit della fonte, se osservabile;
- provenienza;
- versione precedente sostituita;
- data;
- autore o attore;
- data di congelamento.

Una versione usata in una decisione, esecuzione, verifica o approvazione non può essere sovrascritta.

Una modifica produce una nuova versione.

---

# 8. Principio di fonte primaria e sintesi

Le sintesi servono a ridurre il carico cognitivo e il numero di token, ma non diventano automaticamente la fonte primaria.

Regola:

> La sintesi accelera la lettura; la fonte originale conserva la verità storica.

Ogni sintesi deve registrare:

- fonti;
- versioni delle fonti;
- hash;
- scopo;
- livello di dettaglio;
- copertura;
- elementi esclusi;
- data;
- stato di aggiornamento.

Quando una fonte cambia, la sintesi collegata deve poter diventare `STALE`.

---

# 9. Principio di provenienza

Ogni informazione importante deve dichiarare la propria provenienza.

Classificazione minima proposta:

```text
DECLARED
OBSERVED
DERIVED
INFERRED
APPROVED
IMPORTED
GENERATED
```

Questi valori non sono intercambiabili.

Esempio:

```text
“npm run verify è passato”
```

può essere:

- dichiarato da un esecutore;
- osservato da un command run;
- derivato dalla lettura dell’exit code;
- riconciliato con il report;
- approvato da una verifica.

Il sistema deve conservare ogni passaggio senza fonderli in un’unica dichiarazione.

---

# 10. Principio di collegamenti bidirezionali

Ogni relazione rilevante deve essere navigabile in entrambe le direzioni.

Esempi:

```text
requirement → test_definitions
test_definition → requirement

task → decisions
decision → affected_tasks

document_version → executions_that_used_it
task_execution → delivered_document_versions

bug → corrective_task
task → originating_bug
```

Il sistema deve poter rilevare:

- record orfani;
- relazioni interrotte;
- requisiti senza test;
- test senza requisito;
- verifiche senza evidenze;
- approvazioni senza verifiche richieste;
- task senza work item;
- tentativi senza prompt o snapshot;
- documenti senza versione autorevole.

---

# 11. Principio di contesto minimo sufficiente

Le IA e gli operatori non devono ricevere automaticamente l’intero progetto.

Devono ricevere un contesto:

- pertinente;
- minimo;
- sufficiente;
- versionato;
- riproducibile;
- verificabile;
- coerente con ruolo e scope.

La selezione del contesto deve partire da relazioni deterministiche.

La ricerca semantica o l’IA possono proporre elementi aggiuntivi, ma non possono eliminare fonti obbligatorie senza lasciare traccia.

---

# 12. Principio di apertura progressiva

Il contesto deve essere organizzato in livelli:

```text
CORE
SUPPORTING
DEEP_REFERENCE
```

- `CORE`: materiale da leggere immediatamente;
- `SUPPORTING`: materiale pertinente consultabile quando serve;
- `DEEP_REFERENCE`: fonti storiche o dettagliate raggiungibili senza appesantire il contesto iniziale.

Questo consente di attraversare il progetto dal macroscopico al microscopico senza mostrare tutti i livelli contemporaneamente.

---

# 13. Principio di immutabilità storica

Non devono essere riscritti retroattivamente:

- decisioni approvate;
- versioni documentali usate;
- prompt congelati;
- report originali;
- evidenze osservate;
- snapshot;
- eventi;
- risultati conclusi dei command run;
- approvazioni;
- eccezioni approvate;
- baseline approvate.

Una correzione crea:

- una nuova versione;
- un nuovo record;
- un nuovo evento;
- una relazione di sostituzione o rettifica.

Lo storico originario resta consultabile.

---

# 14. Principio di ricostruzione temporale

Il sistema deve poter rispondere:

- qual era lo stato del progetto a una data?
- quali decisioni erano vigenti?
- quale baseline era attiva?
- quale documento governava un tentativo?
- quale contesto era stato consegnato?
- quali bug o eccezioni erano aperti?
- quale commit era osservato?

La ricostruzione storica deve usare versioni, snapshot, eventi, hash e relazioni esplicite.

---

# 15. Principio di completezza prima delle transizioni

Una transizione non deve avvenire soltanto perché un attore la dichiara.

Esempi di controlli:

```text
task READY
→ obiettivo, scope, contratto e criteri presenti

attempt IN_PROGRESS
→ prompt congelato, Context Package e snapshot presenti

verification PASSED
→ scope completo, evidenze disponibili, controlli obbligatori eseguiti

task COMPLETED
→ verifiche, collaudi e approvazioni richiesti presenti
```

Elementi mancanti devono produrre:

- blocco;
- stato incompleto;
- eccezione umana esplicita;
- oppure nuova attività correttiva.

---

# 16. Principio di elementi irrisolti persistenti

Dubbi e problemi non devono scomparire al termine di una chat.

Il modello dovrà rappresentare almeno:

```text
open_questions
assumptions
risks
findings
conflicts
```

Ogni elemento deve conservare:

- identità;
- origine;
- stato;
- impatto;
- responsabile;
- decisione collegata;
- task di risoluzione;
- eventuale scadenza;
- esito.

---

# 17. Principio di sicurezza e minimizzazione

Conservare tutto non significa distribuire tutto.

I pacchetti destinati a IA o operatori devono poter escludere o redigere:

- segreti;
- token;
- credenziali;
- dati personali non necessari;
- percorsi locali non pertinenti;
- documenti fuori autorizzazione;
- payload sensibili.

Ogni esclusione deve essere registrata e motivata.

---

# 18. Principio di integrità e recupero

Il sistema deve proteggere dati e relazioni tramite:

- hash;
- manifest;
- backup;
- export;
- verifica degli allegati;
- verifica delle versioni;
- controllo delle relazioni;
- ripristino testato;
- segnalazione delle divergenze;
- registrazione delle operazioni di recupero.

Un export completo deve permettere di ricostruire:

```text
dati
documenti
allegati
relazioni
versioni
eventi
hash
manifest
```

---

# 19. Principio del Context Graph

Project Integrity OS deve essere trattato come un grafo di contesto governato.

Nodi esemplificativi:

```text
project
phase
work_item
task
attempt
document
decision
requirement
test
report
evidence
bug
approval
```

Relazioni esemplificative:

```text
DERIVES_FROM
IMPLEMENTS
VERIFIES
PRODUCED_BY
SUPERSEDES
BLOCKS
DEPENDS_ON
APPROVED_BY
DISCOVERED_DURING
CORRECTED_BY
INCLUDED_IN_BASELINE
```

Il database relazionale conserva identità e vincoli. Il grafo logico consente la navigazione del contesto.

---

# 20. Stato del documento

Questo documento registra principi approvati nella discussione preliminare, ma non è ancora una fonte autorevole del progetto.

Prima dell’inserimento nella repository dovrà essere:

1. riesaminato;
2. confrontato con i documenti correnti;
3. eventualmente corretto;
4. approvato;
5. versionato come documento corrente;
6. registrato nel Document Registry.
