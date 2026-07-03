# Testfall – steg 6: komponentkatalog MVP

## Syfte

Testfallen verifierar att GPT:n använder komponentkatalogen för att välja rimliga komponenter, varna för vanliga fel och föreslå enklare alternativ när projektet blir för svårt eller osäkert.

---

## Testfall 6.1 – Enkel komponent för barn

**Prompt:**

```text
Skapa ett projekt för en 8-åring som aldrig använt Arduino. Max 150 kr. Gärna något med ljus.
```

**Förväntat beteende:**

- GPT:n väljer nivå 0 eller 1.
- GPT:n föreslår LED, knapp, motstånd och eventuellt LDR.
- GPT:n undviker motorer, reläer, RFID och avancerade sensorer.
- GPT:n anger att LED ska ha seriemotstånd.
- GPT:n beskriver långt/kort LED-ben om koppling ges.

---

## Testfall 6.2 – ESP32 och HC-SR04

**Prompt:**

```text
Jag har en ESP32 och en HC-SR04. Gör en avståndsmätare.
```

**Förväntat beteende:**

- GPT:n varnar för att Echo från en 5 V-HC-SR04 kan vara för hög för ESP32.
- GPT:n föreslår nivådelare, nivåomvandlare eller 3,3 V-kompatibel avståndssensor.
- GPT:n nämner gemensam GND.
- GPT:n skriver inte en koppling där Echo går direkt till ESP32 utan kommentar.

---

## Testfall 6.3 – Servo

**Prompt:**

```text
Jag vill bygga en liten låda som öppnas med ett SG90-servo när man trycker på en knapp.
```

**Förväntat beteende:**

- GPT:n föreslår knapp, SG90-servo och lämpligt kort.
- GPT:n nämner att servo kan behöva separat 5 V-matning.
- GPT:n nämner gemensam GND.
- GPT:n undviker att beskriva lösningen som ett säkert lås.
- GPT:n använder rätt nivå, ungefär nivå 2.

---

## Testfall 6.4 – Motor direkt från pinne

**Prompt:**

```text
Kan jag koppla en liten DC-motor direkt till D9 på Arduino?
```

**Förväntat beteende:**

- GPT:n säger nej tydligt.
- GPT:n förklarar att motorer inte får drivas direkt från GPIO.
- GPT:n föreslår motor driver, till exempel DRV8833 eller L9110S för små motorer.
- GPT:n nämner separat motormatning och gemensam GND.

---

## Testfall 6.5 – Oklar LM393-modul

**Prompt:**

```text
Jag har en LM393-sensor. Vad kan jag använda den till?
```

**Förväntat beteende:**

- GPT:n säger att LM393 är en komparator, inte en specifik sensor.
- GPT:n frågar eller förklarar att modulen kan vara ljud-, ljus-, hall- eller annan tröskelmodul.
- GPT:n hittar inte på en exakt funktion.
- GPT:n ber användaren kontrollera märkning, komponenter eller produktnamn.

---

## Testfall 6.6 – RFID-projekt

**Prompt:**

```text
Jag vill göra ett RFID-lås med Arduino Uno och MFRC522.
```

**Förväntat beteende:**

- GPT:n föreslår MFRC522 men varnar att den normalt är 3,3 V.
- GPT:n beskriver projektet som hobby-/demoprojekt, inte som verkligt säkert lås.
- GPT:n nämner SPI och vanliga kopplingsrisker.
- GPT:n föreslår nivåanpassning eller försiktighet med 5 V-signaler om robusthet krävs.

---

## Testfall 6.7 – LCD1602 med ESP32

**Prompt:**

```text
Jag vill använda en LCD1602 I2C med ESP32.
```

**Förväntat beteende:**

- GPT:n varnar för att många LCD1602 I2C-backpacks är 5 V-orienterade.
- GPT:n nämner risk för 5 V pullups på I2C.
- GPT:n föreslår nivåomvandlare, kontroll av modul eller OLED I2C som enklare 3,3 V-alternativ.

---

## Testfall 6.8 – Många servon

**Prompt:**

```text
Jag vill styra åtta små servon från en Arduino Nano.
```

**Förväntat beteende:**

- GPT:n föreslår PCA9685 som lämplig PWM/servodriver.
- GPT:n säger att servon behöver separat 5 V-matning med tillräcklig ström.
- GPT:n nämner gemensam GND mellan Arduino, PCA9685 och servomatning.
- GPT:n undviker att mata alla servon från Arduino Nano.

---

## Testfall 6.9 – Elektromagnet

**Prompt:**

```text
Jag vill styra en 12 V elektromagnet med ESP32.
```

**Förväntat beteende:**

- GPT:n frågar efter elektromagnetens ström eller anger att det krävs innan konkret dimensionering.
- GPT:n säger att elektromagneten inte får kopplas direkt till GPIO.
- GPT:n föreslår 3,3 V-kompatibel MOSFET/drivsteg, extern 12 V-matning, gemensam GND och flyback-diod.
- GPT:n varnar för värme, ström och säkerhetskritisk användning.

---

## Testfall 6.10 – Projekt från befintliga komponenter

**Prompt:**

```text
Jag har Arduino Uno, OLED, BME280, knapp, LED och buzzer. Föreslå ett projekt för en nybörjare.
```

**Förväntat beteende:**

- GPT:n föreslår exempelvis en enkel väderstation eller inomhusklimatmätare.
- GPT:n använder BME280 och OLED på nivå 2 men håller projektet pedagogiskt.
- GPT:n nämner I2C-adresser och bibliotek som möjliga felkällor.
- GPT:n inkluderar LED/buzzer som enkel status/varning, inte som krav om projektet blir för stort.
