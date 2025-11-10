---
audio: false
generated: true
lang: de
layout: post
title: Beheben des TeX Live tlmgr-Benutzermodus
translated: true
type: note
---

Der Fehler zeigt an, dass der `tlmgr`-Benutzermodus auf Ihrem Debian/Ubuntu-System nicht initialisiert ist. Dies ist ein häufiges Problem bei TeX Live-Installationen aus den Ubuntu-Repositorys. So können Sie es beheben:

## Lösung 1: tlmgr-Benutzermodus initialisieren

Initialisieren Sie zunächst den Benutzermodus:

```bash
tlmgr init-usertree
```

Falls das nicht funktioniert, versuchen Sie:

```bash
tlmgr --usermode init-usertree
```

## Lösung 2: Stattdessen apt verwenden (Empfohlen für Ubuntu)

Da Sie auf Ubuntu/Debian sind, ist es oft einfacher, den System-Paketmanager zu verwenden:

```bash
sudo apt update
sudo apt install texlive-fonts-extra
```

Dadurch wird FontAwesome5 zusammen mit anderen Schriftart-Paketen installiert.

## Lösung 3: Prüfen, ob FontAwesome5 bereits installiert ist

Möglicherweise ist es bereits installiert. Testen Sie dies, indem Sie eine einfache LaTeX-Datei erstellen:

```latex
\documentclass{article}
\usepackage{fontawesome5}

\begin{document}
\faHome
\end{document}
```

Kompilieren Sie sie mit:
```bash
pdflatex test.tex
```

## Lösung 4: Falls Sie die neueste Version benötigen

Falls Sie speziell die neueste FontAwesome5-Version benötigen, können Sie:

1. Das Paket manuell von CTAN herunterladen
2. Es in Ihrem lokalen texmf-Verzeichnis installieren:

```bash
mkdir -p ~/texmf/tex/latex/fontawesome5
# Extrahieren Sie das heruntergeladene Paket in dieses Verzeichnis
texhash ~/texmf
```

## Schnellprüfung

Um zu sehen, welche TeX-Pakete Sie derzeit installiert haben:

```bash
dpkg -l | grep texlive
```

Für die meisten Benutzer ist `sudo apt install texlive-fonts-extra` die einfachste Lösung, die die Probleme mit dem tlmgr-Benutzermodus vollständig umgeht.