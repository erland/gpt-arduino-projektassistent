# Designbeslut – Steg 12

## Syfte

Steg 12 skapar en huvudinstruktion som kan användas i GPT Builder. Tidigare steg har byggt detaljreglerna; detta steg sammanfattar dem till en styrande instruktion som anger roll, prioriteringar och bindande beteende.

## Designbeslut

### 1. Huvudinstruktionen hålls relativt kompakt

Detaljer som komponentposter, fulla mallar och alla kortspecifika regler dupliceras inte i huvudinstruktionen. Dessa ska ligga kvar i Knowledge-filerna. Huvudinstruktionen ska vara tillräckligt tydlig för att styra GPT:n, men inte så lång att den blir svår att underhålla.

### 2. Säkerhet placeras högt och upprepas avsiktligt

Flera säkerhetsregler återkommer i komprimerad form:

- ingen direktstyrning av laster från GPIO
- kontroll av 5 V/3,3 V
- försiktighet med motorer, reläer, elektromagneter och batterier
- undvikande av nätspänning som hobbykoppling

Detta är medvetet eftersom säkerhetsregler måste vara synliga även utan att GPT:n hämtar exakt rätt Knowledge-avsnitt.

### 3. Kopplingstabell görs obligatorisk för byggbara projekt

Huvudinstruktionen kräver att byggbara projekt innehåller kopplingstabell. Det gör projekten lättare att granska och minskar risken för att kod och koppling glider isär.

### 4. Kod får inte skapas frikopplat från hårdvara

Instruktionen betonar att kod, pin-tabell, komponentlista och valt kort måste stämma överens. Detta minskar risken för generisk Arduino-kod som inte passar det föreslagna projektet.

### 5. Prisregler hålls ärliga

Huvudinstruktionen säger att pris ska hanteras som grov uppskattning om aktuella priser inte är verifierade. Detta förhindrar att GPT:n låtsas känna till lagerstatus eller aktuella erbjudanden.

### 6. Svensk standardton

Eftersom projektet primärt utvecklas på svenska anger instruktionen att svenska ska vara standardspråk när användaren skriver svenska.

### 7. Kortversion inkluderas

En kortversion har lagts till för situationer där GPT Builder eller framtida verktyg har begränsat instruktionsutrymme. Huvudversionen är dock den rekommenderade.

## Påverkan på kommande steg

Steg 13 bör utgå från denna huvudinstruktion och därefter skapa en mer slutlig Knowledge-filstruktur för uppladdning i GPT Builder.

Steg 14 kan sedan använda:

- huvudinstruktionen som Custom GPT-instruktion
- Knowledge-filerna som uppladdade filer
- testfallen som kontrollmaterial

## Risker att bevaka

- Huvudinstruktionen kan fortfarande vara för lång om GPT Builder-miljön har praktiska längdbegränsningar.
- Kommande steg bör kontrollera att Knowledge-filerna inte överlappar för mycket.
- Det kan behövas en ännu mer strikt policy för webbsökning när aktuella produktrekommendationer ska ges.
- När SVG- eller ritningsstöd byggs ut behöver huvudinstruktionen eventuellt kompletteras med en kort ritningsregel.
