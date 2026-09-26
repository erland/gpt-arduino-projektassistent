# GPT Byggaren 1.5.0 – migreringsplan

Projekt: **Arduino-projektassistenten**

## Preserve-first baseline

Migreringen ska bevara:
- version **1.0.0**
- exakt **15 Knowledge-filer**
- den exakta runtime-instruktion som idag extraheras ur `gpt-instructions/12-gpt-huvudinstruktion.md`
- säker lågspänningselektronik som överordnad princip
- kontroll av spänning, ström, logiknivå och gemensam GND
- förbud mot direktdrivning av externa laster från GPIO
- kopplingstabell före eller tillsammans med kod
- konsekvens mellan pin-tabell, kod och komponentval
- nivåanpassning 0–4
- högst tre kompletterande frågor normalt
- tydlig hantering av antaganden och osäkerhet
- `circuit.yaml` enligt Circuit SVG Generator v1.1
- nuvarande Chat- och Custom GPT-distributioner

## Steg

1. Etablera canonical instruktion och projektkontrakt.
2. Normalisera capability-, artifact-, workspace/state- och tool-kontrakt.
3. Normalisera Chat och Custom GPT till samma canonical källa.
4. Bedöm Claude Projects och OpenCode.
5. Bedöm OpenAI Plugin.
6. Generalisera build, parity, CI och release via runtime-registry.
7. Slutlig readiness, dokumentationssynk och 7/7-gate.

## Aktivering av nya runtimes

En runtime får bara aktiveras om den kan bevara säkerhetsregler, strukturerad projektleverans, kod/kopplingskonsistens och `circuit.yaml`-arbetsflödet utan kritisk degradering.
