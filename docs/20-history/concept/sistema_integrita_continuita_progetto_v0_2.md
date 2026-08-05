# Sistema di integrità e continuità del progetto

## Bozza concettuale v0.2 — decisioni preliminari approvate

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
- quali dati conservare in file versionati e quali in un database locale;
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
