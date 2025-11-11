---
audio: false
generated: true
lang: de
layout: post
title: Grundlagen der physikalischen Schicht
translated: true
type: note
---

Hier ist ein detailliertes Tutorial, das Ihnen hilft, das Kapitel "Physical Layer" (Bitübertragungsschicht) eines Computer Networks Technology-Kurses (wahrscheinlich Teil des chinesischen Hochschul-Fernstudiensystems) zu lernen. Dieses Tutorial ist so strukturiert, dass es Sie durch die Schlüsselkonzepte – Übertragungsmedien, Signalcodierungstechniken, Grundlagen der Datenübertragung und Hardwarekomponenten – führt und dabei Erklärungen, Beispiele und Lerntipps bietet. Fangen wir an!

---

### **Tutorial: Die Bitübertragungsschicht verstehen**

Die Bitübertragungsschicht ist die Grundlage von Computernetzwerken. Sie befasst sich mit der physischen Verbindung zwischen Geräten und der Übertragung von Rohdaten (Bits) über ein Kommunikationsmedium. Dieses Tutorial unterteilt jedes Thema in überschaubare Abschnitte, erklärt technische Konzepte in einfachen Worten und bietet einen schrittweisen Lernpfad.

---

### **1. Übertragungsmedien**
Das Übertragungsmedium ist der physische Pfad, der Datensignale zwischen Geräten trägt. Es wird in **kabelgebundene** (geleitete) und **drahtlose** (ungeleitete) Medien unterteilt.

#### **Kabelgebundene Übertragungsmedien**
- **Twisted Pair (verdrilltes Paar)**
  - **Beschreibung**: Zwei isolierte Kupferdrähte, die miteinander verdrillt sind, um Interferenzen (elektromagnetisches Rauschen) zu reduzieren.
  - **Typen**:
    - Unshielded Twisted Pair (UTP): Üblich in Ethernet-Kabeln (z.B. Cat5e, Cat6).
    - Shielded Twisted Pair (STP): Zusätzliche Abschirmung für verrauschte Umgebungen.
  - **Vorteile**: Günstig, einfach zu installieren.
  - **Nachteile**: Begrenzte Entfernung (100 Meter für Ethernet), anfällig für Interferenzen.
  - **Beispiel**: Heim-Internetkabel.

- **Koaxialkabel**
  - **Beschreibung**: Ein zentraler Leiter, umgeben von einer Abschirmung, wird für höhere Bandbreite als Twisted Pair verwendet.
  - **Typen**: Dickes Koax (älter) und dünnes Koax.
  - **Vorteile**: Bessere Störfestigkeit, unterstützt längere Distanzen.
  - **Nachteile**: Sperriger und teurer als Twisted Pair.
  - **Beispiel**: Kabelfernsehen oder ältere LANs.

- **Lichtwellenleiter (Glasfaserkabel)**
  - **Beschreibung**: Verwendet Licht (optische Signale) zur Datenübertragung durch dünne Glas- oder Kunststofffasern.
  - **Typen**:
    - Singlemode: Lange Distanzen, ein Lichtpfad.
    - Multimode: Kürzere Distanzen, mehrere Lichtpfade.
  - **Vorteile**: Hohe Bandbreite, lange Distanzen (Kilometer), immun gegen elektromagnetische Interferenzen.
  - **Nachteile**: Teuer, schwieriger zu installieren.
  - **Beispiel**: Internet-Backbones, Hochgeschwindigkeitsnetzwerke.

#### **Drahtlose Übertragungsmedien**
- **Radiowellen**
  - **Beschreibung**: Elektromagnetische Wellen (3 kHz bis 3 GHz), die sich durch die Luft ausbreiten.
  - **Vorteile**: Große Reichweite, keine physischen Kabel.
  - **Nachteile**: Anfällig für Interferenzen (z.B. Wände, Wetter).
  - **Beispiel**: Wi-Fi, Bluetooth.

- **Mikrowellen**
  - **Beschreibung**: Hochfrequente Radiowellen (3 GHz bis 30 GHz), die Sichtverbindung zwischen Sender und Empfänger erfordern.
  - **Vorteile**: Hohe Bandbreite, Langstreckenübertragung.
  - **Nachteile**: Benötigt direkte Ausrichtung, wird durch Wetter beeinflusst.
  - **Beispiel**: Satellitenkommunikation, Mobilfunkmasten.

#### **Lerntipps**
- **Visualisieren**: Zeichnen Sie Diagramme von Twisted-Pair-, Koaxial- und Glasfaserkabeln, um deren Aufbau zu sehen.
- **Vergleichen**: Erstellen Sie eine Tabelle, die kabelgebundene vs. drahtlose Medien vergleicht (Kosten, Geschwindigkeit, Entfernung, Interferenzen).
- **Realweltbezug**: Identifizieren Sie Beispiele in Ihrem Zuhause (z.B. Wi-Fi für Radiowellen, Ethernet für Twisted Pair).

---

### **2. Signalcodierungstechniken**
Die Signalcodierung wandelt Daten (Bits: 0en und 1en) in Signale für die Übertragung um. Sie wird in **analog** (kontinuierliche Wellen) und **digital** (diskrete Pegel) unterteilt.

#### **Analoge vs. digitale Signale**
- **Analog**: Kontinuierliche Wellenform (z.B. Schallwellen).
- **Digital**: Diskrete Werte (z.B. 0V für 0, 5V für 1).
- **Warum codieren?**: Um an das Medium anzupassen und einen genauen Datentransfer zu gewährleisten.

#### **Häufige Codierungstechniken**
- **Digital zu Digital (z.B. für kabelgebundene Medien)**
  - **NRZ (Non-Return-to-Zero)**: 0 = Niedrigspannung, 1 = Hochspannung. Einfach, aber anfällig für Synchronisationsprobleme.
  - **Manchester**: Bit wird durch einen Übergang dargestellt (z.B. niedrig-zu-hoch = 1, hoch-zu-niedrig = 0). Wird in Ethernet verwendet.
  - **Vor-/Nachteile**: Manchester verhindert Synchronisationsverlust, verbraucht aber mehr Bandbreite.

- **Digital zu Analog (z.B. für Modems)**
  - **ASK (Amplitude Shift Keying)**: Amplitude variieren, Frequenz konstant halten.
  - **FSK (Frequency Shift Keying)**: Frequenz variieren (z.B. niedrige Frequenz = 0, hohe Frequenz = 1).
  - **PSK (Phase Shift Keying)**: Phase der Welle variieren.
  - **Beispiel**: Modems, die digitale Daten in Telefonleitungssignale umwandeln.

- **Analog zu Digital (z.B. für Voice over IP)**
  - **PCM (Pulse Code Modulation)**: Analoges Signal abtasten, in digitale Werte quantisieren.
  - **Beispiel**: Digitalisierung von Audio für Telefonanrufe.

#### **Lerntipps**
- **Diagramme**: Skizzieren Sie Wellenformen für NRZ, Manchester, ASK, FSK und PSK, um die Unterschiede zu sehen.
- **Üben**: Codieren Sie eine Binärzeichenkette (z.B. 1010) mit Manchester und NRZ.
- **Zweck verstehen**: Fragen Sie: Warum verhindert Manchester Synchronisationsprobleme? (Hinweis: Übergänge liefern einen Takt.)

---

### **3. Grundlagen der Datenübertragung**
Dieser Abschnitt behandelt, wie Daten effizient und zuverlässig über die Bitübertragungsschicht bewegt werden.

#### **Schlüsselkonzepte**
- **Bandbreite**
  - **Definition**: Der Frequenzbereich, den ein Medium übertragen kann (gemessen in Hz).
  - **Auswirkung**: Höhere Bandbreite = mehr Daten (Bits pro Sekunde).
  - **Beispiel**: Glasfaser hat eine riesige Bandbreite im Vergleich zu Twisted Pair.

- **Durchsatz**
  - **Definition**: Die tatsächlich erreichte Datenrate (Bits pro Sekunde, bps).
  - **Unterschied**: Bandbreite ist das Potenzial; Durchsatz ist die Realität (beeinflusst durch Rauschen, Fehler).
  - **Beispiel**: 100 Mbps Bandbreite, aber nur 80 Mbps Durchsatz aufgrund von Interferenzen.

- **Rauschen**
  - **Definition**: Unerwünschte Signale, die Daten verzerren.
  - **Typen**:
    - Thermisches Rauschen (zufällige Elektronenbewegung).
    - Übersprechen (Interferenz von benachbarten Drähten).
    - Extern (z.B. Blitzschlag).
  - **Auswirkung**: Verursacht Bitlehler (z.B. 0 wird als 1 gelesen).
  - **Lösung**: Abschirmung (STP), Fehlererkennung (höhere Schichten).

#### **Lerntipps**
- **Formeln**: Lernen Sie die Shannon-Kapazität:
  \\( C = B \log_2(1 + S/N) \\)
  Wobei \\( C \\) = Kapazität (bps), \\( B \\) = Bandbreite (Hz), \\( S/N \\) = Signal-zu-Rausch-Verhältnis.
- **Szenario**: Wenn Bandbreite = 1 MHz und S/N = 31, berechnen Sie die maximale Kapazität. (Antwort: ~5 Mbps).
- **Bezug herstellen**: Warum wird Wi-Fi in der Nähe einer Mikrowelle langsamer? (Rauschinterferenz.)

---

### **4. Hardwarekomponenten**
Dies sind die physischen Geräte, die die Datenübertragung auf der Bitübertragungsschicht unterstützen.

#### **Wichtige Geräte**
- **Hubs**
  - **Funktion**: Verbindet mehrere Geräte in einem Netzwerk und sendet Daten an alle Ports.
  - **Vorteile**: Einfach, günstig.
  - **Nachteile**: Keine Intelligenz – verursacht Kollisionen in stark ausgelasteten Netzwerken.
  - **Beispiel**: Alte Ethernet-Netzwerke.

- **Repeater**
  - **Funktion**: Verstärkt oder regeneriert Signale, um die Reichweite zu erweitern.
  - **Vorteile**: Überwindet Signalverlust (Dämpfung).
  - **Nachteile**: Filtert oder verwaltet den Datenverkehr nicht.
  - **Beispiel**: Lange Glasfaserverbindungen.

- **Kabel**
  - **Typen**: Twisted Pair (UTP/STP), Koaxial, Glasfaser (bereits behandelt).
  - **Rolle**: Physisches Medium für die Signalübertragung.

#### **Lerntipps**
- **Vergleichen**: Hubs vs. Repeater (Hubs verbinden Geräte, Repeater erweitern Signale).
- **Diagramm**: Zeichnen Sie ein Netzwerk mit einem Hub, der PCs verbindet, und einem Repeater, der ein Kabel erweitert.
- **Realweltbezug**: Überprüfen Sie Ihren Router – moderne Geräte ersetzen Hubs durch Switches (Layer 2).

---

### **Lernplan**
1. **Tag 1: Übertragungsmedien**
   - Notizen lesen, Diagramme zeichnen, kabelgebunden vs. drahtlos vergleichen.
   - Quiz: Nennen Sie 2 Vor- und Nachteile von Glasfaser.

2. **Tag 2: Signalcodierung**
   - Codierungstypen studieren, Wellenformen skizzieren.
   - Übung: Codieren Sie "1100" in NRZ und Manchester.

3. **Tag 3: Grundlagen der Datenübertragung**
   - Definitionen von Bandbreite, Durchsatz und Rauschen lernen.
   - Rechenaufgabe: Berechnen Sie die Kapazität mit gegebener Bandbreite und S/N.

4. **Tag 4: Hardwarekomponenten**
   - Hubs, Repeater, Kabel verstehen.
   - Zeichnen: Ein Netzwerk mit diesen Geräten.

5. **Tag 5: Wiederholung & Test**
   - Alle Themen rekapitulieren, Schwachstellen wiederholen.
   - Selbsttest: Erklären Sie, wie Wi-Fi auf der Bitübertragungsschicht funktioniert.

---

### **Zusätzliche Ressourcen**
- **Bücher**: "Computer Networks" von Andrew Tanenbaum (einfache Erklärungen).
- **Online**: Khan Academy oder YouTube für visuelle Tutorials zu Codierungs-/Signalkonzepten.
- **Praxis**: Verwenden Sie Simulatoren wie Packet Tracer, um Bitübertragungsschicht-Aufbauten zu sehen.

---

Dieses Tutorial gibt Ihnen eine solide Grundlage für das Kapitel zur Bitübertragungsschicht. Konzentrieren Sie sich darauf, Konzepte zu verstehen (nicht nur auswendig zu lernen), und beziehen Sie sie auf reale Beispiele. Viel Glück bei Ihrer Prüfung im Selbststudium! Lassen Sie es mich wissen, wenn Sie Klärung zu einem Thema benötigen.