# Designbeslut – SVG-generator-kompatibilitet

## Beslut

Projektpaketet kompletteras med en separat Knowledge-fil för `circuit.yaml` v1 så att GPT:n kan skapa kopplingsunderlag som passar den befintliga SVG-generatorn.

## Varför

Det tidigare GPT-paketet hade en bredare elektronikmodell än SVG-generatorn. GPT:n stödde många kort och komponenter, medan generatorns v1 endast stödjer:

- board-id: `arduino_uno`, `esp32_devkit`
- komponenttyper: `resistor`, `led`, `button`, `potentiometer`, `buzzer`, `servo`, `generic_module`, `i2c_module`

Utan särskild styrning skulle GPT:n kunna skapa elektriskt rimliga men icke-renderbara kopplingsunderlag.

## Konsekvens

När användaren uttryckligen vill ha generator-kompatibel YAML ska GPT:n begränsa sig till generatorns nuvarande format. För andra projekt får GPT:n fortsätta använda den bredare komponent- och kortmodellen, men ska då inte kalla underlaget generator-kompatibelt.
