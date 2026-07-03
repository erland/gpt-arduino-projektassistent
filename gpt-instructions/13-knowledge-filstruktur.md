# Steg 13 – Knowledge-filstruktur

Detta dokument beskriver hur GPT:ns Knowledge-underlag ska struktureras, namnges, prioriteras och användas när projektet laddas in i GPT Builder.

## Syfte

Steg 13 ska göra Knowledge-materialet praktiskt användbart som ett sammanhållet kunskapspaket. Målet är att GPT:n ska kunna hitta rätt styrande underlag, undvika motstridiga instruktioner och ge konsekventa svar även när användaren ber om olika typer av Arduino-projekt.

## Grundprincip

GPT:n ska styras av två lager:

1. **Huvudinstruktionen** i GPT Builder.
2. **Knowledge-filerna** som innehåller detaljerade regler, mallar och kunskapsunderlag.

Huvudinstruktionen ska vara kort och bindande. Knowledge-filerna ska vara detaljerade, men strukturerade så att GPT:n kan använda rätt fil för rätt uppgift.

## Rekommenderad Knowledge-struktur

Knowledge-mappen ska innehålla dessa filer:

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
```

## Prioriteringsordning mellan Knowledge-filer

När flera filer är relevanta ska GPT:n använda följande prioritet:

1. `12-gpt-huvudinstruktion.md`
2. `07-kopplingsregler-och-sakerhet.md`
3. `05-mikrokontroller-guide.md`
4. `06-komponentkatalog-mvp.md`
5. `08-kodstandard-arduino.md`
6. `09-ritnings-och-kopplingsstandard.md`
7. `04-leveransmallar.md`
8. `10-dokumentationsstandard.md`
9. `11-inkops-och-prisbedomning.md`
10. `02-malgrupper-och-nivaniva.md`
11. `03-fragemodell.md`
12. `01-roll-och-avgransning.md`
13. `13-knowledge-filstruktur.md`

Säkerhet och elektrisk rimlighet får alltid företräde framför nivå, budget, pedagogik och användarens önskemål.

## Filernas ansvar

### 00-knowledge-index.md

Används som första orienteringsfil. Den beskriver vilka Knowledge-filer som finns, när de ska användas och hur GPT:n ska kombinera dem.

### 01-roll-och-avgransning.md

Definierar GPT:ns uppdrag, gränser och vad den inte ska försöka vara.

### 02-malgrupper-och-nivaniva.md

Definierar målgrupper, nivåmodell och hur ålder, erfarenhet och byggsätt påverkar projektförslag.

### 03-fragemodell.md

Definierar när GPT:n ska fråga, när den ska gå vidare med antaganden och hur många frågor som normalt är rimligt.

### 04-leveransmallar.md

Definierar svarsmallar för projektförslag, kompletta byggprojekt, dokumentation, kortval, komponentval, kod och felsökning.

### 05-mikrokontroller-guide.md

Definierar beslutsmodell för val mellan Arduino Uno, Nano, Mega, Leonardo/Micro, ESP32, ESP8266/NodeMCU, ATmega och närliggande kort.

### 06-komponentkatalog-mvp.md

Definierar MVP-katalog över vanliga komponenter, moduler, risker, krav på motstånd, nivåanpassning, drivsteg och extern matning.

### 07-kopplingsregler-och-sakerhet.md

Definierar säkerhetsregler, kopplingsregler, förbjudna direktkopplingar, regler för externa laster, batterier, 5 V/3,3 V och nätspänning.

### 08-kodstandard-arduino.md

Definierar hur kod ska skrivas, struktureras och kopplas till valt kort, kopplingstabell och nivå.

### 09-ritnings-och-kopplingsstandard.md

Definierar kopplingstabeller, pin-tabeller, strömförsörjningsavsnitt, textskisser, Mermaid och framtida SVG-underlag.

### 10-dokumentationsstandard.md

Definierar hur README, elevinstruktion, lärarhandledning, experimentkapitel och teknisk dokumentation ska skrivas.

### 11-inkops-och-prisbedomning.md

Definierar grova prisnivåer, budgetresonemang, inköpslistor, söktermer, kvalitetskontroll och när aktuella priser behöver verifieras.

### 12-gpt-huvudinstruktion.md

Innehåller huvudinstruktion och kortversion som kan användas direkt i GPT Builder.

### 13-knowledge-filstruktur.md

Definierar hur Knowledge-filerna ska organiseras och kombineras.

## Regler för framtida Knowledge-filer

Nya Knowledge-filer ska:

- ha tvåsiffrig nummerserie
- ha beskrivande svenska filnamn utan å, ä eller ö i filnamnet
- innehålla tydligt syfte
- ange när filen ska användas
- ange relation till andra filer
- inte duplicera hela innehållet från andra filer
- inte sänka säkerhetsnivån från tidigare filer
- använda tydliga rubriker och punktlistor
- innehålla testbara regler där det är möjligt

## När en fil bör delas upp

En Knowledge-fil bör delas upp när den blir svår att överblicka eller när den innehåller flera kunskapsområden som ofta används separat.

Framtida kandidater för uppdelning:

```text
06a-grundkomponenter.md
06b-sensorer.md
06c-displayer.md
06d-motorer-och-drivare.md
06e-kommunikation-och-io-expansion.md
06f-esp32-och-3v3-varningar.md
```

Delning bör dock göras först när MVP:n är testad. För tidig uppdelning kan göra Knowledge-paketet svårare att underhålla.

## Rekommenderat uppladdningspaket i GPT Builder

För första MVP bör följande filer laddas upp som Knowledge:

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
```

`12-gpt-huvudinstruktion.md` ska i första hand användas som källa för GPT Builder-instruktionen, men kan även laddas upp som Knowledge om man vill att GPT:n ska kunna referera tillbaka till sina egna styrregler.

## Rekommenderad användning vid svar

När GPT:n får en användarfråga ska den internt avgöra vilka Knowledge-filer som behövs.

Exempel:

- Projekt från idé: använd 02, 03, 04, 05, 06, 07, 08, 09 och 11.
- Dokumentation av befintligt projekt: använd 03, 04, 07, 08, 09 och 10.
- Kortval: använd 02, 05, 07 och 11.
- Komponentval: använd 06, 07, 09 och 11.
- Kod: använd 07, 08 och 09.
- Felsökning: använd 03, 04, 06, 07, 08 och 09.

## Konflikthantering

Om två filer verkar ge olika riktning gäller:

1. säkerhet före funktion
2. elektrisk kompatibilitet före användarens önskade komponent
3. målgruppsanpassning före avancerad lösning
4. tydliga antaganden före låtsad säkerhet
5. dokumenterad begränsning före gissning

## Krav på underhåll

När en fil uppdateras ska följande kontrolleras:

- Behöver `00-knowledge-index.md` uppdateras?
- Behöver `project-status.md` uppdateras?
- Behöver testfall läggas till eller ändras?
- Har någon regel blivit motstridig mot säkerhetsfilen?
- Har huvudinstruktionen blivit inaktuell?

