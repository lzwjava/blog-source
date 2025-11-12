---
audio: false
generated: true
lang: de
layout: post
title: Digitale Elektronik
translated: true
type: note
---

Absolut! Hier ist ein umfassendes und zugängliches Tutorial für **Teil II: Digitalelektronik** aus *Grundlagen der Elektronik (III)*. Dieser Teil konzentriert sich darauf, wie digitale Systeme binäre Informationen darstellen, verarbeiten und manipulieren.

---

## 🔹 Teil II: Digitalelektronik

---

### **5. Grundlagen digitaler Schaltungen**

#### a. **Zahlensysteme und Codes**
- **Binär (Basis-2)**: Verwendet die Ziffern 0 und 1. Grundlegendstes System für digitale Systeme.
- **Oktal (Basis-8) und Hexadezimal (Basis-16)**: Kurzschreibweisen für Binärgruppen (3 oder 4 Bits).
- **BCD (Binary-Coded Decimal)**: Jede Dezimalziffer wird separat in Binär dargestellt (0000–1001).
- **Gray-Code**: Nur ein Bit ändert sich zwischen aufeinanderfolgenden Werten – wird in Drehgebern verwendet.

#### b. **Boolesche Algebra und Logikgatter**
- **Boolesche Operationen**:
  - **UND**: A·B = 1, wenn beide 1 sind
  - **ODER**: A + B = 1, wenn mindestens einer 1 ist
  - **NICHT**: 𝑨̅ = Inverses von A
- **Abgeleitete Gatter**:
  - **NAND**, **NOR**, **XOR**, **XNOR**
- **Kombinatorische Logik**: Die Ausgabe hängt nur von den aktuellen Eingängen ab.
  - Verwenden Sie **Wahrheitstabellen** und **Karnaugh-Veitch-Diagramme (KV-Diagramme)** zur Vereinfachung.

#### c. **TTL- und CMOS-Integrierte Schaltungen**
- **TTL (Transistor-Transistor-Logik)**:
  - Schneller, aber verbraucht mehr Leistung.
  - Logikpegel 1: ~5V; Pegel 0: ~0V.
- **CMOS (Complementary Metal-Oxide-Semiconductor)**:
  - Geringer Leistungsverbrauch, langsamere Geschwindigkeit, sehr verbreitet in modernen ICs.
  - Kompatibel mit weiten Spannungsbereichen.

---

### **6. Kombinatorische Logikschaltungen**

#### a. **Analyse und Entwurf**
- Beginnen Sie mit einer **Wahrheitstabelle**.
- Leiten Sie einen **booleschen Ausdruck** ab.
- Vereinfachen Sie ihn (mit booleschen Gesetzen oder KV-Diagramm).
- Zeichnen Sie die **Logikschaltung**.

#### b. **Gängige Module**
- **Encoder**: Wandeln 2ⁿ Eingangsleitungen in eine n-Bit-Ausgabe um (z.B. 8-zu-3-Encoder).
- **Decoder**: Gegenteil eines Encoders, wird bei der Speicheradressdecodierung verwendet.
- **Multiplexer (MUX)**: Wählt einen von vielen Eingängen aus.
  - Z.B., 4-zu-1 MUX: 2 Auswahlleitungen, 4 Eingänge → 1 Ausgang.
- **Demultiplexer (DEMUX)**: Ein Eingang wird zu einem von vielen Ausgängen geleitet.

#### c. **Hazards (Glitches)**
- **Statischer Hazard**: Die Ausgabe ändert sich kurzzeitig aufgrund von Gatterlaufzeiten.
- **Dynamischer Hazard**: Mehrere Störungen in der Ausgabe aufgrund von Zeitabweichungen.
- **Beseitigung**: Verwenden Sie redundante Logik oder synchrone Schaltungen.

---

### **7. Sequentielle Logikschaltungen**

#### a. **Flip-Flops (FFs)**
- **RS-Flip-Flop**: Set-Reset, einfacher Speicher.
- **D-Flip-Flop**: Daten- oder Verzögerungs-FF, am gebräuchlichsten.
- **JK-Flip-Flop**: Vielseitig; vermeidet den ungültigen Zustand des RS-FF.
- **T-Flip-Flop**: Toggelt bei Takt; wird in Zählern verwendet.

#### b. **Zähler und Schieberegister**
- **Zähler**:
  - **Asynchron (Ripple)**: Der Takt wird sequentiell weitergegeben; langsamer.
  - **Synchron**: Alle FFs werden gleichzeitig getaktet; schneller.
  - Typen: Aufwärts, Abwärts, Aufwärts/Abwärts.
- **Schieberegister**:
  - Speichern und verschieben Bits seriell oder parallel.
  - Typen: SISO, SIPO, PISO, PIPO.

#### c. **Analyse sequentieller Schaltungen**
- **Zustandstabellen/-diagramme**: Zeigen Übergänge zwischen Zuständen.
- Verwenden Sie FF-Ansteuertabellen zur Analyse und zum Entwurf.
- Synchrone Schaltungen sind einfacher zu steuern und zu debuggen als asynchrone.

---

### **8. Programmierbare Logikbausteine (PLDs)**

#### a. **Arten von PLDs**
- **PAL (Programmable Array Logic)**: Feste ODER-Verknüpfung, programmierbare UND-Verknüpfung.
- **GAL (Generic Array Logic)**: Wiederprogrammierbares PAL.
- **FPGA (Field Programmable Gate Array)**:
  - Hochgradig konfigurierbar.
  - Tausende/Millionen von Logikblöcken.
  - Wird in komplexen Systemen wie digitaler Signalverarbeitung, Videoverarbeitung etc. verwendet.

#### b. **Einführung in HDL (VHDL/Verilog)**
- **HDL (Hardware Description Language)**:
  - VHDL: Umfangreich und stark typisiert.
  - Verilog: Kompakt und C-ähnliche Syntax.
- Wird verwendet, um digitale Systeme auf verschiedenen Ebenen (Gatter, Register-Transfer, Verhaltensbeschreibung) zu modellieren.

#### c. **Beispiele für den Entwurf von Logiksystemen**
- Beispiel 1: 4-Bit-Binärzähler in Verilog.
- Beispiel 2: Einfache Ampelsteuerung mit FSM (Finite State Machine / Endlicher Automat).
- Beispiel 3: ALU (Arithmetic Logic Unit / Arithmetisch-logische Einheit) mit grundlegenden Operationen.

---

Möchten Sie Diagramme, Wahrheitstabellen oder Codeausschnitte (z.B. in Verilog oder VHDL)? Ich kann Ihnen auch Übungsaufgaben, Spickzettel oder Quizfragen zur Wiederholung geben. Lassen Sie mich wissen, wie tief Sie einsteigen möchten!