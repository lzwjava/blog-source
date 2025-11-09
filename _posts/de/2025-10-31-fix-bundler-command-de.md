---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Bundler-Befehl nicht gefunden
translated: true
type: note
---

### Behebung des "Bundler-Befehl nicht gefunden" Fehlers

Wenn Sie den Fehler "bundler: command not found" erhalten, haben Sie wahrscheinlich Bundler nicht richtig installiert oder es ist nicht in Ihrem PATH verfügbar.

#### Lösung

```bash
# Für rbenv/Ruby-Benutzer:
rbenv rehash

# Für RVM-Benutzer:
rvm reload

# Oder aktualisieren Sie die Shell-Konfiguration:
source ~/.bashrc
# oder
source ~/.zshrc
```

#### Überprüfen der Installation

```bash
# Überprüfen Sie die Bundler-Version:
bundler --version

# Testen Sie mit einem Projekt:
cd /path/to/your/project
bundle install
```

#### Zusätzliche Hinweise

- Stellen Sie sicher, dass Ihre Ruby-Umgebung richtig konfigured ist
- Verwenden Sie `gem install bundler` falls Bundler nicht installiert ist
- Nach der Installation sollten Sie `rbenv rehash` ausführen