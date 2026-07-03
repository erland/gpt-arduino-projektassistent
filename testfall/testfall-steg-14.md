# Testfall – Steg 14

Dessa testfall verifierar att GPT Builder-konfigurationen för MVP:n är korrekt.

## Testfall 14.1 – Rätt instruktion används

Prompt:

```text
Vad är ditt uppdrag?
```

Förväntat beteende:

- GPT:n beskriver sig som en Arduino-projektassistent
- den nämner projekt, komponenter, koppling, kod, dokumentation och felsökning
- den nämner säkerhet och nivåanpassning

## Testfall 14.2 – Knowledge-filer används

Prompt:

```text
Vilken typ av svar bör du ge om jag ber om ett byggbart Arduino-projekt?
```

Förväntat beteende:

- GPT:n nämner projektöversikt, komponentlista, kopplingstabell, kod, test, felsökning och säkerhet
- den följer leveransmallarna från Knowledge

## Testfall 14.3 – Webbsökning avstängd

Prompt:

```text
Vad kostar exakt en Arduino Uno idag?
```

Förväntat beteende om webbsökning är av:

- GPT:n säger att aktuellt pris behöver kontrolleras
- ger möjligen grov prisnivå
- låtsas inte känna till dagsaktuellt pris

## Testfall 14.4 – Webbsökning påslagen

Prompt:

```text
Kan du hitta aktuella priser på Arduino Uno och ESP32 i Sverige?
```

Förväntat beteende om webbsökning är på:

- GPT:n söker eller anger att den använder aktuella källor
- skiljer mellan pris, frakt och tillgänglighet
- föreslår inte billigaste alternativet om det innebär teknisk eller säkerhetsmässig risk

## Testfall 14.5 – Bildgenerering inte central

Prompt:

```text
Rita en koppling för Arduino Uno, LED och knapp.
```

Förväntat beteende i MVP:

- GPT:n prioriterar kopplingstabell och pin-tabell
- den kan eventuellt ge enkel textskiss
- den låtsas inte skapa ett verifierat CAD-schema

## Testfall 14.6 – Actions saknas

Prompt:

```text
Hämta lagerstatus från en elektronikbutik via API.
```

Förväntat beteende:

- GPT:n förklarar att MVP:n inte har butik/API-koppling
- föreslår söktermer eller manuell kontroll
- hittar inte på lagerstatus
