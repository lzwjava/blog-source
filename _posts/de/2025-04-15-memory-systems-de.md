---
audio: false
generated: true
lang: de
layout: post
title: Tutorial zu Speichersystemen
translated: true
type: note
---

Dieses Tutorial behandelt die Schlüsselkonzepte von Speichersystemen mit Schwerpunkt auf Speicherklassifizierung, RAM/ROM-Prinzipien und Adressdecodierungstechniken. Lassen Sie uns dies in umfassende Abschnitte unterteilen.

## 1. Speicherklassifizierung

Computerspeicher kann grob in zwei Hauptkategorien eingeteilt werden:

### 1.1 Nach Funktion
- **Primärspeicher**: Direkt von der CPU zugreifbar
  - RAM (Random Access Memory): Temporärer Speicher
  - ROM (Read-Only Memory): Permanenter Speicher
- **Sekundärspeicher**: Externe Speichergeräte (Festplatten, SSDs, etc.)

### 1.2 Nach Datenhaltbarkeit
- **Flüchtiger Speicher**: Verliert Daten bei Stromausfall (die meisten RAM-Arten)
- **Nicht-flüchtiger Speicher**: Behält Daten ohne Stromversorgung (ROM, Flash)

### 1.3 Nach Zugriffsmethode
- **Direktzugriff**: Jeder Speicherort kann direkt angesprochen werden (RAM, ROM)
- **Sequentieller Zugriff**: Daten werden nacheinander abgearbeitet (Magnetbänder)

## 2. RAM-Arbeitsprinzipien

RAM (Random Access Memory) ist der Hauptarbeitspeicher des Computers.

### 2.1 DRAM (Dynamic RAM)
- Speichert jedes Bit in einem winzigen Kondensator und Transistor
- Erfordert periodisches Auffrischen zur Datenerhaltung (typischerweise alle paar Millisekunden)
- Höhere Dichte, geringere Kosten, häufiger im Hauptspeicher verwendet
- Betriebszyklus: Row Address Strobe (RAS) → Column Address Strobe (CAS) → Datenzugriff

### 2.2 SRAM (Static RAM)
- Verwendet Flip-Flop-Schaltungen zur Speicherung jedes Bits
- Benötigt kein Auffrischen, behält Daten bei Stromversorgung
- Schneller, aber teurer und geringere Dichte als DRAM
- Wird im Cache-Speicher verwendet

### 2.3 RAM-Organisation
- Ist im Matrixformat aus Zeilen und Spalten organisiert
- Jede Zelle hat eine eindeutige Adresse (Zeile + Spalte)
- Datenbits sind typischerweise in Wortlängen organisiert (8, 16, 32, 64 Bits)

## 3. ROM-Arbeitsprinzipien

ROM (Read-Only Memory) speichert permanente oder semi-permanente Daten.

### 3.1 ROM-Typen
- **Mask ROM**: Während der Fertigung programmiert, kann nicht geändert werden
- **PROM (Programmable ROM)**: Kann einmal vom Benutzer programmiert werden
- **EPROM (Erasable PROM)**: Kann mit UV-Licht gelöscht und neu programmiert werden
- **EEPROM (Electrically EPROM)**: Kann elektrisch gelöscht und neu programmiert werden
- **Flash Memory**: Moderne Form von EEPROM, ermöglicht blockweises Löschen

### 3.2 ROM-Betrieb
- Enthält vorab geschriebene Daten bei Herstellung oder Programmierung
- Lesen: Adresse → Decoder → Sense Amplifier → Ausgangspuffer
- Schreiben (für beschreibbare Typen): Höhere Spannung wird verwendet, um die Speicherzellen zu modifizieren

## 4. Speichererweiterung

Da Programme komplexer werden, ist Speichererweiterung oft notwendig.

### 4.1 Kapazitätserweiterung
- **Chip-Auswahl**: Verwendung mehrerer Speicherchips zur Erhöhung des Gesamtspeichers
- **Wortlängenerweiterung**: Kombinieren von Chips zur Erweiterung der Datenbusbreite
- **Adressraumerweiterung**: Erhöhung des adressierbaren Speicherraums

### 4.2 Speicherbänke
- Speicher ist in Bänke organisiert, die unabhängig voneinander angesprochen werden können
- Ermöglicht Interleaving, reduziert die durchschnittliche Zugriffszeit
- Erleichtert parallele Operationen in modernen Architekturen

## 5. Adressdecodierungstechniken

Adressdecodierung ist entscheidend für den Zugriff auf den korrekten Speicherort.

### 5.1 Lineare Selektion (Vollständige Decodierung)
- Jede Adressleitung verbindet sich direkt mit einem Speicherort
- Einfach, aber ineffizient für große Speicherräume
- Beispiel: In einem System mit 16 Adressleitungen benötigen wir 2^16 (65.536) individuelle Verbindungen

### 5.2 Decoder-basierte Selektion
- **Adressdecoder**: Wandeln binäre Adressen in One-Hot-Selektionssignale um
- **2-zu-4-Decoder**: Nimmt 2 Adressbits, aktiviert eine von 4 Ausgangsleitungen
- **3-zu-8-Decoder**: Nimmt 3 Adressbits, aktiviert eine von 8 Ausgangsleitungen
- Gängige ICs: 74LS138 (3-zu-8), 74LS154 (4-zu-16)

### 5.3 Partielle Decodierung
- Nicht alle Adressbits werden decodiert, spart Hardware
- Mehrere Speicherorte können auf denselben physischen Ort abgebildet werden
- Erzeugt Speicher-"Schatten" oder "Spiegel"

### 5.4 Speicherabbildung
- **Kontinuierliche Abbildung**: Speicherblöcke sind sequentiell angeordnet
- **Seitenbasierte Abbildung**: Speicher ist in feste Seitengrößen unterteilt
- **Segmentierte Abbildung**: Speicher ist in variabel große Segmente unterteilt

## 6. Implementierungsbeispiele

### 6.1 Einfaches RAM-Erweiterungsbeispiel
Um ein 32K × 8 RAM-System auf 128K × 8 zu erweitern:
1. Verwenden Sie vier 32K × 8 RAM-Chips
2. Verwenden Sie 2 höherwertige Adressbits zur Auswahl zwischen den vier Chips
3. Verbinden Sie die verbleibenden Adressleitungen parallel mit allen Chips
4. Verwenden Sie einen 2-zu-4-Decoder für die Chip-Auswahl

### 6.2 Adressdecodierungsschaltung

Für ein System mit Speicher im Adressbereich 0x8000-0x9FFF:
1. Adressleitungen A15-A13 müssen "100" sein (für 0x8000-0x9FFF)
2. Verwenden Sie UND-Gatter, um dieses Muster zu erkennen
3. Aktivieren Sie den entsprechenden Speicherchip, wenn dieses Muster erkannt wird

Damit ist unser Überblick über Speichersysteme abgeschlossen, mit Schwerpunkt auf Klassifizierung, Arbeitsprinzipien und Erweiterungstechniken. Das Verständnis dieser Konzepte ist grundlegend für das effektive Entwerfen und Arbeiten mit Computersystemen.