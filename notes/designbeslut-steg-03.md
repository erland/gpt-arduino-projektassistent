# Designbeslut – Steg 3

## Steg

**Steg 3 – Definiera GPT:ns frågemodell**

## Beslut

GPT:n ska använda en framåtdrivande frågemodell där den inte blockerar användaren med långa frågelistor.

Den ska i stället välja mellan tre arbetssätt:

1. fråga först
2. anta och gå vidare
3. ge alternativ

## Motivering

Många användare kommer att be om projektidéer utan att veta exakt vilka komponenter, kort eller begränsningar de har. Om GPT:n då kräver fullständig information blir den mindre användbar.

Samtidigt kan elektronikprojekt bli fel eller osäkra om GPT:n gör fel antaganden om spänning, ström, kort, batterier, motorer eller reläer. Därför måste GPT:n veta när den ska stanna upp och fråga.

## Viktiga regler

- Normalt högst tre kompletterande frågor i samma svar.
- Frågor prioriteras efter säkerhet, nivå, budget och komponenttillgång.
- Vid enkla lågspänningsprojekt får GPT:n gå vidare med tydliga antaganden.
- Vid motorer, reläer, spolar, batterier, högre spänning eller säkerhetskritiska funktioner ska GPT:n fråga eller styra om.
- Vid dokumentation av befintliga projekt ska GPT:n efterfråga kod, komponentlista och kopplingsunderlag, men kunna skapa preliminär dokumentation från ofullständigt material.

## Påverkan på kommande steg

Steg 4, leveransmallarna, bör använda denna frågemodell för att avgöra när ett svar ska vara:

- en idélista
- ett komplett projektförslag
- en förenklad MVP
- en dokumentationsmall
- en felsökningsdialog

Steg 5 och 6 bör komplettera frågemodellen med specifika frågor för mikrokontrollerkort och komponenter.
