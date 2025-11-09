---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Beheben von PyYAML-Installationsfehlern
translated: true
type: note
---

### Den Fehler verstehen

Diese Ausgabe scheint von einem `python setup.py install` oder `pip install pyyaml` (aus dem Quellcode) auf einem Linux-System mit Python 3.13 zu stammen. Es gibt zwei Hauptprobleme:

1.  **Kompilierungsfehler für die C-Erweiterung**:
    *   Der Build-Prozess versucht, die C-Erweiterung (`yaml._yaml`) zu kompilieren, kann die Quelldatei `yaml/_yaml.c` jedoch nicht finden.
    *   Dies geschieht, weil neuere Versionen von PyYAML (ab etwa 4.x) die `_yaml.c`-Datei während des Builds dynamisch mit Cython generieren. Die Quellverteilung auf PyPI enthält die vorab generierte `.c`-Datei nicht, daher muss Cython vorher installiert sein, um sie zu erstellen.
    *   Infolgedessen wechselt es zur reinen Python-Version (die funktioniert, aber langsamer ist und einige Funktionen wie libyaml-Unterstützung fehlen).

2.  **Berechtigung verweigert während der Installation**:
    *   Die Installation versucht, in das systemweite Python-Verzeichnis (`/usr/local/lib/python3.13/dist-packages`) zu schreiben, was Root-Rechte erfordert.
    *   Dies ist üblich, wenn man ohne `sudo` oder das `--user`-Flag arbeitet.

### Lösungen

#### Beheben des Kompilierungsproblems
Installieren Sie zuerst Cython und versuchen Sie dann die PyYAML-Installation erneut. Dadurch wird die fehlende `_yaml.c`-Datei generiert und der Bau der C-Erweiterung ermöglicht.

-   **Mit pip (empfohlen)**:
    ```
    pip install cython
    pip install pyyaml
    ```
    *   Wenn Sie die schnellere C-Erweiterung mit libyaml-Unterstützung möchten (erfordert die systemweite Installation von libyaml-dev über Ihren Paketmanager, z.B. `sudo apt install libyaml-dev` auf Ubuntu/Debian):
        ```
        pip install cython libyaml
        pip install --upgrade --force-reinstall --no-cache-dir pyyaml
        ```

-   **Wenn setup.py direkt verwendet wird** (nicht empfohlen, pip bevorzugen):
    ```
    pip install cython
    python setup.py build_ext --inplace
    python setup.py install
    ```

Hinweis: Python 3.13 ist relativ neu, stellen Sie daher sicher, dass Sie die neueste Cython-Version (z.B. 3.0.11 oder neuer) für Kompatibilität verwenden. Wenn Sie einen "free-threaded" Python-Build verwenden, sind möglicherweise zusätzliche Kompilierungsanpassungen erforderlich – prüfen Sie die GitHub-Issues von PyYAML auf Updates.

#### Beheben des Berechtigungsproblems
-   **Im Benutzerverzeichnis installieren** (sicherste Methode, kein sudo erforderlich):
    ```
    pip install --user cython pyyaml
    ```
    *   Dies installiert in `~/.local/lib/python3.13/site-packages`.

-   **Verwenden von sudo für eine systemweite Installation** (mit Vorsicht verwenden, da es zu Konflikten mit Paketmanagern führen kann):
    ```
    sudo pip install cython pyyaml
    ```

-   **Beste Praxis: Verwenden Sie eine Virtuelle Umgebung**:
    Um Berechtigungsprobleme vollständig zu vermeiden:
    ```
    python -m venv myenv
    source myenv/bin/activate  # Auf Linux/Mac
    pip install cython pyyaml
    ```
    Dies hält alles isoliert.

Testen Sie nach der Installation mit `python -c "import yaml; print(yaml.__version__)"`. Wenn es ohne Fehler importiert wird, hat es funktioniert.

Wenn diese Schritte das Problem nicht beheben (z.B. aufgrund eines spezifischen Python-3.13-Problems), geben Sie weitere Details wie Ihren exakten Befehl und die OS-Version an.

[Building on Mac - _yaml.c not found](https://github.com/yaml/pyyaml/issues/122)  
[extension _yaml is not built](https://github.com/yaml/pyyaml/issues/179)  
[Installing Pyyaml with libyaml support on MacOS](https://akasurde.github.io/installing-pyyaml-with-libyaml-on-macos.html)