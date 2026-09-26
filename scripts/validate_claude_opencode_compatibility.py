#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    errors=[]
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    contract=yaml.safe_load((ROOT/"gpt-builder-1.5-contract.yaml").read_text(encoding="utf-8"))
    assessment=(ROOT/"docs/claude-opencode-compatibility.md").read_text(encoding="utf-8")

    for runtime in ("claude","opencode"):
        p=project["runtime"][runtime]
        if p.get("enabled") is not False:
            errors.append(f"{runtime} must remain disabled")
        if p.get("compatibility")!="equivalent":
            errors.append(f"{runtime} compatibility must be equivalent candidate")
        if p.get("activation")!="not_active":
            errors.append(f"{runtime} activation must be not_active")
        if p.get("blocker")!="distribution_and_safety_regression_not_implemented":
            errors.append(f"{runtime} blocker mismatch")
        c=contract["runtime_policy"]["inactive"][runtime]
        if c.get("compatibility")!="equivalent" or c.get("activation")!="not_active":
            errors.append(f"{runtime} contract status mismatch")

    for marker in [
        "säker lågspänningsinriktning",
        "inga externa laster direkt från GPIO",
        "konsistens mellan pinout, koppling och kod",
        "Circuit SVG Generator v1.1",
        "distributionen byggs och valideras i CI",
    ]:
        if marker not in assessment:
            errors.append(f"assessment missing marker: {marker}")

    if errors:
        print("CLAUDE/OPENCODE COMPATIBILITY: FAIL")
        for e in errors: print("-",e)
        return 1
    print("CLAUDE/OPENCODE COMPATIBILITY: PASS")
    print("Both runtimes are equivalent candidates but remain not active until built and safety-validated.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
