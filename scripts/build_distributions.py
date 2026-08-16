#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, re, shutil, zipfile

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = [
    '00-knowledge-index.md','01-roll-och-avgransning.md','02-malgrupper-och-nivaniva.md',
    '03-fragemodell.md','04-leveransmallar.md','05-mikrokontroller-guide.md',
    '06-komponentkatalog-mvp.md','07-kopplingsregler-och-sakerhet.md','08-kodstandard-arduino.md',
    '09-ritnings-och-kopplingsstandard.md','10-dokumentationsstandard.md','11-inkops-och-prisbedomning.md',
    '12-gpt-huvudinstruktion.md','13-knowledge-filstruktur.md','14-circuit-yaml-svg-generator.md'
]
SEMVER = re.compile(r'^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$')

def extract_instruction() -> str:
    p = ROOT/'gpt-instructions/12-gpt-huvudinstruktion.md'
    text = p.read_text(encoding='utf-8')
    marker = '## Färdig huvudinstruktion för GPT Builder'
    pos = text.find(marker)
    if pos < 0: raise RuntimeError('Hittar inte färdig GPT Builder-instruktion')
    tail = text[pos+len(marker):]
    m = re.search(r'```text\s*\n(.*?)\n```', tail, re.S)
    if not m: raise RuntimeError('Hittar inte textblocket med färdig instruktion')
    return m.group(1).rstrip() + '\n'

def sha256(p):
    h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()

def zip_dir(src, dest):
    # Deterministic ZIP
    with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(x for x in src.rglob('*') if x.is_file()):
            rel=p.relative_to(src).as_posix()
            info=zipfile.ZipInfo(rel, date_time=(2020,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644 << 16
            z.writestr(info,p.read_bytes())

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--version'); ap.add_argument('--output-dir', default='dist')
    args=ap.parse_args()
    version=args.version or (ROOT/'VERSION').read_text(encoding='utf-8').strip()
    if not SEMVER.match(version): raise SystemExit(f'Ogiltig version: {version}')
    for f in KNOWLEDGE:
        if not (ROOT/'knowledge'/f).is_file(): raise SystemExit(f'Saknad Knowledge-fil: {f}')
    extra=sorted(p.name for p in (ROOT/'knowledge').glob('*.md') if p.name not in KNOWLEDGE)
    if extra: raise SystemExit(f'Oväntade Knowledge-filer: {extra}')
    out=Path(args.output_dir); out = out if out.is_absolute() else ROOT/out
    shutil.rmtree(out,ignore_errors=True); out.mkdir(parents=True)
    stage=ROOT/'.build-distributions'; shutil.rmtree(stage,ignore_errors=True); stage.mkdir()
    instruction=extract_instruction()

    # Custom GPT distribution: clean installation package representing current Builder config.
    custom=stage/'custom-gpt'; (custom/'gpt-configuration').mkdir(parents=True); (custom/'knowledge-upload').mkdir()
    (custom/'VERSION').write_text(version+'\n',encoding='utf-8')
    (custom/'gpt-configuration/instructions.txt').write_text(instruction,encoding='utf-8')
    (custom/'gpt-configuration/README.md').write_text(
        '# GPT Builder-konfiguration\n\nKlistra in `instructions.txt` i GPT Builder Instructions. Projektet har ännu inga fastställda conversation starters. Ladda upp samtliga filer i `knowledge-upload/` som Knowledge.\n', encoding='utf-8')
    for f in KNOWLEDGE: shutil.copy2(ROOT/'knowledge'/f, custom/'knowledge-upload'/f)
    shutil.copy2(ROOT/'gpt-builder/02-uppladdningslista-knowledge.md', custom/'knowledge-upload-list.md')

    # Portable Chat distribution.
    chat=stage/'chat'; (chat/'assistant').mkdir(parents=True); (chat/'knowledge').mkdir()
    shutil.copy2(ROOT/'portable/START-HERE.md', chat/'START-HERE.md')
    (chat/'VERSION').write_text(version+'\n',encoding='utf-8')
    (chat/'assistant/instructions.txt').write_text(instruction,encoding='utf-8')
    for f in KNOWLEDGE: shutil.copy2(ROOT/'knowledge'/f, chat/'knowledge'/f)
    files=[]
    for p in sorted(x for x in chat.rglob('*') if x.is_file() and x.name!='MANIFEST.json'):
        files.append({'path':p.relative_to(chat).as_posix(),'sha256':sha256(p)})
    manifest={'package':'arduino-projektassistenten','format':'portable-chat-assistant','version':version,
              'entrypoint':'START-HERE.md','instructions':'assistant/instructions.txt','knowledge':[f'knowledge/{f}' for f in KNOWLEDGE], 'files':files}
    (chat/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

    zip_dir(custom,out/f'arduino-projektassistent-custom-gpt-v{version}.zip')
    zip_dir(chat,out/f'arduino-projektassistent-chat-v{version}.zip')
    shutil.rmtree(stage)
    print(f'Byggde distributioner för {version} i {out}')
if __name__=='__main__': main()
