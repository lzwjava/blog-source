---
audio: true
lang: fr
layout: post
title: Options JVM dans WebSphere Liberty Server
translated: true
---

Pour vérifier les options JVM définies dans le fichier `jvm.options` situé dans le répertoire serveur d'un serveur WebSphere Liberty Profile (WLP), vous pouvez utiliser la commande `jinfo` fournie par le Kit de développement Java (JDK). Cette méthode vous permet de vérifier les options appliquées à un serveur en cours d'exécution de manière efficace. Voici un guide étape par étape pour accomplir cela :

### Étapes pour vérifier les options JVM

1. **Comprendre le contexte**
   Le fichier `jvm.options` dans le répertoire serveur (généralement `<WLP_HOME>/usr/servers/<serverName>/jvm.options`) est utilisé pour spécifier des arguments JVM, tels que la taille du tas (par exemple, `-Xmx`), les paramètres de collecte des ordures (par exemple, `-XX:+UseG1GC`), ou les propriétés système (par exemple, `-Dmy.property=value`), qui sont appliqués lorsque le serveur Liberty démarre.

2. **Démarrer le serveur**
   Commencez par démarrer votre serveur Liberty en arrière-plan en utilisant la commande suivante :
   ```
   <WLP_HOME>/bin/server start <serverName>
   ```
   Remplacez `<WLP_HOME>` par le chemin vers votre installation WebSphere Liberty et `<serverName>` par le nom de votre serveur. Cette commande lance le serveur en tant que processus en arrière-plan.

3. **Localiser l'ID de processus (PID)**
   Après avoir démarré le serveur, vous avez besoin de l'ID de processus du processus Java en cours d'exécution. Liberty stocke cela dans un fichier `.pid` situé à :
   ```
   <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
   ```
   Ouvrez ce fichier (par exemple, en utilisant `cat` sur les systèmes Unix-like ou un éditeur de texte) pour récupérer le PID, qui est une valeur numérique représentant le processus du serveur.

4. **Vérifier les drapeaux JVM**
   Utilisez la commande `jinfo` pour inspecter les drapeaux JVM appliqués au serveur en cours d'exécution. Exécutez :
   ```
   jinfo -flags <pid>
   ```
   Remplacez `<pid>` par l'ID de processus obtenu à partir du fichier `.pid`. Cette commande affiche les drapeaux de ligne de commande passés au JVM, tels que `-Xmx1024m` ou `-XX:+PrintGCDetails`. Parcourez la sortie pour confirmer que les drapeaux que vous avez définis dans `jvm.options` sont présents.

5. **Vérifier les propriétés système**
   Si votre fichier `jvm.options` inclut des propriétés système (par exemple, `-Dmy.property=value`), vérifiez-les séparément avec :
   ```
   jinfo -sysprops <pid>
   ```
   Cela affiche toutes les propriétés système définies pour le JVM. Recherchez la sortie pour les propriétés spécifiques que vous avez définies afin de vous assurer qu'elles ont été appliquées correctement.

### Prérequis
- **JDK installé** : La commande `jinfo` fait partie du JDK, pas du JRE. Assurez-vous d'avoir un JDK installé et que l'exécutable `jinfo` est dans le PATH de votre système.
- **Permissions** : Exécutez `jinfo` avec le même utilisateur qui a démarré le serveur ou avec des privilèges suffisants pour se joindre au processus.

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

- **Tracer le script de démarrage** (systèmes Unix-like) :
  1. Exécutez le script du serveur avec le traçage activé :
     ```
     sh -x <WLP_HOME>/bin/server start <serverName>
     ```
  2. Passez en revue la sortie pour trouver la commande Java exécutée par le script, qui inclut toutes les options de `jvm.options`.

### Notes
- **Serveur non en cours d'exécution** : Si le serveur échoue à démarrer en raison d'options invalides, utilisez `server run <serverName>` pour l'exécuter en premier plan et vérifier la sortie de la console pour les erreurs, ou utilisez la méthode de traçage du script pour voir la commande.
- **Fichiers journaux** : Le fichier `console.log` dans `<WLP_HOME>/usr/servers/<serverName>/logs/` peut contenir certaines informations de démarrage, mais il ne liste pas fiablement toutes les options JVM à moins que la journalisation verbale ne soit activée (par exemple, `-XX:+PrintFlagsFinal`).

### Conclusion
La méthode `jinfo` est la manière la plus directe de vérifier les options JVM définies dans `jvm.options` pour un serveur Liberty en cours d'exécution. En suivant les étapes ci-dessus, vous pouvez confirmer que les drapeaux JVM et les propriétés système sont appliqués comme prévu.

---

La commande `jinfo` a signalé qu'elle ne pouvait pas se joindre au processus.

De plus, le fichier `javacore.<timestamp>.txt` n'a pas pu être trouvé après l'utilisation de la commande de dump.

La version de WebSphere Liberty Server est 24.0.0.9.

---

### Résolution des problèmes de vérification des options JVM dans WebSphere Liberty 24.0.0.9

Vous rencontrez des problèmes en utilisant la commande `jinfo` pour vérifier les options JVM dans votre serveur WebSphere Liberty Profile (WLP) version 24.0.0.9, avec une erreur indiquant qu'il "ne pouvait pas se joindre au processus." De plus, après avoir généré un dump du serveur, vous ne parvenez pas à trouver le fichier `javacore.<timestamp>.txt` dans l'emplacement attendu (`<WLP_HOME>/usr/servers/<serverName>/`) dans le fichier `.zip` extrait. Voici un guide détaillé pour dépanner et résoudre ces problèmes, vous assurant de pouvoir vérifier les options JVM définies dans votre fichier `jvm.options`.

---

### Comprendre le problème

- **Échec de `jinfo`** : L'erreur "ne pouvait pas se joindre au processus" signifie généralement que `jinfo` ne peut pas se connecter à la machine virtuelle Java (JVM) en cours d'exécution. Cela est souvent dû à des problèmes de permissions (par exemple, l'exécution de la commande avec un utilisateur différent de celui qui a démarré le serveur) ou à des restrictions sur le processus JVM.
- **Fichier `javacore.<timestamp>.txt` manquant** : Le processus de dump du serveur devrait produire un fichier `.zip` contenant des fichiers de diagnostic, y compris `javacore.<timestamp>.txt`, mais son absence suggère soit que le dump a échoué, soit que le fichier est dans un emplacement inattendu, soit que les contenus attendus n'ont pas été générés.

Étant donné que vous utilisez WebSphere Liberty 24.0.0.9 sur ce qui semble être un système Unix-like (en se basant sur les chemins de fichiers typiques), nous adapterons les solutions en conséquence.

---

### Solutions étape par étape

Voici plusieurs méthodes pour récupérer vos options JVM, en commençant par les alternatives les plus simples à `jinfo` et en abordant le problème du dump du serveur.

#### 1. Vérifiez que le serveur est en cours d'exécution
Avant de procéder, assurez-vous que votre serveur Liberty est actif :

- **Commande** :
  ```bash
  <WLP_HOME>/bin/server status <serverName>
  ```
- **Sortie attendue** :
  Si en cours d'exécution, vous verrez un message comme "Server <serverName> is running with process ID <pid>." Si ce n'est pas le cas, démarrez-le :
  ```bash
  <WLP_HOME>/bin/server start <serverName>
  ```

- **Localiser le PID** :
  Trouvez l'ID de processus dans `<WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid` en utilisant :
  ```bash
  cat <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
  ```
  Notez cet ID de processus pour les étapes suivantes.

#### 2. Utilisez `jps -v` comme alternative à `jinfo`
La commande `jps` (faisant partie du JDK) liste les processus Java et leurs options, souvent en contournant les problèmes de connexion que `jinfo` rencontre.

- **Commande** :
  ```bash
  jps -v
  ```
- **Sortie** :
  Une liste de processus Java, par exemple :
  ```
  12345 Liberty -Xmx1024m -XX:+UseG1GC -Dmy.property=value
  ```
- **Action** :
  Identifiez le processus de votre serveur Liberty en faisant correspondre le PID du fichier `.pid` ou en recherchant "Liberty" ou votre `<serverName>` dans la ligne de commande. Les options listées (par exemple, `-Xmx1024m`, `-Dmy.property=value`) incluent celles de `jvm.options`.

- **Vérification des permissions** :
  Si `jps -v` échoue ou ne montre aucune sortie, exécutez-le en tant que même utilisateur qui a démarré le serveur (par exemple, `sudo -u <serverUser> jps -v`) ou avec `sudo` :
  ```bash
  sudo jps -v
  ```

#### 3. Utilisez `jcmd` pour des informations JVM détaillées
Si `jps -v` n'est pas suffisant, `jcmd` (un autre outil JDK) peut interroger une JVM en cours d'exécution sans certaines des limitations de connexion de `jinfo`.

- **Commandes** :
  - Pour les options JVM :
    ```bash
    jcmd <pid> VM.command_line
    ```
    Sortie : La ligne de commande complète, par exemple, `java -Xmx1024m -XX:+UseG1GC -Dmy.property=value ...`
  - Pour les propriétés système :
    ```bash
    jcmd <pid> VM.system_properties
    ```
    Sortie : Une liste de propriétés, par exemple, `my.property=value`.

- **Action** :
  Remplacez `<pid>` par l'ID de processus de votre serveur. Assurez-vous d'exécuter ces commandes avec les permissions appropriées (par exemple, `sudo jcmd <pid> ...` si nécessaire).

#### 4. Générez et inspectez un fichier javacore
Étant donné que le dump du serveur ne produit pas le fichier `javacore.<timestamp>.txt` attendu, essayez de générer un fichier javacore autonome :

- **Commande** :
  ```bash
  <WLP_HOME>/bin/server javadump <serverName>
  ```
- **Sortie attendue** :
  Un message indiquant l'emplacement du fichier javacore, généralement `<WLP_HOME>/usr/servers/<serverName>/javacore.<timestamp>.txt`.

- **Action** :
  - Vérifiez le répertoire :
    ```bash
    ls <WLP_HOME>/usr/servers/<serverName>/javacore.*.txt
    ```
  - Ouvrez le fichier et recherchez :
    - **CMDLINE** : Liste les options JVM (par exemple, `-Xmx1024m`).
    - **System Properties** : Liste les propriétés `-D`.

- **Dépannage** :
  Si aucun fichier n'apparaît, vérifiez le `console.log` ou `messages.log` du serveur dans `<WLP_HOME>/usr/servers/<serverName>/logs/` pour les erreurs pendant l'exécution de la commande.

#### 5. Revisitez la méthode de dump du serveur
Assurons-nous que le dump complet du serveur fonctionne correctement :

- **Commande** :
  ```bash
  <WLP_HOME>/bin/server dump <serverName>
  ```
- **Sortie attendue** :
  Un fichier `.zip` comme `<serverName>.dump-<timestamp>.zip` dans `<WLP_HOME>/usr/servers/<serverName>/`.

- **Action** :
  - Vérifiez l'existence du fichier :
    ```bash
    ls <WLP_HOME>/usr/servers/<serverName>/*.zip
    ```
  - Extrayez-le :
    ```bash
    unzip <serverName>.dump-<timestamp>.zip -d temp_dir
    ```
  - Recherchez `javacore.<timestamp>.txt` :
    ```bash
    find temp_dir -name "javacore.*.txt"
    ```
  - Ouvrez le fichier et vérifiez les sections "CMDLINE" et "System Properties".

- **Dépannage** :
  - Vérifiez la sortie de la commande dans la console pour les erreurs.
  - Assurez-vous que le serveur était en cours d'exécution pendant le dump (bien que `server dump` puisse fonctionner sur un serveur arrêté, le javacore nécessite une JVM en cours d'exécution).
  - Si le fichier `.zip` est manquant, consultez les journaux dans `<WLP_HOME>/usr/servers/<serverName>/logs/` pour des indices.

#### 6. Activez la sortie JVM verbale (dernier recours)
Si tout le reste échoue, modifiez `jvm.options` pour journaliser tous les drapeaux JVM :

- **Éditez `<WLP_HOME>/usr/servers/<serverName>/jvm.options`** :
  Ajoutez :
  ```
  -XX:+PrintFlagsFinal
  ```
- **Redémarrez le serveur** :
  ```bash
  <WLP_HOME>/bin/server stop <serverName>
  <WLP_HOME>/bin/server start <serverName>
  ```
- **Vérifiez les journaux** :
  Ouvrez `<WLP_HOME>/usr/servers/<serverName>/logs/console.log` et recherchez un tableau de drapeaux JVM, par exemple :
  ```
  [uintx] MaxHeapSize = 1073741824 {product}
  ```

---

### Notes supplémentaires

- **Permissions** :
  L'échec de `jinfo` suggère un problème de permissions. Utilisez toujours le même utilisateur qui a démarré le serveur (par exemple, via `sudo -u <serverUser>` ou en vous connectant en tant que cet utilisateur) pour toutes les commandes.
- **WebSphere Liberty 24.0.0.9** :
  Le comportement du dump devrait s'aligner avec le processus documenté (`.zip` dans `<WLP_HOME>/usr/servers/<serverName>/` contenant `javacore.<timestamp>.txt`). Si cela diffère, consultez la documentation IBM pour les modifications spécifiques à la version, bien que la méthode `server javadump` reste fiable.
- **Exigence JDK** :
  Assurez-vous que votre JDK (et non seulement le JRE) est installé, car `jps`, `jcmd` et `jinfo` sont des outils JDK.

---

### Approche recommandée

1. **Essayez `jps -v` en premier** : C'est rapide et peut éviter les problèmes de connexion.
2. **Revenez à `jcmd`** : Offre une sortie détaillée si `jps` n'est pas suffisant.
3. **Utilisez `server javadump`** : Génère un javacore directement, contournant la complexité du dump complet.
4. **Dépannage du dump** : Re-exécutez `server dump` et vérifiez le contenu du fichier `.zip` si nécessaire.

En suivant ces étapes, vous devriez réussir à récupérer vos options JVM et résoudre les problèmes avec `jinfo` et le fichier javacore manquant. Faites-moi savoir si vous rencontrez des erreurs spécifiques !