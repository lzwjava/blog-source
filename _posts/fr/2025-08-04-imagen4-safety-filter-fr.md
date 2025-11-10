---
audio: false
generated: true
image: false
lang: fr
layout: post
title: BLOCK_LOW_AND_ABOVE
translated: true
type: note
---

Vous rencontrez cette erreur :

```
Only block_low_and_above is supported for safetySetting.
```

Cela se produit lorsque vous définissez `safety_filter_level="BLOCK_MEDIUM_AND_ABOVE"` (ou toute autre valeur) dans `GenerateImagesConfig` pour les modèles **Imagen‑4** — mais au moment de votre requête (août 2025), **l'API n'autorise que `"BLOCK_LOW_AND_ABOVE"`** pour le filtrage de sécurité des images sur ces modèles ([Google Cloud][1]).

---

### ✅ Comment corriger votre code

Mettez simplement à jour le `safety_filter_level` avec la valeur prise en charge :

```python
from google import genai
from google.genai.types import GenerateImagesConfig

client = genai.Client()

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="Un chien lisant un journal",
    config=GenerateImagesConfig(
        image_size="2K",
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

image.generated_images[0].image.save("output-image.png")
print(
    f"Image créée en utilisant {len(image.generated_images[0].image.image_bytes)} octets"
)
```

* `safety_filter_level="BLOCK_LOW_AND_ABOVE"` : seule cette valeur est prise en charge pour **Imagen 4**. D'autres seuils comme `"BLOCK_MEDIUM_AND_ABOVE"` provoqueront l'erreur 400 INVALID\_ARGUMENT ([Medium][2], [Google AI for Developers][3]).
* `number_of_images=1` est explicite pour clarifier que vous demandez une image par appel.

---

### 🧾 Autres paramètres optionnels :

* `person_generation="ALLOW_ADULT"` est le paramètre par défaut, mais il est bon d'être explicite (bloque les enfants ; autorise les images à caractère adulte) ([Google Cloud][1]).
* `image_size="2K"` est valide dans votre code — assurez-vous simplement que votre version du SDK le prend en charge.

---

### TL;DR — Liste de contrôle rapide

| Étape | Action à effectuer                                           |
| ---- | ------------------------------------------------------------ |
| ✅ 1  | Changez safety\_filter\_level en `"BLOCK_LOW_AND_ABOVE"`     |
| 🧾 2 | Gardez `person_generation="ALLOW_ADULT"` (ou omettre pour la valeur par défaut) |
| 🚫 3 | N'utilisez pas `"BLOCK_MEDIUM_AND_ABOVE"` ou `"BLOCK_ONLY_HIGH"` |
| ⏱ 4  | Ne modifiez pas le paramètre de sécurité avant que Google n'ajoute plus de niveaux |

Faites-moi savoir si vous obtenez une autre erreur — heureux de vous aider !

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api?utm_source=chatgpt.com "Generate images | Generative AI on Vertex AI"
[2]: https://medium.com/generative-ai/3-ways-to-try-googles-imagen-4-image-generator-if-you-re-outside-the-us-ee2a1895ca9b?utm_source=chatgpt.com "3 Ways to Try Google's Imagen 4 Image Generator if You're ..."
[3]: https://ai.google.dev/gemini-api/docs/migrate?utm_source=chatgpt.com "Migrate to the Google GenAI SDK - Gemini API"