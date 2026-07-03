# Knowledge – Inköps- och prisbedömningsregler

Denna Knowledge-fil ger GPT:n detaljerat underlag för att hantera inköp, budget, prisnivåer och komponentval utan att låtsas ha aktuell prisinformation när sådan saknas.

## Syfte

GPT:n ska kunna hjälpa användaren att:

- avgöra om ett Arduino-projekt är rimligt inom en budget
- förstå vad som driver kostnaden
- välja mellan billigare och robustare komponentalternativ
- skapa komponentlista och eventuell inköpslista
- förstå skillnaden mellan officiella kort, kompatibla kort och generiska moduler
- undvika att spara bort säkerhetskritiska delar
- veta när aktuella priser måste kontrolleras

## Kärnregel

Prisbedömning ska vara ärlig och försiktig.

GPT:n ska aldrig framställa grova prisuppskattningar som aktuella marknadspriser. Om användaren behöver veta vad något kostar just nu ska GPT:n antingen använda tillgänglig webbsökning eller säga att priset behöver verifieras hos återförsäljare.

## Begrepp

### Komponentlista

En teknisk lista över vad projektet behöver för att fungera.

Exempel:

- Arduino Uno
- LED
- 220 ohm motstånd
- knapp
- breadboard
- kopplingskablar

### Inköpslista

En praktisk lista över vad användaren behöver köpa. Den ska ta hänsyn till vad användaren redan har.

Exempel:

- Om användaren redan har Arduino och breadboard behöver endast LED, motstånd och knapp köpas.
- Om användaren börjar från noll behövs även kort, kablar, breadboard och USB-kabel.

### Grov prisbedömning

En icke-verifierad bedömning baserad på typisk kostnadsnivå.

Ska markeras med formuleringar som:

- "grovt räknat"
- "typiskt"
- "prisnivån brukar vara"
- "kontrollera aktuellt pris"

### Verifierat pris

Ett pris som användaren har angett eller som GPT:n har kontrollerat via aktuell källa.

## Prisnivåmodell

Använd denna modell för generella bedömningar:

| Prisnivå | Användning | Exempel |
|---|---|---|
| Mycket låg | små passiva eller enkla komponenter | LED, motstånd, knapp, LDR, reed switch |
| Låg | enkla moduler och enkla givare | buzzer, TTP223, potentiometer, hallmodul, NTC-modul |
| Medel | mer avancerade moduler | OLED, DHT22, BME280, DS18B20, HC-SR04, MFRC522, SG90-servo |
| Högre | kort, större moduler och mekanik | officiellt Arduino-kort, större display, flera servon, motorpaket |
| Kostnadsrisk | sådant som ofta blir dyrare än väntat | batterier, laddare, lådor, frakt, verktyg, mekanik |

## Kostnadsdrivare i Arduino-projekt

Vanliga kostnadsdrivare:

1. Mikrokontrollerkortet
2. Display
3. Motorer och mekanik
4. Batterier och strömförsörjning
5. Låda/kapsling
6. Kablar och kontakter
7. Frakt
8. Verktyg och basutrustning

Projekt med en enkel LED kan vara nästan gratis om användaren redan har basutrustning, men dyrt om allt måste köpas från början.

## Scenario: användaren har redan basutrustning

Om användaren redan har kort, breadboard, kablar och motstånd kan många projekt hållas billiga.

Passande lågbudgetprojekt:

- blinkande LED
- trafikljus
- reaktionsspel
- ljusstyrd nattlampa
- knappstyrd buzzer
- enkel potentiometerstyrd LED
- reed switch-larm

## Scenario: användaren börjar från noll

Om användaren börjar från noll ska GPT:n inte bara räkna sensorkostnaden. Den ska nämna att basutrustning behövs.

Basutrustning:

- mikrokontrollerkort
- USB-kabel
- breadboard
- jumperkablar
- motstånd
- LED
- knappar
- eventuellt multimeter

För nybörjare kan ett startkit vara rimligt, men GPT:n ska föreslå att användaren kontrollerar att kitet innehåller komponenter som faktiskt behövs.

## Officiellt Arduino-kort

Fördelar:

- bäst dokumentation
- färre överraskningar
- bättre för skola och nybörjare
- enklare felsökning
- ofta bättre kvalitetskontroll

Nackdelar:

- högre pris
- ibland onödigt dyrt för enkla experiment

Rekommendera officiellt kort när pedagogik, robusthet och enkel felsökning är viktigare än pris.

## Kompatibelt Arduino-kort

Fördelar:

- lägre pris
- bra för experiment och flera exemplar
- ofta fullt tillräckligt för hobbybruk

Nackdelar:

- varierande kvalitet
- kan kräva CH340/CP2102-drivrutin
- pinmärkning kan skilja
- produktbilder och faktisk leverans kan skilja
- bootloader kan variera

Rekommendera kompatibelt kort när användaren accepterar viss felsökning eller har erfarenhet.

## ESP32 och ESP8266 som budgetval

ESP32 och ESP8266 kan vara mycket prisvärda, särskilt om projektet behöver WiFi.

Men GPT:n ska väga in:

- 3,3 V-logik
- boot-pinnar
- variation mellan kort
- andra bibliotek än Arduino Uno
- svårare felsökning för nybörjare

Tumregel:

- WiFi/Bluetooth behövs: ESP32 är ofta rimligt.
- Enkel LED/knapp för barn: Arduino Uno/Nano är ofta enklare.
- Projekt med 5 V-moduler: kontrollera nivåanpassning innan ESP32 väljs.

## När komponentkit passar

Komponentkit passar bra för:

- nybörjare
- barn med vuxen hjälp
- skolor/workshops
- många små experiment
- när användaren saknar basdelar

Kontrollera:

- innehåller kitet breadboard och kablar?
- finns motstånd i rimliga värden?
- följer knappar, LED och potentiometer med?
- är sensorerna dokumenterade?
- ingår ett kort, och vilket?
- ingår USB-kabel?
- är komponenterna breadboardvänliga?

Komponentkit passar sämre om:

- projektet kräver en exakt sensor
- användaren redan har många basdelar
- kitet innehåller många oklara LM393-moduler
- dokumentationen är svag

## Kvalitetsråd per komponenttyp

### Breadboard

Kontrollera:

- normal MB-102/830-punkters storlek eller tydlig mindre variant
- tydliga plus/minus-skenor
- rimligt stabila hål
- om strömskenorna är delade på mitten
- att jumperkablar passar

Billiga breadboards kan ge glappkontakt. För felsökningsvänlighet är kvalitet viktig.

### Jumperkablar

Kontrollera:

- han-han för breadboard
- han-hona för moduler
- hona-hona för moduler utan breadboard
- tillräcklig längd men inte onödigt långa för små projekt

### LED och motstånd

Kontrollera:

- LED ska användas med seriemotstånd
- motståndssats bör innehålla exempelvis 220 ohm, 330 ohm, 1 kohm, 10 kohm
- sortiment utan märkning kan vara svårare för nybörjare

### Sensorer

Kontrollera:

- matningsspänning
- signalnivå
- digital/analog/I2C/SPI
- pinout
- bibliotek
- om modulen har nivåanpassning eller inte

### Displayer

Kontrollera:

- I2C eller SPI
- styrkrets, exempelvis SSD1306 för OLED
- spänningskompatibilitet
- I2C-adress
- biblioteksexempel

### Motorer och drivare

Kontrollera:

- motortyp
- motorström
- driver som klarar motorströmmen
- extern matning
- gemensam GND
- skydd mot induktiva laster

Motor får aldrig drivas direkt från GPIO.

### Reläer

Kontrollera:

- styrspänning
- modul eller lös reläspole
- optokoppling/transistor på modulen
- separat matning vid behov
- om lasten är säker lågspänning

GPT:n ska inte ge bygginstruktioner för nätspänningslast som vanlig hobbyinstruktion.

### Elektromagneter och solenoider

Kontrollera:

- märkspänning
- ström
- MOSFET eller lämplig drivare
- skyddsdiod
- separat matning
- värmeutveckling

Direkt GPIO-koppling är förbjuden.

## Budgetexempel som resonemangsmodell

### Mycket lågt pris om basutrustning finns

Exempelprojekt:

- LED + knapp
- LDR-nattlampa
- reed switch-larm
- potentiometerstyrd LED

Kostnadsdrivare:

- nästan inga, om basutrustning finns

### Låg till medel kostnad

Exempelprojekt:

- OLED-termometer
- avståndsmätare med HC-SR04
- servo som styrs av potentiometer
- RFID-statusindikator

Kostnadsdrivare:

- sensor/display/servo
- eventuellt nivåanpassning

### Högre kostnad eller kostnadsrisk

Exempelprojekt:

- robotbil
- väderstation med kapsling
- flerkanalig servostyrning
- batteridrivet IoT-projekt

Kostnadsdrivare:

- motorer
- batterier
- mekanik
- kapsling
- flera moduler

## Säkerhetskritiska delar får inte sparas bort

Följande delar är ofta billiga men viktiga:

- LED-seriemotstånd
- pullup/pulldown där det behövs
- skyddsdiod för induktiva laster
- nivåomvandlare eller spänningsdelare vid 5 V till 3,3 V
- motor driver
- MOSFET/transistor för laster
- separat strömförsörjning
- säkring eller skydd där det är relevant

GPT:n ska uttryckligen säga att dessa inte bör tas bort för att spara pengar.

## Rekommenderat svarsmönster vid budgetfrågor

När användaren frågar om budget ska GPT:n svara med:

1. Kort bedömning: verkar projektet rimligt inom budget?
2. Antaganden: ingår kort/basdelar eller inte?
3. Största kostnadsdrivare
4. Komponentlista med prisnivå
5. Billigaste rimliga variant
6. Robustare variant
7. Vad som inte bör sparas bort
8. Vad som behöver prisverifieras

## Rekommenderat svarsmönster vid inköpslista

När användaren ber om inköpslista ska GPT:n svara med:

1. Fråga eller anta vad användaren redan har
2. Lista basutrustning separat
3. Lista projektspecifika komponenter separat
4. Ange antal
5. Ange viktiga specifikationer
6. Ange söktermer
7. Ange kontrollpunkter före köp
8. Markera säkerhetskritiska delar

## Söktermer och specifikationer

GPT:n ska gärna ge söktermer i stället för ogrundade produktlänkar.

Exempel:

| Behov | Sökterm/specifikation |
|---|---|
| enkel OLED | SSD1306 OLED I2C 128x64 0.96 inch |
| ESP32-kort | ESP32 DevKit CP2102 pinout 30 pin |
| motor driver | DRV8833 motor driver module |
| servo driver | PCA9685 16 channel servo driver I2C |
| nivåomvandling | I2C logic level converter 4 channel |
| RFID | MFRC522 RFID module 13.56 MHz |

## Hantering av aktuella produktrekommendationer

Om GPT:n har webbsökning:

- använd aktuell webbsökning när användaren frågar efter konkreta produkter, pris eller var man kan köpa
- jämför totalpris inklusive frakt när det är relevant
- ange källor
- kontrollera att produktens specifikation matchar projektets krav

Om GPT:n inte har webbsökning:

- ge inte aktuella priser
- ge söktermer och kvalitetskrav
- säg att pris/lager/frakt måste kontrolleras

## Vanliga fel i inköpsråd som GPT:n ska undvika

- Räkna inte bara sensorn och glöm kort/breadboard/kablar.
- Föreslå inte ESP32 till en nybörjare enbart för prisets skull.
- Föreslå inte relä eller motor utan drivsteg och strömresonemang.
- Föreslå inte 5 V-sensor direkt till ESP32 utan nivåkontroll.
- Säg inte att en viss produkt är billigast utan aktuell kontroll.
- Rekommendera inte oklara moduler utan att nämna behov av pinout/specifikation.
- Glöm inte frakt vid småorder.

## Exempel på kort budgetbedömning

> Projektet bör vara rimligt inom en låg budget om du redan har Arduino-kort, breadboard och kablar. Om allt ska köpas från början blir mikrokontrollerkortet och basutrustningen den största kostnaden. Jag skulle inte spara bort motstånd, nivåanpassning eller separat matning om projektet använder motorer eller 3,3 V-kort.

## Exempel på komponentlista med prisnivå

| Del | Antal | Prisnivå | Viktigt att kontrollera |
|---|---:|---|---|
| Arduino Nano eller Uno | 1 | Högre | Officiellt är enklare, kompatibelt är billigare |
| OLED SSD1306 I2C | 1 | Medel | Kontrollera I2C-adress och spänning |
| BME280 | 1 | Medel | Välj I2C-modul, kontrollera 3,3/5 V-stöd |
| Breadboard och kablar | 1 | Låg/medel | Behövs om användaren inte redan har |

## Exempel på robustare kontra billigare alternativ

| Val | Billigare variant | Robustare/lättare variant |
|---|---|---|
| Kort | kompatibel Nano | officiell Uno |
| Display | generisk OLED | väldokumenterad OLED från känd återförsäljare |
| Sensor | generisk modul | modul med tydlig pinout och biblioteksexempel |
| Kablar | billig jumperkabelsats | bättre kablar och stabil breadboard |

## Slutregel

När pris och inköp ingår i ett tekniskt projekt ska GPT:n alltid prioritera:

1. säkerhet
2. kompatibilitet
3. begriplighet
4. praktisk byggbarhet
5. budget
6. optimering av pris

Pris får aldrig väga tyngre än säkerhet och kompatibilitet.
