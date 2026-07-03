# Designbeslut – Steg 10 Dokumentationsstandard

## Syfte med steget

Steg 10 inför en gemensam dokumentationsstandard för Arduino-projektassistenten. Standarden ska göra GPT:n konsekvent när den skapar README, elevinstruktioner, lärarhandledningar, bokliknande experimentkapitel och teknisk projektdokumentation.

## Viktigaste beslut

### 1. Flera dokumentationslägen i stället för en enda mall

GPT:n ska inte alltid använda samma dokumentationsmall. Ett README, en elevinstruktion och ett bokkapitel har olika syften. Därför införs separata lägen med olika struktur.

### 2. Befintliga projekt ska dokumenteras med tydlig osäkerhetshantering

När användaren ger kod eller lösa anteckningar kan GPT:n ofta förstå mycket, men inte allt. Därför ska dokumentationen skilja mellan:

- bekräftat från materialet
- antaganden
- saknad information
- rekommenderade förbättringar

Detta minskar risken att GPT:n hittar på fysisk koppling, modulvariant eller säkerhetsdetaljer.

### 3. Byggbar dokumentation kräver kopplingstabell

Steg 10 lutar sig mot steg 9. Om dokumentationen ska kunna användas för att bygga projektet måste kopplingstabell finnas. Bild, Mermaid eller textskiss får komplettera men inte ersätta teknisk tabell.

### 4. Dokumentation ska inkludera test och felsökning

Ett Arduino-projekt är inte färdigdokumenterat bara för att kod och koppling finns. Användaren behöver veta hur projektet ska bete sig och vad som kan vara fel om det inte fungerar.

### 5. Säkerhetsavsnitt ska vara specifikt

Standarden säger att säkerhetsavsnitt inte får vara generiska. Om projektet innehåller motor, relä, batteri eller 5 V/3,3 V-blandning ska riskerna beskrivas konkret.

### 6. Målgrupp styr detaljnivå

Barn, nybörjare och erfarna användare behöver olika dokumentation. Standarden kopplas därför till nivåmodellen från steg 2.

## Avgränsningar

Steg 10 skapar inte slutlig GPT-huvudinstruktion. Den kommer i steg 12.

Steg 10 skapar inte inköps- och prisregler. Det kommer i steg 11.

Steg 10 skapar inte ett komplett projektbibliotek. Det kommer senare i planen.

## Filer tillagda i detta steg

- `gpt-instructions/10-dokumentationsstandard.md`
- `knowledge/10-dokumentationsstandard.md`
- `notes/designbeslut-steg-10.md`
- `testfall/testfall-steg-10.md`
