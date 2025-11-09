---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Übersicht kombinatorischer Logikbausteine
translated: true
type: note
---

### Übersicht

Das Video von "The Learning Circuit" erklärt kombinatorische Logikbausteine, deren Ausgänge ausschließlich von den aktuellen Eingängen abhängen (kein Speicher für vorherige Zustände). Es behandelt vier wichtige Typen: Multiplexer (MUX), Demultiplexer (DEMUX), Encoder und Decoder. Diese sind wesentlich für Signalrouting, Datenkompression/-expansion und digitale Steuerung in der Elektronik.

### Multiplexer (MUX)

- **Zweck**: Funktioniert wie eine digitale Vermittlungsstelle – wählt einen von vielen Eingängen aus, um ihn an einen einzelnen Ausgang zu senden, gesteuert durch Select-Leitungen.
- **Einfaches Beispiel (74LS157 Quad 2-to-1 MUX)**:
  - 4 Kanäle, jeweils mit Eingängen A und B, einem Select-Pin (S) und einem Enable-Pin (E).
  - S high: Wählt A-Eingänge; S low: Wählt B-Eingänge.
  - E low: Aktiviert den Ausgang; E high: Deaktiviert (Ausgänge werden low).
- **Größere Beispiele**:
  - 4-to-1 MUX: 2 Select-Leitungen wählen aus 4 Eingängen.
  - 8-to-1 MUX: 3 Select-Leitungen; nur ein Eingang wird durchgeschaltet.
- **Tipp**: Allgemeine Form ist \\(2^n\\)-to-1, wobei \\(n\\) die Anzahl der Select-Leitungen ist.

### Demultiplexer (DEMUX)

- **Zweck**: Das Gegenteil eines MUX – leitet einen Eingang zu einem von vielen Ausgängen, basierend auf Select-Leitungen.
- **Einfaches Beispiel (1-to-2 DEMUX)**:
  - Eine Select-Leitung (S): S low → Eingang zu Y0; S high → Eingang zu Y1.
- **Allgemeine Regel**: \\(1\\)-to-\\(2^n\\) Ausgänge, entsprechend den Select-Leitungen des MUX (z.B. 2 Selects → 4 Ausgänge).

### Encoder

- **Zweck**: Komprimiert mehrere Eingänge in eine codierte (z.B. binäre) Ausgabe.
- **Einfacher Binär-Encoder**:
  - Beispiel: 4 Eingänge → 2-Bit-Binärausgabe (z.B. Eingang 3 aktiv → Ausgabe 11).
  - Problem: Mehrere aktive Eingänge können Konflikte verursachen (mehrdeutige Ausgabe).
- **Priority-Encoder** (behebt Konflikte):
  - Weist Prioritäten zu (höchste Priorität überschreibt andere).
  - Beispiel (8-Eingänge, active-low): Eingang 7 (höchste) aktiv → Ausgabe 111, ignoriert niedrigere Eingänge.
  - Keine Eingänge aktiv → Ausgabe 000.

### Decoder

- **Zweck**: Erweitert einen codierten Eingang in mehrere Ausgänge (z.B. aktiviert spezifische Leitungen).
- **Einfacher Binär-Decoder**:
  - Ähnlich einem DEMUX: Binäreingang wählt einen Ausgang aus (z.B. 2-Bit-Eingang 10 → aktiviert Ausgang 2).
- **BCD-zu-7-Segment-Decoder**:
  - 4-Bit-BCD-Eingang (0–9) → Steuert 7 LED-Segmente für die Ziffernanzeige.
  - Beispiele: "0" leuchtet 6 Segmente; "1" leuchtet 2 (rechte Balken).
- **BCD-zu-Dezimal-Decoder**:
  - 4-Bit-Eingang → Aktiviert einen von 10 Ausgängen (für die Ziffern 0–9).

### Wichtige Erkenntnisse

- **MUX/DEMUX**: Datenrouter (Verkehrsleitsysteme).
- **Encoder**: Mehr Eingänge als Ausgänge (Datenkompression, wie Zippen).
- **Decoder**: Mehr Ausgänge als Eingänge (Datenexpansion, wie Entzippen).
- Alle sind "kombinatorisch" – der Ausgang ändert sich sofort mit den Eingängen, keine Takte oder Speicherung.

[How Combinational Logic Devices Work - The Learning Circuit](https://www.youtube.com/watch?v=gsmB7J72Tgc)