---
audio: false
generated: true
image: false
lang: de
layout: post
title: Python Coverage Guide Essentials
translated: true
type: note
---

Hier ist eine praktische, entwicklerorientierte Einführung in das **Coverage**-Paket (coverage.py) – was es misst, wie man es effektiv nutzt und die Einstellungen, die tatsächlich relevant sind.

# Was coverage.py ist

* Ein Python-Tool, das **misst, welche Zeilen und Branches Ihres Codes** während Tests oder beliebigen Ausführungen **laufen**.
* Erstellt **Text-, HTML-, XML- und JSON-Berichte**, damit Sie Lücken erkennen und es in CI-Qualitätsgates integrieren können.
* Funktioniert mit unittest, pytest, nose oder einfachen Skripten.

# Kernkonzepte (einfach erklärt)

* **Zeilenabdeckung (Line Coverage)**: Wurde eine Zeile mindestens einmal ausgeführt?
* **Zweigabdeckung (Branch Coverage)**: Wurde jeder mögliche Pfad einer Entscheidung ausgeführt? (if/else, Boolean Short-Circuit, Exceptions, Comprehensions, etc.)
* **Quellauswahl (Source Selection)**: Messen Sie nur Ihren eigenen Code, um Störungen durch venv/site-packages zu vermeiden.
* **Datenspeicherung (Data Storage)**: Durchläufe erstellen eine `.coverage` (SQLite) Datendatei; Sie können viele Durchläufe zusammenführen.
* **Kontexte (Contexts)**: Versehen Sie die Ausführung mit Labels (z.B. pro Test), um Berichte nach Testnamen, Befehlen etc. aufschlüsseln zu können.

# Schnellstart

```bash
# 1) Installieren
pip install coverage

# 2) Führen Sie Ihre Tests unter coverage aus (pytest ist nur ein Beispiel)
coverage run -m pytest

# 3) Sehen Sie einen Terminalbericht (mit fehlenden Zeilennummern)
coverage report -m

# 4) Generieren Sie HTML (öffnen Sie htmlcov/index.html im Browser)
coverage html

# Optional: Maschinenlesbare Berichte
coverage xml        # für CI-Tools wie Sonar, Jenkins, Azure DevOps
coverage json       # für scriptgesteuerte Analysen
```

# Empfohlene .coveragerc

Erstellen Sie eine Konfiguration im Stammverzeichnis Ihres Repositories, um Ergebnisse lokal und in CI konsistent zu halten.

```ini
[run]
# Messen Sie nur Ihre eigenen Pakete, um Störungen zu reduzieren
source = src, your_package
branch = True
parallel = True                 # Ermöglicht mehreren Prozessen/Durchläufen, eigene Daten zu schreiben
relative_files = True           # Sauberere Pfade in Berichten (CI-freundlich)
concurrency = thread, multiprocessing

# Sie können auch Dateien oder Muster komplett ausschließen
omit =
    */tests/*
    */.venv/*
    */site-packages/*
    */migrations/*

[report]
show_missing = True
skip_covered = False            # Auf True setzen, wenn Sie einen kürzeren Bericht wünschen
fail_under = 90                 # Lässt CI fehlschlagen, wenn die Abdeckung unter 90% liegt
exclude_lines =
    pragma: no cover            # Standard-Pragma, um Zeilen zu ignorieren
    if TYPE_CHECKING:
    raise NotImplementedError

[html]
directory = htmlcov
title = Coverage Report

[xml]
output = coverage.xml

[json]
output = coverage.json

[paths]
# Nützlich beim Kombinieren von Daten von verschiedenen Maschinen/Containern
source =
    src
    */workspace/src
    */checkouts/your_repo/src
```

# Messen von Subprozessen & parallelen Durchläufen

Falls Ihr Code Subprozesse startet (multiprocessing, CLI-Tools), richten Sie **Subprozess-Coverage** ein:

1. In `[run]` belassen Sie `parallel = True`.
2. Exportieren Sie eine Umgebungsvariable, damit Subprozesse Coverage automatisch mit derselben Konfiguration starten:

```bash
export COVERAGE_PROCESS_START=$(pwd)/.coveragerc
```

3. Führen Sie Ihr Programm/Tests normal aus (oder weiterhin via `coverage run -m ...`).
4. Nachdem alle Durchläufe beendet sind, Daten zusammenführen und Bericht erstellen:

```bash
coverage combine
coverage report -m
```

> Tipp: `concurrency = multiprocessing, thread, gevent, eventlet, greenlet` ermöglicht es Coverage, sich in verschiedene Async-Modelle einzuhängen.

# Zweigabdeckung & Pragmas

* Aktivieren Sie `branch = True` in `[run]`. Dies erfasst verpasste `else`-Zweige, Short-Circuits, Exception-Pfade etc.
* Ignorieren Sie nicht testbare Zeilen mit einem nachgestellten Kommentar:

  * `# pragma: no cover` – schließt diese Zeile von der Abdeckungsmessung aus.
  * Für knifflige Zweige: Refaktorisieren Sie, anstatt Pragmas übermäßig zu verwenden.

# Kontexte (Abdeckung nach Test oder Aufgabe aufschlüsseln)

Kontexte heften Labels an ausgeführte Zeilen, sodass Sie fragen können: "Welche Tests decken diesen Code ab?"

* Am einfachsten mit pytest:

  * In `.coveragerc` fügen Sie `dynamic_context = test_function` hinzu.
  * Dann `coverage html --show-contexts` oder inspizieren Sie die Daten pro Kontext, um zu sehen, welcher Test eine Zeile berührt hat.
* Sie können auch `dynamic_context = test` (Test Nodeid) setzen oder `dynacontext` via Env-Variable in benutzerdefinierten Runnern.

# Pytest-Integration

Zwei gängige Muster:

**A. Native Coverage-CLI (einfach & schnell)**

```bash
coverage run -m pytest -q
coverage report -m
```

**B. pytest-cov Plugin (fügt CLI-Sugar hinzu)**

```bash
pip install pytest-cov
pytest --cov=your_package --cov-branch --cov-report=term-missing --cov-report=html
```

Beide nutzen letztendlich coverage.py im Hintergrund; verwenden Sie, was den Konventionen Ihres Teams entspricht.

# Typische CI-Anbindung (GitHub Actions Skizze)

```yaml
- name: Installieren
  run: pip install -U pip coverage pytest

- name: Test mit Coverage
  run: |
    coverage run -m pytest -q
    coverage report -m
    coverage xml
- name: Schwellenwert durchsetzen
  run: coverage report --fail-under=90
- name: HTML hochladen
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: htmlcov
    path: htmlcov/
```

# Häufige Fallstricke & Lösungen

* **Riesige/langsame Berichte**: Beschränken Sie `source=` und verwenden Sie `omit=`, um venv, Tests, generierten Code zu überspringen.
* **Verschiedene Pfade auf CI vs. lokal**: Fügen Sie einen `[paths]`-Abschnitt hinzu, damit `coverage combine` Datensätze zusammenführt.
* **Subprozesse werden nicht gemessen**: Setzen Sie `COVERAGE_PROCESS_START` und belassen Sie `parallel = True`, dann `coverage combine`.
* **Async-Frameworks**: Fügen Sie den relevanten Eintrag zu `concurrency = ...` hinzu.
* **C-Erweiterungen**: coverage.py misst Python, nicht nativen Code – schreiben Sie Hüllentests um die Python-Schnittstelle.
* **Falsch Negative bei unerreichbarem Code**: Markieren Sie mit `# pragma: no cover`, aber ziehen Sie Refaktorieren in Betracht, um das Verhalten testbar zu machen.

# Nützliche Befehle, die Sie tatsächlich nutzen werden

```bash
coverage erase                       # Vorherige Daten löschen
coverage run -m pytest               # Sammeln
coverage report -m                   # Textzusammenfassung mit fehlenden Zeilen
coverage html                        # htmlcov/index.html öffnen
coverage xml                         # Für CI-Parser
coverage json                        # Für Skripte/Automatisierung
coverage combine                     # Parallele/Subprozess-Daten zusammenführen
coverage annotate                    # Pro-Zeile .py, zeigt welche Zeilen liefen
```

# Wann man mit dem Optimieren aufhören sollte

Zielen Sie auf einen **aussagekräftigen Schwellenwert** (z.B. 80–95%), setzen Sie ihn mit `fail_under` durch und konzentrieren Sie Reviews auf **Diff-Abdeckung** (sind die neuen/geänderten Zeilen getestet?). Jagen Sie nicht 100% auf Code hinterher, der schwer zu testen ist (Feature Flags, defensive Guards) – verwenden Sie Pragmas sparsam und bevorzugen Sie ein einfacheres, testbares Design.