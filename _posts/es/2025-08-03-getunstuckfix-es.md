---
audio: false
generated: true
image: false
lang: es
layout: post
title: Fragmento Oficial de Python de Imagen Corregido
translated: true
type: note
---

Básicamente has implementado la lógica correcta, pero las instrucciones para **salir del bloqueo** son ligeramente incorrectas. Aquí tienes una versión limpia adaptada del ejemplo oficial en la documentación:

```python
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# ← Establece tu clave API o usa la variable de entorno GOOGLE_API_KEY / GEMINI_API_KEY
client = genai.Client(api_key="TU_CLAVE_API")

response = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="Un perro leyendo un periódico",
    config=types.GenerateImagesConfig(
        number_of_images=1,
        # image_size="2K",  # opcional para resolución 2K; requiere la biblioteca de vista previa rápida más nueva
        aspect_ratio="1:1",
        safety_filter_level="BLOCK_MEDIUM_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    )
)

for i, generated in enumerate(response.generated_images):
    raw = generated.image.image_bytes
    pil = Image.open(BytesIO(raw))  # Convierte los bytes en bruto en una imagen PIL
    pil.save(f"imagen-salida-{i+1}.png")
    print(f"Imagen {i+1} guardada, {len(raw):,} bytes")
```

Aunque el fragmento de código de Google también usó `image_size="2K"` para su modelo 4‑preview, ten en cuenta que:

* Debes estar ejecutando `google-genai` v1.28 o más reciente para admitir `image_size` en los modelos Imagen 4;
* De lo contrario, omite ese campo (el valor predeterminado es 1,024×1,024 a una resolución de píxeles cuadrados fija) ([GitHub][1]).

---

### 🚩 Errores Comunes y Soluciones

1.  **Falta la instalación de PIL**
    Si instalaste `google-genai` pero no agregaste `Pillow`, las llamadas a `.image.save()` pueden fallar silenciosamente (o generar `AttributeError`). Asegúrate de:

    ```bash
    pip install pillow
    ```

2.  **Sin clave API o servicio incorrecto seleccionado**
    Si llamas a `genai.Client()` sin una clave API y sin credenciales de cloud, el cliente falla en el momento de la llamada con un error de autenticación (por ejemplo, `"401 UNAUTHENTICATED"`). Pasa `api_key="…"` o establece `GOOGLE_API_KEY` en tu shell, para Gemini Developer API ([GitHub][1]).

3.  **Versión de biblioteca no coincide**
    Las versiones antiguas de la biblioteca o el módulo heredado `google.generativeai` no exponen `generate_images()` y aún pueden usar por defecto la interfaz *obsoleta* de IA generativa. Siempre asegúrate de:

    ```bash
    pip install --upgrade google-genai
    ```

    El problema de "no se pueden abrir las imágenes de salida" en repositorios antiguos (`deprecated-generative-ai-python`) resultó de esa falta de coincidencia, y generalmente arrojaba `UnidentifiedImageError` o `FileNotFoundError` después de escribir bytes corruptos ([GitHub][1]).

4.  **UnidentifiedImageError al abrir con PIL**
    Si ves:

    ```
    PIL.UnidentifiedImageError: cannot identify image file <_io.BytesIO …>
    ```

    eso generalmente significa que el búfer de respuesta está corrupto o incompleto. Verifica que:

    * Tu prompt no haya sido filtrado (por ejemplo, bloqueado por RAI);
    * No estés decodificando en base64 los bytes (el SDK ya devuelve datos PNG/JPEG en bruto);
    * Tu descarga de archivo no se haya interrumpido.

---

### ✅ Por Qué Esta Solución Funciona

* El fragmento de código oficial en la documentación de Google del 01-08-2025 usa exactamente:

  ```python
  types.GenerateImagesConfig(image_size="2K")
  ```

  antes de guardar mediante `result.image.save(...)` ([Google Cloud][2]).

* Pero otras guías que usan modelos Imagen 3 solo especifican `number_of_images`, `aspect_ratio` y configuraciones de seguridad, sin `image_size`, porque Imagen 3 no lo admite ([GitHub][1]).

Seguir el flujo anterior debería desbloquearte. Si encuentras un mensaje de error específico (como HTTP 403, falta clave JSON en la respuesta, etc.), no dudes en pegarlo aquí y te ayudaré a solucionar el siguiente paso.

[1]: https://github.com/google-gemini/generative-ai-python/issues/674?utm_source=chatgpt.com "can not open the output images from imagen API · Issue #674 · google-gemini/deprecated-generative-ai-python · GitHub"
[2]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview?utm_source=chatgpt.com "Imagen on Vertex AI | AI Image Generator"