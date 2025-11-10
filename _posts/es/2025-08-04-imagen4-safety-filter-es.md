---
audio: false
generated: true
image: false
lang: es
layout: post
title: Bloqueo Bajo y Superior
translated: true
type: note
---

Estás viendo este error:

```
Only block_low_and_above is supported for safetySetting.
```

Esto sucede cuando configuras `safety_filter_level="BLOCK_MEDIUM_AND_ABOVE"` (o cualquier otro valor) en `GenerateImagesConfig` para los modelos **Imagen‑4**—pero al momento de tu solicitud (agosto 2025), **la API solo permite `"BLOCK_LOW_AND_ABOVE"`** para el filtrado de seguridad de imágenes en esos modelos ([Google Cloud][1]).

---

### ✅ Cómo solucionar tu código

Simplemente actualiza el `safety_filter_level` al valor compatible:

```python
from google import genai
from google.genai.types import GenerateImagesConfig

client = genai.Client()

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="Un perro leyendo un periódico",
    config=GenerateImagesConfig(
        image_size="2K",
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

image.generated_images[0].image.save("output-image.png")
print(
    f"Imagen creada usando {len(image.generated_images[0].image.image_bytes)} bytes"
)
```

* `safety_filter_level="BLOCK_LOW_AND_ABOVE"`: solo este valor es compatible con **Imagen 4**. Otros umbrales como `"BLOCK_MEDIUM_AND_ABOVE"` causarán el error 400 INVALID\_ARGUMENT ([Medium][2], [Google AI for Developers][3]).
* `number_of_images=1` es explícito para que quede claro que estás solicitando una imagen por llamada.

---

### 🧾 Otros parámetros opcionales:

* `person_generation="ALLOW_ADULT"` es la configuración predeterminada, pero está bien ser explícito (bloquea niños; permite imágenes de dominio adulto) ([Google Cloud][1]).
* `image_size="2K"` es válido según tu código—solo asegúrate de que tu versión del SDK lo admita.

---

### TL;DR — Lista de verificación rápida

| Paso | Qué hacer                                                   |
| ---- | ------------------------------------------------------------ |
| ✅ 1  | Cambia safety\_filter\_level a `"BLOCK_LOW_AND_ABOVE"`      |
| 🧾 2 | Mantén `person_generation="ALLOW_ADULT"` (o omítelo para usar el predeterminado) |
| 🚫 3 | No uses `"BLOCK_MEDIUM_AND_ABOVE"` o `"BLOCK_ONLY_HIGH"`  |
| ⏱ 4  | No cambies la configuración de seguridad hasta que Google agregue más niveles      |

¡Avísame si recibes otro error—estaré encantado de ayudar!

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api?utm_source=chatgpt.com "Generate images | Generative AI on Vertex AI"
[2]: https://medium.com/generative-ai/3-ways-to-try-googles-imagen-4-image-generator-if-you-re-outside-the-us-ee2a1895ca9b?utm_source=chatgpt.com "3 Ways to Try Google's Imagen 4 Image Generator if You're ..."
[3]: https://ai.google.dev/gemini-api/docs/migrate?utm_source=chatgpt.com "Migrate to the Google GenAI SDK - Gemini API"