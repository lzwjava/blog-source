---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Prinzip der GPS-Ortung einfach erklärt
translated: true
type: note
---

### Heutige zweite Wissenschaftsvermittlungsaufgabe: Ein Video, das das Prinzip des GPS-Positionssystems erklärt

Ich empfehle euch allen, dieses Video anzuschauen, das die Prinzipien des GPS-Positionssystems erklärt. Allerdings gab es ein kleines Problem mit einem der Bilder darin, deshalb habe ich eine schnelle Korrektur vorgenommen.

Das Prinzip ist eigentlich ganz einfach – man benötigt nur grundlegendes räumliches Geometriewissen, um es zu verstehen. Es lässt sich in einem Satz zusammenfassen: "Der Schnittpunkt von vier Kugeln ist ein einzelner Punkt." Jetzt werde ich im Detail erklären, wie genau das zutrifft:

1.  GPS-Satelliten (oder Boden-Basisstationen) senden Informationen, die ihre "Koordinaten" zum Zeitpunkt der Sendung und einen "Zeitstempel" enthalten. (Abbildung 1)

    *   Wenn der GPS-Empfänger dieses Signal empfängt, kann er die Entfernung \\( r_1 \\) von diesem Satelliten zu sich selbst mit dem Zeitstempel berechnen: \\( r_1 = \\) Lichtgeschwindigkeit × Übertragungszeit.

    *   Alle Positionen im Abstand \\( r_1 \\) von diesem Satelliten liegen auf einer Kugel mit dem Radius \\( r_1 \\). Der Einfachheit halber nenne ich das die "Abstandskugel". Die Geometrie lehrt uns, dass der Schnittpunkt zweier Kugeln ein Kreis ist, also ist der Schnittpunkt dieser "Abstandskugel" mit der Erde ein Kreis (Abbildung 2a – das erfordert etwas räumliches Vorstellungsvermögen). Offensichtlich können wir mit dem Signal nur eines Satelliten unseren genauen Standort nicht bestimmen; wir wissen nur, dass wir uns irgendwo auf diesem Kreis befinden.

    Wenn wir Signale von einem zweiten Satelliten mit seiner Position und Entfernung empfangen, können wir eine weitere Kugel zeichnen. Der Schnittpunkt dieser beiden Abstandskugeln mit der Erde – also drei Kugeln insgesamt – ergibt die möglichen Positionen, an denen wir uns befinden könnten. Dieser Schnittpunkt sind höchstwahrscheinlich nur zwei Punkte, aber wir wissen nicht, welcher der richtige ist. (Abbildung 2b)

    Mit der Position und Entfernung eines dritten Satelliten wird dessen Abstandskugel höchstwahrscheinlich durch einen dieser beiden Punkte verlaufen, aber nicht durch den anderen. Dies bestimmt die Koordinaten des Empfängers auf dem Boden. (Abbildung 2c)

    Wenn wir ein Signal von einem vierten Satelliten erhalten, wird dessen Abstandskugel ebenfalls durch diesen gleichen Punkt verlaufen. Wenn wir also nur Bodenkoordinaten benötigen, ist der vierte Satellit streng genommen nicht unbedingt notwendig. (Abbildung 2d)

All das lässt sich wirklich auf eine entscheidende Erkenntnis reduzieren: der Schnittpunkt von vier Kugeln ist ein einzelner Punkt. Die drei Abstandskugeln der Satelliten plus die Erde selbst (als vierte Kugel) schneiden sich an einem eindeutigen Punkt – nur an einem Ort.

Beachte, dass diese Signale nicht von Satelliten kommen müssen. Boden-Basisstationen mit bekannten Koordinaten können die gleiche Art von Signal senden (Koordinaten + Zeitstempel), und der Empfänger kann seine Position auf genau die gleiche Weise berechnen – es ist einfach eine geometrische Schnittpunktberechnung.

**Übung 1:** Im zweiten Schritt kann man, weil typischerweise ein Zeitunterschied zwischen der Uhr des Empfängers und der Uhr des GPS-Satelliten besteht, die "Übertragungszeit" nicht aus nur einem Signal erhalten. Aber wenn derselbe Satellit zwei Signale sendet, kann man diesen Versatz eliminieren und die Übertragungszeit berechnen. Versuche selbst herauszufinden, warum.

**Übung 2a:** Im vierten Schritt sagte ich, der Schnittpunkt der beiden Abstandskugeln und der Erde sei "höchstwahrscheinlich" nur zwei Punkte. In welchen speziellen Fällen wäre dieser Schnittpunkt mehr als zwei Punkte? Welche andere Form könnte er annehmen?

**Übung 2b:** Im fünften Schritt sagte ich, die Abstandskugel des dritten Satelliten verlaufe "höchstwahrscheinlich" durch einen der beiden Punkte, aber nicht durch den anderen. In welchen speziellen Fällen würde ihre Abstandskugel beide Punkte gleichzeitig durchlaufen?

**Übung 3:** Mit Signalen von vier Satelliten kann man nicht nur Koordinaten, sondern auch die Höhe (Höhenlage) berechnen. Warum ist der vierte Satellit also trotzdem nützlich?

**Übung 4:** Wenn wir uns vollständig auf Boden-Basisstationen verlassen, können wir Koordinaten mit Signalen von drei Stationen berechnen. Können wir mit dem Signal einer vierten Basisstation die Höhe berechnen? Wenn ja, welche Bedingung müssen die Positionen dieser vier Basisstationen erfüllen?

**Übung 5:** Wenn das Setup in Übung 4 machbar ist, entwirf ein "bodengestütztes GPS-System", das überhaupt keine Satelliten verwendet, aber die Funktionalität eines satellitengestützten GPS-Systems vollständig repliziert. Es sollte den Anforderungen der alltäglichen Fahrzeug- und Fußgängernavigation, der Luftfahrt, der Seefahrt, des Wanderns, des Offroad-Fahrens und mehr gerecht werden. Das System muss kostengünstig sein, mit Ausgaben, die nicht höher sind als die eines satellitengestützten Systems.

[Originalbeitrag: GPS-Prinzipien](https://yinwang1.substack.com/p/gps)