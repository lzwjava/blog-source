---
audio: false
generated: true
lang: de
layout: post
title: Bootloader brennen
translated: true
type: note
---

Das Brennen eines Bootloaders auf ein Arduino Uno R3 ist notwendig, wenn der Mikrocontroller (ATmega328P) blank, beschädigt oder ausgetauscht werden muss. Dieser Prozess programmiert den Chip mit der Firmware, die für die Kommunikation mit der Arduino IDE und das Ausführen von Sketches erforderlich ist. Nachfolgend finden Sie eine Schritt-für-Schritt-Anleitung zum Brennen des Bootloaders mit gängigen Methoden.

---

### **Voraussetzungen**
- **Arduino Uno R3** (das Ziel-Board mit dem zu programmierenden ATmega328P).
- **Programmer**: Einer der Folgenden:
  - Ein weiteres funktionierendes Arduino-Board (z.B. ein weiterer Uno R3) als "Arduino as ISP".
  - Ein dedizierter Programmer wie **USBasp**, **AVRISP mkII** oder **Atmel-ICE**.
- **Arduino IDE** (Download von [arduino.cc](https://www.arduino.cc/en/software)).
- **Jumper-Kabel** (falls Arduino als ISP verwendet wird).
- **USB-Kabel** (zum Verbinden des Programmers oder Arduino mit Ihrem Computer).

---

### **Methode 1: Verwendung eines anderen Arduino (Arduino as ISP)**

Diese Methode verwendet ein zweites Arduino-Board (z.B. einen weiteren Uno R3) als In-System Programmer (ISP), um den Bootloader zu brennen.

#### **Schritte**
1. **Bereiten Sie den Programmer-Arduino vor**:
   - Schließen Sie den zweiten Arduino (den Programmer) über USB an Ihren Computer an.
   - Öffnen Sie die Arduino IDE, gehen Sie zu **Datei > Beispiele > 11.ArduinoISP > ArduinoISP** und laden Sie diesen Sketch auf den Programmer-Arduino hoch. Dieser wird dadurch zu einem ISP.

2. **Verbinden Sie die Boards**:
   - Verdrahten Sie den Programmer-Arduino mit dem Ziel-Arduino Uno R3 (der den Bootloader benötigt) wie folgt:
     - **Programmer Arduino** → **Ziel-Arduino Uno R3**:
       - 5V → 5V
       - GND → GND
       - Pin 10 → Reset
       - Pin 11 → Pin 11 (MOSI)
       - Pin 12 → Pin 12 (MISO)
       - Pin 13 → Pin 13 (SCK)
   - Alternativ, wenn der Ziel-Uno R3 einen **ICSP-Header** hat, verbinden Sie die entsprechenden ICSP-Pins (MOSI, MISO, SCK, VCC, GND, Reset) direkt mit Jumper-Kabeln.

3. **Richten Sie die Arduino IDE ein**:
   - Gehen Sie in der Arduino IDE zu **Werkzeuge > Board** und wählen Sie **Arduino Uno** (für den Ziel-Uno R3).
   - Gehen Sie zu **Werkzeuge > Programmer** und wählen Sie **Arduino as ISP**.
   - Stellen Sie sicher, dass der korrekte Port für den Programmer-Arduino unter **Werkzeuge > Port** ausgewählt ist.

4. **Brennen Sie den Bootloader**:
   - Gehen Sie zu **Werkzeuge > Bootloader brennen**.
   - Die IDE verwendet den Programmer-Arduino, um den Bootloader auf den ATmega328P des Ziel-Uno R3 zu flashen. Dies kann eine Minute dauern.
   - Bei Erfolg erscheint die Meldung "Done burning bootloader". Bei einem Fehler sollten Sie die Verbindungen überprüfen und sicherstellen, dass der Programmer-Arduino den ArduinoISP-Sketch ausführt.

5. **Testen Sie das Ziel-Board**:
   - Trennen Sie den Programmer-Arduino und die Kabel.
   - Schließen Sie den Ziel-Uno R3 über USB an Ihren Computer an.
   - Laden Sie einen einfachen Sketch hoch (z.B. Blink aus **Datei > Beispiele > 01.Basics > Blink**), um zu bestätigen, dass der Bootloader funktioniert.

---

### **Methode 2: Verwendung eines dedizierten ISP-Programmers (z.B. USBasp)**

Wenn Sie einen dedizierten Programmer wie den USBasp haben, ist der Prozess einfacher und oft zuverlässiger.

#### **Schritte**
1. **Schließen Sie den Programmer an**:
   - Verbinden Sie den USBasp (oder einen ähnlichen Programmer) über USB mit Ihrem Computer.
   - Verbinden Sie den Programmer mit dem **ICSP-Header** des Ziel-Arduino Uno R3 mit einem 6-poligen ICSP-Kabel. Achten Sie auf die korrekte Ausrichtung (Pin 1 ist durch einen Punkt oder eine Kerbe auf dem ICSP-Header markiert).

2. **Richten Sie die Arduino IDE ein**:
   - Öffnen Sie die Arduino IDE.
   - Gehen Sie zu **Werkzeuge > Board** und wählen Sie **Arduino Uno**.
   - Gehen Sie zu **Werkzeuge > Programmer** und wählen Sie Ihren Programmer (z.B. **USBasp** oder **AVRISP mkII**).
   - Wählen Sie den korrekten Port unter **Werkzeuge > Port** (falls zutreffend, einige Programmer benötigen keine Port-Auswahl).

3. **Brennen Sie den Bootloader**:
   - Gehen Sie zu **Werkzeuge > Bootloader brennen**.
   - Die IDE verwendet den Programmer, um den Bootloader zu flashen. Dies dauert etwa 10-30 Sekunden.
   - Die Meldung "Done burning bootloader" zeigt einen Erfolg an. Schlägt es fehl, überprüfen Sie die Verbindungen und stellen Sie sicher, dass der Programmer von Ihrem Computer erkannt wird.

4. **Testen Sie das Board**:
   - Trennen Sie den Programmer.
   - Schließen Sie den Uno R3 über USB an Ihren Computer an und laden Sie einen Test-Sketch hoch (z.B. Blink), um die Funktionalität zu überprüfen.

---

### **Tipps zur Fehlerbehebung**
- **Fehlermeldungen**: Bei Fehlern wie "avrdude: stk500_getsync()" oder "not in sync" sollten Sie Folgendes überprüfen:
  - Alle Verbindungen (Kabel oder ICSP-Kabel).
  - Der Programmer-Arduino führt den ArduinoISP-Sketch aus (Methode 1).
  - Der korrekte Programmer ist in der IDE ausgewählt.
- **Treiberprobleme**: Für USBasp oder andere Programmer stellen Sie sicher, dass die Treiber installiert sind (z.B. Zadig für USBasp unter Windows).
- **Blanker Mikrocontroller**: Wenn der ATmega328P neu oder blank ist, benötigt er möglicherweise einen externen 16-MHz-Quarz und zwei 22pF-Kondensatoren, die an Pin 9 und 10 (XTAL1/XTAL2) angeschlossen werden, sofern diese nicht bereits auf dem Uno R3-Board vorhanden sind.
- **Stromversorgung**: Stellen Sie sicher, dass das Ziel-Board während der Programmierung mit Strom versorgt wird (über USB oder VIN).

---

### **Zusätzliche Hinweise**
- **Warum einen Bootloader brennen?**: Der Bootloader ermöglicht es dem Arduino Uno R3, über USB mit der Arduino IDE zu kommunizieren, um Sketches hochzuladen. Ohne ihn reagiert das Board nicht auf USB-Uploads.
- **Bootloader-Typ**: Der Uno R3 verwendet den **Optiboot Bootloader**, der kompakt ist und schnellere Uploads im Vergleich zu älteren Bootloadern unterstützt.
- **Austauschen des Mikrocontrollers**: Wenn Sie den ATmega328P austauschen, stellen Sie sicher, dass es sich um einen ATmega328P-PU (DIP-Gehäuse) für den Sockel des Uno R3 handelt. SMD-Versionen erfordern fortgeschrittene Lötkenntnisse.
- **Alternative Tools**: Sie können auch **AVRDUDE** oder **PlatformIO** zum Brennen des Bootloaders verwenden, aber die Arduino IDE ist für Anfänger am einfachsten.

Wenn Sie eine Erklärung zu einem bestimmten Schritt benötigen oder Hilfe mit einem bestimmten Programmer brauchen, lassen Sie es mich wissen!