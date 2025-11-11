---
audio: false
generated: true
lang: de
layout: post
title: Gleichstromnetzteile
translated: true
type: note
---

Dieses Tutorial bietet eine detaillierte Erkundung von **DC-Netzteilen** mit Schwerpunkt auf **Gleichrichter- und Filterkreisen** (Einweg- und Brückengleichrichter) und den Unterschieden zwischen **linearen und Schaltreglern**. Es enthält theoretische Erklärungen, praktische Beispiele, Schaltungsdesigns und reale Anwendungen, um ein gründliches Verständnis für Anfänger und fortgeschrittene Lerner zu gewährleisten.

---

## Inhaltsverzeichnis
1. **Einführung in DC-Netzteile**
2. **Gleichrichter- und Filterkreise**
   - Einweggleichrichter
   - Zweiweggleichrichter (Brückenkonfiguration)
   - Filterkreise
3. **Lineare vs. Schaltregler**
   - Lineare Regler
   - Schaltregler (Buck, Boost, Buck-Boost)
4. **Praktische Beispiele und Schaltungsdesign**
5. **Anwendungen und Überlegungen**
6. **Schlussfolgerung**

---

## 1. Einführung in DC-Netzteile
Ein **DC-Netzteil** wandelt Wechselstrom (AC) in Gleichstrom (DC) um, um elektronische Geräte wie Mikrocontroller, Sensoren und integrierte Schaltkreise mit Strom zu versorgen. Der Prozess umfasst typischerweise:
- **Gleichrichtung**: Umwandlung von AC in pulsierenden DC.
- **Filterung**: Glättung des pulsierenden DC.
- **Regelung**: Stabilisierung der Ausgangsspannung oder des Ausgangsstroms.

DC-Netzteile sind in der Elektronik von entscheidender Bedeutung, da sie sicherstellen, dass Geräte stabilen, rauscharmen Strom erhalten. Die beiden hier behandelten Hauptkomponenten sind **Gleichrichter-/Filterkreise** und **Spannungsregler** (linear und schaltend).

---

## 2. Gleichrichter- und Filterkreise

Gleichrichterschaltungen wandeln AC in DC um, und Filter glätten den Ausgang, um die Welligkeit zu reduzieren. Lassen Sie uns das aufschlüsseln.

### a. Einweggleichrichter
Der **Einweggleichrichter** ist die einfachste Gleichrichterschaltung und verwendet eine einzelne Diode.

#### Funktionsweise
- **Eingang**: AC-Spannung (z.B. von einem Transformator).
- **Betrieb**: Die Diode leitet nur während der positiven Halbwelle der AC-Wellenform und blockiert die negative Halbwelle.
- **Ausgang**: Pulsierender DC mit der gleichen Frequenz wie der AC-Eingang, enthält nur die positiven (oder negativen, je nach Diodenausrichtung) Halbwellen.

#### Schaltplan
```
AC-Quelle ----> Diode (D1) ----> Last (R) ----> Masse
```
- **Komponenten**:
  - **Diode**: Z.B. 1N4007 (Allzweck-Gleichrichterdiode).
  - **Last**: Ein Widerstand oder elektronische Schaltung.

#### Eigenschaften
- **Ausgangsspannung**: Ungefähr \\( V_{out} = V_{in(peak)} - V_{diode} \\) (wobei \\( V_{diode} \approx 0,7V \\) für Siliziumdioden).
- **Effizienz**: Niedrig (~40,6 %), da nur die Hälfte des AC-Zyklus genutzt wird.
- **Welligkeit**: Hoch, da der Ausgang intermittierend ist.

#### Vorteile
- Einfach und kostengünstig.
- Benötigt minimale Komponenten.

#### Nachteile
- Ineffizient (verschwendet die Hälfte des AC-Zyklus).
- Hohe Welligkeit, erfordert große Filter für glatten DC.

---

### b. Zweiweggleichrichter (Brückenkonfiguration)
Der **Zweiweggleichrichter** nutzt sowohl die positiven als auch die negativen Halbwellen des AC-Eingangs und erzeugt einen gleichmäßigeren DC-Ausgang.

#### Funktionsweise
- **Konfiguration**: Verwendet vier Dioden in einer **Brückengleichrichter**-Anordnung.
- **Betrieb**:
  - Während der positiven Halbwelle leiten zwei Dioden und leiten den Strom durch die Last.
  - Während der negativen Halbwelle leiten die anderen beiden Dioden und halten die gleiche Stromrichtung durch die Last aufrecht.
- **Ausgang**: Pulsierender DC mit der doppelten Frequenz des AC-Eingangs.

#### Schaltplan
```
       AC-Eingang
         ------
        |      |
   D1 --|-->|--|-->|-- D2
        |      |       |
        |      R       |
        |      |       |
   D3 --|<--|--|<--|-- D4
        |      |
         ------
       Masse
```
- **Komponenten**:
  - **Dioden**: Vier Dioden (z.B. 1N4007).
  - **Last**: Widerstand oder Schaltung.
  - **Transformator** (optional): Transformiert die AC-Spannung herunter.

#### Eigenschaften
- **Ausgangsspannung**: \\( V_{out} = V_{in(peak)} - 2V_{diode} \\) (zwei Dioden leiten gleichzeitig, also ~1,4V Abfall für Siliziumdioden).
- **Effizienz**: Höher (~81,2 %) als beim Einweggleichrichter.
- **Welligkeit**: Geringer als beim Einweggleichrichter, da die Pulse doppelt so häufig auftreten.

#### Vorteile
- Effizienter, da der volle AC-Zyklus genutzt wird.
- Reduzierte Welligkeit, erfordert kleinere Filter.

#### Nachteile
- Komplexer (vier Dioden).
- Leicht höherer Spannungsabfall (aufgrund von zwei Dioden).

---

### c. Filterkreise
Gleichrichter erzeugen pulsierenden DC, der für die meisten elektronischen Geräte aufgrund von **Welligkeit** (Spannungsschwankungen) ungeeignet ist. Filter glätten den Ausgang, um einen annähernd konstanten DC zu erreichen.

#### Häufiger Filter: Kondensatorfilter
Ein **Kondensatorfilter** ist die gebräuchlichste Methode und wird parallel zur Last geschaltet.

#### Funktionsweise
- **Aufladung**: Während des Spitzenwerts der gleichgerichteten Wellenform lädt sich der Kondensator auf die Spitzenspannung auf.
- **Entladung**: Wenn die gleichrichtete Spannung sinkt, entlädt sich der Kondensator durch die Last und hält so eine konstantere Spannung aufrecht.
- **Ergebnis**: Glatterer DC mit reduzierter Welligkeit.

#### Schaltplan (Zweiweg mit Kondensatorfilter)
```
       AC-Eingang
         ------
        |      |
   D1 --|-->|--|-->|-- D2
        |      |       |
        |      R       C (Kondensator)
        |      |       |
   D3 --|<--|--|<--|-- D4
        |      |
         ------
       Masse
```
- **Komponenten**:
  - **Kondensator**: Der Wert hängt vom Laststrom und der Welligkeitstoleranz ab (z.B. 1000µF für moderate Lasten).
  - **Last**: Widerstand oder Schaltung.

#### Welligkeitsberechnung
Die Welligkeitsspannung (\\( V_r \\)) kann angenähert werden als:
\\[ V_r \approx \frac{I_{last}}{f \cdot C} \\]
Wobei:
- \\( I_{last} \\): Laststrom (A).
- \\( f \\): Frequenz des gleichgerichteten Ausgangs (z.B. 120Hz für Zweiweg bei 60Hz AC).
- \\( C \\): Kapazität (F).

#### Beispiel
Für einen Laststrom von 100mA, einen 1000µF Kondensator und eine Frequenz von 120Hz:
\\[ V_r \approx \frac{0,1}{120 \cdot 1000 \times 10^{-6}} \approx 0,833V \\]
Diese Welligkeit kann für einige Anwendungen akzeptabel sein, kann aber mit einem größeren Kondensator oder zusätzlicher Filterung (z.B. LC-Filter) reduziert werden.

#### Andere Filter
- **Induktorfilter**: Verwendet eine Spule in Reihe mit der Last, um schnellen Stromänderungen entgegenzuwirken.
- **LC-Filter**: Kombiniert Spule und Kondensator für eine bessere Welligkeitsreduzierung.
- **Pi-Filter**: Kondensator-Spule-Kondensator (C-L-C) Konfiguration für sehr glatten DC.

---

## 3. Lineare vs. Schaltregler

Nach der Gleichrichtung und Filterung kann die DC-Spannung immer noch mit Eingangsänderungen oder Lastanforderungen variieren. **Spannungsregler** stabilisieren den Ausgang. Es gibt zwei Haupttypen: **linear** und **schaltend**.

### a. Lineare Regler
Lineare Regler stellen eine stabile Ausgangsspannung bereit, indem sie überschüssige Leistung als Wärme abführen.

#### Funktionsweise
- Verhält sich wie ein variabler Widerstand, der seinen Widerstand anpasst, um eine konstante Ausgangsspannung aufrechtzuerhalten.
- Erfordert, dass die Eingangsspannung höher ist als die gewünschte Ausgangsspannung (Dropout-Spannung).

#### Beispiel: 7805 Linearregler
Der **7805** ist ein beliebter Linearregler, der eine feste 5V Ausgangsspannung liefert.

#### Schaltplan
```
Vin ----> [7805] ----> Vout (5V)
       |         |
      C1        C2
       |         |
      Masse    Masse
```
- **Komponenten**:
  - **7805 IC**: Gibt 5V aus (bis zu 1A mit passender Kühlung).
  - **Kondensatoren**: C1 (0,33µF) und C2 (0,1µF) für Stabilität.
  - **Vin**: Typischerweise 7-12V (muss >5V + Dropout-Spannung, ~2V sein).

#### Eigenschaften
- **Ausgang**: Fest (z.B. 5V für 7805) oder einstellbar (z.B. LM317).
- **Effizienz**: Niedrig, da überschüssige Spannung als Wärme abgeführt wird (\\( Effizienz \approx \frac{V_{out}}{V_{in}} \\)).
- **Rauschen**: Niedrig, ideal für empfindliche Analogschaltungen.

#### Vorteile
- Einfaches Design, einfach zu implementieren.
- Geringes Ausgangsrauschen, geeignet für Audio- und Präzisionsschaltungen.
- Kostengünstig.

#### Nachteile
- Ineffizient, besonders bei großen Spannungsdifferenzen.
- Erzeugt Wärme, erfordert Kühlkörper für hohe Ströme.
- Beschränkt auf Step-Down (Ausgang < Eingang).

---

### b. Schaltregler
Schaltregler verwenden Hochfrequenz-Schalten, um die Energieübertragung zu steuern, und erreichen so hohe Effizienz.

#### Funktionsweise
- Ein Schalter (normalerweise ein MOSFET) schaltet schnell ein/aus und steuert den Energiefluss durch Spulen und Kondensatoren.
- Eine Rückkopplungsschaltung passt den Schalt-Tastgrad an, um eine stabile Ausgabe aufrechtzuerhalten.

#### Arten von Schaltreglern
1. **Buck (Step-Down)**: Verringert die Spannung (z.B. 12V auf 5V).
2. **Boost (Step-Up)**: Erhöht die Spannung (z.B. 5V auf 12V).
3. **Buck-Boost**: Kann hoch- oder heruntertransformieren (z.B. 9V auf 5V oder 12V).

#### Schaltplan (Buck-Wandler Beispiel)
```
Vin ----> Schalter (MOSFET) ----> Induktor ----> Vout
       |                      |
      Diode                  Kondensator
       |                      |
      Masse                 Masse
```
- **Komponenten**:
  - **MOSFET**: Steuert das Schalten.
  - **Induktor**: Speichert Energie während des "Ein"-Zyklus.
  - **Kondensator**: Glättet den Ausgang.
  - **Diode**: Bietet einen Pfad für den Induktorstrom während des "Aus"-Zyklus.
  - **Controller-IC**: Z.B. LM2596 (einstellbarer Buck-Wandler).

#### Eigenschaften
- **Effizienz**: Hoch (80-95 %), da minimale Leistung als Wärme abgeführt wird.
- **Rauschen**: Höher als bei linearen Reglern aufgrund des Schaltens.
- **Flexibilität**: Kann hoch-, heruntertransformieren oder beides.

#### Vorteile
- Hohe Effizienz, ideal für batteriebetriebene Geräte.
- Kompakte Designs mit kleineren Kühlkörpern.
- Vielseitig (Buck-, Boost- oder Buck-Boost-Konfigurationen).

#### Nachteile
- Komplexer, erfordert Induktoren und sorgfältiges Design.
- Schaltrauschen kann empfindliche Schaltungen stören.
- Höhere Kosten aufgrund zusätzlicher Komponenten.

---

## 4. Praktische Beispiele und Schaltungsdesign

### Beispiel 1: 5V DC-Netzteil mit Einweggleichrichter und Linearregler
**Ziel**: Entwerfen Sie eine 5V DC-Versorgung aus einem 9V AC-Transformator.
**Schritte**:
1. **Gleichrichtung**: Verwenden Sie eine 1N4007 Diode für die Einweggleichrichtung.
2. **Filterung**: Fügen Sie einen 1000µF Kondensator hinzu, um den Ausgang zu glätten.
3. **Regelung**: Verwenden Sie einen 7805 Regler für eine stabile 5V Ausgabe.

**Schaltung**:
```
9V AC ----> 1N4007 ----> 1000µF ----> 7805 ----> 5V
                     |             |        |
                    Masse         C1       C2
                                   |        |
                                 Masse    Masse
```
- **C1**: 0,33µF (Eingangsstabilität).
- **C2**: 0,1µF (Ausgangsstabilität).

**Überlegungen**:
- Der Transformator muss nach der Gleichrichtung >7V DC liefern (9V AC ist ausreichend).
- Fügen Sie einen Kühlkörper zum 7805 hinzu, wenn der Laststrom 500mA überschreitet.

---

### Beispiel 2: 5V DC-Netzteil mit Zweiweggleichrichter und Schaltregler
**Ziel**: Entwerfen Sie eine hocheffiziente 5V-Versorgung aus einem 12V AC-Transformator.
**Schritte**:
1. **Gleichrichtung**: Verwenden Sie einen Brückengleichrichter (vier 1N4007 Dioden).
2. **Filterung**: Fügen Sie einen 2200µF Kondensator hinzu.
3. **Regelung**: Verwenden Sie einen LM2596 Abwärtswandler.

**Schaltung**:
```
12V AC ----> Brückengleichrichter ----> 2200µF ----> LM2596 ----> 5V
                         |                       |
                        Masse                  Masse
```
- **LM2596**: Konfiguriert für 5V Ausgang (einstellbar über Feedback-Widerstände).
- **Kondensatoren**: Befolgen Sie das LM2596 Datenblatt für Ein-/Ausgangskondensatoren.

**Überlegungen**:
- Stellen Sie eine ordnungsgemäße Induktorauswahl sicher (gemäß LM2596 Datenblatt).
- Fügen Sie EMI-Filterung hinzu, wenn in rauschempfindlichen Anwendungen verwendet.

---

## 5. Anwendungen und Überlegungen

### Anwendungen
- **Einweggleichrichter**: Kostengünstige, stromsparende Geräte (z.B. einfache Batterieladegeräte).
- **Zweiweggleichrichter**: Allzweck-Stromversorgungen für Elektronik.
- **Lineare Regler**: Audioschaltungen, Präzisionssensoren und stromsparende Geräte.
- **Schaltregler**: Laptops, Smartphones, LED-Treiber und batteriebetriebene Systeme.

### Design-Überlegungen
- **Lastanforderungen**: Stellen Sie sicher, dass die Versorgung den maximalen Strom bewältigen kann.
- **Effizienz**: Wählen Sie Schaltregler für Hochleistungsanwendungen.
- **Rauschen**: Verwenden Sie lineare Regler oder zusätzliche Filterung für empfindliche Schaltungen.
- **Wärmemanagement**: Beziehen Sie Kühlkörper oder ein geeignetes PCB-Layout für die Wärmeableitung ein.
- **Komponentenbewertungen**: Wählen Sie Dioden, Kondensatoren und Regler mit geeigneten Spannungs-/Strombewertungen.

---

## 6. Schlussfolgerung
DC-Netzteile sind unerlässlich für die Stromversorgung elektronischer Geräte, und das Verständnis ihrer Komponenten – Gleichrichter, Filter und Regler – ist der Schlüssel zum Entwerfen zuverlässiger Systeme. **Einweggleichrichter** sind einfach, aber ineffizient, während **Zweiweggleichrichter** eine bessere Leistung bieten. **Lineare Regler** sind ideal für rauscharme Anwendungen, verschwenden aber Energie, wohingegen **Schaltregler** hohe Effizienz für moderne, stromhungrige Geräte bieten. Durch die durchdachte Kombination dieser Elemente können Sie robuste Netzteile erstellen, die auf spezifische Bedürfnisse zugeschnitten sind.

Für praktisches Lernen versuchen Sie, die Beispielschaltungen mit einem Steckbrett oder Simulationssoftware wie LTspice aufzubauen. Experimentieren Sie mit verschiedenen Kondensatorwerten oder Reglertypen, um deren Auswirkungen auf die Leistung zu beobachten.