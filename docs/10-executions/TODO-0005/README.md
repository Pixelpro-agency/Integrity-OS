# TODO-0005 — Applicazione del riallineamento della To-Do

## Scopo

Questo pacchetto crea la To-Do corrente `v0.10`, conserva la `v0.9` come versione storica e aggiorna `docs/README.md`.

## Operazioni

- [ ] Creare una copia di sicurezza della cartella `docs`.
- [ ] Estrarre lo ZIP nella root del progetto.
- [ ] Verificare la presenza di `docs/00-current/Project_Integrity_OS_TODO_MVP_v0_10.md`.
- [ ] Verificare la copia storica in `docs/10-executions/TODO-0005/90-history/`.
- [ ] Eseguire `bash docs/10-executions/TODO-0005/APPLY_TODO-0005_GITBASH.sh`.
- [ ] Controllare che la v0.9 non sia più dentro `docs/00-current/`.
- [ ] Controllare i collegamenti presenti nella v0.10.
- [ ] Non eseguire commit o push come parte di questo pacchetto.

## Risultato atteso

`docs/00-current/` contiene una sola To-Do corrente: `Project_Integrity_OS_TODO_MVP_v0_10.md`.

## Modifiche principali della v0.10

- percorsi reali per gli archivi TODO-0002 e TODO-0003;
- rimozione del riferimento al modello preliminare non più presente;
- registrazione di TODO-0004 come completata;
- sezione TODO-0101 ridotta a stato, riferimenti, deliverable, prossima azione e condizioni per `READY`;
- nessuna duplicazione delle decisioni architetturali.
