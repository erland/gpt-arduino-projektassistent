# Arduino-projektassistenten – portabel Chat-version

Detta paket gör det möjligt att använda Arduino-projektassistentens nuvarande GPT-konfiguration i en vanlig ChatGPT-konversation.

## Start

1. Läs först `assistant/instructions.txt` och använd innehållet som arbetsinstruktion för resten av konversationen.
2. Använd filerna i `knowledge/` som permanent referensmaterial och följ deras prioriteringar, särskilt säkerhetsreglerna.
3. Vid konflikt gäller användarens aktuella instruktioner inom ramen för överordnade säkerhets- och systemregler, därefter `assistant/instructions.txt`, därefter de mer specifika Knowledge-filerna.
4. Läs relevanta Knowledge-filer innan du lämnar byggbara kopplingar, kod, komponentval eller säkerhetsråd.
5. Behåll denna arbetsmodell under hela chatten.

## Viktigt

`assistant/instructions.txt` genereras direkt från blocket **Färdig huvudinstruktion för GPT Builder** i repositoryts `gpt-instructions/12-gpt-huvudinstruktion.md`. Knowledge-filerna kopieras byte-identiskt från repositoryts `knowledge/`.

Projektets historiska `notes/`, `testfall/` och övriga utvecklingsdokument ingår inte eftersom de uttryckligen inte är GPT Knowledge i den nuvarande konfigurationen.
