---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Supprimer la largeur et la hauteur
translated: true
type: note
---

L'erreur que vous voyez :

```
Extra inputs are not permitted [type=extra_forbidden, input_value=1200, input_type=int]
```

est causée par le passage de `width` et `height` dans `GenerateImagesConfig`, qui ne prend **pas en charge** ces champs. Selon le message d'erreur et la conception de l'API Gemini, `image_size` doit être l'une des **valeurs d'énumération prédéfinies**, et `CUSTOM` n'est **pas pris en charge** pour l'API Gemini publique (à ce jour).

---

### ✅ Correction

Vous devez **supprimer** `width` et `height`, et utiliser une valeur d'énumération valide pour `image_size` telle que `"1024x1024"` ou `"512x512"`.

Voici la version corrigée :

```python
from google import genai
from google.genai.types import GenerateImagesConfig
import os

# Configurer le client Vertex AI
client = genai.Client(
    vertexai=True,
    project=os.getenv('GOOGLE_CLOUD_PROJECT'),
    location=os.getenv('GOOGLE_CLOUD_LOCATION')
)

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(
        image_size="1024x1024",  # utiliser une valeur autorisée au lieu de CUSTOM
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

print(f"Created OG image using {len(image.generated_images[0].image.image_bytes)} bytes")
```

---

### 🔍 Pour générer une image de **taille personnalisée** comme `1200x630` :

Les API publiques Gemini/Imagen actuelles **ne prennent pas en charge** les tailles d'image arbitraires. Si vous avez besoin de 1200×630 (par exemple, pour les images OG), vos options sont :

1. **Post-traiter l'image** après la génération pour la redimensionner/la recadrer aux dimensions souhaitées.
2. Utiliser **un autre modèle/API** qui prend en charge les dimensions personnalisées (par exemple, SDXL de Stability AI, Midjourney, ou des points de terminaison privés).
3. Si vous utilisez un accès interne (par exemple, chez Google), consultez la documentation interne ou votre responsable de compte Vertex AI.

Faites-moi savoir si vous avez besoin d'aide pour redimensionner l'image après sa génération.