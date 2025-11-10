---
audio: false
generated: true
lang: fr
layout: post
title: Intégration du profileur YourKit avec WebSphere Liberty sur Windows
translated: true
type: note
---

L'utilisation de YourKit Java Profiler avec WebSphere Liberty Server sur Windows implique l'intégration de l'agent YourKit dans la JVM de WebSphere Liberty et sa configuration pour le profilage. Voici les étapes pour configurer cela, basées sur les informations disponibles et les meilleures pratiques pour l'intégration YourKit et WebSphere Liberty :

### Prérequis
- **YourKit Java Profiler** : Installé sur votre machine Windows. Téléchargez-le depuis [le site officiel de YourKit](https://www.yourkit.com/) et assurez-vous d'avoir une licence valide ou une clé d'essai.
- **WebSphere Liberty** : Installé et fonctionnant sur votre système Windows. Assurez-vous d'avoir un accès administratif aux fichiers de configuration du serveur.
- **Java JDK** : WebSphere Liberty utilise un runtime Java (IBM JDK ou OpenJDK). Confirmez que la version du JDK est compatible avec YourKit (YourKit prend en charge Java 5 et versions ultérieures, mais vérifiez la compatibilité avec votre version spécifique).
- **Privilèges Administratifs** : Requis pour modifier les fichiers de configuration de WebSphere Liberty.

### Guide étape par étape

1. **Installer YourKit Java Profiler**
   - Téléchargez et installez YourKit Java Profiler pour Windows depuis [le site web de YourKit](https://www.yourkit.com/download).
   - Notez le répertoire d'installation, car vous aurez besoin du chemin vers la bibliothèque de l'agent YourKit (`yjpagent.dll`).

2. **Localiser l'agent YourKit**
   - L'agent YourKit pour Windows se trouve généralement à l'emplacement :
     ```
     C:\Program Files\YourKit-Java-Profiler-<version>\bin\win64\yjpagent.dll
     ```
     (Utilisez `win32` au lieu de `win64` si vous utilisez une JVM 32 bits.)
   - Assurez-vous que l'agent correspond à l'architecture de la JVM (32 bits ou 64 bits) utilisée par WebSphere Liberty.

3. **Configurer WebSphere Liberty pour utiliser l'agent YourKit**
   - **Localiser le fichier `jvm.options`** :
     - Accédez au répertoire de configuration de votre serveur WebSphere Liberty, généralement :
       ```
       <LIBERTY_INSTALL_DIR>\usr\servers\<server_name>\jvm.options
       ```
       Remplacez `<LIBERTY_INSTALL_DIR>` par le chemin de votre installation WebSphere Liberty (par exemple, `C:\wlp`), et `<server_name>` par le nom de votre serveur (par exemple, `defaultServer`).
     - Si le fichier `jvm.options` n'existe pas, créez-le dans le répertoire du serveur.
   - **Ajouter le chemin de l'agent YourKit** :
     - Ouvrez `jvm.options` dans un éditeur de texte avec des privilèges administratifs.
     - Ajoutez la ligne suivante pour inclure l'agent YourKit :
       ```
       -agentpath:C:\Program Files\YourKit-Java-Profiler-<version>\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
       ```
       - Remplacez `<version>` par votre version de YourKit (par exemple, `2023.9`).
       - Les options (`disablestacktelemetry`, `disableexceptiontelemetry`, `probe_disable=*`) réduisent la surcharge en désactivant la télémétrie non nécessaire. Le `delay=10000` assure que l'agent démarre après l'initialisation du serveur, et `sessionname=WebSphereLiberty` identifie la session de profilage.
       - Exemple :
         ```
         -agentpath:C:\Program Files\YourKit-Java-Profiler-2023.9\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
         ```
   - **Sauvegarder le fichier** : Assurez-vous d'avoir les permissions d'écriture pour le fichier `jvm.options`.

4. **Vérifier la compatibilité JVM**
   - WebSphere Liberty utilise souvent IBM JDK ou OpenJDK. YourKit est compatible avec les deux, mais si vous rencontrez des problèmes (par exemple, `NoSuchMethodError` comme noté dans certains cas IBM JDK), ajoutez `probe_disable=*` au chemin de l'agent pour désactiver les sondes qui peuvent causer des conflits avec IBM JDK.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=8042)
   - Vérifiez la version Java utilisée par Liberty :
     ```
     <LIBERTY_INSTALL_DIR>\java\bin\java -version
     ```
     Assurez-vous qu'elle est prise en charge par YourKit (Java 5 ou ultérieur pour les anciennes versions ; les versions modernes prennent en charge Java 8+).

5. **Démarrer WebSphere Liberty**
   - Démarrez votre serveur WebSphere Liberty comme d'habitude :
     ```
     <LIBERTY_INSTALL_DIR>\bin\server start <server_name>
     ```
     Exemple :
     ```
     C:\wlp\bin\server start defaultServer
     ```
   - Vérifiez les journaux du serveur (`<LIBERTY_INSTALL_DIR>\usr\servers\<server_name>\logs\console.log` ou `messages.log`) pour toute erreur liée à l'agent YourKit.
   - Recherchez le journal de l'agent YourKit dans :
     ```
     %USERPROFILE%\.yjp\log\<session_name>-<pid>.log
     ```
     Exemple :
     ```
     C:\Users\<YourUsername>\.yjp\log\WebSphereLiberty-<pid>.log
     ```
     Le journal devrait indiquer que l'agent est chargé et écoute sur un port (par défaut : 10001) :
     ```
     Profiler agent is listening on port 10001
     ```

6. **Connecter l'interface utilisateur YourKit Profiler**
   - Lancez l'interface utilisateur YourKit Java Profiler sur votre machine Windows.
   - Dans l'interface utilisateur YourKit, sélectionnez **Profile | Profile Local Java Server or Application** ou **Profile | Profile Remote Java Server or Application**.
     - Pour le profilage local (puisque YourKit et Liberty sont sur la même machine), choisissez **Profile Local Java Server or Application**.
     - L'interface utilisateur devrait détecter le processus WebSphere Liberty (identifié par `sessionname=WebSphereLiberty`).
   - S'il n'est pas détecté automatiquement, utilisez **Profile Remote Java Server or Application**, sélectionnez **Direct Connect**, et entrez :
     - **Host** : `localhost`
     - **Port** : `10001` (ou le port spécifié dans le journal de l'agent).
   - Connectez-vous au serveur. L'interface utilisateur affichera la télémétrie CPU, mémoire et threads.

7. **Profiler l'application**
   - Utilisez l'interface utilisateur YourKit pour :
     - **Profilage CPU** : Activez l'échantillonnage ou le traçage CPU pour identifier les goulots d'étranglement de performance. Évitez d'activer "Profile J2EE" pour les systèmes à charge élevée afin de minimiser la surcharge.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)
     - **Profilage Mémoire** : Analysez l'utilisation du tas et détectez les fuites mémoire en regroupant les objets par application web (utile pour les applications hébergées sur Liberty).[](https://www.yourkit.com/docs/java-profiler/latest/help/webapps.jsp)
     - **Analyse des Threads** : Vérifiez les interblocages ou les threads gelés dans l'onglet Threads.[](https://www.yourkit.com/changes/)
   - Prenez des instantanés pour une analyse hors ligne si nécessaire (File | Save Snapshot).
   - Surveillez l'utilisation de la mémoire, car le profilage peut augmenter la consommation mémoire. Évitez les sessions de profilage longues sans surveillance.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

8. **Dépannage**
   - **Le serveur ne démarre pas ou devient injoignable** :
     - Vérifiez les journaux (`console.log`, `messages.log` et le journal de l'agent YourKit) pour des erreurs comme `OutOfMemoryError` ou `NoSuchMethodError`.[](https://www.yourkit.com/forum/viewtopic.php?t=328)[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
     - Assurez-vous que le `-agentpath` est ajouté au bon fichier `jvm.options` et correspond au script utilisé pour démarrer Liberty.[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
     - Si vous utilisez IBM JDK, essayez d'ajouter `probe_disable=*` au chemin de l'agent pour éviter les conflits.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=8042)
   - **ClassNotFoundException** :
     - Si vous voyez des erreurs comme `java.lang.ClassNotFoundException` (par exemple, pour `java.util.ServiceLoader`), assurez-vous que la version de l'agent YourKit est compatible avec votre JDK. Pour les anciens IBM JDKs (par exemple, Java 5), utilisez YourKit 8.0 ou une version antérieure.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=7149)
   - **Aucune donnée de profilage** :
     - Vérifiez que les versions de l'agent YourKit et de l'interface utilisateur correspondent. Des versions non concordantes peuvent causer des problèmes de connexion.[](https://www.yourkit.com/forum/viewtopic.php?t=328)
     - Assurez-vous que le serveur est accessible via le navigateur (par exemple, `https://localhost:9443` si vous utilisez SSL). Sinon, vérifiez les paramètres du pare-feu ou la configuration SSL.[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
   - **Problèmes de fichiers journaux** :
     - Si aucun journal YourKit n'est créé dans `~/.yjp/log/`, assurez-vous que le processus a les permissions d'écriture dans le répertoire personnel de l'utilisateur.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=3219)
   - **Impact sur les performances** :
     - Le profilage peut affecter les performances. Utilisez des paramètres minimaux (par exemple, désactivez la télémétrie de pile) pour les environnements de type production.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

9. **Optionnel : Utiliser l'Assistant d'Intégration YourKit**
   - YourKit fournit un Assistant d'Intégration de Serveur Java pour simplifier la configuration :
     - Lancez l'interface utilisateur YourKit et sélectionnez **Profile | Profile Local Java Server or Application**.
     - Choisissez **WebSphere Liberty** dans la liste des serveurs pris en charge (ou "Other Java application" si Liberty n'est pas listé).
     - Suivez l'assistant pour générer les paramètres `-agentpath` nécessaires et mettre à jour `jvm.options`. Assurez-vous d'avoir les permissions d'écriture pour les fichiers de configuration.[](https://www.yourkit.com/docs/java-profiler/latest/help/java-server-integration-wizard.jsp)
   - Ceci est particulièrement utile pour garantir des chemins et des paramètres corrects.

10. **Arrêter le profilage**
    - Pour désactiver le profilage, supprimez ou commentez la ligne `-agentpath` dans `jvm.options` et redémarrez le serveur.
    - Alternativement, arrêtez le serveur :
      ```
      <LIBERTY_INSTALL_DIR>\bin\server stop <server_name>
      ```

### Notes supplémentaires
- **Licence** : Aucune clé de licence n'est requise pour l'agent YourKit sur le serveur ; la licence est appliquée dans l'interface utilisateur YourKit. Pour le profilage à distance depuis une autre machine Windows, assurez-vous que l'interface utilisateur a une licence valide.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=11385)[](https://www.yourkit.com/forum/viewtopic.php?t=11385)
- **Profilage à distance** : Si vous profilez depuis une machine différente, assurez-vous de la connectivité réseau vers le port de l'agent (par défaut : 10001) et utilisez l'option **Profile Remote Java Server or Application** avec le nom d'hôte/l'adresse IP du serveur.
- **Considérations de performance** : Le profilage peut augmenter l'utilisation de la mémoire et du CPU. Pour les systèmes de production, commencez avec des options de profilage minimales (par exemple, échantillonnage CPU) et surveillez l'état de santé du serveur.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)
- **Compatibilité** : Si vous utilisez une ancienne version de WebSphere Liberty avec IBM JDK 1.4.2 ou 1.5, vous pourriez avoir besoin d'une ancienne version de YourKit (par exemple, 8.0 pour Java 5).[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=7149)[](https://stackoverflow.com/questions/61795/java-profiler-for-ibm-jvm-1-4-2-websphere-6-0-2)
- **Documentation** : Reportez-vous à la documentation officielle de YourKit pour les options de profilage détaillées : [YourKit Java Profiler Help](https://www.yourkit.com/docs/java/help/).[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

### Exemple de configuration
Voici un exemple de fichier `jvm.options` :
```
-Xmx4G
-Xms4G
-agentpath:C:\Program Files\YourKit-Java-Profiler-2023.9\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
```

### Tester la configuration
- Après avoir démarré le serveur, accédez à votre application (par exemple, `https://localhost:9443`) pour vous assurer qu'elle fonctionne.
- Dans l'interface utilisateur YourKit, vérifiez que les données de télémétrie (CPU, mémoire, threads) sont affichées.
- Si des problèmes surviennent, vérifiez le journal de l'agent YourKit et les journaux Liberty pour des erreurs.

Si vous rencontrez des erreurs spécifiques ou avez besoin d'aide pour une étape particulière, faites-le-moi savoir et je pourrai fournir une assistance supplémentaire !