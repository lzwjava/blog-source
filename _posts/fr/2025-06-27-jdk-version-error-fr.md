---
audio: false
generated: true
lang: fr
layout: post
title: Corriger l'Erreur 'Unsupported OpenJDK' dans VisualVM
translated: true
type: note
---

L'erreur « Version of OpenJDK is not supported. Please use the default-jdk » lors de l'exécution de VisualVM indique que la version du Java Development Kit (JDK) utilisée n'est pas compatible avec VisualVM. Ce problème est courant lorsque VisualVM ne parvient pas à trouver un JDK pris en charge ou lorsque le JDK installé n'est pas correctement configuré. Voici les étapes pour résoudre ce problème, en fonction du contexte de votre configuration (YourKit Java Profiler 2025.3 et VisualVM sur ce qui semble être un système Linux).

### Étapes pour Corriger le Problème

1.  **Vérifier Votre Version Java Actuelle**
    Exécutez la commande suivante pour vérifier la version de Java installée :
    ```bash
    java -version
    ```
    Cela affichera la version d'OpenJDK, par exemple :
    ```
    openjdk version "17.0.9" 2023-10-17
    OpenJDK Runtime Environment (build 17.0.9+9-Ubuntu-122.04)
    OpenJDK 64-Bit Server VM (build 17.0.9+9-Ubuntu-122.04, mixed mode, sharing)
    ```
    VisualVM nécessite généralement un JDK (et pas seulement un JRE) et prend en charge Oracle JDK 8+ ou les versions OpenJDK compatibles. Assurez-vous d'avoir un JDK pris en charge installé.[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://visualvm.github.io/troubleshooting.html)

2.  **Installer le JDK par Défaut**
    L'erreur suggère d'utiliser le `default-jdk`. Sur Ubuntu/Debian, vous pouvez l'installer avec :
    ```bash
    sudo apt update
    sudo apt install default-jdk
    ```
    Cela installe généralement une version OpenJDK stable et prise en charge (par exemple, OpenJDK 11 ou 17). Après l'installation, vérifiez à nouveau la version avec `java -version`.[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

3.  **Définir la Variable d'Environnement JAVA_HOME**
    VisualVM s'appuie sur la variable d'environnement `JAVA_HOME` pour localiser le JDK. Vérifiez si elle est définie :
    ```bash
    echo $JAVA_HOME
    ```
    Si elle n'est pas définie ou pointe vers un JDK non pris en charge, définissez-la sur le chemin correct du JDK. Par exemple, si `default-jdk` a installé OpenJDK 17, le chemin pourrait être `/usr/lib/jvm/java-17-openjdk-amd64`. Définissez-la avec :
    ```bash
    export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
    ```
    Pour rendre cette modification permanente, ajoutez la ligne à votre `~/.bashrc` ou `~/.zshrc` :
    ```bash
    echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
    source ~/.bashrc
    ```
    Remplacez le chemin par le chemin réel du JDK sur votre système (utilisez `update-alternatives --list java` pour le trouver).[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://github.com/oracle/visualvm/issues/558)

4.  **Spécifier le Chemin du JDK pour VisualVM**
    Si la définition de `JAVA_HOME` ne résout pas le problème, vous pouvez spécifier explicitement le chemin du JDK lors du lancement de VisualVM :
    ```bash
    ~/bin/YourKit-JavaProfiler-2025.3/bin/visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64
    ```
    Remplacez `/usr/lib/jvm/java-17-openjdk-amd64` par le chemin vers votre JDK. Cela garantit que VisualVM utilise le JDK spécifié.[](https://visualvm.github.io/download.html)[](https://notepad.onghu.com/2021/solve-visualvm-does-not-start-on-windows-openjdk/)

5.  **Installer un JDK Compatible**
    Si le `default-jdk` est toujours incompatible, envisagez d'installer une version spécifique de JDK connue pour fonctionner avec VisualVM, telle que OpenJDK 11 ou Oracle JDK 8+ :
    ```bash
    sudo apt install openjdk-11-jdk
    ```
    Ensuite, mettez à jour `JAVA_HOME` ou utilisez l'option `--jdkhome` comme décrit ci-dessus.[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)

6.  **Vérifier l'Installation de VisualVM**
    Assurez-vous que VisualVM est correctement installé. L'erreur suggère que vous exécutez VisualVM depuis le répertoire YourKit Java Profiler (`~/bin/YourKit-JavaProfiler-2025.3/bin`). Ceci est inhabituel, car VisualVM est généralement un outil autonome ou fourni avec un JDK. Vérifiez que VisualVM n'est pas corrompu :
    - Téléchargez la dernière version de VisualVM depuis `visualvm.github.io/download.html` (par exemple, VisualVM 2.2, publiée le 22 avril 2025, prend en charge JDK 24).[](https://visualvm.github.io/relnotes.html)[](https://visualvm.github.io/)
    - Décompressez-la dans un nouveau répertoire et exécutez-la :
      ```bash
      unzip visualvm_22.zip
      cd visualvm_22/bin
      ./visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64
      ```
    Évitez de décompresser par-dessus une installation VisualVM existante, car cela peut causer des problèmes.[](https://visualvm.github.io/troubleshooting.html)

7.  **Vérifier les Installations Multiples de Java**
    Plusieurs versions de Java peuvent causer des conflits. Listez toutes les versions de Java installées :
    ```bash
    update-alternatives --list java
    ```
    Si plusieurs versions sont listées, définissez celle souhaitée par défaut :
    ```bash
    sudo update-alternatives --config java
    ```
    Sélectionnez le numéro correspondant au JDK compatible (par exemple, OpenJDK 11 ou 17).[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

8.  **Vérifier les Dépendances de VisualVM**
    VisualVM nécessite `libnb-platform18-java` et `libvisualvm-jni`. Assurez-vous qu'elles sont installées :
    ```bash
    sudo apt install libnb-platform18-java libvisualvm-jni
    ```
    Ceci est particulièrement pertinent si vous avez installé VisualVM via `apt`.[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

9.  **Contourner les Restrictions OpenJDK (Optionnel)**
    Si vous utilisez une version OpenJDK non prise en charge (par exemple, IcedTea ou AdoptOpenJDK), les fonctionnalités de profilage peuvent être limitées. Vous pouvez contourner certaines restrictions en ajoutant un argument en ligne de commande :
    ```bash
    ./visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64 -J-Dorg.graalvm.visualvm.profiler.SupportAllVMs=true
    ```
    Cela active le profilage pour les JVM non prises en charge, bien que cela ne garantisse pas un fonctionnement parfait.[](https://github.com/oracle/visualvm/issues/143)

10. **Vérifier la Compatibilité YourKit et VisualVM**
    Étant donné que vous exécutez VisualVM depuis le répertoire YourKit Java Profiler, assurez-vous que l'environnement YourKit n'interfère pas. YourKit Java Profiler 2025.3 peut inclure une version ou une configuration spécifique de VisualVM. Consultez la documentation de YourKit ou contactez `support@yourkit.com` pour confirmer la compatibilité avec votre JDK. Alternativement, essayez d'exécuter VisualVM indépendamment (téléchargé séparément) pour isoler le problème.[](https://www.yourkit.com/changes/)

### Notes Supplémentaires

-   **Contexte YourKit** : L'erreur n'est pas directement liée à YourKit Java Profiler, mais l'exécution de VisualVM depuis le répertoire de YourKit suggère une intégration. YourKit prend en charge Java 7–15 et les versions ultérieures avec les builds EAP, alors assurez-vous que votre JDK est compatible avec les deux outils s'ils sont utilisés ensemble.[](https://www.yourkit.com/forum/viewtopic.php?t=41723)[](https://www.yourkit.com/forum/viewtopic.php?t=40299)
-   **Fichiers de Log** : Vérifiez les logs de VisualVM pour plus de détails. Les logs se trouvent généralement dans `~/.visualvm/<version>/var/log`. Pour YourKit, vérifiez `~/.yjp/log/` pour les logs de l'agent de profilage. Si les problèmes persistent, envoyez les logs à `support@yourkit.com`.[](https://stackoverflow.com/questions/70211315/java-17-and-yourkit-2021-11)[](https://www.yourkit.com/forum/viewtopic.php?t=40299)
-   **Alternative** : Si VisualVM continue d'échouer, envisagez d'utiliser les outils de profilage intégrés de YourKit ou un autre profileur comme JProfiler ou Async Profiler, qui pourraient avoir une meilleure compatibilité avec votre configuration.[](https://digma.ai/9-best-java-profilers-to-use-in-2024/)[](https://bell-sw.com/blog/a-guide-to-java-profiling-tools-techniques-best-practices/)

### Si le Problème Persiste

Si aucune des solutions ci-dessus ne résout le problème, veuillez fournir :
- La sortie de `java -version` et `echo $JAVA_HOME`.
- La sortie de `update-alternatives --list java`.
- La version exacte de VisualVM (vérifiez via `visualvm --help` ou la page de téléchargement).
- Indiquez si vous utilisez VisualVM fourni avec YourKit ou une installation autonome.

Cela aidera à identifier plus précisément le problème. Vous pouvez également signaler le problème sur la page GitHub de VisualVM (`https://github.com/oracle/visualvm`) ou contacter le support YourKit pour une assistance spécifique.[](https://github.com/oracle/visualvm/issues/558)