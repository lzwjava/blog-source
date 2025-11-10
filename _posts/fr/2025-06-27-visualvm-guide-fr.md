---
audio: false
generated: true
lang: fr
layout: post
title: 'Guide Complet de VisualVM : Profilage et Surveillance Java'
translated: true
type: note
---

# Guide Complet de VisualVM

VisualVM est un outil puissant et open source de profilage et de surveillance Java qui fournit une interface graphique pour analyser les performances des applications Java. Il est inclus dans le Java Development Kit (JDK) et est particulièrement utile pour diagnostiquer les problèmes de performance, les fuites de mémoire et les problèmes liés aux threads. Ce guide couvre les fonctionnalités de VisualVM, son installation, son utilisation et les bonnes pratiques pour les développeurs et les administrateurs système.

## Table des matières
1. [Qu'est-ce que VisualVM ?](#quest-ce-que-visualvm)
2. [Fonctionnalités Clés de VisualVM](#fonctionnalités-clés-de-visualvm)
3. [Configuration Système Requise](#configuration-système-requise)
4. [Installation de VisualVM](#installation-de-visualvm)
5. [Lancement de VisualVM](#lancement-de-visualvm)
6. [Connexion aux Applications Java](#connexion-aux-applications-java)
7. [Utilisation de VisualVM pour la Surveillance et le Profilage](#utilisation-de-visualvm-pour-la-surveillance-et-le-profilage)
   - [Onglet Aperçu](#onglet-aperçu)
   - [Onglet Moniteur](#onglet-moniteur)
   - [Onglet Threads](#onglet-threads)
   - [Échantillonneur](#échantillonneur)
   - [Profileur](#profileur)
   - [Analyse des Heap Dumps](#analyse-des-heap-dumps)
   - [Analyse des Thread Dumps](#analyse-des-thread-dumps)
   - [MBeans](#mbeans)
8. [Surveillance à Distance](#surveillance-à-distance)
9. [Extension de VisualVM avec des Plugins](#extension-de-visualvm-avec-des-plugins)
10. [Bonnes Pratiques](#bonnes-pratiques)
11. [Résolution des Problèmes Courants](#résolution-des-problèmes-courants)
12. [Ressources Supplémentaires](#ressources-supplémentaires)

## Qu'est-ce que VisualVM ?

VisualVM est un outil basé sur Java qui intègre plusieurs utilitaires du JDK (comme `jstack`, `jmap` et `jconsole`) dans une interface unique et conviviale. Il permet aux développeurs de surveiller les applications Java en temps réel, de profiler l'utilisation du CPU et de la mémoire, d'analyser les heap dumps et de gérer les threads. VisualVM est particulièrement précieux pour identifier les goulots d'étranglement de performance, les fuites de mémoire et les problèmes de threading dans les applications Java locales et distantes.

Développé à l'origine par Sun Microsystems, VisualVM fait maintenant partie de l'Oracle JDK et est activement maintenu en tant que projet open source. Il prend en charge les applications Java s'exécutant sur JDK 6 et versions ultérieures.

## Fonctionnalités Clés de VisualVM

- **Surveillance en Temps Réel** : Suit l'utilisation du CPU, la consommation de mémoire, l'activité des threads et le garbage collection.
- **Profilage** : Offre le profilage du CPU et de la mémoire pour identifier les goulots d'étranglement de performance et les modèles d'allocation mémoire.
- **Analyse des Heap Dumps** : Permet d'inspecter le contenu de la mémoire pour diagnostiquer les fuites de mémoire.
- **Analyse des Thread Dumps** : Aide à analyser les états des threads et à détecter les interblocages.
- **Gestion des MBeans** : Fournit un accès aux Java Management Extensions (JMX) pour surveiller et gérer les applications.
- **Surveillance à Distance** : Prend en charge la surveillance des applications Java s'exécutant sur des machines distantes.
- **Extensibilité** : Prend en charge les plugins pour étendre les fonctionnalités, comme l'intégration avec des frameworks spécifiques ou des outils de profilage supplémentaires.
- **Léger et Facile à Utiliser** : Configuration minimale avec une interface graphique intuitive.

## Configuration Système Requise

Pour utiliser VisualVM, assurez-vous des éléments suivants :
- **Système d'Exploitation** : Windows, macOS, Linux ou tout OS prenant en charge une JVM.
- **Version de Java** : JDK 6 ou ultérieur (VisualVM est inclus avec JDK 8 et versions ultérieures).
- **Mémoire** : Au moins 512 Mo de RAM libre pour une surveillance légère ; 1 Go ou plus pour l'analyse des heap dumps.
- **Espace Disque** : Environ 50 Mo pour l'installation de VisualVM.
- **Permissions** : Des privilèges d'administrateur peuvent être requis pour certaines fonctionnalités (par exemple, accéder aux processus système).

## Installation de VisualVM

VisualVM est inclus avec Oracle JDK 8 et versions ultérieures, situé dans le répertoire `bin` de l'installation du JDK (exécutable `jvisualvm`). Alternativement, vous pouvez le télécharger en tant qu'application autonome :

1. **Depuis le JDK** :
   - Si vous avez JDK 8 ou une version ultérieure installé, VisualVM est déjà disponible dans le répertoire `JAVA_HOME/bin` sous le nom `jvisualvm`.
   - Exécutez l'exécutable `jvisualvm` pour lancer l'outil.

2. **Téléchargement Autonome** :
   - Visitez le [site web de VisualVM](https://visualvm.github.io/) pour télécharger la dernière version autonome.
   - Extrayez le fichier ZIP dans un répertoire de votre choix.
   - Exécutez l'exécutable `visualvm` (par exemple, `visualvm.exe` sur Windows).

3. **Vérification de l'Installation** :
   - Assurez-vous que la variable d'environnement `JRE_HOME` ou `JAVA_HOME` pointe vers un JDK/JRE compatible.
   - Testez en lançant VisualVM.

## Lancement de VisualVM

Pour démarrer VisualVM :
- **Sur Windows** : Double-cliquez sur `jvisualvm.exe` dans le dossier `bin` du JDK ou le répertoire d'installation autonome.
- **Sur macOS/Linux** : Exécutez `./jvisualvm` depuis le terminal dans le répertoire `bin`.
- L'interface VisualVM s'ouvrira, affichant une liste des applications Java locales dans le panneau de gauche.

## Connexion aux Applications Java

VisualVM peut surveiller les applications Java locales et distantes.

### Applications Locales
- Au lancement, VisualVM détecte automatiquement les applications Java en cours d'exécution sur la machine locale.
- Double-cliquez sur une application dans le panneau de gauche pour ouvrir son tableau de bord de surveillance.
- Si une application n'est pas listée, assurez-vous qu'elle s'exécute sous une JVM compatible.

### Applications Distantes
Pour surveiller une application Java distante :
1. Activez JMX sur l'application distante en ajoutant des arguments JVM (par exemple, `-Dcom.sun.management.jmxremote`).
2. Dans VisualVM, allez dans **Fichier > Ajouter une connexion JMX**.
3. Entrez l'adresse IP de l'hôte distant et le port (par exemple, `nom_hôte:port`).
4. Fournissez les informations d'identification si l'authentification est activée.
5. Connectez-vous et surveillez l'application.

**Remarque** : Pour les connexions sécurisées, configurez SSL et l'authentification si nécessaire (voir [Surveillance à Distance](#surveillance-à-distance)).

## Utilisation de VisualVM pour la Surveillance et le Profilage

VisualVM fournit plusieurs onglets et outils pour analyser les applications Java. Voici un détail de chaque fonctionnalité.

### Onglet Aperçu
- Affiche des informations générales sur l'application, y compris :
  - Les arguments JVM
  - Les propriétés système
  - Le classpath de l'application
  - Le PID (Identifiant de Processus)
- Utile pour vérifier la configuration de l'application.

### Onglet Moniteur
- Fournit des graphiques en temps réel pour :
  - **Utilisation du CPU** : Suit l'utilisation du CPU de l'application et du système.
  - **Mémoire TAS (Heap)** : Surveille l'utilisation du tas (Eden, Old Gen, PermGen/Metaspace) et l'activité du garbage collection.
  - **Classes** : Affiche le nombre de classes chargées.
  - **Threads** : Affiche le nombre de threads actifs et de threads démons.
- Permet de déclencher manuellement le garbage collection ou les heap dumps.

### Onglet Threads
- Visualise les états des threads (En cours d'exécution, En sommeil, En attente, etc.) au fil du temps.
- Fournit une fonctionnalité de thread dump pour capturer l'état actuel de tous les threads.
- Utile pour identifier les interblocages, les threads bloqués ou une utilisation excessive des threads.

### Échantillonneur
- Offre un échantillonnage léger du CPU et de la mémoire pour l'analyse des performances.
- **Échantillonnage du CPU** :
  - Capture le temps d'exécution au niveau méthode.
  - Identifie les méthodes "chaudes" consommant le plus de temps CPU.
- **Échantillonnage de la Mémoire** :
  - Suit les allocations d'objets et l'utilisation de la mémoire.
  - Aide à identifier les objets consommant une mémoire excessive.
- L'échantillonnage a un impact plus faible que le profilage mais fournit des données moins détaillées.

### Profileur
- Fournit un profilage approfondi du CPU et de la mémoire.
- **Profilage du CPU** :
  - Mesure le temps d'exécution des méthodes.
  - Identifie les goulots d'étranglement de performance au niveau méthode.
- **Profilage de la Mémoire** :
  - Suit les allocations d'objets et les références.
  - Aide à détecter les fuites de mémoire en identifiant les objets qui persistent de manière inattendue.
- **Remarque** : Le profilage a un impact plus élevé que l'échantillonnage et peut ralentir l'application.

### Analyse des Heap Dumps
- Un heap dump est un instantané de la mémoire de l'application.
- Pour générer un heap dump :
  1. Allez dans l'onglet **Moniteur**.
  2. Cliquez sur **Heap Dump**.
  3. Sauvegardez le dump dans un fichier `.hprof` ou analysez-le directement dans VisualVM.
- Fonctionnalités :
  - Voir les instances de classe, les tailles et les références.
  - Identifier les objets avec une utilisation mémoire élevée.
  - Détecter les fuites de mémoire en analysant les chemins de rétention d'objets.
- Utilisez la console **OQL (Object Query Language)** pour des requêtes avancées sur le tas.

### Analyse des Thread Dumps
- Capture l'état de tous les threads à un moment spécifique.
- Pour générer un thread dump :
  1. Allez dans l'onglet **Threads**.
  2. Cliquez sur **Thread Dump**.
  3. Analysez le dump dans VisualVM ou exportez-le pour des outils externes.
- Utile pour diagnostiquer :
  - Les interblocages
  - Les threads bloqués
  - Les problèmes de contention de threads

### MBeans
- Accède aux MBeans JMX pour gérer et surveiller l'application.
- Fonctionnalités :
  - Voir et modifier les attributs des MBeans.
  - Invoquer les opérations des MBeans.
  - Surveiller les notifications des MBeans.
- Utile pour les applications avec une instrumentation JMX personnalisée.

## Surveillance à Distance

Pour surveiller les applications Java distantes :
1. **Configurer la JVM Distante** :
   - Ajoutez les arguments JVM suivants à l'application distante :
     ```bash
     -Dcom.sun.management.jmxremote
     -Dcom.sun.management.jmxremote.port=<port>
     -Dcom.sun.management.jmxremote.ssl=false
     -Dcom.sun.management.jmxremote.authenticate=false
     ```
   - Pour les connexions sécurisées, activez SSL et l'authentification :
     ```bash
     -Dcom.sun.management.jmxremote.ssl=true
     -Dcom.sun.management.jmxremote.authenticate=true
     -Dcom.sun.management.jmxremote.password.file=<fichier_mot_de_passe>
     ```
2. **Configurer VisualVM** :
   - Ajoutez une connexion JMX dans VisualVM en utilisant l'IP et le port de l'hôte distant.
   - Fournissez les informations d'identification si nécessaire.
3. **Configuration du Pare-feu** :
   - Assurez-vous que le port JMX est ouvert sur l'hôte distant.
   - Utilisez le tunneling SSH pour un accès distant sécurisé si nécessaire :
     ```bash
     ssh -L <port_local>:<hôte_distant>:<port_distant> utilisateur@hôte_distant
     ```

## Extension de VisualVM avec des Plugins

VisualVM prend en charge les plugins pour améliorer ses fonctionnalités :
1. **Installer des Plugins** :
   - Allez dans **Outils > Plugins**.
   - Parcourez le Centre de Plugins pour les plugins disponibles (par exemple, Visual GC, BTrace, plugins JConsole).
   - Installez et redémarrez VisualVM.
2. **Plugins Populaires** :
   - **Visual GC** : Visualise l'activité du garbage collection.
   - **BTrace** : Fournit un traçage dynamique pour les applications Java.
   - **Plugins JConsole** : Ajoute des fonctionnalités compatibles JConsole.
3. **Plugins Personnalisés** :
   - Téléchargez des plugins depuis le site web de VisualVM ou des sources tierces.
   - Placez les fichiers du plugin dans le répertoire `plugins` et redémarrez VisualVM.

## Bonnes Pratiques

- **Commencez par l'Échantillonnage** : Utilisez l'échantillonnage avant le profilage pour minimiser l'impact sur les performances.
- **Limitez la Portée du Profilage** : Profilez des packages ou des classes spécifiques pour réduire l'impact.
- **Heap Dumps Réguliers** : Planifiez des heap dumps périodiques pour les applications de longue durée afin de suivre les tendances mémoire.
- **Surveillez le Garbage Collection** : Utilisez le plugin Visual GC pour analyser les performances du GC.
- **Sécurisez les Connexions Distantes** : Utilisez toujours SSL et l'authentification pour la surveillance à distance.
- **Sauvegardez les Instantanés** : Sauvegardez les heap dumps et thread dumps pour une analyse ultérieure ou une collaboration.
- **Utilisez OQL pour une Analyse Avancée** : Apprenez OQL pour des requêtes efficaces sur les heap dumps.
- **Surveillez l'Utilisation des Ressources** : Assurez-vous que VisualVM dispose de suffisamment de mémoire pour les gros heap dumps.

## Résolution des Problèmes Courants

- **Application Non Détectée** :
  - Assurez-vous que l'application s'exécute sur une JVM compatible.
  - Vérifiez si la JVM est configurée pour autoriser les connexions JMX.
- **Impact Élevé Pendant le Profilage** :
  - Passez à l'échantillonnage pour un impact plus faible.
  - Profilez des classes ou des méthodes spécifiques.
- **Problèmes de Connexion pour la Surveillance à Distance** :
  - Vérifiez le port JMX et les paramètres du pare-feu.
  - Testez la connectivité en utilisant `telnet <hôte> <port>`.
- **OutOfMemoryError dans VisualVM** :
  - Augmentez la taille du tas de VisualVM en éditant le fichier `visualvm.conf` :
    ```bash
    -J-Xmx<taille_mémoire>m
    ```
- **L'Analyse des Heap Dumps est Lente** :
  - Utilisez une machine avec plus de RAM.
  - Filtrez les classes pour réduire la portée de l'analyse.

## Ressources Supplémentaires

- **Site Web Officiel** : [visualvm.github.io](https://visualvm.github.io/)
- **Documentation** : [Documentation VisualVM](https://visualvm.github.io/documentation.html)
- **Tutoriels** :
  - [Guide VisualVM d'Oracle](https://www.oracle.com/java/technologies/visualvm.html)
  - [Java Performance Tuning with VisualVM](https://www.baeldung.com/java-visualvm)
- **Communauté** :
  - [VisualVM GitHub Issues](https://github.com/visualvm/visualvm.github.io/issues)
  - [Stack Overflow VisualVM Tag](https://stackoverflow.com/questions/tagged/visualvm)