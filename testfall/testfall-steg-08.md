# Testfall – steg 8: kodstandard för Arduino

Dessa testfall används för att kontrollera att GPT:n följer kodstandarden.

## Testfall 8.1 – Enkel LED och knapp för nybörjare

### Prompt

```text
Jag vill ha kod för en Arduino Uno där en LED på D9 tänds när jag trycker på en knapp på D2.
```

### Förväntat beteende

GPT:n ska:

- skriva kod för Arduino Uno,
- använda namngivna pinnar,
- använda `INPUT_PULLUP`,
- förklara att knappen blir aktiv låg,
- inte använda onödiga bibliotek,
- ge kort testinstruktion.

## Testfall 8.2 – Blinkande LED med parallell knapprespons

### Prompt

```text
Jag vill att en LED blinkar men att Arduino samtidigt ska kunna reagera på en knapp.
```

### Förväntat beteende

GPT:n ska:

- föreslå `millis()` i stället för `delay()`,
- förklara varför,
- skriva kod som inte blockerar knappavläsning,
- hålla koden begriplig.

## Testfall 8.3 – Servo på Arduino Uno

### Prompt

```text
Skriv kod för att styra ett SG90-servo med Arduino Uno.
```

### Förväntat beteende

GPT:n ska:

- använda `Servo.h`,
- ange servo-pin,
- ge komplett kod,
- nämna att servo kan kräva separat 5 V-matning vid belastning,
- nämna gemensam GND om separat matning används.

## Testfall 8.4 – ESP32 och PWM

### Prompt

```text
Skriv kod för att dimra en LED med ESP32.
```

### Förväntat beteende

GPT:n ska:

- anpassa svaret till ESP32,
- inte skriva som om ESP32 vore en Arduino Uno utan kommentar,
- vara tydlig med 3,3 V-logik,
- ange att PWM-hantering kan skilja sig beroende på Arduino-ESP32-version om relevant,
- använda en rimlig GPIO och undvika att förlita sig på fysisk pinnumrering.

## Testfall 8.5 – NodeMCU och pinförväxling

### Prompt

```text
Jag har en NodeMCU och vill läsa en knapp på D1. Kan du skriva kod?
```

### Förväntat beteende

GPT:n ska:

- ange att NodeMCU D-namn och GPIO-nummer kan blandas ihop,
- gärna ange både D1 och GPIO5 om relevant,
- använda 3,3 V-logik,
- använda `INPUT_PULLUP` om kopplingen är knapp till GND,
- ange antagande om koppling.

## Testfall 8.6 – DC-motor direkt från pinne

### Prompt

```text
Skriv kod för att köra en liten DC-motor direkt från pinne 6 på min Arduino.
```

### Förväntat beteende

GPT:n ska:

- inte skriva kod som stödjer direktdrivning från GPIO,
- förklara att motor kräver drivsteg,
- föreslå exempelvis DRV8833, L9110S, transistor/MOSFET-lösning beroende på nivå,
- skriva kod för säker drivmodul endast om antaganden är tydliga,
- nämna separat motormatning och gemensam GND.

## Testfall 8.7 – Relämodul med oklar aktiv nivå

### Prompt

```text
Jag har en relämodul på D7. Skriv kod som slår på den i en sekund.
```

### Förväntat beteende

GPT:n ska:

- fråga eller ange antagande om relämodulen är aktiv HIGH eller aktiv LOW,
- starta i säkert avstängt läge enligt antagandet,
- inte ge instruktioner för nätspänningskoppling,
- påminna om att GPIO styr relämodulens styringång, inte reläspolen direkt.

## Testfall 8.8 – OLED I2C

### Prompt

```text
Skriv kod för en Arduino Nano med en liten OLED-display via I2C.
```

### Förväntat beteende

GPT:n ska:

- ange bibliotek, exempelvis `Wire`, `Adafruit_GFX`, `Adafruit_SSD1306`,
- nämna vanlig I2C-adress 0x3C men att den kan variera,
- ge komplett kod eller tydligt ange bibliotek som krävs,
- föreslå I2C-scanner vid problem.

## Testfall 8.9 – WiFi på ESP32

### Prompt

```text
Skriv en enkel kod som kopplar upp min ESP32 mot WiFi.
```

### Förväntat beteende

GPT:n ska:

- använda `WiFi.h`,
- använda platshållare för SSID och lösenord,
- inte be användaren posta lösenord i chatten,
- skriva debugutskrift till Serial Monitor,
- ange att ESP32 board package behövs.

## Testfall 8.10 – Granskning av befintlig kod

### Prompt

```text
Kan du granska min Arduino-kod? LED sitter på D9, knapp på D2 till GND, men koden använder digitalRead(buttonPin) == HIGH för tryckt knapp.
```

### Förväntat beteende

GPT:n ska:

- upptäcka aktiv låg-felet om `INPUT_PULLUP` används,
- förklara skillnaden,
- föreslå korrigerad kod,
- gärna kontrollera om `pinMode(buttonPin, INPUT_PULLUP)` saknas.

## Testfall 8.11 – Kod utan valt kort

### Prompt

```text
Skriv kod för att läsa HC-SR04 och visa avståndet.
```

### Förväntat beteende

GPT:n ska:

- fråga efter kort eller göra tydligt antagande om Arduino Uno,
- varna om användaren senare använder ESP32/ESP8266 eftersom Echo kan vara 5 V,
- ange pinnar och kopplingstabell eller antaganden,
- ge teststeg.

## Testfall 8.12 – För avancerad kod för barn

### Prompt

```text
Skapa kod för ett blinkprojekt för en 8-åring som aldrig har programmerat.
```

### Förväntat beteende

GPT:n ska:

- ge mycket enkel kod,
- inte använda onödiga funktioner eller tillståndsmaskin,
- förklara `setup()` och `loop()` enkelt,
- hålla kommentarer pedagogiska.
