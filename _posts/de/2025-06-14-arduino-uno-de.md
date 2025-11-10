---
audio: false
generated: true
lang: de
layout: post
title: Arduino Uno Varianten
translated: true
type: note
---

Das Arduino Uno, Uno R3 und Uno Mini sind Varianten der beliebten Arduino-Mikrocontroller-Platine, die sich jeweils in Design, Funktionen und Anwendungsfällen unterscheiden. Nachfolgend finden Sie einen kurzen Vergleich basierend auf ihren Hauptunterschieden:

### 1. **Arduino Uno (Original) vs. Arduino Uno R3**
Das Arduino Uno und Uno R3 sind im Wesentlichen dieselbe Platine, wobei das Uno R3 die dritte Revision (R3) des originalen Uno ist. Die Unterschiede sind geringfügig und konzentrieren sich auf Verbesserungen bei der Benutzerfreundlichkeit und Kompatibilität.

- **Mikrocontroller**: Beide verwenden den **ATmega328P** (8-Bit AVR, 16 MHz Taktfrequenz).
- **Pinbelegung**:
  - Uno R3 fügt **SDA- und SCL-Pins** in der Nähe des AREF-Pins für I2C-Kompatibilität hinzu, was die Shield-Unterstützung verbessert.
  - R3 enthält einen **IOREF-Pin**, der es Shields ermöglicht, sich an die Spannung der Platine (in diesem Fall 5V) anzupassen.
- **USB-zu-Seriell-Chip**:
  - Das originale Uno verwendet einen **FTDI FT232R**-Chip für die USB-zu-seriell-Kommunikation.
  - Uno R3 aktualisiert auf einen **ATmega16U2**-Mikrocontroller, der flexibler ist und eine schnellere Kommunikation unterstützt.
- **Weitere Änderungen**:
  - R3 hat eine stabilere **Reset-Schaltung** und eine gepufferte LED an Pin 13 (über einen Operationsverstärker), um Interferenzen zu vermeiden.
  - R3 fügt dem 6-Pin-Header in der Nähe des Reset-Pins zwei zusätzliche Pins hinzu (einer ist IOREF, der andere ist reserviert).
- **Formfaktor**: Identische Abmessungen (~6,86 cm x 5,33 cm).
- **Verfügbarkeit**: Das Uno R3 ist der aktuelle Standard; ältere Uno-Revisionen (R1, R2) sind größtenteils veraltet.
- **Anwendungsfall**: Beide sind einsteigerfreundlich und ideal für das Prototyping mit Shields. R3 ist besser für moderne Shields aufgrund des aktualisierten Pinouts.

**Hauptunterschied**: Das Uno R3 ist eine verbesserte Version des originalen Uno mit besserer Shield-Kompatibilität und einer robusteren USB-Schnittstelle. Für die meisten Benutzer ist das R3 die bessere Wahl, da es der aktuelle Standard ist.

### 2. **Arduino Uno R3 vs. Arduino Uno Mini Limited Edition**
Das Arduino Uno Mini Limited Edition ist eine kompakte Sonderedition des Uno R3, die für Sammler und Projekte mit geringerem Platzbedarf konzipiert ist.

- **Mikrocontroller**: Beide verwenden den **ATmega328P** (8-Bit AVR, 16 MHz).
- **Formfaktor**:
  - Uno R3: Standardgröße (~6,86 cm x 5,33 cm).
  - Uno Mini: Viel kleiner (~3,30 cm x 2,54 cm), steckbrettfreundlich, mit einer **goldbeschichteten Leiterplatte** für ästhetischen Reiz.
- **Anschlüsse**:
  - Uno R3: Durchsteck- oder SMD-Versionen; Standard-Stiftleisten für Shields.
  - Uno Mini: Vorverlötete Stiftleisten, keine Shield-Kompatibilität aufgrund der Größe und des Layouts.
- **USB-Anschluss**:
  - Uno R3: USB-B-Anschluss.
  - Uno Mini: **USB-C-Anschluss**, moderner und kompakter.
- **I/O-Pins**:
  - Beide haben **14 digitale I/O** (6 PWM) und **6 analoge Eingänge**, aber die Pins des Uno Mini sind aufgrund der kleineren Größe anders angeordnet.
- **Stromversorgung**:
  - Beide arbeiten mit **5V**, aber dem Uno Mini fehlt eine DC-Buchse (Stromversorgung über USB-C oder VIN-Pin).
- **Speicher**: Identisch (**32 KB Flash, 2 KB SRAM, 1 KB EEPROM**).
- **Besondere Merkmale**:
  - Uno Mini ist eine **Limitierte Edition** mit einzigartiger Grafik und Sammlerverpackung, die für Enthusiasten gedacht ist.
- **Preis**: Uno Mini ist typischerweise teurer aufgrund seines Limited-Edition-Status (~45 $ vs. ~27 $ für Uno R3).
- **Anwendungsfall**:
  - Uno R3: Allgemeines Prototyping, shield-kompatibel, einsteigerfreundlich.
  - Uno Mini: Platzbeschränkte Projekte, Sammler oder Entwickler, die eine hochwertige, kompakte Platine wünschen.

**Hauptunterschied**: Das Uno Mini ist eine kleinere, hochwertigere Version des Uno R3 mit einem USB-C-Anschluss und ohne Shield-Unterstützung, ideal für kompakte oder sammelwürdige Projekte.

### 3. **Zusammenfassungstabelle**

| Merkmal                  | Arduino Uno (Original) | Arduino Uno R3         | Arduino Uno Mini       |
|--------------------------|------------------------|------------------------|------------------------|
| **Mikrocontroller**      | ATmega328P            | ATmega328P            | ATmega328P            |
| **Taktfrequenz**         | 16 MHz                | 16 MHz                | 16 MHz                |
| **Formfaktor**           | ~6,86 cm x 5,33 cm    | ~6,86 cm x 5,33 cm    | ~3,30 cm x 2,54 cm    |
| **USB-Anschluss**        | USB-B (FTDI)          | USB-B (ATmega16U2)    | USB-C                 |
| **I/O-Pins**             | 14 digital, 6 analog  | 14 digital, 6 analog  | 14 digital, 6 analog  |
| **Shield-Kompatibilität**| Eingeschränkt (älter) | Ja                    | Nein                  |
| **Stromeingang**         | USB, Buchse, VIN      | USB, Buchse, VIN      | USB-C, VIN            |
| **Besondere Merkmale**   | -                     | SDA/SCL, IOREF Pins   | Limited Edition, goldene Leiterplatte |
| **Preis (ca.)**          | Veraltet              | ~27 $                 | ~45 $                 |
| **Am besten für**        | Legacy-Projekte       | Allgemeines Prototyping| Kompakte/Sammler-Projekte |

### Welches soll man wählen?
- **Arduino Uno R3**: Die Standardwahl für die meisten Benutzer. Es ist weit verbreitet, shield-kompatibel und ideal für Einsteiger oder Allzweck-Projekte. Wählen Sie dieses, es sei denn, Sie haben spezielle Platzbeschränkungen oder möchten ein Sammlerstück.
- **Arduino Uno (Original)**: Nur relevant, wenn Sie mit älteren, pre-R3 Shields arbeiten oder eine bestehende Platine haben. Ansonsten entscheiden Sie sich für das R3.
- **Arduino Uno Mini Limited Edition**: Wählen Sie dieses für platzbeschränkte Projekte, wenn Sie USB-C bevorzugen, oder wenn Sie ein Arduino-Enthusiast/Sammler sind. Es ist weniger vielseitig aufgrund der fehlenden Shield-Unterstützung.

Wenn Sie neu einsteigen, ist das **Uno R3** die beste Allround-Option aufgrund seiner Kompatibilität, Community-Unterstützung und Erschwinglichkeit. Für spezifische Projektanforderungen (z.B. Größe oder Ästhetik) ist das Uno Mini eine gute Alternative.

Lassen Sie mich wissen, wenn Sie Hilfe bei einem bestimmten Projekt oder einem Funktionsvergleich benötigen!