# Claude Projects och OpenCode – runtime compatibility

Projekt: **Arduino-projektassistenten**  
GPT Byggaren: **1.5.0**

## Slutsats

Både Claude Projects och OpenCode bedöms som **equivalent candidates** på kontraktsnivå, men lämnas **inte aktiva** i denna migrering.

Det här projektets kritiska funktioner är främst instruktion-, Knowledge-, kod- och strukturerad text/filgenerering. Till skillnad från projekt som kräver en särskild bildruntime finns ingen separat generativ mediacapability som blockerar parity i sig.

Aktivering kräver däremot mer än teoretisk kompatibilitet: en faktisk distribution/adapterspecifikation måste byggas och de säkerhetskritiska regressionsreglerna måste valideras för respektive runtime.

## Parity-bedömning

| Område | Claude Projects | OpenCode |
|---|---|---|
| Behavior | equivalent candidate | equivalent candidate |
| Capability | equivalent candidate | equivalent candidate |
| Artifact | equivalent candidate | equivalent candidate |
| Workspace/state | equivalent candidate | equivalent candidate |
| Tool | equivalent candidate | equivalent candidate |

## Kritiska regler som måste bevaras

Varje runtime måste bevara:
- säker lågspänningsinriktning,
- inget vanligt hobbybygge med nätspänning/230 V,
- inga externa laster direkt från GPIO,
- kontroll av spänning, ström, logiknivå och gemensam GND,
- kopplingstabell före eller tillsammans med kod,
- konsistens mellan pinout, koppling och kod,
- högst tre kompletterande frågor normalt,
- tydliga antaganden vid ofullständigt underlag,
- `circuit.yaml` enligt Circuit SVG Generator v1.1,
- samtliga 15 Knowledge-filer eller semantiskt equivalent knowledge-paketering.

## Claude Projects

På kontraktsnivå finns inget identifierat kritiskt innehåll som i sig kräver en unik ChatGPT-only capability.

Beslut:
- compatibility: `equivalent`
- activation: `not_active`
- blocker: `distribution_and_safety_regression_not_implemented`

## OpenCode

Projektets fil-, kod- och strukturerade YAML-arbetsflöden passar väl med en workspace-orienterad runtime. Även här saknas dock ännu en byggd och validerad distribution.

Beslut:
- compatibility: `equivalent`
- activation: `not_active`
- blocker: `distribution_and_safety_regression_not_implemented`

## Aktiveringsregel

En runtime får aktiveras först när:
1. canonical instruktion paketeras deterministiskt,
2. 15/15 Knowledge-filer eller verifierad equivalent representation ingår,
3. säkerhetsmarkörerna regressionstestas,
4. kod/kopplings/pin-konsistensreglerna bevaras,
5. `circuit.yaml` v1.1-reglerna verifieras,
6. distributionen byggs och valideras i CI.

Ingen canonical produktregel ändras av denna bedömning.
