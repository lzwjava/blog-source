---
audio: false
generated: true
lang: de
layout: post
title: Energieerhaltung in Stromkreisschleifen
translated: true
type: note
---

Das Kirchhoffsche Spannungsgesetz (KVL) ist ein grundlegendes Prinzip in der Analyse elektrischer Schaltkreise. Es wird oft auch als Kirchhoffs zweites Gesetz oder die Maschenregel bezeichnet.

**Die Grundidee: Energieerhaltung**

Der einfachste Weg, KVL zu verstehen, ist, an die **Energieerhaltung** zu denken. Stellen Sie sich vor, Sie gehen einen geschlossenen Pfad (eine "Masche") in einem Schaltkreis entlang. Dabei treffen Sie auf verschiedene Komponenten wie Batterien und Widerstände.

*   **Batterien (Spannungsquellen):** Diese Komponenten geben Energie an die Ladungen im Stromkreis ab. Sie "heben" die potenzielle Energie der Ladungen, was zu einem Spannungs*anstieg* führt.
*   **Widerstände (Lasten):** Diese Komponenten verbrauchen Energie und wandeln sie in Wärme um. Wenn Ladungen durch sie hindurchfließen, "verlieren" sie potenzielle Energie, was zu einem Spannungs*abfall* führt.

KVL besagt, dass, wenn Sie an einem beliebigen Punkt in einer geschlossenen Masche starten, die gesamte Masche umrunden und zu Ihrem Startpunkt zurückkehren, die **algebraische Summe aller Spannungsanstiege und Spannungsabfälle, die Sie antreffen, null sein muss**.

**Stellen Sie sich eine Achterbahn vor:**

Stellen Sie sich eine Achterbahn vor.
*   Der Lifthügel ist wie eine Batterie – er fügt dem Wagen potenzielle Energie hinzu.
*   die Täler und Kurven sind wie Widerstände – der Wagen verliert potenzielle Energie (und gewinnt kinetische Energie, die aber letztendlich als Wärme oder Schall dissipiert wird).
*   Wenn die Achterbahnstrecke eine geschlossene Schleife ist, muss die gesamte potenzielle Energie des Wagens (relativ zum Startpunkt) dieselbe sein wie beim Verlassen des Startpunkts, wenn er dorthin zurückkehrt. Jeder "Anstieg" der potenziellen Energie vom Lifthügel muss durch "Abfälle" der potenziellen Energie entlang des restlichen Streckenverlaufs ausgeglichen werden.

**Wesentliche Prinzipien und Anwendung von KVL:**

1.  **Geschlossene Masche:** KVL gilt nur für eine geschlossene Masche in einem Stromkreis. Eine Masche ist jeder Pfad, der am selben Punkt beginnt und endet, ohne einen Zwischenknoten zu wiederholen.
2.  **Algebraische Summe:** Das bedeutet, dass Sie die *Polarität* (das Vorzeichen) jeder Spannung berücksichtigen müssen.
    *   **Spannungsanstieg:** Wenn Sie sich vom negativen zum positiven Anschluss einer Komponente (wie einer Batterie) bewegen, ist dies ein Spannungsanstieg, und Sie weisen dieser Spannung ein positives Vorzeichen zu.
    *   **Spannungsabfall:** Wenn Sie sich vom positiven zum negativen Anschluss einer Komponente bewegen (wie einem Widerstand, durch den der Strom von positiv nach negativ fließt), ist dies ein Spannungsabfall, und Sie weisen dieser Spannung ein negatives Vorzeichen zu. (Oder umgekehrt, solange Sie konsequent sind).
3.  **Konsistenz in der Richtung:** Wählen Sie eine Richtung, um die Masche zu durchlaufen (im Uhrzeigersinn oder gegen den Uhrzeigersinn), und bleiben Sie dabei. Das Endergebnis ist unabhängig von der gewählten Richtung, obwohl sich die Vorzeichen der einzelnen Terme umkehren können.
4.  **Mathematische Formulierung:**
    \\(\sum V = 0\\)
    wobei \\(\sum V\\) die algebraische Summe aller Spannungen in der Masche darstellt.

**Beispiel:**

Betrachten Sie einen einfachen Reihenschaltkreis mit einer Batterie (Spannung \\(V_{source}\\)) und zwei Widerständen (\\(R_1\\) und \\(R_2\\)).

Wenn der Strom im Uhrzeigersinn fließt:
*   Wenn Sie durch die Batterie von negativ zu positiv gehen, haben Sie einen Spannungsanstieg (\\(+V_{source}\\)).
*   Wenn Sie durch \\(R_1\\) in Richtung des Stroms gehen, haben Sie einen Spannungsabfall (\\(-V_1 = -IR_1\\)).
*   Wenn Sie durch \\(R_2\\) in Richtung des Stroms gehen, haben Sie einen Spannungsabfall (\\(-V_2 = -IR_2\\)).

Anwendung von KVL auf die Masche:
\\(V_{source} - V_1 - V_2 = 0\\)
oder
\\(V_{source} = V_1 + V_2\\)

Diese einfache Gleichung zeigt, dass die gesamte von der Quelle gelieferte Spannung über die Widerstände in der Masche verteilt (oder an ihnen abfällt) wird.

**Warum ist KVL wichtig?**

*   **Schaltkreisanalyse:** KVL ist unerlässlich für die Analyse elektrischer Schaltkreise, insbesondere komplexer Schaltkreise mit mehreren Maschen und Spannungsquellen.
*   **Ermitteln von Unbekannten:** Durch das Aufstellen von KVL-Gleichungen für verschiedene Maschen können Sie ein Gleichungssystem erstellen, mit dem Sie unbekannte Spannungen, Ströme und Widerstände im Stromkreis lösen können.
*   **Grundlage für andere Methoden:** KVL ist ein Grundbaustein für fortgeschrittenere Schaltkreisanalysetechniken wie die Maschenstromanalyse.

Im Wesentlichen ist KVL ein leistungsstarkes Werkzeug, das uns hilft zu verstehen, wie Energie in einem elektrischen Stromkreis verteilt und erhalten wird.