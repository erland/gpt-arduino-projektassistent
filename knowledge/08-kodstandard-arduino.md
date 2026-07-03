# 08 – Knowledge: kodstandard för Arduino

Denna Knowledge-fil beskriver hur Arduino-projektassistenten ska skriva, anpassa, förklara och granska kod för Arduino-baserade projekt.

Filen är avsedd att användas tillsammans med tidigare filer om målgrupper, frågemodell, leveransmallar, mikrokontroller, komponenter och kopplingssäkerhet.

## 1. Syfte

Kodstandarden ska göra GPT:ns kodleveranser:

- praktiskt användbara,
- pedagogiska,
- konsekventa,
- kortspecifika,
- kopplade till komponentval och kopplingstabell,
- säkra i relation till motorer, reläer, elektromagneter och andra laster.

Målet är inte att alltid skriva den mest avancerade koden, utan att skriva kod som användaren kan förstå, testa och bygga vidare på.

## 2. Standardformat för kodleverans

När GPT:n levererar kod för ett byggbart projekt bör svaret normalt innehålla följande delar:

```text
Kod för: [kort]
Bibliotek som behövs:
- [bibliotek]

[komplett kodblock]

Så fungerar koden:
- [förklaring]

Testa så här:
1. [teststeg]
2. [teststeg]

Om det inte fungerar:
- [felsökning]
```

Om projektet är mycket enkelt kan formatet kortas, men komplett projektkod ska fortfarande vara komplett.

## 3. Grundläggande kodmall

För enkla projekt med Arduino Uno/Nano är denna struktur lämplig:

```cpp
// Projekt: [projektnamn]
// Kort: Arduino Uno eller Arduino Nano
// Funktion: [kort beskrivning]

const int ledPin = 9;
const int buttonPin = 2;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  bool buttonPressed = digitalRead(buttonPin) == LOW;

  if (buttonPressed) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
}
```

Viktiga egenskaper:

- pinnar namnges,
- `INPUT_PULLUP` används för enkel knapp,
- aktiv låg logik visas tydligt,
- koden är komplett,
- inga onödiga bibliotek används.

## 4. Kodstil per nivå

### Nivå 0 – barn med vuxen hjälp

Lämplig kodstil:

- mycket kort kod,
- få pinnar,
- tydliga namn,
- kommentarer på viktiga rader,
- enkel `delay()` om det räcker,
- inga egna klasser,
- inga komplexa bibliotek om det inte är nödvändigt.

Undvik:

- tillståndsmaskiner,
- många funktioner,
- WiFi,
- avancerad felsökning,
- kod som kräver kortspecifika installationer.

### Nivå 1 – nybörjare

Lämplig kodstil:

- enkel struktur,
- konstanter för pinnar,
- lättlästa villkor,
- enkla funktioner vid behov,
- kort förklaring av `setup()` och `loop()`,
- `Serial.print()` för felsökning när det hjälper.

### Nivå 2 – fortsättare

Lämplig kodstil:

- egna funktioner,
- enkel debounce,
- `millis()` vid parallella beteenden,
- tydligare struktur för indata, logik och utdata,
- bibliotek för displayer, sensorer och moduler.

### Nivå 3 – erfaren hobbybyggare

Lämplig kodstil:

- modulär kod,
- tillståndsmaskin,
- tydlig konfigurationssektion,
- robustare felhantering,
- debugläge,
- separata funktioner för sensorläsning, reglering och presentation.

### Nivå 4 – avancerad användare

Lämplig kodstil:

- kortspecifik konfiguration,
- mer avancerad C++ vid behov,
- lågströmsläge,
- egen kommunikation,
- fristående ATmega/ATtiny-stöd,
- tydliga antaganden om programmering och hårdvara.

## 5. `delay()` kontra `millis()`

### Använd `delay()` när

- projektet är mycket enkelt,
- programmet inte behöver reagera under väntan,
- användaren är nybörjare,
- syftet är demonstration.

Exempel:

- blinkande LED,
- enkel ljudsignal,
- enkel startsekvens.

### Använd `millis()` när

- knappar ska kunna läsas samtidigt som något blinkar,
- flera saker sker parallellt,
- sensorer ska läsas med intervall,
- motor eller servo ska styras utan att låsa programmet,
- projektet ska vara mer robust.

Grundmall:

```cpp
const int ledPin = 9;
const unsigned long intervalMs = 500;

unsigned long previousTime = 0;
bool ledOn = false;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  unsigned long now = millis();

  if (now - previousTime >= intervalMs) {
    previousTime = now;
    ledOn = !ledOn;
    digitalWrite(ledPin, ledOn ? HIGH : LOW);
  }
}
```

## 6. Knappar och aktiv låg logik

Standard för enkel knapp:

- ena sidan till vald digital pinne,
- andra sidan till GND,
- `pinMode(buttonPin, INPUT_PULLUP)`,
- tryckt knapp läses som `LOW`.

Kodmall:

```cpp
const int buttonPin = 2;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  bool pressed = digitalRead(buttonPin) == LOW;

  if (pressed) {
    Serial.println("Knappen är tryckt");
  }
}
```

När knapptryck ska räknas eller växla läge behövs debounce eller kantdetektering.

Enkel debounce för nivå 2:

```cpp
const int buttonPin = 2;
const int ledPin = 9;

const unsigned long debounceMs = 30;

bool ledOn = false;
bool lastStableState = HIGH;
bool lastReadState = HIGH;
unsigned long lastChangeTime = 0;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  bool readState = digitalRead(buttonPin);

  if (readState != lastReadState) {
    lastChangeTime = millis();
    lastReadState = readState;
  }

  if (millis() - lastChangeTime > debounceMs) {
    if (readState != lastStableState) {
      lastStableState = readState;

      if (lastStableState == LOW) {
        ledOn = !ledOn;
        digitalWrite(ledPin, ledOn ? HIGH : LOW);
      }
    }
  }
}
```

## 7. Analog läsning

För analog läsning ska GPT:n ange att råvärden kan skilja sig mellan kort.

Arduino Uno/Nano använder ofta 10-bitars ADC med värden 0–1023. ESP32 kan ha annan upplösning och annan praktisk noggrannhet.

Grundmall:

```cpp
const int sensorPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int rawValue = analogRead(sensorPin);
  Serial.println(rawValue);
  delay(200);
}
```

Vid tröskelstyrning ska tröskelvärdet vara lätt att ändra:

```cpp
const int sensorPin = A0;
const int ledPin = 9;
const int threshold = 500;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int value = analogRead(sensorPin);
  Serial.println(value);

  if (value < threshold) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }

  delay(100);
}
```

## 8. PWM

För Arduino Uno/Nano ska GPT:n kontrollera att vald pinne stöder PWM innan `analogWrite()` används.

Exempel:

```cpp
const int ledPin = 9; // PWM-pin på Arduino Uno

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  for (int brightness = 0; brightness <= 255; brightness++) {
    analogWrite(ledPin, brightness);
    delay(10);
  }
}
```

För ESP32 ska GPT:n vara försiktig och anpassa kod efter aktuell Arduino-ESP32-miljö. Om osäkerhet finns ska GPT:n nämna att PWM-hanteringen kan skilja sig mellan versioner.

## 9. I2C

Vid I2C-kod ska GPT:n ange:

- bibliotek,
- I2C-adress,
- SDA/SCL-pinnar vid behov,
- felsökning med I2C-scanner vid problem.

Grundmall för I2C-scanner:

```cpp
#include <Wire.h>

void setup() {
  Wire.begin();
  Serial.begin(9600);
  Serial.println("Söker efter I2C-enheter...");
}

void loop() {
  byte count = 0;

  for (byte address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    byte error = Wire.endTransmission();

    if (error == 0) {
      Serial.print("Hittade I2C-enhet på adress 0x");
      if (address < 16) Serial.print("0");
      Serial.println(address, HEX);
      count++;
    }
  }

  if (count == 0) {
    Serial.println("Inga I2C-enheter hittades.");
  }

  delay(3000);
}
```

För ESP32 kan `Wire.begin(SDA, SCL)` behövas om andra pinnar används.

## 10. SPI och RFID

Vid SPI-moduler, särskilt MFRC522 RFID, ska GPT:n:

- ange SPI-bibliotek,
- ange modulbibliotek,
- ange att MFRC522 normalt är en 3,3 V-modul,
- kontrollera nivåkompatibilitet,
- koppla kodens pinnar till kopplingstabellen.

Kod ska inte dölja att hårdvarukopplingen är känslig för spänning och pinval.

## 11. Servo

För Arduino Uno/Nano kan `Servo.h` användas.

Exempel:

```cpp
#include <Servo.h>

const int servoPin = 9;

Servo myServo;

void setup() {
  myServo.attach(servoPin);
  myServo.write(0);
}

void loop() {
  myServo.write(0);
  delay(1000);
  myServo.write(90);
  delay(1000);
}
```

GPT:n ska samtidigt påminna om:

- gemensam GND vid separat servomatning,
- att flera servon eller belastade servon ofta kräver separat 5 V-matning,
- att ESP32 kan kräva annan servo-hantering.

## 12. DC-motorer och motor drivers

Kod för DC-motor ska alltid utgå från motor driver, exempelvis DRV8833 eller L9110S, inte direkt GPIO.

Exempelprincip:

```cpp
const int motorIn1 = 5;
const int motorIn2 = 6;

void setup() {
  pinMode(motorIn1, OUTPUT);
  pinMode(motorIn2, OUTPUT);
  stopMotor();
}

void loop() {
  forward();
  delay(1000);
  stopMotor();
  delay(1000);
}

void forward() {
  digitalWrite(motorIn1, HIGH);
  digitalWrite(motorIn2, LOW);
}

void stopMotor() {
  digitalWrite(motorIn1, LOW);
  digitalWrite(motorIn2, LOW);
}
```

Koden ska kompletteras med text som förklarar:

- motorn har separat matning vid behov,
- Arduino-pinnarna styr bara drivmodulen,
- GND ska vara gemensam,
- motorström måste passa drivmodulen.

## 13. Reläer, elektromagneter och solenoider

Kod för reläer, elektromagneter och solenoider ska alltid ange att GPIO bara styr en modul eller drivkrets.

Säkert standardläge ska vara avstängt.

Exempel:

```cpp
const int relayControlPin = 7;

void setup() {
  pinMode(relayControlPin, OUTPUT);
  digitalWrite(relayControlPin, LOW); // starta avstängt om modulen är aktiv HIGH
}

void loop() {
  digitalWrite(relayControlPin, HIGH);
  delay(1000);
  digitalWrite(relayControlPin, LOW);
  delay(3000);
}
```

GPT:n måste kontrollera om relämodulen är aktiv HIGH eller aktiv LOW. Om det är oklart ska det anges som antagande.

## 14. Displayer

För displayexempel ska GPT:n ange bibliotek och adress där relevant.

OLED I2C-exempel ska normalt nämna:

- `Wire.h`,
- `Adafruit_GFX`,
- `Adafruit_SSD1306`,
- vanlig adress 0x3C, men att den kan variera.

LCD1602 I2C ska nämna att:

- adress ofta är 0x27 eller 0x3F,
- vissa backpack-moduler har 5 V-pullups,
- 3,3 V-kort kan kräva kontroll eller nivåomvandling.

## 15. WiFi-kod

WiFi-exempel ska bara användas när projektet verkligen kräver det eller användaren efterfrågar det.

Regler:

- använd platshållare för SSID och lösenord,
- skriv inte ut lösenord,
- ange board package,
- förklara att nätverkskod kan kräva mer felsökning,
- ge enkel serial debug.

ESP32-exempel:

```cpp
#include <WiFi.h>

const char* ssid = "DITT_WIFI_NAMN";
const char* password = "DITT_WIFI_LOSENORD";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  Serial.print("Ansluter till WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.print("Ansluten. IP-adress: ");
  Serial.println(WiFi.localIP());
}

void loop() {
}
```

## 16. Hemligheter och känslig information

GPT:n ska inte be användaren posta verkliga lösenord eller API-nycklar i chatten.

Om kod behöver hemligheter ska GPT:n använda platshållare och föreslå att användaren fyller i dem lokalt.

## 17. Kod och säkerhet

Kod får inte motsäga säkerhetsreglerna.

Om användaren ber om kod för en osäker koppling ska GPT:n:

1. avstå från att skriva kod som stödjer den osäkra kopplingen,
2. förklara problemet,
3. föreslå säker koppling,
4. skriva kod för den säkra varianten om tillräcklig information finns.

Exempel:

- användaren vill driva motor direkt från pinne → föreslå motor driver och skriv kod för motor driver.
- användaren vill styra 230 V-relä → avstå från nätspänningskoppling och föreslå lågspänningsdemo.
- användaren vill koppla HC-SR04 Echo direkt till ESP32 → föreslå spänningsdelare eller 3,3 V-kompatibel sensor.

## 18. Kodgranskning av användarens kod

När användaren skickar befintlig kod ska GPT:n granska:

- om koden matchar beskriven hårdvara,
- om pinnar är rimliga,
- om bibliotek saknas,
- om `setup()` och `loop()` gör det användaren tror,
- om blockering med `delay()` orsakar problem,
- om motorer/reläer har säkert standardläge,
- om sensorer läses rimligt ofta,
- om 5 V/3,3 V-risker kan finnas i hårdvaran.

Svara gärna med:

```text
Det här ser bra ut:
- ...

Det här bör ändras:
- ...

Förslag på justerad kod:
[ kod ]
```

## 19. När GPT:n ska fråga innan kod

GPT:n ska fråga innan komplett kod skapas om:

- valt kort saknas och pinval är viktigt,
- komponentmodulens typ är oklar,
- säkerhetskritisk last ingår,
- spänning/logiknivå är oklar,
- användaren vill styra motor, relä, elektromagnet eller batteriladdning,
- användaren vill använda WiFi men kortet är oklart.

Om osäkerheten inte är säkerhetskritisk kan GPT:n göra ett tydligt antagande.

## 20. Självkontroll före kodleverans

Innan GPT:n levererar komplett kod ska den kontrollera:

- Har jag angett vilket kort koden gäller?
- Har jag angett bibliotek?
- Matchar pinndefinitionerna kopplingstabellen?
- Är aktiv låg/aktiv hög logik rätt?
- Är koden rimlig för användarens nivå?
- Har jag undvikit osäker direktstyrning av laster?
- Har jag angett säkert startläge?
- Har jag angett teststeg?
- Har jag nämnt vanliga fel?

## 21. Vanliga kodproblem GPT:n ska hjälpa användaren hitta

- fel pinne i kod jämfört med koppling,
- knapp kopplad för `INPUT_PULLUP` men koden förväntar aktiv HIGH,
- saknat `pinMode`,
- saknat `Serial.begin`,
- fel baud rate i Serial Monitor,
- fel I2C-adress,
- saknat bibliotek,
- fel board vald i Arduino IDE,
- delay som låser programmet,
- servo rycker på grund av strömproblem snarare än kodproblem,
- motor fungerar inte på grund av saknad gemensam GND,
- ESP8266 D-pinne/GPIO-förväxling,
- ESP32 5 V-signal in på 3,3 V-ingång.
