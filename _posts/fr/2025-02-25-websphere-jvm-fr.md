---
audio: true
lang: fr
layout: post
title: Options JVM dans le serveur WebSphere Liberty
translated: true
---

Pour vérifier les options JVM définies dans le fichier `jvm.options` situé dans le répertoire serveur d'un serveur WebSphere Liberty Profile (WLP), vous pouvez utiliser la commande `jinfo` fournie par le Java Development Kit (JDK). Cette méthode vous permet de vérifier efficacement les options appliquées à un serveur en cours d'exécution. Voici un guide étape par étape pour y parvenir :

### Étapes pour vérifier les options JVM

1. **Comprendre le contexte**
   Le fichier `jvm.options` dans le répertoire serveur (généralement `<WLP_HOME>/usr/servers/<serverName>/jvm.options`) est utilisé pour spécifier les arguments JVM, tels que la taille du tas (par exemple, `-Xmx`), les paramètres de collecte des ordures (par exemple, `-XX:+UseG1GC`), ou les propriétés système (par exemple, `-Dmy.property=value`), qui sont appliqués lorsque le serveur Liberty démarre.

2. **Démarrer le serveur**
   Commencez par démarrer votre serveur Liberty en arrière-plan en utilisant la commande suivante :
   ```
   <WLP_HOME>/bin/server start <serverName>
   ```
   Remplacez `<WLP_HOME>` par le chemin d'installation de WebSphere Liberty et `<serverName>` par le nom de votre serveur. Cette commande lance le serveur en tant que processus en arrière-plan.

3. **Localiser l'identifiant de processus (PID)**
   Après avoir démarré le serveur, vous avez besoin de l'identifiant de processus du processus Java en cours d'exécution. Liberty stocke cela de manière pratique dans un fichier `.pid` situé à :
   ```
   <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
   ```
   Ouvrez ce fichier (par exemple, en utilisant `cat` sur les systèmes de type Unix ou un éditeur de texte) pour récupérer le PID, qui est une valeur numérique représentant le processus du serveur.

4. **Vérifier les drapeaux JVM**
   Utilisez la commande `jinfo` pour inspecter les drapeaux JVM appliqués au serveur en cours d'exécution. Exécutez :
   ```
   jinfo -flags <pid>
   ```
   Remplacez `<pid>` par l'identifiant de processus obtenu à partir du fichier `.pid`. Cette commande affiche les drapeaux de ligne de commande passés au JVM, tels que `-Xmx1024m` ou `-XX:+PrintGCDetails`. Parcourez la sortie pour confirmer que les drapeaux que vous avez définis dans `jvm.options` sont présents.

5. **Vérifier les propriétés système**
   Si votre fichier `jvm.options` inclut des propriétés système (par exemple, `-Dmy.property=value`), vérifiez-les séparément avec :
   ```
   jinfo -sysprops <pid>
   ```
   Cela affiche toutes les propriétés système définies pour le JVM. Recherchez la sortie pour les propriétés spécifiques que vous avez définies afin de vous assurer qu'elles ont été appliquées correctement.

### Prérequis
- **JDK installé** : La commande `jinfo` fait partie du JDK, pas du JRE. Assurez-vous d'avoir un JDK installé et que l'exécutable `jinfo` est dans le PATH de votre système.
- **Permissions** : Exécutez `jinfo` avec le même utilisateur qui a démarré le serveur ou avec des privilèges suffisants pour se connecter au processus.

### Méthodes alternatives
Si `jinfo` n'est pas disponible ou si vous préférez une autre approche, voici deux options supplémentaires :

- **Utilisation de `server dump`** :
  1. Démarrez le serveur avec `server start <serverName>`.
  2. Générez un dump du serveur en utilisant :
     ```
     <WLP_HOME>/bin/server dump <serverName>
     ```
  3. Localisez le fichier `.zip` généré dans `<WLP_HOME>/usr/servers/<serverName>/`, extrayez-le et ouvrez le fichier `javacore.<timestamp>.txt`.
  4. Recherchez la section "CMDLINE" pour voir la ligne de commande Java complète, y compris les drapeaux JVM, et la section "System Properties" pour les propriétés système.

- **Tracer le script de démarrage** (systèmes de type Unix) :
  1. Exécutez le script du serveur avec le traçage activé :
     ```
     sh -x <WLP_HOME>/bin/server start <serverName>
     ```
  2. Passez en revue la sortie pour trouver la commande Java exécutée par le script, qui inclut toutes les options de `jvm.options`.

### Notes
- **Serveur non en cours d'exécution** : Si le serveur échoue à démarrer en raison d'options invalides, utilisez `server run <serverName>` pour l'exécuter en premier plan et vérifier la sortie de la console pour les erreurs, ou utilisez la méthode de traçage du script pour voir la commande.
- **Fichiers journaux** : Le fichier `console.log` dans `<WLP_HOME>/usr/servers/<serverName>/logs/` peut contenir certaines informations de démarrage, mais il ne liste pas fiablement toutes les options JVM à moins que la journalisation verbale ne soit activée (par exemple, `-XX:+PrintFlagsFinal`).

### Conclusion
La méthode `jinfo` est la manière la plus simple de vérifier les options JVM définies dans `jvm.options` pour un serveur Liberty en cours d'exécution. En suivant les étapes ci-dessus, vous pouvez confirmer que les drapeaux JVM et les propriétés système sont appliqués comme prévu.

---

La commande `jinfo` a signalé qu'elle ne pouvait pas se connecter au processus.

De plus, le fichier `javacore.<timestamp>.txt` n'a pas pu être trouvé après l'utilisation de la commande de dump.

La version du serveur WebSphere Liberty est 24.0.0.9.