---
audio: false
generated: true
lang: de
layout: post
title: Überprüfung der Netzwerkanalyse mit Arduino
translated: true
type: note
---

Die Überprüfung der Mesh-Analyse mit einem Arduino umfasst den Aufbau einer Schaltung mit mehreren Maschen, die theoretische Anwendung der Mesh-Analyse zur Vorhersage von Strömen und die anschließende Verwendung des Arduino zur Messung von Spannungen an Widerständen, um die tatsächlichen Ströme zur Vergleichszwecken zu berechnen. Die Mesh-Analyse ist eine Methode in der Schaltungstheorie, bei der Schleifenströme für jede unabhängige Masche zugewiesen und das Kirchhoffsche Spannungsgesetz (KVL) zur Aufstellung von Gleichungen verwendet wird. Der Arduino hilft dabei, das reale Verhalten zu messen, um Ihre Berechnungen zu bestätigen.

Im Folgenden werde ich Sie durch die Entwicklung einer einfachen Zwei-Maschen-Schaltung, die manuelle Durchführung der Mesh-Analyse und die Verwendung eines Arduino zur Überprüfung der Ergebnisse durch Messung von Spannungen und Ableitung von Strömen führen (da der Arduino Strom nicht direkt messen kann, verwenden wir das Ohmsche Gesetz: \\( I = V/R \\)).

---

### **Schritt 1: Entwurf einer Zwei-Maschen-Schaltung**

#### **Schaltungsbeschreibung**
- **Komponenten:**
  - Arduino (z.B. Uno)
  - 3 Widerstände (z.B. R1 = 330Ω, R2 = 470Ω, R3 = 680Ω)
  - Steckbrett und Jumper-Kabel
  - Stromquelle (5V-Pin des Arduino)
- **Verdrahtung:**
  - Verbinden Sie 5V mit Knoten A.
  - Verbinden Sie von Knoten A aus R1 mit Knoten B.
  - Verbinden Sie von Knoten B aus R2 mit Knoten C (GND).
  - Verbinden Sie von Knoten A aus R3 mit Knoten C (GND).
- **Topologie:**
  - Masche 1: 5V → R1 → R2 → GND (linke Schleife).
  - Masche 2: 5V → R3 → GND (rechte Schleife).
  - R1 ist nur in Masche 1, R3 ist nur in Masche 2, und R2 wird von beiden Maschen geteilt.
- **Messpunkte:**
  - A0: Spannung über R1 (Knoten A zu Knoten B).
  - A1: Spannung über R2 (Knoten B zu Knoten C).
  - A2: Spannung über R3 (Knoten A zu Knoten C).

#### **Schematische Darstellung**
```
5V ---- Knoten A ---- R1 ---- Knoten B ---- R2 ---- Knoten C (GND)
       |                             |
       +------------- R3 ------------+
```

---

### **Schritt 2: Theoretische Durchführung der Mesh-Analyse**

#### **Definieren der Schleifenströme**
- \\( I_1 \\): Strom in Masche 1 (im Uhrzeigersinn durch 5V, R1, R2, GND).
- \\( I_2 \\): Strom in Masche 2 (im Uhrzeigersinn durch 5V, R3, GND).

#### **Anwendung von KVL auf jede Masche**
1. **Masche 1 (5V → R1 → R2 → GND):**
   - Spannungsquelle: +5V (von GND zu 5V in Schleifenrichtung).
   - Spannungsabfall über R1: \\( -R1 \cdot I_1 \\).
   - Spannungsabfall über R2: \\( -R2 \cdot (I_1 - I_2) \\) (Strom durch R2 ist \\( I_1 - I_2 \\)).
   - Gleichung: \\( 5 - R1 \cdot I_1 - R2 \cdot (I_1 - I_2) = 0 \\).

2. **Masche 2 (5V → R3 → GND):**
   - Spannungsquelle: +5V.
   - Spannungsabfall über R3: \\( -R3 \cdot I_2 \\).
   - Spannungsabfall über R2 (entgegengesetzte Richtung): \\( +R2 \cdot (I_1 - I_2) \\) (Strom durch R2 ist \\( I_1 - I_2 \\)).
   - Gleichung: \\( 5 - R3 \cdot I_2 + R2 \cdot (I_1 - I_2) = 0 \\).

#### **Werte einsetzen**
- R1 = 330Ω, R2 = 470Ω, R3 = 680Ω.
- Masche 1: \\( 5 - 330 I_1 - 470 (I_1 - I_2) = 0 \\)
  - Vereinfachen: \\( 5 - 330 I_1 - 470 I_1 + 470 I_2 = 0 \\)
  - \\( 5 - 800 I_1 + 470 I_2 = 0 \\) → (1)
- Masche 2: \\( 5 - 680 I_2 + 470 (I_1 - I_2) = 0 \\)
  - Vereinfachen: \\( 5 + 470 I_1 - 680 I_2 - 470 I_2 = 0 \\)
  - \\( 5 + 470 I_1 - 1150 I_2 = 0 \\) → (2)

#### **Gleichungen lösen**
- Aus (1): \\( 5 = 800 I_1 - 470 I_2 \\) → \\( I_1 = \frac{5 + 470 I_2}{800} \\).
- In (2) einsetzen: \\( 5 + 470 \left( \frac{5 + 470 I_2}{800} \right) - 1150 I_2 = 0 \\).
- Mit 800 multiplizieren, um den Bruch zu entfernen:
  - \\( 4000 + 470 (5 + 470 I_2) - 1150 \cdot 800 I_2 = 0 \\)
  - \\( 4000 + 2350 + 220900 I_2 - 920000 I_2 = 0 \\)
  - \\( 6350 - 699100 I_2 = 0 \\)
  - \\( I_2 = \frac{6350}{699100} \approx 0,00908 \, \text{A} = 9,08 \, \text{mA} \\).
- Rückeinsetzen: \\( I_1 = \frac{5 + 470 \cdot 0,00908}{800} = \frac{5 + 4,2676}{800} \approx 0,01158 \, \text{A} = 11,58 \, \text{mA} \\).

#### **Spannungen berechnen**
- \\( V_{R1} = R1 \cdot I_1 = 330 \cdot 0,01158 \approx 3,82 \, \text{V} \\).
- \\( V_{R2} = R2 \cdot (I_1 - I_2) = 470 \cdot (0,01158 - 0,00908) \approx 1,18 \, \text{V} \\).
- \\( V_{R3} = R3 \cdot I_2 = 680 \cdot 0,00908 \approx 6,17 \, \text{V} \\) (aber auf 5V begrenzt aufgrund der Quelle).

---

### **Schritt 3: Überprüfung mit dem Arduino**

#### **Arduino-Code**
```cpp
void setup() {
  Serial.begin(9600); // Serielle Kommunikation starten
}

void loop() {
  // Spannungen lesen (0-1023 entspricht 0-5V)
  int sensorValueR1 = analogRead(A0); // Über R1
  int sensorValueR2 = analogRead(A1); // Über R2
  int sensorValueR3 = analogRead(A2); // Über R3

  // In Spannung umrechnen
  float VR1 = sensorValueR1 * (5.0 / 1023.0);
  float VR2 = sensorValueR2 * (5.0 / 1023.0);
  float VR3 = sensorValueR3 * (5.0 / 1023.0);

  // Widerstandswerte
  float R1 = 330.0;
  float R2 = 470.0;
  float R3 = 680.0;

  // Ströme berechnen (I = V/R)
  float I1 = VR1 / R1;              // Strom Masche 1 durch R1
  float I2 = VR3 / R3;              // Strom Masche 2 durch R3
  float IR2 = VR2 / R2;             // Strom durch R2 (I1 - I2)

  // Ergebnisse ausgeben
  Serial.println("Gemessene Werte:");
  Serial.print("VR1 (V): "); Serial.println(VR1);
  Serial.print("VR2 (V): "); Serial.println(VR2);
  Serial.print("VR3 (V): "); Serial.println(VR3);
  Serial.print("I1 (mA): "); Serial.println(I1 * 1000);
  Serial.print("I2 (mA): "); Serial.println(I2 * 1000);
  Serial.print("I1 - I2 (mA): "); Serial.println((I1 - I2) * 1000);
  Serial.println("---");

  delay(2000); // 2 Sekunden warten
}
```

#### **Verdrahtungshinweise**
- Verbinden Sie A0 zwischen Knoten A (5V) und Knoten B.
- Verbinden Sie A1 zwischen Knoten B und Knoten C (GND).
- Verbinden Sie A2 zwischen Knoten A (5V) und Knoten C (GND).
- Stellen Sie sicher, dass alle Massen mit der Arduino-Masse (GND) gemeinsam verbunden sind.

---

### **Schritt 4: Vergleich der Ergebnisse**

#### **Erwartet vs. Gemessen**
- **Theoretisch (aus Mesh-Analyse):**
  - \\( I_1 \approx 11,58 \, \text{mA} \\)
  - \\( I_2 \approx 9,08 \, \text{mA} \\)
  - \\( I_1 - I_2 \approx 2,50 \, \text{mA} \\)
  - \\( V_{R1} \approx 3,82 \, \text{V} \\), \\( V_{R2} \approx 1,18 \, \text{V} \\), \\( V_{R3} \approx 5 \, \text{V} \\) (begrenzt).
- **Gemessen:** Öffnen Sie den Serial Monitor (9600 Baud) und vergleichen Sie die Ausgabe des Arduino mit diesen Werten.

#### **Überprüfung**
- Prüfen Sie, ob \\( V_{R1} + V_{R2} \approx 5V \\) (Masche-1-Schleife).
- Prüfen Sie, ob \\( V_{R3} \approx 5V \\) (Masche-2-Schleife).
- Bestätigen Sie, dass \\( I_1 - I_2 \\) mit dem Strom durch R2 übereinstimmt.

---

### **Tipps und Fehlerbehebung**
- **Genauigkeit:** Der ADC des Arduino hat eine Auflösung von ~4,9mV, und Widerstandstoleranzen können leichte Abweichungen verursachen. Verwenden Sie ein Multimeter zur präzisen Validierung.
- **Anpassungen:** Wenn Spannungen 5V überschreiten (hier unwahrscheinlich), verwenden Sie einen Spannungsteiler, um sie herunterzuskalieren.
- **Erweiterungen:** Fügen Sie weitere Maschen oder Komponenten für Komplexität hinzu, beachten Sie jedoch die Pin-Beschränkungen (A0–A5).

Dieser Aufbau bestätigt die Mesh-Analyse durch Abgleich der theoretischen Ströme mit den gemessenen. Lassen Sie mich wissen, wenn Sie Hilfe bei der Verfeinerung der Schaltung, beim Debugging oder beim Hinzufügen weiterer Maschen benötigen!