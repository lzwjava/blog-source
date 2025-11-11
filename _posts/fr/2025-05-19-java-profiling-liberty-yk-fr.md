---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Profiler Liberty avec YourKit Java Profiler
translated: true
type: note
---

WebSphere Liberty peut être intégré assez facilement avec YourKit Java Profiler, étant donné que Liberty est simplement un autre runtime basé sur JVM. Voici comment cela fonctionne généralement :

---

### 1. Fonctionnement de l'intégration

YourKit Java Profiler n'a pas besoin de plugins spécifiques à Liberty ; il fonctionne en s'attachant au processus JVM dans lequel Liberty s'exécute. Une fois attaché, il intercepte les appels de méthode, les allocations mémoire, l'activité des threads et d'autres événements d'exécution.
Liberty s'exécute sur la JVM OpenJ9 (ou HotSpot), vous pouvez donc activer le profilage en ajoutant l'agent YourKit au démarrage de Liberty.

---

### 2. Attachement de l'agent YourKit

Il existe deux méthodes principales :

* **Attachement au démarrage (préféré pour les serveurs)**
  Ajoutez les options de l'agent YourKit au fichier `jvm.options` de Liberty (dans `<wlp_home>/usr/servers/<nom_serveur>/`).
  Exemple :

  ```
  -agentpath:/chemin/vers/yourkit/bin/linux-x86-64/libyjpagent.so=port=10001,listen=all
  ```

  Cela charge l'agent du profileur dès le démarrage du serveur.

* **Attachement à la volée (dynamique)**
  Si Liberty est déjà en cours d'exécution, vous pouvez attacher YourKit via l'interface graphique. Celui-ci scanne les JVM en cours d'exécution et vous permet de vous connecter sans redémarrage. Utile pour le débogage en production, mais nécessite des autorisations (même utilisateur / tools.jar du JDK).

---

### 3. Profilage dans le contexte Liberty

Lorsque vous exécutez sur Liberty, vous pouvez souhaiter :

* **Filtrer par packages d'application** afin de ne pas être submergé par le code interne de Liberty.
* **Utiliser la vue arbre des appels / points chauds** pour analyser les servlets lentes, les endpoints JAX-RS ou les beans CDI.
* **Surveiller les pools JDBC et de threads** car les applications Liberty reposent souvent sur des ressources gérées par le conteneur. YourKit peut tracer les appels JDBC et mesurer les temps d'attente.
* **Gérer plusieurs applications** – si Liberty héberge plusieurs applications, utilisez les filtres de threads et de classes de YourKit pour cibler le profilage sur celle qui vous intéresse.

---

### 4. Considérations sur les performances

* Le profilage ajoute toujours une surcharge. En développement, il est acceptable d'utiliser le profilage complet du CPU/mémoire ; en production, utilisez le mode *échantillonnage* au lieu de l'instrumentation.
* Le chargement de classes modulaire de Liberty peut parfois entraîner des noms de classes en double ; YourKit gère généralement cela, mais soyez vigilant lors du filtrage.
* Si vous utilisez IBM JDK avec Liberty, assurez-vous de télécharger l'agent YourKit conçu pour IBM J9/OpenJ9, et pas seulement pour HotSpot.

---

### 5. Workflow typique

1. Installez YourKit sur votre machine de développement.
2. Modifiez le fichier `jvm.options` de Liberty avec le chemin de l'agent.
3. Démarrez Liberty.
4. Connectez-vous depuis l'interface graphique de YourKit à la JVM Liberty (via socket ou attachement).
5. Profilez vos endpoints, l'utilisation de la mémoire ou les verrous de threads.
6. Sauvegardez des instantanés pour une analyse hors ligne.

---

👉 Souhaitez-vous que je vous donne un **exemple de configuration étape par étape** pour Liberty sur **OpenJ9** (la JVM Liberty par défaut) avec YourKit, incluant des exemples de paramètres `jvm.options` pour le profilage CPU vs mémoire ?