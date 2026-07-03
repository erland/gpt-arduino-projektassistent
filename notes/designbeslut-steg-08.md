# Designbeslut – steg 8: kodstandard för Arduino

## Beslut

Steg 8 inför en separat kodstandard för hur GPT:n ska skriva, förklara och granska Arduino-kod.

Kodstandarden delas upp i:

- bindande instruktionsutkast i `gpt-instructions/08-kodstandard-arduino.md`,
- mer utförlig Knowledge-fil i `knowledge/08-kodstandard-arduino.md`,
- testfall i `testfall/testfall-steg-08.md`.

## Motiv

Arduino-projektassistenten ska inte bara kunna välja komponenter och skapa kopplingstabeller. Den behöver även skriva kod som:

- stämmer med valt kort,
- stämmer med kopplingstabellen,
- är begriplig för rätt nivå,
- använder rätt bibliotek,
- inte döljer säkerhetsproblem,
- går att testa steg för steg.

Utan en kodstandard finns risk att GPT:n skriver kod som fungerar i teorin men inte passar användarens hårdvara eller nivå.

## Viktiga principer

### Komplett kod först

För byggbara projekt ska GPT:n normalt ge en komplett skiss, inte bara utspridda fragment.

### Kod ska följa kopplingen

Pinnar i koden ska matcha kopplingstabellen. Om kopplingen saknas ska GPT:n antingen skapa den först eller ange antaganden.

### Nivåanpassning

Nybörjare ska få enklare kod. Mer erfarna användare kan få mer strukturerad kod, men koden ska fortfarande vara tydlig.

### Säkerhet före kodgenerering

GPT:n ska inte skriva kod som normaliserar osäkra kopplingar, exempelvis motor direkt från GPIO.

### `delay()` är inte förbjudet

`delay()` tillåts i mycket enkla nybörjarprojekt. `millis()` ska föredras när projektet behöver reagera på flera saker samtidigt.

## Avgränsningar

Steg 8 definierar kodstandard, men inte:

- fullständig dokumentationsstandard,
- ritnings-/SVG-standard,
- inköps- och prislogik,
- slutlig sammanhållen GPT-instruktion.

Dessa hanteras i senare steg enligt planen.

## Särskilda vägval

### Arduino IDE som standard

Koden ska som standard vara kompatibel med Arduino IDE eftersom det är mest pedagogiskt och lättillgängligt.

### Plattformsspecifik försiktighet

ESP32 och ESP8266 hanteras särskilt försiktigt eftersom pinval, PWM, ADC, bibliotek och logiknivåer skiljer sig från klassiska Arduino-kort.

### Bibliotek ska anges tydligt

GPT:n ska inte anta att användaren vet vilka bibliotek som krävs. Bibliotek och eventuell installation ska anges i kodleveransen.

## Risker som kodstandarden minskar

- kod som inte matchar kopplingen,
- fel aktiv låg/aktiv hög-logik,
- fel PWM-pin,
- ESP8266 D/GPIO-förväxling,
- ESP32/5 V-risker,
- motor- eller reläkod utan säker hårdvaruvarning,
- för avancerad kod för nybörjare,
- saknade bibliotek,
- lång blockerande kod där respons krävs.
