---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: GitHub Actions Matrix-Builds Leitfaden
translated: true
type: note
---

Es klingt, als würdest du nach der Verwendung von **GitHub Actions** Matrix-Builds fragen, um Tests parallel auszuführen, und wie man die `fail-fast`-Option in einer Matrix-Strategie verwendet. Lass mich das für dich aufschlüsseln.

---

### Matrix-Builds in GitHub Actions
Die **Matrix-Strategie** ermöglicht es dir, denselben Job parallel mit verschiedenen Parametern auszuführen – zum Beispiel Tests über mehrere Python- oder Node-Versionen hinweg oder auf verschiedenen Betriebssystemen.

Ein minimales Beispiel:

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10]
        os: [ubuntu-latest, windows-latest]
      fail-fast: false
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
```

---

### Wichtige Punkte

- **`matrix`:** Definiert die Variablen, um Job-Kombinationen zu erstellen.  
  Das obige Beispiel führt Tests für alle Kombinationen von (`python-version`, `os`) aus.

- **Parallele Ausführung:** Jeder durch die Matrix generierte Job wird standardmäßig **parallel** ausgeführt.

- **`fail-fast`:**
  - Der Standardwert ist `true`. Das bedeutet, wenn ein Job fehlschlägt, werden die restlichen Matrix-Jobs abgebrochen.
  - Setze `fail-fast: false`, wenn du möchtest, dass alle Matrix-Jobs weiterlaufen, selbst wenn einer fehlschlägt.

  Beispiel:
  ```yaml
  strategy:
    matrix:
      node: [14, 16, 18]
    fail-fast: false
  ```

- **Begrenzung der Gesamt-Jobs:** Du kannst einige Kombinationen ausschließen:
  ```yaml
  strategy:
    matrix:
      python-version: [3.8, 3.9, 3.10]
      os: [ubuntu-latest, windows-latest]
    exclude:
      - python-version: 3.8
        os: windows-latest
  ```

---

### Tests parallel ausführen
- Jeder **Matrix-Job wird parallel** auf seinem eigenen Runner ausgeführt, daher musst du nichts Besonderes tun.
- Innerhalb jedes Jobs, wenn du **parallele Testausführung** möchtest (z.B. pytest `-n auto`), kannst du das auf der Ebene des Testbefehls hinzufügen.

Beispiel:
```yaml
- name: Run pytest in parallel
  run: pytest -n auto
```

---

✅ **Zusammenfassung:**
- Verwende `strategy.matrix`, um verschiedene Parameterkombinationen zu definieren.
- Setze `fail-fast: false`, wenn alle Matrix-Jobs laufen sollen, auch wenn einer fehlschlägt.
- Matrix-Jobs werden automatisch parallel ausgeführt.
- Für schnellere Laufzeit innerhalb jedes Jobs, verwende die Parallelisierung des Test-Frameworks (z.B. pytest-xdist).

---

Möchtest du, dass ich dir ein echtes Beispiel für **das Ausführen von Node/JavaScript-Tests** mit einer Matrix (mehrere Node-Versionen, `fail-fast: false`, parallelisierte Tests mit `npm test`) zeige?