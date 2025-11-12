---
audio: false
generated: true
lang: fr
layout: post
title: Résoudre les problèmes de JDK Eclipse
translated: true
type: note
---

Lorsque vous démarrez Eclipse 4.6.3 en cliquant sur `eclipse.exe` et que vous rencontrez l'erreur "Java was started but returned exit code" avec une référence à `Oracle\Java\javapath\javaw.exe`, cela signifie qu'Eclipse tente d'utiliser une machine virtuelle Java (JVM) qui est soit incompatible, soit mal configurée. Le chemin `Oracle\Java\javapath\javaw.exe` indique qu'Eclipse utilise par défaut une JVM définie dans la variable d'environnement PATH de votre système, qui peut ne pas être adaptée à Eclipse 4.6.3. Pour résoudre ce problème, vous devez spécifier le Java home correct pour Eclipse en le configurant pour qu'il utilise une JVM compatible. Voici comment procéder :

### Solution étape par étape

1. **Comprendre l'exigence**  
   Eclipse 4.6.3 (Neon) nécessite au moins Java 8 pour fonctionner correctement. L'erreur suggère que la JVM actuelle (depuis `Oracle\Java\javapath`) ne répond peut-être pas à cette exigence ou présente des problèmes de configuration. Vous devrez indiquer à Eclipse d'utiliser une installation Java compatible, telle qu'un JDK Java 8.

2. **Localiser votre installation Java**  
   Identifiez où une version compatible de Java (par exemple, JDK 1.8.0) est installée sur votre système. Les emplacements courants sur Windows incluent :  
   - `C:\Program Files\Java\jdk1.8.0_XXX` (pour Java 64 bits)  
   - `C:\Program Files (x86)\Java\jdk1.8.0_XXX` (pour Java 32 bits)  
   Remplacez `XXX` par la version de mise à jour spécifique (par exemple, `231` pour JDK 1.8.0_231). À l'intérieur de ce répertoire, le fichier `javaw.exe` se trouve dans le sous-répertoire `bin` (par exemple, `C:\Program Files\Java\jdk1.8.0_XXX\bin\javaw.exe`).

   **Astuce** : Pour confirmer la version et l'architecture, ouvrez une invite de commande, naviguez vers le répertoire `bin` (par exemple, `cd C:\Program Files\Java\jdk1.8.0_XXX\bin`), et exécutez :
   ```
   java -version
   ```
   Recherchez "64-Bit" ou "32-Bit" dans la sortie pour vérifier l'architecture. Assurez-vous qu'elle correspond à votre version d'Eclipse (probablement 64 bits si téléchargée récemment).

3. **Trouver le fichier `eclipse.ini`**  
   Le fichier `eclipse.ini` est un fichier de configuration situé dans le même répertoire que `eclipse.exe`. Par exemple, si Eclipse est installé dans `C:\eclipse`, le fichier se trouvera à `C:\eclipse\eclipse.ini`. Ce fichier vous permet de spécifier la JVM qu'Eclipse doit utiliser.

4. **Modifier le fichier `eclipse.ini`**  
   Ouvrez `eclipse.ini` dans un éditeur de texte (par exemple, Notepad) avec des privilèges d'administrateur. Vous le modifierez pour inclure l'argument `-vm`, qui indique à Eclipse quelle JVM utiliser. Suivez ces étapes :

   - **Vérifier le contenu existant** : Recherchez un argument `-vm`. S'il est déjà présent, il sera suivi d'un chemin sur la ligne suivante (par exemple, `-vm` suivi de `C:/some/path/bin/javaw.exe`). S'il pointe vers le `Oracle\Java\javapath\javaw.exe` problématique, vous le remplacerez. Si aucun argument `-vm` n'existe, vous l'ajouterez.
   - **Ajouter ou modifier l'argument `-vm`** : Insérez les deux lignes suivantes avant la section `-vmargs` (si elle existe) ou près du début du fichier après les paramètres de démarrage initiaux :
     ```
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     ```
     - Utilisez des barres obliques (`/`) au lieu des barres obliques inverses (`\`) pour éviter les problèmes d'analyse.
     - Remplacez `C:/Program Files/Java/jdk1.8.0_XXX` par le chemin réel de votre installation Java.
   - **Assurer un placement correct** : L'argument `-vm` doit apparaître avant la section `-vmargs`, qui commence généralement par `-vmargs` suivi d'options JVM comme `-Xms256m` ou `-Xmx1024m`. Par exemple, votre `eclipse.ini` pourrait ressembler à ceci après modification :
     ```
     -startup
     plugins/org.eclipse.equinox.launcher_1.3.201.v20161025-1711.jar
     --launcher.library
     plugins/org.eclipse.equinox.launcher.win32.win32.x86_64_1.1.401.v20161122-1740
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     -vmargs
     -Dosgi.requiredJavaVersion=1.8
     -Xms256m
     -Xmx1024m
     ```
   - **Éviter les espaces ou lignes vides supplémentaires** : Assurez-vous qu'il n'y a pas d'espaces inutiles ou de lignes vides immédiatement après les lignes `-vm` ou du chemin, car cela peut amener Eclipse à interpréter incorrectement la configuration.

5. **Sauvegarder et tester**  
   Sauvegardez le fichier `eclipse.ini`, puis double-cliquez sur `eclipse.exe` pour démarrer Eclipse. S'il est configuré correctement, Eclipse devrait démarrer sans l'erreur "Java was started but returned exit code".

### Notes supplémentaires
- **Correspondance d'architecture** : Assurez-vous que l'architecture de la JVM (32 bits ou 64 bits) correspond à votre installation d'Eclipse. Un Eclipse 64 bits nécessite une JVM 64 bits, généralement trouvée dans `C:\Program Files\Java`, tandis qu'un Eclipse 32 bits a besoin d'une JVM 32 bits depuis `C:\Program Files (x86)\Java`.
- **Vérifier le chemin** : Vérifiez que `javaw.exe` existe à l'emplacement spécifié. Si le chemin est incorrect, Eclipse ne pourra pas démarrer.
- **Option de secours** : Si cela ne fonctionne pas, envisagez de définir la variable d'environnement `JAVA_HOME` (par exemple, `C:\Program Files\Java\jdk1.8.0_XXX`) et de mettre à jour le PATH du système pour inclure `%JAVA_HOME%\bin`. Cependant, la modification de `eclipse.ini` est la méthode préférée et plus fiable pour Eclipse.

En modifiant le fichier `eclipse.ini` pour inclure l'argument `-vm` avec le chemin vers un `javaw.exe` compatible, vous spécifiez efficacement le Java home pour Eclipse, garantissant ainsi qu'il utilise la JVM correcte pour démarrer.