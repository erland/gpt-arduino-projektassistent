# Knowledge – Mikrokontroller-guide

Denna Knowledge-fil beskriver hur Arduino-projektassistenten ska resonera kring mikrokontrollerkort.

Guiden är avsedd som ett praktiskt beslutsstöd, inte som en fullständig databladssamling. Vid exakta elektriska gränsvärden ska GPT:n be användaren kontrollera aktuellt datablad eller officiell dokumentation.

## Övergripande beslutsmodell

Kortval ska alltid utgå från projektets behov, inte från vad som råkar vara mest populärt.

### Beslutsfrågor

1. Är användaren nybörjare, fortsättare eller avancerad?
2. Ska projektet vara breadboardvänligt och utan lödning?
3. Krävs WiFi eller Bluetooth?
4. Behövs många digitala pinnar?
5. Behövs många analoga ingångar?
6. Behövs PWM, servo, motorstyrning eller LED-styrning?
7. Behövs USB HID, alltså tangentbord/mus-funktion?
8. Är komponenterna 5 V, 3,3 V eller blandade?
9. Ska projektet drivas från USB, batteri eller extern strömförsörjning?
10. Är låg kostnad, enkelhet eller robusthet viktigast?

## Snabbval

| Situation | Rekommenderat förstahandsval | Kommentar |
|---|---|---|
| Första Arduino-projektet | Arduino Uno R3 eller Uno R4 Minima | Stort ekosystem, tydlig formfaktor, enkel att koppla |
| Billigt litet projekt | Arduino Nano eller Nano Every | Liten, breadboardvänlig, ofta billig |
| Många pinnar | Arduino Mega 2560 | Många I/O och flera seriella portar |
| WiFi/Bluetooth | ESP32 DevKit eller Arduino Nano ESP32 | Kraftfullt men kräver 3,3 V-tänk |
| Officiellt Arduino + IoT | Arduino Nano 33 IoT eller Nano ESP32 | Bra när officiellt ekosystem prioriteras |
| USB-tangentbord/mus | Arduino Leonardo eller Micro | ATmega32U4 kan agera USB-enhet |
| Permanent enkel 5 V-lösning | Arduino Nano-kompatibelt kort | Ofta mer praktiskt än Uno i färdigt bygge |
| Fristående lågkostnad | ATmega328P | Endast för mer avancerad användare |
| Mycket liten enkel funktion | ATtiny | Specialfall, inte MVP för nybörjare |

## Arduino Uno R3

### Profil

Arduino Uno R3 är ett mycket bra standardkort för nybörjare, utbildning och enkla 5 V-projekt.

### Typiska egenskaper

- Mikrokontroller: ATmega328P
- Logiknivå: 5 V
- Digitala I/O: 14, varav 6 med PWM
- Analoga ingångar: 6
- Klockfrekvens: 16 MHz
- Vanligt USB-B-format

### Välj när

- användaren är nybörjare
- projektet använder enkla komponenter som LED, knappar, buzzer, LDR, potentiometer och enklare sensorer
- tydlighet och robusthet är viktigare än låg kostnad eller liten storlek
- 5 V-kompatibilitet förenklar projektet

### Undvik när

- projektet behöver WiFi eller Bluetooth
- projektet behöver många pinnar
- projektet ska vara mycket litet
- projektet ska vara strömsnålt på batteri

### Vanliga fallgropar

- användaren försöker driva motorer eller reläer direkt från I/O-pinnar
- användaren tror att 5 V-pinnen kan driva stora laster
- användaren väljer Uno trots att projektet egentligen kräver trådlöst

## Arduino Uno R4 Minima

### Profil

Arduino Uno R4 Minima är en modernare Uno-variant med samma grundidé: enkel, robust Uno-formfaktor och 5 V-drift, men med kraftfullare 32-bitars mikrokontroller.

### Typiska egenskaper

- 5 V-drift och Uno-formfaktor
- 14 digitala I/O
- 6 analoga ingångar
- 48 MHz klockfrekvens
- mer minne än Uno R3
- USB-C

### Välj när

- användaren vill ha ett officiellt modernt Uno-kort
- projektet är nybörjarvänligt men kan ha nytta av mer minne eller snabbare processor
- 5 V-kompatibilitet är viktig

### Undvik när

- projektet kräver WiFi/Bluetooth och användaren inte vill lägga till separat modul
- äldre bibliotek eller shields måste fungera exakt som på Uno R3
- absolut lägsta pris är viktigast

### Vanliga fallgropar

- anta att alla äldre Uno R3-bibliotek fungerar utan kontroll
- blanda ihop Uno R4 Minima med Uno R4 WiFi
- tro att högre prestanda löser strömproblem för externa laster

## Arduino Nano klassisk

### Profil

Arduino Nano är i praktiken ett litet, breadboardvänligt alternativ till Uno för många enkla 5 V-projekt.

### Typiska egenskaper

- Mikrokontroller: ATmega328P
- Logiknivå: 5 V
- Liten formfaktor
- Breadboardvänlig
- liknar Uno i många programmeringsfall

### Välj när

- projektet ska byggas kompakt på breadboard eller perfboard
- användaren redan kan grunderna med Uno
- kostnad och storlek är viktigare än maximal fysisk robusthet

### Undvik när

- användaren är helt ny och behöver extra tydlig pin-layout
- projektet kräver WiFi/Bluetooth
- USB-drivrutiner för kloner kan bli ett problem

### Vanliga fallgropar

- olika Nano-kloner kan använda olika USB-seriekretsar
- små märkningar gör kopplingar svårare för nybörjare
- användaren kan råka välja fel kort/processor i Arduino IDE

## Arduino Nano Every

### Profil

Nano Every är en modernare Nano-liknande variant med liten formfaktor, låg kostnad och högre resurser än klassisk Nano.

### Typiska egenskaper

- Mikrokontroller: ATmega4809
- Liten Nano-formfaktor
- 20 MHz klockfrekvens
- 48 KB flash enligt Arduino-dokumentation

### Välj när

- liten formfaktor behövs
- användaren vill ha ett officiellt Arduino Nano-liknande kort
- projektet är enkelt till medelsvårt och inte kräver WiFi/Bluetooth

### Undvik när

- äldre AVR-specifika bibliotek måste fungera utan ändring
- användaren förväntar sig exakt samma beteende som klassisk Nano

### Vanliga fallgropar

- vissa äldre bibliotek kan anta ATmega328P
- pinout är lik men intern mikrokontroller skiljer sig från klassisk Nano

## Arduino Mega 2560

### Profil

Arduino Mega 2560 passar projekt där många pinnar behövs eller där flera seriella enheter ska kopplas in.

### Typiska egenskaper

- Mikrokontroller: ATmega2560
- Logiknivå: 5 V
- 54 digitala I/O
- 15 PWM-utgångar
- 16 analoga ingångar
- 4 hårdvaru-UART

### Välj när

- projektet har många knappar, LED, sensorer eller moduler
- flera seriella moduler ska användas samtidigt
- användaren vill slippa I/O-expander i första versionen

### Undvik när

- projektet är enkelt och bara behöver några få pinnar
- liten storlek är viktig
- WiFi/Bluetooth krävs utan separat modul
- budgeten är mycket låg

### Vanliga fallgropar

- välja Mega för att undvika att lära sig I2C-expander eller multiplexing
- driva många laster direkt från kortet
- anta att fler pinnar betyder mer tillgänglig ström

## Arduino Leonardo och Micro

### Profil

Leonardo och Micro bygger på ATmega32U4 och är särskilt intressanta när projektet ska kunna agera USB-tangentbord eller mus.

### Typiska egenskaper

- Mikrokontroller: ATmega32U4
- Logiknivå: normalt 5 V på klassiska Arduino-varianter
- inbyggd USB-funktion i mikrokontrollern
- kan användas för USB HID-projekt

### Välj när

- projektet ska agera tangentbord, mus eller annan USB-enhet
- användaren bygger makroknappar, spelkontroll eller specialinmatning

### Undvik när

- projektet inte behöver USB HID och Uno/Nano är enklare
- användaren är nybörjare och råkar skapa kod som stör tangentbord/mus-funktionen

### Vanliga fallgropar

- felaktig kod kan skicka oönskade tangenttryckningar till datorn
- seriell kommunikation beter sig inte alltid exakt som på Uno
- vissa shields eller exempel är skrivna med Uno i åtanke

## Arduino Nano 33 IoT

### Profil

Arduino Nano 33 IoT är ett officiellt Arduino-kort för uppkopplade projekt med WiFi/Bluetooth i Nano-format.

### Typiska egenskaper

- SAMD21-baserat kort
- WiFi/Bluetooth-modul
- IMU med accelerometer/gyroskop
- 3,3 V-logik
- liten formfaktor

### Välj när

- användaren vill ha officiellt Arduino-kort med IoT-stöd
- projektet behöver WiFi
- projektet kan byggas med 3,3 V-kompatibla komponenter
- IMU är relevant, till exempel rörelse- eller lutningsprojekt

### Undvik när

- projektet använder många 5 V-moduler utan nivåomvandling
- användaren är helt ny och inte behöver uppkoppling
- budgeten är mycket låg

### Vanliga fallgropar

- 3,3 V-logik gör att 5 V-signaler kan skada kortet
- användaren kan tro att Nano 33 IoT beter sig som klassisk 5 V-Nano
- bibliotek för AVR/Uno fungerar inte alltid direkt

## Arduino Nano ESP32

### Profil

Arduino Nano ESP32 kombinerar Arduino Nano-formfaktor med ESP32-S3-baserad funktionalitet, inklusive WiFi och Bluetooth.

### Typiska egenskaper

- ESP32-S3-baserat officiellt Arduino-kort
- WiFi och Bluetooth
- liten formfaktor
- 3,3 V-logik

### Välj när

- användaren vill ha ESP32-funktioner i officiell Arduino-form
- WiFi/Bluetooth behövs
- projektet behöver mer prestanda än Uno/Nano
- användaren vill hålla sig nära Arduino-ekosystemet

### Undvik när

- projektet är enkelt och pedagogisk tydlighet är viktigare än funktioner
- projektet använder 5 V-moduler utan tydlig nivåhantering
- lägsta pris är viktigast

### Vanliga fallgropar

- ESP32-pinnar har fler specialfall än Uno/Nano
- 3,3 V-logik kräver extra kontroll
- gamla Uno-exempel kan behöva ändras

## ESP32 DevKit/DevKitC-liknande kort

### Profil

ESP32 DevKit-kort är kraftfulla och billiga kort för projekt med WiFi, Bluetooth, webbgränssnitt, sensordata, IoT och mer avancerad styrning.

### Typiska egenskaper

- ESP32-familjen
- 3,3 V-logik
- WiFi och Bluetooth på många varianter
- många GPIO, men alla är inte lika lämpliga
- USB och 5 V-ingång på många utvecklingskort via regulator

### Välj när

- projektet behöver WiFi eller Bluetooth
- användaren vill bygga webbserver, IoT-nod, appstyrning eller trådlös sensor
- mer minne eller högre prestanda behövs
- användaren är minst nivå 2, eller får tydliga instruktioner

### Undvik när

- projektet är ett första LED/knapp-projekt utan trådlöst
- komponenterna är 5 V och användaren saknar nivåomvandling
- maximal kompatibilitet med klassiska Arduino-exempel krävs

### Vanliga fallgropar

- 5 V-signaler direkt in på ESP32-GPIO
- bootstrapping-pinnar belastas på fel sätt
- vissa pinnar är input-only på vissa ESP32-varianter
- ADC-beteende skiljer sig från Uno
- olika ESP32-kort har olika pinout
- servobibliotek och PWM fungerar annorlunda än på Uno

### Standardvarning

När GPT:n föreslår ESP32 ska den alltid nämna 3,3 V-logik och att 5 V-moduler kan kräva nivåomvandlare eller spänningsdelare på signalsidan.

## NodeMCU ESP8266

### Profil

NodeMCU ESP8266 är ett äldre men fortfarande vanligt WiFi-kort. Det kan passa enkla WiFi-projekt, men ESP32 är ofta ett bättre förstahandsval i nya projekt.

### Typiska egenskaper

- ESP8266-baserat utvecklingskort
- WiFi
- 3,3 V-logik
- färre pinnar än ESP32
- ofta märkt med D0, D1, D2 osv. i stället för rena GPIO-nummer

### Välj när

- användaren redan har ett NodeMCU-kort
- projektet bara behöver enkel WiFi
- få I/O-pinnar räcker
- låg kostnad är viktigt

### Undvik när

- många pinnar behövs
- Bluetooth behövs
- projektet ska vara lättast möjligt för nybörjare
- ESP32 finns tillgängligt till liknande pris

### Vanliga fallgropar

- D-nummer och GPIO-nummer blandas ihop
- 3,3 V-logik
- boot-pinnar påverkas av externa komponenter
- färre analoga möjligheter än många tror

## ATmega328P fristående

### Profil

ATmega328P är mikrokontrollern i klassiska Uno/Nano. Som fristående krets kan den användas för permanenta och billiga projekt, men är inte lämplig som första väg för nybörjare.

### Välj när

- projektet redan fungerar på Uno/Nano
- användaren vill bygga en permanent egen krets
- låg kostnad och enkel funktion är viktigt
- användaren förstår klocka, reset, programmering och strömförsörjning

### Undvik när

- användaren är nybörjare
- projektet fortfarande utvecklas
- USB-programmering och enkel felsökning behövs
- oscillator, bootloader eller programmerare saknas

### Vanliga fallgropar

- saknar bootloader eller programmeringsmetod
- fel klockinställning
- saknar avkopplingskondensatorer
- reset-koppling saknas eller är fel
- matningsspänning och klockfrekvens kombineras fel

## ATtiny som specialfall

### Profil

ATtiny-kretsar passar mycket små och enkla funktioner, till exempel blinkmönster, enkel sensorlogik eller små batteriprojekt. De är inte förstahandsval för GPT:ns MVP-projekt.

### Välj när

- projektet är mycket enkelt
- få pinnar räcker
- användaren är avancerad
- liten storlek och låg kostnad är viktigare än enkel utveckling

### Undvik när

- projektet kräver många bibliotek
- användaren behöver enkel USB-programmering
- flera moduler eller sensorer ska anslutas
- nybörjare bygger projektet

## Kortval utifrån nivåmodell

| Nivå | Passande kort | Kommentar |
|---|---|---|
| Nivå 0 | Uno R3/R4, eventuellt färdig Nano-labbmiljö | Vuxenstöd, enkel koppling, få komponenter |
| Nivå 1 | Uno R3/R4, Nano | Fokus på tydlighet och klassiska exempel |
| Nivå 2 | Nano, Mega, ESP32 med tydliga varningar | Fler moduler, display, servo, enklare IoT |
| Nivå 3 | ESP32, Nano 33 IoT, Nano ESP32, Mega, Leonardo/Micro | Mer avancerade projekt och kortspecifika detaljer |
| Nivå 4 | ATmega328P fristående, ATtiny, specialkort | Egen krets, optimering, batteri och permanenta byggen |

## Kortval utifrån projektkrav

### Om projektet kräver trådlöst

Föreslå i första hand ESP32 eller officiellt Arduino IoT-kort. Förklara att klassisk Uno/Nano kräver separat WiFi/Bluetooth-modul.

### Om projektet kräver många servon

Föreslå inte bara fler pinnar. Föreslå PCA9685 och separat servoström. Kortvalet kan vara Uno/Nano/ESP32 beroende på övriga krav.

### Om projektet kräver motorer

Kortval är sekundärt. Motordrivare och separat matning är viktigare. Föreslå DRV8833, L9110S eller annan lämplig drivare beroende på motor och ström.

### Om projektet kräver många knappar

Överväg:

- Mega 2560
- PCF8574/PCF8575
- knappmatris
- CD74HC4067

### Om projektet kräver display

Kortval beror på displaytyp:

- I2C OLED/LCD fungerar ofta med Uno/Nano/ESP32
- större TFT-displayer kan kräva mer minne och fler pinnar
- 5 V/3,3 V-kompatibilitet måste kontrolleras

## Standardformuleringar

### När Uno passar

> Jag skulle välja Arduino Uno här eftersom projektet är enklare att förstå med ett 5 V-kort, tydlig pin-layout och många exempel. Det är inte det billigaste kortet, men det minskar risken för nybörjarproblem.

### När Nano passar

> Jag skulle välja Arduino Nano om du vill bygga samma typ av projekt som med Uno men i mindre format. Det är bra på breadboard, men pinnamnen är mindre tydliga för helt nya användare.

### När ESP32 passar

> Jag skulle välja ESP32 eftersom projektet behöver WiFi/Bluetooth. Viktigt är att ESP32 använder 3,3 V-logik, så 5 V-signaler från vissa moduler får inte kopplas direkt till GPIO.

### När Mega passar

> Jag skulle välja Arduino Mega om huvudproblemet är många pinnar. Däremot löser Mega inte strömförsörjning för motorer, servon eller många LED; sådana laster behöver fortfarande rätt drivning.

### När Leonardo/Micro passar

> Jag skulle välja Leonardo eller Micro om kortet ska kunna agera tangentbord eller mus via USB. För vanliga sensor- och LED-projekt är Uno eller Nano oftast enklare.

## Källor och uppdateringsnotering

Denna guide bygger på stabila egenskaper från officiella Arduino- och Espressif-dokumentationer. Vid publicering eller användning i skarpa inköpsråd bör aktuella datablad kontrolleras.

Källor att kontrollera vid framtida uppdatering:

- Arduino Uno R3: https://docs.arduino.cc/hardware/uno-rev3
- Arduino Uno R4 Minima: https://docs.arduino.cc/hardware/uno-r4-minima
- Arduino Nano: https://docs.arduino.cc/hardware/nano
- Arduino Nano Every: https://docs.arduino.cc/hardware/nano-every
- Arduino Mega 2560: https://docs.arduino.cc/hardware/mega-2560/
- Arduino Leonardo: https://docs.arduino.cc/hardware/leonardo
- Arduino Nano 33 IoT: https://docs.arduino.cc/hardware/nano-33-iot
- Arduino Nano ESP32: https://docs.arduino.cc/nano-esp32
- ESP32 DevKitC: https://www.espressif.com/en/products/devkits/esp32-devkitc/overview
- Espressif ESP32 documentation: https://docs.espressif.com/
