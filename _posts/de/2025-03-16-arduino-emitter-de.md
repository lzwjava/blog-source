---
audio: false
generated: true
lang: de
layout: post
title: Aufbau eines Common-Emitter-Verstärkers mit einem Arduino
translated: true
type: note
---

Den Aufbau eines Common-Emitter (CE)-Verstärkers mit einem Arduino zu realisieren, ist ein interessantes Projekt, aber es ist wichtig, die Rollen zu klären: Der Arduino selbst fungiert nicht als Verstärker (es ist ein digitaler Mikrocontroller), aber er kann als Signalquelle oder Messwerkzeug für eine CE-Verstärkerschaltung dienen, die mit einem Bipolartransistor (BJT) aufgebaut ist. Ein CE-Verstärker ist eine klassische analoge Schaltung, die einen NPN- oder PNP-Transistor verwendet, um ein kleines Eingangssignal zu verstärken, und bietet eine moderate Spannungs- und Stromverstärkung.

Hier werde ich Sie durch den Entwurf eines einfachen, auf einem NPN-Transistor basierenden CE-Verstärkers führen und den Arduino zur Erzeugung eines Eingangssignals (über PWM) und zur Messung des Ausgangs nutzen. Dieser Aufbau demonstriert die Verstärkung und nutzt gleichzeitig die Fähigkeiten des Arduino.

---

### **Überblick eines Common-Emitter-Verstärkers**
- **Zweck:** Verstärkt ein kleines AC-Signal (z. B. Audio oder eine Sinuswelle).
- **Hauptmerkmale:**
  - Der Transistor arbeitet im aktiven Bereich.
  - Das Eingangssignal wird an die Basis angelegt, der Ausgang wird vom Kollektor abgenommen.
  - Die Spannungsverstärkung wird durch Widerstandsverhältnisse und Transistoreigenschaften bestimmt.
- **Komponenten:**
  - NPN-Transistor (z. B. 2N3904 oder BC547)
  - Widerstände (für die Vorspannung und Last)
  - Kondensatoren (zum Koppeln von AC-Signalen)
  - Arduino (Signalquelle und Messung)

---

### **Schritt 1: Schaltung entwerfen**

#### **Benötigte Komponenten**
- NPN-Transistor (z. B. 2N3904)
- Widerstände: R1 = 47kΩ, R2 = 10kΩ (Vorspannung), RC = 1kΩ (Kollektor), RE = 220Ω (Emitter)
- Kondensatoren: C1 = 10µF (Eingangskopplung), C2 = 10µF (Ausgangskopplung), CE = 100µF (Emitter-Bypass, optional für höhere Verstärkung)
- Arduino (z. B. Uno)
- Steckbrett, Jumper-Kabel
- Stromversorgung (5V-Pin des Arduino oder externe 9V, je nach Bedarf angepasst)

#### **Schaltplan**
```
Vcc (5V) ---- R1 ----+---- RC ---- Kollektor (C)
             47kΩ     |     1kΩ          |
                      |                  |
Basis (B) --- C1 -----+                  |
            10µF     |                  |
Arduino PWM (Pin 9)  R2                 |
                     10kΩ              Ausgang --- C2 ---- An Arduino A0
                      |                  |         10µF
                      |                  |
                      +---- RE ---- Emitter (E) --- CE (optional) --- GND
                           220Ω                   100µF
                      |
                     GND
```
- **Vorspannung (R1, R2):** Legt den Arbeitspunkt des Transistors fest.
- **RC:** Kollektorwiderstand für das Ausgangssignal.
- **RE:** Emitterwiderstand für Stabilität.
- **C1, C2:** Blockieren DC, lassen AC-Signale durch.
- **CE (optional):** Überbrückt RE für eine höhere AC-Verstärkung.

#### **Arbeitspunkt**
- Ziel: Den Transistor im aktiven Bereich vorspannen (z. B. VCE ≈ 2,5V bei 5V Versorgungsspannung).
- Spannungsteiler (R1, R2): \\( V_B = V_{CC} \cdot \frac{R2}{R1 + R2} = 5 \cdot \frac{10k}{47k + 10k} \approx 0,88V \\).
- \\( V_E = V_B - V_{BE} \approx 0,88 - 0,7 = 0,18V \\).
- \\( I_E = \frac{V_E}{RE} = \frac{0,18}{220} \approx 0,82 \, \text{mA} \\).
- \\( V_C = V_{CC} - I_C \cdot RC \approx 5 - 0,82 \cdot 1k \approx 4,18V \\).
- \\( V_{CE} = V_C - V_E \approx 4,18 - 0,18 = 4V \\) (gut für 5V Versorgungsspannung).

---

### **Schritt 2: Arduino als Signalquelle verwenden**

#### **Rolle des Arduino**
- Erzeugen eines kleinen AC-Signals mittels PWM (Pulsweitenmodulation) an einem Pin wie 9 (der PWM unterstützt).
- Filtern der PWM, um mit einem einfachen RC-Tiefpassfilter (optional) eine angenäherte Sinuswelle zu erzeugen.

#### **Code zur Signalerzeugung**
```cpp
const int pwmPin = 9; // PWM-Ausgangspin

void setup() {
  pinMode(pwmPin, OUTPUT);
  // PWM-Frequenz setzen (optional, Standard ist ~490 Hz)
}

void loop() {
  // Simuliere eine Sinuswelle mit PWM (Bereich 0-255)
  for (int i = 0; i < 360; i += 10) {
    float sineValue = sin(radians(i)); // Sinuswelle von -1 bis 1
    int pwmValue = 127 + 127 * sineValue; // Skaliere auf 0-255
    analogWrite(pwmPin, pwmValue);
    delay(10); // Anpassen für Frequenz (z. B. ~100 Hz hier)
  }
}
```
- **Ausgang:** ~0–5V PWM-Signal, zentriert bei 2,5V mit ~2,5V Spitze-Spitze.
- **C1:** Entfernt den DC-Offset und leitet nur die AC-Komponente (~1,25V Spitze) zur Basis.

#### **Optionaler Filter**
Fügen Sie einen 1kΩ-Widerstand und einen 0,1µF-Kondensator in Reihe von Pin 9 zu GND hinzu, nehmen Sie das Signal vor C1 ab, um die PWM in eine grobe Sinuswelle zu glätten.

---

### **Schritt 3: Den Ausgang messen**

#### **Messung mit dem Arduino**
- Verbinden Sie den Verstärkerausgang (nach C2) mit A0.
- Verwenden Sie den Arduino, um das verstärkte Signal auszulesen und über den Serial Monitor anzuzeigen.

#### **Code zur Messung und Anzeige**
```cpp
const int inputPin = A0; // Messen Sie den Ausgang hier

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(inputPin); // 0-1023 abgebildet auf 0-5V
  float voltage = sensorValue * (5.0 / 1023.0);
  Serial.print("Ausgangsspannung (V): ");
  Serial.println(voltage);
  delay(100); // Abtastrate anpassen
}
```

#### **Erwartete Verstärkung**
- Spannungsverstärkung \\( A_v = -\frac{RC}{RE} = -\frac{1k}{220} \approx -4,5 \\) (negativ aufgrund der Phasenumkehr).
- Eingang: ~1,25V Spitze (nach der Kopplung).
- Ausgang: ~4,5 × 1,25 = 5,625V Spitze (wird aber aufgrund der Versorgungsspannungsbegrenzung auf 5V abgeschnitten).

---

### **Schritt 4: Aufbau und Test**

#### **Aufbau**
1. Verdrahten Sie die Schaltung gemäß dem Schaltplan auf einem Steckbrett.
2. Laden Sie den Code zur Signalerzeugung auf den Arduino hoch und verbinden Sie Pin 9 mit C1.
3. Versorgen Sie die Schaltung über 5V vom Arduino (oder verwenden Sie 9V mit angepassten Widerständen).
4. Laden Sie den Messcode hoch und öffnen Sie den Serial Monitor (9600 Baud).

#### **Überprüfung**
- **Eingangssignal:** ~1–2V Spitze-Spitze nach C1 (verwenden Sie ggf. ein Multimeter oder Oszilloskop).
- **Ausgangssignal:** Sollte größer sein (z. B. 4–5V Spitze-Spitze) und invertiert.
- Überprüfen Sie VCE (~2–4V) mit einem Multimeter, um den Betrieb im aktiven Bereich sicherzustellen.

---

### **Tipps und Fehlerbehebung**
- **Verstärkung zu niedrig:** Fügen Sie CE (100µF) parallel zu RE hinzu, um die AC-Verstärkung zu erhöhen (entfernt die Degeneration durch RE).
- **Clipping (Abschneiden):** Wenn der Ausgang 5V überschreitet, reduzieren Sie die Eingangsamplitude (PWM-Bereich anpassen) oder erhöhen Sie Vcc (z. B. externe 9V Versorgung).
- **Rauschen:** PWM ist quadratisch; eine bessere Sinuswelle (über externen Generator oder Filter) verbessert die Ergebnisse.
- **Transistordaten:** Stellen Sie sicher, dass der 2N3904 die Ströme verarbeiten kann (Ic < 200mA, hier sicher).

Dieser Aufbau demonstriert das Kernverhalten eines CE-Verstärkers – die Spannungsverstärkung – und integriert gleichzeitig den Arduino zur Signalerzeugung und -analyse. Möchten Sie die Verstärkung anpassen, einen Lautsprecher für Audio hinzufügen oder das Signal verbessern? Lassen Sie es mich wissen!