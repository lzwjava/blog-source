---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Extrait de code Python officiel corrigé pour Imagen
translated: true
type: note
---

Vous avez essentiellement implémenté la logique correcte, mais les instructions pour **résoudre le problème** sont légèrement inexactes. Voici une version nettoyée adaptée de l'exemple officiel dans la documentation :

```python
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# ← Définissez votre clé API ou utilisez la variable d'environnement GOOGLE_API_KEY / GEMINI_API_KEY
client = genai.Client(api_key="VOTRE_CLÉ_API")

response = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="Un chien lisant un journal",
    config=types.GenerateImagesConfig(
        number_of_images=1,
        # image_size="2K",  # optionnel pour une résolution 2K ; nécessite une version plus récente de la bibliothèque fast-preview
        aspect_ratio="1:1",
        safety_filter_level="BLOCK_MEDIUM_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    )
)

for i, generated in enumerate(response.generated_images):
    raw = generated.image.image_bytes
    pil = Image.open(BytesIO(raw))  # Convertir les octets bruts en image PIL
    pil.save(f"image-resultat-{i+1}.png")
    print(f"Image {i+1} sauvegardée, {len(raw):,} octets")
```

Bien que l'extrait Python de Google ait également utilisé `image_size="2K"` pour son modèle 4‑preview, soyez conscient que :

* Vous devez utiliser `google-genai` v1.28 ou plus récent pour prendre en charge `image_size` sur les modèles Imagen 4 ;
* Sinon, omettez ce champ (la valeur par défaut est 1 024×1 024 à une résolution carrée fixe) ([GitHub][1]).

---

### 🚩 Pièges Courants & Corrections

1. **Installation de PIL manquante**
   Si vous avez installé `google-genai` mais n'avez pas ajouté `Pillow`, les appels à `.image.save()` peuvent échouer silencieusement (ou lever une `AttributeError`). Assurez-vous d'avoir :

   ```bash
   pip install pillow
   ```

2. **Aucune clé API ou mauvais service sélectionné**
   Si vous appelez `genai.Client()` sans clé API et sans informations d'identification cloud, le client échoue au moment de l'appel avec une erreur d'authentification (par exemple, `"401 UNAUTHENTICATED"`). Passez soit `api_key="…"` soit définissez `GOOGLE_API_KEY` dans votre shell, pour l'API Gemini Developer ([GitHub][1]).

3. **Incompatibilité de version de la bibliothèque**
   Les anciennes versions de la bibliothèque ou l'ancien module `google.generativeai` n'exposent pas `generate_images()` et peuvent encore utiliser par défaut l'interface générative-ai *obsolète*. Assurez-vous toujours d'avoir :

   ```bash
   pip install --upgrade google-genai
   ```

   Le problème "impossible d'ouvrir les images de sortie" dans les anciens dépôts (`deprecated-generative-ai-python`) résultait de cette incompatibilité, et générait généralement une `UnidentifiedImageError` ou une `FileNotFoundError` après avoir écrit des octets corrompus ([GitHub][1]).

4. **UnidentifiedImageError lors de l'ouverture avec PIL**
   Si vous voyez :

   ```
   PIL.UnidentifiedImageError: cannot identify image file <_io.BytesIO …>
   ```

   cela signifie généralement que le tampon de réponse est corrompu ou incomplet. Vérifiez bien que :

   * Votre prompt n'a pas été filtré (par exemple, blocage RAI) ;
   * Vous ne décodez pas les octets en base64 (le SDK renvoie déjà des données brutes PNG/JPEG) ;
   * Votre téléchargement de fichier n'est pas tronqué.

---

### ✅ Pourquoi Cette Correction Fonctionne

* L'extrait officiel dans la documentation de Google du 2025‑08‑01 utilise exactement :

  ```python
  types.GenerateImagesConfig(image_size="2K")
  ```

  avant de sauvegarder via `result.image.save(...)` ([Google Cloud][2]).

* Mais d'autres guides utilisant les modèles Imagen 3 ne spécifient que `number_of_images`, `aspect_ratio` et les paramètres de sécurité—sans `image_size`—car Imagen 3 ne le prend pas en charge ([GitHub][1]).

Suivre le flux ci-dessus devrait vous débloquer. Si vous rencontrez un message d'erreur spécifique (comme HTTP 403, clé JSON manquante dans la réponse, etc.), n'hésitez pas à le coller ici et je vous aiderai à résoudre l'étape suivante.

[1]: https://github.com/google-gemini/generative-ai-python/issues/674?utm_source=chatgpt.com "can not open the output images from imagen API · Issue #674 · google-gemini/deprecated-generative-ai-python · GitHub"
[2]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview?utm_source=chatgpt.com "Imagen on Vertex AI | AI Image Generator"