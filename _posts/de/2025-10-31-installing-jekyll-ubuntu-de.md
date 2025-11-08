---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Jekyll unter Ubuntu installieren
translated: true
type: note
---

### Einrichtung und Ausführung von Jekyll auf Ubuntu

Basierend auf Ihrem Fehler ("Command 'bundle' not found") und den Befehlen, die Sie ausführen möchten, sieht es so aus, als müssten Sie Ruby, Bundler und Jekyll zunächst ordnungsgemäß installieren. Ubuntu wird nicht mit diesen Komponenten ausgeliefert, aber die Einrichtung ist unkompliziert, wenn Sie der offiziellen Jekyll-Anleitung folgen. Ich werde Sie Schritt für Schritt durch die vollständige Einrichtung führen und anschließend erklären, wie Sie Ihre spezifischen Befehle ausführen.

#### Schritt 1: Systemabhängigkeiten installieren
Öffnen Sie Ihr Terminal und führen Sie dies aus, um Ruby und Build-Tools zu installieren (dies beinhaltet Ruby 3.x via `ruby-full`):

```bash
sudo apt update
sudo apt install ruby-full build-essential zlib1g-dev
```

- Damit wird Ruby eingerichtet (überprüfen Sie mit `ruby -v` – es sollte etwas wie 3.0+ angezeigt werden).
- Wenn Sie ein aktuelles Ubuntu (z.B. 22.04+) verwenden, funktioniert dies sofort. Vermeiden Sie nach Möglichkeit die Installation von Ruby via Snap, da dies zu Pfadproblemen führen kann.

#### Schritt 2: Ein Benutzer-Gem-Verzeichnis einrichten (Empfohlen, um Sudo zu vermeiden)
Um Gems ohne Root-Berechtigungen zu installieren (verhindert später Berechtigungsfehler):

```bash
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

- Überprüfung: Führen Sie `gem env` aus – es sollte Ihr `GEM_HOME` als `~/gems` anzeigen.

#### Schritt 3: Jekyll und Bundler installieren
Installieren Sie nun die Tools:

```bash
gem install jekyll bundler
```

- Dies fügt die Befehle `gem`, `jekyll` und `bundle` zu Ihrem Pfad hinzu.
- Wenn Sie Berechtigungsfehler erhalten, überprüfen Sie Schritt 2 oder verwenden Sie vorübergehend `sudo` (vermeiden Sie dies jedoch langfristig).

#### Schritt 4: Ihr Blog erstellen und ausführen
Jetzt können Sie die Befehle aus Ihrem Snippet ausführen. Ich erkläre jeden einzelnen:

1. **Eine neue Jekyll-Seite erstellen**:
   ```bash
   jekyll new myblog
   ```
   - Dies erzeugt eine grundlegende Seite in einem Ordner `myblog`.

2. **In das Verzeichnis wechseln**:
   ```bash
   cd myblog
   ```

3. **Abhängigkeiten installieren** (hier ist Ihr ursprünglicher `bundle install` Befehl fehlgeschlagen – jetzt sollte er funktionieren):
   ```bash
   bundle install
   ```
   - Lädt Gems wie Jekyll-Plugins herunter.

4. **Die Seite bereitstellen** (startet einen lokalen Server unter http://127.0.0.1:4000):
   ```bash
   bundle exec jekyll serve
   ```
   - Öffnen Sie Ihren Browser mit dieser URL, um Ihre Seite zu sehen.

5. **Mit inkrementellen Neubuilds bereitstellen** (schneller für die Entwicklung, baut nur geänderte Dateien neu auf):
   ```bash
   bundle exec jekyll serve --incremental
   ```

6. **Inklusive Entwürfe bereitstellen** (zeigt unveröffentlichte Beiträge an):
   ```bash
   bundle exec jekyll serve --draft
   ```

7. **Wenn Sie einen "webrick"-Fehler erhalten** (häufig bei Ruby 3+, da es nicht standardmäßig gebündelt ist):
   ```bash
   bundle add webrick
   ```
   - Starten Sie dann den Serve-Befehl neu: `bundle exec jekyll serve`.
   - Alternativ fügen Sie `gem "webrick"` zu Ihrer `Gemfile` hinzu und führen `bundle install` aus.

8. **Schnelles Bereitstellen ohne Bundler** (wenn Sie `bundle exec` weglassen):
   ```bash
   jekyll serve
   ```
   - Verwenden Sie jedoch für die Konsistenz in Projekten `bundle exec`.

#### Problembehandlung
- **Immer noch "bundle not found"?** Stellen Sie sicher, dass Schritt 2 Ihre `~/.bashrc` korrekt eingelesen hat (`source ~/.bashrc`), starten Sie Ihr Terminal neu oder führen Sie `hash -r` aus. Überprüfen Sie mit `which bundle`.
- **Berechtigungsprobleme mit Gems?** Bleiben Sie bei der Benutzerverzeichniseinrichtung aus Schritt 2.
- **Ruby-Version zu alt?** Wenn `ruby -v` <3.0 anzeigt, ziehen Sie die Verwendung von rbenv für eine neuere Version in Betracht (Installation via `curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash`, dann `rbenv install 3.2.0`).
- **Blockiert die Firewall Port 4000?** Ubuntu blockiert ihn normalerweise nicht, aber testen Sie mit `curl http://127.0.0.1:4000`.
- Ihr Projekt befindet sich in `~/projects/blog-source` – führen Sie diese Befehle von dort aus oder passen Sie die Pfade an.

Sobald die Seite bereitgestellt ist, bearbeiten Sie Dateien in `_posts/` oder `_config.yml` und speichern Sie – Jekyll baut automatisch neu auf. Für die Produktion bauen Sie mit `jekyll build` und deployen auf GitHub Pages oder Netlify.

[Jekyll Ubuntu Installation Guide](https://jekyllrb.com/docs/installation/ubuntu/)