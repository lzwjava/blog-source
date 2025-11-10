---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide du port JMX distant 9001
translated: true
type: note
---

Un **agent JMX distant** fait partie des Java Management Extensions (JMX). Il vous permet de surveiller et de gérer une application Java en cours d'exécution à distance. Lorsque vous activez la gestion JMX à distance, la JVM démarre un agent qui expose des MBeans (Managed Beans) via un port TCP. Des outils comme **jconsole**, **VisualVM** ou des logiciels de surveillance personnalisés peuvent se connecter à ce port pour inspecter l'utilisation de la mémoire, l'état des threads, l'activité du Garbage Collector, et même invoquer des opérations.

À propos du **port 9001** :

* Le numéro de port réel dépend de la configuration de l'application. Vous verrez couramment 9001, 9090, 9091, etc.
* Si vous voyez quelque chose en écoute sur `9001` et qu'il s'agit d'un **agent JMX distant**, cela signifie qu'un processus Java a démarré avec des propriétés système comme :

  ```bash
  -Dcom.sun.management.jmxremote
  -Dcom.sun.management.jmxremote.port=9001
  -Dcom.sun.management.jmxremote.authenticate=false
  -Dcom.sun.management.jmxremote.ssl=false
  ```

Ceci ouvre JMX sur le port `9001` sans authentification/SSL (souvent réservé à un usage interne ou de développement, car c'est peu sécurisé s'il est exposé publiquement).

---

### Comment vérifier quel programme utilise le port JMX 9001 sur Windows

1. Ouvrez **l'Invite de commandes (en tant qu'Administrateur)**.
2. Exécutez :

   ```cmd
   netstat -ano | findstr :9001
   ```

   Cela affiche le PID (Identifiant de Processus) lié à ce port.
3. Pour identifier le programme :

   ```cmd
   tasklist /FI "PID eq <PID>"
   ```

   Remplacez `<PID>` par le nombre obtenu à l'étape 2.

---

### Comment l'arrêter / le tuer

* Si vous confirmez qu'il s'agit d'un processus Java que vous ne voulez pas, tuez-le avec :

  ```cmd
   taskkill /PID <PID> /F
   ```
* Mais si cela fait partie de votre serveur d'application (Tomcat, WebSphere, application Spring Boot, etc.), il est préférable de l'arrêter via son service/console plutôt que de tuer le processus, afin qu'il s'arrête proprement.

---

👉 Souhaitez-vous que je vous montre également comment **désactiver l'agent JMX distant** dans une application Java afin qu'il n'ouvre pas du tout le port 9001 ?