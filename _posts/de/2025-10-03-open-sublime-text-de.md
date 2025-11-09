---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Sublime Text über die Befehlszeile öffnen
translated: true
type: note
---

### Sublime Text über die Befehlszeile (CLI) öffnen

Sublime Text enthält standardmäßig keinen `sublime`- (oder `subl`-) Befehl unter macOS (was du, basierend auf der `open -a`-Referenz, anscheinend verwendest). Es gibt jedoch eine offizielle und einfache Möglichkeit, ihn mit dem mitgelieferten `subl`-Skript von Sublime hinzuzufügen. Dies ist sauberer, als sich auf den `open`-Befehl zu verlassen. Ich werde dir unten die Optionen erklären, beginnend mit der empfohlenen Vorgehensweise.

#### 1. **Installiere den offiziellen `subl` CLI-Befehl (Empfohlen)**
Sublime Text enthält eine `subl`-Executable in seinem App-Bundle, die du in ein Verzeichnis in deinem PATH (wie `/usr/local/bin`) symlinken kannst. Dies ermöglicht es dir, `subl .` (um das aktuelle Verzeichnis zu öffnen) oder `subl datei.txt` von überall im Terminal aus auszuführen.

**Schritte für macOS (Sublime Text 3 oder 4):**
- Öffne das Terminal.
- Führe diesen Befehl aus, um den Symlink zu erstellen (erfordert Admin-Rechte, du wirst nach deinem Passwort gefragt):
  ```
  sudo ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl
  ```
  - Wenn du Sublime Text 3 verwendest, könnte der Pfad leicht abweichen: `"/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl"` (passe die Versionsnummer nach Bedarf an).
  - Wenn `/usr/local/bin` nicht in deinem PATH enthalten ist, füge es zu deinem Shell-Profil hinzu (z.B. `~/.zshrc` oder `~/.bash_profile`):
    ```
    echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```

- Teste es: Wechsle in ein Verzeichnis (z.B. `cd ~/Desktop`) und führe aus:
  ```
  subl .
  ```
  Dies sollte Sublime Text mit dem aktuellen Ordner öffnen.

Falls der Symlink-Pfad nicht funktioniert (z.B. aufgrund von Versionsunterschieden), überprüfe den genauen Ort:
- Führe `find /Applications/Sublime\ Text.app -name subl` aus, um die Binary zu finden.

**Warum das gut ist:**
- Es ist offiziell und leichtgewichtig – keine Tools von Drittanbietern nötig.
- Funktioniert systemweit, wie eine echte CLI.
- Sublime Text 4 hat sogar eine Option in der Konsole (View > Show Console), um `sublime_installation` oder ähnliches auszuführen, aber der Symlink ist die zuverlässigste Methode.

**Falls du Linux oder Windows verwendest:**
- Linux: Ähnlicher Symlink-Prozess – z.B. `sudo ln -s /opt/sublime_text/sublime_text /usr/local/bin/subl`.
- Windows: Füge `C:\Program Files\Sublime Text\sublime_text.exe` zu deinem PATH hinzu oder verwende eine Batch-Datei für `subl`.

#### 2. **Fallback: Verwende den `open`-Befehl (Keine Installation nötig)**
Wenn du nicht mit Symlinks oder dem PATH herumhantieren möchtest, funktioniert der in macOS integrierte `open`-Befehl gut für die grundlegende Verwendung. Er ist bereits überall verfügbar.

- Um das aktuelle Verzeichnis in Sublime zu öffnen:
  ```
  open -a "Sublime Text" .
  ```
  - Hinweis: Verwende `"Sublime Text"` (mit Leerzeichen), wenn das dein App-Name ist. Wenn es nur "Sublime.app" heißt, passe es entsprechend an. Du kannst den genauen Namen in `/Applications/` überprüfen.

- Um eine bestimmte Datei zu öffnen:
  ```
  open -a "Sublime Text" dateiname.txt
  ```

- Erstelle einen Alias für Bequemlichkeit: Füge dies zu deinem Shell-Profil (`~/.zshrc` oder `~/.bash_profile`) hinzu, um `subl` nachzuahmen:
  ```
  alias subl='open -a "Sublime Text"'
  ```
  Danach mit `source ~/.zshrc` neu laden und `subl .` wie gewohnt verwenden.

**Vor-/Nachteile:**
- Sehr einfach und kein Setup nötig.
- Aber es ist nur für macOS und weniger flexibel (z.B. keine einfache Möglichkeit, Zeilen oder Projekte wie mit `subl` anzugeben).

#### Problembehebung
- **Befehl nicht gefunden?** Stelle sicher, dass dein PATH `/usr/local/bin` enthält (führe `echo $PATH` aus, um es zu überprüfen).
- **App nicht gefunden?** Überprüfe, ob sich Sublime in `/Applications/` befindet. Wenn es woanders ist (z.B. über Homebrew: `brew install --cask sublime-text`), passe die Pfade an.
- **Berechtigungsprobleme?** Der Symlink benötigt sudo, aber sobald er gesetzt ist, funktioniert er.
- Wenn du einen Paketmanager wie Homebrew verwendest, kannst du Sublime via `brew install --cask sublime-text` installieren, und er kümmert sich möglicherweise um die CLI für dich.

Das sollte dich gut zum Laufen bringen! Wenn du auf Fehler stößt oder dein OS/Version spezifizierst, kann ich die Schritte verfeinern.