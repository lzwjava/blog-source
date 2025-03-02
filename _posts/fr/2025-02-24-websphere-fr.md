---
audio: false
generated: false
lang: fr
layout: post
title: Commandes Serveur WebSphere Liberty
translated: true
---

Lors de la gestion d'un serveur WebSphere Liberty, plusieurs commandes sont fréquemment utilisées pour effectuer des tâches essentielles telles que la création, le démarrage, l'arrêt et la surveillance du serveur. Voici une liste des commandes les plus couramment utilisées, accompagnée d'une brève description de chacune :

- **`./server create <server_name>`**
  Crée une nouvelle instance de serveur avec le nom spécifié. Cette commande configure la structure de répertoire nécessaire et les fichiers de configuration par défaut (par exemple, `server.xml`) pour le serveur.

- **`./server start <server_name>`**
  Démarre le serveur en arrière-plan. Le serveur s'exécute en tant que processus en arrière-plan, et les journaux sont écrits dans les fichiers de journalisation du serveur.

- **`./server stop <server_name>`**
  Arrête une instance de serveur en cours d'exécution. Cette commande arrête le serveur de manière élégante.

- **`./server status <server_name>`**
  Vérifie si le serveur spécifié est en cours d'exécution. Elle renvoie l'état actuel (par exemple, démarré ou arrêté).

- **`./server run <server_name>`**
  Démarre le serveur en avant-plan. Cela est utile pour le débogage ou la surveillance, car la sortie du serveur est affichée directement dans la console.

- **`./server package <server_name>`**
  Emballe le serveur, y compris sa configuration et ses applications, dans un fichier zip. Cela est utile pour déployer le serveur dans un autre environnement ou à des fins de sauvegarde.

- **`./server debug <server_name>`**
  Démarre le serveur en mode débogage, permettant d'attacher un débogueur au processus du serveur pour le dépannage.

Ces commandes couvrent les opérations de base nécessaires pour gérer un serveur WebSphere Liberty de manière efficace. Pour des tâches plus avancées, telles que l'installation de fonctionnalités ou la gestion de la sécurité, des utilitaires supplémentaires comme `featureUtility` ou `securityUtility` sont disponibles mais sont moins fréquemment utilisés dans les opérations quotidiennes.