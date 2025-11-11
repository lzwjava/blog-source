---
audio: false
generated: true
lang: fr
layout: post
title: Script de lancement SQuirreL
translated: true
type: note
---

Ce script batch est utilisé pour lancer le client SQL SQuirreL, un outil d'administration de base de données basé sur Java. Voici une explication complète du script, détaillant son objectif, sa structure et son fonctionnement étape par étape.

---

### **Aperçu**
Le script est conçu pour :
1. Configurer l'environnement Java pour exécuter le client SQL SQuirreL.
2. Vérifier la compatibilité de la version Java (nécessite Java 1.6 ou 1.7).
3. Vérifier les mises à jour logicielles et les appliquer si disponibles.
4. Construire le classpath pour SQuirreL et ses bibliothèques.
5. Lancer l'application client SQL SQuirreL avec les paramètres appropriés.

Le script est écrit pour Windows (en utilisant l'extension `.bat`) et utilise le langage de script batch de l'invite de commandes Windows.

---

### **Explication Ligne par Ligne**

#### **1. `@echo off`**
- **Objectif** : Désactive l'écho des commandes vers la console, rendant la sortie du script plus propre en n'affichant que la sortie prévue (par exemple, les messages d'erreur ou les instructions `echo` spécifiques).
- **Effet** : Les commandes exécutées dans le script ne sont pas affichées sauf si elles sont explicitement imprimées en utilisant `echo`.

---

#### **2. `@rem IZPACK_JAVA is filtered in by the IzPack installer when this script is installed`**
- **Objectif** : Un commentaire (`@rem`) indiquant que la variable `IZPACK_JAVA` est définie par l'installateur IzPack pendant l'installation.
- **Contexte** : IzPack est un outil utilisé pour créer des installateurs pour les applications Java. Il définit dynamiquement la variable d'environnement `JAVA_HOME` dans le script pour pointer vers l'installation Java utilisée pendant la configuration.

#### **3. `set IZPACK_JAVA=%JAVA_HOME`**
- **Objectif** : Affecte la valeur de la variable d'environnement `JAVA_HOME` (définie par IzPack) à la variable `IZPACK_JAVA`.
- **Explication** : Cela garantit que le script sait où se trouve l'installation Java. `JAVA_HOME` pointe typiquement vers le répertoire racine d'un Java Development Kit (JDK) ou d'un Java Runtime Environment (JRE).

---

#### **4. Logique de Détection de Java**
```bat
@rem We detect the java executable to use according to the following algorithm:
@rem 1. If the one used by the IzPack installer is available then use that; otherwise
@rem 2. Use the java that is in the command path.
if exist "%IZPACK_JAVA%\bin\javaw.exe" (
  set LOCAL_JAVA=%IZPACK_JAVA%\bin\javaw.exe
) else (
  set LOCAL_JAVA=javaw.exe
)
```
- **Objectif** : Détermine quel exécutable Java utiliser pour exécuter SQuirreL SQL.
- **Logique** :
  1. **Vérifier le Java IzPack** : Le script vérifie si `javaw.exe` existe dans le répertoire `bin` de l'installation Java spécifiée par `IZPACK_JAVA` (c'est-à-dire `%IZPACK_JAVA%\bin\javaw.exe`).
     - `javaw.exe` est un exécutable Java spécifique à Windows qui exécute les applications Java sans ouvrir de fenêtre de console (contrairement à `java.exe`).
     - S'il est trouvé, `LOCAL_JAVA` est défini sur le chemin complet de `javaw.exe`.
  2. **Retour au PATH** : Si `javaw.exe` n'est pas trouvé dans le répertoire `IZPACK_JAVA`, le script utilise `javaw.exe` à partir de la variable d'environnement `PATH` du système.
- **Pourquoi `javaw.exe` ?** : L'utilisation de `javaw.exe` garantit que l'application s'exécute sans une fenêtre de commande persistante, offrant une expérience utilisateur plus propre.

#### **5. `echo Using java: %LOCAL_JAVA%`**
- **Objectif** : Affiche le chemin de l'exécutable Java utilisé sur la console à des fins de débogage ou d'information.
- **Exemple de Sortie** : Si `LOCAL_JAVA` est `C:\Program Files\Java\jre1.6.0_45\bin\javaw.exe`, il affichera :
  ```
  Using java: C:\Program Files\Java\jre1.6.0_45\bin\javaw.exe
  ```

---

#### **6. Détermination du Répertoire d'Installation de SQuirreL SQL**
```bat
set basedir=%~f0
:strip
set removed=%basedir:~-1%
set basedir=%basedir:~0,-1%
if NOT "%removed%"=="\" goto strip
set SQUIRREL_SQL_HOME=%basedir%
```
- **Objectif** : Détermine le répertoire où SQuirreL SQL est installé (`SQUIRREL_SQL_HOME`).
- **Explication** :
  - `%~f0` : Cela s'étend en le chemin complet du script batch lui-même (par exemple, `C:\Program Files\SQuirreL\squirrel-sql.bat`).
  - **Boucle `:strip`** : Le script supprime itérativement le dernier caractère de `basedir` jusqu'à ce qu'il rencontre un backslash (`\`), supprimant effectivement le nom de fichier du script pour obtenir le chemin du répertoire.
  - **Résultat** : `SQUIRREL_SQL_HOME` est défini sur le répertoire contenant le script (par exemple, `C:\Program Files\SQuirreL`).
- **Pourquoi cette approche ?** : Cela garantit que le script peut déterminer dynamiquement son propre répertoire d'installation, le rendant portable sur différents systèmes.

---

#### **7. Vérification de la Version Java**
```bat
"%LOCAL_JAVA%" -cp "%SQUIRREL_SQL_HOME%\lib\versioncheck.jar" JavaVersionChecker 1.6 1.7
if ErrorLevel 1 goto ExitForWrongJavaVersion
```
- **Objectif** : Vérifie que la version Java est compatible avec SQuirreL SQL (nécessite Java 1.6 ou 1.7).
- **Explication** :
  - Le script exécute la classe `JavaVersionChecker` à partir de `versioncheck.jar`, situé dans le répertoire `lib` de SQuirreL SQL.
  - **`-cp`** : Spécifie le classpath, pointant vers `versioncheck.jar`.
  - **Arguments** : `1.6 1.7` indique que la version Java doit être 1.6 ou 1.7.
  - **Note** : `versioncheck.jar` est compilé avec une compatibilité Java 1.2.2, garantissant qu'il peut s'exécuter sur des JVM plus anciennes pour effectuer la vérification de version.
  - **Gestion des Erreurs** : Si la version Java est incompatible, `ErrorLevel` est défini sur 1 et le script saute vers l'étiquette `:ExitForWrongJavaVersion`, mettant fin à l'exécution.
- **Pourquoi cette vérification ?** : SQuirreL SQL nécessite des versions Java spécifiques pour fonctionner correctement, et cela empêche l'application de s'exécuter sur des JVM non prises en charge.

---

#### **8. Vérification des Mises à Jour Logicielles**
```bat
if not exist "%SQUIRREL_SQL_HOME%\update\changeList.xml" goto launchsquirrel
SET TMP_CP="%SQUIRREL_SQL_HOME%\update\downloads\core\squirrel-sql.jar"
if not exist %TMP_CP% goto launchsquirrel
dir /b "%SQUIRREL_SQL_HOME%\update\downloads\core\*.*" > %TEMP%\update-lib.tmp
FOR /F %%I IN (%TEMP%\update-lib.tmp) DO CALL "%SQUIRREL_SQL_HOME%\addpath.bat" "%SQUIRREL_SQL_HOME%\update\downloads\core\%%I"
SET UPDATE_CP=%TMP_CP%
SET UPDATE_PARMS=--log-config-file "%SQUIRREL_SQL_HOME%\update-log4j.properties" --squirrel-home "%SQUIRREL_SQL_HOME%" %1 %2 %3 %4 %5 %6 %7 %8 %9
"%LOCAL_JAVA%" -cp %UPDATE_CP% -Dlog4j.defaultInitOverride=true -Dprompt=true net.sourceforge.squirrel_sql.client.update.gui.installer.PreLaunchUpdateApplication %UPDATE_PARAMS%
```
- **Objectif** : Vérifie et applique les mises à jour logicielles avant de lancer l'application principale.
- **Explication** :
  1. **Vérifier les Fichiers de Mise à Jour** :
     - Le script vérifie si `changeList.xml` existe dans le répertoire `update`. Ce fichier est créé par la fonctionnalité de mise à jour logicielle de SQuirreL pour suivre les mises à jour.
     - Si `changeList.xml` n'existe pas, le script ignore le processus de mise à jour et saute à `:launchsquirrel`.
     - Il vérifie également la présence du `squirrel-sql.jar` mis à jour dans le répertoire `update\downloads\core`. S'il n'existe pas, le script saute à `:launchsquirrel`.
  2. **Construire le Classpath de Mise à Jour** :
     - La commande `dir /b` liste tous les fichiers du répertoire `update\downloads\core` et les écrit dans un fichier temporaire (`%TEMP%\update-lib.tmp`).
     - La boucle `FOR /F` itère sur les fichiers dans `update-lib.tmp` et appelle `addpath.bat` pour ajouter chaque fichier au classpath stocké dans `TMP_CP`.
     - `UPDATE_CP` est défini sur le classpath, commençant par `squirrel-sql.jar` du répertoire de mise à jour.
  3. **Définir les Paramètres de Mise à Jour** :
     - `UPDATE_PARMS` inclut :
       - `--log-config-file` : Spécifie le fichier de configuration Log4j pour la journalisation pendant le processus de mise à jour.
       - `--squirrel-home` : Passe le répertoire d'installation de SQuirreL.
       - `%1 %2 %3 ... %9` : Passe tous les arguments de ligne de commande fournis au script.
  4. **Exécuter l'Application de Mise à Jour** :
     - Le script lance `PreLaunchUpdateApplication` (une classe Java dans `squirrel-sql.jar`) pour appliquer les mises à jour.
     - **`-Dlog4j.defaultInitOverride=true`** : Remplace la configuration Log4j par défaut.
     - **`-Dprompt=true`** : Active probablement les invites interactives pendant le processus de mise à jour.
- **Pourquoi cette étape ?** : SQuirreL SQL prend en charge les mises à jour automatiques, et cette section garantit que toutes les mises à jour téléchargées sont appliquées avant le lancement de l'application principale.

---

#### **9. Lancer SQuirreL SQL**
```bat
:launchsquirrel
@rem build SQuirreL's classpath
set TMP_CP="%SQUIRREL_SQL_HOME%\squirrel-sql.jar"
dir /b "%SQUIRREL_SQL_HOME%\lib\*.*" > %TEMP%\squirrel-lib.tmp
FOR /F %%I IN (%TEMP%\squirrel-lib.tmp) DO CALL "%SQUIRREL_SQL_HOME%\addpath.bat" "%SQUIRREL_SQL_HOME%\lib\%%I"
SET SQUIRREL_CP=%TMP_CP%
echo "SQUIRREL_CP=%SQUIRREL_CP%"
```
- **Objectif** : Construit le classpath pour l'application principale SQuirreL SQL et se prépare à la lancer.
- **Explication** :
  1. **Initialiser le Classpath** :
     - `TMP_CP` est initialisé avec le chemin vers `squirrel-sql.jar` dans le répertoire d'installation de SQuirreL.
  2. **Ajouter les Jars de Bibliothèque** :
     - La commande `dir /b` liste tous les fichiers du répertoire `lib` et les écrit dans `squirrel-lib.tmp`.
     - La boucle `FOR /F` itère sur les fichiers et appelle `addpath.bat` pour ajouter chaque fichier de bibliothèque (par exemple, les fichiers `.jar`) au classpath `TMP_CP`.
  3. **Définir le Classpath Final** :
     - `SQUIRREL_CP` est défini sur le classpath complété.
  4. **Sortie de Débogage** :
     - Le script imprime le classpath final (`SQUIRREL_CP`) à des fins de débogage.

---

#### **10. Définir les Paramètres de Lancement**
```bat
SET TMP_PARMS=--log-config-file "%SQUIRREL_SQL_HOME%\log4j.properties" --squirrel-home "%SQUIRREL_SQL_HOME%" %1 %2 %3 %4 %5 %6 %7 %8 %9
```
- **Objectif** : Définit les paramètres à passer à l'application SQuirreL SQL.
- **Explication** :
  - `--log-config-file` : Spécifie le fichier de configuration Log4j pour l'application principale.
  - `--squirrel-home` : Passe le répertoire d'installation de SQuirreL.
  - `%1 %2 ... %9` : Passe tous les arguments de ligne de commande fournis au script.

---

#### **11. Lancer l'Application**
```bat
@rem -Dsun.java2d.noddraw=true prevents performance problems on Win32 systems.
start "SQuirreL SQL Client" /B "%LOCAL_JAVA%" -Xmx256m -Dsun.java2d.noddraw=true -cp %SQUIRREL_CP% -splash:"%SQUIRREL_SQL_HOME%/icons/splash.jpg" net.sourceforge.squirrel_sql.client.Main %TMP_PARMS%
```
- **Objectif** : Lance l'application client SQL SQuirreL.
- **Explication** :
  - **`start "SQuirreL SQL Client" /B`** : Exécute la commande dans un nouveau processus sans ouvrir de nouvelle fenêtre de console (`/B` supprime la fenêtre).
  - **`%LOCAL_JAVA%`** : Spécifie l'exécutable Java à utiliser.
  - **`-Xmx256m`** : Définit la taille maximale du tas Java à 256 Mo pour limiter l'utilisation de la mémoire.
  - **`-Dsun.java2d.noddraw=true`** : Désactive DirectDraw pour les graphiques Java 2D pour éviter les problèmes de performance sur les systèmes Windows.
  - **`-cp %SQUIRREL_CP%`** : Spécifie le classpath pour l'application.
  - **`-splash:"%SQUIRREL_SQL_HOME%/icons/splash.jpg"`** : Affiche un écran de démarrage (une image) au lancement de l'application.
  - **`net.sourceforge.squirrel_sql.client.Main`** : La classe Java principale à exécuter.
  - **`%TMP_PARMS%`** : Passe les paramètres définis précédemment.

---

#### **12. Sortie pour Version Java Incorrecte**
```bat
:ExitForWrongJavaVersion
```
- **Objectif** : Une étiquette utilisée comme point de sortie si la vérification de la version Java échoue.
- **Explication** : Si la version Java n'est pas 1.6 ou 1.7, le script saute ici et se termine sans lancer l'application.

---

### **Composants et Concepts Clés**
1. **Construction du Classpath** :
   - Le script construit dynamiquement le classpath pour le processus de mise à jour (`UPDATE_CP`) et l'application principale (`SQUIRREL_CP`) en incluant `squirrel-sql.jar` et tous les fichiers `.jar` dans les répertoires `lib` ou `update\downloads\core`.
   - Le script `addpath.bat` (non montré) est supposé ajouter chaque fichier à la variable de classpath.

2. **Configuration Log4j** :
   - Log4j est un framework de journalisation utilisé par SQuirreL SQL. Le script spécifie des fichiers de configuration Log4j séparés pour le processus de mise à jour (`update-log4j.properties`) et l'application principale (`log4j.properties`).

3. **Mécanisme de Mise à Jour Logicielle** :
   - SQuirreL SQL prend en charge les mises à jour automatiques, gérées par la classe `PreLaunchUpdateApplication`. Le script vérifie les fichiers de mise à jour et exécute le processus de mise à jour si nécessaire.

4. **Compatibilité des Versions Java** :
   - Le script impose une compatibilité stricte avec Java 1.6 ou 1.7, probablement en raison de dépendances ou de fonctionnalités spécifiques à ces versions.

5. **Portabilité** :
   - Le script est conçu pour être portable en déterminant dynamiquement le répertoire d'installation et l'emplacement de l'exécutable Java.

---

### **Problèmes Potentiels et Considérations**
1. **Restriction de Version Java** :
   - Le script n'autorise que Java 1.6 ou 1.7, qui sont obsolètes (publiées en 2006 et 2011, respectivement). Les systèmes modernes peuvent avoir des versions Java plus récentes, provoquant l'échec du script sauf si une JRE plus ancienne est installée.
   - **Solution de Contournement** : Les utilisateurs peuvent avoir besoin d'installer une JRE compatible ou de modifier le script pour prendre en charge des versions plus récentes (si SQuirreL SQL est compatible).

2. **Chemins Codés en Dur** :
   - Le script suppose que certains fichiers (par exemple, `squirrel-sql.jar`, `versioncheck.jar`, `addpath.bat`) existent dans des répertoires spécifiques relatifs à `SQUIRREL_SQL_HOME`. S'ils sont manquants ou déplacés, le script échouera.

3. **Spécifique à Windows** :
   - Le script utilise des commandes spécifiques à Windows (`dir /b`, `FOR /F`, `start /B`) et `javaw.exe`, le rendant incompatible avec les systèmes non Windows sans modification.

4. **Gestion des Erreurs** :
   - Le script gère les erreurs de version Java mais ne fournit pas de messages d'erreur détaillés pour d'autres échecs (par exemple, `squirrel-sql.jar` manquant ou classpath invalide).

5. **Limite de Mémoire** :
   - Le drapeau `-Xmx256m` limite la JVM à 256 Mo de mémoire, ce qui peut être insuffisant pour les grandes bases de données ou les requêtes complexes, provoquant potentiellement une `OutOfMemoryError`.

---

### **Résumé**
Ce script batch est un lanceur pour le client SQL SQuirreL, effectuant les tâches suivantes :
- Détecte et configure l'exécutable Java.
- Vérifie la compatibilité de la version Java (1.6 ou 1.7).
- Vérifie et applique les mises à jour logicielles si disponibles.
- Construit le classpath pour l'application.
- Lance SQuirreL SQL avec les paramètres appropriés, y compris un écran de démarrage et des paramètres mémoire.

Le script est bien structuré pour son objectif mais est adapté à un environnement spécifique (Windows, Java 1.6/1.7) et peut nécessiter des mises à jour pour prendre en charge les systèmes modernes ou les versions Java plus récentes.

Si vous avez d'autres questions ou besoin d'aide pour modifier le script (par exemple, pour prendre en charge des versions Java plus récentes), faites-le moi savoir !