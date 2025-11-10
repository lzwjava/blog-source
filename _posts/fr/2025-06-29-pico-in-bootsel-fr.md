---
audio: false
generated: true
lang: fr
layout: post
title: Raspberry Pi Pico en mode BOOTSEL
translated: true
type: note
---

L'appareil listé comme `Bus 001 Device 009: ID 2e8a:0003 Raspberry Pi RP2 Boot` est un Raspberry Pi Pico (ou une carte similaire basée sur le RP2040) en mode BOOTSEL. Voici une explication :

- **ID 2e8a:0003** : Il s'agit de l'ID Vendeur USB (2e8a) et de l'ID Produit (0003) attribués à Raspberry Pi pour le microcontrôleur RP2040 lorsqu'il est en mode BOOTSEL.
- **Raspberry Pi RP2 Boot** : Indique que l'appareil est un Raspberry Pi Pico (ou une autre carte basée sur le RP2040, comme le Pico W ou une carte personnalisée) qui est entré dans son mode bootloader. Dans ce mode, l'appareil apparaît comme un périphérique de stockage de masse USB, vous permettant de télécharger un firmware (par exemple, des fichiers .uf2) en les copiant sur le lecteur.

### Qu'est-ce que le mode BOOTSEL ?
Le mode BOOTSEL est activé en maintenant le bouton BOOTSEL enfoncé sur le Raspberry Pi Pico tout en le branchant sur un port USB ou en le réinitialisant tout en maintenant le bouton enfoncé. Ce mode est utilisé pour flasher un nouveau firmware ou de nouveaux programmes sur le microcontrôleur RP2040. Lorsqu'il est dans ce mode, le Pico apparaît comme un lecteur amovible (nommé `RPI-RP2`) sur votre ordinateur.

### Pourquoi apparaît-il ainsi ?
Votre appareil est probablement en mode BOOTSEL parce que :
1. Vous avez intentionnellement appuyé sur le bouton BOOTSEL pour mettre à jour ou flasher un firmware.
2. L'appareil n'exécute pas de programme et revient par défaut en mode bootloader (par exemple, après un flash raté ou une réinitialisation).
3. Il pourrait y avoir un problème avec le firmware ou les connexions, le faisant rester en mode bootloader. Par exemple, des problèmes avec la mémoire flash ou un flashage incorrect peuvent amener l'appareil à revenir à ce mode.[](https://forums.raspberrypi.com/viewtopic.php?p=2078375)

### Que faire ensuite ?
- **Si vous voulez flasher un firmware** : Copiez un fichier `.uf2` valide (par exemple, un firmware MicroPython ou CircuitPython, ou un programme compilé) sur le lecteur `RPI-RP2`. L'appareil flashera automatiquement le firmware et redémarrera, quittant le mode BOOTSEL.[](https://forum.arduino.cc/t/solved-nano-rp2040-connect-does-not-accept-uf2/888152)
- **S'il est bloqué en mode BOOTSEL** : Cela pourrait indiquer un problème avec la mémoire flash ou le firmware. Essayez :
  1. Re-flasher avec un fichier `.uf2` fonctionnel connu, comme le firmware MicroPython du site officiel de Raspberry Pi.
  2. Vérifier le câble USB et le port, car un câble défectueux peut causer des problèmes.[](https://raspberrypi.stackexchange.com/questions/139506/raspberry-pi-pico-doesnt-create-tty-file)
  3. Utiliser des outils comme `picotool` pour vérifier l'état de l'appareil ou le réinitialiser. Par exemple, exécutez `picotool info` pour vérifier l'état de l'appareil.[](https://forums.raspberrypi.com/viewtopic.php?p=2078375)
  4. Si vous utilisez une carte RP2040 personnalisée, assurez-vous que la puce flash est correctement connectée et configurée, car des problèmes avec les signaux QSPI ou les CI flash peuvent empêcher un flashage réussi.[](https://forums.raspberrypi.com/viewtopic.php?p=2078375)
- **Si vous voulez quitter le mode BOOTSEL** : Si un firmware valide est déjà flashé, débranchez l'appareil, assurez-vous que le bouton BOOTSEL n'est pas enfoncé, et rebranchez-le. L'appareil devrait démarrer dans son mode programmé (par exemple, en exécutant un script MicroPython ou un programme C).

### Notes supplémentaires
- Le RP2040 est le microcontrôleur utilisé dans le Raspberry Pi Pico, le Pico W et d'autres cartes. La désignation `RP2 Boot` se réfère spécifiquement au mode bootloader de la puce RP2040.[](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
- Si vous utilisez un Raspberry Pi Pico W, notez qu'il inclut des capacités sans fil, mais celles-ci ne sont pas actives en mode BOOTSEL.[](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
- Si vous rencontrez des erreurs (par exemple, `picotool` échoue à vérifier ou charger), cela pourrait être dû à un problème matériel (comme une puce flash défectueuse ou un problème de soudure sur une carte personnalisée) ou à un fichier de firmware corrompu.[](https://forums.raspberrypi.com/viewtopic.php?p=2078375)

Si vous avez besoin d'une aide spécifique (par exemple, pour flasher un firmware, dépanner ou identifier la carte exacte), donnez-moi plus de détails sur votre configuration ou ce que vous essayez d'accomplir !