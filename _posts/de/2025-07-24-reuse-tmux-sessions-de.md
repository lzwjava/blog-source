---
audio: false
generated: true
lang: de
layout: post
title: Wiederverwendung bestehender tmux-Sitzungen
translated: true
type: note
---

Um vorhandene tmux-Sitzungen (wie Sitzung `1` oder `8` in Ihrem Fall) wiederzuverwenden, anstatt neue zu erstellen, können Sie sich bei einer bestehenden Sitzung anmelden, wenn Sie tmux starten. So können Sie vorgehen:

### Lösung
1. **Vorhandene Sitzungen auflisten**:
   Führen Sie `tmux list-sessions` (oder `tmux ls`) aus, um alle aktiven Sitzungen zu sehen:
   ```
   tmux list-sessions
   ```
   Ausgabe (aus Ihrem Beispiel):
   ```
   1: 1 windows (created Thu Jul 10 03:03:47 2025)
   8: 1 windows (created Thu Jul 24 02:11:07 2025)
   ```

2. **An einer bestimmten Sitzung anmelden**:
   Anstatt `tmux` auszuführen (was eine neue Sitzung erstellt), verwenden Sie den Befehl `attach-session` (oder `attach`), um sich mit einer bestehenden Sitzung zu verbinden. Zum Beispiel:
   - Um sich an Sitzung `1` anzumelden:
     ```
     tmux attach-session -t 1
     ```
   - Um sich an Sitzung `8` anzumelden:
     ```
     tmux attach-session -t 8
     ```

   Sie können `attach-session` zu `attach` abkürzen:
   ```
   tmux attach -t 1
   ```

3. **Überprüfen, ob tmux bereits läuft**:
   Wenn Sie versuchen, sich an einer nicht vorhandenen Sitzung anzumelden, gibt tmux einen Fehler aus. Um das versehentliche Erstellen einer neuen Sitzung zu vermeiden, können Sie überprüfen, ob tmux läuft, bevor Sie es starten. Fügen Sie dies beispielsweise Ihrem Shell-Skript oder Workflow hinzu:
   ```
   tmux has-session -t 1 && tmux attach -t 1 || tmux new-session -s 1
   ```
   Dies prüft, ob Sitzung `1` existiert; falls ja, meldet es sich daran an, andernfalls wird eine neue Sitzung mit dem Namen `1` erstellt.

4. **Komfortabler gestalten**:
   - **Alias für Komfort**: Fügen Sie Ihrer Shell-Konfiguration (z.B. `~/.zshrc` oder `~/.bashrc`) einen Alias hinzu, um sich immer an einer bestimmten Sitzung anzumelden:
     ```
     alias tmux1='tmux attach -t 1 || tmux new-session -s 1'
     ```
     Wenn Sie dann `tmux1` ausführen, wird sich an Sitzung `1` angemeldet, falls sie existiert, oder sie erstellt, falls nicht.
   - **Standard-Sitzung**: Wenn Sie immer eine bestimmte Sitzung (z.B. `1`) verwenden möchten, können Sie ein Skript erstellen oder Ihre `.tmux.conf` entsprechend konfigurieren, um dies zu automatisieren.

5. **Neue Sitzungen verhindern**:
   Um standardmäßig das Erstellen neuer Sitzungen beim Ausführen von `tmux` zu vermeiden, können Sie Ihren Workflow so konfigurieren, dass immer nach vorhandenen Sitzungen gesucht wird. Ändern Sie beispielsweise Ihre Shell so ab, dass sie Folgendes ausführt:
   ```
   tmux attach -t 1 2>/dev/null || tmux new-session -s 1
   ```
   Dies versucht, sich an Sitzung `1` anzumelden und unterdrückt Fehler, falls sie nicht existiert, und erstellt sie nur bei Bedarf.

6. **Optional: Sitzungen zur besseren Übersicht benennen**:
   Anstatt sich auf numerische Sitzungs-IDs (`1`, `8` usw.) zu verlassen, können Sie Sitzungen zur einfacheren Verwaltung benennen. Zum Beispiel:
   ```
   tmux new-session -s mywork
   ```
   Melden Sie sich später mit folgendem Befehl daran an:
   ```
   tmux attach -t mywork
   ```

### Warum das passiert
Wenn Sie `tmux` ohne Argumente ausführen, wird eine neue Sitzung mit einer automatisch hochzählenden ID (z.B. `1`, `8`) erstellt. Um zu verhindern, dass die Sitzungsnummer ansteigt, müssen Sie sich explizit mit `tmux attach -t <session>` an einer bestehenden Sitzung anmelden.

### Beispiel-Workflow
Um immer Sitzung `1` zu verwenden:
1. Führen Sie `tmux list-sessions` aus, um zu prüfen, ob Sitzung `1` existiert.
2. Wenn sie existiert, führen Sie `tmux attach -t 1` aus.
3. Wenn nicht, führen Sie `tmux new-session -s 1` aus.

Sie können dies in Ihrer Shell automatisieren:
```bash
if tmux has-session -t 1 2>/dev/null; then
  tmux attach -t 1
else
  tmux new-session -s 1
fi
```

### Hinweise
- Wenn eine Sitzung bereits an anderer Stelle angemeldet ist, müssen Sie sie möglicherweise zuerst trennen (`tmux detach`) oder mit `tmux attach -t 1 -d` erzwingen, um andere Clients zu trennen.
- Um ungenutzte Sitzungen zu bereinigen, können Sie sie mit `tmux kill-session -t <session>` beenden (z.B. `tmux kill-session -t 8`).

Dieser Ansatz stellt sicher, dass Sie Sitzungen wie `1` oder `2` wiederverwenden, ohne die Sitzungsanzahl zu erhöhen.

[tmux Man Page](https://man.openbsd.org/tmux.1)