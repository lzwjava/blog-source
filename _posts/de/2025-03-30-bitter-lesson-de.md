---
audio: false
generated: true
lang: de
layout: post
title: Rich Suttons bittere Lektion
translated: true
type: note
---

Rich Suttons "bitter lesson" (bittere Lektion) ist eine zum Nachdenken anregende Beobachtung über die Geschichte der Forschung im Bereich Artificial Intelligence (KI). Im Wesentlichen besagt sie, dass **KI-Forscher, die versuchen, menschenähnliches Wissen und handgefertigte Features in ihre Systeme einzubauen, schließlich an eine Grenze stoßen und von Ansätzen überholt werden, die mehr auf allgemeinen Lernalgorithmen basieren, sofern genügend Rechenleistung zur Verfügung steht.**

Der "bittere" Teil rührt daher, dass Forscher oft starke Intuitionen darüber haben, wie Intelligenz funktioniert und welche Art von Wissen oder Architektur vorteilhaft sein sollte. Die Geschichte hat jedoch wiederholt gezeigt, dass diese Intuitionen im Vergleich dazu, Algorithmen direkt aus Daten lernen zu lassen – durch Methoden wie Search und Learning – oft in Sackgassen führen.

Hier ist eine Aufschlüsselung der Schlüsselaspekte der bitteren Lektion:

* **Menschliches Wissen ist oft eine Krücke für kurzfristige Erfolge:** Obwohl die Einbeziehung menschlichen Wissens zu anfänglichen Fortschritten oder einer besseren Performance bei kleinen Datensätzen führen kann, schränkt es oft die Fähigkeit des Systems ein, zu skalieren und sich an komplexere Probleme oder größere Datenmengen anzupassen. Die handgefertigten Features werden spröde und versagen bei der Generalisierung.
* **Allgemeine Methoden triumphieren mit Skalierung:** Sutton argumentiert, dass die bedeutendsten Durchbrüche in der KI von allgemeinen Methoden wie Search (z.B. beim Spielen von Spielen) und Learning (z.B. im Machine Learning und Deep Learning) stammen. Diese Methoden können, wenn sie mit genügend Daten und Rechenleistung versorgt werden, ihre eigenen Repräsentationen und Strategien entdecken und übertreffen dabei oft von Menschen entwickelte Lösungen.
* **Die Bedeutung von Rechenleistung:** Ein zentrales Thema ist die zunehmende Verfügbarkeit und Bedeutung von Rechenleistung. Mit wachsender Rechenkraft verlagert sich der Vorteil hin zu Methoden, die diese Leistung effektiv nutzen können, um aus riesigen Datenmengen zu lernen.
* **Beispiele, die Sutton oft anführt:**
    * **Spiele (Schach, Go):** Frühe Versuche, schachspielende Programme zu entwickeln, stützten sich stark auf handcodierte Regeln und Bewertungsfunktionen, die auf dem Wissen menschlicher Experten basierten. Diese wurden schließlich von Systemen wie Deep Blue (das massive Search nutzte) und AlphaGo (das Deep Reinforcement Learning einsetzte) übertroffen, die ihre Strategien durch Berechnung und Daten lernten.
    * **Spracherkennung:** Frühe Spracherkennungssysteme beinhalteten viel linguistisches Wissen und handgefertigte Features. Moderne Systeme, die auf Deep Learning basieren und mit riesigen Mengen an Audiodaten trainiert wurden, haben eine viel bessere Leistung erzielt, ohne dieses Wissen explizit zu kodieren.
    * **Computer Vision:** Ähnlich wie bei der Spracherkennung verließ sich die frühe Computer Vision auf handgefertigte Features wie Kantendetektoren und Texturdeskriptoren. Deep-Learning-Modelle, die end-to-end auf großen Bilddatensätzen trainiert wurden, haben das Feld revolutioniert.

**Implikationen für die KI-Forschung:**

Suttons bittere Lektion legt nahe, dass sich die KI-Forschung mehr auf die Entwicklung skalierbarer, allgemeiner Lernalgorithmen konzentrieren und ihnen so viele Daten und Rechenleistung wie möglich zur Verfügung stellen sollte, anstatt zu versuchen, menschenähnliche Intelligenz fest zu kodieren oder sich stark auf handgefertigte Features zu verlassen. Es ist ein Aufruf, auf die Kraft des Lernens und den unaufhaltsamen Anstieg der Rechenressourcen zu vertrauen.

Auch wenn die bittere Lektion den Wert menschlicher Einsicht bei der Gestaltung der Lernalgorithmen selbst nicht vollständig abwertet, betont sie, dass das Wissen über die *Problemdomäne* oft am besten direkt aus den Daten gelernt werden sollte, anstatt es explizit einprogrammiert zu bekommen.

Zusammenfassend ist die bittere Lektion eine Erinnerung daran, dass, auch wenn menschliche Intuition ein Ausgangspunkt sein kann, der langfristige Erfolg der KI oft in der Fähigkeit allgemeiner Lernmethoden liegt, Lösungen durch Berechnung und Daten zu entdecken, selbst wenn diese Lösungen für den Menschen nicht unmittelbar intuitiv sind.