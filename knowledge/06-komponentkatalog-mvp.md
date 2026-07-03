# 06 – Komponentkatalog MVP

## Syfte

Denna Knowledge-fil ger Arduino-projektassistenten en första kontrollerad komponentkatalog. Målet är att GPT:n ska kunna välja vanliga komponenter på ett säkert, pedagogiskt och praktiskt sätt utan att hitta på ogrundade egenskaper.

Katalogen är inte en komplett databladssamling. Den ska användas för projektförslag, komponentval, kopplingstabeller, kodval och felsökning på hobby- och utbildningsnivå.

## Grundregel

När GPT:n föreslår en komponent ska den kontrollera:

1. Om komponenten passar användarens nivå.
2. Om komponenten passar valt mikrokontrollerkort.
3. Om spänning och logiknivå är rimliga.
4. Om komponenten kräver motstånd, drivsteg, extern matning, nivåomvandlare eller skyddsdiod.
5. Om projektet bör förenklas.
6. Om komponenten kräver särskilt bibliotek eller särskild kodmodell.
7. Om komponenten är breadboardvänlig eller kräver lödning/modul.

Om något är oklart ska GPT:n skriva antagandet tydligt och föreslå att användaren kontrollerar märkning/datablad/modulens produktbeskrivning.

## Komponentpostens standardformat

Varje komponent bör beskrivas enligt följande modell:

```text
Komponent:
Kategori:
Typisk användning:
Lämplig nivå:
Typisk spänning:
Signaltyp:
Passar Arduino Uno/Nano 5 V:
Passar ESP32/ESP8266 3,3 V:
Kräver extra skydd/kringkomponenter:
Vanliga bibliotek:
Vanliga fallgropar:
Bra projektidéer:
Undvik när:
Kommentar:
```

GPT:n behöver inte skriva ut hela modellen till användaren, men ska använda den internt när den väljer komponenter.

---

# A. Grundkomponenter

## LED

**Kategori:** ljus/indikering  
**Typisk användning:** visa status, blink, enkel utgång, PWM-dimning  
**Lämplig nivå:** 0–1  
**Typisk spänning:** beror på färg, men kopplas normalt via seriemotstånd  
**Signaltyp:** digital utgång eller PWM  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ja, med rätt motstånd och begränsad ström  
**Kräver extra skydd/kringkomponenter:** seriemotstånd, typiskt 220–1 000 ohm beroende på spänning och önskad ljusstyrka  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- kopplas utan motstånd
- anod/katod vänds fel
- för hög ström från GPIO
- otydlig skillnad mellan långt och kort ben

**Bra projektidéer:** blinkande LED, trafikljus, reaktionsspel, statusindikator  
**Undvik när:** många starka LED ska drivas direkt från mikrokontrollern  
**Kommentar:** För nybörjare bör GPT:n alltid ange långt ben/anod och kort ben/katod.

## RGB LED

**Kategori:** ljus/färg  
**Typisk användning:** färgindikering, stämningsljus, spelstatus  
**Lämplig nivå:** 1–2  
**Typisk spänning:** 5 V eller 3,3 V beroende på koppling och motstånd  
**Signaltyp:** tre digitala/PWM-utgångar  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ja, med rätt motstånd  
**Kräver extra skydd/kringkomponenter:** ett seriemotstånd per färgkanal  
**Vanliga bibliotek:** inga för enkel PWM  
**Vanliga fallgropar:**

- gemensam anod och gemensam katod blandas ihop
- endast ett motstånd används för alla färger
- färgerna hamnar på fel pinnar

**Bra projektidéer:** humörlampa, temperaturfärg, spelindikator  
**Undvik när:** användaren är nivå 0 och saknar vuxenstöd  
**Kommentar:** GPT:n ska fråga eller ange antagande om RGB-LED är common cathode eller common anode.

## Motstånd

**Kategori:** passiv komponent  
**Typisk användning:** strömbegränsning, spänningsdelare, pullup/pulldown  
**Lämplig nivå:** 0–4  
**Typisk spänning:** beror på koppling  
**Signaltyp:** passiv  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ja  
**Kräver extra skydd/kringkomponenter:** nej  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- fel resistansvärde
- glömda LED-motstånd
- spänningsdelare dimensioneras utan hänsyn till signal och last

**Bra projektidéer:** nästan alla nybörjarprojekt  
**Undvik när:** inte relevant  
**Kommentar:** GPT:n bör föreslå vanliga värden som 220 ohm, 330 ohm, 1 kΩ, 4,7 kΩ och 10 kΩ beroende på sammanhang.

## Knapp / tryckknapp

**Kategori:** input  
**Typisk användning:** start, stopp, meny, reaktionstest  
**Lämplig nivå:** 0–1  
**Typisk spänning:** samma logiknivå som kortet  
**Signaltyp:** digital ingång  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ja  
**Kräver extra skydd/kringkomponenter:** normalt inte om intern pullup används  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- flytande ingång utan pullup/pulldown
- knappens fyra ben missförstås på breadboard
- logiken blir aktiv låg när INPUT_PULLUP används
- studs/debounce ignoreras i projekt där det spelar roll

**Bra projektidéer:** reaktionsspel, räknare, startknapp, hemlig kod  
**Undvik när:** användaren behöver robust industriell input  
**Kommentar:** För nybörjare bör GPT:n prioritera `INPUT_PULLUP` och koppla knappen mellan pinne och GND.

## Potentiometer

**Kategori:** analog input  
**Typisk användning:** vred, ljusstyrka, hastighet, menyvärde  
**Lämplig nivå:** 1  
**Typisk spänning:** 5 V på Arduino Uno/Nano, 3,3 V på ESP32/ESP8266  
**Signaltyp:** analog ingång  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ja, men mata inte potentiometern med 5 V om utsignalen går till ESP32/ESP8266  
**Kräver extra skydd/kringkomponenter:** normalt inte  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- ytterben och mittben blandas ihop
- 5 V-signal skickas till 3,3 V-ingång
- ESP32 ADC-värden beter sig inte exakt som Arduino Uno

**Bra projektidéer:** dimmer, servovred, tonkontroll, inställningsratt  
**Undvik när:** mycket exakt mätning behövs  
**Kommentar:** GPT:n ska alltid anpassa matningsspänningen till mikrokontrollerns analogingång.

## LDR / fotomotstånd

**Kategori:** ljussensor  
**Typisk användning:** mäta ljus/mörker  
**Lämplig nivå:** 1  
**Typisk spänning:** 5 V eller 3,3 V beroende på kort  
**Signaltyp:** analog ingång via spänningsdelare  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ja, om spänningsdelaren matas med 3,3 V  
**Kräver extra skydd/kringkomponenter:** fast motstånd, ofta cirka 10 kΩ, som spänningsdelare  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- LDR kopplas direkt utan spänningsdelare
- tröskelvärden hårdkodas utan kalibrering
- varierande ljusmiljö ger oväntade värden

**Bra projektidéer:** nattlampa, ljusmätare, skymningssensor  
**Undvik när:** exakt lux-mätning krävs  
**Kommentar:** GPT:n bör beskriva att värdena behöver testas och justeras i den aktuella miljön.

---

# B. Ljud och enkel interaktion

## Aktiv buzzer

**Kategori:** ljud  
**Typisk användning:** pip, alarm, feedback  
**Lämplig nivå:** 1  
**Typisk spänning:** ofta 3,3–5 V beroende på modul  
**Signaltyp:** digital utgång på/av  
**Passar Arduino Uno/Nano 5 V:** ja om buzzern klarar 5 V  
**Passar ESP32/ESP8266 3,3 V:** ofta ja om modulen fungerar vid 3,3 V  
**Kräver extra skydd/kringkomponenter:** ibland transistor om den drar mer ström än GPIO bör leverera  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- aktiv och passiv buzzer blandas ihop
- för hög ström från GPIO
- polaritet ignoreras på polariserad buzzer

**Bra projektidéer:** timer, reaktionsspel, enkel larmsignal  
**Undvik när:** toner/melodier krävs  
**Kommentar:** Aktiv buzzer piper när den får spänning och behöver normalt inte `tone()`.

## Passiv buzzer / piezo

**Kategori:** ljud  
**Typisk användning:** toner, melodier, ljudfeedback  
**Lämplig nivå:** 1–2  
**Typisk spänning:** 3,3–5 V beroende på komponent  
**Signaltyp:** frekvenssignal/PWM-liknande  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ja, men kod och tone-stöd kan skilja  
**Kräver extra skydd/kringkomponenter:** ibland seriemotstånd eller transistor beroende på buzzer/modul  
**Vanliga bibliotek:** `tone()` på Arduino AVR, ESP32 kan kräva annan lösning beroende på miljö  
**Vanliga fallgropar:**

- passiv buzzer behandlas som aktiv buzzer
- ESP32-kod använder Arduino Uno-specifika antaganden
- ljudet blir svagt eller distorderat

**Bra projektidéer:** melodispelare, Simon Says, enkel dörrklocka  
**Undvik när:** hög ljudvolym krävs  
**Kommentar:** GPT:n ska skilja tydligt mellan aktiv och passiv buzzer.

## TTP223 touch-sensor

**Kategori:** touch-input/modul  
**Typisk användning:** beröringsknapp  
**Lämplig nivå:** 1–2  
**Typisk spänning:** ofta 2–5,5 V beroende på modul  
**Signaltyp:** digital utgång  
**Passar Arduino Uno/Nano 5 V:** ofta ja  
**Passar ESP32/ESP8266 3,3 V:** ofta ja  
**Kräver extra skydd/kringkomponenter:** normalt inte  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- modulens output-läge kan vara momentary eller toggle beroende på lödbryggor
- känslighet påverkas av montering och omgivning
- oklar matningsspänning på vissa moduler

**Bra projektidéer:** touch-lampa, hemlig knapp, interaktiv låda  
**Undvik när:** robust vädertålig knapp krävs  
**Kommentar:** GPT:n ska ange att modulens läge kan variera och bör testas.

---

# C. Sensorer

## DHT11/DHT22

**Kategori:** temperatur/fuktighet  
**Typisk användning:** enkel väder-/rumsmätning  
**Lämplig nivå:** 1–2  
**Typisk spänning:** ofta 3,3–5 V beroende på sensor/modul  
**Signaltyp:** digital enledar-liknande signal  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ofta ja  
**Kräver extra skydd/kringkomponenter:** pullup kan behövas om det inte är en modul med inbyggt motstånd  
**Vanliga bibliotek:** DHT sensor library  
**Vanliga fallgropar:**

- DHT11 och DHT22 blandas ihop i koden
- avläsning sker för ofta
- saknad pullup på naken sensor
- låg noggrannhet jämfört med mer avancerade sensorer

**Bra projektidéer:** rumstermometer, enkel väderstation, fuktlarm  
**Undvik när:** snabb eller exakt mätning krävs  
**Kommentar:** GPT:n bör föreslå BME280 när användaren vill ha en mer komplett och ofta stabilare miljösensor.

## BME280

**Kategori:** miljösensor  
**Typisk användning:** temperatur, luftfuktighet, lufttryck  
**Lämplig nivå:** 2  
**Typisk spänning:** många breakout-moduler stödjer 3,3–5 V, men sensorkretsen är 3,3 V; kontrollera modul  
**Signaltyp:** I2C eller SPI, oftast I2C i nybörjarprojekt  
**Passar Arduino Uno/Nano 5 V:** ja med modul som har regulator/nivåanpassning, annars krävs försiktighet  
**Passar ESP32/ESP8266 3,3 V:** ja  
**Kräver extra skydd/kringkomponenter:** normalt inte på färdig modul, men I2C-nivåer måste kontrolleras  
**Vanliga bibliotek:** Adafruit BME280, Adafruit Unified Sensor  
**Vanliga fallgropar:**

- BME280 förväxlas med BMP280 som saknar luftfuktighet
- I2C-adress kan vara 0x76 eller 0x77
- 5 V I2C till 3,3 V-sensor utan nivåanpassning

**Bra projektidéer:** väderstation, datalogger, inomhusklimat  
**Undvik när:** användaren behöver absolut billigaste sensor  
**Kommentar:** GPT:n ska fråga eller ange antagande om modulen är BME280 och inte BMP280.

## DS18B20

**Kategori:** temperatur  
**Typisk användning:** temperaturmätning, även vattentåliga probvarianter  
**Lämplig nivå:** 2  
**Typisk spänning:** 3,0–5,5 V beroende på sensorvariant  
**Signaltyp:** 1-Wire  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ja  
**Kräver extra skydd/kringkomponenter:** pullup, ofta 4,7 kΩ mellan data och VCC  
**Vanliga bibliotek:** OneWire, DallasTemperature  
**Vanliga fallgropar:**

- saknad pullup
- fel pinout mellan TO-92 och vattentät prob
- parasitic power används utan att användaren förstår begränsningarna

**Bra projektidéer:** termometer, vattentemperatur, frys-/kylövervakning  
**Undvik när:** mycket snabb temperaturrespons krävs  
**Kommentar:** För nybörjare bör GPT:n föreslå normal treledarkoppling, inte parasitic power.

## HC-SR04 ultraljudssensor

**Kategori:** avstånd  
**Typisk användning:** mäta avstånd till objekt  
**Lämplig nivå:** 1–2  
**Typisk spänning:** klassisk HC-SR04 används ofta med 5 V  
**Signaltyp:** digital trigger/echo-puls  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** endast med försiktighet; Echo från 5 V-sensor kan behöva nivådelare/nivåomvandlare  
**Kräver extra skydd/kringkomponenter:** nivådelare på Echo till 3,3 V-kort om sensorn matas med 5 V  
**Vanliga bibliotek:** NewPing eller egen pulseIn-kod  
**Vanliga fallgropar:**

- Echo 5 V kopplas direkt till ESP32/ESP8266
- dåliga mätningar på mjuka eller vinklade ytor
- sensorn används för mycket korta eller mycket långa avstånd

**Bra projektidéer:** avståndsmätare, parkeringssensor, robot som undviker hinder  
**Undvik när:** hög precision eller tillförlitlig säkerhetsmätning krävs  
**Kommentar:** GPT:n ska alltid varna för Echo-nivån när ESP32/ESP8266 används.

## PIR-sensor

**Kategori:** rörelse/närvaro  
**Typisk användning:** upptäcka rörelse från människor/djur  
**Lämplig nivå:** 1–2  
**Typisk spänning:** ofta 5 V på vanliga HC-SR501-moduler, men utgång kan ofta läsas av 3,3 V-kort; kontrollera modul  
**Signaltyp:** digital utgång  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ofta ja på signalnivå, men kontrollera modulens utgång  
**Kräver extra skydd/kringkomponenter:** normalt inte  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- uppvärmningstid ignoreras
- känslighet och delay-potentiometrar missförstås
- sensor reagerar på värmerörelser, inte all rörelse

**Bra projektidéer:** nattlampa, rörelselarm, automatisk belysning  
**Undvik när:** exakt positionsdetektering krävs  
**Kommentar:** GPT:n bör förklara att PIR inte ser objekt, utan förändringar i infraröd värmestrålning.

## Reed switch / reedkontakt

**Kategori:** magnetkontakt  
**Typisk användning:** dörr/fönster, magnetdetektering  
**Lämplig nivå:** 1  
**Typisk spänning:** logiknivå från kortet  
**Signaltyp:** digital ingång  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ja  
**Kräver extra skydd/kringkomponenter:** pullup/pulldown, ofta intern pullup räcker  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- flytande ingång
- glasröret är ömtåligt om det är en lös reedkontakt
- kontaktstuds kan förekomma

**Bra projektidéer:** dörrsensor, magneträknare, enkel säkerhetsindikator på hobbynivå  
**Undvik när:** hög ström ska brytas eller säkerhetskritisk låsning behövs  
**Kommentar:** För nybörjare är reedmodul enklare än lös glaskomponent.

## Hall sensor / Hall-modul

**Kategori:** magnetdetektering  
**Typisk användning:** detektera magnet, varvtal, position  
**Lämplig nivå:** 2  
**Typisk spänning:** beror på sensor/modul, ofta 3,3–5 V för moduler  
**Signaltyp:** digital och/eller analog beroende på modul  
**Passar Arduino Uno/Nano 5 V:** ofta ja  
**Passar ESP32/ESP8266 3,3 V:** ofta ja om modulen stödjer 3,3 V  
**Kräver extra skydd/kringkomponenter:** normalt inte på modul  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- digital Hall-switch och analog Hall-sensor blandas ihop
- LM393-moduler kräver tröskeljustering
- magnetens polaritet och avstånd påverkar resultat

**Bra projektidéer:** varvräknare, magneträknare, positionssensor  
**Undvik när:** användaren inte kan identifiera om modulen är analog eller digital  
**Kommentar:** GPT:n ska fråga eller ange antagande om sensorn är analog, digital eller LM393-baserad modul.

## KY-037 / mikrofonmodul med LM393

**Kategori:** ljudsensor/modul  
**Typisk användning:** upptäcka ljudnivå/klapp, inte spela in ljud  
**Lämplig nivå:** 2  
**Typisk spänning:** ofta 3,3–5 V beroende på modul  
**Signaltyp:** digital tröskel och ibland analog nivå  
**Passar Arduino Uno/Nano 5 V:** ofta ja  
**Passar ESP32/ESP8266 3,3 V:** ofta ja om modulen stödjer 3,3 V, kontrollera analog utgångsnivå  
**Kräver extra skydd/kringkomponenter:** normalt inte  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- förväntas ge tydligt ljudinnehåll, men ger bara nivå/tröskel
- trimpot måste justeras
- brus och omgivningsljud ger falska triggningar

**Bra projektidéer:** klappstyrd LED, ljudindikator  
**Undvik när:** röstigenkänning eller ljudinspelning krävs  
**Kommentar:** GPT:n ska tydligt säga att modulen inte är lämplig för avancerad ljudanalys.

## APDS-9960 / GY-9960

**Kategori:** gest/färg/närhet/ljus  
**Typisk användning:** geststyrning, närhet, färg- och ljusmätning  
**Lämplig nivå:** 3  
**Typisk spänning:** sensorkrets är normalt 3,3 V; breakout-moduler varierar  
**Signaltyp:** I2C  
**Passar Arduino Uno/Nano 5 V:** endast med modul som stödjer 5 V-logik eller med nivåomvandling  
**Passar ESP32/ESP8266 3,3 V:** ja, om I2C-pinnar väljs rätt  
**Kräver extra skydd/kringkomponenter:** eventuell nivåomvandling för 5 V-kort  
**Vanliga bibliotek:** Adafruit APDS9960 eller motsvarande  
**Vanliga fallgropar:**

- 5 V I2C kopplas till 3,3 V-sensor utan skydd
- gestigenkänning fungerar dåligt på fel avstånd
- biblioteksexempel förväntas fungera utan kalibrering

**Bra projektidéer:** geststyrd lampa, beröringsfri meny  
**Undvik när:** nybörjarprojekt med låg budget  
**Kommentar:** GPT:n bör föreslå enklare alternativ, till exempel knapp, TTP223 eller HC-SR04, om användaren är nybörjare.

---

# D. Displayer och visning

## OLED I2C 0,96 tum, ofta SSD1306

**Kategori:** display  
**Typisk användning:** visa text, värden, enkla symboler  
**Lämplig nivå:** 2  
**Typisk spänning:** många moduler stödjer 3,3–5 V, men kontrollera modul  
**Signaltyp:** I2C  
**Passar Arduino Uno/Nano 5 V:** ofta ja med modul som stödjer 5 V  
**Passar ESP32/ESP8266 3,3 V:** ja  
**Kräver extra skydd/kringkomponenter:** normalt inte på färdig modul, men I2C-nivåer ska kontrolleras  
**Vanliga bibliotek:** Adafruit SSD1306, U8g2  
**Vanliga fallgropar:**

- fel I2C-adress, ofta 0x3C eller 0x3D
- displaystorlek i koden matchar inte modulen
- minnesbegränsning på små AVR-kort vid grafik

**Bra projektidéer:** väderstation, avståndsmätare, meny, spelstatus  
**Undvik när:** användaren vill ha mycket stor text eller färg utan att byta displaytyp  
**Kommentar:** GPT:n ska ange bibliotek och I2C-adress som något användaren kan behöva justera.

## LCD1602 med I2C-backpack

**Kategori:** display  
**Typisk användning:** enkel textvisning 16x2 tecken  
**Lämplig nivå:** 2  
**Typisk spänning:** ofta 5 V  
**Signaltyp:** I2C  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ofta problematiskt om modulen kräver 5 V och I2C-pullups går till 5 V; kräver kontroll/nivåomvandling  
**Kräver extra skydd/kringkomponenter:** eventuell nivåomvandling för 3,3 V-kort  
**Vanliga bibliotek:** LiquidCrystal_I2C  
**Vanliga fallgropar:**

- fel I2C-adress, ofta 0x27 eller 0x3F
- kontrastpotentiometer är feljusterad
- 5 V I2C pullups till ESP32/ESP8266

**Bra projektidéer:** enkel klocka, termometer, statuspanel  
**Undvik när:** projektet använder ESP32 och användaren vill slippa nivåproblem; OLED kan vara enklare  
**Kommentar:** GPT:n bör varna tydligt för I2C-nivåer med 3,3 V-kort.

## TM1637 4-siffrig display

**Kategori:** sifferdisplay  
**Typisk användning:** timer, räknare, poäng, klocka  
**Lämplig nivå:** 2  
**Typisk spänning:** ofta 3,3–5 V beroende på modul  
**Signaltyp:** tvåtråds digital modul, inte standard-I2C  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ofta ja, kontrollera modul  
**Kräver extra skydd/kringkomponenter:** normalt inte  
**Vanliga bibliotek:** TM1637Display  
**Vanliga fallgropar:**

- misstas för vanlig I2C
- CLK/DIO kopplas omvänt
- ljusstyrka ställs inte in

**Bra projektidéer:** reaktionstid, timer, räknare, poängtavla  
**Undvik när:** fri text eller grafik krävs  
**Kommentar:** Bra när projektet bara behöver visa siffror.

## MAX7219 LED-matris / 7-segmentdrivare

**Kategori:** LED-display/drivare  
**Typisk användning:** LED-matris, flera 7-segmentsiffror  
**Lämplig nivå:** 2–3  
**Typisk spänning:** ofta 5 V  
**Signaltyp:** SPI-liknande seriell styrning  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ofta möjligt, men kontrollera modul och logiknivåer  
**Kräver extra skydd/kringkomponenter:** extern ström kan behövas för många moduler  
**Vanliga bibliotek:** LedControl, MD_MAX72XX, MD_Parola  
**Vanliga fallgropar:**

- för många moduler drivs från kortets 5 V
- DIN/CS/CLK blandas ihop
- orientering på matrisen blir fel

**Bra projektidéer:** textskylt, enkel animation, poängtavla  
**Undvik när:** mycket strömsnål batteridrift krävs  
**Kommentar:** GPT:n ska uppmärksamma strömförbrukning vid flera LED-moduler.

---

# E. Motorer, rörelse och laster

## SG90 mikroservo

**Kategori:** motor/rörelse  
**Typisk användning:** liten arm, pekare, lucka, enkel mekanik  
**Lämplig nivå:** 2  
**Typisk spänning:** ofta 5 V  
**Signaltyp:** servosignal via digital pinne/timer/PWM-liknande styrning  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ja, men bibliotek och PWM-hantering kan skilja  
**Kräver extra skydd/kringkomponenter:** separat 5 V-matning rekommenderas vid last eller flera servon; gemensam GND krävs  
**Vanliga bibliotek:** Servo.h på Arduino AVR, ESP32Servo eller motsvarande för ESP32  
**Vanliga fallgropar:**

- servo drivs från Arduino 5 V trots hög belastning
- ingen gemensam GND mellan servo och kort
- mekanisk ändläge belastar servot
- ESP32-kod använder Servo.h utan kontroll av stöd

**Bra projektidéer:** servo-lås på hobbynivå, pekarinstrument, liten robotarm  
**Undvik när:** tung mekanik eller säkerhetskritiskt lås krävs  
**Kommentar:** GPT:n ska alltid nämna gemensam GND och extern matning när det är relevant.

## DC-motor

**Kategori:** motor/rörelse  
**Typisk användning:** hjul, fläkt, liten mekanik  
**Lämplig nivå:** 2  
**Typisk spänning:** varierar, ofta 3–12 V  
**Signaltyp:** kräver drivsteg; styrs ofta med PWM och riktning  
**Passar Arduino Uno/Nano 5 V:** ja via motor driver, aldrig direkt från GPIO  
**Passar ESP32/ESP8266 3,3 V:** ja via motor driver som accepterar 3,3 V-logik  
**Kräver extra skydd/kringkomponenter:** motor driver, separat matning, gemensam GND, störningshänsyn  
**Vanliga bibliotek:** ofta inga, styrs med digitalWrite/analogWrite eller plattformens PWM  
**Vanliga fallgropar:**

- motor kopplas direkt till GPIO
- motor drivs från mikrokontrollerns 5 V-pin utan marginal
- saknad gemensam GND
- drivsteg klarar inte motorströmmen

**Bra projektidéer:** enkel bil, fläktstyrning, hastighetsstyrning  
**Undvik när:** användaren saknar motor driver eller extern matning  
**Kommentar:** GPT:n ska aldrig föreslå direktdrivning från GPIO.

## DRV8833 motor driver

**Kategori:** motordrivare  
**Typisk användning:** små DC-motorer eller vissa små stegmotorer  
**Lämplig nivå:** 2–3  
**Typisk spänning:** lågspänningsmotorer, modulens specifikation måste kontrolleras  
**Signaltyp:** digital riktning/PWM  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ofta ja eftersom många DRV8833-moduler accepterar 3,3 V-logik, kontrollera modul  
**Kräver extra skydd/kringkomponenter:** separat motormatning, gemensam GND, avkoppling rekommenderas  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- motorströmmen överskrider modulen
- standby/sleep-pin glöms på vissa moduler
- motor supply och logic supply blandas ihop

**Bra projektidéer:** liten robotbil, motorstyrning med joystick  
**Undvik när:** stora motorer eller 12 V/hög ström krävs utan specifikationskontroll  
**Kommentar:** GPT:n bör föreslå DRV8833 framför äldre L298N för små lågspänningsmotorer när det passar.

## L9110S motor driver

**Kategori:** motordrivare  
**Typisk användning:** små DC-motorer i enkla hobbyprojekt  
**Lämplig nivå:** 2  
**Typisk spänning:** beror på modul, ofta för små lågspänningsmotorer  
**Signaltyp:** digital riktning/PWM  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ofta möjligt, men kontrollera modul  
**Kräver extra skydd/kringkomponenter:** separat motormatning och gemensam GND  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- används till för stor motor
- oklart hur IN-pinnarna styr riktning/broms
- spänningsfall och låg effektivitet missförstås

**Bra projektidéer:** mycket enkel motorstyrning, liten fläkt, liten bil  
**Undvik när:** bättre effektivitet eller mer robust motorstyrning krävs  
**Kommentar:** GPT:n bör nämna att DRV8833 ofta är ett modernare alternativ.

## ULN2003 + 28BYJ-48 stegmotor

**Kategori:** stegmotor/drivare  
**Typisk användning:** långsam positionsstyrning, visare, små mekaniska projekt  
**Lämplig nivå:** 2–3  
**Typisk spänning:** ofta 5 V för vanliga kit  
**Signaltyp:** flera digitala utgångar via ULN2003-drivkort  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ofta möjligt, kontrollera drivkort och logiknivåer  
**Kräver extra skydd/kringkomponenter:** separat 5 V-matning rekommenderas, gemensam GND  
**Vanliga bibliotek:** Stepper, AccelStepper  
**Vanliga fallgropar:**

- motorn drivs från mikrokontrollern utan tillräcklig ström
- sekvensen eller pinnordningen blir fel
- förväntas vara snabb/stark

**Bra projektidéer:** pekare, liten vridplattform, enkel mekanisk indikator  
**Undvik när:** hög hastighet eller stort vridmoment krävs  
**Kommentar:** GPT:n ska förklara att denna stegmotor är långsam men pedagogisk.

## Relämodul

**Kategori:** switch/laststyrning  
**Typisk användning:** slå av/på separat last på hobbynivå  
**Lämplig nivå:** 3, endast lågspänning i denna GPT:s standardläge  
**Typisk spänning:** ofta 5 V relämodul, men varierar  
**Signaltyp:** digital styrsignal  
**Passar Arduino Uno/Nano 5 V:** ja om relämodulen är kompatibel  
**Passar ESP32/ESP8266 3,3 V:** endast om modulen accepterar 3,3 V styrsignal, annars behövs drivning/anpassning  
**Kräver extra skydd/kringkomponenter:** färdig relämodul bör ha drivtransistor och skyddsdiod; extern lastmatning krävs; lågspänningsgräns ska hållas  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- nätspänning används av nybörjare
- relämodulen kräver mer ström än kortet kan ge
- active low/active high missförstås
- COM/NO/NC kopplas fel

**Bra projektidéer:** lågspänningslampa, separat 5–12 V-last på bänk  
**Undvik när:** 230 V, säkerhetskritisk brytning, hög ström eller okänd last  
**Kommentar:** GPT:n ska inte ge praktiska kopplingssteg för nätspänning. Föreslå lågspänningsalternativ eller färdiga certifierade lösningar.

## MOSFET-modul / logic-level MOSFET

**Kategori:** transistorstyrning/laststyrning  
**Typisk användning:** LED-strip, motor, solenoid, elektromagnet, annan DC-last  
**Lämplig nivå:** 3  
**Typisk spänning:** lastspänning beror på last och MOSFET-modul  
**Signaltyp:** digital/PWM till gate/modulingång  
**Passar Arduino Uno/Nano 5 V:** ja med logic-level MOSFET  
**Passar ESP32/ESP8266 3,3 V:** endast med MOSFET/modul som fungerar fullt vid 3,3 V gate-signal  
**Kräver extra skydd/kringkomponenter:** skyddsdiod för induktiv last, gemensam GND, rätt strömtålighet, säkring kan behövas  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- MOSFET är inte logic-level
- 3,3 V gate räcker inte
- induktiv last saknar flyback-diod
- lastströmmen överskrider modulens kapacitet

**Bra projektidéer:** LED-strip dimmer, liten elektromagnet med skydd, DC-laststyrning  
**Undvik när:** användaren inte kan ange lastens spänning och ström  
**Kommentar:** GPT:n ska fråga efter lastdata innan den ger konkret koppling för MOSFET-lösningar.

## Elektromagnet / solenoid / spole

**Kategori:** induktiv last  
**Typisk användning:** magnetlås på hobbynivå, slagpinne, enkel aktivering  
**Lämplig nivå:** 3–4  
**Typisk spänning:** varierar, ofta 5–12 V eller mer  
**Signaltyp:** styrs via MOSFET/transistor/drivare, aldrig direkt från GPIO  
**Passar Arduino Uno/Nano 5 V:** ja som styrning via drivsteg  
**Passar ESP32/ESP8266 3,3 V:** ja som styrning via 3,3 V-kompatibelt drivsteg  
**Kräver extra skydd/kringkomponenter:** MOSFET/transistor, extern matning, flyback-diod, gemensam GND, kontroll av ström och värme  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- kopplas direkt till GPIO
- saknar flyback-diod
- drar för mycket ström
- blir varm vid kontinuerlig drift
- används som säkerhetskritiskt lås

**Bra projektidéer:** kort aktiverad magnet på labbnivå, enkel demonstrator  
**Undvik när:** säkerhetskritiska lås, hög ström, okänd spole, barnprojekt utan vuxenstöd  
**Kommentar:** GPT:n ska vara restriktiv och alltid kräva lastdata före konkret dimensionering.

---

# F. Kommunikations- och identifieringsmoduler

## MFRC522 RFID

**Kategori:** RFID/NFC-läsare  
**Typisk användning:** läsa RFID-taggar/kort  
**Lämplig nivå:** 2–3  
**Typisk spänning:** 3,3 V  
**Signaltyp:** SPI  
**Passar Arduino Uno/Nano 5 V:** ja men modulen ska normalt matas med 3,3 V och signalnivåer bör hanteras försiktigt; många hobbykopplingar fungerar men det är en riskpunkt  
**Passar ESP32/ESP8266 3,3 V:** ja, ofta lämpligare logiknivåmässigt  
**Kräver extra skydd/kringkomponenter:** eventuell nivåomvandling från 5 V-kort beroende på modul och robusthetskrav  
**Vanliga bibliotek:** MFRC522  
**Vanliga fallgropar:**

- matas med 5 V trots 3,3 V-modul
- SPI-pinnar blandas ihop
- används som verkligt säkerhetslås trots låg säkerhetsnivå
- RFID-taggar/kort av fel typ används

**Bra projektidéer:** hobbylåda, närvaromarkering, spel med kort/taggar  
**Undvik när:** verklig åtkomstkontroll eller säkerhet krävs  
**Kommentar:** GPT:n ska beskriva RFID-lösningar som hobby-/lärprojekt, inte säkerhetslösningar.

## I2C Logic Level Converter

**Kategori:** nivåomvandling  
**Typisk användning:** koppla 5 V-kort till 3,3 V-I2C-moduler eller tvärtom  
**Lämplig nivå:** 2–3  
**Typisk spänning:** två sidor, exempelvis HV 5 V och LV 3,3 V  
**Signaltyp:** främst I2C/tvåriktade långsamma signaler beroende på modul  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ja  
**Kräver extra skydd/kringkomponenter:** korrekt HV/LV-matning och gemensam GND  
**Vanliga bibliotek:** inga  
**Vanliga fallgropar:**

- HV och LV kopplas fel
- GND glöms
- används för signaler den inte passar för
- onödig om modulen redan har nivåanpassning

**Bra projektidéer:** 5 V Arduino + 3,3 V I2C-sensor, blandade modulspänningar  
**Undvik när:** signalhastighet/protokoll inte passar modulen  
**Kommentar:** GPT:n ska använda nivåomvandlare som säker standard när 5 V och 3,3 V I2C blandas och modulens skydd är oklart.

## PCA9685 PWM/servo-driver

**Kategori:** PWM-expander/servodrivning  
**Typisk användning:** många servon eller PWM-kanaler  
**Lämplig nivå:** 3  
**Typisk spänning:** logik ofta 3,3–5 V beroende på modul; servomatning separat  
**Signaltyp:** I2C  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ja, kontrollera I2C-nivåer  
**Kräver extra skydd/kringkomponenter:** separat servomatning, gemensam GND, tillräcklig ström  
**Vanliga bibliotek:** Adafruit PWM Servo Driver  
**Vanliga fallgropar:**

- tror att PCA9685 själv matar servon
- servomatning saknar tillräcklig ström
- gemensam GND saknas
- I2C-adresskonflikt

**Bra projektidéer:** robotarm, flera servon, ljusstyrning med många kanaler  
**Undvik när:** bara ett servo behövs i nybörjarprojekt  
**Kommentar:** GPT:n bör föreslå PCA9685 först när antalet servon/PWM-kanaler motiverar det.

## PCF8574 / PCF8575 I/O-expander

**Kategori:** digital I/O-expansion  
**Typisk användning:** fler digitala in-/utgångar via I2C  
**Lämplig nivå:** 3  
**Typisk spänning:** 3,3 eller 5 V beroende på system och modul  
**Signaltyp:** I2C  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ja om modulen/I2C-nivåer är 3,3 V-kompatibla  
**Kräver extra skydd/kringkomponenter:** kontroll av I2C-pullups och ström per pinne  
**Vanliga bibliotek:** PCF8574-bibliotek eller Wire  
**Vanliga fallgropar:**

- förväntas driva hög ström
- I2C-adresser krockar
- kvasi-bidirektionellt beteende missförstås
- 5 V pullups till 3,3 V-kort

**Bra projektidéer:** många knappar, LED-statuspanel med låg ström, enkel I/O-expansion  
**Undvik när:** snabba signaler, PWM eller hög ström krävs  
**Kommentar:** GPT:n ska inte använda PCF8574 som ersättning för motor-/LED-drivare vid högre ström.

## CD74HC4067 analog/digital multiplexer

**Kategori:** multiplexer  
**Typisk användning:** läsa många analoga eller digitala signaler med färre pinnar  
**Lämplig nivå:** 3  
**Typisk spänning:** samma logiknivå som systemet; kontrollera variant/modul  
**Signaltyp:** analog eller digital signalväxling  
**Passar Arduino Uno/Nano 5 V:** ja  
**Passar ESP32/ESP8266 3,3 V:** ja om matad och använd på 3,3 V-nivå  
**Kräver extra skydd/kringkomponenter:** signalerna får inte överskrida matningsspänningen  
**Vanliga bibliotek:** inga eller mux-bibliotek  
**Vanliga fallgropar:**

- används för signaler utanför matningsnivå
- förväntas fungera som isolerad switch för laster
- adresspinnar kopplas fel
- signaler läcker/stör vid hög impedans

**Bra projektidéer:** många potentiometrar, många sensorer, enkel kontrollpanel  
**Undvik när:** hög ström, snabba signaler eller isolering krävs  
**Kommentar:** GPT:n ska förklara att multiplexer inte ger fler samtidiga analoga ingångar, utan växlar mellan dem.

---

# G. Förstärkning och ljudutgång

## LM386 förstärkarmodul

**Kategori:** ljudförstärkare  
**Typisk användning:** driva liten högtalare från ljudsignal  
**Lämplig nivå:** 3  
**Typisk spänning:** ofta 5–12 V beroende på modul  
**Signaltyp:** analog ljudsignal in, högtalare ut  
**Passar Arduino Uno/Nano 5 V:** kan användas för enklare tonutgång via lämplig signal/koppling  
**Passar ESP32/ESP8266 3,3 V:** kan användas, men kräver lämplig ljudsignal och nivå  
**Kräver extra skydd/kringkomponenter:** kontroll av modul, matning och högtalare; ibland kopplingskondensatorer beroende på modul  
**Vanliga bibliotek:** beror på ljudgenerering  
**Vanliga fallgropar:**

- förväntas ge hög ljudkvalitet
- matningsbrus ger störningar
- högtalare kopplas direkt till mikrokontroller i stället för förstärkare

**Bra projektidéer:** enkel ljudgenerator, tonprojekt med högtalare  
**Undvik när:** hög ljudkvalitet, stark ljudvolym eller batterisnål drift krävs  
**Kommentar:** För enklare projekt är passiv buzzer ofta bättre än LM386.

---

# H. Valregler per projekttyp

## Nybörjarprojekt nivå 0–1

Prioritera:

- LED
- knapp
- potentiometer
- LDR
- aktiv buzzer
- enkel RGB LED om användaren är nivå 1
- TTP223 om touch är temat

Undvik normalt:

- motorer
- reläer
- elektromagneter
- RFID om målgruppen är mycket ung
- komplexa I2C/SPI-moduler
- ESP32 om WiFi/Bluetooth inte behövs

## Projekt nivå 2

Lämpliga komponenter:

- OLED I2C
- DHT22
- BME280
- DS18B20
- HC-SR04
- PIR
- servo SG90
- TM1637
- MFRC522 med tydliga varningar
- DRV8833/L9110S för små motorer

Kräver extra tydlighet kring:

- bibliotek
- extern matning
- 3,3 V/5 V
- I2C-adresser
- gemensam GND

## Projekt nivå 3–4

Lämpliga komponenter:

- PCA9685
- PCF8574/PCF8575
- CD74HC4067
- MOSFET-modul
- elektromagnet/solenoid med strikta krav
- APDS-9960
- LM386
- fristående ATmega/ATtiny

Kräver ofta:

- specifikationskontroll
- separat strömförsörjning
- skyddsdioder
- nivåomvandling
- mer avancerad felsökning

---

# I. Standardvarningar som GPT:n ska använda

## GPIO och laster

GPT:n ska aldrig föreslå att motorer, reläspolar, elektromagneter, solenoider, högtalare eller LED-strips drivs direkt från en GPIO-pinne.

## 3,3 V och 5 V

När ESP32 eller ESP8266 används ska GPT:n kontrollera om någon modul kan skicka 5 V till kortets ingångar. Om det är oklart ska GPT:n föreslå nivådelare eller nivåomvandlare.

## Extern matning

Motorer, flera servon, LED-strips, relämoduler och elektromagneter ska behandlas som externa laster. GPT:n ska nämna separat matning och gemensam GND när det är relevant.

## Induktiva laster

Reläer, motorer, solenoider och elektromagneter kan skapa spänningsspikar. GPT:n ska kräva drivsteg och skydd, exempelvis flyback-diod för DC-spolar om skydd inte redan finns i färdig modul.

## Moduler med okänd märkning

Om användaren nämner en modul med oklart namn, exempelvis endast `LM393`, ska GPT:n inte anta exakt funktion. LM393 är en komparator som förekommer på många olika sensormoduler. GPT:n ska fråga vilken modul det gäller eller ge alternativa tolkningar.

---

# J. Pris- och tillgänglighetsnivåer

Denna fil innehåller inte aktuella priser. GPT:n får använda ungefärliga kostnadsnivåer:

- **Mycket låg:** motstånd, LED, knapp, LDR
- **Låg:** buzzer, potentiometer, reedkontakt, TTP223
- **Medel:** OLED, DHT22, BME280, DS18B20, servo, PIR, HC-SR04, TM1637
- **Högre:** officiella Arduino-kort, flera servon, motorer med drivare, större displayer
- **Risk för dyrt projekt:** batterier, låda, mekanik, många LED, flera motorer, färdiga robusta moduler

Om användaren kräver aktuella priser ska GPT:n säga att priser måste kontrolleras mot butik eller använda webbsökning om sådan är tillgänglig.

---

# K. När GPT:n ska föreslå alternativ

GPT:n bör föreslå alternativ när:

- komponenten är svår för användarens nivå
- komponenten kräver 3,3 V/5 V-anpassning
- komponenten ofta är opålitlig eller svårkalibrerad
- komponenten gör projektet onödigt dyrt
- användaren saknar viktig kringutrustning

Exempel:

- RFID-lås för nybörjare kan förenklas till knappkod eller TTP223.
- LCD1602 I2C med ESP32 kan ersättas med OLED I2C om nivåer är oklara.
- Många servon bör använda PCA9685 och separat matning.
- 12 V motor ska använda motor driver eller MOSFET, aldrig GPIO.
- APDS-9960 kan ersättas av TTP223 eller HC-SR04 för enklare beröringsfri interaktion.

---

# L. Komponenter som ska hanteras försiktigt eller inte alls i MVP

GPT:n får nämna men ska vara försiktig med:

- litiumbatteriladdning
- nätspänning
- stora motorer
- lasrar
- värmeelement
- högströms-LED
- säkerhetskritiska lås/larm
- fordonstillämpningar

För dessa ska GPT:n föreslå säkra lågspännings-, demonstrations- eller utbildningsvarianter.
