---
audio: false
generated: true
image: false
lang: es
layout: post
title: Configuración de Imágenes de Google Gen AI
translated: true
type: note
---

Aquí tienes un resumen rápido: el parámetro `image_size` no es compatible con el Google Gen AI (Gemini/Imagen) Python SDK. En su lugar, seleccionas entre variantes de modelos (cada una con resoluciones predeterminadas implícitas), controlas la **relación de aspecto** y—si necesitas un recuento de píxeles mayor—aplicas un **realce de resolución (upscale)**. También puedes ajustar la **compresión** y el **formato de salida**, además de la configuración habitual de "número de imágenes", "indicación negativa (negative prompt)", "seguridad (safety)" y "persona".

## Variantes de Modelo

Seleccionas un nombre de modelo—cada variante tiene su propia resolución predeterminada y perfil de rendimiento:

* Familia **imagen-3.0**:

  * `imagen-3.0-generate-002`
  * `imagen-3.0-generate-001`
  * `imagen-3.0-fast-generate-001`
  * `imagen-3.0-capability-001`
* Familia **imagen-4.0 (Vista previa)**:

  * `imagen-4.0-generate-preview-06-06`
  * `imagen-4.0-fast-generate-preview-06-06`
  * `imagen-4.0-ultra-generate-preview-06-06`
* **Legado**: `imagegeneration@002`, `@005`, `@006` ([Google Cloud][1])

## Resolución Predeterminada

Por defecto, una salida cuadrada ("1:1") de estos modelos es de **1024 × 1024 píxeles**. Si necesitas un archivo más pequeño, puedes reducir la resolución localmente; si necesitas una resolución mayor, consulta **Realce de resolución (Upscaling)** más abajo. ([raymondcamden.com][2])

## Relaciones de Aspecto

En lugar de especificar dimensiones absolutas, utiliza el campo `aspect_ratio` en tu `GenerateImagesConfig`. Valores admitidos:

* `1:1` (cuadrado)
* `3:4` (vertical, retrato para redes sociales)
* `4:3` (fotografía/televisión clásica)
* `16:9` (paisajes panorámicos)
* `9:16` (vertical/retrato, ej. fondos de pantalla de teléfono) ([Google Cloud][1], [Google AI for Developers][3])

Encontrarás la misma lista documentada en tutoriales de la comunidad:

* DataCamp señala exactamente esas cinco proporciones para Imagen 3 ([DataCamp][4])
* La guía de CodeSignal también las enumera para Gemini/Imagen ([CodeSignal][5])

## Realce de Resolución (Upscaling)

Si necesitas salidas verdaderamente "2K" o "4K", llama al modo **upscale**:

```python
from google.genai import types
config = types.GenerateImagesConfig(
    mode="upscale",
    upscale_config=types.UpscaleConfig(upscale_factor="x2"),
)
```

* `"x2"` duplica cada dimensión (ej. 1024 → 2048, aproximadamente 2K)
* `"x4"` cuadruplica (ej. 1024 → 4096, aproximadamente 4K) ([Google Cloud][1])

## Compresión y Formatos

* **Calidad JPEG**: usa `compression_quality` (0–100, predeterminado 75) para equilibrar el tamaño del archivo frente al detalle ([Google Cloud][1])
* **Tipos MIME**: a través de `output_options.mime_type`, puedes elegir
  `image/jpeg`, `image/png`, `image/gif`, `image/webp`, `image/bmp`, `image/tiff`, o `image/vnd.microsoft.icon` ([Google Cloud][6])

## Opciones de Configuración Adicionales

Todo lo demás se encuentra en `GenerateImagesConfig`:

```python
config = types.GenerateImagesConfig(
    number_of_images=1,           # cuántas imágenes generar
    seed=1234,                    # para salidas deterministas
    enhance_prompt=True,          # reescritura de indicación basada en LLM
    negative_prompt="exclude dogs",
    language="en",
    safety_filter_level="block_medium_and_above",  
    person_generation="allow_adult",
)
```

Estos te permiten controlar la aleatoriedad, la mejora de la indicación, los umbrales de seguridad y si el modelo puede incluir personas. ([Google Cloud][1])

## Recomendación

Elimina tu línea `image_size="2K"`—no existe tal parámetro. En su lugar:

1. **Elige el modelo correcto** para velocidad vs. calidad.
2. Usa **`aspect_ratio`** para el encuadre.
3. Si realmente necesitas más píxeles, genera en la resolución base y luego aplica el **realce de resolución (upscale)** integrado ("x2" o "x4").
4. Ajusta **compression\_quality** o reduce la resolución localmente para archivos más pequeños.

Con estos controles puedes lograr encuadres cuadrados o cinemáticos, salidas pequeñas o de alta resolución, sin un parámetro `image_size` no compatible.

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api "Generate images  |  Generative AI on Vertex AI  |  Google Cloud"
[2]: https://www.raymondcamden.com/2025/01/30/generative-ai-images-with-gemini-and-imagen-an-introduction?utm_source=chatgpt.com "Generative AI Images with Gemini and Imagen"
[3]: https://ai.google.dev/gemini-api/docs/imagen?utm_source=chatgpt.com "Generate images using Imagen | Gemini API | Google AI for ..."
[4]: https://www.datacamp.com/tutorial/imagen-3 "Imagen 3: A Guide With Examples in the Gemini API | DataCamp"
[5]: https://codesignal.com/learn/courses/creating-images-with-geminis-imagen-and-flask/lessons/generating-a-simple-image-with-geminis-imagen-and-flask?utm_source=chatgpt.com "Generating a Simple Image with Gemini's Imagen and Flask"
[6]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images?utm_source=chatgpt.com "Generate images using text prompts"