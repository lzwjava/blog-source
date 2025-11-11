---
audio: false
generated: true
lang: de
layout: post
title: Mikrocomputer- und Schnittstellentechnik – Überblick
translated: true
type: note
---

Hier ist eine deutsche Version des Kursplans für **"Mikrocomputer- und Schnittstellentechnik"**, basierend auf dem Syllabus von **Professor Yang Quansheng** (Hinweis: Der tatsächliche Inhalt kann je nach Lehrplan der Bildungseinrichtung variieren):

---

### **Mikrocomputer- und Schnittstellentechnik**
**Dozent:** Yang Quansheng
**Zielstudiengänge:** Informatik, Elektrotechnik, Automatisierungstechnik, etc.

---

#### **1. Kursziele**
1.  Beherrschung der grundlegenden Architektur und Arbeitsweise von Mikrocomputersystemen.
2.  Verständnis der Schnittstellentechnologien zwischen der CPU und Peripheriegeräten sowie der Datenübertragungsmethoden.
3.  Anwendung gängiger Schnittstellenchips (z.B. 8255, 8253, 8251) im Hardware-Design.
4.  Entwicklung von Fähigkeiten in der Assemblerprogrammierung und Schnittstellendebugging.

---

#### **2. Kursinhalt**
**Teil 1: Grundlagen der Mikrocomputer**
1.  Überblick über Mikrocomputersysteme
    - Entwicklung, Von-Neumann-Architektur
    - Wichtige Leistungskennzahlen (Wortlänge, Taktfrequenz, Speicherkapazität)
2.  Mikroprozessor (CPU)-Struktur
    - Interne Register des 8086/8088
    - Bus-Zyklen und Timing-Analyse

**Teil 2: Assemblerprogrammierung**
1.  8086-Befehlssatz
    - Datenübertragungs-, Arithmetik- und Logikbefehle
    - Ablaufsteuerungsbefehle (Sprünge, Schleifen, Unterprogramme)
2.  Assemblerprogrammierung
    - Sequenzielle/Verzweigungs-/Schleifenstrukturen
    - Interrupt-Service-Routinen

**Teil 3: Speichersysteme**
1.  Speicherklassifizierung und -erweiterung
    - Arbeitsprinzipien von RAM/ROM
    - Adressdekodierungstechniken (lineare Selektion, decoderbasiert)

**Teil 4: E/A- und Schnittstellentechnik**
1.  Grundlagen der E/A-Schnittstellen
    - Port-Adressierung (speicherbezogene vs. isolierte E/A)
    - Datenübertragungsmodi (programmgesteuert, interruptgesteuert, DMA)
2.  Interrupt-Systeme
    - Interrupt-Vektortabelle, Prioritätsbehandlung
    - Anwendungen des 8259A-Interrupt-Controllers
3.  Gängige Schnittstellenchips
    - **8255A Parallele Schnittstelle**: Modi (0/1/2) und Anwendungen
    - **8253/8254 Timer**: Zähl-/Zeitgeber-Konfigurationen
    - **8251A Serielle Schnittstelle**: Synchrone/asynchrone Protokolle

**Teil 5: Busse und Erweiterung**
1.  System-Bus-Standards
    - Überblick über ISA-, PCI-Bus
2.  Moderne Schnittstellentechnologien
    - Kurze Einführung in USB, SPI, I²C

---

#### **3. Laborübungen und Praktika**
1.  **Grundlagenübungen**
    - Assemblerprogrammierung (z.B. Tastatureingabe/Displayausgabe)
    - 8255A-gesteuerte LED-/Tastaturexperimente
2.  **Umfassende Übungen**
    - Interrupt-basiertes Ampelssteuerungssystem
    - Serielle Kommunikation (Datenübertragung/-empfang)

---

#### **4. Leistungsbewertung**
1.  **Theorieprüfung (60%)**: Schriftlich, ohne Hilfsmittel, behandelt Schnittstellenprinzipien und Designanalyse.
2.  **Laborbewertung (30%)**: Praktische Experimente und Berichte.
3.  **Teilnahme (10%)**: Aufgaben und Mitarbeit im Unterricht.

---

#### **5. Literatur**
1.  **Primärliteratur**:
    *Microcomputer Principles and Interface Technology* (Yang Quansheng, falls zutreffend)
2.  **Zusätzliche Texte**:
    - *Microcomputer Principles and Interfaces* (Zhou Heqin, Feng Huanqing)
    - *The Intel Microprocessors* (Barry B. Brey)

---

#### **6. Voraussetzungen**
- Digitale Schaltungen
- Rechnerorganisation
- C-Programmierung

---

**Hinweis:** Der aktuelle Lehrplan kann vom Dozenten angepasst werden. Für die neueste Version konsultieren Sie bitte die offiziellen Kursmaterialien oder wenden Sie sich an das Lehrteam.