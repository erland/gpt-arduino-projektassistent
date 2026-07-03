# Installationsguide – MVP i GPT Builder

Denna guide beskriver hur första MVP-versionen av Arduino-projektassistenten skapas i GPT Builder.

## 1. Skapa ny GPT

Skapa en ny GPT i GPT Builder.

Föreslaget namn:

```text
Arduino-projektassistenten
```

Föreslagen beskrivning:

```text
Hjälper dig att välja, planera, bygga, dokumentera och felsöka Arduino-baserade elektronikprojekt med rätt nivå, komponenter, koppling och kod.
```

## 2. Klistra in huvudinstruktionen

Öppna filen:

```text
gpt-instructions/12-gpt-huvudinstruktion.md
```

Använd fullversionen av instruktionen i GPT Builder.

Kontrollera att instruktionen inte ersätts av arbetsanteckningar från andra filer.

## 3. Ladda upp Knowledge-filer

Ladda upp alla filer i:

```text
knowledge/
```

Använd listan i:

```text
gpt-builder/02-uppladdningslista-knowledge.md
```

## 4. Ställ in capabilities

Rekommenderad MVP-konfiguration:

| Capability | MVP-rekommendation |
|---|---|
| Webbsökning | På om aktuella priser/produkter ska stödjas, annars av i första internversion |
| Bildgenerering | Av |
| Code Interpreter / avancerad dataanalys | Valfri, inte nödvändig |
| Actions | Av |

## 5. Lägg inte till Actions i MVP

Första versionen ska inte kopplas till externa API:er. Det gör felsökning och kvalitetssäkring enklare.

Actions kan läggas till senare för:

- produktpriser
- butikslager
- komponentdatabaser
- intern projektdatabas

## 6. Spara som privat testversion

Rekommendation:

```text
Börja som privat GPT.
```

Publicera inte brett förrän steg 16–18 är genomförda och testfallen visar att säkerhets- och hallucinationsskyddet fungerar.

## 7. Kör första verifiering

Använd testlistan i:

```text
gpt-builder/04-forsta-verifiering.md
```

Om GPT:n missar säkerhetskritiska regler ska instruktion eller Knowledge-filer justeras innan GPT:n används vidare.
