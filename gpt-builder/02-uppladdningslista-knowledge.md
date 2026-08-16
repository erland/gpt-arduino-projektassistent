# Uppladdningslista för Knowledge

Dessa filer ska laddas upp som Knowledge i första MVP-versionen med SVG-generatorstöd v1.1.

## Antal filer

```text
15 filer
```

Det ligger under gränsen på 20 Knowledge-filer.

## Filer att ladda upp

```text
knowledge/00-knowledge-index.md
knowledge/01-roll-och-avgransning.md
knowledge/02-malgrupper-och-nivaniva.md
knowledge/03-fragemodell.md
knowledge/04-leveransmallar.md
knowledge/05-mikrokontroller-guide.md
knowledge/06-komponentkatalog-mvp.md
knowledge/07-kopplingsregler-och-sakerhet.md
knowledge/08-kodstandard-arduino.md
knowledge/09-ritnings-och-kopplingsstandard.md
knowledge/10-dokumentationsstandard.md
knowledge/11-inkops-och-prisbedomning.md
knowledge/12-gpt-huvudinstruktion.md
knowledge/13-knowledge-filstruktur.md
knowledge/14-circuit-yaml-svg-generator.md
```

## Filer som inte ska laddas upp som Knowledge

Ladda inte upp repositoryts installations- och byggstöd som Knowledge:

```text
gpt-instructions/
gpt-builder/
portable/
scripts/
.github/
README.md
VERSION
```

Skäl:

- `gpt-instructions/12-gpt-huvudinstruktion.md` är källan till den instruktion som klistras in i GPT Builder, inte en extra Knowledge-fil.
- `gpt-builder/` är installationsstöd för den som konfigurerar GPT:n.
- `portable/`, `scripts/` och `.github/` hör till distribution och release.
- `README.md` och `VERSION` är repositorymetadata.

## Prioritet vid konflikt

Om GPT:n verkar följa fel fil ska följande prioritet gälla:

1. Huvudinstruktionen i GPT Builder
2. `knowledge/07-kopplingsregler-och-sakerhet.md`
3. `knowledge/06-komponentkatalog-mvp.md`
4. `knowledge/05-mikrokontroller-guide.md`
5. `knowledge/08-kodstandard-arduino.md`
6. `knowledge/09-ritnings-och-kopplingsstandard.md`
7. `knowledge/14-circuit-yaml-svg-generator.md`
8. `knowledge/04-leveransmallar.md`
9. övriga Knowledge-filer

## SVG-generator v1.1

`knowledge/14-circuit-yaml-svg-generator.md` ska laddas upp om GPT:n ska kunna skapa `circuit.yaml` för Circuit SVG Generator v1.1.

Filen ersätter den tidigare v1-begränsningen och innehåller nu stöd för fler boards och komponenttyper.
