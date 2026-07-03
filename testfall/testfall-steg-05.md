# Testfall – Steg 5: Mikrokontroller-guide

Dessa testfall används för att verifiera att GPT:n väljer mikrokontrollerkort på ett konsekvent, pedagogiskt och säkert sätt.

## Testfall 5.1 – Första nybörjarprojektet

### Prompt

```text
Jag vill bygga mitt första Arduino-projekt med en LED, en knapp och kanske en buzzer. Vilket kort ska jag köpa?
```

### Förväntat beteende

GPT:n bör rekommendera Arduino Uno R3/R4 eller eventuellt Nano om liten formfaktor är viktig.

GPT:n bör inte välja ESP32 som förstahandsval eftersom WiFi/Bluetooth inte behövs.

### Kontrollpunkter

- nämner enkelhet och pedagogik
- nämner 5 V-fördel
- ger Nano som alternativ
- undviker onödigt avancerat kort

## Testfall 5.2 – WiFi-projekt

### Prompt

```text
Jag vill bygga en temperatursensor som visar värdet på en webbsida i mobilen. Ska jag använda Arduino Uno eller ESP32?
```

### Förväntat beteende

GPT:n bör rekommendera ESP32 eller officiellt Arduino IoT-kort.

### Kontrollpunkter

- motiverar WiFi-behovet
- varnar för 3,3 V-logik
- nämner att Uno kräver separat WiFi-modul
- kopplar kortvalet till sensorval och nivåomvandling

## Testfall 5.3 – Många knappar

### Prompt

```text
Jag vill bygga en kontrollpanel med 35 knappar och några LED. Vilket Arduino-kort passar?
```

### Förväntat beteende

GPT:n bör föreslå Arduino Mega eller I/O-expander/knappmatris beroende på nivå och byggsätt.

### Kontrollpunkter

- nämner Mega som enkelt alternativ
- nämner PCF8574/PCF8575 eller knappmatris som alternativ
- förklarar att många LED kan kräva strömplanering

## Testfall 5.4 – USB-tangentbord

### Prompt

```text
Jag vill bygga egna makroknappar som datorn uppfattar som ett tangentbord. Kan jag använda Arduino Uno?
```

### Förväntat beteende

GPT:n bör rekommendera Leonardo/Micro eller annat ATmega32U4-baserat kort.

### Kontrollpunkter

- säger att Uno normalt inte är rätt val för USB HID
- förklarar varför Leonardo/Micro passar
- varnar för att fel kod kan skicka oönskade tangenttryckningar

## Testfall 5.5 – ESP32 och 5 V-sensor

### Prompt

```text
Jag har en ESP32 och en 5V ultraljudssensor. Är det bara att koppla echo till en GPIO?
```

### Förväntat beteende

GPT:n ska varna för att 5 V-signal inte ska kopplas direkt till ESP32-GPIO utan kontroll/nivåomvandling.

### Kontrollpunkter

- nämner 3,3 V-logik
- föreslår spänningsdelare eller nivåomvandlare
- nämner gemensam GND
- ger inte en riskabel direktkoppling

## Testfall 5.6 – Permanent lågkostnadsprojekt

### Prompt

```text
Jag har byggt ett projekt på Arduino Uno och vill göra det billigare och permanent. Ska jag använda en lös ATmega328P?
```

### Förväntat beteende

GPT:n bör säga att ATmega328P fristående kan passa men är avancerat.

### Kontrollpunkter

- föreslår Nano-kompatibelt kort som enklare mellanväg
- nämner bootloader/programmering/klocka/reset
- rekommenderar inte fristående ATmega till nybörjare utan förbehåll

## Testfall 5.7 – Många servon

### Prompt

```text
Jag vill styra 12 små servon. Borde jag använda Arduino Mega för att få fler pinnar?
```

### Förväntat beteende

GPT:n bör förklara att huvudfrågan inte bara är pinnar utan servostyrning och strömförsörjning.

### Kontrollpunkter

- nämner PCA9685
- nämner separat servoström
- nämner gemensam GND
- säger att Mega kan vara ett alternativ men inte löser strömproblemet

## Testfall 5.8 – Oklart kortnamn

### Prompt

```text
Jag har ett blått ESP-kort med 30 pinnar. Kan jag följa Arduino Uno-kopplingen?
```

### Förväntat beteende

GPT:n bör be användaren identifiera kortet eller läsa märkning, men samtidigt ge generella ESP32/ESP8266-varningar.

### Kontrollpunkter

- antar inte exakt pinout
- nämner 3,3 V-logik
- varnar för pin-skillnader
- ber om märkning/foto/pinout vid behov
