# Designbeslut – Steg 5

## Steg

**Steg 5 – Skapa mikrokontroller-guide**

## Syfte

Syftet med steg 5 är att ge GPT:n en tydlig beslutsmodell för att välja mikrokontrollerkort i Arduino-baserade projekt.

Detta steg ska minska risken att GPT:n slentrianmässigt föreslår Arduino Uno eller ESP32 utan att analysera projektets behov.

## Viktiga designbeslut

### 1. Kortval ska vara behovsstyrt

GPT:n ska välja kort utifrån projektkrav, användarnivå, komponenter och säkerhet.

Det valda kortet ska inte vara det mest avancerade kortet, utan det enklaste kortet som löser uppgiften på ett bra sätt.

### 2. Arduino Uno/Nano är standard för enkla nybörjarprojekt

För projekt utan trådlöst, utan många pinnar och utan särskilda prestandakrav är Uno eller Nano oftast bäst.

Skälet är pedagogik, 5 V-kompatibilitet och mängden exempel.

### 3. ESP32 ska väljas för trådlöst, inte av slentrian

ESP32 är kraftfullt och billigt men innebär fler fallgropar:

- 3,3 V-logik
- boot-pinnar
- varierande pinout
- annan PWM/ADC-hantering än Uno
- större risk för nybörjarförvirring

Därför ska ESP32 främst väljas när WiFi, Bluetooth, mer prestanda eller specifika ESP32-funktioner behövs.

### 4. Mega löser pinbrist men inte strömproblem

Arduino Mega ska rekommenderas när många pinnar eller flera seriella portar behövs. GPT:n ska dock alltid förklara att Mega inte gör det säkert att driva många laster direkt från kortet.

### 5. Leonardo/Micro ska kopplas till USB HID

Leonardo och Micro ska framför allt lyftas fram när projektet behöver tangentbords- eller musfunktion via USB.

### 6. Fristående ATmega och ATtiny är avancerade alternativ

Dessa ska inte rekommenderas till nybörjare. De passar först när användaren vill gå från prototyp till permanent egen krets och kan hantera programmering, klocka, reset och strömförsörjning.

### 7. Guiden är praktisk, inte fullständig databladssamling

Knowledge-filen innehåller praktiska beslutsregler och typiska egenskaper. Vid exakta elektriska gränsvärden ska GPT:n hänvisa till datablad eller be användaren kontrollera modulens specifikation.

## Påverkan på kommande steg

Steg 6, komponentkatalogen, bör knyta varje komponent till lämpliga kort och varningar, särskilt:

- 5 V kontra 3,3 V
- behov av nivåomvandling
- motorer och servon
- I2C/SPI/UART
- kortspecifika pinvarningar för ESP32/ESP8266

Steg 7 bör komplettera med mer bindande kopplings- och säkerhetsregler.
