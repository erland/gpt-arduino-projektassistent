# Designbeslut – Steg 11

## Steg

**Steg 11 – Skapa inköps- och prisbedömningsregler**

## Syfte

Syftet med detta steg är att ge GPT:n ett kontrollerat sätt att resonera om budget, inköp och komponentalternativ utan att hallucinera aktuella priser eller produktrekommendationer.

## Viktigaste designbeslut

### 1. Pris ska behandlas som uppskattning om det inte är verifierat

GPT:n ska inte ange exakta aktuella priser utan källa eller användardata. Den ska använda grova prisnivåer och tydliga reservationer.

Motivering:

- elektronikpriser ändras snabbt
- frakt påverkar småorder mycket
- lagerstatus och produktvarianter förändras
- GPT:n ska vara trovärdig och inte låtsas veta mer än den gör

### 2. Komponentlista och inköpslista hålls isär

Komponentlista beskriver vad projektet tekniskt behöver. Inköpslista beskriver vad användaren behöver köpa.

Motivering:

- användaren kan redan ha basutrustning
- projektkostnaden kan annars bli missvisande
- samma projekt kan vara billigt eller dyrt beroende på vad användaren redan äger

### 3. Två budgetscenarier ska användas

GPT:n ska ofta skilja på:

- användaren har redan kort, breadboard och basdelar
- användaren behöver köpa allt från början

Motivering:

- detta är den största skillnaden i nybörjarprojekt
- det minskar risken att projekt framstår som billigare än de är

### 4. Relativa prisnivåer prioriteras framför exakta priser

Prisnivåer som mycket låg, låg, medel, högre och kostnadsrisk används som huvudmodell.

Motivering:

- fungerar utan aktuell prisdatabas
- räcker ofta för projektplanering
- gör att GPT:n kan resonera ärligt och stabilt

### 5. Billigaste rimliga variant och robustare variant

När budget är viktig ska GPT:n kunna ge både en billigare och en robustare variant.

Motivering:

- användare får bättre beslutsstöd
- nybörjare kan välja enklare felsökning
- mer erfarna kan välja lägre pris

### 6. Säkerhetskritiska delar får inte sparas bort

Reglerna markerar att skyddsdiod, drivsteg, motstånd, nivåanpassning och separat matning inte får tas bort för att minska kostnaden.

Motivering:

- lägre pris får inte leda till skadade komponenter eller farliga kopplingar
- detta förstärker tidigare säkerhetssteg

### 7. Specifika produktrekommendationer kräver aktuell kontroll eller användardata

GPT:n får ge specifika produktförslag om användaren ger alternativen eller om aktuell webbsökning används. Annars ska GPT:n hellre ge söktermer och kontrollpunkter.

Motivering:

- undviker falsk precision
- passar både GPT med och utan webbsökning
- gör Knowledge-filen användbar över tid

## Tillagda filer

- `gpt-instructions/11-inkops-och-prisbedomning.md`
- `knowledge/11-inkops-och-prisbedomning.md`
- `notes/designbeslut-steg-11.md`
- `testfall/testfall-steg-11.md`

## Påverkan på tidigare steg

Steg 11 kompletterar särskilt:

- steg 4, eftersom leveransmallar nu kan innehålla prisnivå och budgetavsnitt
- steg 5, eftersom kortval ofta påverkas av pris kontra robusthet
- steg 6, eftersom komponentval nu får budget- och kvalitetsdimension
- steg 7, eftersom säkerhetskritiska delar inte får sparas bort
- steg 10, eftersom dokumentation kan separera teknisk komponentlista från praktisk inköpslista

## Avsiktlig avgränsning

Detta steg skapar inte en aktuell prisdatabas och inte någon integration mot återförsäljare. Sådant hör hemma i senare versioner om GPT:n får webbsökning eller Actions/API-stöd.
