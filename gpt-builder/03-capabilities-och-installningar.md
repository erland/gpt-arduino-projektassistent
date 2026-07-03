# Capabilities och inställningar för MVP

## Rekommenderad MVP-inställning

| Inställning | Rekommendation | Kommentar |
|---|---|---|
| Standardspråk | Svenska | GPT:n kan byta språk om användaren uttryckligen ber om det. |
| Webbsökning | Valfri | Aktiveras om aktuella priser/produkter ska stödjas. |
| Bildgenerering | Av | Inte tillräckligt verifierbart för första tekniska MVP:n. |
| Code Interpreter | Valfri/av | Inte nödvändig för första MVP:n. |
| Actions | Av | Vänta tills basbeteendet är testat. |

## Webbsökning

Webbsökning kan vara användbar för:

- aktuella priser
- tillgängliga produktvarianter
- om en specifik modul fortfarande säljs
- jämförelse mellan butiker
- verifiering av pinout eller specifikationer när användaren anger exakt modul

Om webbsökning är avstängd ska GPT:n:

- ge grova prisnivåer
- säga att aktuella priser behöver kontrolleras
- ge söktermer i stället för exakta butikslänkar

## Bildgenerering

Bildgenerering bör vara av i MVP.

Skäl:

- kopplingstabeller är mer verifierbara
- genererade bilder kan ge felaktiga kopplingar
- SVG-/ritningsstandard bör testas separat senare

GPT:n kan ändå ge:

- kopplingstabell
- pin-tabell
- textbaserad byggordning
- enkel ASCII-skiss vid behov
- Mermaid-diagram för logiska relationer

## Code Interpreter

Code Interpreter är inte ett krav för MVP.

Det kan bli användbart senare för:

- analysera större kodbaser
- läsa uppladdade komponentlistor
- skapa tabeller
- generera dokumentationsunderlag
- paketera projektfiler

## Actions

Actions ska vara av i första MVP.

Möjliga framtida Actions:

- produkt- och prisuppslag
- komponentdatabas
- intern projektdatabas
- export till dokumentationssystem

Innan Actions aktiveras behövs separata regler för:

- datakvalitet
- källhänvisning
- sekretess
- felhantering
- fallback när API:er inte svarar
