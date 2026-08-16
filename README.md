# Arduino-projektassistenten

Repositoryt innehåller den aktuella källan för Custom GPT:n **Arduino-projektassistenten** samt byggstöd för både Custom GPT- och portabel Chat-distribution.

## Aktuell GPT-konfiguration

Huvudinstruktionen för GPT Builder genereras från blocket **Färdig huvudinstruktion för GPT Builder** i:

```text
gpt-instructions/12-gpt-huvudinstruktion.md
```

Permanent Knowledge består av exakt 15 filer i `knowledge/`:

```text
00-knowledge-index.md
01-roll-och-avgransning.md
02-malgrupper-och-nivaniva.md
03-fragemodell.md
04-leveransmallar.md
05-mikrokontroller-guide.md
06-komponentkatalog-mvp.md
07-kopplingsregler-och-sakerhet.md
08-kodstandard-arduino.md
09-ritnings-och-kopplingsstandard.md
10-dokumentationsstandard.md
11-inkops-och-prisbedomning.md
12-gpt-huvudinstruktion.md
13-knowledge-filstruktur.md
14-circuit-yaml-svg-generator.md
```

Installationsstöd finns i `gpt-builder/`.

## Distributioner

Bygg lokalt med:

```bash
python3 scripts/build_distributions.py
python3 scripts/validate_distributions.py
```

Det skapar:

```text
dist/arduino-projektassistent-custom-gpt-vX.Y.Z.zip
dist/arduino-projektassistent-chat-vX.Y.Z.zip
```

Vanliga push-, pull request- och manuella byggen använder versionen i `VERSION`.

Vid en publicerad GitHub Release används release-taggen som versionskälla. En release med taggen `v1.1.0` bygger därför paket med version `1.1.0`, oberoende av fallback-värdet i `VERSION`.

## Portabel Chat-version

Den portabla ZIP-filen kan bifogas i en vanlig ChatGPT-konversation. Börja med att be ChatGPT läsa `START-HERE.md` och använda paketets instruktioner och Knowledge under konversationen.

## Repositorystruktur

```text
.github/workflows/       GitHub Actions för build och release
gpt-builder/             aktuell installationsguide för GPT Builder
gpt-instructions/        kanonisk källa till GPT Builder-instruktionen
knowledge/               permanent Knowledge
portable/                startinstruktion för portabel Chat-version
scripts/                 build och validering
VERSION                  fallback-version för icke-releasebyggen
```

Historiska utvecklingssteg, designanteckningar och stegvisa testartefakter ligger inte längre kvar i arbetskopian; de bevaras av Git-historiken.
