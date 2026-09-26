# OpenAI Plugin – compatibility assessment

Projekt: **Arduino-projektassistenten**  
GPT Byggaren: **1.5.0**

## Slutsats

OpenAI Plugin bedöms som **equivalent candidate**, **skills-first** och lämnas **inte aktiv** i denna migrering.

Projektets kärna består av instruktioner, Knowledge, strukturerad teknisk rådgivning, kod, kopplingstabeller, dokumentation och `circuit.yaml`. Det finns ingen unik media-capability som i sig blockerar parity.

Aktivering kräver däremot en faktisk plugin-distribution med skills som bevarar säkerhetsregler, Knowledge-prioritet och artefaktkontrakt, samt automatiska regressionstester.

## Parity-bedömning

| Område | Bedömning |
|---|---|
| Behavior | equivalent candidate |
| Capability | equivalent candidate |
| Artifact | equivalent candidate |
| Workspace/state | equivalent candidate |
| Tool | equivalent candidate |

## Skills-first upplägg

En framtida Plugin v1 bör minst ha skills för:
- projektplanering och nivåanpassning,
- säkerhetsgranskning,
- komponent- och mikrokontrollerval,
- kopplingstabell och pinout,
- Arduino-kod,
- felsökning,
- dokumentation,
- `circuit.yaml` enligt Circuit SVG Generator v1.1.

Permanent Knowledge måste antingen inkluderas direkt eller representeras på ett verifierat equivalent sätt.

## Kritiska regler som måste regressionstestas

- säker lågspänningsinriktning,
- inget vanligt hobbybygge med nätspänning/230 V,
- inga externa laster direkt från GPIO,
- kontroll av spänning, ström, logiknivå och gemensam GND,
- kopplingstabell före eller tillsammans med kod,
- konsistens mellan pinout, koppling och kod,
- högst tre kompletterande frågor normalt,
- tydliga antaganden vid ofullständigt underlag,
- `circuit.yaml` enligt Circuit SVG Generator v1.1,
- 15/15 Knowledge-filer eller semantiskt equivalent representation.

## Aktiveringsbeslut

- status: `assessed_not_active`
- compatibility: `equivalent`
- architecture: `skills_first`
- activation: `not_active`
- blocker: `plugin_distribution_and_safety_regression_not_implemented`

Ingen Plugin-distribution byggs eller publiceras i denna migrering.

## Aktiveringsregel

Plugin får aktiveras först när:
1. skills-strukturen är implementerad,
2. canonical instruktion och Knowledge är deterministiskt representerade,
3. säkerhetsmarkörerna regressionstestas,
4. kod/kopplings/pin-konsistensreglerna verifieras,
5. `circuit.yaml` v1.1-reglerna verifieras,
6. plugin-distributionen byggs och valideras i CI.

Ingen canonical produktregel ändras av denna bedömning.
