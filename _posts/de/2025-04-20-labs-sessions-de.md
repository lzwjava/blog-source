---
audio: false
generated: true
lang: de
layout: post
title: 'Mikrocomputer- und Schnittstellentechnik: Laboratorien und Praktika'
translated: true
type: note
---

### **3. Praktische Übungen und Labore**

#### **Grundlagen-Labore**

**1. Assembler-Programmierung (Tastatureingabe/Anzeigeausgabe)**

- **Ziel**:
   Das primäre Ziel dieses Labors ist es, zu lernen, wie man Assemblerprogramme schreibt, die grundlegende Ein- und Ausgabeoperationen auf einem Mikrorechner durchführen.

- **Schlüsselkonzepte**:
   - Verstehen der **Assembler-Sprachsyntax**.
   - Interaktion mit I/O-Ports für **Tastatureingabe** und **Anzeigeausgabe**.
   - Verwendung von **Interrupts** zur Verarbeitung von Eingaben.

- **Laboraufgaben**:
   - **Tastatureingabe**: Schreiben Sie ein Assemblerprogramm, das einen Tastendruck erfasst und in einem Register speichert.
   - **Anzeigeausgabe**: Programmieren Sie das System so, dass die erfasste Taste auf einer 7-Segment-LED-Anzeige oder einem LCD-Bildschirm angezeigt wird.
   - **Programmsteuerung**: Implementieren Sie einfache Programmabläufe wie Schleifen oder bedingte Sprünge basierend auf Benutzereingaben.

- **Werkzeuge**: Mikrocontroller (z.B. 8051, PIC), Entwicklungsumgebungen wie **Keil** oder **MPLAB**, Hardware-Schnittstellen wie **LED-Anzeigen** oder **LCDs** und **Tastaturschnittstellen**.

---

**2. 8255A-gesteuerte LED-/Tastaturexperimente**

- **Ziel**:
   Dieses Labor konzentriert sich auf die Anbindung des **8255A Programmable Peripheral Interface (PPI)** an LEDs und eine Tastatur. Dieser Chip hilft bei der Verwaltung der Ein-/Ausgabeoperationen, was für effiziente Mikrorechnersysteme unerlässlich ist.

- **Schlüsselkonzepte**:
   - **8255A-Schnittstelle**: Lernen, wie man den 8255A-Chip programmiert und anbindet, um Ein-/Ausgabegeräte zu steuern.
   - **Port-Modi**: Der 8255A bietet drei Betriebsarten – **Eingabemodus**, **Ausgabemodus** und **bidirektionaler Modus**. Das Labor betont die Konfiguration des Chips zur effektiven Nutzung dieser Modi.
   - **LED-Steuerung**: Implementieren Sie die Verwendung von LEDs, um die Ergebnisse der vom System verarbeiteten Eingaben zu visualisieren.

- **Laboraufgaben**:
   - **LED-Steuerung**: Entwickeln Sie ein Programm, das bestimmte, an den 8255A-Chip angeschlossene LEDs ein- und ausschaltet.
   - **Tastaturschnittstelle**: Binden Sie ein **Tastenfeld** oder eine **Tastaturmatrix** an das System an, um dem Benutzer die Eingabe von Daten zu ermöglichen, die dann über LEDs angezeigt oder weiterverarbeitet werden können.
   - **Programmsteuerung**: Lernen Sie, wie man **Tastaturabfrage** und **Entprellung** handhabt, um eine genaue Tasterkennung zu gewährleisten.

- **Werkzeuge**: 8255A-Chip, **Mikrocontroller-Entwicklungskits**, Tastatur, LED-Arrays und **Software zum Konfigurieren und Programmieren des 8255A-Chips** (z.B. **Keil** oder **MPLAB**).

---

#### **Umfassende Labore**

**1. Interrupt-basiertes Ampelssteuerungssystem**

- **Ziel**:
   Das Hauptziel hier ist der Aufbau eines Ampelsystems, das durch **Interrupts** gesteuert wird. Dieses Labor konzentriert sich auf die Echtzeitsteuerung und verwendet Interrupts, um die verschiedenen Ampelzustände effizient zu verwalten.

- **Schlüsselkonzepte**:
   - **Interrupt-Behandlung**: Lernen, wie man Interrupt-Service-Routinen (ISRs) implementiert, um Ampelphasenübergänge zu steuern.
   - **Ampelsteuerung**: Steuern Sie mehrere LEDs, die die roten, gelben und grünen Lichter darstellen.
   - **Timer-Interrupts**: Verwenden Sie **Timer-Interrupts**, um in vordefinierten Intervallen zwischen verschiedenen Ampelzuständen zu wechseln.

- **Laboraufgaben**:
   - **Ampelsystem entwerfen**: Verwenden Sie Mikrocontroller und LEDs, um ein funktionierendes Ampelsystem mit mehreren Phasen (z.B. rot, gelb, grün) zu entwerfen.
   - **Interrupt-Service-Routinen (ISR)**: Entwickeln Sie ISRs, um die Lichter basierend auf Zeit oder externen Triggern (z.B. einer Anforderungstaste für Fußgänger) umzuschalten.
   - **Synchronisation**: Stellen Sie sicher, dass die Übergänge zwischen den Lichtern reibungslos erfolgen, um unsichere Situationen an Kreuzungen zu vermeiden.

- **Werkzeuge**: Mikrocontroller, **LED-Arrays** (für Ampeln), **Timer**, **Interrupt-Controller** und Entwicklungsumgebungen (z.B. **Keil**, **MPLAB**).

---

**2. Serielle Kommunikation (Datenübertragung/-empfang)**

- **Ziel**:
   Dieses Labor führt in die **serielle Kommunikation** ein, die für den Datenaustausch zwischen Mikrocontrollern oder Computern und externen Geräten unerlässlich ist.

- **Schlüsselkonzepte**:
   - **UART (Universal Asynchronous Receiver-Transmitter)**: Verstehen Sie den Betrieb des **UART-Protokolls** für die serielle Kommunikation.
   - **Datenframes**: Lernen Sie den Aufbau von Datenpaketen in der seriellen Kommunikation kennen (Startbit, Datenbits, Stoppbit, Parität).
   - **Kommunikationsprotokolle**: Implementieren Sie Protokolle wie **RS232**, **RS485** oder **TTL-Pegel-Kommunikation** zum Senden und Empfangen von Daten.

- **Laboraufgaben**:
   - **UART-Kommunikation implementieren**: Schreiben Sie Assembler- oder C-Programme, um Daten seriell zwischen zwei Mikrocontrollern oder einem Mikrocontroller und einem Computer zu senden und zu empfangen.
   - **Fehlererkennung**: Lernen Sie, wie man **Paritätsprüfung**, **Rahmenfehler** und **Überlauffehler** im Kommunikationsprozess implementiert.
   - **Datenübertragung**: Verwenden Sie die serielle Kommunikation, um einfache Daten wie Text, Zahlen oder Steuersignale zwischen Geräten zu übertragen.

- **Werkzeuge**: Mikrocontroller mit integrierter UART-Unterstützung (z.B. **8051**, **PIC** oder **AVR**), **serielle Schnittstellenmodule** (z.B. **MAX232** für RS232), Entwicklungsumgebungen (**Keil**, **MPLAB**, etc.).

---

### **Laborsicherheit und Fehlerbehebung**

- **Sicherheit**: Achten Sie beim Arbeiten mit Mikrocontrollern und Schnittstellengeräten stets auf einen ordnungsgemäßen Umgang mit der Stromversorgung und vermeiden Sie Kurzschlüsse. Verstehen Sie die Leistungsdaten für Komponenten (z.B. Spannungspegel für Mikrocontroller).

- **Fehlerbehebung**: Häufige Probleme sind falsche Verdrahtung, fehlerhafte Verbindungen und unsachgemäße Programmierung. Verwenden Sie Debugging-Werkzeuge wie **Oszilloskope** und **Logikanalysatoren**, um Signale zu überwachen und Kommunikations- oder Timing-Probleme zu beheben.

---

### **Schlussfolgerung**

Die Labore in diesem Kurs vermitteln praktische Erfahrungen in der Mikrorechner- und Schnittstellentechnologie und verbinden theoretisches Wissen mit praktischen Anwendungen. Sie werden an der Entwicklung von Schlüsselsystemen wie Ampelsteuerungen und seriellen Kommunikationssystemen arbeiten und dabei wertvolle Fähigkeiten für Embedded Systems und die Mikrocontroller-Programmierung erwerben.