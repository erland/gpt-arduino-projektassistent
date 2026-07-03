# Knowledge-filstruktur

Detta dokument definierar hur Knowledge-filerna för Arduino-projektassistent GPT ska organiseras, prioriteras, namnges och underhållas.

## Mål

Knowledge-strukturen ska göra det enkelt att:

- ladda upp rätt filer i GPT Builder
- förstå vilka filer som är bindande respektive stödjande
- bygga ut komponentkatalog och projektbibliotek stegvis
- undvika dubblerade eller motstridiga regler
- hålla säkerhetsregler centrala
- testa GPT:n systematiskt efter varje steg

## Nuvarande filstruktur

```text
knowledge/
├── 00-knowledge-index.md
├── 01-roll-och-avgransning.md
├── 02-malgrupper-och-nivaniva.md
├── 03-fragemodell.md
├── 04-leveransmallar.md
├── 05-mikrokontroller-guide.md
├── 06-komponentkatalog-mvp.md
├── 07-kopplingsregler-och-sakerhet.md
├── 08-kodstandard-arduino.md
├── 09-ritnings-och-kopplingsstandard.md
├── 10-dokumentationsstandard.md
├── 11-inkops-och-prisbedomning.md
├── 12-gpt-huvudinstruktion.md
└── 13-knowledge-filstruktur.md
14-circuit-yaml-svg-generator.md
```

## Filkategorier

### Orientering

- `00-knowledge-index.md`
- `13-knowledge-filstruktur.md`

Dessa filer förklarar hur paketet ska användas och underhållas.

### Roll och styrning

- `01-roll-och-avgransning.md`
- `12-gpt-huvudinstruktion.md`

Dessa filer definierar vad GPT:n är, hur den ska prioritera och vilka gränser som gäller.

### Användarinteraktion

- `02-malgrupper-och-nivaniva.md`
- `03-fragemodell.md`
- `04-leveransmallar.md`

Dessa filer styr hur GPT:n anpassar svar efter användare, när den frågar och hur den strukturerar svar.

### Teknisk kärnkunskap

- `05-mikrokontroller-guide.md`
- `06-komponentkatalog-mvp.md`
- `07-kopplingsregler-och-sakerhet.md`
- `08-kodstandard-arduino.md`
- `09-ritnings-och-kopplingsstandard.md`

Dessa filer är kärnan för byggbara projekt.

### Dokumentation och inköp

- `10-dokumentationsstandard.md`
- `11-inkops-och-prisbedomning.md`

Dessa filer styr hur projekt dokumenteras och hur budget/inköp bedöms.

## Prioritet

När regler krockar gäller denna ordning:

1. Säkerhet och kopplingsregler
2. Mikrokontroller- och komponentkompatibilitet
3. Kod/koppling-matchning
4. Målgrupp och nivå
5. Leveransmall och dokumentationsformat
6. Budget och inköp
7. Stil och pedagogisk formulering

## Namnstandard

Filer ska namnges så här:

```text
NN-kort-beskrivande-namn.md
```

Där:

- `NN` är tvåsiffrigt löpnummer
- filnamnet är på svenska
- å, ä och ö undviks i filnamn
- orden separeras med bindestreck
- filens namn beskriver ansvar, inte bara ämne

Exempel:

```text
14-konversationsstartare.md
15-mvp-builder-checklista.md
16-testfall-typfall.md
17-hallucinationsskydd.md
```

## Rubrikstandard i Knowledge-filer

Varje ny Knowledge-fil bör innehålla:

```text
# Filens titel

## Syfte

## När filen ska användas

## Bindande regler

## Rekommenderat arbetssätt

## Relation till andra filer

## Testbara kontrollpunkter
```

Alla filer behöver inte ha exakt samma rubriker, men de ska vara så strukturerade att GPT:n kan använda dem utan att behöva tolka långa löptexter.

## Uppdelning av stora filer

Stora filer ska inte delas upp för tidigt. När en fil delas ska uppdelningen ha ett tydligt praktiskt värde.

### Rekommenderad framtida uppdelning av komponentkatalogen

```text
06a-grundkomponenter.md
06b-sensorer.md
06c-displayer.md
06d-motorer-drivare-och-laster.md
06e-kommunikation-io-och-expansion.md
06f-ljud-och-forstarkning.md
06g-esp32-esp8266-och-3v3.md
```

### Rekommenderad framtida uppdelning av projektbibliotek

```text
22a-projektbibliotek-niva-0.md
22b-projektbibliotek-niva-1.md
22c-projektbibliotek-niva-2.md
22d-projektbibliotek-esp32-iot.md
22e-projektbibliotek-motor-och-rorelse.md
```

## Uppladdning i GPT Builder

För en första MVP kan alla Knowledge-filer laddas upp, men huvudinstruktionen bör i första hand klistras in i instruktionsfältet från `12-gpt-huvudinstruktion.md`.

Rekommenderad minimilista för uppladdning:

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
13-knowledge-filstruktur.md
14-circuit-yaml-svg-generator.md
```

## Versionsprincip

Varje större steg ska:

- uppdatera `README.md`
- uppdatera `project-status.md`
- lägga till minst ett testfall om beteendet förändras
- dokumentera designbeslut i `notes/`
- skapa en ny zip med stegnummer

## Kontroll före paketering

Innan zip skapas ska följande kontrolleras:

```text
- Finns alla filer som README listar?
- Stämmer project-status med faktisk filstruktur?
- Har stegnumret uppdaterats?
- Finns testfall för nya regler?
- Finns inga uppenbara motsägelser mot säkerhetsreglerna?
- Är filnamnen konsekventa?
- Är zippen skapad från projektroten?
```

