# Steg 14 – Bygg en första MVP i GPT Builder

Detta steg beskriver hur Arduino-projektassistenten ska byggas som en första fungerande MVP i GPT Builder.

Syftet är inte att skapa nya tekniska regler, utan att omsätta tidigare steg i en konkret GPT-konfiguration.

## Mål med steg 14

Efter detta steg ska projektet innehålla en praktisk installations- och konfigurationsguide för att skapa GPT:n i GPT Builder.

MVP:n ska kunna:

- använda huvudinstruktionen från steg 12
- använda Knowledge-filerna från steg 13
- svara på svenska som standard
- skapa projektförslag
- skapa kompletta byggbara Arduino-projekt på säker nivå
- dokumentera befintliga projekt
- rekommendera mikrokontrollerkort
- rekommendera komponenter
- skapa kopplingstabell, kod, teststeg och felsökning
- markera antaganden och säkerhetsrisker
- undvika att låtsas känna till aktuella priser utan verifiering

## Viktig princip

GPT Builder-konfigurationen ska vara enkel i första versionen.

Den ska inte börja med Actions, externa API:er, avancerade ritningsflöden eller automatiserade produktuppslag. Dessa kan läggas till i senare steg.

Första MVP:n ska i stället vara:

- tydligt instruerad
- Knowledge-styrd
- säkerhetsmedveten
- pedagogiskt konsekvent
- enkel att testa
- enkel att justera

## Rekommenderad GPT-identitet

### Namn

Arbetsnamn:

```text
Arduino-projektassistenten
```

Alternativa namn:

```text
Arduino i praktiken – Projektassistent
Arduino Projektguide
Arduino Bygghjälpen
```

Rekommenderat för MVP:

```text
Arduino-projektassistenten
```

### Kort beskrivning

```text
Hjälper dig att välja, planera, bygga, dokumentera och felsöka Arduino-baserade elektronikprojekt med rätt nivå, komponenter, koppling och kod.
```

### Instruktion

Använd den färdiga huvudinstruktionen från:

```text
gpt-instructions/12-gpt-huvudinstruktion.md
```

Använd i första hand fullversionen. Kortversionen används bara om instruktionsutrymmet skulle bli för begränsat.

## Rekommenderade Knowledge-filer

Ladda upp filerna i katalogen:

```text
knowledge/
```

För MVP ska alla befintliga Knowledge-filer från steg 13 laddas upp.

Antal filer efter steg 14:

```text
14 Knowledge-filer
```

Det ligger under gränsen på 20 filer.

Ladda inte upp katalogerna `gpt-instructions/`, `notes/`, `testfall/` eller `gpt-builder/` som Knowledge i GPT Builder. De är projektunderlag, inte primära Knowledge-filer för GPT:n.

## Rekommenderade capabilities

### Webbsökning

Rekommendation för MVP:

```text
Aktivera webbsökning om GPT:n ska kunna svara på aktuella pris-, produkt- och inköpsfrågor.
```

Om webbsökning är aktiverad ska GPT:n fortfarande följa prisreglerna:

- ange när priser är aktuella sökresultat
- ange när priser bara är grova uppskattningar
- inte låtsas veta aktuella priser utan verifiering
- inte välja bort säkerhetskritiska delar för att minska priset

Om GPT:n bara ska användas internt för projektstruktur, kod, dokumentation och komponentresonemang kan webbsökning vara avstängd i första testversionen.

### Bildgenerering

Rekommendation för MVP:

```text
Avstängd.
```

Skäl:

- teknisk korrekthet är viktigare än visuella bilder i första versionen
- kopplingstabell och pin-tabell är lättare att granska
- SVG- eller bildstandard bör byggas separat i senare steg

### Code Interpreter / avancerad dataanalys

Rekommendation för MVP:

```text
Valfri, men inte nödvändig.
```

Den kan vara användbar senare för att analysera större kodfiler, tabeller eller komponentlistor, men är inte ett krav för första MVP:n.

### Actions

Rekommendation för MVP:

```text
Avstängt.
```

Actions bör vänta till senare versioner om GPT:n ska kopplas till externa källor för:

- aktuella komponentpriser
- butikslager
- komponentdatabaser
- projektbibliotek
- intern dokumentationsgenerator

## Rekommenderad startkonfiguration

| Inställning | Rekommendation |
|---|---|
| Namn | Arduino-projektassistenten |
| Beskrivning | Hjälper dig att välja, planera, bygga, dokumentera och felsöka Arduino-baserade elektronikprojekt. |
| Instruktion | Fullversionen i `gpt-instructions/12-gpt-huvudinstruktion.md` |
| Knowledge | Alla filer i `knowledge/` |
| Webbsökning | På om aktuella priser/produkter ska stödjas, annars av i första internversion |
| Bildgenerering | Av |
| Code Interpreter | Valfri/av i första test |
| Actions | Av |
| Standardspråk | Svenska |

## Första manuella kontroll efter skapande

När GPT:n har skapats i GPT Builder ska följande kontrolleras direkt:

1. Svarar den på svenska?
2. Kan den skapa tre projektförslag utifrån ålder, nivå och budget?
3. Kan den skapa ett komplett enkelt Arduino-projekt med kopplingstabell och kod?
4. Varnar den vid direktstyrning av motor från GPIO?
5. Varnar den för 5 V-signal in till ESP32?
6. Dokumenterar den ett befintligt projekt utan att låtsas veta sådant som saknas?
7. Skiljer den mellan grova prisuppskattningar och aktuella priser?
8. Håller den svaren pedagogiska och inte onödigt långa?

## Definition av färdig MVP

MVP:n räknas som färdig när den klarar följande:

- kan ge projektförslag för nybörjare utan att överkomplicera
- kan skapa minst ett säkert byggbart projekt med Uno/Nano
- kan skapa minst ett säkert ESP32-projekt med 3,3 V-varningar
- kan rekommendera kort utifrån behov
- kan rekommendera komponenter utifrån nivå och budget
- kan skapa kopplingstabell och kod som matchar varandra
- kan ge felsökningssteg
- vägrar eller styr om vid uppenbart osäkra kopplingar
- markerar antaganden tydligt
- använder Knowledge-filerna konsekvent

## Avsiktligt utanför MVP

Följande ska inte krävas i steg 14:

- fullständigt projektbibliotek
- externa produktuppslag via API
- lagerstatus från butiker
- automatiska SVG-kopplingsbilder
- Fritzing-export
- komplett komponentdatabas
- stöd för nätspänningsprojekt
- säkerhetskritiska system
- publicerad GPT för extern publik

## Nästa steg

Efter steg 14 är nästa naturliga steg:

1. skapa konversationsstartare
2. testa GPT:n med typfall
3. skärpa hallucinationsskydd
4. skapa intern granskningschecklista
5. eventuellt bygga ut med projektbibliotek och bild-/SVG-standard
