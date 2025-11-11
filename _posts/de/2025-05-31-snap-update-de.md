---
audio: false
generated: true
lang: de
layout: post
title: Aktualisierung von VSCode über Snap unter Ubuntu
translated: true
type: note
---

Um Visual Studio Code (VSCode), das über Snap auf Ubuntu installiert wurde, zu aktualisieren, befolgen Sie diese Schritte:

1. **Öffnen Sie ein Terminal**: Drücken Sie dazu `Strg + Alt + T`.

2. **Prüfen Sie auf Updates**: Snap überprüft automatisch im Hintergrund auf Updates, aber Sie können manuell eine Überprüfung auslösen, indem Sie folgenden Befehl ausführen:
   ```bash
   sudo snap refresh
   ```

3. **VSCode aktualisieren**: Wenn eine neuere Version von VSCode verfügbar ist, lädt der Befehl `snap refresh` diese herunter und installiert sie. Sie sehen eine Ausgabe, die den Fortschritt anzeigt, etwa:
   ```
   code 1.85.2 from Visual Studio Code (code✓) refreshed
   ```
   Falls keine Updates verfügbar sind, wird angezeigt:
   ```
   All snaps up to date.
   ```

4. **Überprüfen Sie das Update**: Um die installierte Version von VSCode zu bestätigen, führen Sie aus:
   ```bash
   code --version
   ```
   Dies zeigt die aktuelle Version von VSCode an.

### Hinweise:
- **Automatische Updates**: Snap-Pakete, einschließlich VSCode, werden typischerweise automatisch im Hintergrund aktualisiert. In der Regel müssen Sie nicht manuell eingreifen, es sei denn, Sie möchten ein Update erzwingen.
- **Root-Rechte**: Der Befehl `sudo` ist für systemweite Snap-Operationen erforderlich.
- **Snap-Status prüfen**: Wenn Sie sehen möchten, welche Snap-Pakete installiert sind und ihre Versionen, verwenden Sie:
   ```bash
   snap list
   ```
- **Fehlerbehebung**: Wenn das Update fehlschlägt, stellen Sie sicher, dass Ihre Internetverbindung stabil ist und der Snap-Daemon läuft (`sudo systemctl status snapd`). Sie können auch versuchen, die Snap-Metadaten mit folgendem Befehl zu aktualisieren:
   ```bash
   sudo snap refresh --list
   ```

Dieser Prozess stellt sicher, dass VSCode mit der neuesten, im Snap Store verfügbaren Version auf dem aktuellen Stand bleibt.