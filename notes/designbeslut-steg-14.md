# Designbeslut – Steg 14

## Beslut

Steg 14 gör GPT:n byggbar som MVP i GPT Builder genom att lägga till praktiska installations- och konfigurationsfiler.

## Viktigaste designbeslut

### 1. MVP:n ska vara Knowledge-styrd, inte Action-styrd

Första versionen ska inte använda externa API:er eller Actions.

Skäl:

- enklare att testa
- mindre risk för käll- och API-fel
- säkerhets- och nivålogik kan verifieras först

### 2. Bildgenerering ska vara av i första MVP

Skäl:

- genererade kopplingsbilder kan vara svåra att verifiera
- textbaserade kopplingstabeller är säkrare i första versionen
- framtida SVG-standard bör byggas separat

### 3. Webbsökning är valfri

Webbsökning kan vara användbar för aktuella priser och produktvarianter, men MVP:n ska fungera även utan webbsökning.

Därför måste prisreglerna kunna hantera båda lägena.

### 4. Endast `knowledge/` laddas upp som Knowledge

Projektet innehåller många stöd- och arbetsfiler. För att undvika förvirring ska bara de normaliserade Knowledge-filerna laddas upp i GPT Builder.

### 5. GPT:n bör börja som privat testversion

Publicering bör vänta tills typfall, hallucinationsskydd och granskningschecklista är klara.

## Konsekvens

Efter steg 14 finns allt som behövs för att skapa en första privat MVP av GPT:n i GPT Builder.
