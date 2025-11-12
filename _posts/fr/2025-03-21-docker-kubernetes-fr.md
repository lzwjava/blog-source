---
audio: false
generated: true
lang: fr
layout: post
title: Docker contre Kubernetes
translated: true
type: note
---

Docker et Kubernetes sont des technologies complémentaires dans l'écosystème des conteneurs, mais ils servent des objectifs différents. Décomposons leurs différences et leur relation.

---

### Docker : Plateforme de conteneurisation
**Ce qu'il fait** : Docker est un outil pour créer, exécuter et gérer des conteneurs individuels — des environnements légers et isolés qui empaquettent une application avec ses dépendances.

#### Fonctionnalités clés
1. **Moteur d'exécution de conteneurs (Runtime)** :
   - Docker utilise un runtime (par exemple, `containerd` ou `runc`) pour exécuter les conteneurs en s'appuyant sur des fonctionnalités du noyau Linux comme les namespaces et les cgroups.
   - Il est responsable du cycle de vie d'un conteneur individuel : construction, démarrage, arrêt, etc.

2. **Gestion des images** :
   - Docker construit des images à partir d'un `Dockerfile`, qui définit l'application, les bibliothèques et les configurations.
   - Les images sont stockées dans des registres (par exemple, Docker Hub) et exécutées en tant que conteneurs.

3. **Centré sur un hôte unique** :
   - Docker excelle dans la gestion des conteneurs sur une seule machine. Vous pouvez exécuter plusieurs conteneurs, mais l'orchestration sur plusieurs hôtes n'est pas intégrée.

4. **Piloté par CLI** :
   - Des commandes comme `docker build`, `docker run` et `docker ps` vous permettent d'interagir directement avec les conteneurs.

#### Cas d'utilisation
- Exécuter une application Spring Boot unique sur votre ordinateur portable ou un serveur :
  ```bash
  docker run -p 8080:8080 myapp:latest
  ```

#### Limitations
- Aucune prise en charge native multi-hôtes.
- Pas de mise à l'échelle automatique, d'auto-réparation ou d'équilibrage de charge.
- Gérer manuellement de nombreux conteneurs devient compliqué.

---

### Kubernetes : Système d'orchestration de conteneurs
**Ce qu'il fait** : Kubernetes (souvent abrégé en K8s) est une plateforme pour gérer et orchestrer de multiples conteneurs à travers un cluster de machines. Il automatise le déploiement, la mise à l'échelle et l'exploitation d'applications conteneurisées.

#### Fonctionnalités clés
1. **Gestion de cluster** :
   - Kubernetes s'exécute sur un cluster de nœuds (machines physiques ou virtuelles). Un nœud est le "plan de contrôle" (gérant le cluster), et les autres sont les "nœuds worker" (exécutant les conteneurs).

2. **Orchestration** :
   - **Planification (Scheduling)** : Décide quel nœud exécute chaque conteneur en fonction des ressources et des contraintes.
   - **Mise à l'échelle (Scaling)** : Augmente ou diminue automatiquement le nombre d'instances de conteneurs (par exemple, basé sur l'utilisation du CPU).
   - **Auto-réparation (Self-Healing)** : Redémarre les conteneurs défaillants, les replanifie si un nœud tombe en panne et garantit que l'état souhaité est maintenu.
   - **Équilibrage de charge (Load Balancing)** : Répartit le trafic entre plusieurs instances de conteneurs.

3. **Couche d'abstraction** :
   - Utilise des "Pods" comme plus petite unité — un Pod peut contenir un ou plusieurs conteneurs (généralement un) qui partagent le stockage et les ressources réseau.
   - Géré via des fichiers YAML déclaratifs (par exemple, définissant des déploiements, des services).

4. **Centré multi-hôtes** :
   - Conçu pour les systèmes distribués, coordonnant les conteneurs sur de nombreuses machines.

5. **Écosystème** :
   - Inclut des fonctionnalités comme la découverte de services, le stockage persistant, la gestion des secrets et les mises à jour progressives (rolling updates).

#### Cas d'utilisation
- Déployer une application microservices avec 10 services, chacun dans son propre conteneur, sur 5 serveurs, avec mise à l'échelle automatique et basculement :
  ```yaml
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: myapp
  spec:
    replicas: 3
    selector:
      matchLabels:
        app: myapp
    template:
      metadata:
        labels:
          app: myapp
      spec:
        containers:
        - name: myapp
          image: myapp:latest
          ports:
          - containerPort: 8080
  ```

#### Limitations
- Courbe d'apprentissage plus raide.
- Excessif pour des applications simples à conteneur unique sur une machine.

---

### Différences principales

| Aspect                | Docker                              | Kubernetes                          |
|-----------------------|-------------------------------------|-------------------------------------|
| **Objectif**          | Création et exécution de conteneurs | Orchestration de conteneurs         |
| **Portée**            | Hôte unique                         | Cluster d'hôtes                     |
| **Unité**             | Conteneur                           | Pod (groupe de 1+ conteneurs)       |
| **Mise à l'échelle**  | Manuelle (ex: `docker run` plusieurs fois) | Automatique (via les replicas)      |
| **Réseau**            | Basique (bridge, host, overlay)     | Avancé (services, ingress)          |
| **Auto-réparation**   | Aucune (redémarrage manuel)         | Intégrée (redémarre, replanifie)    |
| **Gestion**           | CLI ou Docker Compose pour petites configurations | Configs YAML, CLI `kubectl`         |
| **Dépendances**       | Autonome (nécessite Docker Engine)  | A besoin d'un runtime de conteneur (ex: Docker) |

---

### Comment ils travaillent ensemble
- **Docker comme Runtime** : Kubernetes n'exécute pas directement les conteneurs — il s'appuie sur un runtime de conteneur comme Docker (ou des alternatives comme `containerd`) pour démarrer et gérer les conteneurs individuels au sein des Pods.
- **Workflow** :
  1. Vous construisez une image Docker (`docker build -t myapp:latest .`).
  2. Vous la poussez vers un registre (`docker push myapp:latest`).
  3. Kubernetes récupère l'image et la déploie à travers le cluster en fonction de votre configuration YAML (`kubectl apply -f deployment.yaml`).

- **Exemple** : Kubernetes peut utiliser Docker pour exécuter trois instances de `myapp:latest` sur différents nœuds, en les exposant via un service avec équilibrage de charge.

---

### Analogie
- **Docker** : Un chef cuisinant un seul plat dans une cuisine. Vous dites au chef quoi préparer (`Dockerfile`) et comment le servir (`docker run`).
- **Kubernetes** : Un manager de restaurant supervisant plusieurs chefs (instances Docker) dans de nombreuses cuisines (nœuds). Le manager s'assure que les plats sont préparés à temps, augmente le personnel pendant les heures d'affluence et remplace un chef qui tombe malade.

---

### Quand utiliser lequel ?
- **Docker seul** : Pour le développement, les tests ou les applications simples sur une machine (ex: une application Spring Boot unique).
- **Kubernetes** : Pour les applications distribuées de qualité production nécessitant une haute disponibilité, une mise à l'échelle et une résilience (ex: une architecture microservices).

---

Est-ce que cela clarifie la distinction ? Faites-moi savoir si vous souhaitez explorer un aspect spécifique — comme configurer Kubernetes ou le comparer à Docker Compose !