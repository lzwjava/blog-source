---
audio: false
generated: true
lang: de
layout: post
title: Operationsverstärker
translated: true
type: note
---

Hier folgt ein umfassendes Tutorial zu **Operationsverstärkern (Op-Amps) und ihren Anwendungen**, das die angegebenen Themen abdeckt: Op-Amp-Eigenschaften und Parameter (virtueller Kurzschluss, virtueller offener Eingang), typische Op-Amp-Schaltungen (invertierende/nicht-invertierende Verstärker, Integratoren/Differentiatoren) und nichtlineare Anwendungen (Komparatoren, Oszillatoren). Dieses Tutorial ist gründlich, einsteigerfreundlich und technisch präzise, mit praktischen Beispielen und Erklärungen.

---

Operationsverstärker (Op-Amps) sind vielseitige elektronische Verstärker mit hoher Verstärkung, die in analogen Schaltungen zur Signalverarbeitung, Verstärkung, Filterung und mehr weit verbreitet sind. Dieses Tutorial führt Sie durch ihre Eigenschaften, wichtige Schaltungen und nichtlineare Anwendungen.

---

### **1. Op-Amp-Eigenschaften und Parameter**

Ein Operationsverstärker ist ein hochverstärkender, direktgekoppelter Verstärker mit differenziellen Eingängen und einem einzelnen Ausgang. Er wird typischerweise mit externen Rückkopplungskomponenten (Widerstände, Kondensatoren usw.) verwendet, um seine Funktion zu definieren. Nachfolgend sind die wichtigsten Eigenschaften und Parameter eines idealen Op-Amps zusammen mit ihren praktischen Auswirkungen aufgeführt.

#### **Ideale Op-Amp-Eigenschaften**
1.  **Unendliche Leerlaufverstärkung (A_OL)**
    *   Die Leerlaufverstärkung (ohne Rückkopplung) ist theoretisch unendlich, was bedeutet, dass selbst ein winziger Unterschied zwischen den Eingangsklemmen eine große Ausgangsspannung erzeugt. In der Praxis haben echte Op-Amps eine Leerlaufverstärkung von 10^5 bis 10^6.
    *   **Implikation**: Ermöglicht eine präzise Steuerung, wenn eine Rückkopplung angewendet wird.

2.  **Unendliche Eingangsimpedanz**
    *   Die Eingangsklemmen ziehen keinen Strom (die ideale Eingangsimpedanz ist unendlich). Bei echten Op-Amps liegt die Eingangsimpedanz typischerweise im Bereich von Megaohm bis Gigaohm.
    *   **Implikation**: Der Op-Amp belastet die Eingangssignalquelle nicht und erhält so die Signalintegrität.

3.  **Null Ausgangsimpedanz**
    *   Der Ausgang kann jede Last treiben, ohne einen Spannungsabfall zu verursachen. Echte Op-Amps haben eine niedrige Ausgangsimpedanz (z.B. 10–100 Ohm).
    *   **Implikation**: Sichert einen effizienten Signaltransfer zur nächsten Stufe.

4.  **Unendliche Bandbreite**
    *   Ein idealer Op-Amp verstärkt alle Frequenzen gleich. In der Praxis begrenzt das Gain-Bandwidth-Produkt die Leistung (z.B. Unity-Gain-Bandbreite von 1 MHz für einen 741 Op-Amp).
    *   **Implikation**: Die Bandbreite nimmt mit zunehmender Verstärkung in geschlossenen Regelkreisen ab.

5.  **Null Offset-Spannung**
    *   Ohne Eingangssignal ist der Ausgang null. Echte Op-Amps haben kleine Offset-Spannungen (Mikrovolt bis Millivolt), die kompensiert werden müssen.
    *   **Implikation**: Minimiert unerwünschte Ausgangsspannungen in Präzisionsanwendungen.

6.  **Unendliche Gleichtaktunterdrückung (CMRR)**
    *   Der Op-Amp unterdrückt Signale, die beiden Eingängen gemeinsam sind (z.B. Rauschen). Echte Op-Amps haben eine hohe CMRR (80–120 dB).
    *   **Implikation**: Reduziert Rauschen in differenziellen Signal-Anwendungen.

#### **Schlüsselkonzepte: Virtueller Kurzschluss und Virtueller offener Eingang**
*   **Virtueller Kurzschluss**
    *   In einer Gegenkopplungskonfiguration zwingt die hohe Leerlaufverstärkung die Spannungsdifferenz zwischen dem invertierenden (-) und dem nicht-invertierenden (+) Eingang dazu, nahezu null zu sein.
    *   **Erklärung**: Der Op-Amp passt seinen Ausgang an, um V+ ≈ V- zu erreichen (unter der Annahme einer Gegenkopplung). Dies wird als "virtueller Kurzschluss" bezeichnet, weil die Eingänge nicht physisch kurzgeschlossen sind, sich aber so verhalten, als ob sie es wären.
    *   **Beispiel**: In einem invertierenden Verstärker, wenn der nicht-invertierende Eingang geerdet ist (0 V), passt der Op-Amp den Ausgang an, um den invertierenden Eingang auf ungefähr 0 V zu halten.

*   **Virtueller offener Eingang**
    *   Aufgrund der unendlichen Eingangsimpedanz fließt kein Strom in die Eingangsklemmen des Op-Amps.
    *   **Erklärung**: Dieser "virtuelle offene Eingang" bedeutet, dass sich die Eingänge in Bezug auf den Stromfluss so verhalten, als wären sie vom Stromkreis getrennt, sodass der gesamte Eingangsstrom durch externe Komponenten fließt.
    *   **Beispiel**: In einem Spannungsfolger fließt kein Strom in die Op-Amp-Eingänge, was ihn zu einem idealen Buffer macht.

#### **Praktische Parameter**
*   **Slew Rate**: Die maximale Änderungsrate der Ausgangsspannung (z.B. 0,5 V/µs für einen 741 Op-Amp). Begrenzt die Hochfrequenzleistung.
*   **Eingangsruhestrom**: Kleine Ströme (nA bis pA), die von echten Op-Amp-Eingängen benötigt werden.
*   **Störungsunterdrückung der Versorgungsspannung (PSRR)**: Fähigkeit, Versorgungsrauschen zu unterdrücken.
*   **Rauschen**: Internes Rauschen begrenzt die Leistung bei Anwendungen mit niedrigen Signalen.

---

### **2. Typische Op-Amp-Schaltungen**

Op-Amps werden typischerweise in geschlossenen Regelkreisen mit Gegenkopplung verwendet, um stabile, vorhersagbare Schaltungen zu erstellen. Nachfolgend sind die gebräuchlichsten Schaltungen aufgeführt: invertierende und nicht-invertierende Verstärker, Integratoren und Differentiatoren.

#### **Invertierender Verstärker**
*   **Funktion**: Verstärkt das Eingangssignal und invertiert seine Phase (180° Phasenverschiebung).
*   **Schaltung**:
    *   Das Eingangssignal (V_in) wird über den Widerstand R1 an den invertierenden Eingang (-) angelegt.
    *   Der nicht-invertierende Eingang (+) ist geerdet (0 V).
    *   Ein Rückkopplungswiderstand (R_f) verbindet den Ausgang (V_out) mit dem invertierenden Eingang.
*   **Schlüsselgleichungen**:
    *   Spannungsverstärkung: \\( A_v = -\frac{R_f}{R_1} \\)
    *   Ausgangsspannung: \\( V_{out} = -\frac{R_f}{R_1} \cdot V_{in} \\)
    *   Eingangsimpedanz: Ungefähr \\( R_1 \\).
*   **Virtueller Kurzschluss**: Der invertierende Eingang liegt auf 0 V (gleich dem geerdeten nicht-invertierenden Eingang).
*   **Beispiel**: Für \\( R_1 = 10 \, \text{k}\Omega \\), \\( R_f = 20 \, \text{k}\Omega \\) und \\( V_{in} = 1 \, \text{V} \\):
    *   Verstärkung: \\( A_v = -\frac{20k}{10k} = -2 \\)
    *   Ausgang: \\( V_{out} = -2 \cdot 1 = -2 \, \text{V} \\).
*   **Anwendungen**: Audioverstärker, Signalinversion, Summierverstärker.

#### **Nicht-invertierender Verstärker**
*   **Funktion**: Verstärkt das Eingangssignal ohne Phaseninversion.
*   **Schaltung**:
    *   Das Eingangssignal (V_in) wird an den nicht-invertierenden Eingang (+) angelegt.
    *   Der Rückkopplungswiderstand (R_f) verbindet den Ausgang mit dem invertierenden Eingang (-), wobei der Widerstand R_1 vom invertierenden Eingang zur Masse führt.
*   **Schlüsselgleichungen**:
    *   Spannungsverstärkung: \\( A_v = 1 + \frac{R_f}{R_1} \\)
    *   Ausgangsspannung: \\( V_{out} = \left(1 + \frac{R_f}{R_1}\right) \cdot V_{in} \\)
    *   Eingangsimpedanz: Sehr hoch (aufgrund des nicht-invertierenden Eingangs).
*   **Virtueller Kurzschluss**: Die Spannung am invertierenden Eingang entspricht V_in (aufgrund der Rückkopplung).
*   **Beispiel**: Für \\( R_1 = 10 \, \text{k}\Omega \\), \\( R_f = 30 \, \text{k}\Omega \\) und \\( V_{in} = 1 \, \text{V} \\):
    *   Verstärkung: \\( A_v = 1 + \frac{30k}{10k} = 4 \\)
    *   Ausgang: \\( V_{out} = 4 \cdot 1 = 4 \, \text{V} \\).
*   **Anwendungen**: Signalpufferung, Spannungsskalierung.

#### **Integrator**
*   **Funktion**: Integriert das Eingangssignal über die Zeit und erzeugt einen Ausgang, der proportional zum Integral des Eingangs ist.
*   **Schaltung**:
    *   Das Eingangssignal (V_in) wird über einen Widerstand R an den invertierenden Eingang angelegt.
    *   Ein Kondensator (C) wird in den Rückkopplungspfad gelegt (vom Ausgang zum invertierenden Eingang).
    *   Der nicht-invertierende Eingang ist geerdet.
*   **Schlüsselgleichungen**:
    *   Ausgangsspannung: \\( V_{out} = -\frac{1}{R \cdot C} \int V_{in}(t) \, dt \\)
    *   Der Ausgang ist das negative Integral des Eingangs.
*   **Virtueller Kurzschluss**: Der invertierende Eingang liegt auf 0 V.
*   **Praktische Überlegungen**:
    *   Ein Widerstand parallel zum Kondensator kann hinzugefügt werden, um die Niederfrequenzverstärkung zu begrenzen und eine Sättigung zu verhindern.
    *   Begrenzt durch die Slew Rate des Op-Amps und Kondensatorleckströme.
*   **Beispiel**: Für \\( R = 10 \, \text{k}\Omega \\), \\( C = 1 \, \mu\text{F} \\) und konstantes \\( V_{in} = 1 \, \text{V} \\):
    *   Ausgang: \\( V_{out} = -\frac{1}{10k \cdot 1\mu} \int 1 \, dt = -100 \cdot t \, \text{V/s} \\).
    *   Nach 1 ms: \\( V_{out} = -0.1 \, \text{V} \\).
*   **Anwendungen**: Analogrechner, Signalverarbeitung, Tiefpassfilter.

#### **Differentiator**
*   **Funktion**: Differenziert das Eingangssignal und erzeugt einen Ausgang, der proportional zur Änderungsrate des Eingangs ist.
*   **Schaltung**:
    *   Das Eingangssignal (V_in) wird über einen Kondensator (C) an den invertierenden Eingang angelegt.
    *   Ein Widerstand (R) wird in den Rückkopplungspfad gelegt.
    *   Der nicht-invertierende Eingang ist geerdet.
*   **Schlüsselgleichungen**:
    *   Ausgangsspannung: \\( V_{out} = -R \cdot C \cdot \frac{dV_{in}}{dt} \\)
    *   Der Ausgang ist die negative Ableitung des Eingangs.
*   **Virtueller Kurzschluss**: Der invertierende Eingang liegt auf 0 V.
*   **Praktische Überlegungen**:
    *   Anfällig für die Verstärkung von Hochfrequenzrauschen; ein kleiner Widerstand in Reihe mit dem Eingangskondensator kann die Schaltung stabilisieren.
*   **Beispiel**: Für \\( R = 10 \, \text{k}\Omega \\), \\( C = 1 \, \mu\text{F} \\) und \\( V_{in} = t \, \text{V} \\) (lineare Rampe):
    *   Ausgang: \\( V_{out} = -10k \cdot 1\mu \cdot \frac{d(t)}{dt} = -0.01 \, \text{V} \\).
*   **Anwendungen**: Flankendetektion, Hochpassfilter.

---

### **3. Nichtlineare Anwendungen**

Op-Amps können in nichtlinearen Modi arbeiten (ohne Gegenkopplung oder mit spezifischen Komponenten), um Aufgaben wie Signalvergleich oder Wellenformgenerierung durchzuführen.

#### **Komparator**
*   **Funktion**: Vergleicht zwei Eingangsspannungen und gibt ein hohes oder niedriges Signal aus, basierend darauf, welche größer ist.
*   **Schaltung**:
    *   Eine Eingangsspannung (z.B. V_ref) wird an den nicht-invertierenden Eingang (+) angelegt.
    *   Die andere Eingangsspannung (V_in) wird an den invertierenden Eingang (-) angelegt.
    *   Keine Rückkopplung (Leerlauf-Konfiguration).
*   **Funktionsweise**:
    *   Wenn V_in > V_ref, schwingt der Ausgang zur negativen Versorgungsspannung (z.B. -V_cc).
    *   Wenn V_in < V_ref, schwingt der Ausgang zur positiven Versorgungsspannung (z.B. +V_cc).
*   **Schlüsselmerkmale**:
    *   Arbeitet im Leerlaufmodus und nutzt die hohe Verstärkung des Op-Amps, um einen binären Ausgang zu erzeugen.
    *   Echte Op-Amps haben eine endliche Slew Rate, was eine leichte Verzögerung beim Schalten verursacht.
*   **Beispiel**: Für V_ref = 2 V und V_in = 3 V, mit ±12 V Versorgungsspannung:
    *   Da V_in > V_ref, ist V_out ≈ -12 V.
*   **Anwendungen**:
    *   Nulldurchgangsdetektoren, Schwellwertdetektoren, Analog-Digital-Wandlung.
*   **Praktische Überlegungen**:
    *   Hysterese (Mitkopplung) hinzufügen, um Oszillationen nahe der Schwelle zu verhindern (Schmitt-Trigger-Konfiguration).
    *   Dedizierte Komparator-ICs (z.B. LM339) werden oft für schnelleres Schalten bevorzugt.

#### **Oszillatoren**
*   **Funktion**: Erzeugen periodische Wellenformen (z.B. Rechteck-, Dreieck- oder Sinuswellen) unter Verwendung von Op-Amps mit Rückkopplungsnetzwerken.
*   **Typen**:
    1.  **Rechteckgenerator (Astable Multivibrator)**:
        *   **Schaltung**: Verwendet einen Op-Amp mit Mitkopplung über Widerstände und einen Kondensator im Gegenkopplungspfad.
        *   **Funktionsweise**: Der Kondensator lädt und entlädt sich zwischen Schwellspannungen, die durch die Widerstände eingestellt werden, was dazu führt, dass der Ausgang zwischen den Versorgungsspannungen schaltet.
        *   **Frequenz**: Bestimmt durch die RC-Zeitkonstante, z.B. \\( f = \frac{1}{2 \cdot R \cdot C \cdot \ln(3)} \\) (annähernd für einige Konfigurationen).
        *   **Beispiel**: Für \\( R = 10 \, \text{k}\Omega \\), \\( C = 0.1 \, \mu\text{F} \\) beträgt die Frequenz ungefähr 1 kHz.
        *   **Anwendungen**: Taktsignale, Impulserzeugung.

    2.  **Dreieckspannungsgenerator**:
        *   **Schaltung**: Kombiniert typischerweise einen Rechteckgenerator (Komparator mit Mitkopplung) mit einem Integrator.
        *   **Funktionsweise**: Die Rechteckwelle treibt den Integrator an und erzeugt eine lineare Rampe (Dreieckwelle).
        *   **Beispiel**: Eine 1 kHz Rechteckwelle, die in einen Integrator mit \\( R = 10 \, \text{k}\Omega \\), \\( C = 0.1 \, \mu\text{F} \\) eingespeist wird, erzeugt eine 1 kHz Dreieckwelle.
        *   **Anwendungen**: Tests Signale, Pulsweitenmodulation (PWM).

    3.  **Sinusgenerator (Wien-Brücken-Oszillator)**:
        *   **Schaltung**: Verwendet Mitkopplung über ein frequenzselektives Netzwerk (Widerstände und Kondensatoren) und Gegenkopplung zur Amplitudenstabilisierung.
        *   **Funktionsweise**: Schwingt bei einer Frequenz, bei der die Phasenverschiebung null ist, z.B. \\( f = \frac{1}{2 \pi R C} \\).
        *   **Beispiel**: Für \\( R = 1.59 \, \text{k}\Omega \\), \\( C = 0.01 \, \mu\text{F} \\) beträgt die Frequenz ~10 kHz.
        *   **Anwendungen**: Audio-Signalerzeugung, Tests.

---

### **Praktische Design-Überlegungen**
1.  **Stromversorgung**: Op-Amps benötigen duale (z.B. ±12 V) oder einfache Versorgungsspannungen (z.B. 0 bis 5 V für Rail-to-Rail Op-Amps). Stellen Sie sicher, dass die Versorgungsspannung den Eingangs- und Ausgangssignalbereich unterstützt.
2.  **Komponentenauswahl**: Verwenden Sie Präzisionswiderstände und -kondensatoren für eine genaue Verstärkung und Frequenzgang. Überprüfen Sie die Datenblätter der Op-Amps auf Bandbreite, Slew Rate und Rauschspezifikationen.
3.  **Stabilität**: Vermeiden Sie Oszillationen, indem Sie eine ordnungsgemäße Rückkopplung sicherstellen und die Stromversorgung mit Kondensatoren (z.B. 0,1 µF in der Nähe des Op-Amps) entkoppeln.
4.  **Einschränkungen**: Echte Op-Amps weichen vom idealen Verhalten ab (z.B. endliche Verstärkung, Bandbreite, Slew Rate). Wählen Sie Op-Amps wie den LM358 (Allzweck), TL081 (rauscharm) oder OPA2134 (Audio) basierend auf den Anwendungsanforderungen.

---

### **Beispielanwendung: Audio-Preamplifier**
Entwerfen wir einen einfachen invertierenden Audio-Preamplifier:
*   **Anforderungen**: Verstärken eines 50 mV Audiosignals auf 500 mV (Verstärkung = 10).
*   **Schaltung**: Invertierender Verstärker mit \\( R_1 = 10 \, \text{k}\Omega \\), \\( R_f = 100 \, \text{k}\Omega \\).
*   **Berechnung**: \\( A_v = -\frac{100k}{10k} = -10 \\), \\( V_{out} = -10 \cdot 0.05 = -0.5 \, \text{V} \\).
*   **Überlegungen**: Verwenden Sie einen rauscharmen Op-Amp (z.B. OPA2134), fügen Sie einen Koppelkondensator hinzu, um DC zu blockieren, und stellen Sie sicher, dass die Stromversorgung den Signalbereich unterstützt (z.B. ±5 V).

---

### **Schlussfolgerung**
Operationsverstärker sind grundlegende Bausteine in der Analogelektronik und bieten Flexibilität für Verstärkung, Signalverarbeitung und Wellenformerzeugung. Indem Sie ihre Eigenschaften (virtueller Kurzschluss, virtueller offener Eingang usw.) verstehen und die Beherrschung der Schlüsselschaltungen (invertierende/nicht-invertierende Verstärker, Integratoren, Differentiatoren, Komparatoren, Oszillatoren) beherrschen, können Sie eine Vielzahl von Schaltungen entwerfen. Berücksichtigen Sie stets die Einschränkungen der realen Welt und wählen Sie die Komponenten sorgfältig für eine optimale Leistung aus.

Für weitere Erkundungen experimentieren Sie mit Simulationswerkzeugen wie LTspice oder Breadboard-Prototyping und ziehen Sie Op-Amp-Datenblätter für spezifische Anwendungen zu Rate.

---

Wenn Sie eine spezifische Schaltungssimulation, mathematische Herleitung oder ein Diagramm (z.B. Frequenzgang eines Integrators) wünschen, lassen Sie es mich wissen, und ich kann weitere Details oder Visualisierungen bereitstellen!