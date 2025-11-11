---
audio: false
generated: true
lang: de
layout: post
title: Grundlagen der Mikrocomputer
translated: true
type: note
---

Nachfolgend finden Sie ein umfassendes Tutorial für **Teil 1: Grundlagen von Mikrocomputern**, das die in Ihrer Anfrage umrissenen Themen abdeckt: *Überblick über Mikrocomputersysteme, Entwicklung, Von-Neumann-Architektur, Wichtige Leistungskennzahlen, Mikroprozessor (CPU)-Struktur, 8086/8088 interne Register und Bus-Zyklen und Timing-Analyse*. Dieses Tutorial ist gründlich und dennoch zugänglich gestaltet und setzt ein grundlegendes Verständnis von Computersystemen voraus.

---

## Teil 1: Grundlagen von Mikrocomputern

### 1. Überblick über Mikrocomputersysteme

Ein **Mikrocomputer** ist ein kleiner, relativ kostengünstiger Computer mit einem Mikroprozessor als zentrale Recheneinheit (CPU). Er umfasst Speicher, Eingabe-/Ausgabe-(E/A)-Schnittstellen und Peripheriegeräte, was ihn für persönliche, eingebettete oder industrielle Anwendungen geeignet macht.

#### Komponenten eines Mikrocomputersystems
- **Mikroprozessor (CPU)**: Das Gehirn des Systems, das Befehle durch Abrufen, Dekodieren und Ausführen verarbeitet.
- **Speicher**:
  - **ROM (Read-Only Memory)**: Speichert Firmware oder permanente Anweisungen (z.B. BIOS).
  - **RAM (Random Access Memory)**: Temporärer Speicher für Daten und Programme während der Ausführung.
- **Eingabe-/Ausgabe (E/A)-Geräte**: Schnittstellen für die Benutzerinteraktion (z.B. Tastatur, Maus, Bildschirm).
- **Bussystem**:
  - **Datenbus**: Überträgt Daten zwischen Komponenten.
  - **Adressbus**: Gibt Speicher- oder E/A-Adressen an.
  - **Steuerbus**: Überträgt Steuersignale zur Koordination der Vorgänge.
- **Peripheriegeräte**: Speicher (z.B. Festplatten), Kommunikationsanschlüsse und andere Hardware.

#### Merkmale
- Kompakte Größe, niedrige Kosten und Vielseitigkeit.
- Verwendung in Personal Computern, Embedded Systems (z.B. Haushaltsgeräte, Autos) und IoT-Geräten.
- Durch Software für verschiedene Aufgaben programmierbar.

---

### 2. Entwicklung der Mikrocomputer

Die Entwicklung der Mikrocomputer spiegelt Fortschritte in der Halbleitertechnologie, Software und Architekturdesign wider.

#### Wichtige Meilensteine
- **1971: Intel 4004**: Der erste Mikroprozessor, eine 4-Bit-CPU mit 2.300 Transistoren, entwickelt für Taschenrechner.
- **1974: Intel 8080**: Ein 8-Bit-Mikroprozessor, gilt als die erste echte Mikrocomputer-CPU, verwendet in frühen Systemen wie dem Altair 8800.
- **1978: Intel 8086/8088**: 16-Bit-Prozessoren, die den IBM PC (1981) antrieben und die x86-Architektur etablierten.
- **1980er: Personal Computer**: Apple II, IBM PC und Commodore 64 demokratisierten das Computing.
- **1990er–2000er**: 32-Bit- und 64-Bit-Prozessoren (z.B. Intel Pentium, AMD Athlon) mit gesteigerter Leistung.
- **2010er–Heute**: Multi-Core-Prozessoren, GPUs und ARM-basierte Mikrocomputer (z.B. Raspberry Pi) dominieren mobile und eingebettete Systeme.

#### Trends
- **Mooresches Gesetz**: Die Transistoranzahl verdoppelt sich etwa alle 18–24 Monate, was schnellere, kleinere CPUs ermöglicht.
- **Miniaturisierung**: Von raumgroßen Computern zu Handheld-Geräten.
- **Integration**: System-on-Chip (SoC)-Designs kombinieren CPU, GPU und Speicher.
- **Energieeffizienz**: Fokus auf stromsparende Prozessoren für mobile und IoT-Anwendungen.

---

### 3. Von-Neumann-Architektur

Die **Von-Neumann-Architektur** ist die Grundlage der meisten modernen Computer, einschließlich Mikrocomputer. Vorgeschlagen von John von Neumann im Jahr 1945, beschreibt sie ein System, in dem ein einzelner Speicher sowohl Befehle als auch Daten speichert.

#### Wichtige Merkmale
- **Einheitsspeicher**: Programme (Befehle) und Daten teilen sich denselben Speicherbereich, aufgerufen über denselben Bus.
- **Komponenten**:
  - **CPU**: Enthält:
    - **Arithmetisch-logische Einheit (ALU)**: Führt Berechnungen durch.
    - **Steuerwerk (CU)**: Verwaltet Befehlshol-, Dekodier- und Ausführungsvorgänge.
    - **Register**: Kleiner, schneller Speicher für temporäre Daten (z.B. Program Counter, Accumulator).
  - **Speicher**: Speichert Befehle und Daten.
  - **E/A-System**: Schnittstellen zu externen Geräten.
  - **Bus**: Verbindet Komponenten für Daten-, Adress- und Steuersignale.
- **Gespeichertes Programm Konzept**: Befehle werden im Speicher gespeichert, was eine dynamische Programmänderung ermöglicht.
- **Sequenzielle Ausführung**: Befehle werden nacheinander geholt, dekodiert und ausgeführt.

#### Von-Neumann-Flaschenhals
- Der gemeinsame Bus zwischen CPU und Speicher begrenzt die Leistung, da Daten und Befehle nicht gleichzeitig geholt werden können.
- Lösungen: Cache-Speicher, Pipelining und Harvard-Architektur (getrennter Befehls- und Datenspeicher, verwendet in einigen Mikrocontrollern).

#### Beispiel
In einem 8086-basierten Mikrocomputer:
- Befehle (z.B. `MOV AX, BX`) und Daten (z.B. Werte in AX, BX) befinden sich im RAM.
- Die CPU holt Befehle über den Adressbus, verarbeitet sie und speichert Ergebnisse zurück im Speicher oder in Registern.

---

### 4. Wichtige Leistungskennzahlen

Die Leistung eines Mikrocomputers hängt von mehreren Kennzahlen ab, die seine Verarbeitungsfähigkeit und Effizienz definieren.

#### a. Wortbreite
- **Definition**: Die Anzahl der Bits, die die CPU in einem einzigen Vorgang verarbeiten kann (z.B. 8-Bit, 16-Bit, 32-Bit, 64-Bit).
- **Auswirkung**:
  - Größere Wortbreiten ermöglichen die Verarbeitung mehrerer Daten gleichzeitig und verbessern die Leistung.
  - Bestimmt den Bereich des adressierbaren Speichers (z.B. 16-Bit-Adressbus = 64 KB, 32-Bit = 4 GB).
- **Beispiel**: Der Intel 8086 hat eine 16-Bit-Wortbreite, während moderne CPUs 64-Bit-Architekturen verwenden.

#### b. Taktfrequenz
- **Definition**: Die Frequenz, mit der die CPU Befehle ausführt, gemessen in Hertz (Hz), typischerweise MHz oder GHz.
- **Auswirkung**:
  - Höhere Taktfrequenzen bedeuten mehr Zyklen pro Sekunde und steigern den Durchsatz.
  - Begrenzt durch Stromverbrauch und Wärmeentwicklung.
- **Beispiel**: Der 8086 lief mit 4,77–10 MHz; moderne CPUs überschreiten 5 GHz mit Turbo Boost.

#### c. Speicherkapazität
- **Definition**: Die Menge an RAM und ROM, die für die Speicherung von Daten und Programmen verfügbar ist.
- **Auswirkung**:
  - Größerer Speicher unterstützt komplexe Anwendungen und Multitasking.
  - Cache-Speicher (z.B. L1, L2) reduziert die Zugriffszeit.
- **Beispiel**: Frühe 8086-Systeme hatten 64 KB–1 MB RAM; moderne Systeme haben 16–128 GB.

#### Andere Kennzahlen
- **Befehlssatz-Komplexität**: CISC (z.B. x86) vs. RISC (z.B. ARM) beeinflusst die Effizienz.
- **Busbreite**: Breitere Busse (z.B. 32-Bit vs. 16-Bit) verbessern die Datenübertragungsraten.
- **MIPS/FLOPS**: Misst Befehle oder Gleitkommaoperationen pro Sekunde.

---

### 5. Mikroprozessor (CPU)-Struktur

Der Mikroprozessor ist der Kern eines Mikrocomputers und für die Ausführung von Befehlen verantwortlich. Seine Struktur umfasst Funktionseinheiten und Verbindungen.

#### Allgemeine CPU-Komponenten
- **Arithmetisch-logische Einheit (ALU)**: Führt arithmetische (z.B. Addition) und logische Operationen (z.B. AND, OR) durch.
- **Steuerwerk (CU)**: Koordiniert Befehlshol-, Dekodier- und Ausführungsvorgänge.
- **Register**: Hochgeschwindigkeitsspeicher für temporäre Daten (z.B. Akkumulatoren, Indexregister).
- **Program Counter (PC)**: Enthält die Adresse des nächsten Befehls.
- **Instruction Register (IR)**: Speichert den aktuellen Befehl.
- **Bus Interface Unit (BIU)**: Verwaltet die Kommunikation mit Speicher und E/A.

#### 8086/8088 CPU-Struktur
Der Intel 8086 (16-Bit) und 8088 (8-Bit externer Datenbus) teilen sich eine ähnliche interne Struktur, unterteilt in:
- **Bus Interface Unit (BIU)**:
  - Bearbeitet Speicher- und E/A-Operationen.
  - Enthält Segmentregister (CS, DS, SS, ES) für die Adressierung von bis zu 1 MB Speicher.
  - Erzeugt physische Adressen mittels Segment:Offset-Adressierung.
- **Execution Unit (EU)**:
  - Führt Befehle unter Verwendung der ALU und der allgemeinen Register aus.
  - Enthält ein Flag-Register für Statusinformationen (z.B. Zero, Carry, Sign Flags).

---

### 6. 8086/8088 interne Register

Register sind kleine, schnelle Speicherorte innerhalb der CPU. Der 8086/8088 hat 14 16-Bit-Register, kategorisiert wie folgt:

#### a. Allgemeine Register
Werden für Datenmanipulation und Arithmetik verwendet.
- **AX (Akkumulator)**: Primäres Register für Arithmetik, E/A und Datenübertragung.
  - Unterteilt in AH (hohes Byte) und AL (niedriges Byte).
- **BX (Basis)**: Enthält Basisadressen oder Daten.
- **CX (Zähler)**: Wird in Schleifen und Zeichenkettenoperationen verwendet.
- **DX (Daten)**: Speichert Daten oder E/A-Port-Adressen.

#### b. Segmentregister
Werden für die Speicheradressierung (1 MB Adressraum) verwendet.
- **CS (Code Segment)**: Zeigt auf das Codesegment für Befehle.
- **DS (Data Segment)**: Zeigt auf das Datensegment.
- **SS (Stack Segment)**: Zeigt auf den Stack für Funktionsaufrufe und Interrupts.
- **ES (Extra Segment)**: Wird für zusätzliche Datensegmente verwendet.

#### c. Pointer- und Indexregister
Verwalten Speicherzeiger und Indizierung.
- **SP (Stack Pointer)**: Zeigt auf die Spitze des Stacks.
- **BP (Base Pointer)**: Greift auf Stack-Daten zu (z.B. Funktionsparameter).
- **SI (Source Index)**: Zeigt auf Quelldaten in Zeichenkettenoperationen.
- **DI (Destination Index)**: Zeigt auf Zieldaten in Zeichenkettenoperationen.

#### d. Instruction Pointer
- **IP**: Enthält den Offset des nächsten Befehls innerhalb des Codesegments.

#### e. Flag-Register
Ein 16-Bit-Register mit Status- und Steuer-Flags:
- **Status-Flags**:
  - **ZF (Zero Flag)**: Gesetzt, wenn das Ergebnis null ist.
  - **SF (Sign Flag)**: Gesetzt, wenn das Ergebnis negativ ist.
  - **CF (Carry Flag)**: Gesetzt, wenn ein Übertrag/Borrow auftritt.
  - **OF (Overflow Flag)**: Gesetzt, wenn ein arithmetischer Überlauf auftritt.
  - **AF (Auxiliary Carry)**: Wird für BCD-Arithmetik verwendet.
  - **PF (Parity Flag)**: Gesetzt, wenn das Ergebnis eine gerade Parität hat.
- **Steuer-Flags**:
  - **DF (Direction Flag)**: Steuert die Richtung von Zeichenkettenoperationen.
  - **IF (Interrupt Flag)**: Aktiviert/deaktiviert Interrupts.
  - **TF (Trap Flag)**: Aktiviert den Einzelschritt-Debugmodus.

#### Adressierung im 8086/8088
- **Physische Adresse** = Segmentregister × 16 + Offset.
- Beispiel: Wenn CS = 1000h und IP = 0100h, ist die Befehlsadresse 1000h × 16 + 0100h = 10100h.

---

### 7. Bus-Zyklen und Timing-Analyse

Der 8086/8088 kommuniziert mit Speicher und E/A-Geräten über **Bus-Zyklen**, die durch den CPU-Takt synchronisiert werden. Ein Bus-Zyklus definiert den Prozess des Lesens oder Schreibens von Daten.

#### Bus-Zyklus-Typen
- **Memory Read**: Holt Befehle oder Daten aus dem Speicher.
- **Memory Write**: Speichert Daten im Speicher.
- **I/O Read**: Liest Daten von einem E/A-Gerät.
- **I/O Write**: Sendet Daten an ein E/A-Gerät.

#### Bus-Zyklus-Struktur
Jeder Bus-Zyklus besteht aus **4 T-Zuständen** (Taktzyklen):
1. **T1**: Adresse wird auf den Adressbus gelegt; ALE (Address Latch Enable)-Signal wird aktiviert.
2. **T2**: Steuersignale (z.B. RD für Lesen, WR für Schreiben) werden ausgegeben.
3. **T3**: Daten werden über den Datenbus übertragen.
4. **T4**: Bus-Zyklus wird abgeschlossen; Statussignale werden aktualisiert.

#### Timing-Analyse
- **Taktfrequenz**: Bestimmt die Dauer eines T-Zustands (z.B. bei 5 MHz, 1 T-Zustand = 200 ns).
- **Wartezyklen (Wait States)**: Werden hinzugefügt, wenn Speicher/Geräte langsamer als die CPU sind, und verlängern T3.
- **Beispiel**:
  - Für einen Memory Read bei 5 MHz:
    - T1: Adresseneinrichtung (200 ns).
    - T2: RD-Signal aktiv (200 ns).
    - T3: Datenabtastung (200 ns, oder länger mit Wartezyklen).
    - T4: Bus freigegeben (200 ns).
    - Gesamt = 800 ns ohne Wartezyklen.
- **8088 Unterschied**: Der 8088 verwendet einen 8-Bit-Datenbus und benötigt zwei Bus-Zyklen für 16-Bit-Datenübertragungen, was die Leistung im Vergleich zum 16-Bit-Bus des 8086 reduziert.

#### Bus-Signale
- **ALE**: Latched die Adresse vom gemultiplexten Adress-/Datenbus.
- **RD/WR**: Zeigt Lese- oder Schreiboperation an.
- **M/IO**: Unterscheidet Speicher- vs. E/A-Zugriff.
- **DT/R**: Setzt die Datenbusrichtung (Senden/Empfangen).
- **DEN**: Aktiviert Datenbus-Treiber.

#### Praktische Überlegungen
- **Speicherzugriffszeit**: Muss kürzer als die Bus-Zyklus-Dauer sein, um Wartezyklen zu vermeiden.
- **Interrupts**: Können Bus-Zyklen unterbrechen, um externe Ereignisse zu behandeln.
- **DMA (Direct Memory Access)**: Unterbricht vorübergehend den CPU-Buszugriff für schnellere Datenübertragungen.

---

### Beispiel: 8086 Befehlausführung
Verfolgen wir einen einfachen Befehl, `MOV AX, [1234h]`, angenommen DS = 1000h:
1. **Holen**:
   - BIU berechnet Adresse: 1000h × 16 + 1234h = 11234h.
   - Befehl wird über einen Memory-Read-Zyklus (4 T-Zustände) geholt.
2. **Dekodieren**:
   - EU dekodiert `MOV` als eine Speicher-zu-Register-Übertragung.
3. **Ausführen**:
   - BIU führt einen weiteren Memory Read bei 11234h durch, um die 16-Bit-Daten zu holen.
   - Daten werden in AX geladen.
4. **Bus-Zyklen**:
   - Befehlsholen: 4 T-Zustände.
   - Datenholen: 4 T-Zustände.
   - Gesamt: ~8 T-Zustände (1,6 µs bei 5 MHz, keine Wartezyklen).

---

### Zusammenfassung
- **Mikrocomputersysteme**: Integrieren CPU, Speicher, E/A und Busse für vielseitiges Computing.
- **Entwicklung**: Von der 4-Bit Intel 4004 zu modernen 64-Bit Multi-Core-Prozessoren.
- **Von-Neumann-Architektur**: Einheitsspeicher für Befehle und Daten, mit einem sequenziellen Ausführungsmodell.
- **Leistungskennzahlen**: Wortbreite, Taktfrequenz und Speicherkapazität treiben die Fähigkeiten an.
- **8086/8088 Struktur**: BIU und EU mit spezialisierten Registern für Adressierung und Ausführung.
- **Register**: Allgemeine, Segment-, Pointer- und Flag-Register ermöglichen flexibles Programmieren.
- **Bus-Zyklen**: 4 T-Zustände für Speicher-/E/A-Operationen, kritisch für Timing und Leistung.

---

### Übungsfragen
1. Erklären Sie den Von-Neumann-Flaschenhals und wie moderne CPUs ihn mildern.
2. Berechnen Sie die physische Adresse für CS = 2000h, IP = 0500h.
3. Beschreiben Sie die Rolle jedes 8086-Segmentregisters.
4. Wie beeinflusst der 8-Bit-Datenbus des 8088 die Leistung im Vergleich zum 8086?
5. Simulieren Sie den Bus-Zyklus für eine Memory-Write-Operation bei 8 MHz.

---

Dieses Tutorial bietet eine solide Grundlage für das Verständnis der Mikrocomputer-Grundlagen, mit einem Fokus auf die 8086/8088-Architektur. Wenn Sie tiefer in spezifische Themen eintauchen möchten (z.B. Assembler-Programmierung, Interrupt-Behandlung), lassen Sie es mich wissen!