# Designbeslut – Steg 13

## Steg

Steg 13 enligt `[PLAN-GPT-ARDUINO]`: Skapa Knowledge-filstrukturen.

## Beslut 1 – Behåll en samlad MVP-struktur

Komponentkatalogen och övriga kärnfiler delas inte upp ännu. De är fortfarande hanterbara och bör testas som sammanhängande MVP-underlag innan finare uppdelning görs.

## Beslut 2 – Lägg till ett Knowledge-index

En ny fil `knowledge/00-knowledge-index.md` har lagts till. Den fungerar som karta över Knowledge-paketet och visar vilka filer som bör användas för olika uppgiftstyper.

## Beslut 3 – Skapa explicit prioriteringsordning

Knowledge-strukturen definierar att säkerhet och elektrisk rimlighet alltid väger tyngre än nivå, budget, pedagogik och önskad svarsform.

## Beslut 4 – Huvudinstruktionen är primärt instruktion, inte vanlig Knowledge

`12-gpt-huvudinstruktion.md` behålls i Knowledge-mappen som källa och referens, men huvudrekommendationen är att dess innehåll används i GPT Builder-instruktionsfältet.

## Beslut 5 – Framtida uppdelning dokumenteras men genomförs inte ännu

Filen `13-knowledge-filstruktur.md` beskriver hur komponentkatalog och projektbibliotek kan delas upp senare. Detta gör att framtida steg kan byggas ut utan att skapa en spretig struktur redan nu.

## Beslut 6 – Steg 13 är ett struktursteg

Steg 13 lägger i första hand till organisation, index och underhållsregler. Det förändrar inte kärnreglerna för säkerhet, komponentval, kod eller dokumentation från tidigare steg.

