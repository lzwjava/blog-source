---
audio: false
generated: true
lang: fr
layout: post
title: Installation de FontAwesome5 dans LaTeX sur Ubuntu
translated: true
type: note
---

Pour installer FontAwesome5 pour LaTeX sur Ubuntu, vous avez plusieurs options :

## Méthode 1 : Utilisation de tlmgr (TeX Live Manager)

Si vous avez TeX Live installé, vous pouvez utiliser le gestionnaire de paquets :

```bash
sudo tlmgr update --self
sudo tlmgr install fontawesome5
```

## Méthode 2 : Utilisation du gestionnaire de paquets apt

Ubuntu fournit FontAwesome5 via ses dépôts :

```bash
sudo apt update
sudo apt install texlive-fonts-extra
```

Cela installe une collection complète de polices incluant FontAwesome5.

## Méthode 3 : Installation manuelle

Si les méthodes ci-dessus ne fonctionnent pas, vous pouvez installer manuellement :

1. Téléchargez le paquet FontAwesome5 depuis CTAN
2. Extrayez-le dans votre répertoire texmf local :

```bash
mkdir -p ~/texmf/tex/latex/fontawesome5
cd ~/texmf/tex/latex/fontawesome5
# Extrayez le paquet téléchargé ici
```

3. Mettez à jour la base de données TeX :
```bash
texhash ~/texmf
```

## Utilisation de FontAwesome5 dans LaTeX

Une fois installé, vous pouvez l'utiliser dans vos documents LaTeX :

```latex
\documentclass{article}
\usepackage{fontawesome5}

\begin{document}
\faHome \quad Icône accueil
\faEnvelope \quad Icône email
\faGithub \quad Icône GitHub
\end{document}
```

## Dépannage

Si vous rencontrez des problèmes :

1. Vérifiez si votre installation TeX Live est à jour :
```bash
tlmgr --version
```

2. Vérifiez que le paquet est installé :
```bash
tlmgr info fontawesome5
```

3. Assurez-vous d'utiliser XeLaTeX ou LuaLaTeX pour une prise en charge Unicode complète avec FontAwesome5.

L'approche la plus simple est généralement la Méthode 2 utilisant `apt install texlive-fonts-extra` car elle gère automatiquement les dépendances.