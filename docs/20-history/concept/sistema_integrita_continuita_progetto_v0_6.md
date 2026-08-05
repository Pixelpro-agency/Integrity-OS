# Sistema di integrità e continuità del progetto

## Bozza concettuale v0.5 — decisioni pre-MVP consolidate

## 1. Visione

Il progetto non nasce come semplice generatore di prompt, gestore di documentazione, lista To-Do o orchestratore di agenti IA.

L’obiettivo è costruire un **sistema di integrità e continuità del progetto** capace di mantenere nel tempo:

- obiettivi e linee guida;
- decisioni approvate;
- stato reale delle attività;
- storico delle modifiche;
- verifiche ed evidenze;
- bug introdotti e corretti;
- dipendenze tra task, requisiti, file, test e documenti;
- prossime azioni consentite.

Il principio centrale è:

> Nessuna task è completata perché un’IA lo dichiara. È completata soltanto quando il risultato, le evidenze e lo stato complessivo del progetto concordano.

L’orchestrazione degli agenti IA sarà una capacità futura e subordinata. Il software dovrà rimanere indipendente dall’orchestratore utilizzato.

---

## 2. Problema reale da risolvere

Un progetto può già disporre di buona documentazione, una lista To-Do e prompt esecutivi ben costruiti, ma continuare a produrre errori di coordinamento e completezza.

Esempi concreti:

- un agente dichiara che la task è conclusa, ma il collaudo manuale trova problemi;
- il report finale non contiene l’elenco dei file modificati;
- il commit esiste ma il push richiesto non è stato eseguito;
- l’agente dichiara di aver eliminato tutti i riferimenti a una tecnologia o a un file, ma un’occorrenza è ancora presente altrove;
- i test passano, ma il requisito funzionale non è realmente soddisfatto;
- una singola task è corretta nel proprio perimetro, ma crea una contraddizione con una decisione generale del progetto;
- il verificatore controlla soltanto i file modificati dall’esecutore e non individua errori presenti fuori da quello scope;
- un bug viene corretto, ma non viene aggiunta una protezione che ne impedisca il ritorno;
- la documentazione dichiara uno stato diverso da quello reale del repository.

Questi problemi non sono soltanto errori di codice. Sono errori di:

- completezza;
- coerenza;
- tracciabilità;
- validazione;
- comprensione semantica;
- governance del progetto.

---

## 3. Verità locale e verità del progetto

Un agente esecutore opera normalmente su un contesto ristretto:

- task corrente;
- file autorizzati;
- vincoli pertinenti;
- test richiesti;
- formato del report.

Da questo punto di vista può lavorare correttamente e, allo stesso tempo, lasciare il progetto in uno stato incompleto o incoerente.

Il sistema deve quindi distinguere tra:

### Esecuzione conforme allo scope locale

L’agente ha rispettato le istruzioni ricevute e non ha modificato ciò che non era autorizzato a modificare.

### Risultato conforme all’obiettivo generale

Il progetto complessivo soddisfa davvero il requisito, non contiene residui, non viola decisioni esistenti e dispone delle evidenze necessarie.

Queste due condizioni non sono equivalenti.

---

## 4. Regola dello scope

Una regola fondamentale è:

> Lo scope di modifica non deve coincidere con lo scope di verifica.

### Write scope

Deve essere ristretto e controllato. Definisce i file e le aree che l’esecutore può modificare.

### Read and verify scope

Deve essere più ampio. Può includere:

- intero repository;
- documentazione;
- test;
- configurazioni;
- stato Git;
- log;
- artefatti prodotti;
- cronologia delle decisioni;
- task collegate;
- bug storici.

Se un agente trova un problema fuori dal proprio write scope, non deve modificarlo automaticamente, ma deve segnalarlo. La task non può essere considerata completa finché la discrepanza non viene risolta, accettata o trasformata in una nuova task.

---

## 5. I livelli di verifica

Il sistema deve separare più livelli di controllo.

### 5.1 Autoverifica dell’esecutore

L’agente che svolge la task controlla il proprio lavoro:

- sintassi;
- test pertinenti;
- ricerche richieste;
- file modificati;
- rispetto dello scope;
- completezza del report.

Questa verifica è utile, ma non indipendente.

### 5.2 Verifica tecnica indipendente

Un secondo agente o un componente deterministico confronta:

- richiesta originale;
- contratto della task;
- diff reale;
- report dell’esecutore;
- stato del repository;
- test realmente eseguiti;
- commit e push;
- artefatti richiesti.

Esempi di discrepanze:

- il report dichiara tre file modificati, ma Git ne mostra quattro;
- il report dichiara test superati, ma non esiste evidenza della loro esecuzione;
- il push era obbligatorio, ma il commit è soltanto locale;
- il report obbligatorio manca o è incompleto;
- esistono modifiche fuori scope.

### 5.3 Verifica macroscopica o semantica

Il sistema controlla la coerenza con l’intero progetto:

- linee guida;
- decisioni precedenti;
- requisiti;
- documentazione;
- dipendenze;
- comportamenti invarianti;
- bug storici;
- milestone;
- obiettivo generale;
- aree non comprese nella task esecutiva.

Questa fase costituisce la **verifica della verifica**.

### 5.4 Collaudo funzionale

Il comportamento reale viene confrontato con ciò che l’utente aveva richiesto. Può essere:

- manuale;
- automatizzato;
- assistito da un agente;
- misto.

### 5.5 Approvazione umana

L’essere umano mantiene l’autorità finale nei passaggi che richiedono giudizio, modifica dello scope, accettazione di eccezioni o cambiamento delle linee guida.

---

## 6. La task come contratto strutturato

Una task non dovrebbe esistere soltanto come testo libero. Internamente deve diventare un contratto verificabile.

Campi possibili:

- ID;
- titolo;
- obiettivo;
- motivazione;
- requisito di origine;
- decisioni collegate;
- prerequisiti;
- dipendenze;
- file modificabili;
- file in sola lettura;
- aree escluse;
- ricerche globali obbligatorie;
- comportamenti da non modificare;
- output obbligatori;
- test obbligatori;
- collaudo richiesto;
- numero massimo di tentativi;
- commit richiesto;
- push richiesto;
- criteri di accettazione;
- condizioni di blocco;
- formato del report finale.

Esempio concettuale:

```yaml
id: TASK-027
obiettivo: Rimuovere tutti i riferimenti obsoleti alla documentazione MDX

prerequisiti:
  - TASK-025 verificata
  - TASK-026 completata

file_modificabili:
  - docs/current/**
  - frontend/src/**

file_sola_lettura:
  - backend/**
  - docs/archive/**
  - tests/**

ricerche_globali_obbligatorie:
  - "*.mdx"
  - "nomeVecchiaFunzione"
  - "/old-endpoint"

output_obbligatori:
  - report finale
  - elenco file modificati
  - risultati test
  - commit
  - push

tentativi_massimi: 3

criteri_di_accettazione:
  - nessun riferimento residuo nel dominio definito
  - nessuna modifica fuori scope
  - tutti i test richiesti eseguiti
  - working tree coerente con la procedura
  - commit presente sul branch remoto
```

L’interfaccia non deve necessariamente mostrare YAML. Può tradurre questi dati in moduli, pannelli e checklist.

---

## 7. Il report come dichiarazione, non come prova

Il report prodotto da un agente deve essere trattato come una dichiarazione da verificare.

Il sistema confronta automaticamente:

| Dichiarazione dell’agente | Evidenza reale |
|---|---|
| File modificati | Git diff / working tree |
| Test eseguiti | log o esecuzioni registrate |
| Commit creato | stato Git |
| Push completato | stato del branch remoto |
| Nessun riferimento residuo | ricerca reale nel dominio stabilito |
| Nessuna modifica fuori scope | diff confrontato con il contratto |
| Documentazione aggiornata | controllo dei documenti collegati |

Una task può essere dichiarata riuscita dall’agente ma fallire la verifica tecnica.

---

## 8. Test, verifica e collaudo non sono la stessa cosa

Il sistema deve distinguere:

1. **Controllo tecnico** — il codice è valido?
2. **Test automatici** — i test previsti passano?
3. **Verifica della task** — la modifica richiesta è realmente presente?
4. **Verifica di regressione** — qualcosa di già funzionante è stato danneggiato?
5. **Collaudo funzionale** — il comportamento osservabile soddisfa la richiesta?
6. **Collaudo macroscopico** — il risultato è coerente con architettura, documentazione e decisioni?
7. **Accettazione umana** — il risultato può diventare parte della nuova baseline?

Una task può essere implementata senza essere verificata, verificata tecnicamente senza essere collaudata, o collaudata senza essere ancora accettata.

---

## 9. Macchina a stati della task

Una task non passa direttamente da “in corso” a “completata”.

Possibile flusso:

```text
BOZZA
  ↓
ANALIZZATA
  ↓
PRONTA PER L’ESECUZIONE
  ↓
IN ESECUZIONE
  ↓
REPORT RICEVUTO
  ↓
EVIDENZE COMPLETE / EVIDENZE INCOMPLETE
  ↓
VERIFICA TECNICA
  ↓
VERIFICA MACROSCOPICA
  ↓
COLLAUDO
  ↓
APPROVAZIONE UMANA
  ↓
COMPLETATA
```

Stati alternativi:

- BLOCCATA;
- FALLITA;
- PARZIALMENTE COMPLETATA;
- FUORI SCOPE;
- RICHIEDE NUOVA DECISIONE;
- RIAPERTA;
- REGRESSIONE RILEVATA;
- EVIDENZA INSUFFICIENTE;
- REPORT NON CONFORME.

Una task completata può essere riaperta quando una verifica successiva scopre una discrepanza.

---

## 10. Linee guida applicabili

Le linee guida non devono rimanere soltanto testo da ricordare. Devono poter diventare regole operative.

Esempi:

### Limite dei tentativi

Ogni prompt esecutivo può effettuare al massimo tre tentativi ragionati. Dopo il terzo fallimento, il sistema blocca ulteriori esecuzioni e richiede un report diagnostico.

### Commit e push

Se esistono file modificati e la procedura richiede commit e push, la task non può avanzare se uno dei due manca.

### Snapshot condizionati

Gli snapshot sono richiesti soltanto quando esistono file modificati.

### Divieto di modifica

Alcuni flussi o componenti possono essere definiti invarianti per una task. Una modifica rilevata in quelle aree blocca la verifica.

### Obbligo di ricerca globale

Una task che dichiara la rimozione completa di un riferimento richiede una ricerca sull’intero dominio definito, non soltanto nei file modificabili.

Le linee guida possono quindi appartenere a categorie diverse:

- sempre valide;
- valide per un progetto;
- valide per una milestone;
- valide per una classe di task;
- valide soltanto per una task specifica.

---

## 11. Memoria semantica dei bug

I bug non devono essere soltanto voci nella To-Do. Devono diventare parte della conoscenza del progetto.

Per ogni bug il sistema può conservare:

- sintomo;
- data di scoperta;
- task in cui è stato rilevato;
- possibile task o commit di origine;
- requisito violato;
- file e moduli coinvolti;
- causa accertata o ipotizzata;
- perché i controlli precedenti non lo hanno rilevato;
- soluzione adottata;
- test di regressione aggiunto;
- decisioni collegate;
- rischio di ricomparsa;
- task future che devono ricevere questo contesto.

Il sistema non conserva soltanto ciò che è stato fatto, ma anche:

> quali errori sono stati commessi, perché non sono stati trovati e quale protezione è stata introdotta.

---

## 12. Modello semantico del progetto

Il software deve rappresentare le entità e le relazioni del progetto.

### Entità principali

- obiettivo;
- requisito;
- linea guida;
- decisione;
- vincolo;
- comportamento invariante;
- milestone;
- task;
- file;
- modulo;
- documento;
- esecuzione;
- evidenza;
- verifica;
- collaudo;
- bug;
- test;
- commit;
- approvazione.

### Relazioni principali

- deriva da;
- deve rispettare;
- dipende da;
- modifica;
- verifica;
- contraddice;
- ha causato;
- ha corretto;
- ha introdotto una regressione;
- rende obsoleto;
- sostituisce;
- è coperto da;
- è approvato da;
- blocca;
- riapre.

Esempio:

```text
REQ-014
“Mostrare matched volume senza causalità”
        │
        ├── vincolato da DEC-008
        ├── implementato da TASK-2C, TASK-2D, TASK-2E
        ├── modifica MoneyFlowChart
        ├── verificato dai test X e Y
        └── collegato a BUG-021
```

Questo grafo permette di valutare l’impatto di una modifica e di generare il contesto pertinente per le attività future.

---

## 13. Baseline corrente e storico immutabile

Il sistema deve separare ciò che oggi è considerato vero da ciò che è accaduto nel tempo.

### Baseline corrente

Contiene:

- obiettivi vigenti;
- architettura vigente;
- linee guida valide;
- decisioni attive;
- task completate e verificate;
- bug aperti;
- milestone correnti;
- prossimo lavoro consentito;
- riferimento allo stato reale del repository.

### Storico immutabile

Conserva:

- decisioni;
- esecuzioni;
- tentativi;
- verifiche;
- fallimenti;
- bug;
- riaperture;
- cambiamenti di scope;
- approvazioni;
- cambi di baseline.

La baseline può evolvere. Lo storico non deve essere riscritto.

---

## 14. Pacchetto di contesto per ogni esecuzione

La continuità del progetto non deve dipendere dalla memoria di una conversazione.

Ogni nuova esecuzione può partire come se l’agente non avesse mai visto il progetto. Il sistema genera un pacchetto contenente:

- identità del progetto;
- versione della baseline;
- commit di riferimento;
- obiettivo della task;
- motivazione;
- requisiti collegati;
- linee guida applicabili;
- decisioni pertinenti;
- bug storici collegati;
- dipendenze;
- file modificabili;
- area da ispezionare;
- comportamenti invarianti;
- test obbligatori;
- collaudo richiesto;
- output obbligatori;
- formato del report;
- numero massimo di tentativi;
- condizioni di completamento.

Conclusa l’esecuzione, la conversazione può essere eliminata senza perdere la verità del progetto.

---

## 15. Ruolo futuro degli orchestratori di agenti

Il sistema deve essere indipendente dagli orchestratori.

Un orchestratore futuro potrà occuparsi di:

- scegliere il modello;
- assegnare ruoli;
- parallelizzare analisi, implementazione e revisione;
- eseguire strumenti e test;
- coordinare agenti;
- raccogliere risultati.

Il sistema di integrità decide invece:

- quale lavoro è consentito;
- perché deve essere svolto;
- quali linee guida si applicano;
- quale scope è autorizzato;
- quali prove sono obbligatorie;
- se il risultato è accettabile;
- come cambia lo stato complessivo del progetto.

```text
SISTEMA DI INTEGRITÀ DEL PROGETTO
            │
            ├── prepara la task
            ├── applica linee guida
            ├── stabilisce scope e criteri
            ├── verifica evidenze e coerenza
            └── determina lo stato finale
                     │
                     ▼
        ORCHESTRATORE DI AGENTI
                     │
                     ▼
       AGENTI ESECUTORI E REVISORI
```

---

## 16. Definizione sintetica

Il progetto può essere definito come:

> Un sistema che mantiene un modello semantico e verificabile di un progetto, prepara incarichi circoscritti per persone o agenti IA, confronta le loro dichiarazioni con le evidenze reali e controlla che ogni modifica sia coerente con lo stato complessivo, lo storico, le decisioni e i bug del progetto.

Il suo valore principale non è far lavorare più agenti, ma individuare casi in cui:

- l’agente ha lavorato correttamente ma la task non è completa;
- il report non coincide con il repository;
- i test passano ma il requisito non è soddisfatto;
- il verificatore ha controllato un perimetro insufficiente;
- una modifica locale viola una decisione generale;
- manca un passaggio obbligatorio della procedura;
- un bug è stato corretto senza protezione futura;
- una task completata deve essere riaperta.

---

## 17. Decisioni preliminari approvate

Le seguenti decisioni costituiscono la prima impostazione ufficiale del progetto. Non sono ancora specifiche tecniche definitive, ma orientano il modello concettuale e le scelte successive.

### 17.1 Prima versione specializzata nei progetti software

La prima versione sarà progettata specificamente per progetti software.

Dovrà quindi comprendere nativamente concetti come:

- repository;
- file e directory;
- branch;
- commit;
- push;
- pull request;
- diff;
- test;
- build;
- documentazione tecnica;
- frontend, backend, servizi e moduli;
- bug e regressioni;
- collaudo funzionale.

Il modello dovrà comunque evitare dipendenze inutili da un singolo linguaggio, framework, provider Git o orchestratore di agenti. La struttura interna potrà essere estesa in futuro ad altri tipi di progetto, ma la prima versione non cercherà di risolvere contemporaneamente domini troppo diversi.

**Motivazione:** il problema reale da cui nasce il prodotto è già osservabile e verificabile nei progetti software. Tentare fin dall’inizio una generalizzazione universale renderebbe meno precisi task, prove, procedure e controlli.

---

### 17.2 Gerarchia delle fonti di verità

Il sistema adotterà una gerarchia esplicita delle fonti:

```text
1. Evidenze reali del repository, dei test, della CI e degli artefatti
2. Decisioni e approvazioni registrate
3. Baseline corrente del progetto
4. Documentazione e lista To-Do
5. Report e dichiarazioni di persone o agenti
```

Questa gerarchia non significa che il repository descriva da solo l’intero progetto. La documentazione può contenere intenzioni, requisiti o decisioni future non ancora implementate. Il sistema deve quindi distinguere almeno tra:

- **stato deciso**;
- **stato pianificato**;
- **stato dichiarato**;
- **stato implementato**;
- **stato verificato**;
- **stato accettato**.

Quando una fonte inferiore contraddice una fonte superiore, il sistema deve segnalare la discrepanza e impedire che venga assunta come verità senza una decisione esplicita.

**Motivazione:** il report dell’agente e la To-Do sono utili, ma non possono prevalere su un diff reale, un test fallito o l’assenza del push richiesto. Allo stesso tempo, il codice non può sostituire requisiti e decisioni che definiscono ciò che il progetto deve diventare.

---

### 17.3 Blocco automatico con deroga umana registrata

Quando mancano prove obbligatorie o esistono discrepanze rilevanti, il sistema deve bloccare:

- la chiusura della task;
- il passaggio allo stato completato;
- l’avvio delle attività dipendenti, quando il problema compromette i loro prerequisiti.

Il blocco può essere superato soltanto mediante una deroga umana esplicita che registri:

- chi ha autorizzato l’eccezione;
- quando;
- per quale motivo;
- quale rischio viene accettato;
- quali parti restano non verificate;
- se è necessaria una task successiva;
- fino a quando la deroga rimane valida.

La deroga non deve cancellare l’errore o far apparire la task pienamente verificata. Deve produrre uno stato distinto, per esempio:

```text
ACCETTATA CON ECCEZIONE
```

**Motivazione:** un sistema che segnala soltanto gli errori può essere facilmente ignorato; un sistema che blocca senza eccezioni può invece diventare inutilizzabile nei casi reali. Il blocco con deroga tracciata mantiene controllo e flessibilità.

---

### 17.4 Problema trovato fuori dallo scope modificabile

Quando l’esecutore rispetta il proprio write scope ma la verifica globale trova un problema fuori da esso, il sistema deve separare due giudizi:

```text
Esecuzione locale: riuscita
Obiettivo complessivo: non soddisfatto
```

La task non deve diventare automaticamente completata. Deve richiedere una decisione umana tra almeno queste possibilità:

1. estendere formalmente lo scope della task corrente;
2. creare una sotto-task o una task correttiva collegata;
3. accettare esplicitamente il residuo come eccezione;
4. modificare il requisito o il criterio di accettazione, se il problema dimostra che erano formulati in modo errato.

La gravità del residuo può influenzare il tipo di blocco, ma non può trasformare automaticamente un obiettivo non soddisfatto in un successo completo.

**Motivazione:** l’esecutore non deve essere punito per non aver modificato file vietati, ma il progetto non deve nemmeno considerare conclusa una richiesta globale rimasta incompleta.

---

### 17.5 Requisiti di chiusura configurabili per classe di task

Non tutte le task richiedono gli stessi artefatti. Il sistema deve applicare procedure e checklist differenti in base alla classe di lavoro.

Esempi iniziali:

#### Task di sola analisi

Può richiedere:

- file e fonti esaminati;
- conclusioni motivate;
- limiti e parti non verificate;
- nessuna modifica al repository;
- nessun commit o push.

#### Task con modifiche al codice

Può richiedere:

- file verificati;
- file modificati;
- diff coerente con lo scope;
- comandi eseguiti;
- test obbligatori;
- esito completo dei test;
- commit;
- push, quando previsto;
- report finale conforme.

#### Task documentale

Può richiedere:

- ricerca globale dei riferimenti;
- controllo dei collegamenti;
- verifica dei documenti correnti e storici;
- diff;
- eventuale commit e push.

#### Bug fix

Può richiedere:

- descrizione o riproduzione del bug;
- identificazione della causa;
- correzione;
- test di regressione;
- verifica che il comportamento precedente valido non sia stato compromesso;
- aggiornamento della memoria semantica del bug.

Le regole potranno essere ereditate da più livelli:

```text
regole globali
    ↓
regole del progetto
    ↓
regole della milestone
    ↓
regole della classe di task
    ↓
eccezioni della singola task
```

**Motivazione:** rendere commit, push, snapshot o test obbligatori per qualunque attività produrrebbe falsi errori. Le procedure devono essere rigorose, ma coerenti con il tipo di lavoro.

---

### 17.6 Verifica indipendente ibrida

La verifica della verifica non richiederà automaticamente tre agenti IA per ogni attività.

Il modello preferito è:

```text
controlli deterministici obbligatori
+
revisione IA indipendente quando serve giudizio semantico
+
approvazione umana nei passaggi critici
```

I controlli deterministici devono essere preferiti quando il fatto è oggettivamente verificabile. Per esempio:

- file realmente modificati;
- stato del working tree;
- presenza del commit;
- corrispondenza con il branch remoto;
- esecuzione dei comandi registrati;
- risultati dei test;
- presenza di riferimenti testuali residui;
- produzione degli artefatti obbligatori;
- modifiche fuori scope.

Un revisore IA indipendente è utile per domande come:

- la modifica soddisfa semanticamente il requisito?
- esiste un conflitto con una decisione precedente?
- la verifica ha analizzato un dominio sufficiente?
- un report omette un rischio importante?
- la soluzione introduce una deviazione architetturale?

L’approvazione umana resta necessaria per:

- deroghe;
- cambi di scope;
- modifiche a requisiti o linee guida;
- accettazione di rischi;
- nuova baseline;
- risultati il cui collaudo dipende da giudizi funzionali o commerciali.

**Motivazione:** usare IA per verificare fatti già controllabili dal software aumenterebbe costi e possibilità di errore. La componente semantica richiede invece capacità interpretativa e, nei passaggi decisivi, responsabilità umana.

---

### 17.7 Bug scoperto dopo la chiusura di una task

Quando un bug viene scoperto dopo che una task era stata completata e approvata, il sistema non deve riscrivere il passato.

La task originale deve conservare il proprio stato storico:

```text
completata e accettata secondo le evidenze disponibili in quel momento
```

Successivamente il sistema aggiunge:

- il bug scoperto;
- la data e il contesto della scoperta;
- il collegamento alla task o al commit potenzialmente responsabile;
- il motivo per cui le verifiche precedenti non lo avevano rilevato;
- la task correttiva;
- il test o la protezione introdotta per evitarne il ritorno.

La vista corrente del progetto deve però segnalare che quella parte non è più considerata pienamente sana fino alla correzione. Si distinguono così:

- **verità storica:** la task era stata approvata;
- **verità corrente:** è stato successivamente rilevato un difetto collegato;
- **azione necessaria:** correggere, verificare e aggiornare la baseline.

Le metriche storiche non vengono falsificate. Le metriche correnti della milestone possono invece diminuire o assumere uno stato di rischio finché il bug resta aperto.

**Motivazione:** riaprire e sovrascrivere semplicemente la task cancellerebbe informazioni importanti sul processo che non ha individuato il problema. Lasciarla invariata senza impatto sullo stato corrente nasconderebbe invece un difetto reale.

---

## 18. Conseguenze di queste decisioni sul prodotto

Le decisioni precedenti determinano alcuni principi architetturali che dovranno essere rispettati nelle fasi successive.

### 18.1 Il sistema deve rappresentare più stati contemporaneamente

Non può esistere un solo campo generico `status: done`. Devono essere separati almeno:

- stato dell’esecuzione;
- stato delle evidenze;
- stato della verifica tecnica;
- stato della verifica macroscopica;
- stato del collaudo;
- stato dell’accettazione;
- stato corrente di salute dopo eventuali bug successivi.

### 18.2 Le dichiarazioni non possono aggiornare direttamente la baseline

Un report ricevuto non può trasformarsi automaticamente in verità di progetto. Deve attraversare i controlli previsti dalla classe di task.

### 18.3 La ricerca globale deve poter superare lo scope di scrittura

Il sistema deve poter ispezionare aree più ampie di quelle modificabili, mantenendo separati i permessi di lettura, modifica e approvazione.

### 18.4 Le eccezioni devono essere entità di prima classe

Una deroga non deve essere una nota nascosta. Deve avere responsabile, motivazione, durata, rischio, impatto e collegamenti alle task interessate.

### 18.5 Lo storico deve essere append-only

Correzioni, riaperture e cambiamenti di stato devono aggiungere eventi, non riscrivere gli eventi precedenti.

### 18.6 Le procedure devono essere configurabili ma verificabili

Il progetto può definire classi di task e relative checklist. Tuttavia, una volta applicata una procedura a una task, i suoi requisiti diventano parte del contratto e non possono essere ignorati senza una deroga.

---

## 19. Questioni tecniche da definire nella fase successiva

Dopo queste decisioni concettuali, l’allineamento può passare a domande più tecniche, tra cui:

- come acquisire lo stato reale del repository senza affidarsi al report dell’agente;
- quale struttura usare per baseline, eventi, task, bug, evidenze e verifiche;
- quali dati conservare nel repository e quali nel database governato dal software;
- come riconoscere che un test è stato realmente eseguito;
- come verificare commit, push e branch remoto;
- come rappresentare gli scope di lettura, scrittura e verifica;
- come generare e validare il report strutturato dell’esecutore;
- come distinguere automaticamente task di analisi, codice, documentazione e bug fix;
- come stabilire il dominio di una ricerca globale;
- come eseguire la verifica macroscopica senza fornire inutilmente l’intero progetto a un modello;
- come aggiornare la baseline dopo l’approvazione;
- come collegare una task a decisioni, requisiti, bug e file senza creare manutenzione manuale eccessiva;
- come integrare in futuro uno o più orchestratori di agenti mantenendoli sostituibili.

Queste questioni saranno affrontate una alla volta, partendo dai casi reali già osservati nel workflow del progetto Tennis Decision UI.

---

## 20. Decisione sul modello ibrido e sul confine proprietario

Il sistema adotterà un modello ibrido, ma la divisione non sarà semplicemente:

```text
repository = dati importanti
database = dati secondari o voluminosi
```

Questa separazione sarebbe insufficiente, perché una parte essenziale del valore del prodotto risiederà proprio nei dati operativi, semantici e verificati conservati nel database.

La divisione approvata è invece:

```text
REPOSITORY
Verità tecnica e progettuale necessaria per comprendere e mantenere il prodotto

DATABASE GOVERNATO DAL SOFTWARE
Metodo operativo, stato profondo, storico, verifiche, relazioni ed evidenze
```

Il repository deve permettere di capire che cosa è stato costruito e come funziona il progetto. Il database deve permettere di governare il processo con la profondità, la continuità e la capacità di verifica che costituiscono il valore distintivo del software.

---

## 21. Cosa rimane nel repository del progetto

Nel repository devono essere conservate le informazioni specifiche del progetto che servono a sviluppatori, manutentori e agenti autorizzati per comprendere il sistema e continuare a lavorarvi correttamente.

### 21.1 Costituzione e obiettivi del progetto

Una descrizione leggibile di:

- finalità del progetto;
- risultato atteso;
- perimetro funzionale;
- elementi esplicitamente esclusi;
- destinatari;
- vincoli tecnici o di dominio;
- criteri generali di successo del prodotto.

Questi contenuti appartengono al progetto, non al metodo proprietario del software di governance.

### 21.2 Architettura e baseline tecnica corrente

Nel repository devono restare le informazioni necessarie per comprendere lo stato tecnico attuale:

- componenti principali;
- flussi dati;
- dipendenze rilevanti;
- endpoint;
- strutture di persistenza;
- comportamenti attualmente implementati;
- commit o versione di riferimento della baseline pubblicata.

La baseline nel repository è una fotografia leggibile dello stato approvato, non il registro operativo completo che ha portato a quello stato.

### 21.3 Requisiti e comportamenti del prodotto

Devono restare nel progetto:

- requisiti funzionali vigenti;
- criteri di comportamento osservabile;
- invarianti tecnici del prodotto;
- vincoli derivanti dal dominio;
- limitazioni note che influenzano l’implementazione.

Esempio:

> Il matched volume è rappresentato come valore non direzionale e non deve essere interpretato come prova di causalità.

Questa è una decisione specifica del progetto e deve poter essere compresa da chi modifica il codice.

### 21.4 Decisioni tecniche e architetturali specifiche

Nel repository possono essere pubblicate le decisioni necessarie a spiegare:

- perché esiste una determinata architettura;
- quali alternative sono state rifiutate;
- quali vincoli devono essere rispettati;
- quali comportamenti non devono essere reintrodotti.

Queste decisioni descrivono il progetto. Non devono però contenere l’intero metodo con cui il software ha analizzato, verificato o approvato tali decisioni.

### 21.5 Documentazione necessaria alla manutenzione

Restano nel repository:

- istruzioni di installazione e avvio;
- configurazione tecnica;
- descrizione dei moduli;
- contratti API;
- procedure operative proprie del prodotto sviluppato;
- documentazione indispensabile per testare o mantenere il codice.

### 21.6 Manifest minimo di collegamento

Il repository può contenere un manifest essenziale, generato dal software, che colleghi la baseline pubblicata al progetto governato:

```yaml
project_id: TDUI
published_baseline_id: BASELINE-0042
published_baseline_revision: 42
repository_commit: abc123
published_at: 2026-08-04T19:00:00+02:00
```

Il manifest non espone il metodo. Serve a rilevare disallineamenti tra repository e stato governato.

---

## 22. Cosa non deve essere lasciato nel repository

Il metodo di lavoro costituisce una parte proprietaria del prodotto e non deve essere pubblicato come insieme stabile di file replicabili nel progetto del cliente.

Non devono essere conservati nel repository, salvo esportazioni esplicitamente richieste e controllate:

- linee guida generali del metodo;
- regola dei tentativi massimi;
- regole di avanzamento tra gli stati;
- procedure di commit e push;
- formati proprietari dei report;
- checklist di verifica;
- procedure di verifica della verifica;
- logica di classificazione delle task;
- regole per scegliere lo scope di lettura e scrittura;
- criteri di escalation;
- template dei prompt;
- template dei contratti esecutivi;
- regole di orchestrazione degli agenti;
- procedure di gestione delle deroghe;
- algoritmi di analisi delle discrepanze;
- struttura completa del grafo semantico;
- logica che decide quando una task può essere chiusa o riaperta.

Questi elementi appartengono al motore di governance e devono vivere nel software e nel suo database operativo.

---

## 23. Correzione della sezione “Linee guida applicabili”

Le linee guida descritte nella sezione 10 restano valide come concetto, ma non devono essere interpretate come file da inserire nel repository.

Esempi come:

- massimo tre tentativi per esecuzione;
- nessun avanzamento se manca il push richiesto;
- formato minimo del report;
- obbligo di una ricerca globale;
- regole per test, verifica e collaudo;
- classificazione dei file come modificabili o in sola lettura;

sono regole del metodo proprietario.

Devono essere:

1. definite e versionate nel database governato dal software;
2. associate alle classi di task o ai progetti tramite il motore di regole;
3. applicate automaticamente dal sistema;
4. incluse soltanto nella misura necessaria nel pacchetto esecutivo della singola task;
5. escluse dai commit del progetto, salvo contenuti che descrivano un vincolo tecnico specifico del prodotto.

La distinzione fondamentale è:

```text
“Non attribuire causalità al matched volume”
= decisione specifica del progetto, pubblicabile nel repository

“Dopo tre tentativi falliti bloccare l’esecuzione e richiedere un report”
= metodo proprietario del software, conservato nel database
```

---

## 24. Cosa vive nel database governato dal software

Il database non sarà soltanto un deposito di dati secondari. Conterrà il nucleo operativo e semantico del sistema.

### 24.1 Metodo e regole operative

Nel database vivono:

- classi di task;
- procedure applicabili;
- regole di avanzamento;
- condizioni di blocco;
- numero massimo di tentativi;
- requisiti di commit e push;
- report obbligatori;
- criteri di collaudo;
- regole per deroghe ed escalation;
- ruoli autorizzati ad approvare ogni passaggio.

### 24.2 Stato operativo delle task

Per ogni task il sistema conserva separatamente:

- stato di preparazione;
- stato dell’esecuzione;
- stato delle evidenze;
- stato della verifica tecnica;
- stato della verifica macroscopica;
- stato del collaudo;
- stato dell’accettazione;
- salute corrente dopo eventuali bug successivi;
- numero di tentativi utilizzati;
- blocchi ed eccezioni.

### 24.3 Storico immutabile

Il database registra in forma append-only:

- creazione e modifica delle task;
- cambiamenti di scope;
- tentativi;
- fallimenti;
- report ricevuti;
- verifiche;
- approvazioni;
- deroghe;
- riaperture;
- bug scoperti;
- nuove baseline pubblicate.

Il passato non viene riscritto. Gli eventi successivi correggono o qualificano gli eventi precedenti.

### 24.4 Grafo semantico del progetto

Il software conserva le relazioni tra:

- obiettivi;
- requisiti;
- decisioni;
- task;
- file e moduli;
- test;
- commit;
- bug;
- evidenze;
- verifiche;
- approvazioni.

Questo grafo consente di individuare conflitti, impatti, dipendenze, coperture mancanti e possibili regressioni.

### 24.5 Evidenze osservate dal sistema

Il database, o uno storage controllato collegato, conserva:

- diff reali;
- file modificati rilevati;
- hash;
- commit;
- branch;
- stato del remoto;
- risultati dei test;
- log dei comandi;
- esiti CI;
- ricerche globali;
- riferimenti residui;
- stato del working tree;
- artefatti richiesti.

Il report dell’agente resta una dichiarazione separata dalle evidenze osservate.

### 24.6 Confronto tra dichiarazioni e fatti

Il sistema registra le discrepanze tra:

- file dichiarati e file realmente modificati;
- test dichiarati e test realmente osservati;
- push dichiarato e stato del branch remoto;
- assenza dichiarata di riferimenti e risultati della scansione globale;
- scope autorizzato e diff effettivo;
- obiettivo dichiarato completato e criteri di accettazione ancora non soddisfatti.

### 24.7 Verifica della verifica

Il database conserva:

- cosa avrebbe dovuto controllare il revisore;
- quale dominio ha realmente ispezionato;
- quali prove ha utilizzato;
- quali controlli sono stati omessi;
- versione delle regole applicate;
- risultato della revisione indipendente;
- eventuale seconda revisione;
- decisione umana finale.

### 24.8 Memoria completa dei bug

Per ogni bug vengono conservati:

- sintomo;
- ambiente;
- momento della scoperta;
- task durante cui è emerso;
- possibile origine;
- requisito violato;
- causa accertata o ipotizzata;
- motivo per cui i controlli precedenti non lo hanno individuato;
- correzione;
- test di regressione;
- rischio residuo;
- task future interessate.

### 24.9 Pacchetti di contesto ed esecuzioni

Il database conserva:

- baseline utilizzata;
- commit iniziale;
- regole selezionate;
- decisioni pertinenti;
- bug storici inclusi;
- scope di lettura e scrittura;
- prompt o incarico compilato;
- modello o orchestratore utilizzato;
- risposta ricevuta;
- risultato della verifica.

Questo permette di ricostruire cosa sapeva l’agente quando ha operato.

### 24.10 Dati tecnici e voluminosi

Restano fuori dal repository:

- log estesi;
- cache;
- embedding;
- indici semantici;
- scansioni del repository;
- mappe derivate;
- risultati intermedi;
- telemetria;
- stato dell’interfaccia;
- dati temporanei delle esecuzioni.

---

## 25. Pacchetto esecutivo compilato e non versionato

Gli agenti devono ricevere le istruzioni necessarie per lavorare, ma questo non richiede di pubblicare il metodo completo nel repository.

Il software genera per ogni esecuzione un pacchetto temporaneo contenente soltanto ciò che serve per quella task:

- obiettivo;
- contesto tecnico pertinente;
- file modificabili;
- aree da ispezionare;
- vincoli specifici;
- output richiesti;
- test da eseguire;
- condizioni di arresto;
- formato minimo della risposta.

Il pacchetto può essere:

- inviato direttamente all’orchestratore;
- mostrato nell’interfaccia per il copia e incolla;
- salvato nel database come evidenza dell’esecuzione;
- scritto temporaneamente sul filesystem;

ma non deve essere inserito automaticamente nel repository o nei commit del cliente.

Il sistema espone quindi il **contratto compilato della singola task**, non l’intera metodologia che lo ha generato.

---

## 26. Limite reale della protezione del metodo

Nascondere le linee guida nel database riduce la replicabilità diretta, ma non rende il metodo impossibile da dedurre.

Un utente che vede molti pacchetti esecutivi potrebbe riconoscere alcune regole ricorrenti. Un cliente che utilizza agenti locali potrebbe leggere le istruzioni inviate agli agenti.

Per questo motivo il vantaggio competitivo non deve dipendere soltanto dalla segretezza dei prompt o delle checklist.

La parte più difficile da replicare deve risiedere nell’insieme di:

- motore delle regole;
- selezione contestuale;
- grafo semantico;
- acquisizione automatica delle evidenze;
- confronto tra dichiarazioni e fatti;
- verifica della verifica;
- memoria storica dei bug;
- procedure di blocco, deroga e riapertura;
- qualità delle decisioni prodotte dal sistema nel tempo.

La metodologia può quindi essere proprietaria e non pubblicata nel repository, ma il prodotto deve essere difendibile soprattutto per la profondità della sua implementazione.

---

## 27. Proprietà del software e proprietà dei dati

Il software deve distinguere chiaramente:

### Proprietà del produttore

- codice del prodotto;
- schema applicativo;
- motore delle regole;
- workflow;
- algoritmi di verifica;
- modelli semantici generali;
- procedure;
- template interni;
- sistemi di orchestrazione e compilazione del contesto.

### Proprietà del cliente o del titolare del progetto

- codice del progetto;
- requisiti;
- decisioni specifiche;
- report;
- evidenze;
- bug;
- storico operativo del proprio progetto;
- approvazioni e contenuti prodotti durante il lavoro.

Il database è governato dal software e non deve essere modificato direttamente, ma i contenuti specifici del progetto non diventano proprietà del produttore per il solo fatto di essere conservati al suo interno.

La politica di esportazione, portabilità e conservazione dovrà essere definita successivamente senza esporre il metodo proprietario.

---

## 28. Pubblicazione controllata della baseline

Il flusso approvato è:

```text
stato operativo nel database
        ↓
verifiche completate
        ↓
approvazione prevista
        ↓
creazione di una nuova baseline
        ↓
generazione o aggiornamento dei documenti di progetto
        ↓
commit della baseline pubblicata
```

Il software è responsabile di trasformare lo stato verificato in una versione leggibile e coerente da pubblicare nel repository.

Se un documento governato viene modificato manualmente nel repository, il sistema deve rilevare il disallineamento e proporre una delle seguenti azioni:

- importare la modifica come proposta non ancora approvata;
- ripristinare la baseline pubblicata;
- aprire una richiesta di cambiamento;
- registrare una deroga esplicita.

La modifica manuale non deve diventare automaticamente la nuova verità del progetto.

---

## 29. Decisione ufficiale

> Il progetto adotterà un modello ibrido. Nel repository saranno conservate soltanto le informazioni specifiche necessarie a comprendere, eseguire e mantenere il prodotto sviluppato: obiettivi, architettura, baseline tecnica pubblicata, requisiti, comportamenti, vincoli di dominio e decisioni progettuali pertinenti. Il metodo operativo di governance — linee guida, workflow, regole di verifica, formati dei report, gestione dei tentativi, procedure di collaudo, verifica della verifica e orchestrazione — non sarà pubblicato nel repository. Vivrà nel database e nel motore proprietario del software. Per ogni task il sistema compilerà soltanto le istruzioni strettamente necessarie all’esecuzione, mantenendole fuori dai commit del progetto. Il valore e la dipendenza dal prodotto dovranno derivare dalla capacità di governare, verificare e ricostruire il progetto, non dalla sottrazione al cliente dei propri dati.

---

## 30. Prossima questione tecnica

Dopo questa decisione, il prossimo punto da definire è dove debba vivere fisicamente il database governato dal software e come debba essere protetto:

- esclusivamente locale;
- esclusivamente cloud;
- locale con sincronizzazione cloud;
- database centrale con cache locale;
- modalità differenti per uso personale, team e installazione privata.

Questa scelta influenzerà sicurezza, continuità, proprietà dei dati, funzionamento offline, integrazione con repository locali e futura distribuzione del prodotto.


---

# Decisioni tecniche pre-MVP

## Integrazione v0.4 — perimetro iniziale, architettura logica e strategia del database

## 31. Stato raggiunto

Le decisioni concettuali già approvate consentono di iniziare la progettazione dell’MVP senza scegliere ancora un orchestratore di agenti IA.

Sono già definiti:

- scopo generale del prodotto;
- separazione tra verità locale della task e verità complessiva del progetto;
- distinzione tra write scope ristretto e verify scope ampio;
- livelli di verifica, collaudo e approvazione;
- task come contratto strutturato;
- report dell’esecutore trattato come dichiarazione da verificare;
- storico append-only e memoria semantica dei bug;
- modello ibrido repository/database;
- metodo operativo proprietario separato dalla documentazione del progetto;
- indipendenza da provider IA e orchestratori.

Il passo successivo non è ancora sviluppare agenti autonomi, ma costruire il nucleo che osserva, registra, verifica e governa un progetto software reale.

## 32. Responsabilità iniziale del prodotto

La prima versione deve essere capace di:

1. registrare un progetto software e collegarlo a un repository Git locale;
2. importare o registrare obiettivi, requisiti, decisioni, milestone, task e bug conosciuti;
3. creare una baseline iniziale approvata dall’utente;
4. trasformare una task in un contratto esecutivo strutturato;
5. generare un pacchetto temporaneo per un esecutore umano o IA;
6. ricevere e registrare il report dell’esecuzione;
7. osservare direttamente repository, diff, file, commit, branch e remoto;
8. eseguire soltanto controlli e comandi di verifica autorizzati;
9. confrontare quanto dichiarato nel report con le evidenze rilevate;
10. eseguire una verifica tecnica e una verifica macroscopica;
11. registrare collaudo, approvazione, blocchi, deroghe e riaperture;
12. pubblicare una nuova baseline soltanto dopo il completamento delle verifiche previste.

## 33. Funzioni escluse dall’MVP

La prima versione non deve ancora essere:

- un IDE;
- un coding agent;
- un sostituto di Git;
- un orchestratore autonomo obbligatorio;
- un sistema multiutente;
- un servizio cloud;
- un gestore automatico di commit e push senza approvazione;
- un project manager generalista;
- un sistema che modifica autonomamente il codice del cliente.

L’orchestrazione degli agenti verrà aggiunta successivamente tramite adapter, mantenendo separato il nucleo di governance.

## 34. Gerarchia delle fonti

La prima implementazione deve rispettare questa gerarchia:

```text
Evidenze osservate direttamente dal software
        ↓
Decisioni, approvazioni e deroghe registrate
        ↓
Stato operativo governato nel database
        ↓
Baseline pubblicata nel repository
        ↓
Documentazione generale del progetto
        ↓
Report e dichiarazioni di persone o agenti
```

Una dichiarazione non può prevalere su un’evidenza rilevabile.

Esempio:

```text
Report: push completato
Git remoto: commit assente
Esito governato: push non verificato
```

## 35. Modello semantico iniziale

Le entità minime previste sono:

```text
Project
Repository
Baseline
Requirement
Decision
Constraint
Milestone
Task
TaskExecution
ContextPackage
Evidence
Verification
Validation
Acceptance
Bug
Test
Commit
Exception
Approval
Event
Artifact
```

Relazioni minime:

```text
Task deriva da Requirement
Task deve rispettare Decision e Constraint
Task appartiene a Milestone
TaskExecution esegue Task
Evidence documenta TaskExecution
Verification controlla TaskExecution ed Evidence
Bug può essere scoperto durante una TaskExecution
Bug può essere collegato a Task, Commit o Artifact
Test può proteggere dalla ricomparsa di Bug
Baseline raccoglie risultati verificati e approvati
Exception consente una deroga limitata e tracciata
Approval autorizza una transizione o una nuova Baseline
```

## 36. Ciclo di vita iniziale della task

La task non deve avere un unico stato generico `done`.

Flusso principale:

```text
DRAFT
  ↓
ANALYZED
  ↓
READY
  ↓
IN_EXECUTION
  ↓
EXECUTION_REPORTED
  ↓
EVIDENCE_COLLECTION
  ↓
TECHNICAL_VERIFICATION
  ↓
MACRO_VERIFICATION
  ↓
FUNCTIONAL_VALIDATION
  ↓
HUMAN_APPROVAL
  ↓
COMPLETED
```

Stati laterali iniziali:

```text
BLOCKED
FAILED
PARTIALLY_COMPLETED
OUT_OF_SCOPE_FINDINGS
EVIDENCE_INCOMPLETE
REGRESSION_DETECTED
EXCEPTION_REQUIRED
REOPENED
CANCELLED
```

Internamente devono essere separati almeno:

- stato dell’esecuzione;
- completezza delle evidenze;
- verifica tecnica;
- verifica macroscopica;
- collaudo funzionale;
- accettazione umana;
- salute corrente del risultato.

## 37. Architettura logica iniziale

```text
Project Core
├── Project Model
├── Task Lifecycle
├── Baseline Manager
├── Requirement and Decision Registry
├── Bug Memory
└── Event History

Repository Observer
├── File Scanner
├── Git Observer
├── Diff Collector
├── Reference Search
└── Repository Snapshot

Verification Engine
├── Evidence Validator
├── Report Reconciler
├── Scope Validator
├── Technical Verifier
├── Macro Verifier
└── Verification-of-Verification

Method Engine
├── Proprietary Rule Selection
├── Procedure Selection
├── Completion Policies
├── Exception Policies
└── Context Compiler

Integration Layer
├── Manual Execution Adapter
├── Future AI Orchestrator Adapter
├── Git Provider Adapter
└── Test Runner Adapter

Persistence Layer
├── Domain Repository Interfaces
├── SQLite Adapter for MVP
├── Future PostgreSQL Adapter
├── Migration Runner
└── Artifact Storage
```

## 38. Perimetro tecnico dell’MVP

Decisioni approvate:

- un solo utente;
- progetti software;
- un repository locale per progetto;
- Git come primo sistema di versionamento;
- applicazione locale;
- interfaccia web locale;
- piccola CLI o processo ausiliario per scansioni e verifiche;
- database relazionale locale;
- esecuzioni inizialmente manuali o effettuate con strumenti esterni;
- controlli deterministici prima dell’analisi semantica tramite IA;
- approvazione umana per operazioni critiche;
- Tennis Decision UI come primo progetto reale di collaudo.

## 39. Potere del software sul repository

La prima versione adotterà il livello **esecutore controllato**.

Il software potrà:

- leggere file e cartelle autorizzate;
- leggere l’intero repository per le verifiche macroscopiche previste;
- osservare Git status, diff, branch, commit e remote tracking;
- eseguire ricerche testuali e strutturali;
- lanciare test e controlli configurati;
- raccogliere output, codici di risultato e artefatti;
- produrre report di discrepanza;
- preparare una proposta di baseline.

Il software non potrà inizialmente:

- modificare autonomamente il codice;
- cancellare file;
- creare commit senza azione esplicita dell’utente;
- eseguire push senza azione esplicita dell’utente;
- ampliare automaticamente il write scope;
- applicare una deroga senza approvazione.

## 40. Strategia di verifica

La sequenza approvata è:

```text
Controlli deterministici
        ↓
Analisi semantica circoscritta
        ↓
Decisione umana nei casi critici
```

### Controlli deterministici

Devono essere preferiti quando una risposta può essere dimostrata direttamente:

- file modificati reali;
- file dichiarati nel report;
- modifiche fuori scope;
- working tree;
- branch corrente;
- commit presente;
- commit raggiungibile dal remoto;
- test effettivamente eseguiti;
- esito dei test;
- occorrenze residue;
- artefatti obbligatori;
- output mancanti;
- numero di tentativi;
- hash e revisioni.

### Analisi semantica

Viene usata per valutare:

- contraddizioni con decisioni precedenti;
- soddisfacimento parziale del requisito;
- incoerenze nella documentazione;
- rischi di regressione;
- collegamenti con bug storici;
- sufficienza del perimetro di verifica;
- impatto su milestone e baseline;
- necessità di una nuova decisione.

## 41. SQLite: che cos’è e che cosa non è

SQLite non è un database JSON.

È un database relazionale SQL completo, incorporato direttamente nell’applicazione. I dati vengono normalmente conservati in un singolo file locale, per esempio:

```text
project-governance.sqlite
```

Non richiede un server separato, un servizio di rete o un processo database sempre attivo.

SQLite non simula Supabase. Sono due livelli tecnologici differenti:

- SQLite è un motore relazionale embedded e locale;
- Supabase fornisce una piattaforma costruita attorno a PostgreSQL, con database remoto o locale, autenticazione, API, realtime, storage e altre funzioni.

L’MVP può usare SQLite per semplicità e funzionamento locale, ma il modello dati deve essere progettato fin dall’inizio per poter essere trasferito successivamente a PostgreSQL o Supabase.

## 42. Decisione sul database dell’MVP

La prima versione utilizzerà **SQLite locale**, ma non come prototipo usa e getta.

Dovrà essere trattato come il primo adapter di persistenza di un modello relazionale indipendente.

Architettura prevista:

```text
Dominio applicativo
        ↓
Interfacce di persistenza
        ↓
SQLite Adapter — MVP
        ↓
PostgreSQL/Supabase Adapter — futuro
```

Il codice del dominio non deve dipendere direttamente dalle peculiarità di SQLite.

## 43. Regole per rendere semplice la migrazione futura

### 43.1 Schema relazionale normalizzato

Le entità centrali devono essere rappresentate con tabelle e relazioni esplicite. Non bisogna conservare l’intero progetto in un unico documento JSON.

JSON può essere utilizzato soltanto per:

- payload flessibili;
- risultati grezzi di strumenti;
- metadati non centrali;
- dati importati da provider esterni;
- snapshot temporanei o versionati.

Requisiti, task, verifiche, bug, approvazioni ed eventi devono avere strutture relazionali interrogabili.

### 43.2 Identificatori indipendenti dal database

Le entità devono utilizzare identificatori generati dall’applicazione, preferibilmente UUID o identificatori equivalenti, senza dipendere da sequenze locali specifiche di SQLite.

### 43.3 Date e tempo coerenti

Tutti gli eventi devono essere registrati in UTC e convertiti nel fuso dell’utente solo nell’interfaccia.

### 43.4 Migrazioni versionate dal primo giorno

Ogni modifica dello schema deve essere rappresentata da una migrazione numerata e riproducibile.

Non sono ammesse modifiche manuali non registrate alla struttura del database.

### 43.5 Data access layer separato

Query e comandi SQL non devono essere dispersi nell’intera applicazione.

Il dominio deve utilizzare repository o servizi di persistenza con contratti chiari, per esempio:

```text
ProjectRepository
TaskRepository
EvidenceRepository
VerificationRepository
EventStore
BugRepository
BaselineRepository
```

### 43.6 Evitare dipendenze SQLite-specifiche nel nucleo

Nel modello centrale devono essere evitati, salvo adapter dedicati:

- trigger che contengono logica di business fondamentale;
- funzioni SQL disponibili soltanto in SQLite;
- dipendenza dalla tipizzazione permissiva di SQLite;
- query non compatibili con PostgreSQL senza necessità reale;
- uso di `rowid` come identità di dominio;
- logica critica affidata a caratteristiche peculiari del file SQLite.

### 43.7 Tipi compatibili con PostgreSQL

Il modello applicativo deve definire chiaramente:

- UUID;
- stringhe con limiti e semantica espliciti;
- booleani;
- timestamp UTC;
- enumerazioni applicative;
- numeri interi e decimali;
- JSON soltanto dove giustificato;
- chiavi esterne;
- vincoli di unicità;
- campi nullabili definiti intenzionalmente.

L’adapter SQLite tradurrà questi tipi nel formato supportato localmente. L’adapter PostgreSQL li mapperà sui tipi nativi disponibili.

### 43.8 Logica di business nell’applicazione

Le decisioni su transizioni di stato, approvazioni, verifiche, deroghe e pubblicazione della baseline devono vivere nel dominio applicativo e nel Method Engine.

Il database deve imporre integrità strutturale, ma non deve diventare l’unico luogo in cui vive il metodo proprietario.

### 43.9 Esportazione e importazione canoniche

Il prodotto deve prevedere un formato di esportazione versionato, distinto dal file SQLite.

Esempio concettuale:

```text
project-export/
├── manifest.json
├── domain-data.ndjson
├── relations.ndjson
├── events.ndjson
├── evidence-index.ndjson
└── artifacts/
```

La futura migrazione verso PostgreSQL o Supabase deve avvenire attraverso un processo controllato di export/import o mediante uno strumento di migrazione dedicato, non tentando di caricare direttamente il file SQLite nel nuovo servizio.

### 43.10 Test su entrambi gli adapter

Quando verrà introdotto PostgreSQL, gli stessi test di contratto della persistenza dovranno essere eseguiti su:

- SQLite;
- PostgreSQL.

Il comportamento osservabile del dominio deve rimanere equivalente.

## 44. Quanto sarà semplice migrare a Supabase

La migrazione potrà essere resa **ordinata e prevedibile**, ma non sarà una conversione automatica perfetta del file SQLite.

SQLite e PostgreSQL differiscono per:

- sistema dei tipi;
- concorrenza;
- gestione di alcune alterazioni dello schema;
- funzioni SQL;
- vincoli e valori predefiniti;
- JSON e tipi avanzati;
- autenticazione e permessi;
- comportamento di alcune query.

Per questo la facilità della migrazione dipenderà più dall’architettura applicativa che dalla scelta di un ORM specifico.

Con le regole precedenti, il passaggio previsto sarà:

```text
1. creare lo schema PostgreSQL dalle migrazioni compatibili;
2. esportare i dati canonici dal database SQLite;
3. trasformare e validare i tipi;
4. importarli in PostgreSQL/Supabase;
5. confrontare conteggi, relazioni, hash ed eventi;
6. eseguire i test di contratto della persistenza;
7. cambiare l’adapter configurato;
8. mantenere SQLite come modalità locale o archivio esportabile.
```

## 45. Alternativa: PostgreSQL locale fin dall’inizio

Esiste una seconda possibilità: eseguire localmente PostgreSQL o l’intero stack Supabase tramite container.

Questa scelta renderebbe più simili gli ambienti locale e cloud, ma introdurrebbe fin dall’MVP:

- installazione più pesante;
- dipendenza da container o servizi locali;
- maggiore complessità per utenti non tecnici;
- avvio e manutenzione più articolati;
- più componenti da diagnosticare.

Per il primo MVP personale e single-user, SQLite offre un rapporto migliore tra semplicità e solidità.

PostgreSQL locale potrà essere aggiunto come modalità avanzata o usato nei test di compatibilità prima della migrazione cloud.

## 46. Protezione del metodo proprietario con database locale

Un file SQLite locale può essere ispezionato da un utente determinato. Per questo il metodo proprietario non deve essere protetto semplicemente nascondendolo nel database.

Nel database locale possono essere conservati:

- identificativi delle policy applicate;
- versione del motore;
- decisioni prodotte;
- controlli richiesti;
- risultati;
- eventi;
- pacchetti esecutivi compilati;
- evidenze del progetto.

Non devono necessariamente essere conservati in forma leggibile:

- l’intero catalogo delle regole proprietarie;
- le strategie complete di selezione;
- i pesi del motore di rischio;
- tutte le euristiche interne;
- i template sorgente del metodo;
- la logica completa della verifica della verifica.

Questi elementi devono vivere principalmente nel codice e nei moduli del prodotto. Il database registra che cosa è stato applicato e con quale versione, non deve contenere obbligatoriamente l’intera ricetta che ha prodotto la decisione.

## 47. Flusso completo dell’MVP

```text
1. Creazione o importazione del progetto
2. Collegamento del repository locale
3. Scansione iniziale di file, Git e documentazione
4. Estrazione assistita di requisiti, decisioni, task e bug
5. Conferma umana della baseline iniziale
6. Creazione di una task strutturata
7. Compilazione del pacchetto esecutivo
8. Esecuzione manuale o tramite strumento esterno
9. Importazione del report dell’esecutore
10. Raccolta automatica delle evidenze reali
11. Riconciliazione report/evidenze
12. Controlli tecnici deterministici
13. Verifica macroscopica e semantica
14. Collaudo funzionale
15. Approvazione umana o registrazione del blocco
16. Pubblicazione della nuova baseline
17. Registrazione append-only dell’intero passaggio
```

## 48. Decisione ufficiale della fase pre-MVP

> La prima versione sarà un’applicazione locale, single-user e orientata ai progetti software. Utilizzerà un database relazionale SQLite incorporato, non un archivio JSON. SQLite sarà implementato come adapter di persistenza di un dominio indipendente e progettato per una futura migrazione verso PostgreSQL o Supabase. Lo schema sarà relazionale, versionato tramite migrazioni e accompagnato da un formato canonico di esportazione. La logica di governance resterà nel dominio applicativo e nel motore proprietario, non verrà affidata a caratteristiche specifiche del database. Il software potrà leggere il repository ed eseguire controlli autorizzati, ma non modificherà autonomamente il codice né effettuerà commit o push senza un’azione esplicita dell’utente. Il primo collaudo reale verrà eseguito sul progetto Tennis Decision UI.

## 49. Questioni ancora da decidere

Prima di scrivere la specifica tecnica completa restano da definire:

1. stack applicativo e linguaggio del prodotto;
2. forma esatta dell’interfaccia web locale e della CLI;
3. confine tra un database globale del software e database separati per progetto;
4. struttura concreta delle tabelle e dell’event store;
5. modalità di importazione della documentazione e della To-Do esistenti;
6. formato strutturato dei report degli esecutori;
7. modalità sicura di esecuzione dei test e dei comandi autorizzati;
8. strategia iniziale della verifica semantica tramite IA;
9. meccanismo di pubblicazione della baseline nel repository;
10. regole di backup, esportazione e recupero del database locale;
11. criteri per introdurre il primo adapter di orchestrazione degli agenti;
12. limiti esatti dell’MVP da collaudare sul Tennis Decision UI.

---

## 50. Database SQLite separato per ciascun progetto

La prima versione utilizzerà **un database SQLite indipendente per ogni progetto**.

Struttura concettuale:

```text
Progetto A
├── repository A
└── database operativo A

Progetto B
├── repository B
└── database operativo B
```

Questa scelta viene adottata per i seguenti motivi:

- isolamento dei dati tra progetti e clienti differenti;
- riduzione del rischio che errori o corruzioni coinvolgano l’intera installazione;
- backup, ripristino, archiviazione e trasferimento eseguibili per singolo progetto;
- crescita controllata di log, evidenze, esecuzioni e storico;
- possibilità di migrare i progetti verso PostgreSQL in momenti diversi;
- maggiore semplicità nel collaudo iniziale e nella diagnosi dei problemi;
- minore rischio di contaminazione semantica tra contesti differenti.

Ogni database conserverà esclusivamente lo stato operativo e semantico del progetto al quale appartiene.

## 51. Registro globale minimo dell’applicazione

Pur adottando un database per progetto, l’applicazione dovrà mantenere un piccolo registro globale per individuare i progetti conosciuti.

Il registro conterrà soltanto dati di apertura e localizzazione, per esempio:

```text
project_id
project_name
repository_path
database_path
schema_version
last_opened_at
availability_status
```

Non conterrà:

- task;
- bug;
- decisioni;
- verifiche;
- evidenze;
- storico operativo;
- pacchetti di contesto.

Il registro globale non sarà quindi una fonte di verità del progetto, ma soltanto l’indice locale dell’installazione.

## 52. Presenza obbligatoria di `project_id`

Anche se ogni database contiene inizialmente un solo progetto, tutte le entità principali dovranno includere un identificatore stabile `project_id`.

Esempio:

```text
tasks
├── id
├── project_id
├── title
└── ...

bugs
├── id
├── project_id
├── title
└── ...
```

La ridondanza è intenzionale e prepara la futura migrazione verso un database PostgreSQL condiviso, nel quale più progetti potranno convivere mantenendo una separazione esplicita.

## 53. Collocazione fisica dei database

Il file SQLite non dovrà essere versionato normalmente dentro il repository Git del progetto.

Motivazioni:

- SQLite è un file binario che cambia frequentemente;
- Git non può rappresentarne utilmente le differenze interne;
- il database può contenere log, evidenze, output degli agenti e informazioni operative sensibili;
- il metodo proprietario e lo stato di governance non devono diventare parte della documentazione pubblicata nel repository;
- il database deve poter essere sottoposto a backup con procedure differenti rispetto al codice.

La collocazione predefinita sarà nell’area privata dell’applicazione:

```text
Project Integrity OS/
└── data/
    └── <project-uuid>/
        ├── project.sqlite
        ├── backups/
        ├── evidence-files/
        ├── exports/
        └── project-link.json
```

Il collegamento con il repository verrà mantenuto tramite:

- UUID del progetto;
- percorso locale del repository;
- remote Git, quando disponibile;
- hash o identificatore della baseline pubblicata;
- commit Git di riferimento;
- versione dello schema del database.

## 54. Manifest minimo nel repository

Nel repository potrà essere pubblicato un manifest minimo, privo del metodo proprietario, per collegare il codice alla baseline governata dal software.

Esempio concettuale:

```yaml
project_id: 3af04a07-...
governance_manifest_version: 1
published_baseline_id: baseline-0042
published_baseline_revision: 42
repository_commit: abc123
```

Il manifest non conterrà procedure, workflow, euristiche o linee guida proprietarie del software.

## 55. Modalità portabile, backup ed esportazione

In futuro il software dovrà poter produrre un pacchetto trasportabile per:

- backup completo;
- trasferimento su un altro computer;
- passaggio a un altro utente;
- archiviazione del progetto concluso;
- migrazione verso PostgreSQL o un servizio cloud.

Esempio concettuale:

```text
<project-name>.project-package
├── project.sqlite
├── manifest.json
├── exported-documents/
├── evidence-index/
└── checksums.json
```

Il pacchetto portabile non sostituisce il formato canonico di esportazione definito per le migrazioni, ma può contenerlo o richiamarlo.

## 56. Nome tecnico provvisorio e cartella di lavoro

Il nome tecnico provvisorio scelto per il progetto è:

```text
Project Integrity OS
```

La cartella principale di lavoro sul computer dell’utente sarà:

```text
C:\Users\Utente\Desktop\Project Integrity OS
```

Il nome è intenzionalmente indipendente da:

- uno specifico modello IA;
- un determinato orchestratore;
- un provider Git;
- uno stack applicativo;
- una singola modalità di esecuzione.

Descrive invece il nucleo del prodotto: mantenere integrità, continuità, verificabilità e governo semantico dei progetti.

## 57. Decisione ufficiale aggiornata

> La prima versione di Project Integrity OS adotterà un database SQLite indipendente per ogni progetto. I database risiederanno nell’area privata dell’applicazione e non saranno normalmente versionati nei repository Git. Un piccolo registro globale conterrà soltanto i dati necessari a localizzare e aprire i progetti. Ogni entità manterrà comunque il proprio `project_id` per preparare la futura migrazione verso PostgreSQL. Il repository potrà contenere un manifest minimo che collega il codice alla baseline pubblicata, senza esporre il metodo proprietario. Saranno previste procedure di backup, esportazione e trasferimento per singolo progetto.

## 58. Prossime decisioni tecniche

Con questa scelta risultano chiuse le questioni relative a:

- database locale o JSON;
- preparazione alla migrazione PostgreSQL/Supabase;
- database unico o separato per progetto;
- collocazione del file SQLite;
- registro globale dell’applicazione;
- identità stabile del progetto;
- nome tecnico e cartella iniziale di lavoro.

Le prossime aree da definire sono:

1. stack applicativo e linguaggi;
2. struttura delle cartelle del nuovo software;
3. architettura dei processi locali;
4. schema dati iniziale del database;
5. forma dell’interfaccia web locale e della CLI;
6. modalità di collegamento e scansione di un repository esistente;
7. formato del contratto della task e del report esecutivo;
8. sistema sicuro per eseguire controlli e test autorizzati;
9. strategia della prima verifica macroscopica;
10. confine esatto dell’MVP da collaudare sul Tennis Decision UI.


---

# Aggiornamento v0.6 — Stack applicativo desktop

## 59. Decisione sullo stack applicativo

La prima versione di **Project Integrity OS** sarà realizzata come applicazione desktop locale con il seguente stack:

```text
Desktop shell e integrazione nativa: Tauri 2
Interfaccia utente: React + TypeScript + Vite
Core applicativo locale: Rust
Runtime asincrono: Tokio, dove necessario
Persistenza MVP: SQLite
Toolkit SQL e migrazioni: SQLx
Persistenza futura: adapter PostgreSQL, compatibile con un eventuale servizio Supabase
Distribuzione iniziale: installer Windows NSIS o MSI
```

Questa scelta mantiene la familiarità del frontend React, ma sostituisce il normale backend Node.js con un core nativo Rust progettato specificamente per:

- accesso controllato al filesystem;
- osservazione del repository;
- interrogazione dello stato Git;
- esecuzione sicura di test e verifiche autorizzate;
- gestione dei database SQLite locali;
- raccolta delle evidenze;
- applicazione delle procedure proprietarie;
- futura distribuzione come programma desktop installabile.

## 60. Motivazione della scelta di Tauri 2

Tauri viene scelto perché separa bene due responsabilità:

```text
React / TypeScript
→ visualizzazione, navigazione e interazione con l’utente

Rust
→ dominio, sicurezza, persistenza, filesystem, Git,
  processi locali, evidenze e verifiche
```

I vantaggi concreti per Project Integrity OS sono:

1. applicazione desktop reale, senza dover mantenere un server locale separato visibile all’utente;
2. accesso nativo controllato alle risorse del computer;
3. frontend web moderno, riutilizzabile in parte in una futura interfaccia cloud;
4. backend compilato e fortemente tipizzato;
5. modello di permessi e capacità adatto a limitare l’accesso di ogni finestra e comando;
6. installer Windows e meccanismo di aggiornamento disponibili nell’ecosistema ufficiale;
7. dimensioni generalmente inferiori rispetto a framework che incorporano un intero browser;
8. possibilità di aggiungere in futuro supporto per macOS e Linux senza cambiare il dominio centrale.

## 61. Ruolo del frontend

Il frontend React non sarà la fonte della verità e non accederà direttamente al database.

Avrà il compito di:

- mostrare stato, task, bug, decisioni, verifiche e baseline;
- raccogliere intenzioni e approvazioni dell’utente;
- visualizzare discrepanze ed evidenze;
- avviare operazioni esplicite attraverso comandi tipizzati;
- mostrare avanzamento, errori e risultati dei controlli.

Il frontend non dovrà:

- costruire direttamente query SQL;
- modificare file arbitrari;
- eseguire comandi generici;
- determinare autonomamente che una task è completata;
- aggiornare lo stato governato senza passare dal core applicativo.

## 62. Ruolo del core Rust

Il core Rust sarà il vero livello applicativo locale.

Conterrà:

```text
Domain
├── Project
├── Task
├── Requirement
├── Decision
├── Bug
├── Verification
├── Evidence
├── Baseline
└── Event

Application Services
├── Task Lifecycle Service
├── Evidence Collection Service
├── Verification Service
├── Baseline Service
├── Context Compiler
├── Bug Memory Service
└── Exception and Approval Service

Infrastructure
├── SQLite Persistence Adapter
├── Future PostgreSQL Adapter
├── Repository Observer
├── Git Adapter
├── File Search Adapter
├── Controlled Process Runner
├── Backup and Export Adapter
└── Orchestrator Adapters
```

Le finestre Tauri comunicheranno con il core tramite comandi espliciti e tipizzati. Non verrà esposto al frontend un accesso generico al sistema operativo.

## 63. Persistenza con SQLx

Per l’MVP verrà utilizzato SQLx dal lato Rust, non l’accesso diretto al database dal frontend.

SQLx viene scelto perché supporta sia SQLite sia PostgreSQL e offre:

- query SQL esplicite;
- supporto alle migrazioni;
- transazioni;
- mapping tipizzato dei risultati;
- supporto a UUID, date e JSON;
- possibilità di realizzare adapter distinti sullo stesso dominio.

Architettura prevista:

```text
Dominio e servizi applicativi
          ↓
Interfacce di persistenza
          ↓
SQLite Adapter — prima versione
          ↓
PostgreSQL Adapter — futuro
```

Non si assumerà che una query SQLite funzioni automaticamente su PostgreSQL. Le differenze di dialetto, tipi e migrazioni verranno isolate nei rispettivi adapter e verificate con test condivisi di conformità.

## 64. Regola: nessun accesso diretto dal frontend a SQLite

Anche se l’ecosistema Tauri permette tecnicamente di comunicare con SQLite dal codice TypeScript, Project Integrity OS non utilizzerà questa scorciatoia per il dominio principale.

Il flusso corretto sarà:

```text
Interfaccia React
      ↓ richiesta tipizzata
Servizio applicativo Rust
      ↓ applicazione di regole e autorizzazioni
Repository di dominio
      ↓
SQLx / SQLite
```

Questa separazione serve a:

- proteggere il metodo proprietario;
- impedire aggiornamenti incoerenti;
- applicare sempre regole, eventi e transazioni;
- facilitare il passaggio a PostgreSQL;
- rendere testabile il dominio senza dipendere dall’interfaccia grafica.

## 65. Esecuzione sicura dei comandi locali

Il software non offrirà un terminale generico e non inoltrerà stringhe arbitrarie a una shell.

Verrà creato un **Controlled Process Runner** che riceve definizioni strutturate:

```text
program
arguments
working_directory
allowed_paths
timeout
environment_allowlist
expected_outputs
capture_stdout
capture_stderr
```

Principi iniziali:

- esecuzione senza shell quando possibile;
- programma e argomenti separati;
- directory di lavoro limitata al repository autorizzato;
- lista dei programmi consentiti;
- timeout obbligatorio;
- cattura completa di output ed errori;
- nessuna modifica automatica al codice;
- nessun commit o push senza azione umana esplicita;
- registrazione dell’esecuzione come evidenza;
- impossibilità per il frontend di aggirare il runner controllato.

Il sistema di capacità e permessi Tauri verrà usato come ulteriore barriera, ma la validazione principale resterà nel core Rust.

## 66. Distribuzione iniziale

La prima distribuzione sarà rivolta a Windows.

Obiettivi:

- installer standard;
- installazione per utente senza privilegi amministrativi, quando possibile;
- area dati privata dell’applicazione;
- database separato per progetto;
- backup configurabili;
- aggiornamenti firmati in una fase successiva;
- possibilità futura di pubblicazione tramite canali standard Windows.

La compatibilità multipiattaforma resterà un vincolo architetturale, ma non allargherà il perimetro del primo MVP.

## 67. Alternative considerate

### Electron

Electron resta una soluzione valida e molto diffusa, ma non viene scelto come base iniziale perché Project Integrity OS richiede un nucleo locale privilegiato, strettamente controllato e separato dall’interfaccia. Tauri permette di mantenere il frontend web senza incorporare l’intero modello Node.js come base del livello nativo.

### Avalonia / .NET

Avalonia sarebbe una buona alternativa per un’applicazione desktop completamente .NET, con accesso naturale a SQLite e ai processi locali. Non viene scelto come prima opzione perché React è già familiare, una parte maggiore dell’interfaccia potrà essere riutilizzata in un futuro prodotto web e Tauri offre una separazione particolarmente adatta tra webview e core nativo.

Avalonia resta una possibile alternativa tecnica qualora Tauri introduca limiti concreti durante il prototipo.

## 68. Rischi e limiti della scelta

La scelta non è priva di costi:

- Rust introduce una curva di apprendimento superiore a Node.js;
- la compilazione nativa può essere più lenta durante lo sviluppo;
- occorre progettare con attenzione il confine tra frontend e backend;
- le WebView di sistemi operativi diversi possono avere differenze;
- SQLx supporta più database, ma non rende automaticamente portabili query e migrazioni;
- l’esecuzione di processi locali rimane una funzione sensibile e dovrà essere progettata con test di sicurezza specifici;
- la firma degli installer e degli aggiornamenti richiederà una procedura dedicata prima della distribuzione pubblica.

Questi costi sono accettati perché corrispondono alle necessità centrali del prodotto: controllo locale, sicurezza, persistenza, verificabilità e distribuzione desktop.

## 69. Decisione ufficiale sullo stack

> Project Integrity OS sarà sviluppato inizialmente con Tauri 2, React, TypeScript, Vite e un core Rust. Il database operativo sarà SQLite, gestito dal core tramite SQLx e separato per progetto. L’architettura di persistenza sarà basata su interfacce e adapter per consentire un futuro backend PostgreSQL. Il frontend non accederà direttamente al database o al sistema operativo. Test, ricerche, Git e altri processi locali passeranno attraverso servizi Rust controllati, con permessi, scope, timeout e registrazione delle evidenze. La prima distribuzione sarà Windows, mantenendo il dominio indipendente dalla piattaforma.

## 70. Prossime decisioni tecniche

Dopo la scelta dello stack, le prossime decisioni sono:

1. topologia dei processi e confine preciso tra Tauri, core e processi figli;
2. struttura iniziale delle cartelle e dei crate Rust;
3. schema relazionale SQLite della prima versione;
4. identificatori, timestamp, revisioni e strategia degli eventi;
5. contratto tipizzato tra React e Rust;
6. modello del Controlled Process Runner;
7. integrazione Git iniziale: CLI controllata oppure libreria;
8. struttura dell’interfaccia principale;
9. formato del progetto importato e procedura di onboarding;
10. perimetro esatto del primo vertical slice da provare sul Tennis Decision UI.
