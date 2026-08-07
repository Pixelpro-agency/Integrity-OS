# Project Integrity OS
## Prompt di avvio chat esecutiva — TODO-0002

> **Nome documentale normalizzato.** L’artefatto originale, con il nome usato durante l’esecuzione, è conservato nel pacchetto, sotto `preserved-originals/20-history/original-artifacts/legacy-names/`.


Agisci esclusivamente come **esecutore tecnico** della task `TODO-0002 — Creare la struttura iniziale del repository Project Integrity OS`.

## Documenti autorevoli allegati

1. `Project_Integrity_OS_Flussi_MVP_v0_2_FROZEN.md`
2. `Project_Integrity_OS_TODO_MVP_v0_3.md`
3. `Project_Integrity_OS_Brief_TODO-0002.md`

Leggili integralmente prima di modificare file. In caso di conflitto, prevale il brief esecutivo per lo scope della task e la specifica FROZEN per i vincoli funzionali generali.

## Percorso di lavoro

```text
C:\Users\Utente\Desktop\Project Integrity OS
```

Se la cartella non esiste, creala. Se esiste, ispezionala prima di intervenire e non sovrascrivere materiale non riconosciuto.

## Obiettivo unico

Creare e verificare lo scaffold iniziale con:

- Tauri 2;
- React;
- TypeScript;
- Vite;
- core Rust;
- comando Tauri tipizzato `get_app_info`;
- schermata iniziale che mostri caricamento, risultato ed errore;
- documenti approvati nella cartella `docs/`;
- README aderente allo stato reale.

Non implementare SQLite, Git Inspector, task lifecycle, motori di verifica, orchestratori, API IA, cloud, commit automatici o push automatici.

## Metodo obbligatorio

- Esegui il pre-flight previsto dal brief.
- Usa massimo 3 tentativi ragionati.
- Non usare comandi che chiudano la shell o terminino la sessione.
- In caso di controllo fallito, stampa chiaramente l’errore e impedisci i passaggi successivi con condizioni o catene sicure.
- Non dichiarare verifiche visuali, build, commit o push che non hai realmente osservato.
- Non iniziare TODO-0003 o task successive.

## Git

- Inizializza Git solo se necessario.
- Non eseguire push.
- Crea un commit solo se il brief e lo stato locale lo consentono; in ogni caso riporta con precisione ciò che è stato fatto.

## Output finale obbligatorio

Restituisci esattamente tutte le sezioni richieste nel paragrafo **12. Report finale obbligatorio** del brief, senza omissioni. Usa `nessuno`, `non eseguito` o `non verificato` quando appropriato.

Fermati dopo il report. Non proporre né avviare la task successiva.
