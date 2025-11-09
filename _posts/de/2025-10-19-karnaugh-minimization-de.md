---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Karnaugh-Veitch-Diagramm Minimierungsbeispiel
translated: true
type: note
---

### Beispiel zur Verwendung von Karnaugh-Veitch-Diagrammen: Minimierung einer 3-Variablen-Booleschen Funktion

Gehen wir ein praktisches Beispiel durch, bei dem ein KV-Diagramm verwendet wird, um einen booleschen Ausdruck zu vereinfachen. Wir verwenden eine Funktion mit 3 Variablen (A, B, C), bei der der Ausgang für die Minterme m(1, 2, 4, 7) gleich 1 ist. Das bedeutet:

- f(A, B, C) = A'B'C + A'BC' + AB'C' + ABC

Das Ziel ist es, dies in so wenige Terme (und Literale) wie möglich zu minimieren, was die Anzahl der Logikgatter in einer Schaltung reduziert.

#### Schritt 1: Konstruiere das KV-Diagramm
Ein 3-Variablen-KV-Diagramm ist ein 2x4-Gitter (oder 4x2, aber wir verwenden Zeilen für AB und Spalten für C). Die Zeilen sind in Gray-Code-Reihenfolge (00, 01, 11, 10) beschriftet, um sicherzustellen, dass sich benachbarte Zellen nur um ein Bit unterscheiden. Setze 1en in die Zellen, die den Mintermen entsprechen:

| AB \ C | 0     | 1     |
|--------|-------|-------|
| **00** | 0     | 1 (m1) |
| **01** | 1 (m2) | 0     |
| **11** | 0     | 1 (m7) |
| **10** | 1 (m4) | 0     |

(Hier ist m1 = A'B'C, m2 = A'BC', m4 = AB'C', m7 = ABC.)

#### Schritt 2: Gruppiere benachbarte 1en
Der Schlüssel zur Minimierung liegt darin, die größtmöglichen Gruppen (Rechtecke oder Quadrate) von 1en zu finden, die benachbart sind (einschließlich wrap-around Rändern, wie bei einem Torus). Jede Gruppe muss eine Zweierpotenz (1, 2, 4, 8, usw.) in der Größe sein. Gruppen können sich überlappen.

- **Gruppe 1**: Die beiden 1en in der linken Spalte (m2 und m4) bilden ein vertikales Paar. Sie teilen sich A'B'C' – Moment, nein – Bitanalyse: m2 (010) und m4 (100) unterscheiden sich nur in A und B, aber im Gray-Code sind die Zeilen 01 und 10 benachbart. Diese Gruppe deckt die Änderung von A ab, also ist es B'C' (A ist Don't-Care).
- **Gruppe 2**: Die beiden 1en in der rechten Spalte (m1 und m7) bilden ein vertikales Paar, das sich um die Ränder herum erstreckt (Zeilen 00 und 11 sind nicht direkt benachbart, Moment – eigentlich für diese Karte, bessere Gruppierung: beachte m1 (001) und m2 (010) sind horizontal benachbart in Zeile 00-01? Moment, Korrektur.

Moment, zur Klarheit neu zeichnen – eigentlich, optimale Gruppen für diese Funktion:

- Horizontales Paar: m1 (Zeile00 Spalte1) und m2 (Zeile01 Spalte0)? Nein, nicht benachbart.
Standardgruppierung für diese Minterme:
- Quad? Nein. Paare:
  - m1 und m2? m1=001, m2=010 – unterscheiden sich in zwei Bits, nicht benachbart.
  Besser: m2 (010) und m4 (100) – unterscheiden sich in A (0 zu 1) und B (1 zu 0), zwei Bits – nicht benachbart.

Ich habe ein schlechtes Beispiel gewählt – lassen Sie mich ein besseres mit klaren Gruppen zur Veranschaulichung wählen.

**Überarbeitetes Beispiel zur Klarheit**: Verwenden wir f(A, B, C) = Σ m(0, 1, 2, 4, 5, 6) = A'B'C' + A'B'C + A'BC' + AB'C' + AB'C + ABC'

KV-Diagramm:

| AB \ C | 0     | 1     |
|--------|-------|-------|
| **00** | 1 (m0) | 1 (m1) |
| **01** | 1 (m2) | 0 (m3) |
| **11** | 1 (m6) | 0 (m7) |
| **10** | 1 (m4) | 1 (m5) |

Minterme: 0(000),1(001),2(010),4(100),5(101),6(110)—ja m3(011)=0, m7(111)=0.

Also Tabelle:

| AB \ C | 0     | 1     |
|--------|-------|-------|
| **00** | 1     | 1     |
| **01** | 1     | 0     |
| **11** | 1     | 0     |
| **10** | 1     | 1     |

#### Schritt 3: Identifiziere Gruppen
Nun gruppieren wir die 1en:

- **Große Gruppe (4 1en)**: Die gesamte linke Spalte (C=0): m0, m2, m6, m4. Dies sind alle Zellen, in denen C=0 ist und AB variiert – alle benachbart in einer Spalte (wrap-around für Zeilen). Dies deckt **C'** ab (da C 0 ist, sind A und B Don't-Care).
- **Paargruppe (2 1en)**: Obere Zeile rechts (m0 und m1? m0 Spalte0, m1 Spalte1 – horizontales Paar in Zeile 00: A'B' (C Don't-Care).
- Aber m1 (001) ist noch nicht abgedeckt? Moment, obere Zeile: m0 und m1 sind horizontal benachbart und decken A'B' ab (C variiert).
- Auch untere Zeile rechts m5 (101 Spalte1 Zeile10) – aber um m1 und m5 abzudecken? Sie sind in Spalte1, Zeilen 00 und 10, die benachbart sind (wrap-around), also vertikales Paar in Spalte1: m1 und m5, decken AC ab (Moment, Bits: 001 und 101 = A Don't-Care, B=0, C=1? 001 B=0 C=1, 101 A=1 B=0 C=1 – ja B'C.

Um zu minimieren, wählen wir nicht-überlappende oder minimale abdeckende Gruppen, die alle 1en mit den größten Größen abdecken.

Optimal:
- Gruppe 1: 4-Zellen vertikal in Spalte0: deckt C' ab (alle 1en dort: m0,m2,m4,m6 → Term: C')
- Gruppe 2: 2-Zellen horizontal in Zeile00: m0 und m1 → A'B'
- Gruppe 3: 2-Zellen vertikal wrap-around in Spalte1 Zeilen10 und 00? Moment, Zeilen 00 und 10 sind für Spalte1 benachbart: m1(001) und m5(101) → unterscheiden sich nur in A, also B'C (A Don't-Care).

m5 ist abgedeckt, m1 abgedeckt.

Hinweis: m0 ist sowohl in Gruppe1 als auch in Gruppe2, aber das ist OK – Überlappungen sind erlaubt.

#### Schritt 4: Leite den minimierten Ausdruck ab
Jede Gruppe wird zu einem Produktterm (UND der gemeinsamen Literale):
- Gruppe 1 (C'): **C'**
- Gruppe 2 (A'B'): **A' B'**
- Gruppe 3 (B' C): **B' C**

Also, minimierte SOP (Summe der Produkte): f = C' + A'B' + B'C

Überprüfung: Dies hat 3 Terme (vs. ursprünglich 6), weniger Literale (4 vs. 12), einfachere Schaltung (im Wesentlichen 3 UND/ODER-Gatter).

Man kann dies in einer Wahrheitstabelle darstellen, um zu bestätigen, dass es den ursprünglichen 1en entspricht.

#### Warum minimiert dies?
- **Nachbarschaftsregel**: Gruppen nur dort, wo sich Variablen um ein Bit ändern, um sicherzustellen, dass der Term diese Variable ignoriert (Don't-Care = - in der Karte).
- **Größte zuerst**: Größere Gruppen = weniger Variablen im Term = einfacher.
- **Decke alle 1en ab**: Keine 1 bleibt übrig; 0en müssen 0 bleiben (gruppiere sie nicht).
- Für mehr Variablen (4-Var-KV-Diagramm ist 4x4) gleicher Prozess, aber visuell schwieriger.

Dieses Beispiel zeigt, wie KV-Diagramme eine Summe von Mintermen schnell ohne algebraische Manipulation in eine kompakte Form bringen. Für 4+ Variablen verwende Software, aber Übung mit 2-3 Var Beispielen baut Intuition auf.

[Digital Logic Design Basics](https://www.allaboutcircuits.com/textbook/digital/chpt-7/karnaugh-mapping/)