# TODO-0011 — Documentare i link storici non risolvibili

## Scopo

Applica `DOC-FIX-009`.

## Modifica

Nel file:

`docs/10-executions/TODO-0101/README.md`

viene aggiunta la nota:

> I collegamenti presenti nei documenti sotto `90-history` riflettono la struttura storica originaria e possono non essere risolvibili nel tree corrente.

La nota chiarisce che gli snapshot storici non vengono riscritti retroattivamente.

## Verifica

Sul tree simulato dopo TODO-0010 + questa modifica:

```text
Link Markdown esaminati: 167
Link relativi non risolti nei documenti correnti: 0
Link relativi non risolti nei documenti storici: 124
```

I collegamenti storici possono restare non risolti per preservare l'autenticità degli snapshot.

## Applicazione

Estrarre lo ZIP nella root del progetto e consentire la sovrascrittura del README TODO-0101, quindi:

```bash
bash docs/10-executions/TODO-0011/VERIFY_TODO-0011_GITBASH.sh
```

Lo script non modifica Git.
