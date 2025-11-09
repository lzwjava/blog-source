---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Behebung von npm-Installationsfehlern
translated: true
type: note
---

### Fehleranalyse

Dies ist ein npm-Installationsfehler während eines globalen Updates (oder einer Installation) des Pakets `@anthropic-ai/claude-code`. Das Kernproblem liegt in der "Reify"-Phase, in der npm versucht, das bestehende Paketverzeichnis zu "pensionieren" (sichert es) bevor die neue Version installiert wird. Konkret:

- npm versucht, `/usr/lib/node_modules/@anthropic-ai/claude-code` in ein temporäres Backup wie `/usr/lib/node_modules/@anthropic-ai/.claude-code-ZjqcDZyQ` umzubenennen.
- Dies schlägt mit `ENOTEMPTY: directory not empty` (errno -39) fehl, was typischerweise auftritt, wenn:
  - Das Quellverzeichnis Dateien/Unterverzeichnisse enthält, die gesperrt sind, in Benutzung sind oder Berechtigungsprobleme aufweisen.
  - Es defekte Symlinks, offene Dateihandles (z.B. von einem laufenden `claude`-Prozess) oder Dateisystem-Anomalien unter Linux gibt.
  - In seltenen Fällen tritt eine Race Condition in npm's interner Move-File-Logik auf.

Ihr Setup:
- Node: v22.18.0
- npm: v11.6.1
- OS: Linux 6.14.0-29-generic (wahrscheinlich Ubuntu/Debian)
- Läuft als root (basierend auf dem Log-Pfad `/root/.npm/_logs/`), daher sind Berechtigungen nicht die Ursache.
- Arbeitsverzeichnis: `/home/lzwjava/projects/blog-source` (aber dies ist eine globale Installation, also irrelevant).

Bei dem Paket scheint es sich um Anthropics Claude Code Tool zu handeln (CLI für KI-Coding-Unterstützung), und Zeile 73 zeigt eine Abhängigkeits-Warnung für `@img/sharp-libvips-linux-x64` an, aber das ist nicht mit dem Absturz verbunden.

### Schnelle Lösungen (In dieser Reihenfolge versuchen)

1. **Laufende Prozesse beenden**:
   - Beenden Sie alle `claude`-CLI oder verwandten Prozesse: `pkill claude` (oder `ps aux | grep claude` um PIDs zu finden, dann `kill <PID>`).
   - Schließen Sie Terminals/IDEs, die das Paket verwenden.

2. **Verzeichnis manuell bereinigen**:
   - Entfernen Sie das vorhandene Paket und das Binary:
     ```
     sudo rm -rf /usr/lib/node_modules/@anthropic-ai/claude-code
     sudo rm -f /usr/bin/claude
     ```
   - Dies umgeht den npm-Backup-Schritt. Versuchen Sie dann die Installation erneut:
     ```
     sudo npm install -g @anthropic-ai/claude-code
     ```

3. **npm-Cache leeren und erneut versuchen**:
   - Führen Sie aus:
     ```
     sudo npm cache clean --force
     sudo npm install -g @anthropic-ai/claude-code
     ```
   - Wenn das Problem bestehen bleibt, fügen Sie `--no-optional` hinzu, um optionale Abhängigkeiten wie die Sharp-Image-Bibliothek zu überspringen.

4. **Alternative: npx verwenden oder globale Installation vermeiden**:
   - Wenn Sie es nicht global benötigen, installieren Sie es lokal in Ihrem Projekt: `npm install @anthropic-ai/claude-code` (dann ausführen via `npx claude`).
   - Oder verwenden Sie Yarn: `sudo yarn global add @anthropic-ai/claude-code` (Yarn handhabt Verschiebungen manchmal anders).

5. **Wenn immer noch fehlerhaft**:
   - Überprüfen Sie auf Dateisystemprobleme: `ls -la /usr/lib/node_modules/@anthropic-ai/` (nach seltsamen Symlinks oder Sperren suchen).
   - npm vorübergehend downgraden: `sudo npm install -g npm@10` (v11 hat gelegentliche Reify-Bugs; danach zurücksetzen).
   - Vollständiges Log: Überprüfen Sie `/root/.npm/_logs/2025-10-27T16_10_10_534Z-debug-0.log` für mehr Hinweise.

Dies sollte das Problem beheben – npm-Globalinstallationen unter Linux können bei Umbenennungen empfindlich sein. Wenn Sie den exakten Befehl, den Sie ausgeführt haben, oder mehr Log-Kontext teilen, kann ich dies verfeinern.