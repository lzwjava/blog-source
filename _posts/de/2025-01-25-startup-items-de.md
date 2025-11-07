---
audio: false
generated: false
image: false
lang: de
layout: post
title: Startup-Elemente in macOS bereinigen
translated: true
type: post
---

Um Anwendungen und Prozesse zu verwalten, die automatisch gestartet werden, wenn Sie sich bei macOS (einschließlich macOS 15.2 und neuer) anmelden, können Sie Ihre Startelemente anpassen. Hier ist wie:

### 1. **Verwendung der Systemeinstellungen (oder Systemeinstellungen)**

   - **Schritt 1:** Klicken Sie auf das Apple-Menü () in der oberen linken Ecke Ihres Bildschirms und wählen Sie **Systemeinstellungen** (oder **Systemeinstellungen** auf älteren macOS-Versionen).
   - **Schritt 2:** Gehen Sie zu **Allgemein** und dann zu **Anmeldeelemente**.
   - **Schritt 3:** Eine Liste der Apps und Dienste, die beim Start gestartet werden, wird angezeigt. Um ein Element zu entfernen, wählen Sie es aus und klicken Sie auf die **Minus (–)** Schaltfläche unter der Liste.
   - **Schritt 4:** Wiederholen Sie dies für alle Elemente, die Sie entfernen möchten.

### 2. **Anpassen app-spezifischer Einstellungen**

   - Viele Anwendungen enthalten eigene Einstellungen, um das Startverhalten zu steuern. Suchen Sie in den Einstellungen oder Präferenzen der App, um den automatischen Start zu deaktivieren.

### 3. **Verwalten von Launch Agents und Daemons (Fortgeschritten)**

   - Hintergrundprozesse können durch Launch Agents oder Launch Daemons verwaltet werden. Diese befinden sich typischerweise in den folgenden Verzeichnissen:
     - `~/Library/LaunchAgents` (für benutzerspezifische Agents)
     - `/Library/LaunchAgents` (für systemweite Agents)
     - `/Library/LaunchDaemons` (für systemweite Daemons)
   - **Vorsicht:** Das Ändern dieser Dateien kann die Systemstabilität beeinträchtigen. Gehen Sie vorsichtig vor.

### Tipps:

- **Starten Sie Ihren Mac neu:** Nachdem Sie Änderungen vorgenommen haben, starten Sie Ihren Mac neu, um sicherzustellen, dass die Startelemente nicht mehr gestartet werden.