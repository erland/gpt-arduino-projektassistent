# GPT Builder-underlag

Denna katalog innehåller praktiska filer för att skapa första MVP-versionen av Arduino-projektassistenten i GPT Builder.

Filerna i denna katalog är **inte** avsedda att laddas upp som Knowledge i första MVP:n. De är installations-, konfigurations- och kontrollstöd.

## Filer

- `01-installationsguide-mvp.md` – steg-för-steg-guide för att skapa GPT:n
- `02-uppladdningslista-knowledge.md` – exakt lista över Knowledge-filer som ska laddas upp
- `03-capabilities-och-installningar.md` – rekommenderade capabilities och inställningar
- `04-forsta-verifiering.md` – första verifiering efter att GPT:n skapats

## Viktig regel

I GPT Builder ska följande användas:

- **Instruktion:** texten från `gpt-instructions/12-gpt-huvudinstruktion.md`
- **Knowledge:** filerna i `knowledge/`

Ladda inte upp hela projektpaketet som Knowledge. Det skulle göra GPT:n rörigare och riskera att blanda arbetsmaterial, testfall och faktiska styrfiler.
