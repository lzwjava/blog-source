---
audio: false
generated: true
image: false
lang: de
layout: post
model: anthropic/claude-4.5-sonnet
title: TCP- und UDP-Verbindungsunterschiede
translated: true
type: note
---

Du hast die richtige Intuition! Lassen Sie mich die wichtigsten Unterschiede verdeutlichen:

## TCP-Verbindung

Wenn eine TCP-Verbindung **hergestellt** wird (über den 3-Wege-Handschlag), pflegen beide Seiten **Statusinformationen** übereinander:

**Was jede Seite speichert:**
- **Remote-IP-Adresse und Port** (mit wem spreche ich?)
- **Lokale IP-Adresse und Port** (mein Endpunkt)
- **Sequenznummern** (für Reihenfolge und Zuverlässigkeit)
- **Fenstergrößen** (für Flusskontrolle)
- **Verbindungsstatus** (ESTABLISHED, CLOSING, etc.)

"Verbunden" bedeutet also, dass sowohl Client als auch Server Speicher und Ressourcen zugewiesen haben, um diese spezifische Kommunikation zu verfolgen. Sie wissen voneinander und pflegen diese Beziehung, bis die Verbindung geschlossen wird.

## UDP - Keine Verbindung

UDP ist **verbindungslos**. Es gibt keinen Handschlag, keinen gespeicherten Status:

- Der Client sendet einfach ein Paket an eine IP:Port
- Der Server empfängt es und verarbeitet es
- **Keine Seite pflegt jegliche Beziehungsinformationen**
- Jedes Paket ist unabhängig
- Sehr leichtgewichtig - kein Speicher-Overhead pro "Verbindung"

## Der entscheidende Unterschied

**TCP:** "Hallo, ich bin Client X. Lass uns reden. Hier sind meine Informationen, ich habe deine. Wir sind jetzt verbunden." → **Zustandsbehaftet**

**UDP:** "Hier ist ein Paket für Adresse Y:Port Z" → Fire-and-Forget → **Zustandslos**

Du hast absolut recht, dass UDP viel leichtergewichtig ist, weil es keinen Verbindungsstatus zu pflegen gibt, keine Puffer zu verwalten und keine Bestätigungen zu verfolgen gibt. Der Kompromiss ist, dass TCP Zuverlässigkeit, Reihenfolge und Flusskontrolle bietet, während UDP Geschwindigkeit und Einfachheit bietet.