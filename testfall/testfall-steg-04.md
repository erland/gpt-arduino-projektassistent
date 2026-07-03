# Testfall – Steg 4: Leveransmallar

Dessa testfall används för att kontrollera att GPT:n väljer rätt leveransmall och ger svar med lämplig struktur.

## Testfall 4.1 – Projektidéer för barn

### Prompt

```text
Skapa några Arduino-projekt för en 9-åring som är nybörjare. Max 200 kr. Gärna något med ljus.
```

### Förväntat beteende

GPT:n ska använda mallen för flera projektförslag.

Svaret bör innehålla:

- 2–4 projektförslag
- nivåangivelse
- ungefärlig kostnad
- kort motivering
- rekommenderat förstaval
- nästa steg

GPT:n ska inte direkt leverera ett stort komplett projekt om användaren först verkar vilja välja mellan idéer.

## Testfall 4.2 – Komplett projekt från idé

### Prompt

```text
Jag vill bygga en automatisk nattlampa med Arduino. Gör ett komplett projekt med komponenter, koppling och kod.
```

### Förväntat beteende

GPT:n ska använda komplett projektmall.

Svaret bör innehålla:

- projektöversikt
- antaganden
- målgrupp och nivå
- rekommenderad mikrokontroller
- komponentlista
- kopplingstabell
- kod
- teststeg
- felsökning
- säkerhetsnoteringar
- förbättringsförslag

## Testfall 4.3 – Dokumentation av befintligt projekt

### Prompt

```text
Här är min kod till ett Arduino-projekt med knapp och LED. Skapa dokumentation som passar en elevinstruktion.
```

### Förväntat beteende

GPT:n ska använda dokumentationsmall.

Svaret bör innehålla:

- projektnamn
- sammanfattning
- funktion
- målgrupp
- komponenter
- koppling eller antagande om koppling
- kodförklaring
- testinstruktioner
- felsökning
- osäkerheter att verifiera

GPT:n ska inte hitta på säkra kopplingar om koden eller underlaget inte visar dem.

## Testfall 4.4 – Kortval

### Prompt

```text
Borde jag använda Arduino Uno, Nano eller ESP32 till en väderstation med display?
```

### Förväntat beteende

GPT:n ska använda kortvalsmall eller jämförelsemall.

Svaret bör innehålla:

- tydlig rekommendation
- jämförelse av alternativen
- motivering utifrån display, sensorer, WiFi-behov, nivå och pris
- 3,3 V-varning om ESP32 nämns
- slutsats

## Testfall 4.5 – Komponentval

### Prompt

```text
Vilken motorsstyrning bör jag välja för två små DC-motorer i ett Arduino-projekt?
```

### Förväntat beteende

GPT:n ska använda komponentvalsmall.

Svaret bör innehålla:

- rekommenderad motorstyrning
- alternativ
- varför valet passar
- kompatibilitet med Arduino och eventuell ESP32
- krav på extern matning och gemensam GND
- vanliga fallgropar

GPT:n ska inte föreslå att motorer drivs direkt från GPIO.

## Testfall 4.6 – Koppling

### Prompt

```text
Hur kopplar jag en LED och en knapp till Arduino Uno?
```

### Förväntat beteende

GPT:n ska använda kopplingstabell.

Svaret bör innehålla:

- förutsättningar
- konkret kopplingstabell
- motstånd till LED
- INPUT_PULLUP eller annan tydlig knappstrategi
- kontroll innan start

## Testfall 4.7 – Kod

### Prompt

```text
Skriv kod för att tända en LED när jag trycker på en knapp.
```

### Förväntat beteende

GPT:n ska använda kodmall.

Svaret bör innehålla:

- antaget kort
- pinlista
- komplett kod
- kort kodförklaring
- teststeg

Koden och pinlistan ska stämma överens.

## Testfall 4.8 – Felsökning

### Prompt

```text
Min OLED-display visar inget när jag kopplar den till min Arduino Nano. Vad kan vara fel?
```

### Förväntat beteende

GPT:n ska använda felsökningsmall.

Svaret bör innehålla:

- troligaste orsaker
- snabba kontroller
- stegvis felsökning
- I2C-adress som möjlig orsak
- GND, VCC, SDA, SCL som tidiga kontroller
- bibliotek och exempelprogram

## Testfall 4.9 – Enkel fråga

### Prompt

```text
Måste jag ha ett motstånd till en LED?
```

### Förväntat beteende

GPT:n ska använda kort pedagogisk förklaring.

Svaret bör vara kort men tydligt och säga att LED normalt ska ha seriemotstånd för att begränsa strömmen.

## Testfall 4.10 – Kort fråga med säkerhetsrisk

### Prompt

```text
Kan jag koppla en 12 V motor direkt till en Arduino-pin?
```

### Förväntat beteende

GPT:n ska svara kort men med tydlig säkerhetsgräns.

Svaret ska säga nej och förklara att motor kräver motorstyrning/transistor/MOSFET, extern matning, gemensam GND och skydd mot induktionsspikar beroende på lösning.
