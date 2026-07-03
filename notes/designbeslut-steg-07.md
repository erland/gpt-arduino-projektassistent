# Designbeslut – steg 7

## Steg

**Steg 7 – Skapa kopplingsregler och säkerhetsregler**

## Beslut 1: Säkerhet ska vara ett separat lager

Kopplings- och säkerhetsreglerna har lagts i egna filer i stället för att enbart ligga inbäddade i komponentkatalogen.

Skäl:

- samma säkerhetsregler gäller många komponenter,
- GPT:n behöver kunna kontrollera projekt som kombinerar flera komponenter,
- säkerhetsregler ska kunna prioriteras högre än komponentval och projektidéer,
- framtida steg kan bygga ritningsstandard och kodstandard ovanpå samma regler.

## Beslut 2: Reglerna är konservativa

Reglerna är avsiktligt försiktiga. GPT:n ska inte försöka optimera för lägsta pris eller minsta antal komponenter om det gör kopplingen osäker.

Exempel:

- motorer ska inte drivas direkt från GPIO,
- 5 V-signaler ska inte kopplas direkt till ESP32-ingångar,
- nätspänning ska styras om till säkrare alternativ,
- litiumbatterier ska hanteras restriktivt.

## Beslut 3: Direktkoppling av laster förbjuds

Filen innehåller en tydlig lista över laster som inte får kopplas direkt till GPIO.

Detta är ett centralt skydd mot vanliga fel i hobbyprojekt.

## Beslut 4: 5 V/3,3 V har fått hög prioritet

Eftersom GPT:n ska stödja både klassiska Arduino-kort och ESP32/ESP8266 behövs tydliga regler för logiknivåer.

Särskilt viktiga fall:

- HC-SR04 mot ESP32/ESP8266,
- LCD1602 I2C med 5 V-pullups,
- MFRC522 RFID,
- okända 5 V-moduler.

## Beslut 5: Kopplingstabell är obligatorisk för byggbara projekt

Reglerna kräver kopplingstabell med matning, jord, signalpinnar och kommentarer.

Skäl:

- tabeller är lättare att granska än fria textbeskrivningar,
- GPT:n kan synliggöra GND, motstånd, nivåomvandlare och externa matningar,
- formatet fungerar väl både för nybörjare och teknisk dokumentation.

## Beslut 6: Strömförsörjning ska få eget avsnitt vid laster

När projekt använder motorer, servon, reläer, LED-strips, elektromagneter eller extern matning ska GPT:n skriva ett separat strömförsörjningsavsnitt.

Detta minskar risken att användaren tror att Arduino-kortet kan driva allt själv.

## Beslut 7: Risknivåer används i Knowledge-filen

Knowledge-filen delar upp projekt i säkerhetsnivå A, B och C.

Syftet är att hjälpa GPT:n att anpassa svar efter användarens erfarenhet.

- A: normalt lämpligt för nybörjare.
- B: kräver extra kontroll.
- C: ska undvikas, förenklas eller styras om.

## Beslut 8: GPT:n ska fråga vid säkerhetskritiska oklarheter

Även om frågemodellen säger att GPT:n normalt ska begränsa antalet frågor, ska säkerhetskritiska oklarheter prioriteras.

Exempel där GPT:n bör fråga eller avstå från komplett koppling:

- okänd motorström,
- okänd batterityp,
- okänd modulspänning,
- nätspänningslast,
- okänd 3,3 V/5 V-kompatibilitet.

## Påverkan på kommande steg

Steg 8, kodstandard, bör hänvisa till dessa regler så att koden inte motsäger kopplingen.

Steg 9, ritnings- och kopplingsstandard, bör bygga vidare på kopplingstabellen och säkerhetsmarkeringarna.

Steg 18, intern granskningschecklista, kan senare lyfta in självkontrollen från detta steg.
