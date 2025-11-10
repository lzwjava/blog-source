---
audio: false
generated: true
lang: fr
layout: post
title: Flasher le micrologiciel Pico via UF2
translated: true
type: note
---

Pour flasher le firmware sur votre Raspberry Pi Pico (ou une carte basée sur le RP2040) en mode BOOTSEL en copiant un fichier `.uf2` sur le lecteur `RPI-RP2`, suivez ces étapes :

### Guide étape par étape
1. **Confirmer que l'appareil est en mode BOOTSEL** :
   - Votre appareil devrait apparaître comme un lecteur USB nommé `RPI-RP2` lorsqu'il est connecté à votre ordinateur. Cela confirme qu'il est en mode BOOTSEL (comme indiqué par `Bus 001 Device 009: ID 2e8a:0003 Raspberry Pi RP2 Boot`).
   - S'il n'est pas en mode BOOTSEL, débranchez l'appareil, maintenez le bouton BOOTSEL sur le Pico enfoncé, et branchez-le sur le port USB de votre ordinateur tout en maintenant le bouton. Relâchez le bouton après quelques secondes.

2. **Obtenir un fichier `.uf2` valide** :
   - **MicroPython** : Téléchargez le dernier firmware MicroPython pour le Raspberry Pi Pico depuis le [site officiel de MicroPython](https://micropython.org/download/rp2-pico/). Choisissez le fichier `.uf2` pour le Pico ou Pico W (par exemple, `rp2-pico-latest.uf2`).
   - **CircuitPython** : Téléchargez le firmware CircuitPython depuis le [site de CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) pour le Pico ou Pico W.
   - **Programme personnalisé** : Si vous avez écrit un programme (par exemple, en C/C++ en utilisant le Pico SDK), compilez-le pour générer un fichier `.uf2`. Par exemple, utilisez le Pico SDK ou l'IDE Arduino pour construire votre projet.
   - Enregistrez le fichier `.uf2` à un emplacement facile d'accès sur votre ordinateur (par exemple, le Bureau ou le dossier Téléchargements).

3. **Localiser le lecteur RPI-RP2** :
   - Sur votre ordinateur, ouvrez l'explorateur de fichiers :
     - **Windows** : Cherchez `RPI-RP2` sous "Ce PC" en tant que lecteur amovible.
     - **macOS** : Le lecteur devrait apparaître sur le Bureau ou dans le Finder sous "Périphériques".
     - **Linux** : Vérifiez sous `/media` ou `/mnt`, ou utilisez `lsblk` pour lister les lecteurs connectés.
   - Si le lecteur n'apparaît pas, assurez-vous que le câble USB prend en charge le transfert de données (et pas seulement l'alimentation) et essayez un port USB ou un câble différent.

4. **Copier le fichier `.uf2` sur le lecteur RPI-RP2** :
   - Glissez-déposez le fichier `.uf2` sur le lecteur `RPI-RP2`, ou copiez-collez-le en utilisant votre explorateur de fichiers.
   - Alternativement, utilisez une commande terminal (sur Linux/macOS) :
     ```bash
     cp /chemin/vers/votre/fichier.uf2 /media/votre_nom_utilisateur/RPI-RP2/
     ```
     Remplacez `/chemin/vers/votre/fichier.uf2` par le chemin vers votre fichier `.uf2` et ajustez le point de montage si nécessaire.

5. **Attendre la fin du processus de flash** :
   - Une fois le fichier `.uf2` copié, le Raspberry Pi Pico flash le firmware automatiquement. Le lecteur `RPI-RP2` disparaîtra (démontage) lorsque l'appareil redémarre, indiquant que le processus est terminé.
   - Cela prend typiquement quelques secondes. Ne débranchez pas l'appareil pendant ce temps.

6. **Vérifier l'appareil** :
   - Après le flash, le Pico devrait quitter le mode BOOTSEL et exécuter le nouveau firmware.
   - Pour MicroPython ou CircuitPython, connectez-vous à l'appareil en utilisant un terminal (par exemple, PuTTY, screen, ou l'IDE Thonny) via le port série USB (par exemple, `COM3` sur Windows ou `/dev/ttyACM0` sur Linux/macOS). Vous devriez voir une invite REPL Python.
   - Pour les programmes personnalisés, vérifiez le comportement attendu (par exemple, une LED qui clignote, une sortie série, etc.).
   - Si le lecteur `RPI-RP2` réapparaît, le flash a peut-être échoué. Essayez un autre fichier `.uf2` ou vérifiez les problèmes matériels (par exemple, câble USB, puce de mémoire flash).

### Dépannage
- **Le lecteur n'apparaît pas** : Assurez-vous que le Pico est en mode BOOTSEL et que le câble USB prend en charge le transfert de données. Essayez d'appuyer sur BOOTSEL, puis d'appuyer brièvement sur le bouton RESET (s'il est disponible) pendant la connexion.
- **La copie échoue ou le lecteur réapparaît** : Le fichier `.uf2` peut être corrompu, ou la mémoire flash peut être défectueuse. Téléchargez un nouveau fichier `.uf2` ou testez avec un fichier minimal, comme celui de MicroPython. Si le problème persiste, utilisez `picotool` pour diagnostiquer :
  ```bash
  picotool info
  ```
  Installez `picotool` depuis le [Raspberry Pi Pico SDK](https://github.com/raspberrypi/picotool).
- **Aucune réponse après le flash** : Si vous utilisez MicroPython/CircuitPython, assurez-vous que votre IDE (par exemple, Thonny) est configuré sur le bon port série. Pour les programmes personnalisés, vérifiez que le code a été compilé correctement.

### Exemple : Flasher MicroPython
1. Téléchargez le fichier `.uf2` MicroPython depuis [micropython.org](https://micropython.org/download/rp2-pico/).
2. Maintenez BOOTSEL enfoncé, branchez le Pico, puis relâchez BOOTSEL.
3. Ouvrez votre explorateur de fichiers, trouvez le lecteur `RPI-RP2`, et copiez le fichier `.uf2` dessus.
4. Attendez que le lecteur disparaisse.
5. Ouvrez l'IDE Thonny, sélectionnez le port série du Pico, et commencez à coder en MicroPython.

Si vous avez besoin d'aide avec un fichier `.uf2` spécifique, un outil, ou une configuration (par exemple, installer `picotool` ou utiliser Thonny), faites-le moi savoir !