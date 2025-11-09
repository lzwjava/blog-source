---
audio: false
generated: true
image: false
lang: fr
layout: post
model: anthropic/claude-sonnet-4
title: Guide d'installation de Docker sur Ubuntu
translated: true
type: note
---

D'après la sortie de votre système Ubuntu, vous avez plusieurs options pour installer Docker. Voici l'approche recommandée :

## Option 1 : Installer Docker Engine (Recommandée)

La méthode la plus courante et recommandée est d'installer Docker Engine depuis le dépôt officiel de Docker :

```bash
# Mettre à jour l'index des paquets
sudo apt update

# Installer les prérequis
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Ajouter la clé GPG officielle de Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Ajouter le dépôt Docker
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Mettre à jour l'index des paquets à nouveau
sudo apt update

# Installer Docker Engine
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Option 2 : Installation rapide via APT (Plus simple)

D'après les options affichées dans votre terminal, vous pouvez utiliser :

```bash
sudo apt install docker.io
```

## Configuration post-installation

Après l'installation, vous devrez :

1. **Démarrer et activer le service Docker :**
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

2. **Ajouter votre utilisateur au groupe docker** (pour exécuter Docker sans sudo) :
```bash
sudo usermod -aG docker $USER
```

Puis déconnectez-vous et reconnectez-vous, ou exécutez :
```bash
newgrp docker
```

3. **Vérifier l'installation :**
```bash
docker --version
docker run hello-world
```

## Quelle option choisir ?

- **L'option 1** vous donne la dernière version de Docker directement depuis Docker Inc.
- **L'option 2** est plus simple mais peut avoir une version légèrement plus ancienne depuis les dépôts d'Ubuntu

Pour la plupart des utilisateurs, l'option 2 (`sudo apt install docker.io`) est parfaitement adaptée et beaucoup plus simple. La différence de version est généralement minime pour une utilisation régulière.

Souhaitez-vous que j'explique une de ces étapes plus en détail ?