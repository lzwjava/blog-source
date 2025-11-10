---
audio: false
generated: true
lang: de
layout: post
title: Installieren Sie XeLaTeX
translated: true
type: note
---

Um XeLaTeX auf Ubuntu 24.04 oder 22.04 zu installieren, folgen Sie diesen Schritten:

1. **Paketliste aktualisieren**:
   ```bash
   sudo apt update
   ```

2. **TeX Live installieren (das XeLaTeX enthält)**:
   - Für eine vollständige Installation (empfohlen für die meisten Benutzer, enthält XeLaTeX und viele Pakete):
     ```bash
     sudo apt install texlive-xetex
     ```
   - Wenn Sie eine minimale Installation wünschen, können Sie stattdessen `texlive` installieren, aber `texlive-xetex` wird für die XeLaTeX-Unterstützung bevorzugt.

3. **Installation überprüfen**:
   Führen Sie den folgenden Befehl aus, um zu prüfen, ob XeLaTeX installiert ist:
   ```bash
   xelatex --version
   ```
   Sie sollten eine Ausgabe wie `XeTeX 3.14159265-2.6-0.999991` sehen (Versionsnummern können variieren).

4. **Optional: Zusätzliche Schriftarten installieren** (falls Sie bestimmte Schriftarten für XeLaTeX benötigen):
   ```bash
   sudo apt install texlive-fonts-extra
   ```

5. **XeLaTeX testen**:
   Erstellen Sie eine einfache `.tex`-Datei, z.B. `test.tex`:
   ```latex
   \documentclass{article}
   \usepackage{fontspec}
   \setmainfont{Liberation Serif}
   \begin{document}
   Hello, XeLaTeX!
   \end{document}
   ```
   Kompilieren Sie sie mit:
   ```bash
   xelatex test.tex
   ```
   Dies sollte eine `test.pdf`-Datei erzeugen.

**Hinweise**:
- Das Paket `texlive-xetex` ist in den Ubuntu 22.04- und 24.04-Repositorys verfügbar.
- Wenn Sie die neueste TeX Live-Version benötigen, können Sie sie manuell von der TeX Live-Website installieren, aber das Ubuntu-Paket ist in der Regel ausreichend.
- Stellen Sie sicher, dass Sie genügend Festplattenspeicher haben (~1-2 GB für `texlive-xetex`, mehr für `texlive-full`).
- Wenn Sie auf Probleme stoßen, prüfen Sie mit `sudo apt install -f` auf fehlende Abhängigkeiten.

Lassen Sie mich wissen, wenn Sie weitere Hilfe benötigen!