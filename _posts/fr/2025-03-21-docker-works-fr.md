---
audio: false
generated: true
lang: fr
layout: post
title: Fonctionnement de Docker
translated: true
type: note
---

Plongeons dans le fonctionnement de Docker, en nous concentrant sur son utilisation du système de fichiers Linux et sur la façon dont il isole les applications les unes des autres.

---

### Qu'est-ce que Docker, fondamentalement ?
Docker est une plateforme qui vous permet de packager, distribuer et exécuter des applications dans des environnements légers et isolés appelés **conteneurs**. Contrairement aux machines virtuelles (VM), qui incluent un système d'exploitation complet, les conteneurs Docker partagent le noyau du système hôte et utilisent ses fonctionnalités pour fournir isolation et efficacité.

---

### Comment fonctionne Docker
Docker exploite plusieurs fonctionnalités du noyau Linux pour créer et gérer des conteneurs :
1. **Namespaces** - Pour l'isolation.
2. **Groupes de contrôle (cgroups)** - Pour la gestion des ressources.
3. **Systèmes de fichiers Union (Union Filesystems)** - Pour un stockage et un empilement efficaces.

Voici comment ces éléments s'assemblent :

---

#### 1. Les Namespaces Linux : Mécanisme d'isolation
Les namespaces créent des "vues" isolées des ressources système, garantissant que les processus d'un conteneur n'interfèrent pas avec ceux d'un autre. Les principaux namespaces utilisés par Docker incluent :

- **Namespace PID (PID Namespace)** : Chaque conteneur a son propre espace d'identifiants de processus (PID). Le processus avec l'ID 1 à l'intérieur d'un conteneur est isolé du PID 1 de l'hôte (généralement `init` ou `systemd`).
- **Namespace Réseau (Network Namespace)** : Les conteneurs obtiennent leur propre pile réseau (adresse IP, ports, tables de routage). C'est pourquoi deux conteneurs peuvent écouter sur le port 8080 sans conflit.
- **Namespace Montage (Mount Namespace)** : Chaque conteneur a sa propre vue du système de fichiers, isolée de l'hôte et des autres conteneurs.
- **Namespace UTS (UTS Namespace)** : Les conteneurs peuvent avoir leur propre nom d'hôte et nom de domaine.
- **Namespace IPC (IPC Namespace)** : Isole la communication inter-processus (par exemple, mémoire partagée, files de messages).
- **Namespace Utilisateur (User Namespace)** (optionnel) : Mappe les utilisateurs du conteneur vers les utilisateurs de l'hôte, améliorant la sécurité.

**Exemple** : Si vous exécutez `ps` à l'intérieur d'un conteneur, vous ne voyez que les processus dans le namespace PID de ce conteneur, pas les processus de l'hôte.

---

#### 2. Groupes de contrôle (cgroups) : Limites des ressources
Les cgroups limitent et surveillent l'utilisation des ressources (CPU, mémoire, E/S disque, etc.) pour chaque conteneur. Cela empêche un conteneur d'accaparer toutes les ressources système et d'en priver les autres.

- **Comment ça marche** : Docker assigne un cgroup à chaque conteneur. Vous pouvez définir des limites comme :
  ```bash
  docker run --memory="512m" --cpus="0.5" myapp
  ```
  Cela restreint le conteneur à 512 Mo de RAM et la moitié d'un cœur de CPU.

- **Isolation** : Alors que les namespaces isolent la visibilité, les cgroups isolent la consommation de ressources.

---

#### 3. Systèmes de fichiers Union (Union Filesystems) : Stockage en couches
Docker utilise un **système de fichiers union** (par exemple, OverlayFS, AUFS) pour gérer efficacement les images de conteneurs et leurs systèmes de fichiers. Voici comment cela s'intègre au système de fichiers Linux :

- **Couches d'image (Image Layers)** : Une image Docker est construite à partir de couches empilées en lecture seule. Chaque couche représente un ensemble de modifications (par exemple, installer un package, copier des fichiers) définies dans votre `Dockerfile`.
  - Exemple : `FROM openjdk:17` est une couche, `COPY app.jar` en ajoute une autre.
  - Les couches sont mises en cache et réutilisées, économisant l'espace disque et accélérant les builds.

- **Système de fichiers du conteneur (Container Filesystem)** : Lorsque vous exécutez un conteneur, Docker ajoute une fine couche inscriptible au-dessus des couches d'image en lecture seule. C'est ce qu'on appelle un mécanisme **copy-on-write (CoW)** :
  - Les lectures se font à partir des couches d'image.
  - Les écritures (par exemple, fichiers de log, données temporaires) vont dans la couche inscriptible.
  - Si un fichier dans une couche inférieure est modifié, il est d'abord copié dans la couche inscriptible (d'où le terme "copy-on-write").

- **Isolation** : Chaque conteneur obtient sa propre couche inscriptible, ainsi les modifications dans un conteneur n'affectent pas les autres, même s'ils partagent la même image de base.

- **Sur le disque** : Sur l'hôte, ces couches sont stockées dans `/var/lib/docker` (par exemple, `/var/lib/docker/overlay2` pour OverlayFS). Vous n'interagissez pas directement avec cela — Docker le gère.

---

### Comment les applications sont isolées les unes des autres
Voici comment les composants ci-dessus travaillent ensemble pour isoler les applications :

1. **Isolation des processus (Namespace PID)** :
   - Chaque conteneur exécute son application comme une arborescence de processus indépendante, ignorant les autres conteneurs ou l'hôte.

2. **Isolation réseau (Namespace Réseau)** :
   - Les conteneurs ont des interfaces réseau séparées. Le réseau "bridge" par défaut de Docker assigne une IP unique à chaque conteneur, et le NAT gère la communication externe.
   - Exemple : Deux applications Spring Boot peuvent toutes deux se lier au port 8080 à l'intérieur de leurs conteneurs sans conflit.

3. **Isolation du système de fichiers (Namespace Montage + UnionFS)** :
   - Chaque conteneur ne voit que son propre système de fichiers, construit à partir des couches d'image plus sa couche inscriptible.
   - Si le Conteneur A écrit dans `/tmp`, le Conteneur B ne le voit pas.

4. **Isolation des ressources (cgroups)** :
   - Une application ne peut pas épuiser le CPU ou la mémoire de l'hôte et en faire planter une autre.

5. **Noyau partagé (Shared Kernel)** :
   - Les conteneurs partagent le noyau Linux de l'hôte, mais les namespaces garantissent qu'ils ne se marchent pas sur les pieds. Les appels système sont filtrés ou redirigés si nécessaire.

---

### Workflow simplifié
1. **Build (Construction)** : Vous créez une image avec un `Dockerfile`, définissant l'application et ses dépendances. Docker les empile en couches en utilisant un système de fichiers union.
2. **Run (Exécution)** : Docker crée un conteneur en :
   - Configurant les namespaces pour l'isolation.
   - Allouant les cgroups pour les limites de ressources.
   - Montant les couches d'image plus une couche inscriptible.
   - Démarant votre application comme point d'entrée (par exemple, `java -jar app.jar`).
3. **Nettoyage (Cleanup)** : Lorsque le conteneur s'arrête, la couche inscriptible est supprimée (sauf si elle est sauvegardée en tant que nouvelle image avec `docker commit`).

---

### Pourquoi Linux ?
Docker repose sur des fonctionnalités du noyau Linux (namespaces, cgroups, systèmes de fichiers union) qui sont profondément intégrées à son mode de fonctionnement. Sur macOS ou Windows, Docker exécute une machine virtuelle Linux légère (via HyperKit ou WSL2) pour fournir ces capacités, puis les mappe sur le système d'exploitation hôte.

---

### Analogie visuelle
Imaginez les conteneurs Docker comme des appartements dans un immeuble :
- **Namespaces** : Les murs et les portes séparent les locataires.
- **Cgroups** : Le propriétaire limite l'eau ou l'électricité par appartement.
- **UnionFS** : Tous les appartements partagent un plan commun (couches d'image), mais chaque locataire peut décorer son espace (couche inscriptible).

---

Est-ce que cela clarifie le fonctionnement de Docker et l'isolation des applications ? Faites-moi savoir si vous souhaitez approfondir une partie en particulier !