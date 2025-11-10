---
audio: false
generated: true
lang: fr
layout: post
title: Installer Go via APT sur Debian
translated: true
type: note
---

Pour installer Go en utilisant `apt` sur un système Linux basé sur Debian (par exemple, Ubuntu), suivez ces étapes. Notez que `apt` peut installer une version plus ancienne de Go (par exemple, 1.18 sur Ubuntu 22.04), vous devriez donc vérifier si elle répond aux exigences de votre projet (vérifiez le fichier `go.mod` dans `~/Projects/clash-core` pour la version de Go requise).

### Étapes pour installer Go en utilisant APT

1. **Mettre à jour l'index des paquets**
   - Assurez-vous que vos listes de paquets sont à jour :
     ```bash
     sudo apt update
     ```

2. **Installer Go**
   - Installez le paquet Go :
     ```bash
     sudo apt install golang-go
     ```
   - Cela installe le compilateur Go, les outils et la bibliothèque standard.

3. **Vérifier l'installation**
   - Vérifiez la version de Go installée :
     ```bash
     go version
     ```
   - Vous devriez voir une sortie comme :
     ```
     go version go1.18.1 linux/amd64
     ```
     (La version dépend du référentiel de paquets de votre distribution.)

4. **Configurer GOPATH (Optionnel)**
   - Les versions modernes de Go (1.13+) utilisent des modules, donc `GOPATH` est optionnel, mais le configurer peut être utile pour certains projets.
   - Modifiez votre profil de shell (par exemple, `~/.bashrc` ou `~/.zshrc`) :
     ```bash
     nano ~/.bashrc
     ```
   - Ajoutez les lignes suivantes :
     ```bash
     export GOPATH=$HOME/go
     export PATH=$PATH:$GOPATH/bin
     ```
   - Sauvegardez et rechargez la configuration du shell :
     ```bash
     source ~/.bashrc
     ```

5. **Relancer la construction**
   - Accédez au répertoire de votre projet :
     ```bash
     cd ~/Projects/clash-core
     ```
   - Exécutez à nouveau la commande `make` :
     ```bash
     make
     ```

### Notes
- **Vérification de version** : Si votre projet nécessite une version plus récente de Go (par exemple, 1.20 ou ultérieure), la version d'`apt` pourrait être obsolète. Vérifiez la version requise dans `go.mod` ou la documentation du projet. Si nécessaire, installez une version plus récente manuellement en téléchargeant l'archive depuis [https://go.dev/dl/](https://go.dev/dl/) (comme décrit dans la réponse précédente).
- **Dépôts alternatifs** : Pour une version plus récente via `apt`, vous pouvez ajouter un PPA tiers (par exemple, `ppa:longsleep/golang-backports` sur Ubuntu). Exécutez :
  ```bash
  sudo add-apt-repository ppa:longsleep/golang-backports
  sudo apt update
  sudo apt install golang-go
  ```
- **Dépannage** :
  - Si `go` n'est pas trouvé, assurez-vous que `/usr/bin/go` existe (`ls /usr/bin/go`). Sinon, réinstallez avec `sudo apt install --reinstall golang-go`.
  - Si vous obtenez des erreurs de dépendances, exécutez `sudo apt install -f` pour les corriger.
  - Pour les problèmes de permissions, assurez-vous d'avoir les privilèges `sudo`.

### Sources
- Guide d'installation de Go sur Ubuntu : [https://ubuntu.com/server/docs/programming-go](https://ubuntu.com/server/docs/programming-go)
- Utilisation générale d'apt : [https://help.ubuntu.com/community/AptGet/Howto](https://help.ubuntu.com/community/AptGet/Howto)

Si la version installée est trop ancienne ou si vous rencontrez des problèmes, indiquez-moi votre distribution Linux (par exemple, Ubuntu 22.04) et la version de Go requise, et je vous guiderai davantage !