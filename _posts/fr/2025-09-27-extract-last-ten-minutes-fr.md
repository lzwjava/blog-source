---
audio: false
generated: true
image: false
lang: fr
layout: post
model: google/gemini-2.5-flash
title: Extraction des dix dernières minutes audio
translated: true
type: note
---

Pour obtenir les 10 dernières minutes du fichier audio `lobby-zh.ogg`, vous devez utiliser les informations suivantes :

1.  **Durée totale :** La durée du fichier d'entrée est de `00:33:34.40`.
2.  **Longueur du segment souhaité :** 10 minutes (ou 600 secondes).
3.  **Calcul de l'heure de début :** Vous devez calculer le point 10 minutes *avant* la fin du fichier.

### Calcul

*   Durée totale en secondes :
    $$(33 \times 60) + 34.40 = 1980 + 34.40 = 2014.40 \text{ secondes}$$
*   Heure de début :
    $$2014.40 \text{ secondes} - 600 \text{ secondes} = 1414.40 \text{ secondes}$$

Au format `HH:MM:SS.sss` :
$$1414.40 \text{ secondes} = 23 \text{ minutes et } 34.40 \text{ secondes} \quad (1414.40 / 60 = 23.5733\dots)$$
$$\text{Heure de début} = 00:23:34.40$$

### Commande FFmpeg

Vous utiliserez l'option d'entrée `-ss` (rechercher la position) combinée à l'option `-t` (durée).

1.  `-ss 00:23:34.40` : Définit la position de départ pour l'extraction.
2.  `-t 00:10:00` : Définit la durée du segment de sortie à exactement 10 minutes.

```bash
ffmpeg -i lobby-zh.ogg -ss 00:23:34.40 -t 00:10:00 last_10_minutes.ogg
```

**Note :** Si vous souhaitez utiliser les paramètres de débit binaire/codec d'origine du fichier de sortie, vous pouvez ajouter `-c copy` pour un traitement plus rapide :

```bash
ffmpeg -i lobby-zh.ogg -ss 00:23:34.40 -t 00:10:00 -c copy last_10_minutes_copy.ogg
```