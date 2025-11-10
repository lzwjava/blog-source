---
audio: false
generated: true
image: false
lang: de
layout: post
title: 'Schwarz: Python Code Formatierer Leitfaden'
translated: true
type: note
---

Black ist ein meinungsstarker, kompromissloser Python-Code-Formatierer, der von der Python Software Foundation (PSF) entwickelt wurde. Er formatiert Python-Code automatisch so um, dass er einem einheitlichen Stil entspricht, der hauptsächlich auf einer strikten Teilmenge von PEP 8 basiert, und legt dabei Wert auf Lesbarkeit, Konsistenz und minimale Diffs in der Versionskontrolle. Durch die Verwendung von Black erklären sich Entwickler damit einverstanden, die Kontrolle über kleinere Formatierungsdetails im Austausch für Geschwindigkeit, Determinismus und weniger Debatten über Stil während Code-Reviews abzugeben. Black stellt sicher, dass formatierter ("geschwärzter") Code in verschiedenen Projekten einheitlich aussieht, und spart so Zeit und mentale Energie für wichtigere Aspekte der Entwicklung. Es unterstützt Python 3.8 und höher, wobei die neueste stabile Version 25.1.0 ist (veröffentlicht am 29. Januar 2025), die den 2025 Stable Style mit Verbesserungen wie normalisierter Unicode-Escape-Schreibweise und besserer Handhabung von nachgestellten Kommas einführt.

Die Philosophie von Black priorisiert:
- **Konsistenz**: Ähnliche Konstrukte werden identisch formatiert.
- **Allgemeingültigkeit**: Regeln gelten weitgehend ohne Sonderfälle.
- **Lesbarkeit**: Fokus auf einfach lesbaren Code.
- **Diff-Minimierung**: Reduziert Änderungen in Git-Diffs, um Reviews zu beschleunigen.

Aufgrund seiner Zuverlässigkeit und Integrationsfähigkeiten wird es weit verbreitet in Open-Source- und professionellen Projekten eingesetzt.

## Installation

Black ist auf PyPI verfügbar und kann mit pip installiert werden. Es wird empfohlen, es in einer virtuellen Umgebung zu installieren, um Projekte zu isolieren.

- Grundinstallation:
  ```
  pip install black
  ```

- Für zusätzliche Funktionen wie Jupyter Notebook-Unterstützung oder farbige Diffs:
  ```
  pip install 'black[jupyter,colorama]'
  ```
  (Das `d`-Extra ist für blackd, einen Daemon für Editor-Integrationen.)

Auf Arch Linux kann es über den Paketmanager installiert werden: `pacman -S python-black`.

Black kann auch via conda oder andere Paketmanager installiert werden. Nach der Installation mit `black --version` verifizieren.

Für Entwicklung oder Tests kann das GitHub-Repository geklont und im editierbaren Modus installiert werden:
```
git clone https://github.com/psf/black.git
cd black
pip install -e .
```

## Verwendung

Black ist in erster Linie ein Kommandozeilen-Tool. Der grundlegende Befehl formatiert Dateien oder Verzeichnisse direkt:

```
black {quelldatei_oder_verzeichnis}
```

Falls das Ausführen von Black als Skript nicht funktioniert (z.B. aufgrund von Umgebungsproblemen), verwenden:
```
python -m black {quelldatei_oder_verzeichnis}
```

### Wichtige Kommandozeilen-Optionen

Black bietet verschiedene Flags zur Anpassung und Kontrolle. Hier eine Zusammenfassung der wichtigsten:

- `-h, --help`: Hilfe anzeigen und beenden.
- `-c, --code <code>`: Einen Code-String formatieren (z.B. gibt `black --code "print ( 'hello, world' )"` die formatierte Version aus).
- `-l, --line-length <int>`: Zeilenlänge setzen (Standard: 88).
- `-t, --target-version <version>`: Python-Versionen für Kompatibilität angeben (z.B. `py38`, mehrfach möglich wie `-t py311 -t py312`).
- `--pyi`: Dateien als Typing-Stubs behandeln (`.pyi`-Stil).
- `--ipynb`: Dateien als Jupyter Notebooks behandeln.
- `--python-cell-magics <magic>`: Benutzerdefinierte Jupyter-Magics erkennen.
- `-x, --skip-source-first-line`: Erste Zeile nicht formatieren (nützlich für Shebangs).
- `-S, --skip-string-normalization`: Strings nicht auf doppelte Anführungszeichen oder Präfixe normalisieren.
- `-C, --skip-magic-trailing-comma`: Nachgestellte Kommas für Zeilenumbrüche ignorieren.
- `--preview`: Experimentelle Stiländerungen für die nächste Version aktivieren.
- `--unstable`: Alle Preview-Änderungen plus instabile Funktionen aktivieren (erfordert `--preview`).
- `--enable-unstable-feature <feature>`: Bestimmte instabile Funktionen aktivieren.
- `--check`: Prüfen, ob Dateien Neuformatierung benötigen, ohne sie zu ändern (Exit-Code 1, wenn Änderungen nötig).
- `--diff`: Diff der Änderungen anzeigen, ohne Dateien zu schreiben.
- `--color / --no-color`: Diff-Ausgabe einfärben.
- `--line-ranges <ranges>`: Bestimmte Zeilenbereiche formatieren (z.B. `--line-ranges=1-10`).
- `--fast / --safe`: AST-Sicherheitsprüfungen überspringen (`--fast`) oder erzwingen (`--safe`) (Standard: safe).
- `--required-version <version>`: Bestimmte Black-Version voraussetzen.
- `--exclude <regex>`: Dateien/Verzeichnisse per Regex ausschließen.
- `--extend-exclude <regex>`: Zu Standard-Ausschlüssen hinzufügen.
- `--force-exclude <regex>`: Ausschließen, auch wenn explizit übergeben.
- `--include <regex>`: Dateien/Verzeichnisse per Regex einschließen.
- `-W, --workers <int>`: Anzahl paralleler Worker setzen (Standard: CPU-Anzahl).
- `-q, --quiet`: Nicht-Fehlermeldungen unterdrücken.
- `-v, --verbose`: Detaillierte Ausgabe anzeigen.
- `--version`: Black-Version anzeigen.
- `--config <file>`: Konfiguration aus einer Datei laden.

### Beispiele

- Einzelne Datei formatieren: `black example.py`
- Ohne Formatierung prüfen: `black --check .`
- Diff anzeigen: `black --diff example.py`
- Stdin formatieren: `echo "print('hello')" | black -`
- Mit benutzerdefinierter Zeilenlänge formatieren: `black -l 79 example.py`
- Jupyter Notebook formatieren: `black notebook.ipynb`

### Tipps und Hinweise

- Black formatiert gesamte Dateien; verwende `# fmt: off` / `# fmt: on` zum Überspringen von Blöcken oder `# fmt: skip` für Zeilen.
- Für Stdin `--stdin-filename` verwenden, um Ausschlüsse zu respektieren.
- Black ist deterministisch: Gleiche Eingabe ergibt immer gleiche Ausgabe.
- `--preview` verwenden, um kommende Stile zu testen, beachte aber, dass sie sich ändern können.

## Konfiguration

Black kann über Kommandozeilen-Flags oder eine `pyproject.toml`-Datei (bevorzugt für Projekte) konfiguriert werden. Die Konfiguration in `pyproject.toml` erfolgt in einem Abschnitt `[tool.black]`.

### pyproject.toml verwenden

Beispiel:
```
[tool.black]
line-length = 79
target-version = ['py311']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
skip-string-normalization = true
```

Unterstützte Optionen spiegeln CLI-Flags wider (z.B. `line-length`, `skip-string-normalization`). Mehrfachwert-Optionen wie `target-version` verwenden Arrays.

### Reihenfolge

- Kommandozeilen-Flags überschreiben Konfigurationsdatei-Einstellungen.
- Wenn keine `pyproject.toml` gefunden wird, verwendet Black Standardwerte und durchsucht übergeordnete Verzeichnisse.
- `--config` verwenden, um eine benutzerdefinierte Konfigurationsdatei anzugeben.

### Datei-Erkennung und Ignorieren

Black erkennt Python-Dateien in Verzeichnissen automatisch und respektiert standardmäßig `.gitignore`. Verwende `--include`/`--exclude` zur Anpassung. Es ignoriert gemeinsame Verzeichnisse wie `.git`, `.venv` usw., sofern nicht überschrieben.

Für die Versionskontrolle mit Tools wie pre-commit integrieren, um Formatierung durchzusetzen.

## Der Black-Code-Stil

Black erzwingt einen bestimmten Stil mit begrenzter Konfigurierbarkeit. Wichtige Regeln:

### Zeilenlänge
- Standard: 88 Zeichen. Kann überschritten werden, wenn unbrechbar (z.B. lange Strings).

### Strings
- Bevorzugt doppelte Anführungszeichen; normalisiert Präfixe zu Kleinbuchstaben (z.B. `r` vor `f`).
- Wandelt Escape-Sequenzen in Kleinbuchstaben um (außer `\N`-Namen).
- Verarbeitet Docstrings: Korrigiert Einrückung, entfernt zusätzliche Leerzeichen/Zeilenumbrüche, erhält Tabs im Text.

### Numerische Literale
- Kleinbuchstaben für syntaktische Teile (z.B. `0xAB`), Großbuchstaben für Ziffern.

### Zeilenumbrüche und Operatoren
- Umbrüche vor binären Operatoren.
- Einfache Leerzeichen um die meisten Operatoren; keine Leerzeichen für unäre/Potenz mit einfachen Operanden.

### Nachgestellte Kommas
- Fügt sie zu mehrzeiligen Sammlungen/Funktionsargumenten hinzu (wenn Python 3.6+).
- "Magisches" nachgestelltes Komma explodiert Listen, wenn vorhanden.

### Kommentare
- Zwei Leerzeichen vor Inline-Kommentaren; ein Leerzeichen vor Text.
- Erhält speziellen Abstand für Shebangs, Doc-Kommentare usw.

### Einrückung
- 4 Leerzeichen; passt Klammern mit de-eingerückten Schließern ab.

### Leere Zeilen
- Minimaler Leerraum: Einfach in Funktionen, Doppelt auf Modulebene.
- Spezifische Regeln für Docstrings, Klassen und Funktionen.

### Importe
- Teilt lange Importe auf; kompatibel mit isorts `black`-Profil.

### Andere Regeln
- Bevorzugt Klammern gegenüber Backslashes.
- Normalisiert Zeilenenden basierend auf Datei.
- Knapper Stil für `.pyi`-Dateien (z.B. keine zusätzlichen Zeilen zwischen Methoden).
- Reduziert leere Zeilen nach Importen im Preview-Modus.

Black zielt darauf ab, Diffs zu reduzieren und die Lesbarkeit zu verbessern, mit Änderungen hauptsächlich für Fehlerbehebungen oder neue Syntaxunterstützung.

## Integrationen

Black integriert sich nahtlos in Editoren und Versionskontrolle für automatisierte Formatierung.

### Editoren

- **VS Code**: Verwende die Python-Erweiterung mit Black als Formatierer. Setze `"python.formatting.provider": "black"` in settings.json. Für LSP, installiere python-lsp-server und python-lsp-black.
- **PyCharm/IntelliJ**:
  - Eingebaut (2023.2+): Einstellungen > Tools > Black, Pfad konfigurieren.
  - Externes Tool: Einstellungen > Tools > Externe Tools, Black mit `$FilePath$`-Argument hinzufügen.
  - File Watcher: Für Auto-Formatierung beim Speichern.
  - BlackConnect-Plugin für Daemon-basierte Formatierung.
- **Vim**: Verwende das offizielle Plugin (via vim-plug: `Plug 'psf/black', { 'branch': 'stable' }`). Befehle: `:Black` zum Formatieren. Auto-Speichern: Autocmd zur vimrc hinzufügen. Konfigurationsvariablen wie `g:black_linelength`.
- **Emacs**: Verwende reformatter.el oder python-black-Paket für Formatierung beim Speichern.
- **Andere**: Unterstützt Sublime Text, JupyterLab, Spyder usw. via Plugins oder Erweiterungen.

### Versionskontrolle

- **Pre-commit Hooks**: Zu `.pre-commit-config.yaml` hinzufügen:
  ```
  repos:
    - repo: https://github.com/psf/black-pre-commit-mirror
      rev: 25.1.0
      hooks:
        - id: black
          language_version: python3.11
  ```
  Für Jupyter: Verwende `id: black-jupyter`.
- **GitHub Actions**: Verwende Actions wie `psf/black-action` in Workflows für CI-Checks.
- **Git**: Führe Black in Pre-commit-Skripts oder husky zur Durchsetzung aus.

## Fortgeschrittene Themen

- **Preview und Instabile Stile**: Verwende `--preview` für zukünftige Änderungen (z.B. bessere Klammerumarmung). `--unstable` für experimentelle Funktionen.
- **Blackd**: HTTP-Server für Integrationen (`blackd --bind-host 127.0.0.1 --bind-port 45484`).
- **Jupyter-Unterstützung**: Formatiert Notebooks und erhält Magics.
- **Typing-Stubs**: Spezielle knappe Formatierung für `.pyi`-Dateien.
- **Kompatibilität**: Ziel ist Python 3.8+; verwende `--target-version` für älteren Code.
- **Alternativen**: Verglichen mit autopep8 (flexibler, aber weniger meinungsstark) oder Ruff (schneller, inklusive Linting).

Für die Fehlerbehebung, siehe FAQ in der offiziellen Dokumentation oder GitHub-Issues.

## Referenzen

- [Black 25.1.0 Dokumentation](https://black.readthedocs.io/en/stable/)
- [psf/black GitHub Repository](https://github.com/psf/black)
- [The Black Code Style](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)
- [Usage and Configuration](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html)
- [Editor Integrations](https://black.readthedocs.io/en/stable/integrations/editors.html)
- [Version Control Integration](https://black.readthedocs.io/en/stable/integrations/source_version_control.html)
- [Python Code Formatting Using Black - GeeksforGeeks](https://www.geeksforgeeks.org/python/python-code-formatting-using-black/)
- [How to Auto-Format Your Python Code with Black - freeCodeCamp](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)
- [Black - PyPI](https://pypi.org/project/black/)
- [Introduction to Python Black Module - GeeksforGeeks](https://www.geeksforgeeks.org/introduction-to-python-black-module/)
- [Python Auto Formatter: Autopep8 vs. Black - Built In](https://builtin.com/data-science/autopep8-vs-black)