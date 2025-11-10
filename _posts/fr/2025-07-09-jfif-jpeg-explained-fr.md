---
audio: false
generated: true
image: false
lang: fr
layout: post
title: 'JFIF expliqué : c''est simplement le JPEG'
translated: true
type: note
---

JFIF signifie **JPEG File Interchange Format**.

### Qu'est-ce que JFIF

* Ce n'est pas un format d'image différent du JPEG, mais plutôt **une manière standardisée d'intégrer des métadonnées et une structure dans un fichier JPEG**.
* Les fichiers avec l'extension `.jfif` sont toujours des **images JPEG** — ils déclarent simplement la spécification JFIF dans leurs en-têtes.
* De nombreux outils (en particulier les plus anciens comme Windows Paint ou certains appareils photo/scanners) utilisaient `.jfif` comme extension par défaut au lieu de `.jpg` ou `.jpeg`.

Ainsi, lorsque vous voyez un fichier `.jfif`, vous pouvez le traiter exactement comme une image `.jpg`.

---

### Comment convertir JFIF en formats d'image standard

1. **Renommer l'extension**

   * Dans la plupart des cas, renommez simplement `image.jfif` → `image.jpg`.
   * Comme le format sous-jacent est JPEG, la plupart des programmes l'ouvriront sans problème.

2. **Utiliser des éditeurs d'image**

   * Ouvrez le fichier `.jfif` dans Photoshop, GIMP, Paint ou Preview (macOS).
   * Enregistrez/Exportez-le en `.jpg` ou `.png`.

3. **Utiliser Python (Pillow)**

   ```python
   from PIL import Image

   img = Image.open("image.jfif")
   img.save("image.jpg")   # enregistrer en JPEG
   img.save("image.png")   # ou convertir en PNG
   ```

4. **Utiliser la ligne de commande (ImageMagick)**

   ```bash
   magick image.jfif image.jpg
   ```

   Ou avec FFmpeg (puisqu'il peut aussi décoder les images) :

   ```bash
   ffmpeg -i image.jfif image.jpg
   ```

---

✅ En résumé : **JFIF est simplement un JPEG**, vous pouvez donc l'ouvrir comme n'importe quel `.jpg`. Si la compatibilité pose problème, renommez-le ou convertissez-le avec Pillow/ImageMagick.

Voulez-vous que je vous donne un **script Python** rapide qui peut convertir par lots tous les fichiers `.jfif` d'un dossier en `.jpg` ?