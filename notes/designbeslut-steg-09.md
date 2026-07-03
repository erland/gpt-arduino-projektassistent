# Designbeslut – Steg 9

## Steg

**Steg 9 – Skapa ritnings- och kopplingsstandard**

## Syfte

Syftet med detta steg är att definiera hur GPT:n ska beskriva kopplingar på ett sätt som är pedagogiskt, konsekvent och möjligt att verifiera. Fokus ligger på kopplingstabeller och textbaserade underlag i stället för att börja med avancerade bildscheman.

## Viktigaste designbeslut

### 1. Kopplingstabell före bild

Beslut: Alla byggbara projekt ska ha en kopplingstabell.

Motiv: En tabell är enklare att granska, felsöka och jämföra mot kod än en bild. Bilder kan vara pedagogiskt bra, men kan också dölja fel eller antaganden.

### 2. Pin-tabell används vid större eller känsligare projekt

Beslut: Pin-tabell krävs inte för minsta projekt men bör användas när projektet har flera komponenter, bussar, ESP32/ESP8266 eller externa laster.

Motiv: Pin-tabellen gör det lättare att se belastning, pin-konflikter och relationen mellan kod och fysisk koppling.

### 3. Strömförsörjning är en egen del

Beslut: Projekt med mer än trivial LED/knapp-koppling ska ha ett separat strömförsörjningsavsnitt.

Motiv: Många Arduino-fel handlar om ström, gemensam GND, USB-begränsningar och externa laster.

### 4. Mermaid används endast för logisk översikt

Beslut: Mermaid får användas för att visa relationer men inte presenteras som exakt kopplingsschema.

Motiv: Mermaid är bra för överblick men dåligt för exakta breadboarddetaljer.

### 5. SVG skjuts fram till senare version

Beslut: I steg 9 definieras SVG som framtida bildunderlag, inte som krav för MVP.

Motiv: Projektet behöver först ha stabila regler för komponenter, säkerhet, kopplingstabeller och kod. SVG-bilder kan byggas ovanpå detta i ett senare steg.

### 6. Osäkerhet ska synas

Beslut: GPT:n ska markera när modulvariant, pinout eller spänning är antagen.

Motiv: Elektronikmoduler med samma namn kan ha olika pinout, logiknivå eller integrerade motstånd. GPT:n ska inte skapa falsk precision.

### 7. Kontroll mot kod är obligatorisk

Beslut: Kopplingstabell och kod ska kontrolleras mot varandra.

Motiv: Ett vanligt fel är att koden använder pinnar som inte matchar kopplingstabellen.

## Konsekvens för kommande steg

Steg 10 kan bygga vidare på denna standard när dokumentationsmallar skapas. Senare steg om projektbibliotek och bok-/kursintegration kan använda kopplingstabellen som stabil grund för genererade experiment.
