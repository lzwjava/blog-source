---
audio: false
generated: true
lang: de
layout: post
title: Ubuntus Maus-Batterieverwaltung
translated: true
type: note
---

Ubuntu verfügt über mehrere integrierte Funktionen, die helfen, den Stromverbrauch der Maus zu verwalten und Benachrichtigungen bei niedrigem Batteriestand bereitzustellen:

## Stromverwaltung für Mäuse in Ubuntu

**Batterieüberwachung:**
- Das Energieverwaltungssystem von Ubuntu überwacht die Batteriestände von kabellosen Mäusen über Bluetooth- oder USB-Empfänger-Verbindungen.
- Das System liest Batteriedaten aus der Firmware der Maus, sofern verfügbar.
- Strombenachrichtigungen erscheinen im System-Tray, wenn der Batteriestand unter bestimmte Schwellenwerte fällt (normalerweise bei etwa 20 % und 10 %).

**Wie das Benachrichtigungssystem funktioniert:**
- **UPower-Daemon** – Überwacht die Energiezustände angeschlossener Geräte, einschließlich kabelloser Mäuse.
- **GNOME Power Manager** – Verarbeitet die eigentlichen Benachrichtigungen und Energieeinstellungen.
- **Bluetooth-Stack** – Für Bluetooth-Mäuse werden Batterieinformationen über Standard-Bluetooth-Protokolle übertragen.
- **USB HID** – Für kabellose Mäuse mit USB-Dongles kommen die Batteriedaten über HID (Human Interface Device)-Reports.

**Energiesparfunktionen:**
- Automatischer Ruhemodus der Maus bei Inaktivität.
- Reduzierte Abfrageraten bei geringer Aktivität.
- Einstellungen für Verbindungstimeouts zur Batterieschonung.
- Option zum Deaktivieren des Maus-Aufweckens aus dem Ruhezustand.

**Batteriestatus der Maus prüfen:**
Sie können den Batteriestatus der Maus überprüfen durch:
- Systemeinstellungen → Energie (zeigt angeschlossene Geräte an).
- Befehlszeile: `upower -i /org/freedesktop/UPower/devices/mouse_*`.
- Batterieanzeige in der oberen Leiste (falls von der Maus unterstützt).

Das System funktioniert, indem es kontinuierlich angeschlossene Geräte auf ihren Energiezustand abfragt und Desktop-Benachrichtigungsdienste nutzt, um Benutzer zu warnen, wenn Eingreifen nötig ist. Dies hilft, unerwartete Trennungen während wichtiger Arbeiten zu verhindern.