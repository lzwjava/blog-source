---
audio: false
lang: fr
layout: post
title: Profilage des applications Java avec VisualVM
translated: true
---

Voici un guide clair et concis sur **comment utiliser VisualVM** pour surveiller et profiler les applications Java. VisualVM est un outil gratuit et puissant inclus avec le JDK qui vous aide à analyser les performances, l'utilisation de la mémoire et l'activité des threads dans vos applications Java.

---

### Étape 1 : Installer et lancer VisualVM
- **Vérifiez si VisualVM est installé** : VisualVM est généralement inclus avec le JDK (version 6 mise à jour 7 et ultérieures). Recherchez-le dans le répertoire `bin` de votre installation JDK (par exemple, `jdk/bin/visualvm.exe` sous Windows).
- **Téléchargez si nécessaire** : Si ce n'est pas inclus, téléchargez-le depuis le [site officiel de VisualVM](https://visualvm.github.io/).
- **Lancez VisualVM** : Exécutez l'exécutable `visualvm`. Lorsqu'il démarre, vous verrez une liste des processus Java actuellement en cours d'exécution sur votre machine locale.

---

### Étape 2 : Se connecter à votre application Java
- **Applications locales** : VisualVM détecte automatiquement les processus Java en cours d'exécution sur votre machine. Double-cliquez sur le processus que vous souhaitez surveiller pour vous y connecter.
- **Applications distantes** : Pour surveiller un processus Java sur une autre machine :
  1. Démarrez la JVM distante avec JMX activé (par exemple, ajoutez `-Dcom.sun.management.jmxremote` aux arguments de la JVM).
  2. Dans VisualVM, faites un clic droit sur **Remote** dans le panneau de gauche, sélectionnez **Add Remote Host**, et entrez les détails de la machine distante.
  3. Une fois connecté, sélectionnez le processus distant à surveiller.

---

### Étape 3 : Surveiller les performances de l'application
Après la connexion, l'onglet **Overview** affiche des détails de base comme l'ID du processus et les arguments de la JVM. Passez à l'onglet **Monitor** pour obtenir des données de performance en temps réel :
- **Utilisation du CPU** : Suit la quantité de CPU utilisée par votre application.
- **Utilisation de la mémoire** : Affiche la consommation de l'heap et du metaspace au fil du temps.
- **Threads** : Affiche le nombre de threads actifs.
- **Collecte des ordures** : Surveille l'activité de la collecte des ordures.

Ces graphiques vous donnent une vue d'ensemble de la santé de votre application.

---

### Étape 4 : Profiler l'utilisation du CPU et de la mémoire
Pour une analyse plus approfondie, utilisez l'onglet **Profiler** :
- **Profilage du CPU** : Identifie les méthodes qui consomment le plus de temps CPU.
  1. Allez à l'onglet **Profiler** et cliquez sur **CPU**.
  2. Cliquez sur **Start** pour commencer le profilage.
  3. Utilisez votre application pour générer la charge de travail que vous souhaitez analyser.
  4. Cliquez sur **Stop** et examinez les résultats pour voir quelles méthodes sont les plus lentes.
- **Profilage de la mémoire** : Suit les allocations d'objets et détecte les fuites de mémoire.
  1. Dans l'onglet **Profiler**, cliquez sur **Memory**.
  2. Cliquez sur **Start**, utilisez votre application, puis cliquez sur **Stop**.
  3. Vérifiez les résultats pour les comptes et tailles d'objets afin de repérer d'éventuels problèmes de mémoire.

**Note** : Le profilage ajoute une surcharge, utilisez-le donc dans des environnements de développement ou de test, pas en production.

---

### Étape 5 : Analyser les dumps de l'heap et des threads
- **Dumps de l'heap** : Capturez des instantanés de la mémoire pour une analyse détaillée.
  1. Dans l'onglet **Monitor**, cliquez sur **Heap Dump**.
  2. Explorez le dump dans les vues **Classes** ou **Instances** pour voir les allocations d'objets.
  3. Recherchez des motifs inhabituels (par exemple, trop d'objets) qui pourraient indiquer des fuites.
- **Dumps des threads** : Diagnostiquez les problèmes de threading comme les deadlocks.
  1. Dans l'onglet **Threads**, cliquez sur **Thread Dump**.
  2. Vérifiez les états des threads (par exemple, RUNNABLE, WAITING) pour identifier les problèmes.

---

### Étape 6 : Explorer les fonctionnalités supplémentaires
- **Sampler** : Trouvé dans l'onglet **Sampler**, il fournit une analyse légère du CPU et de la mémoire avec moins de surcharge qu'un profilage complet.
- **Visual GC** : Installez le plugin Visual GC (via **Tools > Plugins**) pour visualiser le comportement de la collecte des ordures.
- **MBeans** : Utilisez l'onglet **MBeans** pour afficher et gérer les beans JMX pour des métriques personnalisées.

---

### Meilleures pratiques
- **Évitez le profilage en production** : Le profilage ralentit votre application, donc restez sur les configurations de développement ou de test.
- **Commencez simplement** : Utilisez l'onglet **Monitor** en premier pour obtenir une ligne de base avant de profiler.
- **Ciblez des problèmes spécifiques** : Concentrez le profilage sur les zones problématiques suspectées pour minimiser la surcharge.
- **Revuez les données GC** : Analysez les statistiques de la collecte des ordures pour optimiser l'utilisation de la mémoire.

---

### Dépannage
- **Application non affichée** : Assurez-vous qu'elle s'exécute avec une JVM compatible et que VisualVM y a accès.
- **Problèmes distants** : Confirmez que la JVM distante est configurée pour JMX et que les paramètres réseau (par exemple, les pare-feu) permettent la connexion.
- **Impact sur les performances** : Si le profilage est trop lent, passez au **Sampler** pour une option plus légère.

---

VisualVM est un excellent outil pour comprendre et optimiser vos applications Java. Suivez ces étapes pour surveiller les performances, profiler les goulots d'étranglement et diagnostiquer les problèmes efficacement. Pour plus de détails, consultez la [documentation officielle de VisualVM](https://visualvm.github.io/documentation.html).