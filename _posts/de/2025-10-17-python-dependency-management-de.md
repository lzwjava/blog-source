---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Abhängigkeitsverwaltung für Python mit Poetry
translated: true
type: note
---

### Was ist Poetry?

Poetry ist ein Tool für Dependency Management und Packaging in Python. Es ermöglicht Ihnen, die Bibliotheken, von denen Ihr Projekt abhängt, zu deklarieren, und kümmert sich automatisch um deren Installation, Aktualisierung und Auflösung, während es reproduzierbare Umgebungen sicherstellt.

### Hauptzweck
Poetry vereinfacht Python-Projekt-Workflows, indem es Abhängigkeiten über eine einzige Konfigurationsdatei (`pyproject.toml`) verwaltet, eine Lockdatei für konsistente Installationen auf verschiedenen Rechnern erstellt und den Build von Projekten für die Distribution (z.B. zu PyPI) unterstützt. Es wurde entwickelt, um fragmentierte Tools wie `pip`, `pipenv` und `setuptools` durch einen einheitlichen, benutzerfreundlichen Ansatz zu ersetzen.

### Hauptfunktionen
- **Dependency Resolution**: Installiert und aktualisiert Abhängigkeiten automatisch und löst Konflikte intelligent.
- **Lockfile**: Erzeugt `poetry.lock`, um exakte Versionen für wiederholbare Builds festzuhalten.
- **Virtuelle Umgebungen**: Erstellt isolierte Umgebungen pro Projekt, um globale Verschmutzung zu vermeiden.
- **Packaging**: Baut Wheels oder sdists für einfache Distribution.
- **Multi-Plattform-Unterstützung**: Funktioniert unter Linux, macOS und Windows.
- **Shell-Integration**: Tab-Completion für Bash, Fish und Zsh.
- **Python 3.9+ Kompatibel**: Erfordert moderne Python-Versionen.

### Installation
Installieren Sie Poetry in einer isolierten Umgebung mit `pipx` (empfohlen für globalen Zugriff ohne Konflikte):

1. Installieren Sie `pipx`, falls benötigt (über Ihren OS-Paketmanager oder `python -m pip install --user pipx`).
2. Führen Sie aus: `pipx install poetry`.

Für Updates: `pipx upgrade poetry`.  
Für Deinstallation: `pipx uninstall poetry`.

Aktivieren Sie Shell-Completions (z.B. für Bash: `poetry completions bash >> ~/.bash_completion`).

### Grundlegende Verwendung
Initialisieren Sie ein neues Projekt: `poetry init`.  
Fügen Sie eine Abhängigkeit hinzu: `poetry add requests`.  
Installieren Sie aus einer Lockdatei: `poetry install`.  
Führen Sie Skripte aus: `poetry run python script.py`.  
Bauen Sie ein Package: `poetry build`.

Für alle Befehle, lesen Sie die Dokumentation.

[Poetry-Dokumentation](https://python-poetry.org/docs/)