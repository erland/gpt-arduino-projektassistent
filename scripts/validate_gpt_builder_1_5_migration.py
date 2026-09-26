#!/usr/bin/env python3
from pathlib import Path
import re
import yaml

ROOT=Path(__file__).resolve().parents[1]

def extract_legacy() -> str:
    text=(ROOT/"gpt-instructions/12-gpt-huvudinstruktion.md").read_text(encoding="utf-8")
    marker="## Färdig huvudinstruktion för GPT Builder"
    pos=text.find(marker)
    if pos<0:
        raise SystemExit("legacy marker missing")
    m=re.search(r"```text\s*\n(.*?)\n```", text[pos+len(marker):], re.S)
    if not m:
        raise SystemExit("legacy instruction block missing")
    return m.group(1).rstrip()+"\n"

def main() -> int:
    errors=[]
    status=yaml.safe_load((ROOT/"migration-status-1.5.yaml").read_text(encoding="utf-8"))
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    registry=yaml.safe_load((ROOT/"runtime-distribution-registry.yaml").read_text(encoding="utf-8"))
    canonical=(ROOT/project["instructions"]["canonical"]).read_text(encoding="utf-8")
    legacy=extract_legacy()
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()
    readme=(ROOT/"README.md").read_text(encoding="utf-8")

    progress=status.get("progress",{})
    if progress.get("last_completed_step")!=7:
        errors.append("migration last_completed_step must be 7")
    if progress.get("completed_steps")!=list(range(1,8)):
        errors.append("migration completed_steps must be exactly 1..7")
    if status.get("final_readiness",{}).get("migration_steps_complete")!=7:
        errors.append("final readiness must declare 7/7")
    if canonical!=legacy:
        errors.append("canonical instruction diverges from extracted legacy runtime instruction")
    if version!="1.0.0":
        errors.append(f"VERSION changed: {version!r}")

    knowledge=sorted((ROOT/"knowledge").glob("*.md"))
    if len(knowledge)!=15:
        errors.append(f"expected exactly 15 Knowledge files, found {len(knowledge)}")

    if registry.get("active_targets")!=["chat","custom-gpt"]:
        errors.append(f"unexpected active targets: {registry.get('active_targets')}")
    for name in ("claude","opencode","openai_plugin"):
        if name not in registry.get("inactive_targets",{}):
            errors.append(f"missing inactive runtime decision: {name}")

    critical=[
        "Skapa alltid kopplingstabell innan eller tillsammans med kod.",
        "Koppla inte 5 V-signaler direkt till 3,3 V-ingångar om det inte är verifierat säkert.",
        "Rekommendera aldrig att motorer, reläer, elektromagneter, solenoider, högtalare eller andra externa laster drivs direkt från en GPIO-pin.",
        "Hjälp inte användaren att bygga projekt med nätspänning/230 V som vanlig hobbykoppling.",
        "Ställ normalt högst tre kompletterande frågor.",
        "skapa `circuit.yaml` enligt Circuit SVG Generator v1.1",
    ]
    for marker in critical:
        if marker not in canonical:
            errors.append(f"canonical behavior marker missing: {marker}")

    if "7/7 komplett" not in readme:
        errors.append("README does not state completed GPT Builder 1.5 migration")

    if errors:
        print("GPT BUILDER 1.5 MIGRATION: FAIL")
        for e in errors: print("-",e)
        return 1

    print("GPT BUILDER 1.5 MIGRATION: PASS")
    print("7/7 complete; VERSION 1.0.0; 15/15 Knowledge; safety/code/wiring/circuit.yaml behavior preserved")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
