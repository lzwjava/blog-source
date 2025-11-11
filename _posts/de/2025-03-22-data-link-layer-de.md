---
audio: false
generated: true
lang: de
layout: post
title: Sicherungsschicht
translated: true
type: note
---

Hier ist ein detailliertes Tutorial, das dir hilft, das Kapitel **Data Link Layer** im Kurs **Computer Networks Technology** (02141 im chinesischen Selbststudium-Prüfungssystem) zu lernen.

---

## **1. Überblick über die Data Link Layer**
Die Data Link Layer ist die **zweite Schicht** im **OSI-Modell** und dafür verantwortlich, eine **zuverlässige Datenübertragung** zwischen direkt verbundenen Knoten bereitzustellen. Sie stellt sicher, dass Frames (Datenpakete auf dieser Schicht) korrekt formatiert, übertragen und empfangen werden.

### **Wichtige Aufgaben:**
- **Framing** – Kapselt Daten in Frames für die Übertragung ein.
- **Fehlererkennung & -korrektur** – Erkennt und korrigiert Übertragungsfehler.
- **Flusskontrolle** – Stellt sicher, dass der Sender den Empfänger nicht überlastet.
- **Medium Access Control (MAC)** – Legt fest, wie mehrere Geräte das Übertragungsmedium teilen.
- **Switching-Techniken** – Verwaltet, wie Daten sich durch Netzwerke bewegen.

---

## **2. Framing**
Framing beinhaltet das Unterteilen eines kontinuierlichen Datenstroms in kleinere Einheiten, genannt **Frames**, die Synchronisationsinformationen enthalten.

### **Arten von Framing-Methoden:**
1. **Character Count Method** – Das erste Feld im Frame gibt die Anzahl der Zeichen an.
2. **Flag-basiertes Framing (Bit Stuffing)** – Verwendet spezielle Flag-Bits (z.B. `01111110` in HDLC), um Anfang und Ende zu markieren.
3. **Zeichenbasiertes Framing (Byte Stuffing)** – Verwendet Escape-Sequenzen, um Steuerzeichen von Daten zu unterscheiden.

---

## **3. Fehlererkennung und -korrektur**
Die Fehlerbehandlung stellt sicher, dass die Datenübertragung genau ist.

### **Fehlererkennungstechniken:**
- **Parity Bits** – Eine einfache Methode, die ein zusätzliches Bit zur Fehlererkennung hinzufügt.
- **Cyclic Redundancy Check (CRC)** – Verwendet Polynomdivision, um Fehler zu erkennen.
- **Checksum** – Ein mathematischer Wert, der aus den Daten berechnet wird, um die Genauigkeit zu überprüfen.

### **Fehlerkorrekturtechniken:**
- **Forward Error Correction (FEC)** – Verwendet redundante Daten, um Fehler ohne erneute Übertragung zu korrigieren.
- **Automatic Repeat reQuest (ARQ)** – Verwendet Bestätigungen und erneute Übertragungen.
  - **Stop-and-Wait ARQ** – Wartet auf eine Bestätigung, bevor der nächste Frame gesendet wird.
  - **Go-Back-N ARQ** – Sendet mehrere Frames, überträgt aber ab dem ersten Fehler erneut.
  - **Selective Repeat ARQ** – Überträgt nur fehlerhafte Frames erneut.

---

## **4. Flusskontrolle**
Die Flusskontrolle verhindert, dass der Sender den Empfänger überlastet.

### **Methoden der Flusskontrolle:**
- **Stop-and-Wait** – Der Sender wartet auf eine Bestätigung, bevor er den nächsten Frame sendet.
- **Sliding Window Protocol** – Der Sender kann mehrere Frames senden, bevor er eine Bestätigung benötigt.

---

## **5. Data Link Layer Protokolle**

### **5.1 Ethernet (IEEE 802.3)**
**Ethernet** ist eine weit verbreitete LAN-Technologie, die auf dem **IEEE 802.3-Standard** basiert.

#### **Ethernet-Frame-Struktur:**

| Feld | Beschreibung |
|--------|------------|
| Preamble | Synchronisation |
| Destination Address | MAC-Adresse des Empfängers |
| Source Address | MAC-Adresse des Senders |
| Type/Length | Identifiziert den Protokolltyp (IPv4, IPv6, etc.) |
| Data | Tatsächliche Nutzlast |
| CRC | Fehlerprüfwert |

#### **Ethernet-Übertragungsmodi:**
- **Halbduplex** – Geräte senden abwechselnd Daten.
- **Vollduplex** – Geräte können gleichzeitig senden und empfangen.

---

### **5.2 Point-to-Point Protocol (PPP)**
PPP wird in **Einwahl- und Breitbandverbindungen** verwendet.

#### **PPP-Merkmale:**
- **Unterstützt Authentifizierung** (z.B. PAP, CHAP).
- **Multiprotokoll-Unterstützung** (z.B. IPv4, IPv6).
- **Fehlererkennung** via CRC.

#### **PPP-Frame-Struktur:**

| Feld | Beschreibung |
|--------|------------|
| Flag | Markiert Anfang und Ende des Frames |
| Address | Normalerweise `0xFF` (Broadcast) |
| Control | Normalerweise `0x03` (Unnumbered Information) |
| Protocol | Zeigt das verwendete Protokoll an (IPv4, IPv6, etc.) |
| Data | Tatsächliche Daten-Nutzlast |
| CRC | Fehlerprüfung |

---

## **6. Medium Access Control (MAC) Methoden**

### **6.1 Carrier Sense Multiple Access with Collision Detection (CSMA/CD)**
- Wird in **kabelgebundenen Ethernet-Netzwerken** verwendet.
- Geräte prüfen, ob das Medium frei ist, bevor sie senden.
- **Tritt eine Kollision auf**, stoppen die Geräte die Übertragung und versuchen es nach einer zufälligen Verzögerung erneut.

### **6.2 Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA)**
- Wird in **drahtlosen Netzwerken (Wi-Fi)** verwendet.
- Geräte versuchen, Kollisionen zu vermeiden, indem sie vor dem Senden von Daten warten.
- Verwendet **Request-to-Send (RTS) und Clear-to-Send (CTS)** Mechanismen.

---

## **7. Switching-Techniken**
Switching bestimmt, wie Daten in einem Netzwerk weitergeleitet werden.

### **7.1 Circuit Switching**
- Ein **dedizierter** Kommunikationspfad wird aufgebaut (z.B. Telefonnetze).
- **Vorteile**: Zuverlässige, kontinuierliche Datenübertragung.
- **Nachteile**: Ineffizient für intermittierenden Datentransfer.

### **7.2 Packet Switching**
- Daten werden **in Pakete unterteilt** und unabhängig voneinander gesendet.
- Wird in **IP-Netzwerken** verwendet (z.B. das Internet).
- **Vorteile**: Effizient, unterstützt mehrere Benutzer.
- **Nachteile**: Pakete können in falscher Reihenfolge ankommen.

### **7.3 Message Switching**
- Ganze Nachrichten werden gespeichert und weitergeleitet.
- **Vorteil**: Keine dedizierte Verbindung erforderlich.
- **Nachteil**: Langsamer als Packet Switching.

---

## **8. Einführung in LAN-Technologien**
LAN (Local Area Network) Technologien definieren, wie Geräte in einem lokalen Netzwerk kommunizieren.

### **Arten von LAN-Technologien:**
1. **Ethernet (IEEE 802.3)** – Verwendet CSMA/CD, unterstützt Geschwindigkeiten von 10 Mbps bis 100 Gbps.
2. **Wi-Fi (IEEE 802.11)** – Verwendet CSMA/CA, drahtlose Übertragung.
3. **Token Ring (IEEE 802.5)** – Verwendet eine Token-Passing-Methode zur Zugriffskontrolle.
4. **FDDI (Fiber Distributed Data Interface)** – Verwendet Glasfaserkabel für Hochgeschwindigkeits-Netzwerke.

---

## **9. Zusammenfassung**
- Die **Data Link Layer** stellt eine **zuverlässige Übertragung** zwischen direkt verbundenen Geräten sicher.
- **Framing** organisiert Daten in handhabbare Einheiten.
- **Fehlererkennung und -korrektur** erhalten die Datenintegrität.
- **Flusskontrolle** verhindert Datenüberlastung.
- **Ethernet und PPP** sind wichtige Data Link Layer Protokolle.
- **CSMA/CD und CSMA/CA** behandeln den Medienzugriff.
- **Switching-Techniken** bestimmen die Datenweiterleitungsmethoden.
- **LAN-Technologien** umfassen Ethernet, Wi-Fi, Token Ring und FDDI.

---

## **10. Übungsfragen**
1. Was ist die Hauptfunktion der Data Link Layer im OSI-Modell?
2. Vergleiche CSMA/CD und CSMA/CA.
3. Erkläre den Unterschied zwischen Circuit Switching und Packet Switching.
4. Was sind die Hauptunterschiede zwischen Ethernet und PPP?
5. Wie funktioniert die Fehlererkennung mit CRC?

---

Dieses Tutorial bietet eine solide Grundlage, um die **Data Link Layer** in deinem Kurs **Computer Networks Technology (02141)** zu meistern. Wenn du weitere Erklärungen, Übungsaufgaben oder Beispiele aus der Praxis benötigst, zögere nicht zu fragen! 🚀