# Justering – SVG-generator v1.1

Detta steg uppdaterar Arduino-projektassistentens underlag så GPT:n kan skapa `circuit.yaml` för **Circuit SVG Generator v1.1**.

## Bakgrund

Den tidigare GPT-kompletteringen utgick från generatorns v1-format, där bara `arduino_uno`, `esp32_devkit` och ett fåtal grundkomponenter kunde användas. SVG-generatorn har nu byggts ut till v1.1 med fler boards, fler komponenttyper, förbättrad modulrendering, BOM, kopplingssteg och JSON Schema.

## Ändringar i GPT-paketet

Följande filer har uppdaterats:

- `knowledge/14-circuit-yaml-svg-generator.md`
- `knowledge/00-knowledge-index.md`
- `knowledge/13-knowledge-filstruktur.md`
- `gpt-builder/02-uppladdningslista-knowledge.md`
- `gpt-builder/04-forsta-verifiering.md`
- `README.md`
- `project-status.md`

Följande fil har lagts till:

- `testfall/testfall-svg-generator-v1-1.md`

## Viktigaste justeringen

GPT:n ska nu använda generatorns v1.1-stöd för:

- `arduino_nano`
- `arduino_mega`
- `nodemcu_esp8266`
- `arduino_leonardo`
- `arduino_micro`
- `arduino_nano_esp32`
- nya specifika komponenttyper som `bme280`, `hc_sr04`, `mfrc522_rfid`, `drv8833`, `pca9685`, `logic_level_converter`, `ws2812_led` m.fl.

GPT:n ska inte längre säga att generatorn bara stödjer `arduino_uno`, `esp32_devkit`, `generic_module` och `i2c_module`.

## Huvudinstruktionen

Huvudinstruktionen är fortfarande under 8 000 tecken och har bara fått en kort komplettering som säger att generator-kompatibel YAML ska följa Knowledge-filen för SVG-generatorn.

Detaljerna ligger i Knowledge, inte i huvudinstruktionen.
