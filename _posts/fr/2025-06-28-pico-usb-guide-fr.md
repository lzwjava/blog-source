---
audio: false
generated: true
lang: fr
layout: post
title: Guide du câble USB pour Raspberry Pi Pico sur Ubuntu
translated: true
type: note
---

Pour votre **Raspberry Pi Pico (avec connecteurs)** de la **Raspberry Pi Foundation** (en supposant que "duistou" soit une faute de frappe ou une marque de revendeur), vous avez besoin du bon câble USB pour le configurer avec Ubuntu. Voici ce dont vous avez besoin :

### Exigences du câble USB
1. **Type** : Câble USB vers Micro-USB
   - Le Raspberry Pi Pico (original, avec connecteurs) utilise un port **Micro-USB** pour l'alimentation et les données.
   - Assurez-vous que le câble prend en charge le **transfert de données**, et pas seulement la charge. Certains câbles Micro-USB bon marché sont uniquement conçus pour l'alimentation et ne fonctionneront pas pour la programmation ou la communication.

2. **Spécifications du câble** :
   - **Connecteur** : USB-A (ou USB-C, selon les ports de votre ordinateur) vers Micro-USB.
   - **Qualité** : Utilisez un câble de haute qualité pour éviter les problèmes de connexion. Un câble d'une marque réputée (par exemple, Anker, Belkin, ou celui fourni avec des appareils comme des téléphones ou des tablettes) fonctionne bien.
   - **Longueur** : Un câble de 1 à 3 pieds (30 à 100 cm) est idéal pour minimiser les problèmes de signal.

3. **Port de l'ordinateur** :
   - Si votre machine Ubuntu a des **ports USB-A**, utilisez un câble USB-A vers Micro-USB.
   - Si elle n'a que des **ports USB-C**, utilisez un câble USB-C vers Micro-USB ou un hub/adaptateur USB-C avec un câble USB-A vers Micro-USB.

### Notes de configuration
- **Connexion** : Branchez l'extrémité Micro-USB dans le port Micro-USB du Pico et l'autre extrémité dans votre ordinateur Ubuntu.
- **Mode** :
  - **Mode Normal** : Branchez le Pico directement pour le connecter à la programmation (par exemple, MicroPython, C/C++).
  - **Mode BOOTSEL** : Maintenez le bouton **BOOTSEL** sur le Pico tout en le branchant pour entrer en mode stockage de masse pour les mises à jour du firmware (il apparaît comme un lecteur nommé `RPI-RP2`).
- **Vérification** : Après la connexion, utilisez les étapes de ma réponse précédente pour confirmer qu'Ubuntu détecte le Pico (par exemple, `lsusb`, `ls /dev/tty*`, ou `lsblk`).

### Dépannage des problèmes de câble
- Si le Pico n'est pas détecté (aucun périphérique `/dev/ttyACM0` ou lecteur `RPI-RP2`), essayez un autre câble ou port USB.
- Évitez d'utiliser des hubs USB, car ils peuvent parfois causer des problèmes de détection.
- Vérifiez le câble en le testant avec un autre appareil (par exemple, un téléphone) pour confirmer qu'il prend en charge le transfert de données.

Si vous n'êtes pas sûr de votre câble ou si vous rencontrez toujours des problèmes, décrivez votre configuration (par exemple, les ports de votre ordinateur, le type de câble, ce que vous voyez lors du branchement), et je pourrai vous guider davantage !