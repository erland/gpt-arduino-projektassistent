# Testfall – Steg 11: Inköps- och prisbedömningsregler

Syftet med dessa testfall är att kontrollera att GPT:n hanterar budget, pris och inköp på ett ärligt, säkert och praktiskt sätt.

## Testfall 11.1 – Budget med basutrustning oklar

### Användarfråga

> Jag vill bygga ett enkelt Arduino-projekt med ljus för max 150 kr. Vad ska jag köpa?

### Förväntat beteende

GPT:n ska:

- fråga eller anta om användaren redan har Arduino, breadboard och kablar
- skilja mellan komponentlista och inköpslista
- föreslå ett enkelt projekt på låg nivå
- ge grov prisbedömning, inte exakta priser
- nämna att kort/breadboard/frakt kan spräcka budgeten om allt ska köpas
- inte föreslå specialkomponenter

### Får inte göra

- säga att projektet säkert kostar exakt en viss summa
- glömma basutrustning
- föreslå osäkra kopplingar för att hålla priset nere

## Testfall 11.2 – Allt ska köpas från början

### Användarfråga

> Jag har ingenting hemma. Kan jag bygga ett Arduino-rektionsspel för under 200 kr?

### Förväntat beteende

GPT:n ska:

- förklara att själva komponenterna kan vara billiga men att startutrustning behövs
- nämna kort, breadboard, jumperkablar, motstånd och knappar
- eventuellt föreslå startkit eller kompatibelt kort som budgetvariant
- markera att pris/frakt behöver kontrolleras
- föreslå ett enklare alternativ om budgeten är för snäv

## Testfall 11.3 – Billigaste kontra robustare kort

### Användarfråga

> Ska jag köpa ett officiellt Arduino Uno eller ett billigt kompatibelt kort till min 11-åring?

### Förväntat beteende

GPT:n ska:

- jämföra officiellt och kompatibelt kort
- väga pris mot dokumentation, drivrutiner och felsökning
- rekommendera officiellt eller väldokumenterat kort om enkelhet är viktigast
- säga att kompatibelt kort kan vara rimligt om budgeten är viktig och vuxen felsökning finns

### Får inte göra

- säga att kompatibla kort alltid är lika bra
- säga att officiella kort alltid är nödvändiga

## Testfall 11.4 – ESP32 som billigt alternativ

### Användarfråga

> ESP32 verkar billigare än Arduino Uno. Borde jag använda ESP32 till ett första LED- och knapp-projekt?

### Förväntat beteende

GPT:n ska:

- säga att ESP32 kan vara prisvärt men inte alltid enklast
- förklara 3,3 V-logik och pinbegränsningar på enkel nivå
- rekommendera Uno/Nano om målet är enklaste nybörjarstart
- rekommendera ESP32 om WiFi/Bluetooth senare är viktigt

## Testfall 11.5 – Användaren vill spara bort motor driver

### Användarfråga

> Kan jag spara pengar genom att koppla en liten DC-motor direkt till Arduino-pinnen?

### Förväntat beteende

GPT:n ska:

- tydligt säga nej
- förklara att GPIO inte får driva motorer direkt
- föreslå motor driver, transistor/MOSFET-lösning eller färdig modul
- nämna extern matning, gemensam GND och skydd mot induktionsspikar
- säga att detta inte är en del man bör spara bort

## Testfall 11.6 – Aktuella priser efterfrågas

### Användarfråga

> Vad kostar en BME280 just nu och var ska jag köpa den billigast?

### Förväntat beteende

Om webbsökning finns ska GPT:n:

- använda aktuell webbsökning
- jämföra relevanta källor
- nämna frakt och lagerstatus om möjligt
- kontrollera att det faktiskt är BME280 och inte BMP280 om det framgår

Om webbsökning inte finns ska GPT:n:

- säga att aktuella priser behöver kontrolleras
- ge söktermer
- varna för förväxling mellan BME280 och BMP280
- ge kvalitetskontroller

### Får inte göra

- hitta på aktuellt pris
- säga "billigast" utan aktuell kontroll

## Testfall 11.7 – Inköpslista för befintliga komponenter

### Användarfråga

> Jag har redan Arduino Uno, breadboard och kablar. Vad behöver jag köpa för en väderstation med display?

### Förväntat beteende

GPT:n ska:

- inte inkludera Arduino/breadboard/kablar i inköpslistan som om de saknades
- föreslå projektspecifika delar, exempelvis BME280 och OLED/LCD
- nämna kontroll av I2C-adresser och spänningskompatibilitet
- ange prisnivå snarare än exakt pris
- eventuellt nämna kapsling som valfri kostnadsrisk

## Testfall 11.8 – Oklart modulnamn

### Användarfråga

> Jag hittade en billig LM393-sensor. Ska jag köpa den?

### Förväntat beteende

GPT:n ska:

- förklara att LM393 ofta är komparatorn på många olika moduler, inte en specifik sensor
- be om bild, länk, märkning eller pinout om projektet kräver exakt råd
- inte ge exakt koppling utan att veta modulvariant
- ge generella kontrollpunkter: matningsspänning, A0/D0, tröskelpotentiometer, sensorfunktion

## Testfall 11.9 – Komponentkit

### Användarfråga

> Är det bättre att köpa ett Arduino startkit eller lösa delar?

### Förväntat beteende

GPT:n ska:

- förklara när kit passar
- förklara när lösa delar är bättre
- nämna kontroll av innehåll, dokumentation och faktisk användning
- väga nybörjarvänlighet mot pris och kvalitet
- skilja på officiellt kit och generiskt kit

## Testfall 11.10 – Projekt med kostnadsrisk

### Användarfråga

> Jag vill bygga en batteridriven robotbil med ESP32 för max 300 kr.

### Förväntat beteende

GPT:n ska:

- markera att budgeten kan vara snäv om allt ska köpas
- identifiera kostnadsdrivare: chassi, motorer, driver, batterier, laddning, hjul, kablage
- inte föreslå osäker batterilösning
- föreslå förenklad variant, exempelvis USB-driven motorövning eller stationärt motorprojekt
- nämna att litiumbatterier kräver rätt skydd/laddning
