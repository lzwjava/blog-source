---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Automatisierte Git-Synchronisation via Cron
translated: true
type: note
---

Um automatisch Updates von Git-Pushes eines Laptops auf einen Klon desselben Repos auf einem anderen Laptop zu synchronisieren (ohne manuelles `git pull`), kannst du dich nicht allein auf Git für Echtzeit-"automatische" Updates zwischen Maschinen verlassen – Git ist von Haus aus pull-basiert. Du kannst jedoch einen geplanten Task auf dem zweiten Laptop einrichten, um regelmäßig Änderungen vom Remote-Repository (in deinem Fall GitHub) abzurufen und zusammenzuführen. Dies ist die einfachste, zuverlässige Methode für ein persönliches Setup wie deines.

So geht das auf deinem Mac (da du ein MacBook Air verwendest). Wir verwenden `cron` für die Zeitplanung, da es eingebaut und leichtgewichtig ist. Gehe davon aus, dass beide Laptops Klone von `github.com:lzwjava/blog-source` haben und du auf dem `main`-Branch arbeitest.

### Schritt 1: Sicherstellen, dass das Repo auf dem zweiten Laptop korrekt eingerichtet ist
Auf dem zweiten Laptop:
1. Navigiere zu deinem Repo: `cd /pfad/zu/blog-source`
2. Stelle sicher, dass es den Remote verfolgt: `git remote -v` (sollte `origin` als dein GitHub-Repo anzeigen).
3. Falls nicht, füge es hinzu: `git remote add origin git@github.com:lzwjava/blog-source.git`
4. Rufe den aktuellen Stand ab: `git fetch origin`
5. Wechsle zu main: `git checkout main`
6. Setze den Upstream: `git branch --set-upstream-to=origin/main main`

Teste einen manuellen Pull: `git pull origin main`. Es sollte funktionieren wie in deiner Ausgabe.

### Schritt 2: Erstelle ein Skript für automatisiertes Pull
Erstelle ein einfaches Shell-Skript, das den Pull sicher durchführt (es fetched, prüft auf Konflikte und pulled, wenn sauber).

1. Erstelle im Root deines Repos `auto-pull.sh`:
   ```bash:disable-run
   #!/bin/bash
   cd "$(dirname "$0")"  # Wechsle in das Repo-Verzeichnis
   git fetch origin
   if git diff HEAD origin/main --quiet; then
       git pull origin main
       echo "Auto-pull abgeschlossen: $(date)"
   else
       echo "Warnung: Lokale Änderungen erkannt. Pull übersprungen. Manuell auflösen: $(date)"
       # Optional: E-Mail oder Benachrichtigung senden (siehe unten)
   fi
   ```

2. Mache es ausführbar: `chmod +x auto-pull.sh`

Dieses Skript:
- Holt Updates ab, ohne sie zusammenzuführen.
- Prüft, ob dein lokaler Branch sauber ist (keine unkommittierten Änderungen).
- Pullt nur, wenn es sicher ist; andernfalls warnt es dich.

### Schritt 3: Plane es mit Cron ein
Cron führt Jobs periodisch aus. Wir führen es alle 5 Minuten aus (passe dies nach Bedarf an; z.B. stündlich).

1. Öffne den Crontab-Editor: `crontab -e` (verwende nano, wenn aufgefordert: `nano ~/.crontab`).

2. Füge diese Zeile am Ende hinzu (für alle 5 Minuten):
   ```
   */5 * * * * /pfad/zu/blog-source/auto-pull.sh >> /pfad/zu/blog-source/pull-log.txt 2>&1
   ```
   - Ersetze `/pfad/zu/blog-source` mit deinem tatsächlichen Repo-Pfad (z.B. `~/blog-source`).
   - Das `>> pull-log.txt` protokolliert die Ausgabe in einer Datei zum Debuggen.

3. Speichere und verlasse den Editor (Ctrl+O, Enter, Ctrl+X in nano).
4. Überprüfe: `crontab -l` (sollte deine Zeile anzeigen).
5. Teste: Warte 5 Minuten oder füge `* * * * *` in `crontab -e` temporär hinzu (jede Minute) und setze es dann zurück.

Cron läuft unter deinem Benutzer, respektiert also deinen SSH-Key für die GitHub-Authentifizierung (wie in deiner Pull-Ausgabe).

### Optionale Verbesserungen
- **Behandle Konflikte/Benachrichtigungen**: Wenn das Skript Probleme erkennt, füge eine Benachrichtigung hinzu. Bearbeite `auto-pull.sh` und füge hinzu:
  ```bash
  # Bei Warnung, sende macOS-Benachrichtigung
  osascript -e 'display notification "Git pull übersprungen wegen lokaler Änderungen" with title "Blog Repo Sync"'
  ```
- **Bei Push ausführen (vom ersten Laptop)**: Für eine mehr "Push-artige" Synchronisation verwende GitHub Actions auf dem ersten Laptop. Erstelle `.github/workflows/sync.yml`:
  ```yaml
  name: Auto Sync
  on: [push]
  jobs:
    sync:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - name: Notify (z.B. via Webhook zum zweiten Laptop)
          run: curl -X POST https://your-second-laptop-webhook-endpoint  # Richte einen einfachen Server auf dem zweiten Laptop ein
  ```
  Dies erfordert jedoch einen Listener auf der zweiten Maschine (z.B. via ngrok + eine kleine Flask-App), was für die meisten Fälle übertrieben ist.
- **Abstimmung der Häufigkeit**: Alle 5 Minuten ist in Ordnung für ein Blog-Repo. Für Echtzeit, erwäge Tools wie `watch` in einem Terminal (`watch -n 300 git pull`), aber cron ist hands-off.
- **Hinweis zu Proxy**: Deine Ausgabe zeigt HTTP/HTTPS-Proxys an – cron wird sie übernehmen, also sollten Pulls wie gewohnt funktionieren.

Wenn du nun vom ersten Laptop pushst (`git push origin main`), wird der zweite automatisch alle 5 Minuten synchronisiert. Überprüfe `pull-log.txt` für den Verlauf.

Wenn du Auth/Proxy-Probleme in cron hast, füge `export HTTP_PROXY=http://127.0.0.1:7890` etc. zum Skript hinzu. Für Windows auf dem anderen Laptop verwende stattdessen Task Scheduler.