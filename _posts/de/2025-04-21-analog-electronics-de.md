---
audio: false
generated: true
lang: de
layout: post
title: Analoge Elektronik
translated: true
type: note
---

Fantastisch! Hier ist ein umfassendes Tutorial zu **Teil I: Analoge Elektronik** aus *Grundlagen der Elektronik (III)*. Ich werde es abschnittsweise mit Erklärungen, Diagrammen (wo hilfreich) und Praxisbezug aufschlüsseln.

---

## 🔹 Teil I: Analoge Elektronik

---

### **1. Grundlagen der Schaltungsanalyse**

#### a. **Grundlegende Schaltungsbegriffe und Gesetze**
- **Spannung (V)**: Elektrische Potentialdifferenz zwischen zwei Punkten.
- **Strom (I)**: Fluss elektrischer Ladung; gemessen in Ampere (A).
- **Widerstand (R)**: Opposition zum Stromfluss; gemessen in Ohm (Ω).
- **Leistung (P)**: Pro Zeiteinheit verbrauchte Energie: \\( P = VI \\)

#### ⚡ **Ohmsches Gesetz**
\\[
V = IR
\\]
Einfach und entscheidend. Es setzt Spannung, Strom und Widerstand in einem linearen Widerstand in Beziehung.

#### ⚡ **Kirchhoffsche Gesetze**
- **KCL (Knotenregel)**: Die Summe der in einen Knoten hineinfließenden Ströme ist gleich der Summe der herausfließenden Ströme.
  \\[
  \sum I_{in} = \sum I_{out}
  \\]
- **KVL (Maschenregel)**: Die Summe der Spannungen in einer geschlossenen Masche ist null.
  \\[
  \sum V = 0
  \\]

#### b. **Methoden zur Analyse linearer Schaltungen**
- **Knotenpotentialanalyse**: Löse nach Knotenspannungen mit KCL.
  - Wähle einen Referenzknoten (Masse).
  - Stelle Stromgleichungen für jeden Knoten auf.
- **Überlagerungssatz**:
  - Bei linearen Schaltungen mit mehreren Quellen, analysiere eine Quelle nach der anderen.
  - Ersetze andere Spannungsquellen durch Kurzschlüsse und Stromquellen durch Unterbrechungen.

#### c. **Schaltvorgänge und Einschwingverhalten**
- **RC- und RL-Schaltungen**: Einschwingverhalten beim Ein- und Ausschalten.
  - Kondensatorspannung: \\( V(t) = V_0 (1 - e^{-t/RC}) \\)
  - Induktorstrom: \\( I(t) = I_0 (1 - e^{-t/LR}) \\)
- **Zeitkonstanten**: RC oder L/R; gibt an, wie schnell Schaltungen auf Änderungen reagieren.

---

### **2. Grundlagen von Verstärkerschaltungen**

#### a. **Halbleiterbauelemente**
- **Dioden**: Lassen Strom nur in eine Richtung fließen; werden in Gleichrichtern verwendet.
- **Bipolare Transistoren (BJTs)**:
  - Drei Anschlüsse: Basis, Kollektor, Emitter.
  - **Aktiver Bereich**: Stromverstärkung.
  - **Kennlinien**: Zeigen Ausgangsstrom über Kollektor-Emitter-Spannung.

#### b. **Grundlegende Verstärkerschaltungen**
- **Common Emitter (CE) (Basissschaltung)**:
  - Hohe Verstärkung.
  - Phasenverschiebung: 180°.
- **Common Collector (CC) (Kollektorschaltung / Emitterfolger)**:
  - Verstärkung ≈1, aber exzellenter Impedanzwandler.
- **Common Base (CB) (Basisschaltung)**:
  - Niedrige Eingangsimpedanz, Anwendungen bei hohen Frequenzen.

#### c. **Frequenzgang und Stabilität**
- **Bandbreite**: Frequenzbereich, in dem der Verstärker gut funktioniert.
- **Verstärkungs-Bandbreite-Produkt**: Kompromiss zwischen Verstärkung und Geschwindigkeit.
- **Stabilität**: Vermeidung von Schwingungen, oft gesteuert durch Rückkopplung.

---

### **3. Operationsverstärker (Op-Amps) und Anwendungen**

#### a. **Op-Amp Eigenschaften**
- **Idealer Op-Amp**:
  - Unendliche Verstärkung
  - Unendliche Eingangsimpedanz
  - Null Ausgangsimpedanz
- **Virtueller Kurzschluss**: \\( V_+ = V_- \\), wenn Gegenkopplung vorhanden ist.
- **Virtueller Leerlauf**: Eingangsstrom ≈ 0

#### b. **Typische Op-Amp Schaltungen**
- **Invertierender Verstärker**:
  \\[
  V_{out} = -\left(\frac{R_f}{R_{in}}\right) V_{in}
  \\]
- **Nicht-invertierender Verstärker**:
  \\[
  V_{out} = \left(1 + \frac{R_f}{R_1}\right) V_{in}
  \\]
- **Integrator / Differenzierer**: Verwendet Kondensator in der Rückkopplung oder am Eingang.

#### c. **Nichtlineare Anwendungen**
- **Komparator**: Vergleicht zwei Spannungen, gibt High oder Low aus.
- **Schmitt-Trigger**: Fügt einem Komparator Hysterese für Rauschunterdrückung hinzu.
- **Signalgeneratoren**: Erzeugen Rechteck-, Dreieck- oder Sinussignale mit Op-Amps und Rückkopplung.

---

### **4. Gleichstromnetzteile**

#### a. **Gleichrichter- und Filter-Schaltungen**
- **Einweggleichrichter**: Verwendet eine Diode.
- **Brückengleichrichter (Zweiweggleichrichter)**: Verwendet vier Dioden (Brücke).
- **Filter**: Meist Kondensatoren zum Glätten der Ausgangsspannung.

#### b. **Lineare vs. Schaltnetzteile**
- **Linearregler**:
  - Einfach, stabil, aber ineffizient (Verlustwärme).
  - Beispiel: 7805 (5V Ausgang)
- **Schaltregler**:
  - Verwendet schnelles Schalten und Induktivitäten/Kondensatoren.
  - Hoher Wirkungsgrad.
  - Typen: Tiefsetzsteller (Buck), Hochsetzsteller (Boost), Tief-Hochsetzsteller (Buck-Boost).