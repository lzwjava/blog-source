---
audio: false
generated: true
image: false
lang: fr
layout: post
model: anthropic/claude-sonnet-4
title: Méthodes d'installation de fichiers DEB Discord
translated: true
type: note
---

Pour installer le fichier `discord-0.0.111.deb`, vous pouvez utiliser plusieurs méthodes :

**Méthode 1 : Utilisation de dpkg (ligne de commande)**
```bash
sudo dpkg -i discord-0.0.111.deb
```

Si vous rencontrez des problèmes de dépendances, exécutez :
```bash
sudo apt-get install -f
```

**Méthode 2 : Utilisation de apt (recommandée)**
```bash
sudo apt install ./discord-0.0.111.deb
```

Cette méthode gère automatiquement les dépendances mieux que dpkg.

**Méthode 3 : Utilisation de gdebi (s'il est installé)**
```bash
sudo gdebi discord-0.0.111.deb
```

**Méthode 4 : Méthode graphique**
Si vous utilisez un environnement de bureau, vous pouvez souvent double-cliquer sur le fichier .deb et il s'ouvrira dans votre gestionnaire de paquets (comme le Centre de logiciels) pour l'installation.

**Prérequis :**
- Assurez-vous d'être dans le répertoire contenant le fichier .deb
- Vous aurez besoin des privilèges sudo
- Si vous n'avez pas encore le fichier, vous pouvez le télécharger depuis le site officiel de Discord

**Après l'installation :**
Vous devriez pouvoir lancer Discord depuis votre menu d'applications ou en exécutant `discord` dans le terminal.

Quelle méthode préférez-vous utiliser, ou avez-vous besoin d'aide pour une étape spécifique ?