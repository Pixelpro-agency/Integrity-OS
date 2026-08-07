from pathlib import Path
import shutil
import re

BASE = Path(r"C:\Users\Utente\Desktop\Project Integrity OS")
CLOSED_AT = "2026-08-05 02:15 Europe/Rome"

EXECUTOR_REPORT = '# Project Integrity OS\n## Report esecutivo — TODO-0002\n### Modalità BROWSER_OPERATOR_ASSISTED\n\n**Esito dichiarato dall’esecutore:** SUCCESSO TECNICO  \n**Proponibile per verifica indipendente:** sì  \n**Stato della task al momento del report:** `IN_PROGRESS`\n\n---\n\n## Tentativi eseguiti\n\nDue tentativi correttivi falliti complessivi:\n\n1. prima scrittura di `app/mod.rs` incompleta a causa dell’incolla parziale del blocco PowerShell;\n2. primo `cargo check` del frontend integrato fallito per il residuo `opener:default` nella capability Tauri.\n\nEntrambi i problemi sono stati diagnosticati e risolti al tentativo successivo. Nessun problema ha raggiunto il limite di tre tentativi.\n\n---\n\n## Prerequisiti verificati\n\n- Windows 10 x64, build 19045;\n- PowerShell 5.1;\n- Node.js `24.11.1`;\n- npm `11.6.2`;\n- Rustup `1.29.0`;\n- Rust `1.97.1`;\n- Cargo `1.97.1`;\n- toolchain `stable-x86_64-pc-windows-msvc`;\n- Visual Studio Build Tools 2022 `17.14.37`;\n- workload C++ desktop;\n- MSVC v143 x64/x86;\n- Windows 11 SDK `10.0.26100.0`;\n- CMake tools per Windows;\n- WebView2 Runtime presente;\n- Git `2.42.0.windows.2`.\n\n**Evidenza dichiarata:** output dei controlli PowerShell, `rustup`, `rustc`, `cargo`, `node`, `npm` e `vswhere` forniti durante i checkpoint.\n\n**Elementi non verificati dichiarati:** nessuno tra i prerequisiti obbligatori di TODO-0002.\n\n---\n\n## File e cartelle dichiarati creati\n\n- scaffold Tauri in `C:\\Users\\Utente\\Desktop\\Project Integrity OS`;\n- `.vscode/`;\n- `public/`;\n- `src/`;\n- `src-tauri/`;\n- `src-tauri/src/app/`;\n- `src-tauri/src/app/mod.rs`;\n- `node_modules/`;\n- `dist/`;\n- `src-tauri/target/`;\n- `.git/`;\n- `package-lock.json`;\n- file standard React, TypeScript, Vite e Tauri generati dallo scaffold.\n\nLa cartella `docs/` preesistente è stata conservata e integrata nel repository senza sovrascritture.\n\n**Evidenza dichiarata:** elenco top-level osservato, verifica dei file in `src/`, `src-tauri/src/` e audit finale.\n\n---\n\n## File dichiarati modificati\n\n- `src/App.tsx`;\n- `src/App.css`;\n- `src-tauri/src/lib.rs`;\n- `src-tauri/src/app/mod.rs`;\n- `src-tauri/Cargo.toml`;\n- `src-tauri/tauri.conf.json`;\n- `src-tauri/capabilities/default.json`;\n- `package.json`;\n- `package-lock.json`;\n- `README.md`;\n- `.gitignore`;\n- `docs/00-current/Project_Integrity_OS_Brief_TODO-0002_v0_2_ACTIVE.md`, limitatamente alla correzione dei riferimenti interni al nome versionato del brief.\n\n**Evidenza dichiarata:** contenuti dei file Rust mostrati, controlli JSON, ricerca dei residui e audit README.\n\n---\n\n## Comandi dichiarati eseguiti dall’utente\n\n- installazione e verifica Visual Studio Build Tools;\n- installazione Rustup tramite `winget`;\n- configurazione toolchain Rust MSVC;\n- `npm create tauri-app@latest project-integrity-os`;\n- `cargo fmt`;\n- `cargo check`;\n- `npm install`;\n- `npm run build`;\n- `npm run tauri dev`;\n- `npm run tauri build`;\n- avvio manuale dell’eseguibile release;\n- `git init -b main`;\n- verifiche `git status`;\n- rimozione degli installer fuori procedura;\n- rimozione della cartella temporanea dello scaffold.\n\n**Output dichiarato:** scaffold creato, compilazioni concluse, applicazione avviata, repository Git inizializzato e audit finale superato.\n\n---\n\n## Esito dichiarato dei controlli e test\n\n- scaffold React + TypeScript + Vite confermato;\n- identifier Tauri: `com.projectintegrity.os`;\n- product name: `Project Integrity OS`;\n- window title: `Project Integrity OS`;\n- comando Rust `get_app_info` compilato e registrato;\n- serializzazione Rust in camelCase verificata;\n- `cargo check`: codice `0`;\n- build frontend: riuscita;\n- `npm run tauri dev`: riuscito;\n- finestra desktop: aperta correttamente;\n- comunicazione frontend–Rust: riuscita;\n- nessun residuo operativo di `greet`, `plugin-opener`, `tauri_plugin_opener` o `opener:default`;\n- README generico dello scaffold rimosso;\n- README coerente con TODO-0002;\n- dipendenze e output di build esclusi dal working tree tramite `.gitignore`;\n- bundle MSI/NSIS residui: assenti;\n- cartella temporanea dello scaffold: assente;\n- audit finale: `CHECKPOINT I SUPERATO`.\n\nLa build release è terminata con codice `0`, producendo inizialmente eseguibile e installer. Gli installer sono stati poi rimossi perché il brief stabiliva di non costruirli durante TODO-0002.\n\n---\n\n## Verifica dichiarata dell’avvio Tauri\n\n- applicazione avviata tramite `npm run tauri dev`;\n- output: `Finished dev profile` e avvio di `target\\debug\\project-integrity-os.exe`;\n- finestra verificata tramite screenshot;\n- titolo: `Project Integrity OS`;\n- nessun errore runtime visibile;\n- warning linker osservato ma non bloccante.\n\n**Tipo evidenza:** output e conferma manuale tramite screenshot.\n\n---\n\n## Verifica dichiarata della comunicazione frontend–Rust\n\nLa UI ha mostrato:\n\n- Application: `Project Integrity OS`;\n- Version: `0.1.0`;\n- Core status: `ready`;\n- Operating mode: `deterministic-first`.\n\n**Tipo evidenza:** output di compilazione e conferma manuale tramite screenshot.\n\n---\n\n## Git al momento del report\n\n- repository inizializzato: sì;\n- branch: `main`;\n- commit creato: no;\n- hash commit: non applicabile;\n- push eseguito: no;\n- working tree: non pulito, con file non tracciati;\n- `node_modules/`, `dist/` e `src-tauri/target/` esclusi dal working tree.\n\n---\n\n## Discrepanze dichiarate\n\n1. `npm run tauri build` è stato eseguito nonostante il brief vietasse la costruzione degli installer in TODO-0002. Gli installer sono stati successivamente rimossi.\n2. Alcuni blocchi PowerShell sono stati incollati parzialmente, producendo output incompleti o codice inizialmente corrotto. I file sono stati riscritti e validati.\n3. L’audit finale del README è basato su ricerca dei riferimenti obbligatori e assenza del testo generico; il contenuto completo finale non è stato nuovamente incollato nella chat.\n4. Al momento del report non era ancora stata eseguita una verifica indipendente.\n\n---\n\n## Funzioni volutamente non implementate\n\n- database e persistenza SQLite;\n- schema dati di dominio;\n- Git Inspector;\n- lifecycle delle task;\n- Verification Engine;\n- orchestratore;\n- API di intelligenza artificiale;\n- servizi cloud;\n- commit o push automatici;\n- logging strutturato definitivo;\n- lint e suite di test definitive;\n- convenzioni tecniche di TODO-0003;\n- qualsiasi logica di dominio del prodotto.\n\n---\n\n## Limiti dichiarati\n\n- nessun test automatico Rust unitario dedicato a `get_app_info`;\n- nessun test automatico frontend;\n- nessun lint configurato;\n- nessun commit Git creato;\n- nessun push eseguito;\n- nessuna installazione degli installer generati e poi rimossi;\n- nessuna prova su sistemi operativi diversi dalla macchina Windows utilizzata;\n- stato `DONE` non ancora scritto nella To-Do;\n- verifica indipendente non ancora eseguita al momento del report.\n\n---\n\n## Conclusione dell’esecutore\n\nI criteri funzionali di TODO-0002 sono stati dichiarati soddisfatti. La task è stata proposta per verifica indipendente e TODO-0003 non è stata avviata.\n'
VERIFICATION_REPORT = '# Project Integrity OS\n## Verifica indipendente — TODO-0002\n### Verifica tecnica, documentale e di coerenza\n\n**Data conclusione verifica:** 2026-08-05  \n**Esito:** SUPERATA  \n**Verificatore:** chat amministratore con operatore umano  \n**Modalità:** verifica deterministica tramite output locale fornito dall’utente\n\n---\n\n## 1. Scope della verifica\n\nLa verifica ha controllato:\n\n- struttura del repository;\n- branch e stato Git;\n- documenti correnti;\n- riferimenti operativi;\n- implementazione e registrazione di `get_app_info`;\n- configurazione Tauri;\n- dipendenze e script frontend;\n- residui della demo e del plugin opener;\n- assenza degli installer residui;\n- assenza della cartella temporanea dello scaffold;\n- build frontend;\n- formattazione Rust;\n- compilazione Rust;\n- corrispondenza tra report ed evidenze osservate.\n\n---\n\n## 2. Audit strutturale osservato\n\n- repository: `C:/Users/Utente/Desktop/Project Integrity OS`;\n- branch: `main`;\n- repository senza commit al momento dell’audit;\n- file applicativi e documentali presenti;\n- `docs/00-current/` presente e popolata;\n- `get_app_info` invocato da `src/App.tsx`;\n- `get_app_info` implementato in `src-tauri/src/app/mod.rs`;\n- comando registrato in `src-tauri/src/lib.rs`;\n- nessun residuo operativo di `greet`, `plugin-opener`, `tauri_plugin_opener` o `opener:default`;\n- product name: `Project Integrity OS`;\n- version: `0.1.0`;\n- identifier: `com.projectintegrity.os`;\n- window title: `Project Integrity OS`;\n- cartella bundle assente;\n- cartella temporanea dello scaffold assente.\n\n---\n\n## 3. Verifica del codice osservato\n\n### Rust\n\n`AppInfo` è serializzato in camelCase e contiene:\n\n- `appName`;\n- `version`;\n- `coreStatus`;\n- `operatingMode`.\n\n`get_app_info` restituisce:\n\n- `Project Integrity OS`;\n- versione Cargo;\n- `ready`;\n- `deterministic-first`.\n\nIl comando è registrato tramite:\n\n```rust\ntauri::generate_handler![app::get_app_info]\n```\n\n### Frontend\n\nIl frontend:\n\n- usa `invoke<AppInfo>("get_app_info")`;\n- gestisce stato `loading`;\n- gestisce stato `ready`;\n- gestisce stato `error`;\n- mostra i quattro valori restituiti dal core;\n- non contiene logica di dominio osservabile.\n\n### Capability\n\n`src-tauri/capabilities/default.json` è JSON valido e contiene soltanto `core:default`.\n\n---\n\n## 4. Controlli ripetibili osservati\n\n### Frontend\n\n```text\nnpm run build\n```\n\nEsito:\n\n- TypeScript completato;\n- Vite build completata;\n- codice `0`.\n\n### Rust formatting\n\nIl primo tentativo da Git Bash non ha trovato Cargo nel `PATH`. Non era un errore del progetto: `cargo.exe` era presente in `C:\\Users\\Utente\\.cargo\\bin`.\n\nDopo l’aggiunta temporanea di `$HOME/.cargo/bin` al `PATH` della sessione:\n\n```text\ncargo fmt --manifest-path ".../src-tauri/Cargo.toml" -- --check\n```\n\nEsito: codice `0`.\n\n### Rust compilation\n\n```text\ncargo check --manifest-path ".../src-tauri/Cargo.toml"\n```\n\nEsito:\n\n- `Finished dev profile`;\n- codice `0`.\n\n---\n\n## 5. Collaudo umano\n\nL’utente ha confermato di aver visto personalmente la finestra dell’applicazione con:\n\n- Application: `Project Integrity OS`;\n- Version: `0.1.0`;\n- Core status: `ready`;\n- Operating mode: `deterministic-first`.\n\nIl collaudo visuale è classificato come conferma manuale dell’utente.\n\n---\n\n## 6. Finding documentali\n\n### Risolto nella chiusura\n\nLa To-Do v0.4 indicava il nome non versionato del brief. La chiusura crea una nuova To-Do v0.5 e registra sia il brief effettivamente utilizzato sia la versione finale archiviata.\n\n### Storico preservato\n\nLa To-Do v0.4 non viene riscritta retroattivamente. Viene conservata come versione storica.\n\n---\n\n## 7. Deviazione procedurale\n\nÈ stata registrata la deviazione:\n\n```text\nDEV-TODO-0002-001\n```\n\nMotivo: esecuzione di `npm run tauri build` nonostante il brief vietasse la costruzione degli installer durante TODO-0002.\n\nStato finale osservato:\n\n- installer rimossi;\n- cartella bundle assente;\n- nessun impatto tecnico residuo osservato.\n\nLa deviazione è stata accettata dall’utente senza task correttiva.\n\n---\n\n## 8. Git\n\nAl momento della verifica:\n\n- repository inizializzato;\n- branch `main`;\n- nessun commit;\n- nessun push;\n- output di build esclusi tramite `.gitignore`.\n\nL’utente ha autorizzato la creazione del primo commit baseline e ha negato l’autorizzazione al push.\n\n---\n\n## 9. Conclusione\n\nTODO-0002 soddisfa i criteri tecnici e funzionali osservabili:\n\n- applicazione Tauri avviabile;\n- finestra desktop funzionante;\n- React + TypeScript + Vite presenti;\n- core Rust valido;\n- comunicazione frontend–Rust confermata;\n- caricamento ed errore gestiti;\n- nessuna logica di dominio introdotta;\n- verifica ripetibile frontend e Rust superata;\n- deviazione procedurale registrata e accettata.\n\n**Decisione:** VERIFICA INDIPENDENTE SUPERATA.  \n**Transizione autorizzata:** `HUMAN_APPROVAL` → `DONE`, subordinata alla normalizzazione documentale e alla creazione del commit baseline senza push.\n'
APPROVAL_REPORT = '# Project Integrity OS\n## Approvazione umana — TODO-0002\n\n**Data:** 2026-08-05 02:15 Europe/Rome  \n**Stato:** APPROVATA  \n**Task:** TODO-0002  \n**Push autorizzato:** NO\n\n---\n\n## Dichiarazione dell’utente\n\n> APPROVO TODO-0002.  \n> Confermo di aver visto personalmente la finestra di Project Integrity OS con Application, Version, Core status e Operating mode corretti.  \n> Accetto la deviazione DEV-TODO-0002-001 relativa alla costruzione temporanea degli installer.  \n> Autorizzo la chiusura documentale di TODO-0002 e la creazione del primo commit baseline.  \n> Non autorizzo alcun push.\n\n---\n\n## Effetti autorizzati\n\n- registrazione della verifica indipendente;\n- registrazione della deviazione;\n- creazione della nuova To-Do corrente con TODO-0002 `DONE`;\n- archiviazione delle versioni precedenti;\n- creazione del primo commit baseline locale.\n\n## Azioni non autorizzate\n\n- push verso qualsiasi remoto;\n- avvio di TODO-0003;\n- modifiche funzionali ulteriori.\n'
DEVIATION_REPORT = '# Project Integrity OS\n## Deviazione DEV-TODO-0002-001\n\n**Task:** TODO-0002  \n**Stato:** ACCETTATA  \n**Decisione:** nessuna task correttiva richiesta  \n**Approvazione:** utente, 2026-08-05 02:15 Europe/Rome\n\n---\n\n## Regola prevista\n\nIl brief di TODO-0002 stabiliva di non costruire installer MSI/NSIS.\n\n## Evento osservato\n\nÈ stato eseguito:\n\n```text\nnpm run tauri build\n```\n\nIl comando ha generato temporaneamente l’eseguibile release e gli installer configurati da Tauri.\n\n## Ripristino\n\nGli installer sono stati rimossi prima della chiusura della task.\n\n## Evidenza finale\n\nL’audit indipendente ha osservato:\n\n```text\nOK: cartella bundle non presente\n```\n\n## Impatto\n\n- nessun installer residuo;\n- nessuna funzione fuori scope introdotta;\n- nessun impatto tecnico residuo osservato;\n- deviazione procedurale conservata nello storico.\n\n## Decisione umana\n\nLa deviazione è accettata senza apertura di una task correttiva.\n'


def write_new(path: Path, content: str) -> None:
    if path.exists():
        raise RuntimeError(f"Destinazione già esistente: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(
            f"Pattern {label} atteso una volta, trovato {count} volte: {old!r}"
        )
    return text.replace(old, new, 1)


def main() -> None:
    if not BASE.is_dir():
        print(f"ERRORE: cartella progetto non trovata: {BASE}")
        print("Nessun file è stato modificato.")
        return

    current = BASE / "docs" / "00-current"
    execution = BASE / "docs" / "10-executions" / "TODO-0002"
    history = BASE / "docs" / "20-history"

    todo_v4 = current / "Project_Integrity_OS_TODO_MVP_v0_4.md"
    todo_v5 = current / "Project_Integrity_OS_TODO_MVP_v0_5.md"
    brief_v2 = current / "Project_Integrity_OS_Brief_TODO-0002_v0_2_ACTIVE.md"
    brief_v2_history = (
        execution / "superseded" /
        "Project_Integrity_OS_Brief_TODO-0002_v0_2_ACTIVE.md"
    )
    brief_v3 = (
        execution / "instructions" /
        "Project_Integrity_OS_Brief_TODO-0002_v0_3_FINAL.md"
    )
    registry_v1 = current / "Project_Integrity_OS_Document_Registry_v0_1.md"
    registry_v2 = current / "Project_Integrity_OS_Document_Registry_v0_2.md"

    required = [todo_v4, brief_v2, registry_v1]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("ERRORE: mancano file obbligatori:")
        for path in missing:
            print(f"- {path}")
        print("Nessun file è stato modificato.")
        return

    destinations = [
        todo_v5,
        brief_v2_history,
        brief_v3,
        registry_v2,
        execution / "reports" /
        "Project_Integrity_OS_Report_Esecutivo_TODO-0002_v0_1.md",
        execution / "reports" /
        "Project_Integrity_OS_Verifica_Indipendente_TODO-0002_v0_1.md",
        execution / "validation" / "approvals" /
        "Project_Integrity_OS_Approvazione_Umana_TODO-0002_v0_1.md",
        execution / "validation" / "exceptions" /
        "Project_Integrity_OS_Deviazione_DEV-TODO-0002-001_v0_1.md",
        history / "todo" / todo_v4.name,
        history / "registry" / registry_v1.name,
    ]
    conflicts = [str(path) for path in destinations if path.exists()]
    if conflicts:
        print("ERRORE: una o più destinazioni esistono già:")
        for path in conflicts:
            print(f"- {path}")
        print("Nessun file è stato modificato.")
        return

    todo_text = todo_v4.read_text(encoding="utf-8")
    brief_text = brief_v2.read_text(encoding="utf-8")
    registry_text = registry_v1.read_text(encoding="utf-8")

    # Crea la To-Do v0.5 senza riscrivere retroattivamente la v0.4.
    todo_new = replace_once(
        todo_text,
        "## To-Do del primo MVP — v0.4",
        "## To-Do del primo MVP — v0.5",
        "versione To-Do",
    )
    todo_new = replace_once(
        todo_new,
        "**Stato corrente:** TODO-0001 completata; TODO-0002 in esecuzione tramite modalità `BROWSER_OPERATOR_ASSISTED`.",
        "**Stato corrente:** TODO-0001 e TODO-0002 completate; TODO-0003 è la prossima task ma non è stata avviata.",
        "stato corrente",
    )

    start = todo_new.index(
        "## TODO-0002 — Creare struttura iniziale del repository Project Integrity OS"
    )
    end = todo_new.index("## TODO-0003 — Definire convenzioni tecniche e qualità")
    section = todo_new[start:end]

    section = replace_once(
        section,
        "**Stato:** IN_PROGRESS",
        "**Stato:** DONE",
        "stato TODO-0002",
    )
    section = replace_once(
        section,
        "**Brief esecutivo:** `Project_Integrity_OS_Brief_TODO-0002.md`",
        "**Brief utilizzato:** `Project_Integrity_OS_Brief_TODO-0002_v0_2_ACTIVE.md`  \n"
        "**Brief finale archiviato:** `Project_Integrity_OS_Brief_TODO-0002_v0_3_FINAL.md`",
        "riferimento brief",
    )
    section = replace_once(
        section,
        "**Modalità corrente:** `BROWSER_OPERATOR_ASSISTED`",
        "**Modalità utilizzata:** `BROWSER_OPERATOR_ASSISTED`",
        "modalità",
    )
    section = replace_once(
        section,
        "**Prompt corrente:** `Project_Integrity_OS_Prompt_Esecutivo_Browser_TODO-0002.md`",
        "**Prompt utilizzato:** `Project_Integrity_OS_Prompt_Esecutivo_Browser_TODO-0002.md`  \n"
        f"**Chiusura:** {CLOSED_AT}  \n"
        "**Verifica indipendente:** SUPERATA  \n"
        "**Approvazione umana:** APPROVATA  \n"
        "**Deviazione accettata:** `DEV-TODO-0002-001`  \n"
        "**Baseline Git:** autorizzata; commit locale da creare senza push",
        "chiusura TODO-0002",
    )
    todo_new = todo_new[:start] + section + todo_new[end:]

    # Crea il brief finale e conserva la versione realmente usata.
    brief_final = replace_once(
        brief_text,
        "**Versione del brief:** v0.2",
        "**Versione del brief:** v0.3",
        "versione brief",
    )
    brief_final = replace_once(
        brief_final,
        "**Stato:** CORRENTE",
        "**Stato:** FINAL",
        "stato brief",
    )
    brief_final = replace_once(
        brief_final,
        "`Project_Integrity_OS_Brief_TODO-0002_v0_2_ACTIVE.md`",
        "`Project_Integrity_OS_Brief_TODO-0002_v0_3_FINAL.md`",
        "autoriferimento brief",
    )
    brief_final = brief_final.rstrip() + f"""

---

# 13. Chiusura

**Chiusura:** {CLOSED_AT}  
**Verifica indipendente:** SUPERATA  
**Approvazione umana:** APPROVATA  
**Deviazione accettata:** `DEV-TODO-0002-001`  
**Documento di stato successivo:** `Project_Integrity_OS_TODO_MVP_v0_5.md`  
**Push:** non autorizzato

Questo documento è la versione finale archiviata del brief. La versione v0.2 effettivamente utilizzata durante l’esecuzione viene conservata separatamente senza riscrittura retroattiva.
"""

    # Crea il registro v0.2, mantenendo il registro v0.1 nello storico.
    registry_new = replace_once(
        registry_text,
        "## Document Registry — v0.1",
        "## Document Registry — v0.2",
        "versione registro",
    )
    registry_new = replace_once(
        registry_new,
        "| DOC-002 | To-Do | Project_Integrity_OS_TODO_MVP_v0_4.md | v0.4 | ACTIVE | Sì | Project_Integrity_OS_TODO_MVP_v0_3.md | Globale | docs/00-current/ | To-Do operativa corrente |",
        "| DOC-002 | To-Do | Project_Integrity_OS_TODO_MVP_v0_4.md | v0.4 | SUPERSEDED | No | Project_Integrity_OS_TODO_MVP_v0_3.md | Globale | docs/20-history/todo/ | Stato durante l’esecuzione di TODO-0002 |",
        "riga DOC-002",
    )
    registry_new = replace_once(
        registry_new,
        "| DOC-004 | Brief | Project_Integrity_OS_Brief_TODO-0002_v0_2_ACTIVE.md | v0.2 | ACTIVE | Sì | Project_Integrity_OS_Brief_TODO-0002_v0_1_SUPERSEDED.md | TODO-0002 | docs/00-current/ | Deve riferirsi alla To-Do v0.4 |",
        "| DOC-004 | Brief | Project_Integrity_OS_Brief_TODO-0002_v0_2_ACTIVE.md | v0.2 | SUPERSEDED | No | Project_Integrity_OS_Brief_TODO-0002_v0_1_SUPERSEDED.md | TODO-0002 | docs/10-executions/TODO-0002/superseded/ | Versione effettivamente utilizzata durante l’esecuzione |",
        "riga DOC-004",
    )
    registry_new = replace_once(
        registry_new,
        "| DOC-005 | Prompt | Project_Integrity_OS_Prompt_Esecutivo_Browser_TODO-0002.md | n.d. | ACTIVE | Sì, per TODO-0002 | Project_Integrity_OS_Prompt_Esecutivo_TODO-0002.md | TODO-0002 | docs/10-executions/TODO-0002/instructions/ | Modalità browser con operatore |",
        "| DOC-005 | Prompt | Project_Integrity_OS_Prompt_Esecutivo_Browser_TODO-0002.md | n.d. | FINAL | Sì, come storico della task | Project_Integrity_OS_Prompt_Esecutivo_TODO-0002.md | TODO-0002 | docs/10-executions/TODO-0002/instructions/ | Prompt realmente utilizzato |",
        "riga DOC-005",
    )
    registry_new = replace_once(
        registry_new,
        "| DOC-006 | Start Here | START_HERE_Browser_Project_Integrity_OS_TODO-0002.md | n.d. | ACTIVE | Sì, per TODO-0002 | START_HERE_Project_Integrity_OS_TODO-0002.md | TODO-0002 | docs/10-executions/TODO-0002/instructions/ | Procedura di avvio browser |",
        "| DOC-006 | Start Here | START_HERE_Browser_Project_Integrity_OS_TODO-0002.md | n.d. | FINAL | Sì, come storico della task | START_HERE_Project_Integrity_OS_TODO-0002.md | TODO-0002 | docs/10-executions/TODO-0002/instructions/ | Procedura realmente utilizzata |",
        "riga DOC-006",
    )

    marker = "| DOC-019 | Concetto | sistema_integrita_continuita_progetto_v0_6.md | v0.6 | SUPERSEDED | No | v0.5 | Globale | docs/20-history/concept/ | Ultima versione concettuale prima dei flussi operativi |"
    additions = """| DOC-020 | To-Do | Project_Integrity_OS_TODO_MVP_v0_5.md | v0.5 | ACTIVE | Sì | Project_Integrity_OS_TODO_MVP_v0_4.md | Globale | docs/00-current/ | TODO-0002 chiusa; TODO-0003 non avviata |
| DOC-021 | Brief | Project_Integrity_OS_Brief_TODO-0002_v0_3_FINAL.md | v0.3 | FINAL | Sì, come fonte finale della task | Project_Integrity_OS_Brief_TODO-0002_v0_2_ACTIVE.md | TODO-0002 | docs/10-executions/TODO-0002/instructions/ | Brief finale di chiusura |
| DOC-022 | Report | Project_Integrity_OS_Report_Esecutivo_TODO-0002_v0_1.md | v0.1 | FINAL | Sì, come dichiarazione dell’esecutore | — | TODO-0002 | docs/10-executions/TODO-0002/reports/ | Report della chat esecutiva |
| DOC-023 | Verifica | Project_Integrity_OS_Verifica_Indipendente_TODO-0002_v0_1.md | v0.1 | FINAL | Sì | — | TODO-0002 | docs/10-executions/TODO-0002/reports/ | Verifica amministratore e controlli ripetibili |
| DOC-024 | Approvazione | Project_Integrity_OS_Approvazione_Umana_TODO-0002_v0_1.md | v0.1 | FINAL | Sì | — | TODO-0002 | docs/10-executions/TODO-0002/validation/approvals/ | Approvazione e autorizzazione commit |
| DOC-025 | Deviazione | Project_Integrity_OS_Deviazione_DEV-TODO-0002-001_v0_1.md | v0.1 | ACCEPTED | Sì | — | TODO-0002 | docs/10-executions/TODO-0002/validation/exceptions/ | Build installer temporanea, poi rimossa |"""
    registry_new = replace_once(
        registry_new,
        marker,
        marker + "\n" + additions,
        "aggiunta documenti di chiusura",
    )

    # Scrive prima i nuovi documenti; gli spostamenti avvengono solo dopo.
    write_new(todo_v5, todo_new)
    write_new(brief_v3, brief_final)
    write_new(registry_v2, registry_new)
    write_new(
        execution / "reports" /
        "Project_Integrity_OS_Report_Esecutivo_TODO-0002_v0_1.md",
        EXECUTOR_REPORT,
    )
    write_new(
        execution / "reports" /
        "Project_Integrity_OS_Verifica_Indipendente_TODO-0002_v0_1.md",
        VERIFICATION_REPORT,
    )
    write_new(
        execution / "validation" / "approvals" /
        "Project_Integrity_OS_Approvazione_Umana_TODO-0002_v0_1.md",
        APPROVAL_REPORT,
    )
    write_new(
        execution / "validation" / "exceptions" /
        "Project_Integrity_OS_Deviazione_DEV-TODO-0002-001_v0_1.md",
        DEVIATION_REPORT,
    )

    # Archivia i documenti sostituiti.
    brief_v2_history.parent.mkdir(parents=True, exist_ok=True)
    (history / "todo").mkdir(parents=True, exist_ok=True)
    (history / "registry").mkdir(parents=True, exist_ok=True)

    shutil.move(str(brief_v2), str(brief_v2_history))
    shutil.move(str(todo_v4), str(history / "todo" / todo_v4.name))
    shutil.move(str(registry_v1), str(history / "registry" / registry_v1.name))

    print("CHIUSURA DOCUMENTALE TODO-0002: COMPLETATA")
    print()
    print("Creati:")
    for path in [
        todo_v5,
        brief_v3,
        registry_v2,
        execution / "reports" /
        "Project_Integrity_OS_Report_Esecutivo_TODO-0002_v0_1.md",
        execution / "reports" /
        "Project_Integrity_OS_Verifica_Indipendente_TODO-0002_v0_1.md",
        execution / "validation" / "approvals" /
        "Project_Integrity_OS_Approvazione_Umana_TODO-0002_v0_1.md",
        execution / "validation" / "exceptions" /
        "Project_Integrity_OS_Deviazione_DEV-TODO-0002-001_v0_1.md",
    ]:
        print(f"- {path.relative_to(BASE)}")

    print()
    print("Archiviati:")
    for path in [
        brief_v2_history,
        history / "todo" / todo_v4.name,
        history / "registry" / registry_v1.name,
    ]:
        print(f"- {path.relative_to(BASE)}")

    print()
    print("Nessun commit e nessun push sono stati eseguiti dallo script.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"ERRORE: {error}")
        print("Controllare lo stato dei file prima di ripetere lo script.")
