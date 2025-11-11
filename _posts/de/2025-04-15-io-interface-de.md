---
audio: false
generated: true
lang: de
layout: post
title: Eingabe- und Ausgabetechnologie
translated: true
type: note
---

Perfekt! Hier ist ein **umfassendes Tutorial** für **Teil 4: E/A- und Schnittstellentechnologie**, basierend auf Ihrem Kursplan. Dieses Tutorial ist so strukturiert, dass es Konzepte klar erklärt, praktische Beispiele liefert und zeigt, wie Komponenten wie 8255A, 8253/8254 und 8251A in einem Mikrocomputersystem zusammenarbeiten.

---

## 📘 Teil 4: E/A- und Schnittstellentechnologie

---

### **1. Grundlagen der E/A-Schnittstellen**

#### ✅ Port-Adressierung

E/A-Schnittstellen ermöglichen es einem Mikroprozessor, mit externen Geräten zu kommunizieren. Es gibt **zwei Hauptadressierungsverfahren**:

- **Speicherbezogene E/A (Memory-Mapped I/O)**:
  - E/A-Geräte werden wie Speicherstellen behandelt.
  - Verwendet die gleichen Befehle wie der Speicherzugriff (z.B. `MOV`).
  - Vorteile: Größerer Adressraum, kann alle CPU-Befehle nutzen.
  - Nachteile: Belegt Speicheradressraum.

- **Isolierte E/A (Port-Mapped I/O)**:
  - Spezielle Befehle wie `IN` und `OUT`.
  - Eingeschränkter Adressraum (normalerweise 256 Ports).
  - Separater Adressraum vom Speicher.

| Typ                  | Verwendeter Befehlssatz | Adressraum        |
|----------------------|-------------------------|-------------------|
| Speicherbezogen      | `MOV`, etc.             | Teil des Speichers|
| Isoliert (E/A-gemappt)| `IN`, `OUT`             | Separater E/A-Bereich|

---

#### ✅ Datenübertragungsmodi

1. **Programmgesteuerte E/A**:
   - Die CPU prüft den Gerätestatus und liest/schreibt Daten direkt.
   - Einfach, aber ineffizient (Busy Waiting).

2. **Interrupt-gesteuerte E/A**:
   - Das Gerät benachrichtigt die CPU, wenn es bereit ist, über einen **Interrupt**.
   - Die CPU führt eine Interrupt-Service-Routine (ISR) aus.
   - Verbessert die Effizienz.

3. **DMA (Direct Memory Access)**:
   - Das Gerät überträgt Daten direkt in den/vom Speicher.
   - Umgeht die CPU für große/schnelle Datenübertragungen.
   - Wird für Hochgeschwindigkeitsgeräte wie Festplatten verwendet.

---

### **2. Interrupt-Systeme**

#### ✅ Interrupt-Vektortabelle

- Speichert Adressen von **Interrupt-Service-Routinen (ISRs)**.
- Jeder Interrupt-Typ hat einen **eindeutigen Vektor** (z.B. INT 0x08 für Timer).
- Die CPU schlägt in der Tabelle nach, um zur richtigen ISR zu springen.

#### ✅ Prioritätsbehandlung

- Wenn mehrere Interrupts gleichzeitig auftreten, bestimmt die **Priorität**, welcher zuerst bearbeitet wird.
- Die Priorität kann **fest** oder **programmierbar** sein.

#### ✅ 8259A Programmierbarer Interrupt-Controller

- Verwaltet mehrere Interrupt-Quellen (bis zu 8).
- Kann für 64 Interrupt-Eingänge **kaskadiert** werden.
- Wichtige Funktionen:
  - Interrupt-Masking.
  - Prioritätseinstellung.
  - Senden des Interrupt-Vektors an die CPU.

**Register**:
- IMR (Interrupt Mask Register)
- ISR (In-Service Register)
- IRR (Interrupt Request Register)

**Beispiel**: Tastatur und Timer lösen beide Interrupts aus – der 8259A priorisiert sie basierend auf der konfigurierten Priorität.

---

### **3. Häufig verwendete Schnittstellen-Chips**

---

#### ✅ 8255A Programmierbare Peripherie-Schnittstelle (PPI)

Wird verwendet, um mit externen parallelen Geräten wie Schaltern, LEDs usw. zu verbinden.

- Hat 3 Ports: **Port A**, **Port B** und **Port C**.
- Wird über das **Steuerwort** gesteuert.

**Betriebsmodi**:

- **Modus 0** – Einfache E/A
  - Jeder Port kann Eingabe/Ausgabe sein.
- **Modus 1** – Handshake-E/A
  - Unterstützt Synchronisation mit dem Peripheriegerät.
- **Modus 2** – Bidirektionale E/A (nur für Port A)
  - Bidirektionale Datenübertragung mit Handshake.

**Beispiel**:
- Port A: Ausgabe zur LED-Anzeige
- Port B: Eingabe von DIP-Schaltern
- Port C: wird für Steuersignale verwendet

---

#### ✅ 8253 / 8254 Programmierbarer Intervall-Timer

Wird zur Erzeugung von Verzögerungen, Baudraten usw. verwendet.

- Hat 3 unabhängige 16-Bit-Zähler.
- Jeder Zähler hat Modi (0–5), z.B.:

| Modus | Beschreibung               |
|------|---------------------------|
| 0    | Interrupt bei Endezählstand |
| 2    | Raten-Generator (z.B. für Takt) |
| 3    | Rechteck-Generator     |

**Anwendungen**:
- Verzögerungserzeugung
- Echtzeituhr
- Baudraten-Erzeugung für serielle Schnittstellen

**Typische Verwendung**:
- Zähler 0: Betriebssystem-Timer-Tick
- Zähler 1: DRAM-Refresh
- Zähler 2: Lautsprecher-Ton

---

#### ✅ 8251A USART (Universal Synchronous/Asynchronous Receiver Transmitter)

Wird für **serielle Kommunikation** verwendet.

- Konvertiert zwischen parallelen und seriellen Daten.
- Unterstützt beides:
  - **Synchrone**: benötigt Taktsignal
  - **Asynchrone**: verwendet Start-/Stopp-Bits

**Wichtige Merkmale**:
- Baudraten-Steuerung (über 8253/8254)
- Konfigurierbare Zeichenlänge, Stopp-Bits, Parität
- Unterstützt Sende- und Empfangspufferung

**Anwendung**: Serielle Kommunikation mit PC oder Mikrocontroller.

---

## ✅ Übersichtstabelle

| Chip   | Funktion                   | Wichtige Merkmale                          |
|--------|----------------------------|----------------------------------------|
| 8255A  | Parallele E/A              | 3 Ports, 3 Modi, Handshake          |
| 8253/54| Zeitgeber/Zähler           | 3 Zähler, mehrere Modi             |
| 8251A  | Serielle Kommunikation     | Sync/Async, Baudraten-Steuerung               |
| 8259A  | Interrupt-Steuerung        | Priorität, Maskierung, ISR-Vektorisierung       |

---

## 🧠 Praxisbeispiel

Sie möchten ein einfaches Mikrocomputersystem entwerfen, um:

- Eine LED-Matrix über Port A (8255A Modus 0) zu steuern
- Tastatureingaben über Interrupts (8259A) zu empfangen
- Einen periodischen System-Tick alle 1ms zu erzeugen (8253 Modus 2)
- Sensordaten über die serielle Schnittstelle an einen PC zu senden (8251A im Async-Modus)

Jeder Chip würde durch Adressdekodierung und Steuersignale mit der CPU verbunden und konfiguriert, wobei entsprechende Software geschrieben wird, um die Kommunikation zu verwalten.

---

Lassen Sie mich wissen, wenn Sie Beispielcode, Simulationsdiagramme oder ein Quiz zu diesem Kapitel möchten!