#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, re, tempfile, zipfile, yaml
from build_distributions import ROOT, KNOWLEDGE, extract_instruction

def sha(b): return hashlib.sha256(b).hexdigest()
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--version'); ap.add_argument('--input-dir',default='dist'); args=ap.parse_args()
    version=args.version or (ROOT/'VERSION').read_text(encoding='utf-8').strip()
    inp=Path(args.input_dir); inp=inp if inp.is_absolute() else ROOT/inp
    registry=yaml.safe_load((ROOT/'runtime-distribution-registry.yaml').read_text(encoding='utf-8'))
    active=list(registry.get('active_targets',[]) or [])
    expected={registry['targets'][name]['artifact_pattern'].format(version=version) for name in active}
    actual={p.name for p in inp.glob('*.zip')}
    if actual!=expected:
        raise SystemExit(f'Distribution set mismatch. expected={sorted(expected)} actual={sorted(actual)}')
    paths=[inp/name for name in sorted(expected)]
    for p in paths:
        if not p.is_file(): raise SystemExit(f'Saknad distribution: {p}')
        with zipfile.ZipFile(p) as z: bad=z.testzip();
        if bad: raise SystemExit(f'Korrupt ZIP {p}: {bad}')
    instr=(ROOT/'assistant/instructions.md').read_bytes()
    custom=inp/f'arduino-projektassistent-custom-gpt-v{version}.zip'
    chat=inp/f'arduino-projektassistent-chat-v{version}.zip'
    if 'custom-gpt' in active:
      with zipfile.ZipFile(custom) as z:
          if z.read('VERSION').decode().strip()!=version: raise SystemExit('Fel VERSION i Custom GPT')
          if z.read('gpt-configuration/instructions.txt')!=instr: raise SystemExit('Custom GPT instruction avviker från canonical instruktion')
          custom_instr=z.read('gpt-configuration/instructions.txt').decode('utf-8')
          for marker in [
              'Skapa alltid kopplingstabell innan eller tillsammans med kod.',
              'Koppla inte 5 V-signaler direkt till 3,3 V-ingångar om det inte är verifierat säkert.',
              'Rekommendera aldrig att motorer, reläer, elektromagneter, solenoider, högtalare eller andra externa laster drivs direkt från en GPIO-pin.',
              'Hjälp inte användaren att bygga projekt med nätspänning/230 V som vanlig hobbykoppling.',
              'skapa `circuit.yaml` enligt Circuit SVG Generator v1.1',
          ]:
              if marker not in custom_instr: raise SystemExit('Custom GPT saknar kritisk beteendemarkör: '+marker)
          for f in KNOWLEDGE:
              if z.read('knowledge-upload/'+f)!=(ROOT/'knowledge'/f).read_bytes(): raise SystemExit(f'Custom Knowledge avviker: {f}')
    if 'chat' in active:
      with zipfile.ZipFile(chat) as z:
          if z.read('VERSION').decode().strip()!=version: raise SystemExit('Fel VERSION i Chat')
          if z.read('assistant/instructions.txt')!=instr: raise SystemExit('Portable instruction avviker från canonical instruktion')
          chat_instr=z.read('assistant/instructions.txt').decode('utf-8')
          for marker in [
              'Skapa alltid kopplingstabell innan eller tillsammans med kod.',
              'Koppla inte 5 V-signaler direkt till 3,3 V-ingångar om det inte är verifierat säkert.',
              'Rekommendera aldrig att motorer, reläer, elektromagneter, solenoider, högtalare eller andra externa laster drivs direkt från en GPIO-pin.',
              'Hjälp inte användaren att bygga projekt med nätspänning/230 V som vanlig hobbykoppling.',
              'skapa `circuit.yaml` enligt Circuit SVG Generator v1.1',
          ]:
              if marker not in chat_instr: raise SystemExit('Chat saknar kritisk beteendemarkör: '+marker)
          for f in KNOWLEDGE:
              if z.read('knowledge/'+f)!=(ROOT/'knowledge'/f).read_bytes(): raise SystemExit(f'Portable Knowledge avviker: {f}')
          manifest=json.loads(z.read('MANIFEST.json'))
          if manifest.get('version')!=version: raise SystemExit('Fel manifestversion')
          for item in manifest['files']:
              if sha(z.read(item['path']))!=item['sha256']: raise SystemExit('Manifesthash avviker: '+item['path'])
    print(f'OK: båda distributionerna för {version} verifierade; {len(KNOWLEDGE)} Knowledge-filer är byte-identiska.')
if __name__=='__main__': main()
