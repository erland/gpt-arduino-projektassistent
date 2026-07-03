# Testfall – Steg 9: Ritnings- och kopplingsstandard

Dessa testfall används för att kontrollera att GPT:n följer ritnings- och kopplingsstandarden.

## Testfall 9.1 – Enkelt LED-projekt

**Prompt:**

```text
Skapa ett enkelt Arduino-projekt där en LED blinkar.
```

**Förväntat beteende:**

- GPT:n anger valt kort eller antagande.
- GPT:n ger kopplingstabell.
- LED har seriemotstånd.
- Långt/kort LED-ben nämns.
- Koden använder samma pinne som kopplingstabellen.
- Enkel byggordning ges.

## Testfall 9.2 – Knapp med INPUT_PULLUP

**Prompt:**

```text
Skapa ett projekt där en knapp tänder en LED med Arduino Uno.
```

**Förväntat beteende:**

- Kopplingstabellen visar knapp mellan digital pinne och GND.
- Koden använder `INPUT_PULLUP`.
- GPT:n förklarar att knappen är aktiv låg.
- Koppling och kod är konsekventa.

## Testfall 9.3 – ESP32 och HC-SR04

**Prompt:**

```text
Visa hur jag kopplar en HC-SR04 till en ESP32.
```

**Förväntat beteende:**

- GPT:n varnar för att Echo ofta är 5 V.
- GPT:n föreslår spänningsdelare eller nivåomvandling för Echo.
- Kopplingstabellen visar nivåanpassning.
- GPT:n markerar att pin-val kan behöva anpassas till exakt ESP32-kort.
- Ingen förenklad direktkoppling av Echo till ESP32 utan kommentar.

## Testfall 9.4 – I2C OLED

**Prompt:**

```text
Jag vill koppla en I2C OLED till Arduino Nano.
```

**Förväntat beteende:**

- GPT:n ger kopplingstabell med VCC, GND, SDA och SCL.
- GPT:n anger Nano/Uno-liknande I2C-pinnar eller förklarar hur de hittas.
- GPT:n nämner I2C-adress som möjlig felsökningspunkt.
- GPT:n nämner att VCC-spänning ska kontrolleras mot modulen.

## Testfall 9.5 – Mermaid-diagram

**Prompt:**

```text
Skapa en översikt i Mermaid för ett Arduino-projekt med knapp, LED och buzzer.
```

**Förväntat beteende:**

- GPT:n får använda Mermaid.
- GPT:n markerar att Mermaid är en logisk översikt.
- GPT:n ger fortfarande kopplingstabell om svaret är byggbart.
- Mermaid-diagrammet ersätter inte tabellen.

## Testfall 9.6 – Motor med extern matning

**Prompt:**

```text
Visa kopplingen för att styra en liten DC-motor med Arduino och DRV8833.
```

**Förväntat beteende:**

- GPT:n visar Arduino till DRV8833-signaler.
- GPT:n visar motor till DRV8833-utgångar.
- GPT:n visar separat motormatning om det behövs.
- GPT:n kräver gemensam GND.
- GPT:n säger inte att motorn ska drivas direkt från Arduino-pin.
- Strömförsörjningsavsnitt finns.

## Testfall 9.7 – Dokumentera befintlig kod med oklart schema

**Prompt:**

```text
Dokumentera mitt projekt. Koden använder D9 för servo och D2 för knapp, men jag har inte skrivit hur det är kopplat.
```

**Förväntat beteende:**

- GPT:n skiljer mellan observerad information och antaganden.
- GPT:n kan föreslå rekommenderad koppling men markerar den som antagen.
- GPT:n frågar eller varnar om servomatning saknas.
- GPT:n hittar inte på att befintlig koppling är verifierad.

## Testfall 9.8 – Kontrollista före ström

**Prompt:**

```text
Skapa ett byggbart projekt med Arduino, relämodul och LED.
```

**Förväntat beteende:**

- GPT:n varnar kring relä och last.
- GPT:n undviker nätspänning som standard.
- GPT:n ger kopplingstabell.
- GPT:n har kontrollista före strömanslutning.
- GPT:n förklarar gemensam GND och matning.

## Testfall 9.9 – Oklart modulnamn

**Prompt:**

```text
Hur kopplar jag min LM393-modul till ESP32?
```

**Förväntat beteende:**

- GPT:n frågar eller anger att LM393 bara beskriver komparatorkretsen/modulfamiljen.
- GPT:n ber användaren kontrollera modulens märkning och funktion.
- GPT:n ger inte definitiv pinout om modulen är oklar.
- GPT:n påminner om 3,3 V-logik för ESP32.

## Testfall 9.10 – Kod/koppling-matchning

**Prompt:**

```text
Skapa ett projekt med Arduino Uno, LED på D6, knapp på D4 och buzzer på D8.
```

**Förväntat beteende:**

- Kopplingstabellen använder D6, D4 och D8.
- Koden använder samma pinnar.
- Pin-tabellen visar samma pinnar.
- GPT:n blandar inte in andra pinnar utan att ange varför.
