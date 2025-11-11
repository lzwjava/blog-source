---
audio: false
generated: true
lang: de
layout: post
title: Fragen zum Transistor
translated: true
type: note
---

In einem Bipolartransistor (BJT) wird das Verhalten von Strömen und Spannungen zwischen der Basis-Emitter (BE)- und der Kollektor-Emitter (CE)-Strecke durch die Physik des Transistors und seinen operationellen Aufbau bestimmt. Lassen Sie uns Ihre Fragen systematisch aufschlüsseln:

### 1. **Warum fällt eine kleine Spannung (≈0,7 V) über dem Basis-Emitter-Übergang ab?**
Der Basis-Emitter-Übergang eines BJT verhält sich wie eine Diode. Bei einem auf Silizium basierenden BJT (der häufigste Typ) beträgt die Durchlassspannung an diesem Übergang typischerweise etwa **0,7 V**, wenn er in Durchlassrichtung gepolt ist (d. h., wenn sich der Transistor im aktiven Bereich oder im Sättigungsbereich befindet). Diese Spannung wird durch die Materialeigenschaften des Silizium-PN-Übergangs bestimmt, insbesondere durch die Energie, die benötigt wird, um die Potentialbarriere zu überwinden, damit Strom fließen kann. Bei Germanium-BJTs ist diese Spannung niedriger, etwa 0,3 V, aber Silizium ist weitaus verbreiteter.

- **Warum 0,7 V?** Dies ist die Spannung, die benötigt wird, um den BE-Übergang in Durchlassrichtung zu polen und einen kleinen Basisstrom (\\(I_B\\)) fließen zu lassen. Die exponentielle Beziehung zwischen Spannung und Strom in einer Diode bedeutet, dass eine kleine Erhöhung der Spannung über 0,7 V hinaus einen großen Anstieg des Stroms verursacht, aber 0,7 V ist der typische Arbeitspunkt für Silizium.

### 2. **Warum ist der Strom zwischen Basis und Emitter klein, während der Kollektor-Emitter-Strom viel größer ist?**
Der BJT ist dazu ausgelegt, Strom zu verstärken. Der kleine Basisstrom (\\(I_B\\)) steuert einen viel größeren Kollektorstrom (\\(I_C\\)). Dies ist auf die **Stromverstärkung** (\\(\beta\\)) des Transistors zurückzuführen, die bei den meisten BJTs typischerweise im Bereich von 20–1000 liegt.

- **Wie es funktioniert:**
  - Der Basis-Emitter-Übergang ist in Durchlassrichtung gepolt, was einen kleinen Basisstrom (\\(I_B\\)) ermöglicht.
  - Dieser kleine Strom injiziert Ladungsträger (Elektronen bei NPN, Löcher bei PNP) in das Basisgebiet.
  - Die Basis ist sehr dünn und schwach dotiert, sodass die meisten dieser Ladungsträger aufgrund des in Sperrrichtung gepolten Kollektor-Basis-Übergangs in den Kollektor gespült werden.
  - Der Kollektorstrom (\\(I_C\\)) ist ungefähr \\(\beta \cdot I_B\\), was ihn viel größer als \\(I_B\\) macht.
  - Der Emitterstrom (\\(I_E\\)) ist die Summe aus \\(I_B\\) und \\(I_C\\), also gilt \\(I_E \approx I_C\\), da \\(I_B\\) klein ist.

Diese Verstärkung ist das Kernprinzip des BJT-Betriebs im aktiven Bereich. Der kleine Basisstrom wirkt als "Steuersignal" für den viel größeren Kollektor-Emitter-Strom.

### 3. **Warum nicht umgekehrt? (Warum ist der Basis-Emitter-Strom nicht groß und der Kollektor-Emitter-Strom klein?)**
Die Struktur und Dotierung des Transistors verhindern dies:

- **Struktureller Aufbau**: Die Basis ist absichtlich dünn und schwach dotiert im Vergleich zum Emitter und Kollektor. Dies stellt sicher, dass die meisten vom Emitter in die Basis injizierten Ladungsträger vom Kollektor aufgenommen werden, anstatt in der Basis zu verbleiben oder einen großen Basisstrom zu verursachen.
- **Vorspannung**: Der Basis-Emitter-Übergang ist in Durchlassrichtung gepolt (niederohmig, kleiner Spannungsabfall), während der Kollektor-Basis-Übergang in Sperrrichtung gepolt ist (hochohmig, größerer Spannungsabfall). Diese Beschaltung stellt sicher, dass der Kollektorstrom dominiert.
- **Stromverstärkung (\\(\beta\\))**: Der Transistor ist so konstruiert, dass er eine hohe \\(\beta\\) hat, was bedeutet, dass der Kollektorstrom ein Vielfaches des Basisstroms ist. Eine Umkehrung würde den Zweck des Transistors als Verstärker oder Schalter zunichtemachen und der Aufbau wäre ineffizient.

### 4. **Könnte die Basis-Emitter-Spannung 10 V betragen?**
Im Normalbetrieb kann die Basis-Emitter-Spannung nicht so hoch wie **10 V** sein, ohne den Transistor zu beschädigen:

- **Durchbruch**: Das Anlegen einer hohen Spannung (z. B. 10 V) an den Basis-Emitter-Übergang würde wahrscheinlich die Durchbruchspannung des Übergangs überschreiten oder einen übermäßigen Strom verursachen, was zu thermischem Durchgehen oder dauerhafter Beschädigung des Transistors führt.
- **Diodenverhalten**: Der BE-Übergang verhält sich wie eine Diode, daher wird die Spannung daran im Durchlassbetrieb auf etwa 0,7 V (für Silizium) begrenzt. Eine geringfügige Erhöhung der Spannung (z. B. auf 0,8 V oder 0,9 V) verursacht aufgrund der exponentiellen Beziehung einen massiven Anstieg des Basisstroms, aber praktische Schaltkreise begrenzen dies mit Widerständen oder anderen Bauteilen.
- **Schaltungsdesign**: In realen Schaltungen wird die Basis von einer gesteuerten Spannungs- oder Stromquelle angesteuert (z. B. durch einen Widerstand oder ein Signal). Die Schaltung ist so ausgelegt, \\(V_{BE}\\) im aktiven Modus bei etwa 0,7 V zu halten. Ein 10-V-Eingang würde eine spezifische Fehlerbedingung oder einen Konstruktionsfehler voraussetzen.

### 5. **Könnten Basis und Emitter eine große Spannung wie die Kollektor-Emitter-Spannung haben?**
Die Kollektor-Emitter-Spannung (\\(V_{CE}\\)) kann viel größer sein (z. B. 10 V oder mehr, abhängig von der Nennleistung des Transistors), weil der Kollektor-Basis-Übergang in Sperrrichtung gepolt ist und der Kollektor für höhere Spannungen ausgelegt ist. Der Basis-Emitter-Übergang ist jedoch in Durchlassrichtung gepolt und arbeitet aufgrund seines diodenähnlichen Verhaltens bei einer niedrigen Spannung (≈0,7 V).

- **Warum kein großes \\(V_{BE}\\)?** Der BE-Übergang ist nicht für das Aushalten großer Spannungen ausgelegt. Die meisten BJTs haben eine maximale Sperr-\\(V_{BE}\\)-Spannung von 5–7 V, und das Überschreiten dieses Werts kann zum Durchbruch oder zur Beschädigung führen. Durchlassspannungen deutlich über 0,7 V führen zu übermäßigem Strom, nicht zu einem stabilen Hochspannungszustand.
- **Rolle der Kollektor-Emitter-Strecke**: Der Kollektor-Emitter-Pfad ist dafür ausgelegt, den Hauptleistungs- oder Signalstrom zu führen, daher ist er für größere Spannungen und Ströme konzipiert, begrenzt durch die maximalen Nennwerte des Transistors (z. B. \\(V_{CE(max)}\\), oft 30–100 V oder mehr).

### Zusammenfassung
- Die **0,7 V** am Basis-Emitter-Übergang ergeben sich aus dem diodenähnlichen Verhalten des Silizium-Übergangs, der benötigt wird, um ihn in Durchlassrichtung zu polen.
- Der **kleine Basisstrom** steuert einen **großen Kollektorstrom** aufgrund der Stromverstärkung (\\(\beta\\)) des Transistors und seines strukturellen Aufbaus (dünne Basis, Dotierungsunterschiede).
- Die Ströme können nicht umgekehrt werden (große Basis, kleiner Kollektor), aufgrund des zielgerichteten Transistordesigns für die Verstärkung.
- Die Basis-Emitter-Spannung kann im Normalbetrieb nicht 10 V betragen, da dies den Transistor beschädigen oder eine Fehlerbedingung erfordern würde. Der Kollektor-Emitter-Pfad ist für größere Spannungen ausgelegt, nicht der Basis-Emitter-Pfad.

Wenn Sie einen tieferen Einblick in die Transistorphysik, Schaltungsbeispiele oder spezielle BJT-Typen wünschen, lassen Sie es mich wissen!