---
audio: false
generated: true
lang: de
layout: post
title: Wie eine CPU Befehle verarbeitet
translated: true
type: note
---

Dieses Bild scheint eine Seite aus einem Lehrbuch oder Vorlesungsnotizen zur Computerarchitektur zu sein, mit einem spezifischen Fokus auf den Entwurf einer CPU (Central Processing Unit) und insbesondere auf den Memory Address Register (MAR) und dessen zugehörige Operationen. Hier ist eine detaillierte Erklärung des Inhalts:

### Textbeschreibung:
1.  **Einführung:**
    - Der Text erwähnt eine 16-Bit-CPU und erörtert die Rolle des Memory Address Register (MAR) im Betrieb der CPU.
    - Der MAR wird als ein 16-Bit-Register beschrieben, das zum Speichern von Speicheradressen verwendet wird.

2.  **Operationen mit MAR-Beteiligung:**
    - **Anweisung 1:** Der Text beschreibt einen Vorgang, bei dem der Inhalt von Register R2 vom Inhalt von Register R1 subtrahiert wird und das Ergebnis wieder in R1 gespeichert wird. Zusätzlich wird der Inhalt des MAR in R1 verschoben.
    - **Anweisung 2:** Der Text erwähnt eine weitere Operation, die den MAR beteiligt, aber die spezifischen Details sind auf dem Bild nicht vollständig sichtbar.

### Diagrammbeschreibung:
Das Diagramm veranschaulicht die Struktur und den Datenfluss innerhalb einer CPU und hebt die Interaktion zwischen verschiedenen Registern und der Arithmetic Logic Unit (ALU) hervor. Hier sind die Schlüsselkomponenten:

1.  **Register:**
    - **IR (Instruction Register):** Enthält den aktuell ausgeführten Befehl.
    - **PC (Program Counter):** Verfolgt die Adresse des nächsten auszuführenden Befehls.
    - **MAR (Memory Address Register):** Speichert die Adresse des Speicherorts, auf den zugegriffen wird.
    - **MDR (Memory Data Register):** Enthält die Daten, die aus dem Speicher gelesen oder in diesen geschrieben werden.
    - **R1 und R2:** Allgemeine Register, die zur temporären Speicherung und Manipulation von Daten verwendet werden.
    - **Y:** Ein weiteres Register, das an der Datenverarbeitung beteiligt ist.

2.  **ALU (Arithmetic Logic Unit):**
    - Führt arithmetische und logische Operationen mit den in den Registern gespeicherten Daten durch.
    - Die ALU hat Eingänge A und B und einen Ausgang Z.
    - Zu den Operationen gehören Addition (ADD), Subtraktion (SUB) und bitweise Operationen (1-Cx).

3.  **Datenfluss:**
    - Das Diagramm zeigt den Fluss der Daten zwischen den Registern, der ALU und dem Speicher.
    - Pfeile zeigen die Richtung der Datenübertragung an, z. B. vom MAR zum Speicheradressbus und vom Speicherdatenbus zum MDR.

### Zusammenfassung:
Das Bild bietet einen Überblick darüber, wie eine CPU Befehle verarbeitet, mit einem Fokus auf die Rolle des MAR bei der Adressierung des Speichers und die Interaktion zwischen verschiedenen Registern und der ALU. Text und Diagramm veranschaulichen zusammen die grundlegenden Operationen einer CPU, einschließlich Datenübertragung und arithmetischen/logischen Operationen.