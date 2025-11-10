---
audio: false
generated: true
lang: fr
layout: post
title: Flasher Pico avec un fichier UF2
translated: true
type: note
---

Pour flasher le fichier `RPI_PICO-20250415-v1.25.0.uf2` sur votre Raspberry Pi Pico, qui est monté à `/media/lzw/RPI-RP2`, utilisez la commande suivante :

```bash
cp ~/Downloads/RPI_PICO-20250415-v1.25.0.uf2 /media/lzw/RPI-RP2/
```

### Explication
- `cp` : Copie le fichier.
- `~/Downloads/RPI_PICO-20250415-v1.25.0.uf2` : Le chemin vers votre fichier `.uf2` dans le répertoire Téléchargements.
- `/media/lzw/RPI-RP2/` : Le point de montage du lecteur `RPI-RP2` du Pico, comme indiqué dans votre sortie.

### Après l'exécution de la commande
- Le fichier `.uf2` sera copié sur le Pico, et l'appareil flashera automatiquement le firmware.
- Le lecteur `RPI-RP2` se démontera (disparaîtra) une fois le flashage terminé, indiquant le succès.
- Si le lecteur réapparaît, le flashage a peut-être échoué. Vérifiez que le fichier `.uf2` est valide ou essayez un autre câble/port USB.

Si vous rencontrez des problèmes ou avez besoin d'aide supplémentaire, faites-le-moi savoir !