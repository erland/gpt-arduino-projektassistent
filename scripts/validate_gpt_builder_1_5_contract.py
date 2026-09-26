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
    contract=yaml.safe_load((ROOT/"gpt-builder-1.5-contract.yaml").read_text(encoding="utf-8"))
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    canonical=(ROOT/project["instructions"]["canonical"]).read_text(encoding="utf-8")
    legacy=extract_legacy()
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()

    if contract["builder"]["target_version"]!="1.5.0":
        errors.append("target builder version must be 1.5.0")
    if contract["builder"]["behavior_preserving"] is not True:
        errors.append("migration must remain behavior-preserving")
    if canonical!=legacy:
        errors.append("canonical instruction diverges from extracted legacy runtime instruction")
    if version!="1.0.0":
        errors.append(f"VERSION changed during migration: {version!r}")

    knowledge=sorted((ROOT/"knowledge").glob("*.md"))
    if len(knowledge)!=15:
        errors.append(f"expected exactly 15 Knowledge files, found {len(knowledge)}")

    markers=[
        "Prioritera alltid säkerhet, pedagogik och praktisk byggbarhet.",
        "Skapa alltid kopplingstabell innan eller tillsammans med kod.",
        "Koppla inte 5 V-signaler direkt till 3,3 V-ingångar om det inte är verifierat säkert.",
        "Rekommendera aldrig att motorer, reläer, elektromagneter, solenoider, högtalare eller andra externa laster drivs direkt från en GPIO-pin.",
        "Hjälp inte användaren att bygga projekt med nätspänning/230 V som vanlig hobbykoppling.",
        "Ställ normalt högst tre kompletterande frågor.",
        "skapa `circuit.yaml` enligt Circuit SVG Generator v1.1",
    ]
    for marker in markers:
        if marker not in canonical:
            errors.append(f"canonical instruction missing behavior marker: {marker}")

    b=contract["behavior"]
    checks={
        "safety_priority_first": True,
        "low_voltage_default": True,
        "mains_230v_hobby_builds_allowed": False,
        "gpio_direct_external_load_drive_allowed": False,
        "voltage_current_logic_level_and_gnd_checks_required": True,
        "wiring_table_before_or_with_code": True,
        "code_pin_and_wiring_consistency_required": True,
        "safe_load_start_state_required": True,
    }
    for key,value in checks.items():
        if b.get(key) is not value:
            errors.append(f"{key} must be {value}")
    if b.get("max_normal_followup_questions")!=3:
        errors.append("max_normal_followup_questions must remain 3")
    if b.get("circuit_yaml_specification")!="Circuit SVG Generator v1.1":
        errors.append("circuit.yaml specification changed")

    if errors:
        print("GPT BUILDER 1.5 CONTRACT: FAIL")
        for e in errors: print("-",e)
        return 1
    print("GPT BUILDER 1.5 CONTRACT: PASS")
    print("VERSION 1.0.0; 15/15 Knowledge; safety/wiring/code/circuit.yaml behavior preserved")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
