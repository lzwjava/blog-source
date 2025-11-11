---
audio: false
generated: true
lang: de
layout: post
title: Bipolare Sperrschichttranzistoren
translated: true
type: note
---

Bipolartransistoren (BJTs) sind grundlegende Halbleiterbauelemente, die zur Verstärkung, Schaltung und Signalverarbeitung eingesetzt werden. Es handelt sich um Drei-Anschluss-Bauelemente mit einer Struktur, die eine Stromsteuerung und -verstärkung ermöglicht, was sie für die Analog- und Digitalelektronik unverzichtbar macht. Lassen Sie uns, wie gewünscht, tief in ihre Struktur, Funktionsweise, Betriebsarten und Kennlinien eintauchen und dabei die Erklärung umfassend und dennoch zugänglich halten.

---

### **1. Struktur und Anschlüsse eines BJT**
Ein BJT besteht aus drei dotierten Halbleiterbereichen, die zwei p-n-Übergänge bilden, und wird in zwei Typen eingeteilt: **NPN** und **PNP**. Die drei Anschlüsse sind:

- **Basis (B)**: Ein dünner, schwach dotierter Bereich, der den Betrieb des Transistors steuert. Er fungiert als "Torwächter" für den Stromfluss.
- **Kollektor (C)**: Ein mäßig dotierter Bereich, der die Ladungsträger (Elektronen beim NPN, Löcher beim PNP) vom Emitter sammelt.
- **Emitter (E)**: Ein stark dotierter Bereich, der Ladungsträger in die Basis emittiert.

**NPN-BJT**: Besteht aus zwei n-Typ-Bereichen (Kollektor und Emitter), die einen dünnen p-Typ-Basisbereich umschließen. Elektronen sind die primären Ladungsträger.
**PNP-BJT**: Besteht aus zwei p-Typ-Bereichen (Kollektor und Emitter), die einen dünnen n-Typ-Basisbereich umschließen. Löcher sind die primären Ladungsträger.

Die beiden p-n-Übergänge sind:
- **Basis-Emitter-Übergang**: Zwischen Basis und Emitter.
- **Basis-Kollektor-Übergang**: Zwischen Basis und Kollektor.

Die dünne Basisregion ist entscheidend, da sie es dem BJT ermöglicht, große Ströme mit einem kleinen Basisstrom zu steuern und so eine Verstärkung zu ermöglichen.

---

### **2. Betriebsarten eines BJT**
BJTs arbeiten in drei primären Modi, die durch die Vorspannung (angelegte Spannung) der Basis-Emitter- und Basis-Kollektor-Übergänge bestimmt werden:

1.  **Aktiver Betrieb** (verwendet zur Verstärkung):
    - **Basis-Emitter-Übergang**: In Flussrichtung vorgespannt (eingeschaltet, lässt Strom fließen).
    - **Basis-Kollektor-Übergang**: In Sperrrichtung vorgespannt (blockiert Strom, ermöglicht aber einen gesteuerten Fluss von Ladungsträgern).
    - Bei NPN-BJTs injiziert ein kleiner Basisstrom (I_B) Elektronen vom Emitter in die Basis. Die meisten dieser Elektronen diffundieren durch die dünne Basis und werden in den Kollektor gezogen, wodurch ein größerer Kollektorstrom (I_C) erzeugt wird.
    - **Stromverstärkung**: Der Kollektorstrom ist proportional zum Basisstrom, mit einer Stromverstärkung (β), die typischerweise zwischen 20 und 1000 liegt. Mathematisch:  
      \\[
      I_C = \beta \cdot I_B
      \\]
    - Der Emitterstrom ist die Summe aus Basis- und Kollektorstrom:  
      \\[
      I_E = I_B + I_C
      \\]
    - Dieser Modus wird in Verstärkern verwendet, da ein kleines Eingangssignal (Basisstrom oder -spannung) ein großes Ausgangssignal (Kollektorstrom oder -spannung) steuert.

2.  **Sättigungsbetrieb** (verwendet zum Schalten, "Ein"-Zustand):
    - Sowohl Basis-Emitter- als auch Basis-Kollektor-Übergang sind in Flussrichtung vorgespannt.
    - Der Transistor verhält sich wie ein geschlossener Schalter, lässt einen maximalen Kollektorstrom fließen und weist eine minimale Kollektor-Emitter-Spannung (V_CE ≈ 0,2V) auf.
    - Wird in Digitalschaltungen verwendet, um eine logische "1" darzustellen.

3.  **Sperrbetrieb** (verwendet zum Schalten, "Aus"-Zustand):
    - Beide Übergänge sind in Sperrrichtung vorgespannt.
    - Der Transistor verhält sich wie ein offener Schalter, es fließt kein Kollektorstrom (I_C ≈ 0).
    - Wird in Digitalschaltungen verwendet, um eine logische "0" darzustellen.

Andere, weniger gebräuchliche Modi sind:
- **Inverser aktiver Betrieb**: Die Rollen von Kollektor und Emitter sind vertauscht, dies wird jedoch aufgrund schlechterer Leistung (niedrigerer β) selten verwendet.
- **Durchbruchsbetrieb**: Tritt auf, wenn die Spannungen die Nennwerte des Transistors überschreiten und ihn möglicherweise beschädigen.

---

### **3. Aktiver Betrieb: Verstärkungsmechanismus**
Im aktiven Betrieb resultiert die Fähigkeit des BJT, Strom zu verstärken, aus seiner Struktur und Vorspannung:
- **In Flussrichtung vorgespannte Basis-Emitter-Diode**: Bei einem NPN-BJT wird eine positive Spannung (V_BE ≈ 0,7V für Silizium) angelegt, die es Elektronen ermöglicht, vom Emitter in die Basis zu fließen.
- **Dünne Basis**: Die Basis ist so dünn, dass die meisten aus dem Emitter injizierten Elektronen nicht mit Löchern in der p-Typ-Basis rekombinieren. Stattdessen diffundieren sie zum in Sperrrichtung vorgespannten Basis-Kollektor-Übergang.
- **In Sperrrichtung vorgespannte Basis-Kollektor-Diode**: Das elektrische Feld an diesem Übergang zieht die Elektronen in den Kollektor und erzeugt einen großen Kollektorstrom.
- **Verstärkung**: Ein kleiner Basisstrom (I_B) steuert einen viel größeren Kollektorstrom (I_C), wobei die Beziehung durch die Stromverstärkung (β) bestimmt wird. Zum Beispiel: Wenn β = 100, kann ein Basisstrom von 1 µA einen Kollektorstrom von 100 µA erzeugen.

Diese Verstärkung macht BJTs ideal für Anwendungen wie Audioverstärker, Hochfrequenzverstärker und Operationsverstärkerschaltungen.

---

### **4. Kennlinien**
Das Verhalten eines BJT im aktiven Betrieb wird am besten durch seine **Kennlinien** verstanden, die die Beziehung zwischen Strömen und Spannungen darstellen. Es gibt zwei Haupttypen von Kennlinien:

#### **a. Eingangskennlinie**
- **Darstellung**: Basisstrom (I_B) über Basis-Emitter-Spannung (V_BE) für eine feste Kollektor-Emitter-Spannung (V_CE).
- **Verhalten**: Ähnelt der I-V-Kennlinie einer Diode in Flussrichtung, da der Basis-Emitter-Übergang ein p-n-Übergang ist.
- **Wichtige Punkte**:
  - V_BE beginnt typischerweise bei ~0,6–0,7V (für Silizium-BJTs), um einen signifikanten Basisstrom zu initiieren.
  - Kleine Änderungen in V_BE verursachen große Änderungen in I_B aufgrund der exponentiellen Beziehung.
  - Wird verwendet, um die Eingangsvorspannungsschaltung zu entwerfen.

#### **b. Ausgangskennlinienfeld**
- **Darstellung**: Kollektorstrom (I_C) über Kollektor-Emitter-Spannung (V_CE) für verschiedene Werte des Basisstroms (I_B).
- **Bereiche**:
  1.  **Aktiver Bereich**:
      - I_C ist für einen gegebenen I_B nahezu konstant, selbst wenn V_CE zunimmt.
      - I_C ≈ β · I_B, zeigt die Stromverstärkung des Transistors.
      - Die Kurven sind nahezu horizontal, was anzeigt, dass I_C unabhängig von V_CE ist (ideales Stromquellenverhalten).
  2.  **Sättigungsbereich**:
      - Bei niedrigem V_CE (z.B. < 0,2V) sinkt der Kollektorstrom und der Transistor ist vollständig "eingeschaltet".
      - Die Kurven knicken nach unten ab, wenn der Basis-Kollektor-Übergang in Flussrichtung vorgespannt wird.
  3.  **Sperrbereich**:
      - Wenn I_B = 0, ist I_C ≈ 0 und der Transistor ist "ausgeschaltet".
  4.  **Durchbruchsbereich**:
      - Bei hohem V_CE kann der Transistor in den Durchbruch gehen, wobei I_C unkontrolliert ansteigt (in Standardkennlinien nicht dargestellt).
- **Wichtige Punkte**:
  - Jede Kurve entspricht einem festen I_B (z.B. 10 µA, 20 µA, etc.).
  - Der Abstand zwischen den Kurven spiegelt die Stromverstärkung (β) wider.
  - Wird verwendet, um das Verhalten des Transistors in Verstärkern und Schaltern zu analysieren.

#### **c. Übertragungskennlinie**
- **Darstellung**: Kollektorstrom (I_C) über Basisstrom (I_B) für eine feste V_CE.
- **Verhalten**: Zeigt die lineare Beziehung I_C = β · I_B im aktiven Bereich.
- **Verwendung**: Hilft, die Stromverstärkung (β) zu bestimmen und Vorspannungsschaltungen zu entwerfen.

---

### **5. Wichtige Parameter und Gleichungen**
- **Stromverstärkung (β)**:
  \\[
  \beta = \frac{I_C}{I_B}
  \\]
  Typischerweise 20–1000, abhängig vom Transistortyp und den Betriebsbedingungen.
- **Alpha (α)**: Stromverstärkung in Basisschaltung, das Verhältnis von Kollektorstrom zu Emitterstrom:
  \\[
  \alpha = \frac{I_C}{I_E}
  \\]
  Da I_E = I_B + I_C, steht α in Beziehung zu β:
  \\[
  \alpha = \frac{\beta}{\beta + 1}
  \\]
  α liegt typischerweise bei 0,95–0,999, also nahe 1.
- **Basis-Emitter-Spannung (V_BE)**:
  - ~0,7V für Silizium-BJTs im aktiven Betrieb.
  - Folgt der Diodengleichung:  
    \\[
    I_B \propto e^{V_{BE}/V_T}
    \\]
    wobei V_T die Temperaturspannung ist (~26 mV bei Raumtemperatur).
- **Kollektor-Emitter-Spannung (V_CE)**:
  - Im aktiven Betrieb ist V_CE > V_CE(sat) (~0,2V), um die Sättigung zu vermeiden.
  - In Sättigung ist V_CE ≈ 0,2V.
- **Verlustleistung**:
  \\[
  P = V_{CE} \cdot I_C
  \\]
  Muss unter dem maximalen Nennwert des Transistors bleiben, um Beschädigungen zu vermeiden.

---

### **6. Anwendungen von BJTs**
- **Verstärker**:
  - **Emitterschaltung**: Hohe Spannungs- und Stromverstärkung, weit verbreitet in Audio- und HF-Schaltungen.
  - **Basisschaltung**: Niedrige Eingangsimpedanz, verwendet in Hochfrequenzanwendungen.
  - **Kollektorschaltung (Emitterfolger)**: Hohe Eingangsimpedanz, verwendet für Impedanzanpassung.
- **Schalter**:
  - In Digitalschaltungen arbeiten BJTs im Sättigungs- (Ein) oder Sperrbetrieb (Aus), um Logikzustände zu steuern.
- **Oszillatoren**: Werden in HF-Schaltungen verwendet, um sinusförmige Signale zu erzeugen.
- **Spannungsregler**: BJTs stabilisieren Ausgangsspannungen in Netzteilen.
- **Signalverarbeitung**: Verwendet in Mischern, Modulatoren und Demodulatoren.

---

### **7. Praktische Überlegungen**
- **Vorspannung**: Eine korrekte Gleichstromvorspannung stellt sicher, dass der BJT im gewünschten Modus arbeitet (aktiv für Verstärkung, Sättigung/Sperre für Schalten). Gängige Vorspannungsschaltungen sind die Festspannungsvorspannung, die Kollektor-Basis-Vorspannung und die Spannungsteilervorspannung.
- **Thermisches Durchgehen**: Übermäßige Temperatur kann I_C erhöhen, was zu weiterer Erwärmung und möglicher Zerstörung führt. Vorspannungsschaltungen beinhalten oft eine thermische Kompensation (z.B. Emitterwiderstände).
- **Kleinsignal-Modelle**: Für den Verstärkerentwurf werden BJTs mit Hybrid-Pi- oder T-Modellen modelliert, um das Wechselstromverhalten zu analysieren.
- **Einschränkungen**:
  - BJTs benötigen im Gegensatz zu MOSFETs einen kontinuierlichen Basisstrom, was zu Leistungsverlusten führen kann.
  - Geringere Schaltgeschwindigkeit im Vergleich zu MOSFETs in Hochfrequenzanwendungen.
  - Anfällig für Temperaturschwankungen und Rauschen.

---

### **8. Vergleich mit anderen Transistoren**
- **Vs. MOSFETs**:
  - BJTs sind stromgesteuert, während MOSFETs spannungsgesteuert sind.
  - BJTs haben einen höheren Leistungsverbrauch in der Steuerschaltung aufgrund des Basisstroms.
  - MOSFETs werden in modernen digitalen ICs aufgrund schnelleren Schaltens und geringerer Leistungsaufnahme bevorzugt.
- **Vs. JFETs**:
  - JFETs sind spannungsgesteuert und haben eine höhere Eingangsimpedanz.
  - BJTs bieten eine höhere Stromverstärkung und sind besser für Lasten mit niedriger Impedanz geeignet.

---

### **9. Kennlinien im Detail (Visualisierung der Ausgangskennlinien)**
Um die **Ausgangskennlinien** (I_C über V_CE für verschiedene I_B) weiter zu verdeutlichen:
- **X-Achse**: V_CE, von 0V bis zur maximalen Nennspannung (z.B. 40V für einen typischen BJT).
- **Y-Achse**: I_C, von 0 bis zum maximalen Kollektorstrom (z.B. 100 mA).
- **Kurven**: Jede Kurve repräsentiert einen festen I_B (z.B. 10 µA, 20 µA, 30 µA).
- **Aktiver Bereich**: Der flache Teil der Kurven, wo I_C proportional zu I_B und unabhängig von V_CE ist.
- **Sättigungsbereich**: Der steile Teil nahe V_CE = 0, wo I_C abfällt, wenn V_CE abnimmt.
- **Sperrbereich**: Die horizontale Linie bei I_C = 0, wenn I_B = 0.
- **Early-Effekt**: Im aktiven Bereich steigen die Kurven aufgrund der Basisweitenmodulation leicht an (ein Sekundäreffekt, bei dem eine Erhöhung von V_CE die effektive Basisweite verringert und I_C erhöht).

Diese Kurven sind entscheidend für:
- **Arbeitsgeraden-Analyse**: Bestimmen des Arbeitspunkts (Q-Punkt) des Transistors in einer Schaltung.
- **Verstärkerentwurf**: Sicherstellen, dass der Transistor im aktiven Bereich für lineare Verstärkung bleibt.
- **Schaltungsentwurf**: Sicherstellen, dass der Transistor vollständig in Sättigung oder Sperre geht.

---

### **10. Fortgeschrittene Themen (Optionale Vertiefung)**
- **Ebers-Moll-Modell**: Ein mathematisches Modell, das das BJT-Verhalten in allen Betriebsarten beschreibt, basierend auf gekoppelten Diodengleichungen.
- **Gummel-Poon-Modell**: Ein komplexeres Modell, das in Schaltungssimulatoren (z.B. SPICE) verwendet wird, um nicht-ideale Effekte wie den Early-Effekt, Hochstromeffekte und parasitäre Kapazitäten zu berücksichtigen.
- **Frequenzgang**: BJTs haben eine Grenzfrequenz (f_T), bei der die Stromverstärkung auf 1 absinkt, was ihre Verwendung in Hochfrequenzanwendungen einschränkt.
- **Rauschen**: BJTs erzeugen Schrot- und thermisches Rauschen, das in Anwendungen mit schwachen Signalen berücksichtigt werden muss.
- **Leistungs-BJTs**: Spezialisierte BJTs (z.B. Darlington-Transistoren) sind für Hochstromanwendungen wie Motorsteuerungen ausgelegt.

---

### **Schlussfolgerung**
Bipolartransistoren (BJTs) sind vielseitige Bauelemente mit drei Anschlüssen (Basis, Kollektor, Emitter), die sich in der Verstärkung und im Schalten auszeichnen. Im **aktiven Betrieb** verstärken sie Strom, indem sie einen kleinen Basisstrom verwenden, um einen großen Kollektorstrom zu steuern, gesteuert durch die Stromverstärkung (β). Ihre **Kennlinien** (Eingangs-, Ausgangs- und Übertragungskennlinie) bieten eine grafische Darstellung ihres Verhaltens, wobei die Ausgangskennlinien (I_C über V_CE) besonders wichtig für das Verständnis von Verstärkung und Schalten sind. Durch die Nutzung der einzigartigen Eigenschaften ihrer p-n-Übergänge und der dünnen Basis ermöglichen BJTs eine breite Palette von Anwendungen, von Verstärkern bis zur digitalen Logik. Ihre Leistung hängt jedoch von einer korrekten Vorspannung, thermischem Management und dem Verständnis ihrer Grenzen im Vergleich zu modernen Bauelementen wie MOSFETs ab.

Wenn Sie eine tiefere Untersuchung eines bestimmten Aspekts wünschen (z.B. Vorspannungsschaltungen, Kleinsignal-Modelle oder Anwendungen), oder wenn Sie möchten, dass ich ein Diagramm der Kennlinien erstelle (mit Benutzerbestätigung), lassen Sie es mich wissen!