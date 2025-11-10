---
audio: false
generated: true
lang: fr
layout: post
title: Correction du mode utilisateur de tlmgr dans TeX Live
translated: true
type: note
---

L'erreur indique que le mode utilisateur `tlmgr` n'est pas initialisé sur votre système Debian/Ubuntu. C'est un problème courant avec les installations de TeX Live à partir des dépôts Ubuntu. Voici comment le résoudre :

## Solution 1 : Initialiser le mode utilisateur tlmgr

Commencez par initialiser le mode utilisateur :

```bash
tlmgr init-usertree
```

Si cela ne fonctionne pas, essayez :

```bash
tlmgr --usermode init-usertree
```

## Solution 2 : Utiliser apt à la place (Recommandé pour Ubuntu)

Puisque vous êtes sur Ubuntu/Debian, il est souvent plus simple d'utiliser le gestionnaire de paquets du système :

```bash
sudo apt update
sudo apt install texlive-fonts-extra
```

Cela installera FontAwesome5 ainsi que d'autres paquets de polices.

## Solution 3 : Vérifier si FontAwesome5 est déjà installé

Il se peut qu'il soit déjà installé. Testez en créant un simple fichier LaTeX :

```latex
\documentclass{article}
\usepackage{fontawesome5}

\begin{document}
\faHome
\end{document}
```

Compilez-le avec :
```bash
pdflatex test.tex
```

## Solution 4 : Si vous avez besoin de la dernière version

Si vous avez spécifiquement besoin de la dernière version de FontAwesome5, vous pouvez :

1. Télécharger le paquet manuellement depuis CTAN
2. L'installer dans votre répertoire texmf local :

```bash
mkdir -p ~/texmf/tex/latex/fontawesome5
# Extrayez le paquet téléchargé dans ce répertoire
texhash ~/texmf
```

## Vérification rapide

Pour voir quels paquets TeX vous avez actuellement installés :

```bash
dpkg -l | grep texlive
```

Pour la plupart des utilisateurs, `sudo apt install texlive-fonts-extra` est la solution la plus simple qui évite complètement les problèmes de mode utilisateur tlmgr.