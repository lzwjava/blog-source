---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Deaktivieren der Klingelbenachrichtigung in Ghostty
translated: true
type: note
---

### Was ist Ghosttys "Benachrichtigungs-Tab"?

In Ghostty (einem GPU-beschleunigten Terminalemulator) bezieht sich der "Benachrichtigungs-Tab" wahrscheinlich auf die visuelle Klingel-Benachrichtigungsfunktion. Wenn ein Klingelzeichen (`\a`) von einem laufenden Befehl oder einer Anwendung im Terminal gesendet wird (z.B. von einem langlaufenden Prozess oder einem Fehler), kann Ghostty dem Titel des betroffenen Tabs oder Fensters ein Klingel-Emoji (🔔) voranstellen. Dies dient als dezenter Hinweis, um Ihre Aufmerksamkeit wieder auf diesen Tab zu lenken, insbesondere wenn das Terminal nicht im Fokus ist oder Sie in einem anderen Tab arbeiten. Es ist Teil von Ghosttys Klingel-Behandlungssystem, das nicht aufdringliche Benachrichtigungen ohne alleinige Abhängigkeit von Audio- oder System-Popups bieten soll.

Dieses Verhalten ist standardmäßig unter der `bell-features`-Konfiguration aktiviert, speziell die `title`-Option. Es ist für Workflows wie das Abschließen von Hintergrundjobs hilfreich, kann sich aber in der Tab-Leiste wie eine unerwünschte "Benachrichtigung" anfühlen.

### So deaktivieren Sie es

Um diese Klingel-Titel-Benachrichtigung (und möglicherweise andere Klingel-Verhaltensweisen) zu deaktivieren, bearbeiten Sie Ihre Ghostty-Konfigurationsdatei. Der Standardspeicherort ist `~/.config/ghostty/config` unter Linux oder `~/Library/Application Support/com.mitchellh.Ghostty/config` unter macOS.

1. Öffnen Sie die Konfigurationsdatei in Ihrem bevorzugten Editor.
2. Fügen Sie die folgende Zeile hinzu oder ändern Sie sie, um speziell das Titel-Emoji zu deaktivieren (während andere Klingel-Funktionen wie Aufmerksamkeitsanfragen erhalten bleiben):
   ```
   bell-features = no-title
   ```
   - Dies entfernt das 🔔 aus dem Tab-Titel, erlaubt aber andere Klingel-Effekte (z.B. Systemaudio oder Fensterhervorhebung).

3. Für eine umfassendere Deaktivierung (kein Titel-Emoji, keine Aufmerksamkeitsanfragen, etc.) verwenden Sie:
   ```
   bell-features = false
   ```
   - Dies schaltet alle Klingel-Funktionen vollständig aus.

4. Speichern Sie die Datei und laden Sie Ihre Konfiguration in Ghostty neu:
   - Drücken Sie `Cmd/Ctrl + Umschalt + ,` (oder führen Sie `ghostty --reload-config` von einem anderen Terminal aus).
   - Neue Fenster/Tabs verwenden die aktualisierten Einstellungen; bestehende müssen möglicherweise neu gestartet werden.

Falls dies nicht die exakte Benachrichtigung ist, die Sie meinen (z.B. wenn es sich um ein In-App-Toast wie "In Zwischenablage kopiert" oder Desktop-Benachrichtigungen von Apps handelt), können Sie diese auch deaktivieren:
- Für In-App-Toasts (nur Linux GTK): `app-notifications = false`
- Für Desktop-Benachrichtigungen von Terminal-Apps: `desktop-notifications = false`

Testen Sie dies, indem Sie einen Befehl ausführen, der eine Klingel auslöst, wie `echo -e '\a'`.

[Ghostty Config Reference](https://ghostty.org/docs/config/reference)  
[Ghostty Bell Features Discussion](https://github.com/ghostty-org/ghostty/discussions/3242)