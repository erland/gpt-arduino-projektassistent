# Arduino-projektassistent GPT

Detta projektpaket innehåller arbetet med att skapa en specialiserad GPT som hjälper användare att välja, planera, bygga, dokumentera och felsöka Arduino-baserade elektronikprojekt.

Paketet är avsett att byggas ut steg för steg enligt `[PLAN-GPT-ARDUINO]`.

## Nuvarande status

Detta paket innehåller nu:

- **Steg 1 – Fastställ GPT:ns syfte och gränser**
- **Steg 2 – Definiera målgrupper och nivåer**
- **Steg 3 – Definiera GPT:ns frågemodell**
- **Steg 4 – Skapa leveransmallar**
- **Steg 5 – Skapa mikrokontroller-guide**
- **Steg 6 – Skapa komponentkatalog MVP**
- **Steg 7 – Skapa kopplingsregler och säkerhetsregler**
- **Steg 8 – Skapa kodstandard**
- **Steg 9 – Skapa ritnings- och kopplingsstandard**
- **Steg 10 – Skapa dokumentationsstandard**
- **Steg 11 – Skapa inköps- och prisbedömningsregler**
- **Steg 12 – Skapa GPT-instruktionen**
- **Steg 13 – Skapa Knowledge-filstrukturen**
- **Steg 14 – Bygg en första MVP i GPT Builder**
- **Komplettering – SVG-generator v1.1-kompatibilitet**

Steg 1 definierar:

- vad GPT:n ska hjälpa användaren med
- vilka användarflöden den ska stödja
- vilka typer av mikrokontrollerkort som ska ingå
- vilka typer av komponentval den ska kunna stödja
- vilka säkerhetsmässiga och praktiska gränser den ska hålla sig inom
- vilka principer som ska styra GPT:ns svar

Steg 2 definierar:

- målgrupper
- erfarenhetsnivåer
- nivåmodell från nivå 0 till nivå 4
- standardantagande när användaren inte anger nivå
- hur ålder och erfarenhet ska vägas mot varandra
- när projekt ska förenklas
- hur projektförslag ska nivåmärkas

Steg 3 definierar:

- när GPT:n ska fråga först
- när GPT:n ska gå vidare med tydliga antaganden
- principen om normalt högst tre kompletterande frågor
- frågemodeller för projekt från målgrupp, projekt från idé och dokumentation av befintligt projekt
- hur säkerhetskritiska frågor ska prioriteras
- hur GPT:n ska hantera oklara kortval, komponentval, budget och felsökning

Steg 4 definierar:

- leveransmallar för projektidéer, kompletta projekt, dokumentation, kortval, komponentval, koppling, kod och felsökning
- gemensamma krav för tekniska leveranser
- när olika mallar ska användas
- miniminivå för byggbara projekt
- krav på kopplingstabell, antaganden, teststeg och säkerhetsnoteringar
- testfall för att verifiera att GPT:n väljer rätt svarsmall

Steg 5 definierar:

- beslutsmodell för val av mikrokontrollerkort
- snabbval för vanliga projektsituationer
- stöd för Arduino Uno, Nano, Mega, Leonardo/Micro, Nano 33 IoT, Nano ESP32, ESP32, NodeMCU/ESP8266, ATmega328P och ATtiny
- nivåanpassning av kortval
- varningar för 5 V/3,3 V, ESP32/ESP8266-pinnar och externa laster
- praktiska regler för när kort ska väljas eller undvikas

Steg 6 definierar:

- komponentkatalog MVP för vanliga Arduino-komponenter och moduler
- standardformat för komponentposter
- nivåanpassning av komponentval
- stöd för grundkomponenter, sensorer, displayer, motorer, drivare, I/O-expansion och enklare ljud
- regler för när komponenter kräver motstånd, pullup, drivsteg, extern matning, nivåomvandlare eller skyddsdiod
- särskilda varningar för ESP32/ESP8266, 5 V/3,3 V, motorer, reläer, elektromagneter och oklara LM393-moduler
- testfall för att verifiera komponentval och säkerhetsvarningar

Steg 7 definierar:

- säkerhetshierarki för kopplings- och projektbeslut
- regler för spänning, logiknivå, ström och gemensam GND
- förbjudna direktkopplingar från GPIO
- hantering av nätspänning, batterier och externa laster
- regler för LED, knappar, analoga sensorer, I2C, SPI, motorer, servon, reläer och elektromagneter
- krav på kopplingstabell för byggbara projekt
- när GPT:n ska fråga, avstå från komplett koppling eller föreslå säkrare förenkling
- testfall för att verifiera säkerhetsvarningar och kopplingskontroll

Steg 8 definierar:

- kodstandard för Arduino-baserade projekt
- hur kod ska kopplas till kopplingstabell, kortval och komponentval
- normalformat för kodleveranser
- nivåanpassning av kod från barn/nybörjare till avancerade användare
- när `delay()` är acceptabelt och när `millis()` bör användas
- regler för pinnar, kommentarer, bibliotek, Serial Monitor och felsökning
- kortspecifika regler för Arduino Uno/Nano/Mega, Leonardo/Micro, ESP32, ESP8266/NodeMCU och fristående ATmega
- kodregler för knappar, analog läsning, PWM, I2C, SPI, servon, motorer, reläer, displayer och WiFi
- krav på säkert startläge och att kod inte får normalisera osäkra kopplingar
- testfall för att verifiera kodstandard och nivåanpassning

Steg 9 definierar:

- ritnings- och kopplingsstandard
- obligatorisk kopplingstabell för byggbara projekt
- pin-tabell för större eller mer känsliga projekt
- strömförsörjningsavsnitt för projekt med mer än trivial koppling
- standard för breadboard-beskrivningar, pin-namn, I2C, SPI, UART och externa laster
- när ASCII, Mermaid och SVG-underlag får användas
- färgstandard för framtida kopplingsbilder
- kontroll mot kod och säkerhetsregler
- hantering av osäkerhet kring modulvarianter, pinout och spänningsnivå
- testfall för kopplingstabeller, diagram, kod/koppling-matchning och osäkra moduler


Steg 10 definierar:

- dokumentationsstandard för README, elevinstruktion, lärarhandledning, bok-/experimentkapitel och teknisk projektdokumentation
- komplett standardmall för byggbar projektdokumentation
- hur befintliga projekt ska dokumenteras utifrån kod, komponentlista, foto, skiss eller anteckningar
- hur GPT:n ska skilja mellan bekräftad information, antaganden, saknad information och rekommenderade förbättringar
- krav på komponentlista, kopplingstabell, kodförklaring, test och felsökning
- nivåanpassning av dokumentation för barn, nybörjare, fortsättare och erfarna användare
- säkerhetskrav för dokumentation av projekt med motorer, reläer, batterier, externa laster och 5 V/3,3 V-blandning
- testfall för README, elevinstruktion, lärarhandledning, bokkapitel och dokumentation från ofullständigt material


Steg 11 definierar:

- inköps- och prisbedömningsregler för Arduino-projekt
- skillnaden mellan teknisk komponentlista och praktisk inköpslista
- hur GPT:n ska ge grova budgetbedömningar utan att låtsas känna till aktuella priser
- prisnivåer och kostnadsdrivare för vanliga Arduino-projekt
- två budgetscenarier: användaren har redan basutrustning eller behöver köpa allt från början
- regler för billigaste rimliga variant och robustare/lättare variant
- hur officiella Arduino-kort, kompatibla kort, ESP32 och ESP8266 ska värderas ur pris-, kvalitet- och nybörjarperspektiv
- när komponentkit är rimliga och när lösa delar är bättre
- kvalitetskontroller, söktermer och frakt/småorder-resonemang
- att säkerhetskritiska delar som drivsteg, motstånd, nivåanpassning och skyddsdioder aldrig får sparas bort
- testfall för budget, aktuella priser, inköpslistor, kit och kostnadsrisker

Steg 12 definierar:

- en färdig huvudinstruktion för GPT Builder
- en kortversion av huvudinstruktionen för begränsat instruktionsutrymme
- bindande prioriteringsordning mellan säkerhet, elektrisk rimlighet, nivå, budget och pedagogik
- hur huvudinstruktionen ska användas tillsammans med Knowledge-filerna
- krav på kopplingstabell, kod/koppling-matchning, säkerhetskontroll och tydliga antaganden
- regler för svenska som standardspråk, prisuppskattningar, dokumentation och felsökning
- självkontroll före byggbara svar
- testfall för att verifiera att huvudinstruktionen styr GPT:n korrekt


Steg 13 definierar:

- Knowledge-filstruktur för GPT Builder
- nytt Knowledge-index som karta över filerna
- ansvar och prioritet för varje Knowledge-fil
- vilka filer som bör användas för olika uppgiftstyper
- konfliktregler mellan säkerhet, komponentval, nivå, budget och dokumentationsformat
- namnstandard och rubrikstandard för framtida Knowledge-filer
- rekommendation för vilka filer som ska laddas upp i första MVP:n
- underhållsregler för kommande steg och filuppdelning

Steg 14 definierar:

- praktisk installationsguide för första MVP i GPT Builder
- rekommenderat GPT-namn och beskrivning
- exakt vilken huvudinstruktion som ska klistras in
- exakt vilka Knowledge-filer som ska laddas upp
- vilka projektfiler som inte ska laddas upp som Knowledge
- rekommenderade capabilities för webbsökning, bildgenerering, Code Interpreter och Actions
- första verifieringschecklista efter att GPT:n skapats
- definition av när MVP:n räknas som färdig
- avgränsning för vad som medvetet ligger utanför första MVP:n

## Föreslagen fortsatt ordning

Nästa steg enligt planen är:

1. Steg 15 – Skapa konversationsstartare
2. Steg 16 – Testa GPT:n med typfall
3. Steg 17 – Justera hallucinationsskydd
4. Steg 18 – Skapa intern granskningschecklista
5. Steg 19 – Skapa version 1 och använd den praktiskt

## Filstruktur

```text
arduino-gpt-project/
├── README.md
├── project-status.md
├── gpt-builder/
│   ├── README.md
│   ├── 01-installationsguide-mvp.md
│   ├── 02-uppladdningslista-knowledge.md
│   ├── 03-capabilities-och-installningar.md
│   └── 04-forsta-verifiering.md
├── gpt-instructions/
│   ├── 01-syfte-och-granser.md
│   ├── 02-malgrupper-och-nivaniva.md
│   ├── 03-fragemodell.md
│   ├── 04-leveransmallar.md
│   ├── 05-mikrokontroller-guide.md
│   ├── 06-komponentkatalog-mvp.md
│   ├── 07-kopplingsregler-och-sakerhet.md
│   ├── 08-kodstandard-arduino.md
│   ├── 09-ritnings-och-kopplingsstandard.md
│   ├── 10-dokumentationsstandard.md
│   ├── 11-inkops-och-prisbedomning.md
│   ├── 12-gpt-huvudinstruktion.md
│   ├── 13-knowledge-filstruktur.md
│   └── 14-bygg-mvp-i-gpt-builder.md
├── knowledge/
│   ├── 00-knowledge-index.md
│   ├── 01-roll-och-avgransning.md
│   ├── 02-malgrupper-och-nivaniva.md
│   ├── 03-fragemodell.md
│   ├── 04-leveransmallar.md
│   ├── 05-mikrokontroller-guide.md
│   ├── 06-komponentkatalog-mvp.md
│   ├── 07-kopplingsregler-och-sakerhet.md
│   ├── 08-kodstandard-arduino.md
│   ├── 09-ritnings-och-kopplingsstandard.md
│   ├── 10-dokumentationsstandard.md
│   ├── 11-inkops-och-prisbedomning.md
│   ├── 12-gpt-huvudinstruktion.md
│   └── 13-knowledge-filstruktur.md
├── notes/
│   ├── designbeslut-steg-01.md
│   ├── designbeslut-steg-02.md
│   ├── designbeslut-steg-03.md
│   ├── designbeslut-steg-04.md
│   ├── designbeslut-steg-05.md
│   ├── designbeslut-steg-06.md
│   ├── designbeslut-steg-07.md
│   ├── designbeslut-steg-08.md
│   ├── designbeslut-steg-09.md
│   ├── designbeslut-steg-10.md
│   ├── designbeslut-steg-11.md
│   ├── designbeslut-steg-12.md
│   ├── designbeslut-steg-13.md
│   └── designbeslut-steg-14.md
└── testfall/
    ├── testfall-steg-01.md
    ├── testfall-steg-02.md
    ├── testfall-steg-03.md
    ├── testfall-steg-04.md
    ├── testfall-steg-05.md
    ├── testfall-steg-06.md
    ├── testfall-steg-07.md
    ├── testfall-steg-08.md
    ├── testfall-steg-09.md
    ├── testfall-steg-10.md
    ├── testfall-steg-11.md
    ├── testfall-steg-12.md
    ├── testfall-steg-13.md
    └── testfall-steg-14.md
```

## Användning i kommande steg

I kommande steg kan dessa filer kompletteras, delas upp eller ersättas av mer detaljerade Knowledge-filer. `gpt-instructions/` innehåller utkast till bindande GPT-instruktioner. `knowledge/` innehåller mer utförliga underlag som lämpar sig som Knowledge-filer i en Custom GPT.


## SVG-generator v1.1-kompatibilitet

Paketet är uppdaterat för Circuit SVG Generator v1.1.

Det innebär att GPT:n kan skapa `circuit.yaml` för generatorns utökade stöd för fler boards och komponenttyper, bland annat Arduino Nano, Arduino Mega, NodeMCU ESP8266, Arduino Leonardo/Micro, Arduino Nano ESP32, BME280, HC-SR04, OLED I2C, MFRC522, DRV8833, PCA9685, logic level converter och fler vanliga moduler.

Den styrande filen är:

```text
knowledge/14-circuit-yaml-svg-generator.md
```

Knowledge-paketet innehåller nu 15 filer och ligger fortfarande under gränsen 20 filer.
