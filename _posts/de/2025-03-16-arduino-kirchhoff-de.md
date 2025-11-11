---
audio: false
generated: true
lang: de
layout: post
title: Kirchhoffsche Gesetze mit Arduino
translated: true
type: note
---

Die Verwendung eines Arduino zur Überprüfung der Kirchhoffschen Gesetze – speziell des Kirchhoffschen Stromgesetzes (KCL) und des Kirchhoffschen Spannungsgesetzes (KVL) – ist eine großartige Methode, um Elektroniktheorie mit praktischen Experimenten zu verbinden. KCL besagt, dass der gesamte in einen Knotenpunkt eintretende Strom gleich dem gesamten austretenden Strom ist, während KVL besagt, dass die Summe der Spannungsabfälle in einer geschlossenen Masche gleich der zugeführten Spannung ist. Im Folgenden wird beschrieben, wie Sie einfache Schaltungen entwerfen und einen Arduino zur Messung von Strömen und Spannungen verwenden können, um diese Gesetze zu bestätigen.

Da ein Arduino Strom nicht direkt messen kann, leiten wir ihn indirekt durch Messung der Spannung an Widerständen ab (unter Verwendung des Ohmschen Gesetzes: \\( I = V/R \\)), und er kann Spannung über seine analogen Pins (0–5V Bereich) messen. Nachfolgend skizziere ich zwei Experimente – eines für KCL und eines für KVL – mit Schritt-für-Schritt-Anleitungen, Verdrahtung und Code.

---

### **Experiment 1: Überprüfung des Kirchhoffschen Stromgesetzes (KCL)**

#### **Ziel**
Demonstrieren, dass der in einen Knotenpunkt eintretende Strom gleich dem austretenden Strom ist.

#### **Schaltungsaufbau**
- **Komponenten:**
  - Arduino (z.B. Uno)
  - 3 Widerstände (z.B. R1 = 330Ω, R2 = 470Ω, R3 = 680Ω)
  - Steckbrett und Jumper-Kabel
  - 5V Stromquelle (5V-Pin des Arduino)
- **Verdrahtung:**
  - Verbinden Sie den Arduino 5V-Pin mit einem Knotenpunkt (nennen wir ihn Knoten A).
  - Verbinden Sie von Knoten A aus R1 mit GND (Zweig 1).
  - Verbinden Sie von Knoten A aus R2 mit GND (Zweig 2, parallel zu R1).
  - Verbinden Sie von Knoten A aus R3 mit GND (Zweig 3, parallel zu R1 und R2).
  - Verwenden Sie Arduino analoge Pins, um die Spannung an jedem Widerstand zu messen:
    - A0 über R1 (eine Sonde an Knoten A, die andere an GND).
    - A1 über R2.
    - A2 über R3.
- **Hinweis:** GND ist der gemeinsame Bezugspunkt.

#### **Theorie**
- Der Gesamtstrom von 5V zu Knoten A (\\( I_{in} \\)) teilt sich in \\( I_1 \\), \\( I_2 \\) und \\( I_3 \\) durch R1, R2 und R3 auf.
- KCL: \\( I_{in} = I_1 + I_2 + I_3 \\).
- Messen Sie die Spannung an jedem Widerstand und berechnen Sie dann den Strom: \\( I = V/R \\).

#### **Arduino Code**
```cpp
void setup() {
  Serial.begin(9600); // Serielle Kommunikation starten
}

void loop() {
  // Spannungen auslesen (0-1023 abbildet auf 0-5V)
  int sensorValue1 = analogRead(A0); // Spannung über R1
  int sensorValue2 = analogRead(A1); // Spannung über R2
  int sensorValue3 = analogRead(A2); // Spannung über R3

  // In Spannung umrechnen (5V Referenz, 10-Bit ADC)
  float V1 = sensorValue1 * (5.0 / 1023.0);
  float V2 = sensorValue2 * (5.0 / 1023.0);
  float V3 = sensorValue3 * (5.0 / 1023.0);

  // Widerstandswerte (in Ohm)
  float R1 = 330.0;
  float R2 = 470.0;
  float R3 = 680.0;

  // Ströme berechnen (I = V/R)
  float I1 = V1 / R1;
  float I2 = V2 / R2;
  float I3 = V3 / R3;

  // Gesamtstrom, der in den Knoten eintritt (angenommen Vsource = 5V)
  float totalResistance = 1.0 / ((1.0/R1) + (1.0/R2) + (1.0/R3)); // Parallel
  float Iin = 5.0 / totalResistance;

  // Ergebnisse ausgeben
  Serial.print("I1 (mA): "); Serial.println(I1 * 1000);
  Serial.print("I2 (mA): "); Serial.println(I2 * 1000);
  Serial.print("I3 (mA): "); Serial.println(I3 * 1000);
  Serial.print("Iin (mA): "); Serial.println(Iin * 1000);
  Serial.print("Summe I1+I2+I3 (mA): "); Serial.println((I1 + I2 + I3) * 1000);
  Serial.println("---");

  delay(2000); // 2 Sekunden warten
}
```

#### **Überprüfung**
- Öffnen Sie den Serial Monitor (Strg+Umschalt+M in der Arduino IDE, eingestellt auf 9600 Baud).
- Vergleichen Sie \\( I_{in} \\) (berechnet aus dem Gesamtwiderstand) mit \\( I_1 + I_2 + I_3 \\). Sie sollten ungefähr gleich sein, was KCL verifiziert.
- Geringe Abweichungen können von Widerstandstoleranzen oder der Arduino-ADC-Präzision herrühren.

---

### **Experiment 2: Überprüfung des Kirchhoffschen Spannungsgesetzes (KVL)**

#### **Ziel**
Zeigen, dass die Summe der Spannungsabfälle in einer geschlossenen Masche gleich der Versorgungsspannung ist.

#### **Schaltungsaufbau**
- **Komponenten:**
  - Arduino
  - 2 Widerstände (z.B. R1 = 330Ω, R2 = 470Ω)
  - Steckbrett und Jumper-Kabel
  - 5V Stromquelle (5V-Pin des Arduino)
- **Verdrahtung:**
  - Verbinden Sie 5V mit R1.
  - Verbinden Sie R1 mit R2.
  - Verbinden Sie R2 mit GND.
  - Messen Sie die Spannungen:
    - A0 über die gesamte Masche (5V zu GND), um die Versorgungsspannung zu bestätigen.
    - A1 über R1 (5V zur Verbindung von R1 und R2).
    - A2 über R2 (Verbindung zu GND).
- **Hinweis:** Verwenden Sie einen Spannungsteiler-Aufbau; stellen Sie sicher, dass die Spannungen 5V (Arduino-Limit) nicht überschreiten.

#### **Theorie**
- KVL: \\( V_{source} = V_{R1} + V_{R2} \\).
- Messen Sie jeden Spannungsabfall und prüfen Sie, ob ihre Summe der Quellspannung (5V) entspricht.

#### **Arduino Code**
```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  // Spannungen auslesen
  int sensorValueSource = analogRead(A0); // Über 5V zu GND
  int sensorValueR1 = analogRead(A1);     // Über R1
  int sensorValueR2 = analogRead(A2);     // Über R2

  // In Spannung umrechnen
  float Vsource = sensorValueSource * (5.0 / 1023.0);
  float VR1 = sensorValueR1 * (5.0 / 1023.0);
  float VR2 = sensorValueR2 * (5.0 / 1023.0);

  // Ergebnisse ausgeben
  Serial.print("Vsource (V): "); Serial.println(Vsource);
  Serial.print("VR1 (V): "); Serial.println(VR1);
  Serial.print("VR2 (V): "); Serial.println(VR2);
  Serial.print("VR1 + VR2 (V): "); Serial.println(VR1 + VR2);
  Serial.println("---");

  delay(2000);
}
```

#### **Überprüfung**
- Prüfen Sie im Serial Monitor, ob \\( V_{source} \approx V_{R1} + V_{R2} \\) gilt.
- Für R1 = 330Ω und R2 = 470Ω in Reihe erwarten Sie \\( V_{R1} \approx 2.1V \\) und \\( V_{R2} \approx 2.9V \\) (basierend auf dem Spannungsteiler: \\( V_{R1} = 5 \cdot \frac{R1}{R1+R2} \\)), was sich zu ~5V summiert.

---

### **Tipps und Hinweise**
- **Präzision:** Der 10-Bit-ADC des Arduino (0–1023) hat eine Auflösung von ~4.9mV, daher sind geringe Abweichungen zu erwarten. Verwenden Sie bei Bedarf ein Multimeter zur Gegenprüfung.
- **Sicherheit:** Halten Sie Spannungen unter 5V und Ströme niedrig, um eine Beschädigung des Arduino zu vermeiden.
- **Skalierung:** Für komplexere Schaltungen fügen Sie mehr Widerstände hinzu oder verwenden Sie externe Sensoren (z.B. INA219 für direkte Strommessung).
- **Fehlersuche:** Wenn die Ergebnisse nicht übereinstimmen, überprüfen Sie die Widerstandswerte, Verbindungen und die GND-Konsistenz.

Diese Experimente vereinfachen reale Bedingungen, demonstrieren die Kirchhoffschen Gesetze aber effektiv. Möchten Sie diese Aufbauten anpassen oder benötigen Hilfe zu einem bestimmten Teil (wie Verdrahtung oder Code)? Lassen Sie es mich wissen!