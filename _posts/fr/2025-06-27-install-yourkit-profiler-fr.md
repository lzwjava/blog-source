---
audio: false
generated: true
lang: fr
layout: post
title: Installation du profileur Java YourKit sur Ubuntu
translated: true
type: note
---

Pour installer YourKit Java Profiler sur Ubuntu, suivez ces étapes en vous basant sur les informations disponibles sur le site web de YourKit :

1. **Télécharger le profileur** :
   - Visitez la page de téléchargement de YourKit Java Profiler à l'adresse [https://www.yourkit.com/java/profiler/download/](https://www.yourkit.com/java/profiler/download/).
   - Sélectionnez la version Linux de YourKit Java Profiler 2025.3, qui prend en charge Java 8 à Java 24 et est compatible avec Linux (y compris Ubuntu) sur des architectures comme arm32, arm64, ppc64le, x64 et x86. Assurez-vous que votre système répond aux [exigences système](https://www.yourkit.com/docs/java/system-requirements/) pour la compatibilité.

2. **Télécharger l'archive** :
   - Téléchargez l'archive `.zip` pour Linux (par exemple, `YourKit-JavaProfiler-2025.3-<build>.zip`). Le lien de téléchargement est disponible sur la page de téléchargement de YourKit.

3. **Dézipper l'archive** :
   - Ouvrez un terminal et naviguez vers le répertoire où se trouve le fichier téléchargé (par exemple, `~/Téléchargements`).
   - Dézippez l'archive en utilisant la commande suivante :
     ```bash
     unzip YourKit-JavaProfiler-2025.3-<build>.zip -d /opt/yourkit
     ```
     Remplacez `<build>` par le numéro de build réel du fichier téléchargé. Cette commande extrait le profileur vers `/opt/yourkit`. Vous pouvez choisir un autre répertoire si vous préférez.

4. **Exécuter le profileur** :
   - Naviguez vers le répertoire extrait :
     ```bash
     cd /opt/yourkit
     ```
   - Exécutez le profileur en utilisant le script fourni :
     ```bash
     ./bin/profiler.sh
     ```
     Cela lance l'interface utilisateur de YourKit Java Profiler.

5. **Optionnel : Installation sans surveillance avec clé de licence** :
   - Si vous avez une clé de licence et souhaitez automatiser l'installation, vous pouvez utiliser des options en ligne de commande pour accepter le CLUF et appliquer la clé de licence. Par exemple :
     ```bash
     ./bin/profiler.sh -accept-eula -license-key=<clé>
     ```
     Remplacez `<clé>` par votre véritable clé de licence. Ceci est utile pour l'automatisation ou les configurations scriptées.

6. **Intégrer avec l'environnement de développement (Optionnel)** :
   - Si vous utilisez un IDE comme Eclipse, IntelliJ IDEA ou NetBeans, YourKit fournit des plugins pour une intégration transparente. Pour Eclipse, par exemple :
     - Ouvrez Eclipse et allez dans **Aide > Installer un nouveau logiciel**.
     - Ajoutez le dépôt de plugins YourKit : `https://www.yourkit.com/download/yjp2025_3_for_eclipse/`.
     - Sélectionnez le plugin YourKit Java Profiler, suivez les invites d'installation et redémarrez Eclipse si nécessaire.
     - Alternativement, utilisez l'archive hors ligne située à `<Répertoire d'installation du profileur>/lib/eclipse-plugin/yjp2025_3_for_eclipse.zip`.
   - Après l'installation, l'action "Profile" apparaîtra dans la barre d'outils, le menu principal ou les menus contextuels d'Eclipse pour un profilage facile.

7. **Vérifier l'installation** :
   - Une fois le profileur en cours d'exécution, l'écran de bienvenue vous permettra de surveiller les applications Java en cours d'exécution localement, de vous connecter à des applications distantes ou d'ouvrir des snapshots existants. Vous pouvez également charger une application de démonstration pour explorer les fonctionnalités du profileur.

8. **Notes supplémentaires** :
   - Si vous rencontrez des problèmes, assurez-vous que Java (version 8 ou supérieure) est installé sur votre système, car YourKit Java Profiler nécessite une JVM compatible. Vous pouvez vérifier votre version de Java avec :
     ```bash
     java -version
     ```
   - Pour le profilage à distance, assurez-vous que l'accès SSH est configuré si vous profilez des applications sur des serveurs distants.
   - YourKit propose un essai gratuit de 15 jours, donc aucune clé de licence n'est requise initialement. Pour les projets open source non commerciaux, vous pouvez contacter le service commercial de YourKit pour obtenir une licence gratuite.
   - Si le profileur ne parvient pas à démarrer (par exemple, en raison d'espaces dans le répertoire d'installation), déplacez le dossier extrait vers un chemin sans espaces, tel que `/opt/yourkit`.

Pour une assistance supplémentaire, consultez la [documentation YourKit](https://www.yourkit.com/docs/java/) ou contactez leur support via le [site web YourKit](https://www.yourkit.com/support/).

Faites-moi savoir si vous avez besoin d'aide pour une étape spécifique !