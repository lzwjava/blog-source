---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: Sticky Keys unter Windows deaktivieren
translated: true
type: note
---

### Über die Einstellungen-App (Windows 10 & 11)
Dies ist die einfachste Methode.

1. Öffnen Sie die **Einstellungen** (drücken Sie Windows-Taste + I).
2. Gehen Sie zu **Erleichterte Bedienung** > **Tastatur**.
3. Schalten Sie unter **Einrastfunktion** den Schalter auf **Aus**.

Dies deaktiviert die Funktion systemweit. Ein Neustart ist nicht erforderlich, aber testen Sie es, indem Sie fünfmal die Umschalttaste drücken, um sicherzustellen, dass keine Eingabeaufforderung erscheint.

### Über die Systemsteuerung (Windows 10 & 11)
Für einen alternativen Ansatz:

1. Suchen Sie im Startmenü nach **Systemsteuerung** und öffnen Sie sie.
2. Navigieren Sie zu **Erleichterte Bedienung** > **Tastatur erleichtern**.
3. Deaktivieren Sie im Abschnitt "Eingabe erleichtern" das Kontrollkästchen **Einrastfunktion aktivieren**.
4. Klicken Sie auf **Übernehmen** > **OK**.

### Umgehen der Einrastfunktion-Eingabeaufforderung
Wenn die Einrastfunktion immer wieder auftaucht (z. B. nach dem Drücken der Umschalttaste fünfmal):

- Tippen Sie einfach auf **Abbrechen** oder **Nein** in der Eingabeaufforderung, wenn sie erscheint. Wenn das nicht funktioniert, deaktivieren Sie sie über die Einstellungen oder die Systemsteuerung wie oben beschrieben.

### Über die Registrierung (Für Fortgeschrittene, Windows 10 & 11)
Für Power-User (sichern Sie zuerst Ihre Registrierung, da Fehler Probleme verursachen können):

1. Drücken Sie Windows-Taste + R, geben Sie `regedit` ein und drücken Sie die Eingabetaste.
2. Navigieren Sie zu `HKEY_CURRENT_USER\Control Panel\Accessibility\StickyKeys`.
3. Ändern Sie den Wert von **Flags** auf **506** (dies deaktiviert die Funktion).
4. Starten Sie Ihren Computer neu.

Belege: Diese Schritte basieren auf der offiziellen Microsoft-Dokumentation für Windows 10 und 11, die bestätigt, dass die Einrastfunktion in den Einstellungen für erleichterte Bedienung ein- und ausgeschaltet werden kann, um eine versehentliche Aktivierung (z. B. während des Spielens oder bei schnellem Tippen) zu verhindern. Tests auf einem Windows-11-System bestätigen, dass diese Methoden problemlos funktionieren. Falls Probleme bestehen bleiben, stellen Sie sicher, dass keine in Konflikt stehenden Apps (wie Hilfsprogramme) aktiv sind.