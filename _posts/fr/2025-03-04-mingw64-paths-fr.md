---
audio: false
generated: true
lang: fr
layout: post
title: Gestion des chemins dans MINGW64 sous Windows
translated: true
---

MINGW64, faisant partie du projet MSYS2, fournit un environnement de type Unix sur Windows, vous permettant d'utiliser des commandes de shell bash et des outils de style Unix. Un aspect clé du travail dans cet environnement est la gestion des chemins de fichiers, surtout puisque les systèmes Windows et Unix utilisent des conventions différentes. Ci-dessous, j'expliquerai comment gérer les chemins dans MINGW64, fournir des exemples (y compris les cas avec des espaces), et clarifier quand utiliser le chemin absolu d'une commande.

#### 1. **Conventions de Chemin dans MINGW64**
- **Chemins Windows** : Utilisent généralement des barres obliques inverses (par exemple, `C:\Users`).
- **Chemins Unix** : Utilisent des barres obliques (par exemple, `/usr/bin`). Dans MINGW64, les lecteurs Windows sont montés sous `/`, donc `C:\` devient `/c/`, `D:\` devient `/d/`, et ainsi de suite.
- **Règle Générale** : MINGW64 préfère les chemins de style Unix avec des barres obliques. Par exemple, `C:\Program Files` s'écrit `/c/Program Files`.

#### 2. **Gestion des Chemins avec des Espaces**
Dans les shells de type Unix (comme le shell bash dans MINGW64), les espaces sont des caractères spéciaux qui séparent les arguments. Si un chemin contient des espaces (par exemple, `Program Files`), vous devez empêcher le shell de l'interpréter incorrectement. Il existe deux façons de gérer cela :

- **Échapper l'Espace avec une Barre Oblique Inverse (`\`)** :
  - Exemple : Pour changer vers `C:\Program Files`, utilisez :
    ```bash
    cd /c/Program\ Files
    ```
  - La barre oblique inverse indique au shell de traiter l'espace comme faisant partie du chemin, et non comme un séparateur.

- **Enfermer le Chemin dans des Guillemets (`"` ou `'`)** :
  - Exemple : En utilisant des guillemets doubles :
    ```bash
    cd "/c/Program Files"
    ```
  - Exemple : En utilisant des guillemets simples :
    ```bash
    cd '/c/Program Files'
    ```
  - Les guillemets garantissent que l'ensemble du chemin est traité comme une seule entité. Les guillemets doubles sont plus courants et lisibles, bien que les guillemets simples fonctionnent également (avec des différences mineures dans la manière dont les caractères spéciaux sont traités).

Les deux méthodes fonctionnent également bien dans MINGW64. Les guillemets sont souvent préférés pour la clarté, surtout avec plusieurs espaces ou des chemins complexes.

#### 3. **Utilisation des Chemins Absolus pour les Commandes**
Dans MINGW64, lorsque vous tapez une commande (par exemple, `python`), le shell recherche dans les répertoires listés dans la variable d'environnement `PATH`. Cependant, vous pourriez avoir besoin d'utiliser le **chemin absolu** d'une commande dans ces situations :

- **Multiples Versions Existent** : Pour spécifier une version particulière d'un outil (par exemple, un `python.exe` spécifique).
- **Commande Non dans `PATH`** : Si l'exécutable n'est pas dans un répertoire listé dans `PATH`.
- **Éviter l'Ambiguïté** : Pour s'assurer que la commande exacte que vous souhaitez est exécutée.

Lors de l'utilisation d'un chemin absolu pour une commande, surtout s'il contient des espaces, vous devez gérer les espaces comme décrit ci-dessus.

#### 4. **Exemples**
Voici des exemples pratiques couvrant la gestion générale des chemins, les espaces dans les chemins et les chemins de commande absolus :

##### **Exemple 1 : Changement de Répertoire**
- **Objectif** : Naviguer vers `C:\Program Files`.
- **Commandes** :
  ```bash
  cd "/c/Program Files"    # En utilisant des guillemets
  cd /c/Program\ Files     # En utilisant une échappatoire
  ```
- **Explication** : Les deux commandes fonctionnent car elles gèrent correctement l'espace dans "Program Files".

##### **Exemple 2 : Exécution d'une Commande avec un Chemin Absolu**
- **Objectif** : Exécuter `python.exe` situé à `C:\Python39\python.exe` avec un script `script.py`.
- **Commande** :
  ```bash
  "/c/Python39/python.exe" script.py
  ```
- **Explication** : Le chemin absolu `/c/Python39/python.exe` est entre guillemets (bien que ce ne soit pas strictement nécessaire ici car il n'y a pas d'espaces) et exécute l'exécutable Python spécifique.

##### **Exemple 3 : Chemin de Commande avec des Espaces**
- **Objectif** : Exécuter `python.exe` situé à `C:\Program Files\Python39\python.exe`.
- **Commande** :
  ```bash
  "/c/Program Files/Python39/python.exe" script.py
  ```
- **Alternative** :
  ```bash
  /c/Program\ Files/Python39/python.exe script.py
  ```
- **Explication** : Les guillemets ou les échappatoires sont nécessaires en raison de l'espace dans "Program Files". Cela garantit que le shell exécute la version exacte de Python à cet emplacement.

##### **Exemple 4 : Commande avec un Argument de Chemin Windows**
- **Objectif** : Ouvrir `C:\My Documents\note.txt` en utilisant `notepad.exe` (situé à `C:\Windows\notepad.exe`).
- **Commande** :
  ```bash
  "/c/Windows/notepad.exe" 'C:\My Documents\note.txt'
  ```
- **Explication** :
  - Le chemin de la commande `/c/Windows/notepad.exe` utilise des barres obliques de style Unix et est entre guillemets.
  - L'argument `'C:\My Documents\note.txt'` utilise des barres obliques inverses de style Windows car `notepad.exe` est un programme Windows natif qui s'attend à des chemins Windows. Les guillemets simples évitent l'interprétation par le shell des barres obliques inverses (dans des guillemets doubles, vous auriez besoin de `C:\\My Documents\\note.txt`).

#### 5. **Notes Supplémentaires**
- **Chemins Unix vs. Windows pour les Arguments** :
  - Les commandes compilées pour MINGW64 (par exemple, les outils Unix) s'attendent généralement à des chemins Unix (par exemple, `/c/users/file.txt`).
  - Les programmes Windows natifs (par exemple, `notepad.exe`) s'attendent à des chemins Windows (par exemple, `C:\Users\file.txt`). Vérifiez la documentation de la commande ou testez les deux formats.
- **Simplification avec `PATH`** : Si une commande est dans votre `PATH`, vous pouvez omettre le chemin absolu (par exemple, `notepad` au lieu de `/c/Windows/notepad.exe`), mais les chemins absolus garantissent la précision.
- **Outils comme `cygpath`** : MINGW64 hérite de `cygpath` de MSYS2, qui convertit les chemins (par exemple, `cygpath -u "C:\Users"` produit `/c/Users`). Cependant, cela est rarement nécessaire pour une utilisation de base.

#### Résumé
- **Chemins dans MINGW64** : Utilisez des chemins de style Unix (par exemple, `/c/Users` pour `C:\Users`).
- **Espaces** : Utilisez des guillemets (`"/c/Program Files"`) ou échappez les espaces (`/c/Program\ Files`).
- **Chemins de Commande Absolus** : Utilisez-les pour spécifier un exécutable particulier ; mettez les chemins avec des espaces entre guillemets (par exemple, `"/c/Program Files/app.exe"`).
- **Arguments** : Adaptez le style de chemin (Unix ou Windows) à ce que la commande attend.

Ces techniques vous aideront à naviguer et à exécuter des commandes efficacement dans MINGW64, même avec des chemins complexes.