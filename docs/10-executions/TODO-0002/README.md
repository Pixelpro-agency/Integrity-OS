# TODO-0002 — Archivio organizzato della task

## Scopo del pacchetto

Questo archivio conserva **tutti i 13 file presenti nello ZIP originale**, senza modificarne il contenuto. I file sono stati soltanto:

- distribuiti in cartelle secondo il ruolo reale svolto nella task;
- rinominati con nomi più espliciti e ordinabili;
- collegati al nome e al percorso originali tramite `FILE_MAP.csv` e `manifest.json`;
- protetti da hash SHA-256 riportati in `MANIFEST_SHA256.txt`.

Il pacchetto serve sia alla consultazione umana sia a un futuro importatore di Project Integrity OS capace di ricostruire il ciclo di lavoro.

## Stato ricostruito della task

| Campo | Valore |
|---|---|
| Task | `TODO-0002 — Creare la struttura iniziale del repository Project Integrity OS` |
| Modalità effettiva | `BROWSER_OPERATOR_ASSISTED` |
| Brief realmente usato | v0.2 |
| Prompt realmente usato | prompt browser v0.1 |
| Report esecutore | presente |
| Verifica indipendente | `SUPERATA` |
| Approvazione umana | `APPROVATA` |
| Deviazione | `DEV-TODO-0002-001 — ACCETTATA` |
| Commit baseline | autorizzato localmente |
| Push | non autorizzato |
| Stato finale | `DONE`, subordinato alla chiusura documentale e al commit baseline locale |

## Ordine di lettura consigliato

### Per capire come fu eseguita la task

1. `01-esecuzione-effettiva/TODO-0002_01_Brief_Esecuzione_v0_2_USED_THEN_SUPERSEDED.md`
2. `01-esecuzione-effettiva/TODO-0002_02_Prompt_Browser_Operatore_v0_1_USED.md`
3. `01-esecuzione-effettiva/TODO-0002_03_Start_Here_Browser_Operatore_v0_1_USED.md`
4. `02-risultati-e-verifica/TODO-0002_04_Report_Esecutore_v0_1_FINAL.md`
5. `02-risultati-e-verifica/TODO-0002_05_Verifica_Indipendente_v0_1_PASSED.md`
6. `03-validazione-umana/TODO-0002_07_Deviazione_DEV-TODO-0002-001_v0_1_ACCEPTED.md`
7. `03-validazione-umana/TODO-0002_06_Approvazione_Umana_v0_1_APPROVED.md`
8. `04-chiusura-documentale/TODO-0002_08_Brief_Finale_Chiusura_v0_3_FINAL.md`

### Per studiare l’evoluzione del metodo

Dopo la sequenza principale, leggere:

- `90-storico-non-utilizzato/TODO-0002_91_Brief_Iniziale_v0_1_SUPERSEDED.md`;
- `90-storico-non-utilizzato/TODO-0002_92_Prompt_Desktop_v0_1_NOT_USED_SUPERSEDED.md`;
- `90-storico-non-utilizzato/TODO-0002_93_Start_Here_Desktop_v0_1_NOT_USED_SUPERSEDED.md`.

Questi documenti mostrano il passaggio dalla modalità desktop/local alla modalità browser con operatore umano.

## Significato delle cartelle

### `01-esecuzione-effettiva/`

Contiene le istruzioni realmente utilizzate durante la task. Il brief v0.2 porta oggi lo stato `SUPERSEDED`, ma resta la **baseline autentica dell’esecuzione**.

### `02-risultati-e-verifica/`

Contiene due livelli distinti:

- il report dell’esecutore, cioè ciò che è stato dichiarato;
- la verifica indipendente, cioè il controllo delle dichiarazioni rispetto alle evidenze disponibili.

### `03-validazione-umana/`

Contiene la decisione umana finale e la deviazione procedurale accettata.

### `04-chiusura-documentale/`

Contiene gli artefatti prodotti o utilizzati per chiudere documentalmente la task. Il brief v0.3 è la versione finale archiviata, non il brief che guidò materialmente l’esecuzione.

### `90-storico-non-utilizzato/`

Contiene versioni sostituite o mai utilizzate. Sono conservate perché permettono di ricostruire decisioni e cambi di modalità.

## Avvertenze importanti

1. **Non eseguire nuovamente lo script di chiusura.**
   `TODO-0002_10_Script_Chiusura_v0_1_EXECUTED_DO_NOT_RERUN.py` contiene percorsi assoluti, nomi storici e condizioni valide nel contesto originario.

2. Il runbook di chiusura cita `close_todo_0002.py`, mentre lo script conservato nello ZIP originale aveva un nome diverso. La discrepanza viene mantenuta perché i file non sono stati riscritti.

3. Alcuni documenti citano artefatti esterni come specifica FROZEN, To-Do, modalità di esecuzione o `preserved-originals`. Tali file non erano contenuti nello ZIP sorgente e quindi non sono stati inventati o aggiunti.

4. `FINAL`, `USED`, `PASSED`, `APPROVED`, `ACCEPTED` ed `EXECUTED` descrivono ruoli diversi:
   - `USED`: realmente impiegato durante l’esecuzione;
   - `FINAL`: artefatto conclusivo;
   - `PASSED`: verifica superata;
   - `APPROVED`: approvazione umana;
   - `ACCEPTED`: deviazione accettata;
   - `EXECUTED`: procedura o script già eseguiti;
   - `SUPERSEDED`: sostituito da una versione successiva;
   - `NOT_USED`: conservato ma non utilizzato nella task reale.

## File di supporto

- `FILE_MAP.csv`: mappa il percorso originale al nuovo percorso organizzato.
- `manifest.json`: metadati strutturati per un futuro importatore.
- `MANIFEST_SHA256.txt`: hash dei 13 documenti copiati.

## Integrità

I 13 documenti originari sono stati copiati byte per byte. La riorganizzazione modifica soltanto cartelle e nomi dei file. Gli hash permettono di verificare che il contenuto sia rimasto invariato.
