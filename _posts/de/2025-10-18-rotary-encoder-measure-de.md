---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Rotary Encoder messen Drehbewegungen
translated: true
type: note
---

### Was ist ein Drehgeber?

Ein **Drehgeber** (Rotary Encoder) ist ein elektromechanischer Sensor, der verwendet wird, um die Winkelposition oder Drehung einer Welle (wie bei Knöpfen, Drehreglern oder Rädern) in mechanischen Vorrichtungen zu erfassen und zu messen. Er wandelt Rotationsbewegung in digitale oder analoge Signale um, sodass Geräte verfolgen können, wie viel und in welche Richtung sich etwas gedreht hat. Sie sind in allem zu finden, von Lautstärkereglern an Audiogeräten bis hin zu Lenkrädern in der Robotik und Industrieausrüstung.

#### Wichtigste Typen
Es gibt zwei Hauptarten, basierend darauf, wie sie die Positionsverfolgung handhaben:

| Typ              | Beschreibung | Am besten geeignet für |
|-------------------|-------------|----------|
| **Inkremental**  | Gibt Impulse (oder "Ticks") für jede kleine Drehungsänderung aus und zählt Schritte relativ zu einem Startpunkt. Die Position wird durch Verfolgen dieser Änderungen über die Zeit berechnet. | Allmähliche, kontinuierliche Bewegungen wie Scrollräder oder Motorrückmeldung, bei denen die absolute Position nicht kritisch ist. |
| **Absolut**     | Liefert einen eindeutigen digitalen Code für jede mögliche Winkelposition, kennt also die exakte Position selbst nach einem Stromausfall. | Präzise Anwendungen wie Aufzüge oder CNC-Maschinen, bei denen es essentiell ist, die "Home"-Position ohne Zurücksetzen zu kennen. |

#### Funktionsweise (Vereinfacht)
- **Optisch**: Eine Lichtquelle scheint durch eine gemusterte Scheibe (mit Schlitzen oder Markierungen), die an der rotierenden Welle befestigt ist. Ein Sensor erkennt Unterbrechungen des Lichts, um Signale zu erzeugen.
- **Magnetisch**: Verwendet Magnete und Hall-Effekt-Sensoren, um Änderungen im Magnetfeld zu erfassen, wenn sich die Welle dreht.
- **Mechanisch**: Ältere Bauart mit direkten Kontakten, aber weniger zuverlässig aufgrund von Verschleiß.

Die von Ihnen erwähnten "allmählichen Positionsänderungen" passen perfekt zu inkrementalen Drehgebern, da sie sich hervorragend zum Erfassen sanfter, schrittweiser Drehungen eignen, ohne dass ein Zurücksetzen erforderlich ist.

Falls dies nicht ganz das ist, was Sie mit "was ist das?" gemeint haben (z. B. wenn Sie an ein bestimmtes Gerät oder einen Vergleich denken), klären Sie dies bitte gerne!