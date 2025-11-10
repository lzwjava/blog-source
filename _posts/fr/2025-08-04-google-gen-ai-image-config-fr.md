---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Configuration d'Image Google Gen AI
translated: true
type: note
---

Voici un aperçu rapide : le paramètre `image_size` n'est pas pris en charge dans le SDK Python Google Gen AI (Gemini/Imagen). Au lieu de cela, vous choisissez parmi des variantes de modèles (qui ont chacune des résolutions par défaut implicites), vous contrôlez le **ratio d'aspect**, et—si vous avez besoin de plus de pixels—vous appliquez un **upscale**. Vous pouvez également ajuster la **compression** et le **format de sortie**, plus les paramètres habituels comme le "nombre d'images", le "negative prompt", les paramètres de "sécurité" et de "personne".

## Variantes de Modèles

Vous choisissez un nom de modèle—chaque variante a sa propre résolution par défaut et son profil de performance :

* Famille **imagen-3.0** :

  * `imagen-3.0-generate-002`
  * `imagen-3.0-generate-001`
  * `imagen-3.0-fast-generate-001`
  * `imagen-3.0-capability-001`
* Famille **imagen-4.0 (Aperçu)** :

  * `imagen-4.0-generate-preview-06-06`
  * `imagen-4.0-fast-generate-preview-06-06`
  * `imagen-4.0-ultra-generate-preview-06-06`
* **Anciennes versions** : `imagegeneration@002`, `@005`, `@006` ([Google Cloud][1])

## Résolution par Défaut

Par défaut, une sortie carrée ("1:1") de ces modèles est de **1024 × 1024 pixels**. Si vous avez besoin d'un fichier plus petit, vous pouvez le sous-échantillonner localement ; si vous avez besoin d'une résolution plus élevée, voir **Upscaling** ci-dessous. ([raymondcamden.com][2])

## Ratios d'Aspect

Au lieu de spécifier des dimensions absolues, utilisez le champ `aspect_ratio` dans votre `GenerateImagesConfig`. Valeurs prises en charge :

* `1:1` (carré)
* `3:4` (portrait, plus haut, pour les réseaux sociaux)
* `4:3` (format classique photo/TV)
* `16:9` (paysage grand écran)
* `9:16` (format vertical/portrait, par ex. pour fonds d'écran de téléphone) ([Google Cloud][1], [Google AI for Developers][3])

Vous trouverez la même liste documentée dans les tutoriels de la communauté :

* DataCamp souligne ces cinq ratios exacts pour Imagen 3 ([DataCamp][4])
* Le guide de CodeSignal les énumère également pour Gemini/Imagen ([CodeSignal][5])

## Upscaling

Si vous avez besoin de véritables sorties "2K" ou "4K", appelez le mode **upscale** :

```python
from google.genai import types
config = types.GenerateImagesConfig(
    mode="upscale",
    upscale_config=types.UpscaleConfig(upscale_factor="x2"),
)
```

* `"x2"` double chaque dimension (par ex. 1024 → 2048, environ 2K)
* `"x4"` quadruple (par ex. 1024 → 4096, environ 4K) ([Google Cloud][1])

## Compression & Formats

* **Qualité JPEG** : utilisez `compression_quality` (0–100, défaut 75) pour arbitrer entre la taille du fichier et le détail ([Google Cloud][1])
* **Types MIME** : via `output_options.mime_type`, vous pouvez choisir
  `image/jpeg`, `image/png`, `image/gif`, `image/webp`, `image/bmp`, `image/tiff`, ou `image/vnd.microsoft.icon` ([Google Cloud][6])

## Options de Configuration Supplémentaires

Tout le reste se trouve dans `GenerateImagesConfig` :

```python
config = types.GenerateImagesConfig(
    number_of_images=1,           # nombre d'images à générer
    seed=1234,                    # pour des sorties déterministes
    enhance_prompt=True,          # réécriture de prompt basée sur LLM
    negative_prompt="exclure les chiens",
    language="en",
    safety_filter_level="block_medium_and_above",  
    person_generation="allow_adult",
)
```

Ces options vous permettent de contrôler l'aléatoire, l'amélioration du prompt, les seuils de sécurité et si le modèle peut inclure des personnes. ([Google Cloud][1])

## Recommandation

Supprimez votre ligne `image_size="2K"`—ce flag n'existe pas. Au lieu de cela :

1. **Choisissez le bon modèle** pour un compromis vitesse vs. qualité.
2. Utilisez **`aspect_ratio`** pour le cadrage.
3. Si vous avez vraiment besoin de plus de pixels, générez à la résolution de base puis appliquez l'**upscale** intégré ("x2" ou "x4").
4. Ajustez **`compression_quality`** ou sous-échantillonnez localement pour des fichiers plus petits.

Avec ces réglages, vous pouvez obtenir un cadrage carré ou cinématographique, des sorties petites ou haute résolution, sans utiliser le paramètre non pris en charge `image_size`.

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api "Generate images  |  Generative AI on Vertex AI  |  Google Cloud"
[2]: https://www.raymondcamden.com/2025/01/30/generative-ai-images-with-gemini-and-imagen-an-introduction?utm_source=chatgpt.com "Generative AI Images with Gemini and Imagen"
[3]: https://ai.google.dev/gemini-api/docs/imagen?utm_source=chatgpt.com "Generate images using Imagen | Gemini API | Google AI for ..."
[4]: https://www.datacamp.com/tutorial/imagen-3 "Imagen 3: A Guide With Examples in the Gemini API | DataCamp"
[5]: https://codesignal.com/learn/courses/creating-images-with-geminis-imagen-and-flask/lessons/generating-a-simple-image-with-geminis-imagen-and-flask?utm_source=chatgpt.com "Generating a Simple Image with Gemini's Imagen and Flask"
[6]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images?utm_source=chatgpt.com "Generate images using text prompts"