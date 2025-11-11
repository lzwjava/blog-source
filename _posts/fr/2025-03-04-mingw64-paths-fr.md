---
audio: false
generated: true
lang: fr
layout: post
title: Gestion des Chemins dans MINGW64 sur Windows
translated: true
type: note
---

MINGW64, qui fait partie du projet MSYS2, fournit un environnement de type Unix sur Windows, vous permettant d'utiliser les commandes du shell bash et les outils de style Unix. Un aspect clé du travail dans cet environnement est la gestion des chemins de fichiers, surtout puisque Windows et les systèmes Unix utilisent des conventions différentes. Ci-dessous, j'expliquerai comment gérer les chemins dans MINGW64, je fournirai des exemples (y compris des cas avec des espaces) et je clarifierai quand utiliser le chemin absolu d'une commande.

#### 1. **Conventions de chemins dans MINGW64**
- **Chemins Windows** : Utilisent généralement des barres obliques inverses (p. ex., `C:\Users`).
- **Chemins Unix** : Utilisent des barres obliques (p. ex., `/usr/bin`). Dans MINGW64, les lecteurs Windows sont montés sous `/`, donc `C:\` devient `/c/`, `D:\` devient `/d/`, etc.
- **Règle générale** : MINGW64 préfère les chemins de style Unix avec des barres obliques. Par exemple, `C:\Program Files` s'écrit `/c/Program Files`.

#### 2. **Gestion des chemins avec des espaces**
Dans les shells de type Unix (comme le shell bash dans MINGW64), les espaces sont des caractères spéciaux qui séparent les arguments. Si un chemin contient des espaces (p. ex., `Program Files`), vous devez empêcher le shell de le mal interpréter. Il existe deux façons de gérer cela :

- **Échapper l'espace avec une barre oblique inverse (`\`)** :
  - Exemple : Pour accéder à `C:\Program Files`, utilisez :
    ```bash
    cd /c/Program\ Files
    ```
  - La barre oblique inverse indique au shell de traiter l'espace comme faisant partie du chemin, et non comme un séparateur.

- **Encadrer le chemin avec des guillemets (`"` ou `'`)** :
  - Exemple : En utilisant des guillemets doubles :
    ```bash
    cd "/c/Program Files"
    ```
  - Exemple : En utilisant des guillemets simples :
    ```bash
    cd '/c/Program Files'
    ```
  - Les guillemets garantissent que le chemin entier est traité comme une seule entité. Les guillemets doubles sont plus courants et lisibles, bien que les guillemets simples fonctionnent aussi (avec de légères différences dans le traitement des caractères spéciaux).

Les deux méthodes fonctionnent aussi bien dans MINGW64. Les guillemets sont souvent préférés pour plus de clarté, surtout avec des espaces multiples ou des chemins complexes.

#### 3. **Utilisation des chemins absolus pour les commandes**
Dans MINGW64, lorsque vous tapez une commande (p. ex., `python`), le shell la recherche dans les répertoires listés dans la variable d'environnement `PATH`. Cependant, vous pourriez avoir besoin d'utiliser le **chemin absolu** d'une commande dans ces situations :

- **Plusieurs versions existent** : Pour spécifier une version particulière d'un outil (p. ex., un `python.exe` spécifique).
- **Commande non dans le `PATH`** : Si l'exécutable n'est pas dans un répertoire listé dans `PATH`.
- **Éviter l'ambiguïté** : Pour s'assurer que la commande exacte que vous souhaitez est exécutée.

Lorsque vous utilisez un chemin absolu pour une commande, surtout s'il contient des espaces, vous devez gérer les espaces comme décrit ci-dessus.

#### 4. **Exemples**
Voici des exemples pratiques couvrant la gestion générale des chemins, les espaces dans les chemins et les chemins absolus des commandes :

##### **Exemple 1 : Changement de répertoire**
- **Objectif** : Naviguer vers `C:\Program Files`.
- **Commandes** :
  ```bash
  cd "/c/Program Files"    # Utilisation de guillemets
  cd /c/Program\ Files     # Utilisation d'un échappement
  ```
- **Explication** : Les deux commandes fonctionnent car elles gèrent correctement l'espace dans "Program Files".

##### **Exemple 2 : Exécution d'une commande avec un chemin absolu**
- **Objectif** : Exécuter `python.exe` situé à `C:\Python39\python.exe` avec un script `script.py`.
- **Commande** :
  ```bash
  "/c/Python39/python.exe" script.py
  ```
- **Explication** : Le chemin absolu `/c/Python39/python.exe` est entre guillemets (bien que ce ne soit pas strictement nécessaire ici puisqu'il n'y a pas d'espaces) et exécute l'exécutable Python spécifique.

##### **Exemple 3 : Chemin de commande avec des espaces**
- **Objectif** : Exécuter `python.exe` situé à `C:\Program Files\Python39\python.exe`.
- **Commande** :
  ```bash
  "/c/Program Files/Python39/python.exe" script.py
  ```
- **Alternative** :
  ```bash
  /c/Program\ Files/Python39/python.exe script.py
  ```
- **Explication** : Les guillemets ou les échappements sont requis à cause de l'espace dans "Program Files". Cela garantit que le shell exécute la version exacte de Python à cet emplacement.

##### **Exemple 4 : Commande avec un argument de chemin Windows**
- **Objectif** : Ouvrir `C:\My Documents\note.txt` en utilisant `notepad.exe` (situé à `C:\Windows\notepad.exe`).
- **Commande** :
  ```bash
  "/c/Windows/notepad.exe" 'C:\My Documents\note.txt'
  ```
- **Explication** :
  - Le chemin de la commande `/c/Windows/notepad.exe` utilise des barres obliques de style Unix et est entre guillemets.
  - L'argument `'C:\My Documents\note.txt'` utilise des barres obliques inverses de style Windows car `notepad.exe` est un programme Windows natif qui attend des chemins Windows. Les guillemets simples évitent l'interprétation des barres obliques inverses par le shell (avec des guillemets doubles, vous auriez besoin de `C:\\My Documents\\note.txt`).

#### 5. **Notes supplémentaires**
- **Chemins Unix vs. Windows pour les arguments** :
  - Les commandes compilées pour MINGW64 (p. ex., les outils Unix) attendent généralement des chemins Unix (p. ex., `/c/users/file.txt`).
  - Les programmes Windows natifs (p. ex., `notepad.exe`) attendent des chemins Windows (p. ex., `C:\Users\file.txt`). Consultez la documentation de la commande ou testez les deux formats.
- **Simplification avec `PATH`** : Si une commande est dans votre `PATH`, vous pouvez omettre le chemin absolu (p. ex., `notepad` au lieu de `/c/Windows/notepad.exe`), mais les chemins absolus garantissent la précision.
- **Outils comme `cygpath`** : MINGW64 hérite de `cygpath` depuis MSYS2, qui convertit les chemins (p. ex., `cygpath -u "C:\Users"` affiche `/c/Users`). Cependant, cela est rarement nécessaire pour une utilisation basique.

#### Résumé
- **Chemins dans MINGW64** : Utilisez des chemins de style Unix (p. ex., `/c/Users` pour `C:\Users`).
- **Espaces** : Utilisez des guillemets (`"/c/Program Files"`) ou échappez les espaces (`/c/Program\ Files`).
- **Chemins absolus des commandes** : Utilisez-les pour spécifier un exécutable particulier ; mettez entre guillemets les chemins avec des espaces (p. ex., `"/c/Program Files/app.exe"`).
- **Arguments** : Adaptez le style de chemin (Unix ou Windows) à ce que la commande attend.

Ces techniques vous aideront à naviguer et à exécuter des commandes efficacement dans MINGW64, même avec des chemins complexes.