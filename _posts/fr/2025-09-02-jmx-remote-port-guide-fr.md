---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide du port de l'agent JMX distant
translated: true
type: note
---

L'**agent JMX distant** fait partie de la technologie Java Management Extensions (JMX). Il permet aux administrateurs ou aux outils de surveillance de se connecter à une application Java en cours d'exécution depuis l'extérieur du processus JVM, généralement via TCP/IP. Ceci est couramment utilisé pour la surveillance, le diagnostic et la gestion des applications Java en production.

Voici une explication détaillée :

### 1. Qu'est-ce que l'agent JMX distant

* Il expose les éléments internes de la JVM (utilisation de la mémoire, activité des threads, garbage collection, chargement des classes, etc.) sous forme de *Managed Beans (MBeans)*.
* Il vous permet de vous connecter à distance (par exemple, via **jconsole**, **VisualVM**, ou des outils de surveillance comme les exportateurs Prometheus).
* Il est généralement activé par des flags de démarrage JVM tels que :

  ```bash
  -Dcom.sun.management.jmxremote
  -Dcom.sun.management.jmxremote.port=9091
  -Dcom.sun.management.jmxremote.authenticate=false
  -Dcom.sun.management.jmxremote.ssl=false
  ```
* Une fois activé, la JVM exécute un serveur de connecteur RMI (Remote Method Invocation) lié au port spécifié.

### 2. À propos du port 9091

* Le numéro **9091** en lui-même n'a rien de spécial ; il s'agit simplement d'un port TCP que vous configurez pour les connexions JMX.
* Les administrateurs choisissent souvent 9091 (ou 9010, 9999, etc.) par commodité et pour éviter les conflits avec les ports standard.
* Lorsqu'il écoute sur `9091`, la JVM acceptera les connexions JMX distantes sur ce port.
* S'il n'est pas sécurisé (`authenticate=false, ssl=false`), toute personne ayant un accès réseau peut contrôler ou observer votre JVM — ce qui représente un risque de sécurité majeur.

### 3. Utilisation typique

* Surveillance avec **JConsole** :

  ```bash
  jconsole hôte:9091
  ```
* Intégration avec des systèmes de surveillance (par exemple, Prometheus JMX Exporter).
* Gestion à distance lors du dépannage (par exemple, vérification des heap dumps, des threads, du comportement du GC).

### 4. Considérations de sécurité

* Protégez toujours le port JMX avec :

  * Des pare-feux réseau (restreindre l'accès).
  * Une authentification (fichiers `password` et `access`).
  * SSL si nécessaire.
* Sinon, l'exposer sur le port 9091 sans sécurité équivaut à donner un contrôle au niveau du shell distant de votre JVM.

---

✅ En bref : **L'agent JMX distant sur le port 9091** signifie que votre JVM expose une interface de gestion et de surveillance sur le port TCP 9091, qui peut être utilisée par des outils comme JConsole ou Prometheus, mais qui doit être sécurisée.

Souhaitez-vous que je vous montre les **flags JVM exacts** pour l'activer avec une authentification par mot de passe (au lieu du mode non sécurisé) ?