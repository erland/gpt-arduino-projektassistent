# Testfall – SVG-generator-kompatibel `circuit.yaml`

Den här filen ersätter de tidigare v1-testfallen. För komplett testsvit mot Circuit SVG Generator v1.1, använd även:

```text
testfall/testfall-svg-generator-v1-1.md
```

## Grundtest – enkel LED

Prompt:

```text
Skapa ett generator-kompatibelt circuit.yaml för en röd LED med 220 ohm motstånd på Arduino Uno D8.
```

Förväntat:

- `version: 1.1`
- `experiment.board: arduino_uno`
- komponenttyperna `resistor` och `led`
- endpoints `board.D8`, `r1.1`, `r1.2`, `led1.anode`, `led1.cathode`, `board.GND`
- notes för långt/kort LED-ben
- inga okända komponenttyper eller pins

## Grundtest – specifik I2C-modul

Prompt:

```text
Skapa circuit.yaml för en OLED I2C-display på Arduino Uno.
```

Förväntat:

- `type: oled_i2c`, inte bara `i2c_module`
- kopplingar till `board.5V` eller `board.3V3` beroende på vald modul, `board.GND`, `board.SDA`, `board.SCL`
- inga fria pin-namn som `VCC` utan komponentprefix

## Grundtest – nytt v1.1-kort

Prompt:

```text
Skapa circuit.yaml för Arduino Mega med LED på D22.
```

Förväntat:

- `experiment.board: arduino_mega`
- giltig boardpin `board.D22`
- GPT:n ska inte längre säga att Mega saknas i generatorn.
