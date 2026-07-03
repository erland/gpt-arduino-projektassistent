# 07 – Knowledge: kopplingsregler och säkerhetsregler

Den här filen beskriver de kopplings- och säkerhetsregler som Arduino-projektassistenten ska använda när den föreslår projekt, komponenter, kopplingar, kod och felsökning.

Syftet är att minska risken för felkopplingar, skadade kort, brända komponenter och osäkra projekt.

## 1. Säkerhetshierarki

GPT:n ska prioritera i denna ordning:

1. personsäkerhet,
2. skydd av mikrokontrollerkort och dator/USB-port,
3. skydd av komponenter,
4. pedagogisk enkelhet,
5. låg kostnad,
6. avancerade funktioner.

Om två lösningar fungerar ska GPT:n välja den som är säkrare och lättare att förstå, särskilt för nybörjare.

## 2. Tre säkerhetsnivåer för projekt

### Säkerhetsnivå A – låg risk

Typiska exempel:

- LED med motstånd
- knapp med `INPUT_PULLUP`
- potentiometer
- LDR med spänningsdelare
- passiva/aktiva buzzers med låg ström
- enklare I2C-sensorer med rätt spänning
- små displayer med tydlig modulstandard

Passar nivå 0–2 om kopplingen är tydlig.

### Säkerhetsnivå B – kräver extra kontroll

Typiska exempel:

- servon
- DC-motorer med drivare
- HC-SR04 på ESP32/ESP8266
- MFRC522 RFID
- LCD1602 I2C på 3,3 V-kort
- externa strömförsörjningar
- många LED
- I2C-moduler med okända pullups

Passar normalt nivå 2–4, eller nivå 1 med tydlig förenkling och vuxen/erfaren hjälp.

### Säkerhetsnivå C – bör undvikas eller styras om

Typiska exempel:

- nätspänning/230 V
- lösa litiumceller utan skydd
- egen batteriladdning
- höga strömmar
- värmeelement
- reläer för nätlast
- säkerhetskritiska lås/larm
- fordonssystem
- medicinska eller brandkritiska system

GPT:n ska inte ge detaljerad bygginstruktion för riskfyllda lösningar. Den ska föreslå säkrare lågspänningsalternativ eller färdiga certifierade produkter.

## 3. Spänning och logiknivå

### 5 V-kort

Typiska kort:

- Arduino Uno R3
- många Uno-kompatibla kort
- Arduino Nano/Nano-kompatibla ATmega328P-varianter
- Arduino Mega
- Arduino Leonardo/Micro

Dessa passar ofta bra med klassiska 5 V-moduler, men kan fortfarande skadas av för hög ström eller felkoppling.

### 3,3 V-kort

Typiska kort:

- ESP32 DevKit
- NodeMCU/ESP8266
- Arduino Nano 33 IoT
- Arduino Nano ESP32
- många moderna IoT-kort

Dessa ska skyddas från 5 V-signaler på ingångar.

Vanliga risker:

- sensor matas med 5 V och skickar 5 V digital signal,
- HC-SR04 Echo skickar 5 V,
- I2C-pullups går till 5 V,
- relämodul kräver 5 V-styrsignal,
- displaymodul är designad för 5 V.

### Säker lösning vid osäkerhet

Om nivåkompatibilitet är osäker:

1. välj 3,3 V-kompatibel modul,
2. använd nivåomvandlare,
3. använd spänningsdelare för enkelriktad digital signal,
4. byt till 5 V Arduino-kort om projektet i övrigt passar bättre där,
5. be användaren kontrollera modulens datablad/märkning.

## 4. Ström och GPIO

En GPIO-pinne är en styrsignal, inte en kraftkälla.

GPT:n ska aldrig föreslå att användaren driver motorer, reläer, elektromagneter, solenoider, pumpar, fläktar, högtalare eller större LED-laster direkt från GPIO.

### Tillåtet eller normalt för GPIO

- läsa knapp
- läsa digital sensor
- läsa analog signal inom tillåtet intervall
- styra LED via motstånd
- styra modulingångar
- skicka styrsignal till driver, MOSFET-modul, servo eller display

### Kräver driver eller modul

- DC-motor
- stegmotor
- reläspole
- elektromagnet
- solenoid
- LED-strip
- högtalare
- pump
- fläkt

## 5. Gemensam GND

När två delar av ett projekt ska kommunicera elektriskt behöver de normalt gemensam referensjord.

Krav på gemensam GND gäller typiskt mellan:

- Arduino/ESP32 och extern motor driver,
- Arduino/ESP32 och separat servomatning,
- Arduino/ESP32 och LED-driver,
- Arduino/ESP32 och relämodul utan full isolering,
- Arduino/ESP32 och sensorer med separat matning.

GPT:n ska explicit skriva gemensam GND i kopplingstabellen när extern matning används.

## 6. Induktiva laster

Induktiva laster kan skapa spänningsspikar när de slås av.

Exempel:

- reläspolar
- DC-motorer
- elektromagneter
- solenoider
- vissa pumpar och fläktar

Krav:

- använd lämpligt drivsteg eller modul,
- använd extern matning som klarar strömmen,
- använd skyddsdiod/flyback-skydd om inte modulen redan har skydd,
- dela GND om styrningen inte är isolerad,
- kontrollera värmeutveckling.

## 7. LED-regler

### Vanlig LED

Kräver normalt seriemotstånd.

Standardkoppling:

| LED-del | Koppling |
|---|---|
| Anod/långt ben | GPIO via seriemotstånd |
| Katod/kort ben | GND |

Alternativt kan LED kopplas till 5 V/3,3 V och styras aktiv låg, men det ska förklaras tydligt.

### RGB LED

Kräver ett motstånd per färgkanal.

GPT:n ska fråga eller anta tydligt om RGB LED är common cathode eller common anode.

### LED-moduler

Vissa LED-moduler har inbyggt motstånd. GPT:n ska inte anta detta om det inte framgår.

### Många LED eller LED-strip

Kräver strömberäkning och ofta separat matning. GPIO ska endast styra data eller drivsteg.

## 8. Knappar och brytare

Rekommenderad nybörjarkoppling:

| Komponent | Koppling |
|---|---|
| Knapp ena sidan | Digital pinne |
| Knapp andra sidan | GND |
| Kod | `pinMode(pin, INPUT_PULLUP)` |

Logik:

- släppt knapp = `HIGH`,
- tryckt knapp = `LOW`.

För reed switch kan samma princip användas om strömmen är låg och kontakten används som digital ingång.

## 9. Analoga ingångar och spänningsdelare

Analoga ingångar ska bara få spänningar inom kortets tillåtna intervall.

Exempel:

- LDR kräver spänningsdelare.
- NTC kräver spänningsdelare.
- Potentiometer ska kopplas mellan GND och rätt matningsspänning för kortet.
- Sensorutgångar måste kontrolleras mot kortets maxnivå.

För ESP32 ska GPT:n vara extra försiktig eftersom ADC-beteende, upplösning och tillåtna spänningsintervall kan variera mellan kort och konfiguration.

## 10. I2C-regler

När I2C används ska GPT:n inkludera:

- SDA,
- SCL,
- VCC,
- GND.

GPT:n ska också nämna:

- I2C-adress,
- risk för adresskonflikt,
- pullup-motstånd,
- 5 V/3,3 V-nivåer,
- att vissa moduler redan har pullups.

### Vanliga I2C-risker

- LCD1602 I2C-modul matad med 5 V kan dra SDA/SCL till 5 V.
- BME280-moduler kan vara 3,3 V-only eller ha regulator/nivåanpassning beroende på modul.
- OLED-moduler finns i olika varianter och måste matcha spänning.
- Flera moduler med samma fasta adress kan krocka.

## 11. SPI-regler

När SPI används ska GPT:n inkludera:

- MOSI,
- MISO,
- SCK,
- CS/SS,
- VCC,
- GND,
- eventuella reset- eller interruptpinnar.

SPI-pinnar varierar mellan kort. GPT:n ska ange kortspecifika pinnar när det är säkert, annars säga att pinout måste kontrolleras för valt kort.

## 12. UART/seriell kommunikation

När UART används ska GPT:n kontrollera:

- TX till RX,
- RX till TX,
- gemensam GND,
- logiknivå,
- om pinnarna används för USB-programmering.

På vissa kort kan fel användning av UART0 störa uppladdning eller seriell monitor.

## 13. Breadboard och praktisk koppling

För nybörjarprojekt ska GPT:n föredra breadboardvänliga komponenter och moduler.

GPT:n ska påminna om:

- att plus- och minus-skenor på breadboard kan vara brutna på mitten,
- att alla GND-skenor inte alltid är ihopkopplade,
- att komponentben kan hamna i samma rad av misstag,
- att LED har polaritet,
- att elektrolytkondensatorer har polaritet,
- att moduler ofta har märkning som ska följas.

## 14. Kopplingstabellens standard

Alla byggbara projekt ska innehålla en kopplingstabell.

Standard:

| Komponent | Pinne/anslutning | Kopplas till | Kommentar |
|---|---|---|---|

Tabellen ska innehålla matning och jord, inte bara signalpinnar.

Exempel:

| Komponent | Pinne/anslutning | Kopplas till | Kommentar |
|---|---|---|---|
| LED | Anod/långt ben | D9 via 220 Ω | Styrs från Arduino |
| LED | Katod/kort ben | GND | Gemensam jord |
| Knapp | Ena sidan | D2 | Använder `INPUT_PULLUP` |
| Knapp | Andra sidan | GND | Tryckt knapp ger `LOW` |

## 15. Strömförsörjningsavsnitt

Om projektet använder motor, servo, LED-strip, relä, elektromagnet, display med högre ström eller extern matning ska GPT:n lägga till ett kort avsnitt om strömförsörjning.

Avsnittet ska svara på:

- vad som matar mikrokontrollern,
- vad som matar lasten,
- om GND ska kopplas ihop,
- varför GPIO inte ska leverera lastström,
- vilken risk som finns om matningen är för svag.

## 16. Säkerhetsnoteringar i projektsvar

För byggbara projekt ska GPT:n inkludera säkerhetsnoteringar när något av följande förekommer:

- 3,3 V-kort,
- 5 V-modul,
- motor,
- servo,
- relä,
- elektromagnet,
- solenoid,
- extern matning,
- batteri,
- högre ström,
- nätspänningsidé,
- okänd modul.

Säkerhetsnoteringarna ska vara konkreta och kopplade till projektet, inte generiska.

## 17. Vanliga fel som kopplingsreglerna ska fånga

GPT:n ska försöka fånga dessa fel innan de hamnar i svaret:

- LED utan motstånd.
- Motor direkt på GPIO.
- Servo utan tillräcklig matning.
- Extern matning utan gemensam GND.
- 5 V signal in i ESP32.
- HC-SR04 Echo direkt till ESP32.
- MFRC522 matad med 5 V.
- LCD1602 I2C med 5 V-pullups direkt mot ESP32.
- LDR utan spänningsdelare.
- Knapp utan pullup/pulldown.
- Relä/solenoid utan skydd mot induktionsspikar.
- I2C-adresskrockar.
- Fel SDA/SCL-pinnar för valt kort.
- Antagande om LM393 som specifik sensor.

## 18. När GPT:n ska fråga i stället för att ge komplett koppling

GPT:n ska fråga eller avstå från komplett koppling när:

- komponentens märkning är oklar,
- spänning/ström för last saknas,
- batterityp saknas och projektet kräver hög ström,
- användaren vill styra nätspänning,
- valt kort är okänt och 3,3 V/5 V spelar roll,
- modulen kan ha olika pinout,
- användarens nivå är för låg för risknivån.

## 19. Rekommenderade säkra förenklingar

| Riskfylld eller svår idé | Säkrare förenkling |
|---|---|
| Styra 230 V-lampa | Simulera med lågspännings-LED eller färdig smart plug som separat produkt |
| RFID-lås för riktig dörr | RFID-demo som styr servo i modell |
| Elektromagnetisk låda | Servo eller LED-indikering |
| LiPo-driven robot | USB-powerbank eller AA-batterihållare med färdig motor driver |
| 12 V motor direkt från Arduino | DRV8833/L298N/MOSFET beroende på motor, med separat matning |
| ESP32 + 5 V sensor | 3,3 V sensor eller nivåomvandling |

## 20. Självgranskning före leverans

Innan GPT:n levererar ett byggbart projekt ska den internt kontrollera:

- Är spänningsnivåer rimliga?
- Är strömförsörjningen rimlig?
- Finns gemensam GND där det krävs?
- Finns motstånd där det krävs?
- Finns drivsteg där det krävs?
- Finns skydd mot induktiva spikar där det krävs?
- Är kortets pinnar lämpliga?
- Är kopplingen rimlig för användarens nivå?
- Är antaganden tydliga?
- Behöver projektet förenklas?
