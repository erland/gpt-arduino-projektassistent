# Projektstatus

## Projekt

**Namn:** Arduino-projektassistent GPT  
**Syfte:** Skapa en specialiserad GPT som hjälper användare att välja, planera, bygga, dokumentera och felsöka Arduino-baserade elektronikprojekt.  
**Status:** Steg 1–14 genomförda + SVG-generator v1.1-kompatibilitet  
**Senast uppdaterad:** 2026-07-03

## Genomförda steg

### Steg 1 – Fastställ GPT:ns syfte och gränser

Klart.

Detta steg har definierat:

- GPT:ns övergripande uppdrag
- huvudsakliga användarflöden
- stöd för mikrokontrollerkort
- stöd för komponentval
- säkerhetsgränser
- praktiska avgränsningar
- kvalitetsprinciper för svar
- vad GPT:n inte ska försöka vara

### Steg 2 – Definiera målgrupper och nivåer

Klart.

Detta steg har definierat:

- målgrupper för GPT:n
- femgradig nivåmodell från nivå 0 till nivå 4
- hur ålder och erfarenhet ska hanteras separat
- standardantagande när information saknas
- hur budget, verktyg och byggsätt påverkar nivå
- när GPT:n ska förenkla ett projekt
- när GPT:n ska erbjuda enklare och mer avancerade alternativ
- hur projektförslag ska nivåmärkas

### Steg 3 – Definiera GPT:ns frågemodell

Klart.

Detta steg har definierat:

- när GPT:n ska fråga först
- när GPT:n ska gå vidare med antaganden
- max tre kompletterande frågor som normalregel
- prioritering av frågor utifrån säkerhet, nivå, budget och komponenttillgång
- frågemodell för projekt från målgrupp, erfarenhet och budget
- frågemodell för projekt från idé
- frågemodell för dokumentation av befintliga projekt
- frågemodell för komponentval, kortval, budget och felsökning
- säkerhetsundantag där GPT:n ska styra om eller fråga mer noggrant

### Steg 4 – Skapa leveransmallar

Klart.

Detta steg har definierat:

- gemensamma krav för tekniska leveranser
- mall för flera projektförslag
- mall för komplett byggbart projekt
- mall för dokumentation av befintligt projekt
- mall för mikrokontrollerrekommendation
- mall för komponentrekommendation
- mall för kopplingstabell
- mall för kodleverans
- mall för felsökning
- mall för jämförelser och korta pedagogiska svar
- miniminivå för byggbara projekt, dokumentation och kortval
- regler för antaganden, säkerhetsnoteringar och nästa steg

### Steg 5 – Skapa mikrokontroller-guide

Klart.

Detta steg har definierat:

- beslutsmodell för val av mikrokontrollerkort
- när Uno, Nano, Mega, Leonardo/Micro, ESP32, NodeMCU/ESP8266 och ATmega-baserade lösningar passar
- nivåanpassning av kortval
- snabbval utifrån projektkrav
- vanliga fallgropar för respektive kortfamilj
- varningar för 5 V/3,3 V-logik, boot-pinnar och externa laster
- hur kortval ska kopplas till komponentval, kod och säkerhet

### Steg 6 – Skapa komponentkatalog MVP

Klart.

Detta steg har definierat:

- en komponentkatalog MVP för vanliga Arduino-komponenter och moduler
- standardformat för komponentposter
- nivåanpassning av komponentval
- komponentgrupper för grundkomponenter, ljud, sensorer, displayer, motorer, drivare, I/O-expansion och enklare förstärkning
- krav på motstånd, pullup, spänningsdelare, drivsteg, extern matning, nivåomvandling och skyddsdiod där det behövs
- särskilda regler för ESP32/ESP8266 och 5 V/3,3 V-kompatibilitet
- säkerhetsregler för motorer, reläer, elektromagneter, solenoider och andra laster
- hantering av oklara modulnamn, särskilt LM393
- testfall för att verifiera komponentval och säkerhetsvarningar

### Steg 7 – Skapa kopplingsregler och säkerhetsregler

Klart.

Detta steg har definierat:

- säkerhetshierarki för kopplings- och projektbeslut
- säkerhetsnivåer för projekt och komponentkombinationer
- regler för spänning, logiknivåer och 5 V/3,3 V-kompatibilitet
- regler för GPIO, ström, externa laster och gemensam GND
- regler för nätspänning, batterier och litiumceller
- kopplingsregler för LED, knappar, analoga sensorer, I2C, SPI, UART, motorer, servon, reläer och elektromagneter
- krav på kopplingstabell och strömförsörjningsavsnitt
- när GPT:n ska fråga, avstå från komplett koppling eller föreslå säkrare alternativ
- självkontroll före leverans av byggbara projekt

### Steg 8 – Skapa kodstandard

Klart.

Detta steg har definierat:

- kodstandard för Arduino-baserade projekt
- hur kod ska matcha kopplingstabell, komponentval och valt mikrokontrollerkort
- normalformat för kodleveranser
- nivåanpassning av kod från barn/nybörjare till avancerade användare
- när `delay()` är acceptabelt och när `millis()` bör användas
- regler för pinnar, kommentarer, bibliotek, Serial Monitor och felsökning
- kortspecifika kodregler för klassiska Arduino-kort, Leonardo/Micro, ESP32, ESP8266/NodeMCU och fristående ATmega328P
- kodregler för knappar, analog läsning, PWM, I2C, SPI, servon, motorer, reläer, elektromagneter, displayer och WiFi
- krav på säkert startläge för laster
- regler för att GPT:n inte ska skriva kod som stödjer osäkra kopplingar
- testfall för att verifiera kodstandard, nivåanpassning och säkerhetskoppling

### Steg 9 – Skapa ritnings- och kopplingsstandard

Klart.

Detta steg har definierat:

- ritnings- och kopplingsstandard för Arduino-projekt
- obligatorisk kopplingstabell för byggbara projekt
- pin-tabell för större eller mer känsliga projekt
- strömförsörjningsavsnitt för projekt med mer än trivial koppling
- standard för breadboard-beskrivningar och byggordning
- namnstandard för pinnar och anslutningar
- regler för I2C, SPI, UART, motorer, reläer och externa laster
- hur ASCII, Mermaid och framtida SVG-underlag får användas
- färgstandard för framtida kopplingsbilder
- kontroll mot kod, komponentval och säkerhetsregler
- hur osäkerhet kring modulvarianter, pinout och spänningsnivå ska markeras
- testfall för kopplingstabeller, diagram, kod/koppling-matchning och osäkra moduler


### Steg 10 – Skapa dokumentationsstandard

Klart.

Detta steg har definierat:

- dokumentationsstandard för Arduino-baserade projekt
- dokumentationslägen för README, elevinstruktion, lärarhandledning, bok-/experimentkapitel och teknisk projektdokumentation
- komplett standardmall för byggbara projekt
- hur dokumentation av befintliga projekt ska skilja mellan bekräftat material, antaganden, saknad information och rekommenderade förbättringar
- krav på komponentlista, kopplingstabell, kod, kodförklaring, test, felsökning och vidareutveckling
- hur säkerhetsavsnitt ska användas och göras specifika
- nivåanpassning för barn, nybörjare, fortsättare och erfarna användare
- när GPT:n inte ska skapa byggbar dokumentation utan i stället föreslå säker översikt eller säkrare variant
- testfall för dokumentationsformat och osäkerhetshantering


### Steg 11 – Skapa inköps- och prisbedömningsregler

Klart.

Detta steg har definierat:

- inköps- och prisbedömningsregler för Arduino-projekt
- skillnaden mellan komponentlista och inköpslista
- hur GPT:n ska hantera grova prisuppskattningar utan att låtsas känna till aktuella priser
- prisnivåer i stället för exakta belopp när prisdata inte är verifierad
- två budgetscenarier: användaren har basutrustning respektive behöver köpa allt från början
- regler för billigaste rimliga variant och robustare/lättare variant
- när officiella Arduino-kort, kompatibla kort och ESP32/ESP8266 är rimliga ur pris- och nybörjarperspektiv
- regler för komponentkit, frakt, småorder och kvalitetskontroll vid köp
- söktermer och specifikationskrav när specifika produkter inte kan verifieras
- att säkerhetskritiska delar aldrig får sparas bort för att minska kostnaden
- testfall för budget, inköp, aktuella priser, kit, kompatibla kort och kostnadsrisker

### Steg 12 – Skapa GPT-instruktionen

Klart.

Detta steg har definierat:

- färdig huvudinstruktion för GPT Builder
- kortversion av huvudinstruktionen
- bindande prioriteringsordning för säkerhet, elektrisk rimlighet, nivå, budget, pedagogik och pris
- hur huvudinstruktionen ska samspela med Knowledge-filerna
- krav på byggbara projektsvar, kopplingstabell, kod, test, felsökning och säkerhetsnoteringar
- regler för hur GPT:n ska hantera kortval, komponentval, 5 V/3,3 V, externa laster, nätspänning, batterier, dokumentation och prisuppskattningar
- självkontroll före byggbara svar
- testfall för att verifiera huvudinstruktionens styrning

### Steg 13 – Skapa Knowledge-filstrukturen

Klart.

Detta steg har definierat:

- Knowledge-filstruktur för GPT Builder och framtida underhåll
- nytt Knowledge-index som karta över filerna
- ansvarsfördelning mellan roll, nivå, frågemodell, leveransmallar, kortval, komponentval, säkerhet, kod, koppling, dokumentation och inköp
- prioriteringsordning mellan Knowledge-filer
- vilka filer som bör användas för olika uppgiftstyper
- konfliktregler när säkerhet, nivå, budget eller användarens önskemål drar åt olika håll
- namnstandard och rubrikstandard för framtida Knowledge-filer
- rekommenderad uppladdningslista för första MVP:n i GPT Builder
- underhållsregler och kontroll före paketering
- testfall för att verifiera att Knowledge-strukturen används som avsett

### Steg 14 – Bygg en första MVP i GPT Builder

Klart.

Detta steg har definierat:

- praktisk installationsguide för att skapa första MVP:n i GPT Builder
- rekommenderat namn och beskrivning för GPT:n
- vilken huvudinstruktion som ska användas i GPT Builder
- vilka Knowledge-filer som ska laddas upp och vilka projektfiler som inte ska laddas upp
- rekommenderade capabilities för webbsökning, bildgenerering, Code Interpreter och Actions
- varför Actions och bildgenerering bör vara av i första MVP
- första verifieringschecklista efter att GPT:n skapats
- definition av när MVP:n är godkänd för vidare test
- avgränsningar för vad som medvetet ligger utanför första MVP:n

## Ej påbörjade steg

- Steg 15 – Skapa konversationsstartare
- Steg 16 – Testa GPT:n med typfall
- Steg 17 – Justera hallucinationsskydd
- Steg 18 – Skapa intern granskningschecklista
- Steg 19 – Skapa version 1 och använd den praktiskt
- Steg 20 – Bygg version 2 med bättre kopplingsbilder
- Steg 21 – Bygg version 3 med inköpsstöd
- Steg 22 – Bygg version 4 med projektbibliotek
- Steg 23 – Bygg version 5 med bok-/kursintegration

## Tillagda filer i steg 2

- `gpt-instructions/02-malgrupper-och-nivaniva.md`
- `knowledge/02-malgrupper-och-nivaniva.md`
- `notes/designbeslut-steg-02.md`
- `testfall/testfall-steg-02.md`

## Tillagda filer i steg 3

- `gpt-instructions/03-fragemodell.md`
- `knowledge/03-fragemodell.md`
- `notes/designbeslut-steg-03.md`
- `testfall/testfall-steg-03.md`

## Tillagda filer i steg 4

- `gpt-instructions/04-leveransmallar.md`
- `knowledge/04-leveransmallar.md`
- `notes/designbeslut-steg-04.md`
- `testfall/testfall-steg-04.md`

## Tillagda filer i steg 5

- `gpt-instructions/05-mikrokontroller-guide.md`
- `knowledge/05-mikrokontroller-guide.md`
- `notes/designbeslut-steg-05.md`
- `testfall/testfall-steg-05.md`

## Tillagda filer i steg 6

- `gpt-instructions/06-komponentkatalog-mvp.md`
- `knowledge/06-komponentkatalog-mvp.md`
- `notes/designbeslut-steg-06.md`
- `testfall/testfall-steg-06.md`

## Tillagda filer i steg 7

- `gpt-instructions/07-kopplingsregler-och-sakerhet.md`
- `knowledge/07-kopplingsregler-och-sakerhet.md`
- `notes/designbeslut-steg-07.md`
- `testfall/testfall-steg-07.md`

## Tillagda filer i steg 8

- `gpt-instructions/08-kodstandard-arduino.md`
- `knowledge/08-kodstandard-arduino.md`
- `notes/designbeslut-steg-08.md`
- `testfall/testfall-steg-08.md`

## Tillagda filer i steg 9

- `gpt-instructions/09-ritnings-och-kopplingsstandard.md`
- `knowledge/09-ritnings-och-kopplingsstandard.md`
- `notes/designbeslut-steg-09.md`
- `testfall/testfall-steg-09.md`


## Tillagda filer i steg 10

- `gpt-instructions/10-dokumentationsstandard.md`
- `knowledge/10-dokumentationsstandard.md`
- `notes/designbeslut-steg-10.md`
- `testfall/testfall-steg-10.md`


## Tillagda filer i steg 11

- `gpt-instructions/11-inkops-och-prisbedomning.md`
- `knowledge/11-inkops-och-prisbedomning.md`
- `notes/designbeslut-steg-11.md`
- `testfall/testfall-steg-11.md`
## Tillagda filer i steg 12

- `gpt-instructions/12-gpt-huvudinstruktion.md`
- `knowledge/12-gpt-huvudinstruktion.md`
- `notes/designbeslut-steg-12.md`
- `testfall/testfall-steg-12.md`


## Tillagda filer i steg 13

- `gpt-instructions/13-knowledge-filstruktur.md`
- `knowledge/00-knowledge-index.md`
- `knowledge/13-knowledge-filstruktur.md`
- `notes/designbeslut-steg-13.md`
- `testfall/testfall-steg-13.md`

## Tillagda filer i steg 14

- `gpt-instructions/14-bygg-mvp-i-gpt-builder.md`
- `gpt-builder/README.md`
- `gpt-builder/01-installationsguide-mvp.md`
- `gpt-builder/02-uppladdningslista-knowledge.md`
- `gpt-builder/03-capabilities-och-installningar.md`
- `gpt-builder/04-forsta-verifiering.md`
- `notes/designbeslut-steg-14.md`
- `testfall/testfall-steg-14.md`

## Rekommenderad nästa prompt

```text
Gör steg 15 enligt [PLAN-GPT-ARDUINO] utifrån senaste projekt zip och ge mig en uppdaterad projekt zip.
```


## Komplettering – SVG-generator-kompatibilitet

Tillagt:

- `knowledge/14-circuit-yaml-svg-generator.md`
- `testfall/testfall-svg-generator-kompatibilitet.md`
- `notes/designbeslut-svg-generator-kompatibilitet.md`

Syfte: säkerställa att GPT:n kan skapa `circuit.yaml` som passar den befintliga SVG-generatorn och inte blandar ihop den bredare komponentmodellen med generatorns mer begränsade v1-format.

Knowledge-filer efter komplettering: 15 av max 20.


### Komplettering – SVG-generator v1.1-kompatibilitet

Klart.

Detta steg har uppdaterat GPT-paketet efter att Circuit SVG Generator kompletterats till v1.1.

Detta har definierat:

- att GPT:n ska skapa `version: 1.1` i generator-kompatibel YAML
- stöd för nya board-id:n: `arduino_nano`, `arduino_mega`, `nodemcu_esp8266`, `arduino_leonardo`, `arduino_micro`, `arduino_nano_esp32`
- stöd för nya specifika komponenttyper, bland annat `rgb_led`, `ldr`, `dht22`, `bme280`, `hc_sr04`, `oled_i2c`, `lcd1602_i2c`, `mfrc522_rfid`, `relay_module`, `dc_motor`, `drv8833`, `l9110s`, `pca9685`, `pcf8574`, `pcf8575`, `cd74hc4067`, `logic_level_converter` och `ws2812_led`
- regler för när GPT:n ska använda specifik komponenttyp i stället för `generic_module` eller `i2c_module`
- att generatorn skapar logiska kopplingsbilder, inte exakt breadboardplacering
- att säkerhetsregler fortfarande går före renderbarhet
- nya testfall för SVG-generator v1.1

Knowledge-paketet innehåller nu 15 filer, vilket är under gränsen 20 filer. Huvudinstruktionen är fortfarande under 8 000 tecken.
