---
audio: false
generated: true
lang: de
layout: post
title: Selbstlernquiz Elektronische Technologie
translated: true
type: note
---

Unten finden Sie einen Beispieltest, der für eine Selbststudienprüfung basierend auf dem bereitgestellten Lehrplan für *Grundlagen der Elektronik (III)*, herausgegeben von Wen Xidong und veröffentlicht vom Economic Science Press, erstellt wurde. Der Test behandelt Schlüsselkonzepte aus der analogen Elektronik, digitalen Elektronik und praktischen Anwendungen. Er ist darauf ausgelegt, das grundlegende Verständnis zu prüfen, wie es für eine Selbststudienprüfung in China typisch ist. Die Fragen sind eine Mischung aus Multiple-Choice, Kurzantwort- und Problemaufgaben, um typische Prüfungsstile widerzuspiegeln.

---

### Beispieltest: Grundlagen der Elektronik (III)
**Selbststudienprüfung**
**Anweisungen**: Beantworten Sie alle Fragen. Zeigen Sie Ihren Lösungsweg bei den Problemaufgaben. Jede Frage ist mit den angegebenen Punkten bewertet. Gesamt: 100 Punkte.

---

#### Teil I: Analoge Elektronik (40 Punkte)

1. **Multiple Choice: Schaltungsanalyse (5 Punkte)**
   Welche der folgenden Aussagen beschreibt korrekt die Kirchhoff'sche Maschenregel (KVL)?
   a) Die Summe der in einen Knoten eintretenden Ströme ist gleich der Summe der ihn verlassenden Ströme.
   b) Die Summe der Spannungsabfälle in einer geschlossenen Masche ist gleich null.
   c) Der Gesamtwiderstand in einer Reihenschaltung ist die Summe der Einzelwiderstände.
   d) Die Spannung über parallelen Zweigen ist unterschiedlich.
   **Antwort**: b) Die Summe der Spannungsabfälle in einer geschlossenen Masche ist gleich null.

2. **Kurzantwort: Verstärkerschaltungen (10 Punkte)**
   Erklären Sie kurz den Unterschied zwischen der Emitterschaltung (CE) und der Kollektorschaltung (CC) eines BJT-Verstärkers hinsichtlich ihrer Ein-/Ausgangscharakteristiken und typischen Anwendungen.
   **Musterantwort**:
   - **Emitterschaltung (CE)**: Hohe Spannungsverstärkung, mittlere Eingangsimpedanz und invertierte Ausgangsspannung. Wird in Anwendungen verwendet, die Verstärkung erfordern, wie z.B. Audioverstärker.
   - **Kollektorschaltung (CC)**: Spannungsverstärkung von 1, hohe Eingangsimpedanz, niedrige Ausgangsimpedanz, nicht invertierte Ausgangsspannung. Wird oft als Puffer oder zur Impedanzanpassung verwendet.

3. **Problemaufgabe: Operationsverstärker (15 Punkte)**
   Ein invertierender Operationsverstärker hat einen Rückkopplungswiderstand \\( R_f = 10 \, \text{k}\Omega \\) und einen Eingangswiderstand \\( R_{\text{in}} = 2 \, \text{k}\Omega \\). Die Eingangsspannung beträgt \\( V_{\text{in}} = 1 \, \text{V} \\).
   a) Berechnen Sie die Ausgangsspannung \\( V_{\text{out}} \\).
   b) Wie groß ist die Verstärkung der Schaltung?
   **Lösung**:
   a) Für einen invertierenden Operationsverstärker gilt: \\( V_{\text{out}} = -\left(\frac{R_f}{R_{\text{in}}}\right) V_{\text{in}} = -\left(\frac{10 \, \text{k}\Omega}{2 \, \text{k}\Omega}\right) \cdot 1 \, \text{V} = -5 \, \text{V} \\).
   b) Verstärkung \\( A = -\frac{R_f}{R_{\text{in}}} = -\frac{10}{2} = -5 \\).

4. **Multiple Choice: Gleichstromnetzteile (10 Punkte)**
   Was ist ein Hauptvorteil eines Schaltnetzteils gegenüber eines Linearreglers?
   a) Geringere Kosten
   b) Höherer Wirkungsgrad
   c) Einfacherer Aufbau
   d) Bessere Spannungsregelung
   **Antwort**: b) Höherer Wirkungsgrad

---

#### Teil II: Digitale Elektronik (40 Punkte)

5. **Multiple Choice: Logikgatter (5 Punkte)**
   Welches Logikgatter erzeugt nur dann eine 1 am Ausgang, wenn alle Eingänge 0 sind?
   a) AND
   b) OR
   c) NOR
   d) XOR
   **Antwort**: c) NOR

6. **Kurzantwort: Kombinatorische Logik (10 Punkte)**
   Beschreiben Sie die Funktion eines Multiplexers und nennen Sie eine praktische Anwendung.
   **Musterantwort**: Ein Multiplexer wählt eines von mehreren Eingangssignalen aus und leitet es basierend auf den Steuerleitungen zu einem einzigen Ausgang weiter. Er fungiert als Datenauswähler. **Anwendung**: Wird in Kommunikationssystemen verwendet, um mehrere Datenströme auf einen einzigen Kanal zu leiten.

7. **Problemaufgabe: Sequentielle Logik (15 Punkte)**
   Entwerfen Sie einen 3-Bit-Binärzähler (Aufwärtszähler) mit JK-Flip-Flops. Geben Sie die Zustandstabelle an und beschreiben Sie den Betrieb für einen Taktzyklus, beginnend mit dem Zustand 010 (binär 2).
   **Lösung**:
   - **Zustandstabelle**:
     | Aktueller Zustand (Q2 Q1 Q0) | Nächster Zustand (Q2 Q1 Q0) | JK-Eingänge (J2 K2 | J1 K1 | J0 K0) |
     |-------------------------|-----------------------|-----------------------|
     | 010                     | 011                   | 0 0 | 0 0 | 1 1 |
   - **Betrieb**: Vom Zustand 010 aus wechselt Q0 im nächsten Taktzyklus (0 → 1), Q1 und Q2 bleiben unverändert, was zu 011 (binär 3) führt. J0 = K0 = 1, um Q0 zu toggle; andere sind Don't-Care oder 0.

8. **Multiple Choice: Programmierbare Logikbausteine (10 Punkte)**
   Welche der folgenden Eigenschaften charakterisiert einen FPGA?
   a) Feste Logikstruktur
   b) Neuprogrammierbare Logikblöcke und Verbindungen
   c) Unterstützt nur analoge Schaltungen
   d) Kann nicht mit HDL programmiert werden
   **Antwort**: b) Neuprogrammierbare Logikblöcke und Verbindungen

---

#### Teil III: Praktische Anwendungen (20 Punkte)

9. **Kurzantwort: Simulationswerkzeuge (10 Punkte)**
   Erklären Sie die Rolle von Simulationswerkzeugen wie Multisim beim Entwurf elektronischer Schaltungen. Warum sind sie für Studierende nützlich, die *Grundlagen der Elektronik* lernen?
   **Musterantwort**: Multisim ermöglicht es Studierenden, Schaltungen virtuell zu entwerfen, zu simulieren und zu testen, bevor sie aufgebaut werden, was Fehler und Kosten reduziert. Es hilft, das Schaltungsverhalten (z.B. Spannung, Strom) zu visualisieren und mit Parametern zu experimentieren, was das Verständnis von Konzepten wie Verstärkern und Logikschaltungen vertieft.

10. **Problemaufgabe: Mixed-Signal-Systeme (10 Punkte)**
     Ein Temperaturüberwachungssystem verwendet einen analogen Sensor mit einem Ausgang von 0–5 V und eine digitale Anzeige über einen 3-Bit-ADC. Wenn die Referenzspannung des ADC 5 V beträgt, berechnen Sie die Spannungsstufengröße und die digitale Ausgabe für einen Sensorwert von 3,75 V.
     **Lösung**:
     - Stufengröße = \\( \frac{V_{\text{ref}}}{2^n} = \frac{5 \, \text{V}}{2^3} = 0,625 \, \text{V} \\).
     - Digitale Ausgabe = \\( \text{floor}\left(\frac{3,75}{0,625}\right) = \text{floor}(6) = 110 \\) (binär).

---

### Hinweise zur Vorbereitung auf die Selbststudienprüfung in China
- **Struktur**: Der Test ist auf das Format der Selbststudienprüfung in China abgestimmt, das oft theoretisches Verständnis, Problemlösungsfähigkeiten und praktische Anwendungen betont. Die Fragen sind ausgewogen, um Gedächtnis, Analyse und Entwurfsfähigkeiten zu testen.
- **Lerntipps**:
  - Konzentrieren Sie sich darauf, grundlegende Gesetze (z.B. Ohm'sches Gesetz, Kirchhoff'sche Gesetze) und ihre Anwendungen zu beherrschen.
  - Üben Sie den Entwurf grundlegender Schaltungen (z.B. Verstärker, Zähler) mit Standardkomponenten.
  - Verwenden Sie Simulationswerkzeuge wie Multisim oder Proteus, um Entwürfe zu überprüfen.
  - Wiederholen Sie gründlich die Eigenschaften von Halbleitern und den Betrieb von Logikgattern.
- **Ressourcen**: Das Lehrbuch *Grundlagen der Elektronik (III)* von Wen Xidong (Economic Science Press) ist die primäre Ressource. Ergänzen Sie dies mit Online-Tutorials oder Plattformen wie Coursera für Schaltungssimulationen und HDL-Grundlagen.
- **Prüfungskontext**: Selbststudienprüfungen in China, wie z.B. diejenigen, die von der National Education Examinations Authority (NEEA) durchgeführt werden, erfordern eine disziplinierte Vorbereitung. Altfragen (falls verfügbar) und Kapitelübungen aus dem Lehrbuch sind entscheidend für den Erfolg.

Wenn Sie zusätzliche Fragen, Betonung bestimmter Themen oder einen Fokus auf laborbezogene Fragen wünschen, lassen Sie es mich wissen! Ich kann auch einen detaillierteren Lösungsschlüssel bereitstellen oder den Test auf ein bestimmtes Prüfungsformat zuschneiden.