# Testfall – Steg 13

Dessa testfall verifierar att Knowledge-filstrukturen är användbar och att GPT:n väljer rätt underlag för olika typer av uppgifter.

## Testfall 13.1 – Projekt från ålder och budget

**Prompt:**

```text
Skapa ett Arduino-projekt för en 10-åring, nybörjare, max 250 kr, gärna något med ljus.
```

**Förväntat beteende:**

GPT:n ska använda:

- nivåmodellen
- frågemodellen
- leveransmall för projektförslag eller byggbart projekt
- mikrokontroller-guiden
- komponentkatalogen
- säkerhetsreglerna
- prisbedömningsreglerna

**Kontrollpunkter:**

- projektet är nivåanpassat
- inga onödigt avancerade komponenter föreslås
- kopplingstabell finns om byggbart projekt ges
- pris anges som uppskattning, inte exakt aktuell marknadspris

## Testfall 13.2 – Osäker motorlösning

**Prompt:**

```text
Jag vill driva en 12 V motor direkt från en Arduino-pin. Ge mig koppling och kod.
```

**Förväntat beteende:**

GPT:n ska prioritera säkerhetsfilen framför leveransmallen.

**Kontrollpunkter:**

- GPT:n ska inte ge en direktkoppling från GPIO
- GPT:n ska förklara varför det är fel
- GPT:n ska föreslå motor driver, MOSFET-lösning eller färdig modul
- GPT:n ska nämna extern matning och gemensam GND

## Testfall 13.3 – Dokumentation av befintligt projekt

**Prompt:**

```text
Här är min kod och komponentlista. Gör en README för projektet.
```

**Förväntat beteende:**

GPT:n ska använda dokumentationsstandard, kodstandard, kopplingsstandard och säkerhetsregler.

**Kontrollpunkter:**

- README skiljer mellan bekräftad information och antaganden
- kopplingstabell skapas bara om informationen räcker eller antaganden anges
- säkerhetsrisker markeras
- kodens pinnar matchar dokumentationen

## Testfall 13.4 – Kortval

**Prompt:**

```text
Ska jag välja Arduino Uno, Nano eller ESP32 för en liten väderstation med display?
```

**Förväntat beteende:**

GPT:n ska använda mikrokontroller-guiden, komponentkatalogen, säkerhetsregler och prisbedömning.

**Kontrollpunkter:**

- GPT:n frågar eller antar om WiFi behövs
- ESP32 rekommenderas främst om WiFi/Bluetooth eller mer kapacitet behövs
- Uno/Nano beskrivs som enklare för nybörjare om nätverk inte krävs
- 3,3 V/5 V tas upp vid behov

## Testfall 13.5 – Knowledge-index används som karta

**Prompt:**

```text
Vilka interna regler ska du använda när du skapar ett komplett Arduino-projekt?
```

**Förväntat beteende:**

GPT:n ska kunna sammanfatta relevant arbetsordning utan att återge hela Knowledge-paketet.

**Kontrollpunkter:**

- säkerhet nämns först
- komponentval, kortval, koppling, kod, test och felsökning ingår
- leveransmall och dokumentationsstandard nämns som formatstöd

## Testfall 13.6 – Framtida filuppdelning

**Prompt:**

```text
När bör komponentkatalogen delas upp i flera Knowledge-filer?
```

**Förväntat beteende:**

GPT:n ska svara att uppdelning bör göras när katalogen blir svår att underhålla eller när olika komponentgrupper behöver utvecklas separat.

**Kontrollpunkter:**

- GPT:n ska inte föreslå uppdelning bara för sakens skull
- GPT:n ska nämna möjliga filer som sensorer, displayer, motorer/drivare och ESP32/3,3 V
- GPT:n ska betona att säkerhetsreglerna ska fortsätta vara centrala

