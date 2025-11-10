---
audio: false
generated: true
image: false
lang: de
layout: post
title: Schwarzer Python Code-Formatierer Leitfaden
translated: true
type: note
---

Das `black`-Paket auf PyPI ist ein **Python-Code-Formatierer**. Es formatiert Ihren Python-Code automatisch neu, um einheitlichen Stilregeln zu folgen (PEP 8-kompatibel, aber mit eigenen strengen Ansichten). So verwenden Sie es:

---

### 1. Black installieren

```bash
pip install black
```

Wenn Sie sicherstellen möchten, dass Sie immer die neueste stabile Version erhalten:

```bash
pip install -U black
```

---

### 2. Eine Datei oder ein Verzeichnis formatieren

Führen Sie Black für eine Datei aus:

```bash
black my_script.py
```

Führen Sie Black für ein ganzes Verzeichnis aus (rekursiv):

```bash
black src/
```

Standardmäßig werden Dateien direkt mit dem formatierten Code überschrieben.

---

### 3. Formatierung prüfen ohne Änderungen

Verwenden Sie `--check`, um zu sehen, ob Ihre Dateien neu formatiert werden müssen:

```bash
black --check my_script.py
```

Dies ist nützlich für CI-Pipelines, um Stilkonsistenz sicherzustellen.

---

### 4. Häufige Optionen

* `--line-length 88` → Zeilenlänge ändern (Standard: 88).
* `--diff` → Zeigt, was sich ändern würde, ohne die Datei zu modifizieren.
* `--skip-string-normalization` → String-Anführungszeichen nicht ändern.
* `--exclude` → Bestimmte Dateien/Ordner überspringen.

Beispiel:

```bash
black --line-length 100 --diff src/
```

---

### 5. Integration

* **IDE-Unterstützung**: Black ist als Plugin in PyCharm, VS Code, Vim, Emacs, etc. verfügbar.
* **Pre-commit Hook**: Fügen Sie Black zu `.pre-commit-config.yaml` hinzu, damit Code vor Commits formatiert wird:

  ```yaml
  repos:
    - repo: https://github.com/psf/black
      rev: stable
      hooks:
        - id: black
  ```
* **CI/CD**: Fügen Sie `black --check .` in Ihrer CI-Pipeline hinzu.

---

👉 Soll ich Ihnen auch zeigen, wie Sie **automatische Formatierung in VSCode oder PyCharm** einrichten, damit Sie `black` nicht manuell ausführen müssen?