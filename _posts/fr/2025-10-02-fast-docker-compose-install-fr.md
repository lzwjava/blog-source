---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Méthodes Rapides d'Installation de Docker Compose
translated: true
type: note
---

### Méthodes alternatives rapides pour télécharger/installer Docker Compose sur Ubuntu

En supposant que vous cherchez à obtenir rapidement la dernière binaire Docker Compose (actuellement v2.37.3 en octobre 2025, selon la documentation officielle) sans les tracas de la page complète des releases GitHub (par exemple, la vérification manuelle curl + sha256), voici des options fiables et plus rapides. Elles exploitent le gestionnaire de paquets d'Ubuntu ou les dépôts de Docker pour des installations quasi instantanées. Je privilégierai la vitesse et la simplicité—la plupart prennent moins d'une minute.

#### 1. **Via APT d'Ubuntu (Le plus rapide pour la plupart des utilisateurs)**
   Si vous avez Docker installé (qui inclut le `docker-compose-plugin`), utilisez simplement la sous-commande—aucun téléchargement séparé nécessaire. C'est la méthode moderne et intégrée qui évite la gestion manuelle des binaires.
   
   - **Vérifier si déjà disponible** :
     ```
     docker compose version
     ```
     Si cela affiche v2.x, c'est terminé—vous avez la dernière version via votre installation Docker.
   
   - **Installer/Mettre à jour si nécessaire** (ajoute le plugin s'il est manquant) :
     ```
     sudo apt update
     sudo apt install docker-compose-plugin
     ```
     - **Pourquoi c'est rapide ?** Pas de trafic GitHub ; utilise les dépôts locaux. Se met à jour automatiquement avec `apt upgrade`.
     - **Utilisation** : Exécutez avec `docker compose up` (notez l'espace, pas le trait d'union).
     - **Conseil pro** : Si Docker n'est pas encore installé, ajoutez d'abord le dépôt Docker :
       ```
       sudo apt update
       sudo apt install ca-certificates curl
       sudo install -m 0755 -d /etc/apt/keyrings
       sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
       sudo chmod a+r /etc/apt/keyrings/docker.asc
       echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
       sudo apt update
       sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
       ```

#### 2. **Curl en une ligne depuis GitHub (Légèrement plus rapide que la release complète)**
   Évitez de naviguer sur la page des releases—curl récupère directement le dernier binaire Linux x86_64 et l'installe. C'est plus rapide que la sélection manuelle des assets mais utilise toujours GitHub.
   
   ```
   VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d\" -f4) && sudo curl -L "https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose && docker-compose --version
   ```
   - **Pourquoi c'est rapide ?** L'API récupère la version en quelques secondes ; une seule commande gère le téléchargement et l'installation.
   - **Vérifier** : Le `--version` à la fin le confirme.
   - **Note** : Pour la version v2.39.4 spécifiquement, remplacez `${VERSION}` par `v2.39.4`.

#### 3. **Via Snap (Le gestionnaire de paquets universel d'Ubuntu)**
   Snap est préinstallé sur Ubuntu 24.04 et récupère instantanément la dernière version depuis le store de Canonical.
   
   ```
   sudo snap install docker
   ```
   - **Pourquoi c'est rapide ?** Aucune configuration de dépôt ; télécharge en parallèle et se met à jour automatiquement. Inclut le plugin Compose.
   - **Utilisation** : Identique à la méthode APT (`docker compose`).
   - **Vérifier la version** : `docker compose version`.

#### 4. **Via Pip (Puisque vous avez Python 3.13.4)**
   Si vous préférez une installation basée sur Python (style legacy v1, mais pip a des wrappers v2), c'est une installation rapide sans dépendances système.
   
   ```
   sudo pip3 install docker-compose
   ```
   - **Pourquoi c'est rapide ?** Pip utilise un cache et résout les dépendances rapidement ; pas d'implication de GitHub.
   - **Limitation** : C'est surtout pour la compatibilité v1—utilisez APT pour le plugin v2 officiel.
   - **Vérifier** : `docker-compose --version` (avec un trait d'union).

Ces méthodes sont toutes plus rapides que l'interface utilisateur de GitHub car elles minimisent les clics ou utilisent des APIs/caches. APT ou Snap sont mes recommandations principales pour Ubuntu—elles s'intègrent parfaitement et gèrent les mises à jour. Si vous vouliez dire autre chose par "docker compose down" (par exemple, la commande elle-même), précisez !

[Guide d'installation officiel de Docker Compose](https://docs.docker.com/compose/install/linux/)  
[Releases Docker](https://github.com/docker/compose/releases)