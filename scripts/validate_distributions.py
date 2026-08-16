#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, re, tempfile, zipfile
from build_distributions import ROOT, KNOWLEDGE, extract_instruction

def sha(b): return hashlib.sha256(b).hexdigest()
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--version'); ap.add_argument('--input-dir',default='dist'); args=ap.parse_args()
    version=args.version or (ROOT/'VERSION').read_text(encoding='utf-8').strip()
    inp=Path(args.input_dir); inp=inp if inp.is_absolute() else ROOT/inp
    paths=[inp/f'arduino-projektassistent-custom-gpt-v{version}.zip', inp/f'arduino-projektassistent-chat-v{version}.zip']
    for p in paths:
        if not p.is_file(): raise SystemExit(f'Saknad distribution: {p}')
        with zipfile.ZipFile(p) as z: bad=z.testzip();
        if bad: raise SystemExit(f'Korrupt ZIP {p}: {bad}')
    instr=extract_instruction().encode('utf-8')
    with zipfile.ZipFile(paths[0]) as z:
        if z.read('VERSION').decode().strip()!=version: raise SystemExit('Fel VERSION i Custom GPT')
        if z.read('gpt-configuration/instructions.txt')!=instr: raise SystemExit('Custom GPT instruction avviker från Builder-instruktionen')
        for f in KNOWLEDGE:
            if z.read('knowledge-upload/'+f)!=(ROOT/'knowledge'/f).read_bytes(): raise SystemExit(f'Custom Knowledge avviker: {f}')
    with zipfile.ZipFile(paths[1]) as z:
        if z.read('VERSION').decode().strip()!=version: raise SystemExit('Fel VERSION i Chat')
        if z.read('assistant/instructions.txt')!=instr: raise SystemExit('Portable instruction avviker från Builder-instruktionen')
        for f in KNOWLEDGE:
            if z.read('knowledge/'+f)!=(ROOT/'knowledge'/f).read_bytes(): raise SystemExit(f'Portable Knowledge avviker: {f}')
        manifest=json.loads(z.read('MANIFEST.json'))
        if manifest.get('version')!=version: raise SystemExit('Fel manifestversion')
        for item in manifest['files']:
            if sha(z.read(item['path']))!=item['sha256']: raise SystemExit('Manifesthash avviker: '+item['path'])
    print(f'OK: båda distributionerna för {version} verifierade; {len(KNOWLEDGE)} Knowledge-filer är byte-identiska.')
if __name__=='__main__': main()
