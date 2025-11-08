---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résolution des Conflits de Pilotes NVIDIA
translated: true
type: note
---

Cela ressemble à un conflit classique de paquets lors d'une mise à jour du pilote NVIDIA sur Ubuntu (probablement la 22.04 d'après les versions des paquets). Le paquet `nvidia-kernel-common-535` tente d'écraser un fichier de firmware (`gsp_ga10x.bin`) qui est déjà détenu par `nvidia-firmware-535`, ce qui fait que dpkg abandonne. C'est un problème connu avec les pilotes NVIDIA série 535 des dépôts Ubuntu.

Ne paniquez pas — votre système devrait toujours démarrer (bien que les graphiques puissent être en mode rendu logiciel si le pilote est partiellement cassé). Voici une solution étape par étape pour résoudre le problème en toute sécurité. Exécutez ces commandes dans un terminal (utilisez TTY si l'interface graphique est instable : Ctrl+Alt+F3 pour basculer).

### Tentative de Correction Rapide (La Plus Sûre en Premier)
1. Essayez de corriger automatiquement les paquets cassés :
   ```
   sudo apt --fix-broken install
   ```
   Cela résout souvent les problèmes de dépendances/dépaquetage sans intervention manuelle.

2. Si cela échoue (ou réussit partiellement mais laisse des erreurs), nettoyez l'installation interrompue :
   ```
   sudo dpkg --configure -a
   sudo apt update
   sudo apt upgrade
   ```

### Si Toujours Bloqué : Forcer l'Écrasement du Fichier en Conflit
L'erreur concerne spécifiquement le fichier deb `nvidia-kernel-common-535`. Forcez dpkg à écraser le fichier dupliqué :
```
sudo dpkg -i --force-overwrite /var/cache/apt/archives/nvidia-kernel-common-535_535.274.02-0ubuntu1_amd64.deb
```
- Cela installe uniquement ce paquet, en ignorant le conflit de fichier.
- Exécutez ensuite :
  ```
  sudo apt --fix-broken install
  sudo apt autoremove
  sudo apt upgrade
  ```
- Redémarrez ensuite : `sudo reboot`.

### Option Nucléaire : Purger et Réinstaller les Paquets NVIDIA
Si la méthode ci-dessus ne fonctionne pas (par exemple, à cause d'un décalage de version plus profond), supprimez les éléments NVIDIA conflictuels et réinstallez :
1. Purgez les paquets problématiques (adaptez les versions si nécessaire — vérifiez avec `dpkg -l | grep nvidia`) :
   ```
   sudo dpkg --force-all -P nvidia-firmware-535-535.274.02 nvidia-kernel-common-535
   ```
2. Nettoyez :
   ```
   sudo apt autoremove --purge
   sudo apt autoclean
   ```
3. Réinstallez le pilote :
   ```
   sudo apt update
   sudo apt install nvidia-driver-535
   ```
4. Redémarrez.

### Prévention/Conseils
- Ajoutez le PPA graphics-drivers pour des mises à jour NVIDIA plus stables : `sudo add-apt-repository ppa:graphics-drivers/ppa && sudo apt update`.
- Si vous êtes sur un ordinateur portable, assurez-vous que Secure Boot est désactivé dans le BIOS avant d'installer les pilotes.
- Testez après le redémarrage avec `nvidia-smi` (devrait afficher votre GPU) ou `prime-select query` (si NVIDIA Optimus).
- Si cela casse complètement votre affichage, démarrez en mode recovery et exécutez les correctifs à partir de là.

Si rien de tout cela ne fonctionne ou si vous obtenez une nouvelle erreur, collez la sortie complète ici pour plus d'ajustements.

### Références
- [Unmet dependencies nvidia-dkms-535 - package conflict breaks Ubuntu 22.04 install](https://forums.developer.nvidia.com/t/unmet-dependencies-nvidia-dkms-535-package-conflict-breaks-ubuntu-22-04-install/265788)
- [Ubuntu and NVIDIA-provided packages conflict, breaking installation](https://forums.developer.nvidia.com/t/ubuntu-and-nvidia-provided-packages-conflict-breaking-installation/259150)
- [Problem with nvidia package dependencies](https://askubuntu.com/questions/1491916/problem-with-nvidia-package-dependencies)
- [nvidia-kernel-common-535 conflicts with nvidia-firmware-535](https://superuser.com/questions/1833427/nvidia-kernel-common-535-conflicts-with-nvidia-firmware-535-535-161-07-535-161-0)