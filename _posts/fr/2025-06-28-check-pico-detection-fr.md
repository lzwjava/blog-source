---
audio: false
generated: true
lang: fr
layout: post
title: Détection de la Raspberry Pi Pico sur Ubuntu
translated: true
type: note
---

Pour vérifier si votre Raspberry Pi Pico est détecté par Ubuntu après l'avoir branché, suivez ces étapes :

1. **Vérifier les périphériques USB** :
   - Ouvrez un terminal et exécutez :
     ```bash
     lsusb
     ```
   - Cherchez une entrée comme `Raspberry Pi Pico` ou un périphérique avec l'ID vendeur `2E8A` (l'ID vendeur de Raspberry Pi). Par exemple :
     ```
     Bus XXX Device XXX: ID 2e8a:0003 Raspberry Pi Pico
     ```

2. **Vérifier les ports série** :
   - Si le Pico est en mode BOOTSEL (pour flasher le firmware) ou exécute un programme MicroPython/Arduino avec une sortie série, vérifiez la présence d'un port série :
     ```bash
     ls /dev/tty*
     ```
   - Cherchez un périphérique comme `/dev/ttyACM0` ou `/dev/ttyUSB0`. Le Pico apparaît typiquement comme `/dev/ttyACM0` lorsqu'il exécute MicroPython.

3. **Vérifier les périphériques de stockage (Mode BOOTSEL)** :
   - Si le Pico est en mode BOOTSEL (en maintenant le bouton BOOTSEL enfoncé lors du branchement), il devrait apparaître comme un périphérique de stockage de masse. Exécutez :
     ```bash
     lsblk
     ```
   - Cherchez un périphérique comme `/dev/sdb` (ou similaire) avec un point de montage, souvent nommé `RPI-RP2`.

4. **Utiliser `dmesg` pour les logs du noyau** :
   - Exécutez :
     ```bash
     dmesg | tail -n 20
     ```
   - Vérifiez les messages indiquant que le Pico a été détecté, par exemple :
     ```
     [1234.567890] usb 1-1: New USB device found, idVendor=2e8a, idProduct=0003
     [1234.567891] usb 1-1: Product: Pico
     [1234.567892] cdc_acm 1-1:1.0: ttyACM0: USB ACM device
     ```
   - Ceci confirme que le Pico est reconnu et qu'un port lui est attribué (par exemple, `ttyACM0`).

5. **Tester avec MicroPython (si installé)** :
   - Si vous utilisez MicroPython, installez un outil comme `picocom` ou `minicom` :
     ```bash
     sudo apt install picocom
     ```
   - Connectez-vous au port série du Pico :
     ```bash
     picocom /dev/ttyACM0
     ```
   - S'il est détecté, vous devriez voir l'invite REPL de MicroPython (>>>). Appuyez sur `Ctrl+C` pour quitter.

**Notes** :
- Assurez-vous que le Pico est correctement connecté via un bon câble USB (données, pas seulement alimentation).
- En mode BOOTSEL, le Pico apparaît comme un périphérique de stockage, pas comme un périphérique série.
- S'il n'est pas détecté, essayez un autre port USB, un autre câble, ou vérifiez si les pilotes (comme `cdc_acm` pour le série) sont chargés :
  ```bash
  lsmod | grep cdc_acm
  ```

Si vous ne voyez pas le Pico dans l'une de ces vérifications, donnez-moi plus de détails (par exemple, le mode du Pico, ce que vous essayez de faire), et je peux aider à diagnostiquer le problème plus en détail !