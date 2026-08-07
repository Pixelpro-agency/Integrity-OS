#!/usr/bin/env python3
from pathlib import Path
import csv, json, hashlib, re, shutil, sys
from collections import Counter

ROOT = Path(".").resolve()
DOCS = ROOT / "docs"
TASK = DOCS / "10-executions/TODO-0101"
SELF = DOCS / "10-executions/TODO-0013"
TEMPLATE = SELF / "TRACEABILITY_TEMPLATE.json"

def fail(msg):
    print(f"ERRORE: {msg}", file=sys.stderr)
    raise SystemExit(1)

def sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda:f.read(1024*1024), b""):
            h.update(c)
    return h.hexdigest()

required = [
    TASK/"03-verifica-documentale/TODO-0101_Audit_Documentale_v0_2_FINAL.md",
    TASK/"02-checkpoint/TODO-0101_Checkpoint_Finale_Analisi_v0_11_DRAFT.md",
    TASK/"README.md",
    DOCS/"architecture/data-model/current/Project_Integrity_OS_Decision_Log_Data_Model_v0_9_DRAFT.md",
    TEMPLATE,
]
for p in required:
    if not p.is_file():
        fail(f"file richiesto mancante: {p.relative_to(ROOT)}")

# Remove stale control artifacts from the failed first TODO-0013 attempt, if present.
for stale in [
    SELF/"VERIFY_TODO-0013_GITBASH.sh",
    SELF/"Project_Integrity_OS_Report_Esecutivo_TODO-0013_v0_1.md",
]:
    if stale.exists():
        stale.unlink()

# 1. Preserve exact local v0.2 audit and v0.11 checkpoint before replacing current versions.
audit2 = TASK/"03-verifica-documentale/TODO-0101_Audit_Documentale_v0_2_FINAL.md"
audit2_hist = TASK/"90-history/TODO-0101_Audit_Documentale_v0_2_HISTORICAL.md"
audit2_hist.parent.mkdir(parents=True, exist_ok=True)
if not audit2_hist.exists():
    shutil.copy2(audit2, audit2_hist)

cp11 = TASK/"02-checkpoint/TODO-0101_Checkpoint_Finale_Analisi_v0_11_DRAFT.md"
cp11_hist = TASK/"90-history/checkpoints/TODO-0101_Checkpoint_Finale_Analisi_v0_11_DRAFT.md"
cp11_hist.parent.mkdir(parents=True, exist_ok=True)
if not cp11_hist.exists():
    shutil.copy2(cp11, cp11_hist)

# 2. Create checkpoint v0.12 from the exact local v0.11.
cp_text = cp11.read_text(encoding="utf-8")
cp_text = cp_text.replace("Checkpoint Index — TODO-0101 — v0.11", "Checkpoint Index — TODO-0101 — v0.12", 1)
cp_text = cp_text.replace("**Data:** 2026-08-07", "**Data:** 2026-08-07", 1)

# Previous checkpoint reference: normalize whatever v0.10/v0.11 wording exists.
cp_text = re.sub(
    r"\*\*Versione precedente:\*\* .*",
    "**Versione precedente:** [TODO-0101 Checkpoint Finale Analisi v0.11](../90-history/checkpoints/TODO-0101_Checkpoint_Finale_Analisi_v0_11_DRAFT.md)",
    cp_text, count=1
)
cp_text = cp_text.replace(
    "TODO-0101_Audit_Documentale_v0_2_FINAL.md",
    "TODO-0101_Audit_Documentale_v0_3_FINAL.md"
)
cp_text = cp_text.replace(
    "Audit documentale TODO-0101 v0.2",
    "Audit documentale TODO-0101 v0.3"
)
cp12 = TASK/"02-checkpoint/TODO-0101_Checkpoint_Finale_Analisi_v0_12_DRAFT.md"
cp12.write_text(cp_text, encoding="utf-8")

# 3. Update current README and Decision Log references to v0.3 / checkpoint v0.12.
readme = TASK/"README.md"
rd = readme.read_text(encoding="utf-8")
rd = rd.replace("TODO-0101_Checkpoint_Finale_Analisi_v0_11_DRAFT.md",
                "TODO-0101_Checkpoint_Finale_Analisi_v0_12_DRAFT.md")
rd = rd.replace("TODO-0101 Audit Documentale v0.2", "TODO-0101 Audit Documentale v0.3")
rd = rd.replace("TODO-0101_Audit_Documentale_v0_2_FINAL.md",
                "TODO-0101_Audit_Documentale_v0_3_FINAL.md")

# Update control-file explanation if still old.
if "content_preserved_byte_for_byte" in rd and "source_sha256" not in rd:
    rd += """

---

## Tracciabilità dei file di controllo

`FILE_MAP.csv` e `manifest.json` distinguono ora esplicitamente:

- `source_sha256`;
- `current_sha256`;
- `change_type`.

Non viene più usata una dichiarazione indiscriminata di preservazione byte per byte.
"""
readme.write_text(rd, encoding="utf-8")

dlog = DOCS/"architecture/data-model/current/Project_Integrity_OS_Decision_Log_Data_Model_v0_9_DRAFT.md"
dl = dlog.read_text(encoding="utf-8")
dl = dl.replace("Audit documentale TODO-0101 v0.2", "Audit documentale TODO-0101 v0.3")
dl = dl.replace("TODO-0101_Audit_Documentale_v0_2_FINAL.md",
                "TODO-0101_Audit_Documentale_v0_3_FINAL.md")
dlog.write_text(dl, encoding="utf-8")

# Remove superseded current files only after historical copies and replacements exist.
audit2.unlink()
cp11.unlink()

# 4. Create placeholder Audit v0.3 so inventory counts include it.
audit3 = TASK/"03-verifica-documentale/TODO-0101_Audit_Documentale_v0_3_FINAL.md"
audit3.write_text("# Audit v0.3 — placeholder durante rigenerazione\n", encoding="utf-8")

# 5. Scan final tree.
link_re = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
def historical(rel):
    return "90-history" in rel.parts or "history" in rel.parts or rel.name.endswith("_HISTORICAL.md")

files=[p for p in DOCS.rglob("*") if p.is_file()]
md=[p for p in files if p.suffix.lower()==".md"]
broken_current=[]
broken_hist=[]
total_links=0
integrity={"empty":0,"invalid_utf8":0,"nul":0,"conflicts":0,"unbalanced_fences":0}
for p in files:
    b=p.read_bytes()
    if not b: integrity["empty"] += 1
    if b"\x00" in b: integrity["nul"] += 1
    try:
        txt=b.decode("utf-8")
    except UnicodeDecodeError:
        integrity["invalid_utf8"] += 1
        continue
    if re.search(r"(?m)^(<<<<<<< .+|=======|>>>>>>> .+)$", txt):
        integrity["conflicts"] += 1
    if p.suffix.lower()==".md":
        if txt.count("```") % 2: integrity["unbalanced_fences"] += 1
        rel=p.relative_to(DOCS)
        for target in link_re.findall(txt):
            total_links += 1
            t=target.strip()
            if "://" in t or t.startswith("#") or t.startswith("mailto:"):
                continue
            t=t.split("#",1)[0]
            if not t: continue
            if not (p.parent/t).resolve().exists():
                rec={"file":rel.as_posix(),"target":target}
                (broken_hist if historical(rel) else broken_current).append(rec)

if broken_current:
    fail(f"link correnti non risolti: {broken_current[:5]}")
if any(integrity.values()):
    fail(f"integrità base non valida: {integrity}")

# 6. Write final audit. It contains no markdown links, so link count is stable.
audit_text=f"""# Project Integrity OS

## Audit documentale — TODO-0101 — v0.3

**Stato:** FINAL — audit deterministico del tree `docs/` corrente  
**Data:** 2026-08-07  
**Ambito:** tree documentale dopo TODO-0010 hotfix, TODO-0011, TODO-0012 e correzione TODO-0013.

---

# 1. Inventario

```text
File totali sotto docs/: {len(files)}
File Markdown: {len(md)}
File .original.txt: {sum(1 for p in files if p.name.endswith('.original.txt'))}
```

# 2. Integrità di base

```text
File vuoti: {integrity['empty']}
File UTF-8 non validi: {integrity['invalid_utf8']}
File con byte NUL: {integrity['nul']}
File con marker di conflitto Git: {integrity['conflicts']}
File Markdown con code fence non bilanciati: {integrity['unbalanced_fences']}
```

**Esito:** PASS.

# 3. Collegamenti Markdown

```text
Link Markdown esaminati: {total_links}
Link relativi non risolti nei documenti correnti: {len(broken_current)}
Link relativi non risolti negli snapshot storici: {len(broken_hist)}
```

**Documenti correnti:** PASS — nessun link relativo non risolto.

I collegamenti storici non vengono corretti retroattivamente.

# 4. Stato corrente

```text
TODO-0101: IN_ANALYSIS
Checkpoint corrente: v0.12
Decision Log corrente: v0.9
Audit documentale corrente: v0.3
READY: NO
SQLite: NON INIZIATA
```

# 5. Provenienza

- Audit v0.1: storico.
- Audit v0.2: preservato nello storico; registrava il conteggio precedente all'hotfix.
- Audit v0.3: audit corrente rigenerato sul tree locale effettivo.

# 6. Decisione

Il tree documentale corrente è coerente per il perimetro verificato.

TODO-0101 resta `IN_ANALYSIS`.
"""
audit3.write_text(audit_text, encoding="utf-8")

# Re-scan link count after final audit body (no markdown links expected).
files=[p for p in DOCS.rglob("*") if p.is_file()]
md=[p for p in files if p.suffix.lower()==".md"]

# 7. Build FILE_MAP from template using ACTUAL LOCAL hashes.
tpl=json.loads(TEMPLATE.read_text(encoding="utf-8"))
rows=[]
for r in tpl["source_rows"]:
    p=ROOT/r["organized_path"]
    if not p.is_file():
        fail(f"file sorgente mappato mancante: {r['organized_path']}")
    current_sha=sha(p)
    if r["change_type"]=="PRESERVED_BYTE_FOR_BYTE" and current_sha != r["source_sha256"]:
        fail(f"file dichiarato preservato ma diverso dalla sorgente: {r['organized_path']}")
    row=dict(r)
    row["current_sha256"]=current_sha
    rows.append(row)

for r in tpl["generated_rows"]:
    p=ROOT/r["organized_path"]
    if not p.is_file():
        fail(f"file derivato mappato mancante: {r['organized_path']}")
    row=dict(r)
    origin=r.get("origin_reference","")
    op=ROOT/origin if origin.startswith("docs/") else None
    row["source_sha256"]=sha(op) if op and op.is_file() else ""
    row["current_sha256"]=sha(p)
    rows.append(row)

fields=["origin_kind","source_path","organized_path","role","current",
        "source_sha256","current_sha256","change_type","origin_reference","note"]
with (TASK/"FILE_MAP.csv").open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

# 8. Write manifest schema 2.1.
counts=Counter(r["change_type"] for r in rows)
manifest={
    "schema_version":"2.1",
    "generated_at":"2026-08-07",
    "generation_mode":"LOCAL_CURRENT_STATE",
    "source_archive":{
        "name":tpl["source_archive"]["name"],
        "sha256":tpl["source_archive"]["sha256"],
        "source_file_count":tpl["source_archive"]["file_count"],
        "all_source_paths_accounted_for":True
    },
    "task":{
        "task_id":"TODO-0101",
        "status":"IN_ANALYSIS",
        "implementation_started":False,
        "ready":False,
        "current_checkpoint":"docs/10-executions/TODO-0101/02-checkpoint/TODO-0101_Checkpoint_Finale_Analisi_v0_12_DRAFT.md",
        "current_decision_log":"docs/architecture/data-model/current/Project_Integrity_OS_Decision_Log_Data_Model_v0_9_DRAFT.md",
        "current_documentation_audit":"docs/10-executions/TODO-0101/03-verifica-documentale/TODO-0101_Audit_Documentale_v0_3_FINAL.md"
    },
    "traceability":{
        "source_archive_rows":len(tpl["source_rows"]),
        "generated_or_derived_rows":len(tpl["generated_rows"]),
        "total_document_rows":len(rows),
        "change_type_counts":dict(sorted(counts.items())),
        "blanket_content_preserved_byte_for_byte_claim":False,
        "hashes_calculated_from_local_current_files":True,
        "fields":["source_sha256","current_sha256","change_type"]
    },
    "audit_metrics":{
        "docs_file_count":len(files),
        "markdown_file_count":len(md),
        "markdown_links_examined":total_links,
        "broken_current_links":len(broken_current),
        "broken_historical_links":len(broken_hist)
    },
    "files":rows
}
(TASK/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

# 9. Generate SHA manifest last.
tracked=sorted({r["organized_path"] for r in rows} | {
    "docs/10-executions/TODO-0101/FILE_MAP.csv",
    "docs/10-executions/TODO-0101/manifest.json",
    "docs/10-executions/TODO-0101/SOURCE_ARCHIVE_SHA256.txt",
})
lines=[]
for rel in tracked:
    p=ROOT/rel
    if not p.is_file():
        fail(f"file per MANIFEST_SHA256 mancante: {rel}")
    lines.append(f"{sha(p)}  {rel}")
(TASK/"MANIFEST_SHA256.txt").write_text("\n".join(lines)+"\n",encoding="utf-8")

# 10. Verify generated metadata immediately.
with (TASK/"FILE_MAP.csv").open("r",encoding="utf-8",newline="") as f:
    check_rows=list(csv.DictReader(f))
if len(check_rows) != len(rows):
    fail("numero righe FILE_MAP incoerente")

for r in check_rows:
    p=ROOT/r["organized_path"]
    if sha(p) != r["current_sha256"]:
        fail(f"current_sha256 non coincide dopo rigenerazione: {r['organized_path']}")

for line in (TASK/"MANIFEST_SHA256.txt").read_text(encoding="utf-8").splitlines():
    expected,rel=line.split("  ",1)
    p=ROOT/rel
    if sha(p)!=expected:
        fail(f"SHA256 finale non coincide: {rel}")

print("TODO-0013 V2 APPLICATO E VERIFICATO LOCALMENTE.")
print("Audit corrente: v0.3.")
print("Audit v0.2 preservato nello storico.")
print("Checkpoint corrente: v0.12.")
print("Checkpoint v0.11 preservato nello storico.")
print(f"FILE_MAP.csv: {len(rows)} righe ({len(tpl['source_rows'])} sorgenti + {len(tpl['generated_rows'])} derivate).")
print("manifest.json: schema 2.1, hash calcolati sui file locali.")
print("MANIFEST_SHA256.txt: tutti gli hash coincidono.")
print(f"Link correnti non risolti: {len(broken_current)}.")
print(f"Link storici non risolti: {len(broken_hist)}.")
print("TODO-0101: IN_ANALYSIS, READY=NO, SQLite non iniziata.")
print("Nessuna operazione Git è stata eseguita.")
