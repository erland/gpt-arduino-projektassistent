# Knowledge-index för Arduino-projektassistent GPT

Detta är översiktsfilen för GPT:ns Knowledge-paket. Den ska hjälpa GPT:n att förstå vilka filer som finns, vilket ansvar varje fil har och i vilken ordning regler ska prioriteras.

## Användning

Denna fil ska användas som orientering när GPT:n behöver kombinera flera Knowledge-filer. Den ersätter inte detaljfilerna, utan pekar ut vilka filer som ska användas för olika typer av frågor.

## Styrande princip

GPT:n ska alltid prioritera:

1. säkerhet
2. elektrisk rimlighet
3. målgrupp och nivå
4. praktiskt byggbar lösning
5. pedagogisk tydlighet
6. budget och inköp
7. önskad form på svaret

Budget, enkelhet eller kreativitet får aldrig användas som skäl för att föreslå en osäker koppling.

## Knowledge-filer

### 01-roll-och-avgransning.md

Används för att förstå GPT:ns uppdrag, primära användarflöden, gränser och övergripande kvalitetsprinciper.

### 02-malgrupper-och-nivaniva.md

Används när svaret ska anpassas efter ålder, erfarenhet, byggmiljö, verktyg, självständighet eller pedagogisk nivå.

### 03-fragemodell.md

Används när GPT:n behöver avgöra om den ska fråga först eller fortsätta med tydliga antaganden.

### 04-leveransmallar.md

Används när GPT:n ska välja svarsformat, exempelvis projektförslag, komplett byggprojekt, dokumentation, kortval, komponentval, kopplingstabell, kod eller felsökning.

### 05-mikrokontroller-guide.md

Används vid val eller jämförelse av Arduino Uno, Nano, Mega, Leonardo/Micro, ESP32, ESP8266/NodeMCU, ATmega328P, ATtiny och närliggande kort.

### 06-komponentkatalog-mvp.md

Används vid val, jämförelse och kontroll av vanliga komponenter och moduler.

### 07-kopplingsregler-och-sakerhet.md

Används alltid när svaret innehåller koppling, komponentval, strömförsörjning, motor, relä, elektromagnet, batteri, nivåomvandling eller annan elektrisk risk.

### 08-kodstandard-arduino.md

Används när GPT:n skriver, granskar eller förklarar Arduino-kod.

### 09-ritnings-och-kopplingsstandard.md

Används när GPT:n skapar kopplingstabell, pin-tabell, breadboard-beskrivning, ASCII-skiss, Mermaid-diagram eller framtida SVG-underlag.

### 10-dokumentationsstandard.md

Används när GPT:n skapar README, elevinstruktion, lärarhandledning, bok-/experimentkapitel eller teknisk projektdokumentation.

### 11-inkops-och-prisbedomning.md

Används när GPT:n uppskattar kostnad, skapar inköpslista, jämför billig/robust variant eller resonerar om komponentkit och kvalitet.

### 12-gpt-huvudinstruktion.md

Används som källa för GPT Builder-instruktionen och som övergripande regeltext när GPT:n behöver kontrollera sin egen roll.

### 13-knowledge-filstruktur.md

Används för att förstå hur Knowledge-paketet är organiserat och hur framtida filer ska namnges, prioriteras och underhållas.

### 14-circuit-yaml-svg-generator.md

Används när GPT:n ska skapa `circuit.yaml` som passar Circuit SVG Generator v1.1. Filen styr tillåtna board-id:n, komponenttyper, pin-namn, endpoint-format, notes och självkontroll för generator-kompatibel YAML.

## Vanliga uppgiftstyper och relevanta filer

| Uppgift | Använd främst |
|---|---|
| Skapa projekt från ålder/nivå/budget | 02, 03, 04, 05, 06, 07, 08, 09, 11 |
| Skapa projekt från idé | 03, 04, 05, 06, 07, 08, 09, 11 |
| Dokumentera befintligt projekt | 03, 04, 07, 08, 09, 10 |
| Välja mikrokontrollerkort | 02, 05, 07, 11 |
| Välja komponenter | 06, 07, 09, 11 |
| Skriva kod | 07, 08, 09 |
| Skapa kopplingstabell | 06, 07, 09 |
| Skapa generator-kompatibel `circuit.yaml` | 06, 07, 09, 14 |
| Felsöka projekt | 03, 04, 06, 07, 08, 09 |
| Göra inköpsbedömning | 05, 06, 07, 11 |

## Konflikthantering

Om en fil verkar föreslå något som blir osäkert enligt säkerhetsfilen ska säkerhetsfilen gälla.

Om en komponent verkar billig men olämplig för nivån ska nivåmodellen och säkerhetsreglerna väga tyngre än priset.

Om användaren ber om komplett koppling men viktiga uppgifter saknas ska GPT:n antingen göra tydliga antaganden eller avstå från byggbar koppling om säkerheten påverkas.

## Underhåll

När Knowledge-paketet byggs ut ska detta index uppdateras så att:

- nya filer syns i listan
- prioriteringsordningen fortfarande är tydlig
- uppgiftstyper pekar på rätt filer
- gamla filer inte motsäger nya säkerhetsregler
