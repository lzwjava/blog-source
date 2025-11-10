---
audio: false
generated: true
lang: de
layout: post
title: Installation von FontAwesome5 in LaTeX auf Ubuntu
translated: true
type: note
---

Um FontAwesome5 für LaTeX auf Ubuntu zu installieren, haben Sie mehrere Möglichkeiten:

## Methode 1: Verwendung von tlmgr (TeX Live Manager)

Falls Sie TeX Live installiert haben, können Sie den Paketmanager verwenden:

```bash
sudo tlmgr update --self
sudo tlmgr install fontawesome5
```

## Methode 2: Verwendung des apt-Paketmanagers

Ubuntu bietet FontAwesome5 über seine Repositorys an:

```bash
sudo apt update
sudo apt install texlive-fonts-extra
```

Dies installiert eine umfassende Sammlung von Schriftarten, einschließlich FontAwesome5.

## Methode 3: Manuelle Installation

Falls die oben genannten Methoden nicht funktionieren, können Sie manuell installieren:

1. Laden Sie das FontAwesome5-Paket von CTAN herunter
2. Extrahieren Sie es in Ihr lokales texmf-Verzeichnis:

```bash
mkdir -p ~/texmf/tex/latex/fontawesome5
cd ~/texmf/tex/latex/fontawesome5
# Extrahieren Sie das heruntergeladene Paket hier
```

3. Aktualisieren Sie die TeX-Datenbank:
```bash
texhash ~/texmf
```

## Verwendung von FontAwesome5 in LaTeX

Nach der Installation können Sie es in Ihren LaTeX-Dokumenten verwenden:

```latex
\documentclass{article}
\usepackage{fontawesome5}

\begin{document}
\faHome \quad Home-Icon
\faEnvelope \quad E-Mail-Icon
\faGithub \quad GitHub-Icon
\end{document}
```

## Problembehandlung

Falls Sie auf Probleme stoßen:

1. Überprüfen Sie, ob Ihre TeX Live-Installation aktuell ist:
```bash
tlmgr --version
```

2. Verifizieren Sie, dass das Paket installiert ist:
```bash
tlmgr info fontawesome5
```

3. Stellen Sie sicher, dass Sie XeLaTeX oder LuaLaTeX für die volle Unicode-Unterstützung mit FontAwesome5 verwenden.

Der einfachste Ansatz ist in der Regel Methode 2 mit `apt install texlive-fonts-extra`, da sie Abhängigkeiten automatisch behandelt.