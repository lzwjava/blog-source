---
audio: false
generated: true
lang: fr
layout: post
title: Écrire des fichiers batch Windows
translated: true
type: note
---

Un fichier batch Windows (.bat ou .cmd) est un fichier de script contenant une série de commandes exécutées par l'invite de commandes Windows (cmd.exe). Les fichiers batch automatisent les tâches répétitives, gèrent les opérations système ou exécutent des programmes. Ce qui suit est une introduction complète à l'écriture de fichiers batch Windows, couvrant leur objectif, leur syntaxe, les commandes courantes et les bonnes pratiques.

### Qu'est-ce qu'un fichier Batch ?
Un fichier batch est un fichier texte brut avec une extension `.bat` ou `.cmd` qui contient des commandes interprétées par l'invite de commandes Windows. Lorsqu'il est exécuté, les commandes s'exécutent séquentiellement, permettant l'automatisation de tâches comme la gestion de fichiers, la configuration du système ou l'installation de logiciels.

### Pourquoi utiliser des fichiers Batch ?
- **Automatisation** : Exécuter plusieurs commandes avec un seul script.
- **Simplicité** : Aucune connaissance avancée en programmation n'est requise.
- **Gestion du système** : Effectuer des tâches comme des sauvegardes, la gestion des utilisateurs ou la configuration de l'environnement.
- **Compatibilité** : Fonctionne sur toutes les versions de Windows avec l'invite de commandes.

### Créer un fichier Batch
1. **Écrire le script** : Utilisez un éditeur de texte (par exemple, Notepad, VS Code) pour écrire les commandes.
2. **Sauvegarder avec la bonne extension** : Sauvegardez le fichier avec une extension `.bat` ou `.cmd` (par exemple, `script.bat`).
3. **Exécuter** : Double-cliquez sur le fichier ou exécutez-le via l'invite de commandes.

### Syntaxe et structure de base
- **Commandes** : Les fichiers batch utilisent les commandes de l'invite de commandes (par exemple, `dir`, `copy`, `del`) et des commandes spécifiques aux batchs (par exemple, `echo`, `set`, `goto`).
- **Commentaires** : Utilisez `REM` ou `::` pour ajouter des commentaires pour plus de clarté.
- **Non-sensibilité à la casse** : Les commandes et les variables ne sont pas sensibles à la casse.
- **Exécution ligne par ligne** : Les commandes s'exécutent ligne par ligne à moins d'être contrôlées par des commandes de flux comme `if`, `for` ou `goto`.

### Commandes et fonctionnalités courantes
#### 1. **Commandes de base**
- `ECHO` : Contrôle l'affichage des commandes ou affiche du texte.
  - Exemple : `ECHO Bonjour le monde !` affiche "Bonjour le monde !".
  - `ECHO OFF` : Supprime l'affichage des commandes pendant l'exécution.
- `CLS` : Efface l'écran de l'invite de commandes.
- `PAUSE` : Met l'exécution en pause, en attendant une entrée utilisateur.
- `EXIT` : Termine le script ou la session de l'invite de commandes.

#### 2. **Variables**
- **Définir des variables** : Utilisez `SET` pour créer ou modifier des variables.
  - Exemple : `SET MA_VAR=Bonjour` crée une variable `MA_VAR`.
- **Utiliser des variables** : Référencez avec `%NOM_VARIABLE%`.
  - Exemple : `ECHO %MA_VAR%` affiche "Bonjour".
- **Variables d'environnement** : Variables intégrées comme `%PATH%`, `%USERNAME%` ou `%DATE%`.

#### 3. **Entrée et sortie**
- **Entrée utilisateur** : Utilisez `SET /P` pour demander une entrée.
  - Exemple : `SET /P NOM=Entrez votre nom : ` stocke l'entrée utilisateur dans `NOM`.
- **Rediriger la sortie** : Utilisez `>` pour écrire la sortie dans un fichier ou `>>` pour ajouter.
  - Exemple : `DIR > liste_fichiers.txt` sauvegarde la liste du répertoire dans `liste_fichiers.txt`.

#### 4. **Instructions conditionnelles**
- Utilisez `IF` pour exécuter des commandes basées sur des conditions.
  - Syntaxe : `IF condition command [ELSE command]`
  - Exemple : `IF "%NOM%"=="Admin" ECHO Bienvenue, Admin ! ELSE ECHO Accès refusé.`

#### 5. **Boucles**
- **Boucle FOR** : Itère sur des fichiers, répertoires ou valeurs.
  - Exemple : `FOR %i IN (*.txt) DO ECHO %i` liste tous les fichiers `.txt`.
  - Note : Dans les fichiers batch, utilisez `%%i` au lieu de `%i` pour les variables.
- **Boucles de type WHILE** : Simulées avec `GOTO` et `IF`.

#### 6. **Sous-routines et labels**
- **Labels** : Utilisez `:label` pour marquer une section de code.
- **GOTO** : Saute vers une section labellisée.
  - Exemple : `GOTO :EOF` saute vers la fin du fichier.
- **CALL** : Appelle un autre fichier batch ou une sous-routine.
  - Exemple : `CALL :maSousRoutine` exécute une sous-routine labellisée.

#### 7. **Gestion des erreurs**
- Vérifiez le succès d'une commande avec `%ERRORLEVEL%`.
  - Exemple : `IF %ERRORLEVEL% NEQ 0 ECHO La commande a échoué.`

### Bonnes pratiques
- **Utiliser `ECHO OFF`** : Réduit l'encombrement en masquant la sortie des commandes.
- **Ajouter des commentaires** : Utilisez `REM` ou `::` pour documenter le code.
- **Tester de manière incrémentale** : Exécutez de petites sections pour déboguer.
- **Gérer les erreurs** : Vérifiez `%ERRORLEVEL%` pour les échecs.
- **Utiliser des guillemets pour les chemins** : Entourez les chemins de fichiers de guillemets pour gérer les espaces (par exemple, `"C:\Program Files\"`).
- **Éviter les noms réservés** : N'utilisez pas de noms comme `CON`, `NUL` ou `PRN` pour les fichiers ou variables.
- **Utiliser `@` pour le silence** : Préfixez les commandes avec `@` pour supprimer l'affichage individuel des commandes (par exemple, `@ECHO OFF`).

### Exemple de fichier Batch
Ci-dessous un exemple de fichier batch qui démontre des fonctionnalités courantes : demander une entrée utilisateur, créer un répertoire et journaliser les actions.

```batch
@echo off
REM Exemple de fichier batch pour créer un répertoire et journaliser les actions
ECHO Démarrage du script...

:: Demander le nom du répertoire
SET /P NOM_REP=Entrez le nom du répertoire : 

:: Vérifier si l'entrée est vide
IF "%NOM_REP%"=="" (
    ECHO Erreur : Aucun nom de répertoire fourni.
    PAUSE
    EXIT /B 1
)

:: Créer le répertoire et journaliser le résultat
MKDIR "%NOM_REP%"
IF %ERRORLEVEL%==0 (
    ECHO Répertoire "%NOM_REP%" créé avec succès.
    ECHO %DATE% %TIME% : Répertoire "%NOM_REP%" créé >> journal.txt
) ELSE (
    ECHO Échec de la création du répertoire "%NOM_REP%".
    ECHO %DATE% %TIME% : Échec de la création du répertoire "%NOM_REP%" >> journal.txt
)

PAUSE
ECHO Terminé.
EXIT /B
```

### Exécution du fichier Batch
- Sauvegardez le code ci-dessus sous `exemple.bat`.
- Double-cliquez dessus ou exécutez-le via l'invite de commandes (`cmd.exe /c exemple.bat`).

### Conseils avancés
- **Expansion retardée** : Utilisez `SETLOCAL EnableDelayedExpansion` pour les variables mises à jour dans les boucles (par exemple, `!VAR!` au lieu de `%VAR%`).
- **Niveaux d'erreur** : Testez les commandes avec `IF ERRORLEVEL n` pour des codes de sortie spécifiques.
- **Outils externes** : Intégrez des outils comme `PowerShell` ou `curl` pour des fonctionnalités avancées.
- **Sécurité** : Évitez d'exécuter des fichiers batch provenant de sources non fiables pour empêcher l'exécution de code malveillant.

### Limitations
- **Complexité** : Les fichiers batch sont moins puissants que PowerShell ou Python pour les tâches complexes.
- **Gestion des erreurs** : Limitée par rapport aux langages de script modernes.
- **Multiplateforme** : Les fichiers batch sont spécifiques à Windows.

### Ressources
- **Documentation officielle** : La référence de l'invite de commandes de Microsoft (commande `help` dans cmd.exe).
- **Tutoriels** : Des sites web comme SS64.com fournissent des références détaillées des commandes.
- **Communauté** : Recherchez des exemples de fichiers batch sur X ou des forums comme Stack Overflow.

Cette introduction fournit une base pour écrire des fichiers batch. Pratiquez avec des scripts simples et explorez les commandes via `help` dans l'invite de commandes pour développer vos compétences.