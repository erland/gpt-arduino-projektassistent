# Designbeslut – steg 6

## Steg

**Steg 6 – Skapa komponentkatalog MVP**

## Huvudbeslut

Komponentkatalogen utformas som en praktisk beslutsmodell, inte som en komplett databladssamling.

Syftet är att GPT:n ska kunna göra säkrare och mer konsekventa komponentval i projektförslag, kopplingstabeller, kod och felsökning.

## Avgränsning

MVP-katalogen omfattar vanliga komponenter och moduler för Arduino-baserade hobby- och utbildningsprojekt:

- grundkomponenter
- ljud och enkel interaktion
- sensorer
- displayer
- motorer och laster
- kommunikations- och expansionsmoduler
- enkel ljudförstärkning

Den omfattar inte fullständig elektrisk dimensionering, exakta databladsvärden, nätspänningskopplingar eller avancerad produktjämförelse.

## Viktiga designval

### 1. Komponenter nivåmärks

Varje komponent kopplas till ungefärlig användarnivå. Detta gör att GPT:n kan föreslå enklare komponenter för barn och nybörjare och mer avancerade komponenter först när användarens nivå motiverar det.

### 2. Säkerhetsregler placeras nära komponenterna

Katalogen innehåller inte bara vad komponenten gör, utan även vanliga fel och säkerhetskrav. Detta är viktigt eftersom elektronikprojekt ofta misslyckas på grund av ström, spänning, nivåer eller saknade skyddskomponenter.

### 3. Moduler behandlas försiktigt

Många hobbykomponenter säljs som moduler med varierande utformning. Därför säger katalogen ofta att användaren ska kontrollera modulens märkning eller produktbeskrivning i stället för att GPT:n ska anta exakt konstruktion.

### 4. LM393 hanteras som osäker beteckning

LM393 är en komparator och förekommer på många olika moduler. GPT:n ska därför inte behandla `LM393` som en specifik sensor.

### 5. ESP32/ESP8266 kräver extra nivåkontroll

Eftersom många Arduino-moduler är 5 V-orienterade måste GPT:n särskilt kontrollera 3,3 V-kompatibilitet när ESP32 eller ESP8266 används.

## Tillagda filer

- `knowledge/06-komponentkatalog-mvp.md`
- `gpt-instructions/06-komponentkatalog-mvp.md`
- `notes/designbeslut-steg-06.md`
- `testfall/testfall-steg-06.md`

## Fortsatt arbete

Nästa steg bör skapa en separat och mer bindande fil för kopplingsregler och säkerhetsregler. Komponentkatalogen innehåller redan många säkerhetsnoteringar, men steg 7 bör samla dessa till en tydligare generell regelmodell.
