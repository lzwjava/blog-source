---
audio: false
generated: true
lang: de
layout: post
title: MOSFET als von Arduino gesteuerter Schalter
translated: true
type: note
---

Es scheint ein Missverständnis in Ihrer Frage zu geben. Ein Arduino kann nicht verwendet werden, um Metall-Oxid-Halbleiter-Feldeffekttransistoren (MOSFETs) *herzustellen*, da es sich bei MOSFETs um grundlegende Halbleiterbauelemente handelt, die durch komplexe Prozesse wie Fotolithografie und Dotierung in einer Reinraumumgebung gefertigt werden. Ich nehme jedoch an, Sie meinten "wie man einen Arduino verwendet, um eine Schaltung *mit* MOSFETs aufzubauen" oder "wie man MOSFETs in einem Arduino-Projekt verwendet". Falls ich das falsch verstanden habe, klären Sie es bitte auf!

Ich werde fortfahren, indem ich erkläre, wie man einen Arduino verwendet, um einen MOSFET in einer praktischen Schaltung zu steuern, z.B. als einfachen Schalter oder Verstärker. MOSFETs sind vielseitige Komponenten, die oft als Schalter oder in Verstärkerschaltungen eingesetzt werden und sich gut mit den digitalen Ausgängen des Arduino kombinieren lassen. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung für eine häufige Anwendung: die Verwendung eines N-Kanal-MOSFETs (z.B. IRF540 oder 2N7000) als leistungsstarken Schalter, gesteuert durch einen Arduino.

---

### **Projekt: MOSFET als schaltbarer Schalter mit Arduino**

#### **Überblick**
- **Zweck:** Verwendung eines Arduino, um eine leistungsstarke Last (z.B. einen LED-Streifen, Motor oder Lampe) über einen MOSFET ein- und auszuschalten.
- **Warum MOSFET?** Im Gegensatz zu BJTs sind MOSFETs spannungsgesteuert, benötigen nur minimalen Strom vom Arduino und können höhere Ströme/Spannungen handhaben als die Pins des Arduino (max. 40mA, 5V).

#### **Benötigte Komponenten**
- Arduino (z.B. Uno)
- N-Kanal-MOSFET (z.B. IRF540 oder 2N7000; IRF540 für höhere Leistung)
- Widerstände: R1 = 10kΩ (Pull-Down), R2 = 220Ω (Gate-Schutz, optional)
- Last: z.B. 12V LED-Streifen, DC-Motor oder Lampe (mit entsprechender Stromversorgung)
- Diode (z.B. 1N4007, für induktive Lasten wie Motoren)
- Steckbrett, Jumper-Kabel
- Externe Stromversorgung (z.B. 12V für die Last)

#### **Schaltplan**
```
Arduino Pin 9 ---- R2 (220Ω) ---- Gate (G)
                             |
                             |
V_Last (z.B., 12V) ---- Last ---- Drain (D)
                             | 
                             |
                            Source (S) ---- GND
                             |
                            R1 (10kΩ)
                             |
                            GND
```
- **Für induktive Lasten (z.B. Motor):** Fügen Sie eine Freilaufdiode (1N4007) parallel zur Last hinzu (Kathode zu V_Last, Anode zu Drain), um den MOSFET vor Spannungsspitzen zu schützen.
- **Stromversorgung:** Arduino über USB oder 5V; Last über externe Stromversorgung (z.B. 12V). Verbinden Sie alle GND miteinander.

#### **Funktionsweise**
- **Rolle des MOSFET:** Fungiert als Schalter zwischen Drain und Source, gesteuert durch die Gate-Spannung.
- **Rolle des Arduino:** Gibt ein HIGH (5V) oder LOW (0V) Signal an das Gate über Pin 9 aus.
- **Logik:**
  - HIGH (5V) am Gate → MOSFET schaltet EIN → Last erhält Strom.
  - LOW (0V) am Gate → MOSFET schaltet AUS → Last stoppt.
- **R1 (Pull-Down):** Stellt sicher, dass das Gate auf LOW-Potential liegt, wenn der Arduino ausgeschaltet ist oder der Pin im hochohmigen Zustand ist.
- **R2 (Optional):** Begrenzt den Strom zum Gate (normalerweise bei Logik-Level-MOSFETs unnötig).

---

### **Schritt 1: Schaltung aufbauen**

1. **MOSFET anschließen:**
   - **Gate (G):** An Arduino Pin 9 über R2 (220Ω, optional).
   - **Drain (D):** An die negative Seite der Last (z.B. Kathode des LED-Streifens).
   - **Source (S):** An GND.
2. **Last und Stromversorgung:**
   - Verbinden Sie die positive Seite der Last mit V_Last (z.B. 12V Netzteil).
   - Verbinden Sie das GND des 12V Netzteils mit dem Arduino GND.
3. **Sicherheit:**
   - Fügen Sie R1 (10kΩ) zwischen Gate und GND hinzu.
   - Für Motoren fügen Sie die Diode parallel zur Last hinzu.

---

### **Schritt 2: Arduino-Code**

#### **Einfacher Ein/Aus-Schalter**
```cpp
const int mosfetPin = 9; // PWM-fähiger Pin

void setup() {
  pinMode(mosfetPin, OUTPUT); // Pin als Ausgang setzen
}

void loop() {
  digitalWrite(mosfetPin, HIGH); // MOSFET EINSCHALTEN
  delay(1000);                   // 1 Sekunde warten
  digitalWrite(mosfetPin, LOW);  // MOSFET AUSSCHALTEN
  delay(1000);                   // 1 Sekunde warten
}
```
- **Ausgabe:** Last schaltet sich jede Sekunde ein und aus.

#### **PWM-Dimmung (für LEDs/Motoren)**
```cpp
const int mosfetPin = 9;

void setup() {
  pinMode(mosfetPin, OUTPUT);
}

void loop() {
  for (int helligkeit = 0; helligkeit <= 255; helligkeit += 5) {
    analogWrite(mosfetPin, helligkeit); // Helligkeit erhöhen
    delay(50);
  }
  for (int helligkeit = 255; helligkeit >= 0; helligkeit -= 5) {
    analogWrite(mosfetPin, helligkeit); // Helligkeit verringern
    delay(50);
  }
}
```
- **Ausgabe:** Last (z.B. LED) leuchtet langsam auf und ab.

---

### **Schritt 3: Testen und Überprüfen**

1. **Code hochladen:** Verwenden Sie die Arduino IDE, um einen der Sketche hochzuladen.
2. **Stromversorgung anschließen:** Schließen Sie den Arduino via USB und die externe Stromversorgung für die Last an.
3. **Beobachten:**
   - Beim Ein/Aus-Code sollte die Last im Sekundentakt schalten.
   - Bei PWM sollte die Last allmählich heller und dunkler werden.
4. **Messen:** Verwenden Sie ein Multimeter, um zu prüfen:
   - Spannung am Gate (0V oder 5V).
   - Spannung über der Last (0V oder V_Last).

---

### **Den richtigen MOSFET wählen**
- **Logik-Level-MOSFET (z.B. IRL540, 2N7000):** Schaltet mit 5V vom Arduino vollständig durch. Bevorzugt für dieses Projekt.
- **Standard-MOSFET (z.B. IRF540):** Benötigt ~10V am Gate für vollständiges Durchschalten. Bei 5V könnte er nur teilweise leiten – verwenden Sie einen Transistor oder Treiber (z.B. BJT oder IC wie TC4420), um die Gate-Spannung zu erhöhen, falls Sie diese verwenden.
- **Spezifikationen:** Prüfen Sie, ob V_DS (max. Spannung) und I_D (max. Strom) Ihrer Last entsprechen (z.B. IRF540: 100V, 33A).

---

### **Alternative: MOSFET-Verstärker**
Falls Sie einen MOSFET-basierten Verstärker (z.B. Common-Source-Verstärker) meinten, hier eine kurze Übersicht:
- **Aufbau:** Ähnlich dem CE-Verstärker, aber mit einem MOSFET (z.B. 2N7000).
- **Schaltplan:** Vcc → RD (Drain-Widerstand) → Drain; Source → GND; Gate → Eingangssignal (über Kondensator).
- **Rolle des Arduino:** Erzeugt ein kleines AC-Signal (wie im CE-Verstärker-Beispiel).
- **Verstärkung:** \\( A_v = -g_m \cdot R_D \\), wobei \\( g_m \\) die Steilheit ist.
- **Herausforderung:** Erfordert präzise Vorspannung; weniger gebräuchlich für Anfänger als BJT-Verstärker.

Lassen Sie es mich wissen, wenn Sie stattdessen hierauf umschwenken möchten!

---

### **Tipps und Fehlerbehebung**
- **Hitze:** Wenn der MOSFET heiß wird, schaltet er nicht vollständig durch (Logik-Level-Kompatibilität prüfen) oder die Last übersteigt seine Nennwerte – fügen Sie einen Kühlkörper hinzu oder reduzieren Sie den Strom.
- **Keine Reaktion:** Verbindungen, MOSFET-Pinbelegung (GDS) und Stromversorgung überprüfen.
- **Rauschen:** PWM-Schalten kann bei Motoren hörbar sein – ggf. Frequenz anpassen (fortgeschrittene Anpassung).
- **Höhere Spannung:** Für Lasten >5V sicherstellen, dass die V_GS-Schwellenspannung des MOSFETs erreicht wird.

Dieses Projekt zeigt, wie man einen MOSFET mit dem Arduino für die praktische Steuerung integriert. Möchten Sie es erweitern (z.B. Motor-Geschwindigkeitsregelung) oder stattdessen Verstärkung erkunden? Sagen Sie einfach Bescheid!