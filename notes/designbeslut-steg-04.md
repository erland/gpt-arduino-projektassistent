# Designbeslut – Steg 4: Leveransmallar

## Bakgrund

Steg 4 enligt [PLAN-GPT-ARDUINO] handlar om att skapa leveransmallar. Syftet är att GPT:n inte ska ge spretiga svar utan följa tydliga strukturer beroende på användarens behov.

## Beslut 1 – Flera mallar i stället för en universalmall

Vi använder flera mallar i stället för en enda projektmall.

Motiv:

- En felsökningsfråga ska inte få samma struktur som ett komplett projekt.
- Ett kortval kräver annan information än dokumentation av befintligt projekt.
- Nybörjare behöver kortare och tydligare svar än avancerade användare.

## Beslut 2 – Komplett projektmall ska innehålla både koppling och kod

Ett byggbart projekt ska inte bara innehålla idé och komponentlista. Det ska även innehålla kopplingstabell, kod, teststeg och felsökning.

Motiv:

- Det minskar risken för att användaren fastnar mellan idé och genomförande.
- Det gör svaret lättare att granska.
- Det gör GPT:n mer användbar som praktisk projektassistent.

## Beslut 3 – Kopplingstabell är standardformat

Kopplingstabell väljs som primär representation för kopplingar i MVP:n.

Motiv:

- Tabeller är lättare att kontrollera än genererade bilder.
- De fungerar i text, README, bokkapitel och dokumentation.
- De kan senare ligga till grund för SVG- eller diagramgenerering.

## Beslut 4 – Säkerhetsinformation får inte försvinna i korta svar

Även när användaren ber om ett kort svar ska GPT:n lägga till en kort säkerhetsnotering om ämnet rör riskområden som motorer, reläer, spänning, batterier eller 3,3 V/5 V.

Motiv:

- Elektronikfel kan skada komponenter eller skapa farliga situationer.
- Korta svar får inte bli vilseledande.

## Beslut 5 – Antaganden ska ligga nära början

När information saknas ska GPT:n ange antaganden tidigt i svaret.

Motiv:

- Användaren kan snabbt se om svaret bygger på fel kort, fel spänning eller fel nivå.
- Det minskar risken för att användaren bygger utifrån dolda antaganden.

## Beslut 6 – Mallarna ska kunna användas både i GPT-instruktion och Knowledge

Det finns en kortare instruktion i `gpt-instructions/04-leveransmallar.md` och en mer utförlig Knowledge-version i `knowledge/04-leveransmallar.md`.

Motiv:

- GPT-instruktionen bör hållas relativt bindande och överskådlig.
- Knowledge-filen kan innehålla längre mallar, exempel och kvalitetskriterier.

## Konsekvens för kommande steg

Nästa steg kan bygga vidare på mallarna:

- Steg 5 kan fylla kortvalsmallen med konkret mikrokontrollerkunskap.
- Steg 6 kan fylla komponentvalsmallen med komponentkatalog.
- Steg 7 kan stärka kopplings- och säkerhetsdelarna.
- Steg 8 kan koppla kodstandard till kodmallen.
