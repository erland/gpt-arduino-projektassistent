# Designbeslut – SVG-generator v1.1 i Arduino-GPT

## Beslut

GPT-paketet uppdateras för att stödja Circuit SVG Generator v1.1 genom att ersätta den tidigare v1-baserade generator-Knowledge-filen med en v1.1-baserad version.

## Motivering

Generatorn har nu stöd för fler boards och fler komponenttyper. Om GPT:n fortsätter använda v1-regler skulle den i onödan falla tillbaka till `generic_module` eller säga att fullt renderbara projekt inte stöds.

## Avgränsning

Själva SVG-generatorns kod inkluderas inte i GPT-paketet. GPT:n ska bara kunna skapa korrekt `circuit.yaml` och förklara hur den används.

## Viktigt

Generatorn gör inte fullständig elsäkerhetsanalys. GPT:n ska därför fortfarande prioritera säkerhets- och kopplingsreglerna före renderbarhet.
