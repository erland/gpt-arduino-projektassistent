# 14 – Circuit YAML för SVG-generator v1.1

Detta dokument beskriver hur Arduino-projektassistenten ska skapa kopplingsunderlag som passar **Circuit SVG Generator v1.1**.

Målet är att GPT:n vid behov ska kunna skapa en `circuit.yaml` som kan valideras och renderas av generatorn, i stället för att bara ge fri text, kopplingstabell eller generell SVG-idé.

## När denna standard ska användas

Använd denna standard när användaren ber om något av följande:

- kopplingsschema som ska gå att rendera med SVG-generatorn
- `circuit.yaml`
- YAML-underlag för kopplingsbild
- generator-kompatibelt kopplingsschema
- experimentunderlag som ska passa bokens SVG-generator

Om användaren bara ber om ett vanligt projektförslag räcker normalt kopplingstabell och kod. `circuit.yaml` kan inkluderas som extra avsnitt när användaren uttryckligen vill ha SVG-/generatorunderlag eller när det passar svarets längd.

## Viktig begränsning

SVG-generatorn v1.1 beskriver **logiska kopplingar**, inte exakt fysisk breadboardplacering.

Det betyder:

- `connections` beskriver vilka punkter som ska kopplas elektriskt.
- YAML-filen ska inte försöka beskriva varje hål på en breadboard.
- Pedagogiska detaljer, risker och byggtips ska uttryckas med `notes`, vanlig kopplingstabell och textinstruktioner.
- Generatorn gör ingen fullständig elsäkerhetsanalys. GPT:n måste fortfarande följa säkerhetsreglerna i `07-kopplingsregler-och-sakerhet.md`.
- Att något går att rendera betyder inte automatiskt att det är säkert eller lämpligt.

## Formatversion

Generatorn accepterar filer utan `version`, men GPT:n bör sätta:

```yaml
version: 1.1
```

Det gör det tydligt att filen är avsedd för generatorns utökade v1.1-stöd.

## Övergripande YAML-struktur

En generator-kompatibel fil ska använda denna struktur:

```yaml
version: 1.1
experiment:
  id: E001
  title: Blinkande LED
  board: arduino_uno

components:
  - id: r1
    type: resistor
    label: 220 ohm
    value: 220
    unit: ohm

connections:
  - from: board.D8
    to: r1.1
  - from: r1.2
    to: led1.anode
  - from: led1.cathode
    to: board.GND

notes:
  - target: led1.anode
    text: LED:ens långa ben är anod.
```

Obligatoriska sektioner:

- `experiment`
- `components`
- `connections`

Valfria sektioner:

- `version`
- `notes`
- `layout`

## Boards som stöds av generatorn v1.1

Använd bara dessa board-id:n i generator-kompatibel YAML:

| Kort | YAML board-id | Tillåtna board-pinnar |
|---|---|---|
| Arduino Uno | `arduino_uno` | `5V, 3V3, GND, VIN, D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, A0, A1, A2, A3, A4, A5, SDA, SCL` |
| ESP32 DevKit | `esp32_devkit` | `3V3, VIN, 5V, GND, GPIO0, GPIO1, GPIO2, GPIO3, GPIO4, GPIO5, GPIO12, GPIO13, GPIO14, GPIO15, GPIO16, GPIO17, GPIO18, GPIO19, GPIO21, GPIO22, GPIO23, GPIO25, GPIO26, GPIO27, GPIO32, GPIO33, GPIO34, GPIO35, GPIO36, GPIO39, TX0, RX0, SDA, SCL` |
| Arduino Nano | `arduino_nano` | `5V, 3V3, GND, VIN, D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, A0, A1, A2, A3, A4, A5, A6, A7, SDA, SCL` |
| Arduino Mega | `arduino_mega` | `5V, 3V3, GND, VIN, D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30, D31, D32, D33, D34, D35, D36, D37, D38, D39, D40, D41, D42, D43, D44, D45, D46, D47, D48, D49, D50, D51, D52, D53, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, SDA, SCL, MISO, MOSI, SCK, SS` |
| NodeMCU ESP8266 | `nodemcu_esp8266` | `3V3, VIN, 5V, GND, D0, D1, D2, D3, D4, D5, D6, D7, D8, A0, SDA, SCL, SCK, MISO, MOSI, SS` |
| Arduino Leonardo | `arduino_leonardo` | `5V, 3V3, GND, VIN, D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, A0, A1, A2, A3, A4, A5, SDA, SCL` |
| Arduino Micro | `arduino_micro` | `5V, 3V3, GND, VIN, D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, A0, A1, A2, A3, A4, A5, SDA, SCL` |
| Arduino Nano ESP32 | `arduino_nano_esp32` | `3V3, 5V, VIN, GND, D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, A0, A1, A2, A3, A4, A5, A6, A7, SDA, SCL` |

Regler:

- Skriv alltid board-anslutningar som `board.<pin>`, till exempel `board.D8`, `board.GND`, `board.SDA`.
- Använd hellre `board.SDA` och `board.SCL` än underliggande analoga/digitala pinnar vid I2C om boarden har dessa alias.
- För NodeMCU ESP8266 ska GPT:n använda `D0`–`D8` i YAML, inte råa GPIO-nummer, eftersom generatorns boardmodell använder NodeMCU-D-pinnar.
- För ESP32 DevKit används `GPIOxx`, till exempel `board.GPIO21`, men `board.SDA`/`board.SCL` bör användas för I2C när det passar.
- För Arduino Nano ESP32 används generatorns Arduino-liknande `D`/`A`-pinnar; vid hårdvaruspecifika projekt ska GPT:n ange att exakt GPIO-mappning behöver kontrolleras.
- Även om en pinne stöds av generatorn måste GPT:n följa kortets verkliga begränsningar, till exempel input-only-pinnar, boot-pinnar och 3,3 V-logik.

## Komponenttyper som stöds av generatorn v1.1

Använd bara dessa komponenttyper i generator-kompatibel YAML:

| YAML type | Pins | Render-shape | Kommentar |
|---|---|---|---|
| `resistor` | `1, 2` | `resistor` | Motstånd. |
| `led` | `anode, cathode` | `led` | Enkel LED. |
| `button` | `1, 2` | `switch` | Tryckknapp/reed switch-liknande brytare. |
| `potentiometer` | `left, wiper, right` | `potentiometer` | Potentiometer. |
| `buzzer` | `plus, minus` | `buzzer` | Aktiv/passiv buzzer. |
| `servo` | `signal, vcc, gnd` | `module` | Hobbyservo; ström måste bedömas separat. |
| `generic_module` | `vcc, gnd, signal` | `module` | Förenklad modul med en signal. |
| `i2c_module` | `vcc, gnd, sda, scl` | `module` | Generisk I2C-modul. |
| `rgb_led` | `red, green, blue, common` | `rgb_led` | RGB-LED; ange common tydligt. |
| `ldr` | `1, 2` | `module` | LDR/fotoresistor. |
| `dht11` | `vcc, data, gnd` | `module` | Temperatur/fukt-sensor. |
| `dht22` | `vcc, data, gnd` | `module` | Temperatur/fukt-sensor. |
| `bme280` | `vcc, gnd, sda, scl` | `module` | I2C miljösensor. |
| `ds18b20` | `vcc, data, gnd` | `module` | 1-Wire temperatursensor. |
| `hc_sr04` | `vcc, trig, echo, gnd` | `hc_sr04` | Ultraljudssensor; echo kan kräva nivåanpassning till 3,3 V. |
| `pir_sensor` | `vcc, out, gnd` | `module` | PIR-modul. |
| `ttp223_touch` | `vcc, out, gnd` | `module` | Touchmodul. |
| `reed_switch` | `1, 2` | `switch` | Reedkontakt. |
| `hall_sensor` | `vcc, gnd, out` | `module` | Hall-sensormodul. |
| `oled_i2c` | `vcc, gnd, sda, scl` | `oled_i2c` | OLED I2C-display. |
| `lcd1602_i2c` | `vcc, gnd, sda, scl` | `lcd1602_i2c` | LCD1602 med I2C-backpack. |
| `tm1637_display` | `vcc, gnd, clk, dio` | `module` | 4-siffrig TM1637-display. |
| `mfrc522_rfid` | `vcc, gnd, sda, sck, mosi, miso, rst` | `module` | SPI RFID-modul, normalt 3,3 V. |
| `relay_module` | `vcc, gnd, in` | `relay_module` | Relämodul; endast lågspänningslast i GPT-projekt. |
| `mosfet_module` | `signal, vcc, gnd, load_plus, load_minus` | `module` | MOSFET-modul för extern last; kontrollera last/matning. |
| `dc_motor` | `plus, minus` | `dc_motor` | DC-motor; ska inte kopplas direkt till GPIO. |
| `drv8833` | `vm, vcc, gnd, ain1, ain2, aout1, aout2, bin1, bin2, bout1, bout2` | `module` | Motordrivare. |
| `l9110s` | `vcc, gnd, ia, ib, oa, ob` | `module` | Motordrivare. |
| `pca9685` | `vcc, gnd, sda, scl, vplus, ch0_signal, ch0_vcc, ch0_gnd` | `module` | I2C PWM/servodrivare. |
| `pcf8574` | `vcc, gnd, sda, scl` | `module` | I2C I/O-expander. |
| `pcf8575` | `vcc, gnd, sda, scl` | `module` | I2C I/O-expander. |
| `cd74hc4067` | `vcc, gnd, sig, s0, s1, s2, s3, en` | `module` | Analog/digital multiplexer. |
| `logic_level_converter` | `hv, lv, gnd, hv1, lv1, hv2, lv2` | `logic_level_converter` | Nivåomvandlare. |
| `ws2812_led` | `vcc, gnd, din, dout` | `module` | Adresserbar RGB LED/NeoPixel-liknande. |

Regler:

- Om komponenten finns som egen typ ska den egna typen användas, exempelvis `hc_sr04`, `bme280`, `oled_i2c`, `mfrc522_rfid` eller `drv8833`.
- Använd `generic_module` endast när komponenten verkligen kan beskrivas som VCC/GND/en signal.
- Använd `i2c_module` endast när en mer specifik I2C-typ saknas.
- Använd inte egna påhittade typer. Om en komponent inte stöds, säg det tydligt och ge vanlig kopplingstabell i stället eller föreslå närmaste renderbara förenkling.

## Endpoint-format

Alla kopplingar ska skrivas med punktnotation:

```text
board.<pin>
<componentId>.<pin>
```

Exempel:

```yaml
connections:
  - from: board.D8
    to: r1.1
  - from: r1.2
    to: led1.anode
  - from: led1.cathode
    to: board.GND
```

Regler:

- `from` och `to` är obligatoriska.
- Alla komponent-id:n i `connections` måste finnas i `components`.
- Alla komponentpins måste finnas i den valda komponenttypen.
- Alla boardpins måste finnas i vald boardtyp.
- Skriv `board.GND`, inte bara `GND`.
- Skriv `board.5V` eller `board.3V3`, inte `5V` eller `3V3` utan prefix.

## Id-standard

Använd stabila, korta id:n utan å, ä, ö, mellanslag eller specialtecken.

| Komponent | Id-exempel |
|---|---|
| Motstånd | `r1`, `r2` |
| LED | `led1`, `led2` |
| RGB LED | `rgb1` |
| Tryckknapp | `button1` |
| Potentiometer | `pot1` |
| Buzzer | `buzzer1` |
| Servo | `servo1` |
| Sensor | `sensor1`, `dht1`, `bme1`, `pir1` |
| Display | `display1`, `oled1`, `lcd1` |
| Motordrivare | `driver1` |
| Motor | `motor1` |
| Nivåomvandlare | `level1` |
| I/O-expander | `io1` |

## Rekommenderade kopplingsmönster

### LED med motstånd

```yaml
version: 1.1
experiment:
  id: LED001
  title: LED med seriemotstånd
  board: arduino_uno
components:
  - id: r1
    type: resistor
    label: 220 ohm
    value: 220
    unit: ohm
  - id: led1
    type: led
    label: LED
connections:
  - from: board.D8
    to: r1.1
  - from: r1.2
    to: led1.anode
  - from: led1.cathode
    to: board.GND
notes:
  - target: led1.anode
    text: LED:ens långa ben är anod.
  - target: led1.cathode
    text: LED:ens korta ben är katod och går mot GND.
```

### I2C-modul med specifik typ

```yaml
version: 1.1
experiment:
  id: BME001
  title: BME280 med ESP32
  board: esp32_devkit
components:
  - id: bme1
    type: bme280
    label: BME280
connections:
  - from: board.3V3
    to: bme1.vcc
  - from: board.GND
    to: bme1.gnd
  - from: board.SDA
    to: bme1.sda
  - from: board.SCL
    to: bme1.scl
notes:
  - target: bme1.vcc
    text: Många BME280-moduler fungerar med 3,3 V. Kontrollera modulens märkning.
```

### HC-SR04 med 5 V Arduino

```yaml
version: 1.1
experiment:
  id: DIST001
  title: Avståndsmätare med HC-SR04
  board: arduino_uno
components:
  - id: sensor1
    type: hc_sr04
    label: HC-SR04
connections:
  - from: board.5V
    to: sensor1.vcc
  - from: board.GND
    to: sensor1.gnd
  - from: board.D9
    to: sensor1.trig
  - from: sensor1.echo
    to: board.D10
notes:
  - target: sensor1.echo
    text: Till ESP32/3,3 V-kort ska Echo normalt nivåanpassas.
```

### DRV8833 med DC-motor

```yaml
version: 1.1
experiment:
  id: MOTOR001
  title: DC-motor med DRV8833
  board: arduino_uno
components:
  - id: driver1
    type: drv8833
    label: DRV8833
  - id: motor1
    type: dc_motor
    label: DC-motor
connections:
  - from: board.5V
    to: driver1.vcc
  - from: board.GND
    to: driver1.gnd
  - from: board.D5
    to: driver1.ain1
  - from: board.D6
    to: driver1.ain2
  - from: driver1.aout1
    to: motor1.plus
  - from: driver1.aout2
    to: motor1.minus
notes:
  - target: driver1.vm
    text: Motorernas VM-matning behöver ofta separat batteri eller extern matning. Koppla aldrig motorn direkt till GPIO.
  - target: driver1.gnd
    text: Extern motormatning och mikrokontroller måste dela GND.
```

## Notes

Använd `notes` för pedagogiska detaljer, säkerhetsvarningar och praktiska byggtips som inte är egna elektriska kopplingar.

Typiska notes:

- LED:ens långa ben är `anode`.
- LED:ens korta ben är `cathode`.
- Servo behöver ofta separat 5 V-matning vid belastning.
- Alla externa matningar måste dela GND med mikrokontrollern.
- ESP32/ESP8266 är 3,3 V-logik och får inte få 5 V direkt på GPIO.
- HC-SR04 Echo behöver nivåanpassas till ESP32/3,3 V-kort.
- MFRC522 är normalt 3,3 V och ska inte matas med 5 V om modulen inte uttryckligen stödjer det.
- Relämoduler i GPT-projekt ska bara användas för säkra lågspänningslaster.

## Layout

`layout` är valfritt. GPT:n ska normalt inte ange manuell layout om det inte behövs.

Tillåtet format:

```yaml
layout:
  direction: left-to-right
  nodes:
    board:
      x: 80
      y: 120
    led1:
      x: 420
      y: 120
  wires:
    style: orthogonal
```

Regler:

- Använd `direction: left-to-right` eller `top-to-bottom`.
- `nodes` kan ange `x` och `y` för `board` och komponent-id:n.
- `wires.style` kan vara `orthogonal` eller `direct`.
- Låt generatorn sköta layout om projektet är enkelt.

## BOM och kopplingssteg

Generator v1.1 kan även skapa BOM och kopplingssteg från samma YAML.

GPT:n bör därför:

- använda tydliga `label`, `value` och `unit` där det hjälper BOM:en
- inte gömma viktiga komponenter i fri text om de ska synas i BOM
- lägga in säkerhetsrelevanta förklaringar i `notes` när de hör till en viss anslutning eller komponent

## När GPT:n ska avstå från generator-YAML

Avstå från att påstå att YAML är renderbar om:

- användaren vill använda en komponenttyp som saknas i generatorn och den inte kan förenklas utan att bli missvisande
- kopplingen kräver säkerhetskritisk information som saknas, exempelvis okänd batterityp, okänd motorström eller okänd relälast
- projektet handlar om nätspänning eller annan farlig last
- komponentens pinout är oklar och flera vanliga varianter finns

Då ska GPT:n ge vanlig kopplingstabell, tydliga antaganden och förklara vad som behöver kontrolleras eller läggas till i generatorn.

## Förhållande till övriga Knowledge-filer

Den här filen styr bara **generatorformatet**. Den ersätter inte:

- säkerhetsreglerna i `07-kopplingsregler-och-sakerhet.md`
- komponentreglerna i `06-komponentkatalog-mvp.md`
- kodstandarden i `08-kodstandard-arduino.md`
- den vanliga ritnings- och kopplingsstandarden i `09-ritnings-och-kopplingsstandard.md`

Prioritet vid konflikt:

1. Säkerhet och elektrisk rimlighet
2. Verklig komponent-/kortkompatibilitet
3. Generatorns accepterade YAML-format
4. Pedagogisk layout och notes

## Självkontroll före svar med `circuit.yaml`

Innan GPT:n lämnar generator-kompatibel YAML ska den kontrollera:

- Är `experiment.board` ett av generatorns v1.1-stödda board-id:n?
- Finns varje `component.type` i generatorns v1.1-komponentlista?
- Finns varje komponentpin i komponenttypen?
- Finns varje boardpin i vald board?
- Har alla komponenter stabila id:n?
- Matchar YAML, kopplingstabell och eventuell kod samma pinnar?
- Finns säkerhetsnoteringar för motorer, reläer, servon, nivåomvandling, externa matningar och 5 V/3,3 V-blandning?
- Har GPT:n tydligt sagt om något är en förenklad logisk bild snarare än exakt breadboardplacering?
