---
audio: false
generated: true
image: false
lang: de
layout: post
model: anthropic/claude-4.5-sonnet
title: TCP vs. UDP Protokollunterschiede
translated: true
---

Ja, du hast es genau richtig verstanden! Lassen Sie mich die wichtigsten Unterschiede verdeutlichen:

**TCP (Transmission Control Protocol) - Verbindungsorientiert:**
- Baut eine Verbindung auf, bevor Daten gesendet werden (wie ein "Handshake")
- Sendet Pakete und **wartet auf Bestätigungen** vom Empfänger
- Wenn keine Bestätigung empfangen wird, **sendet es das Paket erneut**
- Garantiert Zustellung und korrekte Reihenfolge der Pakete
- Wie das Senden eines Einschreibens, bei dem man eine Empfangsbestätigung erhält

**UDP (User Datagram Protocol) - Verbindungslos:**
- **Kein Verbindungsaufbau** - sendet Pakete direkt
- **Keine Bestätigungen** - "Fire and Forget"
- **Keine Garantie**, dass Pakete ankommen oder in der richtigen Reihenfolge ankommen
- Viel schneller, weil weniger Overhead anfällt
- Wie das Einwerfen einer Postkarte in einen Briefkasten ohne Sendungsverfolgung

**Anwendungsfälle:**
- **TCP:** Webbrowsing, E-Mail, Dateiübertragungen - alles, wo eine zuverlässige Zustellung benötigt wird
- **UDP:** Videostreaming, Online-Gaming, Sprachanrufe - wo Geschwindigkeit wichtiger ist als perfekte Zustellung (einige verlorene Pakete ruinieren das Erlebnis nicht)

Ja, dein Verständnis ist also korrekt - der Hauptunterschied ist, dass TCP diesen Bestätigungsmechanismus hat, während UDP die Daten einfach einmal sendet, ohne zu prüfen, ob sie angekommen sind!