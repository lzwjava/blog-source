---
audio: false
generated: true
lang: fr
layout: post
title: Installer XeLaTeX
translated: true
type: note
---

Pour installer XeLaTeX sur Ubuntu 24.04 ou 22.04, suivez ces étapes :

1. **Mettre à jour la liste des paquets** :
   ```bash
   sudo apt update
   ```

2. **Installer TeX Live (qui inclut XeLaTeX)** :
   - Pour une installation complète (recommandée pour la plupart des utilisateurs, inclut XeLaTeX et de nombreux paquets) :
     ```bash
     sudo apt install texlive-xetex
     ```
   - Si vous voulez une installation minimale, vous pouvez installer `texlive` à la place, mais `texlive-xetex` est préféré pour la prise en charge de XeLaTeX.

3. **Vérifier l'installation** :
   Exécutez la commande suivante pour vérifier si XeLaTeX est installé :
   ```bash
   xelatex --version
   ```
   Vous devriez voir une sortie comme `XeTeX 3.14159265-2.6-0.999991` (les numéros de version peuvent varier).

4. **Optionnel : Installer des polices supplémentaires** (si vous avez besoin de polices spécifiques pour XeLaTeX) :
   ```bash
   sudo apt install texlive-fonts-extra
   ```

5. **Tester XeLaTeX** :
   Créez un simple fichier `.tex`, par exemple `test.tex` :
   ```latex
   \documentclass{article}
   \usepackage{fontspec}
   \setmainfont{Liberation Serif}
   \begin{document}
   Bonjour, XeLaTeX !
   \end{document}
   ```
   Compilez-le avec :
   ```bash
   xelatex test.tex
   ```
   Cela devrait générer un fichier `test.pdf`.

**Notes** :
- Le paquet `texlive-xetex` est disponible dans les dépôts d'Ubuntu 22.04 et 24.04.
- Si vous avez besoin de la dernière version de TeX Live, vous pouvez l'installer manuellement depuis le site web de TeX Live, mais le paquet Ubuntu est généralement suffisant.
- Assurez-vous d'avoir suffisamment d'espace disque (~1-2 Go pour `texlive-xetex`, plus pour `texlive-full`).
- Si vous rencontrez des problèmes, vérifiez les dépendances manquantes avec `sudo apt install -f`.

Faites-moi savoir si vous avez besoin d'une aide supplémentaire !