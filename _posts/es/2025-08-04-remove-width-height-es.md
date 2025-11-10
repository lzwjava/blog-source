---
audio: false
generated: true
image: false
lang: es
layout: post
title: Eliminar el ancho y el alto
translated: true
type: note
---

El error que estás viendo:

```
Extra inputs are not permitted [type=extra_forbidden, input_value=1200, input_type=int]
```

se debe a que estás pasando `width` y `height` a `GenerateImagesConfig`, que **no admite** esos campos. Según el mensaje de error y el diseño de la API de Gemini, `image_size` debe ser uno de los **valores de enumeración predefinidos**, y `CUSTOM` **no es compatible** con la API pública de Gemini (hasta ahora).

---

### ✅ Solución

Debes **eliminar** `width` y `height`, y usar un `image_size` válido de la enumeración, como `"1024x1024"` o `"512x512"`.

Aquí tienes la versión corregida:

```python
from google import genai
from google.genai.types import GenerateImagesConfig
import os

# Configurar el cliente de Vertex AI
client = genai.Client(
    vertexai=True,
    project=os.getenv('GOOGLE_CLOUD_PROJECT'),
    location=os.getenv('GOOGLE_CLOUD_LOCATION')
)

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(
        image_size="1024x1024",  # usa un valor permitido en lugar de CUSTOM
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

print(f"Created OG image using {len(image.generated_images[0].image.image_bytes)} bytes")
```

---

### 🔍 Para generar una imagen con **tamaño personalizado** como `1200x630`:

Las APIs públicas actuales de Gemini/Imagen **no admiten** tamaños de imagen arbitrarios. Si necesitas 1200×630 (por ejemplo, para imágenes OG), tus opciones son:

1. **Post-procesar la imagen** después de generarla para cambiar el tamaño/recortarla a las dimensiones deseadas.
2. Usar **un modelo/API diferente** que admita dimensiones personalizadas (por ejemplo, SDXL de Stability AI, Midjourney o endpoints privados).
3. Si tienes acceso interno (por ejemplo, dentro de Google), confirma con la documentación interna o con el administrador de tu cuenta de Vertex AI.

Déjame saber si necesitas ayuda para cambiar el tamaño de la imagen después de generarla.