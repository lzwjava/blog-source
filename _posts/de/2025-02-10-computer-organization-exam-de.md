---
audio: false
lang: de
layout: post
title: Computer Organization - Prüfungsfragen
translated: true
type: note
---

## April 2022 National Higher Education Self-Study Examination

## Rechnerorganisation

(Course Code 02318)

### Hinweise:

1.  Der Prüfungsbogen besteht aus zwei Teilen: Teil 1 (Multiple-Choice) und Teil 2 (Nicht-Multiple-Choice).
2.  Die Kandidaten müssen die Fragen in der vorgegebenen Reihenfolge an den dafür vorgesehenen Stellen auf dem Antwortbogen (Papier) beantworten. Auf dem Prüfungsbogen geschriebene Antworten sind ungültig.
3.  Für die Ausfüll- und Zeichenabschnitte muss ein 2B-Bleistift verwendet werden, für den Schreibabschnitt ein schwarzer Tintenstift.

### Teil 1: Multiple-Choice-Fragen

#### I. Multiple-Choice-Fragen: Dieser Abschnitt besteht aus 10 Fragen, je 1 Punkt, insgesamt 10 Punkte.

1.  Welche der folgenden Optionen gibt die Geschwindigkeit von Gleitkommaoperationen eines Computers an?
    -   A. CPI
    -   B. MIPS
    -   C. MFLOPS
    -   D. Taktfrequenz

2.  Im IEEE754-Gleitkomma-Darstellungsformat einfacher Genauigkeit (32-Bit) ist die Bias-Konstante des im Bias-Code dargestellten Exponenten
    -   A. 127
    -   B. 128
    -   C. 255
    -   D. 256

3.  In einem Computer ist die Ausrichtungsoperation für die Gleitkomma-Addition und -Subtraktion
    -   A. Die Zahl mit dem kleineren Exponenten erhöht ihren Exponenten und verschiebt die Mantisse nach rechts.
    -   B. Die Zahl mit dem kleineren Exponenten erhöht ihren Exponenten und verschiebt die Mantisse nach links.
    -   C. Die Zahl mit dem größeren Exponenten verringert ihren Exponenten und verschiebt die Mantisse nach links.
    -   D. Die Zahl mit dem größeren Exponenten verringert ihren Exponenten und verschiebt die Mantisse nach rechts.

4.  Der Wertebereich einer 8-Bit-Binär-Festkommazahl X in Zweierkomplement-Darstellung ist
    -   A. $-128<X<128$
    -   B. $-128<X \leqslant 128$
    -   C. $-128 \leqslant X \leqslant 127$
    -   D. $-128 \leqslant X \leqslant 128$

5.  Wenn zwei n-Bit-Zweierkomplement-Zahlen addiert werden, sind $\mathrm{C}_{n}$ und $\mathrm{C}_{n-1}$ die Übertragsbits, die jeweils von dem höchstwertigen und dem zweithöchstwertigen Bit erzeugt werden. Der logische Ausdruck für die Überlauferkennung ist
    -   A. $\mathrm{OF}=\mathrm{C}_{n}$
    -   B. $\mathrm{OF}=\mathrm{C}_{n}+\mathrm{C}_{n-1}$
    -   C. $\mathrm{OF}=\mathrm{C}_{n} \oplus \mathrm{C}_{n-1}$
    -   D. $\mathrm{OF}=\mathrm{C}_{n}-\mathrm{C}_{n-1}$

6.  Die Instruktion liefert eine Registernummer und eine Konstante. Wenn die Operandenadresse gleich der Summe des Registerinhalts und der Konstante ist, dann ist die Adressierungsart des Operanden
    -   A. Direkte Adressierung
    -   B. Registeradressierung
    -   C. Verschiebungsadressierung (Displacement Addressing)
    -   D. Indirekte Adressierung

7.  Welche der folgenden Beschreibungen passt am besten zu einem RISC-Computer?
    -   A. Viele Adressierungsarten für Instruktionen, die meisten Instruktionen können auf den Speicher zugreifen.
    -   B. Nur wenige Instruktionen können auf den Speicher zugreifen.
    -   C. Der Instruktionssatz hat eine große Anzahl von Instruktionen.
    -   D. Der Instruktionssatz hat Instruktionen variabler Länge.

8.  In einem Computer mit Mikroprogramm-Steuerwerk ist das Mikroprogramm gespeichert in
    -   A. Stack
    -   B. Hauptspeicher
    -   C. CPU
    -   D. Festplatte

9.  Cache-Speicher verwendet im Allgemeinen
    -   A. Dynamischen Speicher
    -   B. Statischen Speicher
    -   C. Nur-Lese-Speicher (ROM)
    -   D. Nichtflüchtigen Speicher

10. Das Sichern des Haltepunkts während des Interrupt-Behandlungsprozesses bezieht sich auf
    -   A. Das Auf den Stack schieben (Pushen) der Inhalte aller allgemeinen Register in der CPU.
    -   B. Das Auf den Stack schieben (Pushen) des Inhalts des Programmzählers (PC).
    -   C. Das Auf den Stack schieben (Pushen) des Inhalts des Instruktionsregisters in der CPU.
    -   D. Das Auf den Stack schieben (Pushen) des Inhalts des Registers SP.

### Teil 2: Nicht-Multiple-Choice-Fragen

#### II. Lückentext: Dieser Abschnitt besteht aus 15 Lücken, 1 Punkt pro Lücke, insgesamt 15 Punkte.

11. Im Entwicklungsprozess elektronischer Digitalrechner hatte jedes Zeitalter seine repräsentativen elektronischen Bauelemente. Die erste Generation verwendete Vakuumröhren, die zweite Generation verwendete _______, und ab der dritten Generation ist das Hauptbauelement _______.

12. Die Adressierungsmethoden des Hosts zu Peripherieports werden unterteilt in _______ und _______.

13. Die Adressabbildungsmethoden zwischen Hauptspeicher und Cache umfassen _______, vollassociative Abbildung und _______ Methoden.

14. Übliche Ein-/Ausgabe-Übertragungssteuerungsmethoden umfassen direkte Programmübertragung, _______ und _______.

15. Die Instruktionsformate im MIPS-Instruktionssatz sind unterteilt in _______ Typ, _______ Typ und I Typ.

16. Wenn die IEEE754-Gleitkommazahl einfacher Genauigkeit binär dargestellt wird, beträgt die Länge des Exponenten _______ Bits und die Länge der Mantisse _______ Bits.

17. Intel unterteilt externe Interrupts in _______ Interrupts und _______ Interrupts.

18. Die durchschnittliche Zugriffszeit eines Plattenspeichergeräts umfasst hauptsächlich Suchzeit, _______ Zeit und Datenübertragungszeit.

#### III. Begriffsdefinitionen: Dieser Abschnitt besteht aus 5 Fragen, je 3 Punkte, insgesamt 15 Punkte.

19. (Computer-)Wortlänge
20. Paritätsprüfcode
21. Registerindirekte Adressierung
22. Programmstatuswort-Register (PSW)
23. Direktzugriffsspeicher (RAM)

#### IV. Kurzfrage-Antworten: Dieser Abschnitt besteht aus 4 Fragen, je 5 Punkte, insgesamt 20 Punkte.

24. In modernen Computersystemen gibt es Betriebssysteme, Anwendungsprogramme, Computerhardware, Sprachverarbeitungssysteme, Instruktionssatzarchitekturen und andere Hardware- und Softwarekomponenten. Zeichnen Sie ein schematisches Diagramm der hierarchischen Beziehung zwischen ihnen.

25. Beschreiben Sie kurz die Methode zur Implementierung der Zweierkomplement-Subtraktion in einer Recheneinheit unter Verwendung eines Addierers und zeichnen Sie ein schematisches Diagramm der Implementierungsschaltung (Hinweis: Behandeln Sie den Addierer als Ganzes und müssen Sie seine interne spezifische Implementierung nicht zeichnen).

26. Beschreiben Sie kurz die Entsprechung zwischen Maschineninstruktionen, Mikroprogrammen, Mikroinstruktionen, Mikrobefehlen und Mikrooperationen in einer Mikroprogrammsteuerung.

27. Was ist dynamische Speicherauffrischung (Refresh)? Welche Anordnungsmethoden für den Refresh-Zyklus gibt es?

#### V. Berechnungsfragen: Dieser Abschnitt besteht aus 3 Fragen, je 6 Punkte, insgesamt 18 Punkte.

28. Die Maschinenzahl einer IEEE754-Gleitkommazahl einfacher Genauigkeit ist 41A50000H. Wandeln Sie sie in eine Dezimaldarstellung einer reellen Zahl um.

29. Verwenden Sie das 8-Bit-Binär-Zweierkomplement, um "-115 - ( -100 )" zu berechnen. Geben Sie das Ergebnis im Zweierkomplement an und geben Sie die endgültigen Flag-Bits SF, CF, OF und ZF jeweils an.

30. Ein Programm in einer Hochsprache wird von einem Compiler in eine ausführbare Instruktionssequenz übersetzt, die auf einer Maschine mit einer Taktfrequenz von 1 GHz läuft. Die in der Zielinstruktionssequenz verwendeten Instruktionstypen sind A, B, C und D. Die CPI der vier Instruktionstypen auf der Maschine und die Anzahl der Instruktionen jedes Typs sind in der folgenden Tabelle aufgeführt.

| Instruktionstyp | A | B | C | D |
| :--------------- | :-: | :-: | :-: | :-: |
| CPI jedes Typs | 1 | 2 | 3 | 4 |
| Anzahl der Instruktionen jedes Typs | 4 | 5 | 2 | 3 |

Wie hoch ist die CPI des Programms? Wie hoch ist die Ausführungszeit in ns? Runden Sie das Berechnungsergebnis auf eine Dezimalstelle.

#### VI. Umfassende Anwendungsfragen: Dieser Abschnitt besteht aus 2 Fragen, Frage 31 ist 12 Punkte wert und Frage 32 ist 10 Punkte wert, insgesamt 22 Punkte.

31. Ein Computer hat eine Wortlänge von 16 Bit und verwendet ein 16-Bit-Instruktionsformat fester Länge. Die teilweise Datenpfadstruktur ist in Abbildung 31 dargestellt. Nehmen Sie an, dass die Ausgabe von MAR immer aktiviert ist. Für die Instruktion SUB R1,(R2) beantworten Sie bitte die folgenden zwei Fragen.

(1) Wie viele Taktzyklen werden in der Ausführungsphase benötigt?
(2) Was ist die Funktion jedes Taktzyklus? Welche gültigen Steuersignale werden benötigt?

Hinweis: Die Funktion dieser Instruktion ist: R[R1] ← R[R1] - M[R[R2]]

32. Nehmen Sie an, dass eine 4-fach satzassociative Abbildungsmethode zwischen Hauptspeicher und Cache verwendet wird, die Datengröße eines Blocks 512 Byte beträgt, die Cache-Datenbereichskapazität 32 kByte beträgt und die Hauptspeicherraumgröße 1 MByte beträgt, byte-adressiert. Frage:

(1) In welche Teile ist die Hauptspeicheradresse unterteilt? Welche Adressbits sind in jedem Teil?
(2) Wie hoch ist die Gesamtkapazität des Cache in Bit? (Einschließlich des Gültigkeitsbits V)

---

### April 2022 National Higher Education Self-Study Examination Rechnerorganisation Prüfungsfragen Antworten und Bewertungsreferenz

(Course Code 02318)

#### I. Multiple-Choice-Fragen: Dieser Abschnitt besteht aus 10 Fragen, je 1 Punkt, insgesamt 10 Punkte.

1.  C
2.  A
3.  A
4.  C
5.  C
6.  C
7.  B
8.  C
9.  B
10. B

#### II. Lückentext: Dieser Abschnitt besteht aus 15 Lücken, 1 Punkt pro Lücke, insgesamt 15 Punkte.

11. Transistoren, Integrierte Schaltkreise
12. Separate Peripherieadressierung, Vereinheitlichte Peripherieadressierung
13. Direkte Abbildung, Satzassociative Abbildung
14. Interrupt-Übertragungsmodus, DMA-Übertragungsmodus
15. R, J
16. 8, 23
17. Maskierbare, Nicht-maskierbare
18. Umlaufverzögerung (Rotational Latency)

#### III. Begriffsdefinitionen: Dieser Abschnitt besteht aus 5 Fragen, je 3 Punkte, insgesamt 15 Punkte.

19. Antwort: Bezieht sich auf die grundlegende Anzahl von Binärstellen, die ein Computer in einer Operation verarbeitet. Wie z.B. 16 Bit, 32 Bit, 64 Bit.
20. Antwort: Fügen Sie zu den gültigen Datenbits ein Paritätsbit hinzu, so dass die Anzahl der "1"en in der Gesamtcodierung eine ungerade oder eine gerade Zahl ist.
21. Antwort: Der im Befehl angegebene Adresscode ist eine Registernummer, und das Register speichert die effektive Adresse des Operanden.
22. Antwort: Zeichnet den aktuellen Laufzustand des Programms auf und zeigt den Arbeitsmodus des Programms an.
23. Antwort: Zugriff auf Speicherzellen über Adressen, die Zugriffszeit jeder Speicherzelle ist eine Konstante, unabhängig von der Adressgröße.

#### IV. Kurzfrage-Antworten: Dieser Abschnitt besteht aus 4 Fragen, je 5 Punkte, insgesamt 20 Punkte.

24. Antwort: Das hierarchische Strukturdiagramm dieser fünf Teile ist wie folgt:

| Anwendungsprogramme |
| :------------------: |
| Sprachverarbeitungssystem |
|   Betriebssystem   |
| Instruktionssatzarchitektur |
|   Computerhardware  |

Bewertungshinweise: 1 Punkt für jeden Teil, die grafische Darstellung kann beliebig sein, solange sie die hierarchische Beziehung zwischen den Teilen erklären kann, wird sie als korrekt betrachtet.

25. Antwort: Nach dem Grundprinzip der Zweierkomplement-Operation: $[\mathrm{A}-\mathrm{B}]_{\text{Zweierkomplement}}=[\mathrm{A}]_{\text{Zweierkomplement}}+$ logisches NICHT($[\mathrm{B}]_{\text{Zweierkomplement}}$) (2 Punkte)
    Das logische NICHT([B] Zweierkomplement) bedeutet, [B] Zweierkomplement zu invertieren und 1 zu addieren, und das Addieren von 1 wird erreicht, indem der niedrigste Übertragseingang Cin des Addierers auf 1 gesetzt wird. (1 Punkt)

26. Antwort: Eine Maschineninstruktion entspricht einem Mikroprogramm (2 Punkte), ein Mikroprogramm besteht aus mehreren Mikroinstruktionen (1 Punkt), eine Mikroinstruktion erzeugt im Allgemeinen mehrere Mikrobefehle (1 Punkt) und ein Mikrobefehl entspricht im Allgemeinen einer Mikrooperation (1 Punkt).

27. Antwort: Da dynamischer Speicher auf Kondensatoren zur Informationsspeicherung angewiesen ist und die Kondensatorkapazität begrenzt ist und es Leckagen gibt, kann die Ladung nicht lange gespeichert werden. Um sicherzustellen, dass die gespeicherte Information nicht verloren geht, muss die Ladung in bestimmten Zeitintervallen periodisch auf den Kondensator nachgeladen werden; dies ist die Auffrischung (Refresh) des dynamischen Speichers. (2 Punkte)
    Anordnungsmethoden für den Refresh-Zyklus umfassen zentralisiertes Refresh (1 Punkt), verteiltes Refresh (1 Punkt) und asynchrones Refresh (1 Punkt).

#### V. Berechnungsfragen: Dieser Abschnitt besteht aus 3 Fragen, je 6 Punkte, insgesamt 18 Punkte.

28. Lösung: $41 \mathrm{~A} 50000 \mathrm{H}=01000001101001010000000000000000 \mathrm{~B}(1$ Punkt $)$
    Gemäß dem IEEE754-Gleitkommaformat einfacher Genauigkeit:
    Vorzeichen $\mathrm{s}=0$, die reelle Zahl ist positiv, der Dezimalteil der Mantisse $\mathrm{f}=(0.0100101) 2 (1$ Punkt $)$
    Exponent $\mathrm{e}=(\mathrm{1} 0000011) 2=(\mathrm{131}) 10(1$ Punkt $)$ , der wiederhergestellte Exponent ist $\mathrm{e}-127=131-127=4$ (1 Punkt), also ist die Gleitkommazahl:
    $(1.0100101) 2 \times 2^{4}=(10100.101) 2=20.625$ (2 Punkte)

29. Lösung: $[-115]_{Zweierkomplement}=10001101 \mathrm{~B},[-100]_{Zweierkomplement}=10011100 \mathrm{~B}, \quad[100]_{Zweierkomplement}=01100100 \mathrm{~B}$
    $[-115]_{Zweierkomplement}-[-100]_{Zweierkomplement}=[-115]_{Zweierkomplement}+[100]_{Zweierkomplement}=10001101 \mathrm{~B}+01100100 \mathrm{~B}=11110001 \mathrm{~B}(3$ Punkte $)$
    $\mathrm{SF}=1$ (1 Punkt), $\mathrm{CF}=1$ (1 Punkt), $\mathrm{OF}=0$ (1 Punkt)

30. Lösung: Das Programm hat insgesamt 14 Instruktionen, und die Anzahl der enthaltenen Taktzyklen beträgt $4 \times 1+5 \times 2+2 \times 3+3 \times 4=32$

    CPI ist $32 / 14 \approx 2.3$
    (3 Punkte)
    Ausführungszeit ist $32 / 1 \mathrm{G}=32.0 \mathrm{~ns}$
    (3 Punkte)

#### VI. Umfassende Anwendungsfragen: Dieser Abschnitt besteht aus 2 Fragen, Frage 31 ist 12 Punkte wert und Frage 32 ist 10 Punkte wert, insgesamt 22 Punkte.

31. Antwort:
    (1) 4 oder 5 Taktzyklen werden benötigt
    (2 Punkte)
    (2) Steuersignal Funktion
    R2out, MARin MAR ← (R2)
    MemR MDR ← M(MAR)
    $(\begin{array}{ll}2 & 2\end{array})$
    R1out, Yin Y ← (R1)
    MDRout, SUB ALU Z ← Y - (MDR)
    $(\begin{array}{ll}2 & 2\end{array})$
    Zout, R1in R1 ← (Z)
    (2 Punkte)
    Dabei können die 2. und 3. Zeile in einem Taktzyklus abgeschlossen werden oder jeweils einen Taktzyklus belegen.

32. Antwort: (1) Hauptspeicherraum 1 MByte $=2^{20}$ Byte, daher hat die Hauptspeicheradresse 20 Bit, Cache hat $32 \mathrm{~kB} / 512 \mathrm{~B}=64$ Zeilen, alle 4 Zeilen sind in 1 Gruppe, es gibt $64 / 4=16$ Gruppen, daher benötigt die Gruppennummer 4 Bit zur Darstellung.
    Die Hauptspeicheradresse ist in drei Teile unterteilt: Blockoffset, Gruppennummer und Tag (2 Punkte), die drei Teile sind:
    Blockoffset 9 Bits: $\mathrm{A}_{8} \sim \mathrm{A}_{0} \quad(2$ Punkte $)$
    Cache-Gruppennummer 4 Bits: $\mathrm{A}_{12} \sim \mathrm{A}_{9} \quad(2$ Punkte $)$
    Tag $20-9-4=7$ Bits: $\mathrm{A}_{19} \sim \mathrm{A}_{13} \quad(2$ Punkte $)$
    (2) Gesamt-Cache-Kapazität $=32 \mathrm{~KB}+(7+1) \times 64=32 \mathrm{~KB}+64 \mathrm{~B}=32832 \mathrm{~B}=262656$ Bit (2 Punkte)