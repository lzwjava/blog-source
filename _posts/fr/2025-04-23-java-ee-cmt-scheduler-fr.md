---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Planificateur de Tâches Géré par Conteneur Java EE
translated: true
type: note
---

Un **ManagedScheduledExecutorService** est une ressource Java EE (Jakarta EE) fournie par le serveur d'applications (par exemple WebSphere, WebLogic, WildFly) qui vous permet de planifier des tâches pour qu'elles s'exécutent dans le futur ou périodiquement, similairement au `ScheduledExecutorService` dans le Java SE standard, mais avec **les avantages de la gestion par le conteneur** :

---

### Fonctionnement

* **Intégration avec le conteneur**
  Il est géré par le serveur d'applications, ce qui signifie que les tâches s'exécutent avec le contexte de sécurité, le classloader et les limites transactionnelles de l'application. Cela évite les problèmes courants des threads non gérés dans Java EE.

* **Capacités de planification**
  Vous pouvez planifier des tâches pour :

  * S'exécuter une fois après un délai.
  * S'exécuter à un rythme fixe (par exemple, toutes les 5 secondes).
  * S'exécuter avec un délai fixe entre les exécutions.

* **Gestion du cycle de vie**
  Le conteneur prend en charge le cycle de vie du pool de threads, le nettoyage et la gestion des ressources. Vous n'avez pas besoin de l'arrêter manuellement comme avec un `ExecutorService` standard.

---

### Délai d'expiration (Timeout)

* Il n'existe pas un paramètre unique de "timeout" pour le pool lui-même, mais deux éléments sont pertinents :

  * **Timeout d'exécution d'une tâche** : Vous pouvez encapsuler des tâches avec `ManagedTaskListener` et spécifier des propriétés comme `ManagedTask.TIMEOUT` (selon le support du fournisseur). Certains serveurs vous permettent de configurer des timeouts de tâche par défaut afin que les tâches qui se bloquent soient annulées par le conteneur.
  * **Timeout de `Future.get()`** : Comme avec le `ScheduledExecutorService` classique, vous pouvez utiliser `future.get(timeout, unit)` pour limiter le temps d'attente des résultats.

Ainsi, le "timeout" est généralement appliqué par tâche, et non au niveau du pool.

---

### Configuration de la Taille du Pool

* Chaque serveur d'applications possède sa propre configuration pour le pool de threads sous-jacent.
  Exemples :

  * **WebSphere Liberty / Traditional** : vous configurez le pool dans `server.xml` sous `<managedScheduledExecutorService>` avec des attributs comme `corePoolSize` et `maximumPoolSize`.
  * **WebLogic** : vous le configurez via la Console d'Administration ou `weblogic-managed-executor`.
  * **WildFly / JBoss EAP** : configuré dans le sous-système EE.

* Les configurations typiques de pool incluent :

  * **Taille de pool principale (Core pool size)** : nombre minimum de threads maintenus actifs.
  * **Taille de pool maximale (Maximum pool size)** : nombre maximum de threads simultanés.
  * **Taille de la file d'attente / Politique de rejet** : ce qui se passe lorsque tous les threads sont occupés.
  * **Durée de maintien (Keep-alive time)** : durée pendant laquelle les threads inactifs sont conservés avant d'être libérés.

---

✅ **En résumé** :
Le `ManagedScheduledExecutorService` fonctionne comme le planificateur de Java SE mais est adapté au conteneur, vous offrant ainsi un threading sécurisé dans les applications Java EE. Le timeout est généralement appliqué par tâche (soit via l'API, soit via la configuration du serveur), tandis que la taille du pool (nombre de threads principal/maximum) est configurée au niveau du conteneur, et non dans votre code d'application.

---

Souhaitez-vous que je vous montre un **exemple de snippet de configuration pour WebSphere Liberty** concernant la taille du pool et le timeout ?