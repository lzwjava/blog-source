---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía Preliminar de Google Imagen 4
translated: true
type: note
---

Para usar Google Imagen 4 Preview 0606, necesitas acceder a través de la plataforma Vertex AI de Google, ya que es una oferta de vista previa de Generative AI diseñada para la generación de texto a imagen. A continuación, se presenta una guía paso a paso basada en la información disponible:

### Cómo usar Google Imagen 4 Preview 0606

1. **Acceder a Vertex AI**:
   - **Plataforma**: Imagen 4 Preview 0606 está disponible en Vertex AI de Google Cloud. Necesitarás una cuenta de Google Cloud para comenzar.
   - **Registrarse**: Si no tienes una cuenta, regístrate en [cloud.google.com](https://cloud.google.com) y configura un proyecto. Asegúrate de que la facturación esté habilitada, ya que esta es una oferta de vista previa con costos potenciales (los detalles de precios están disponibles en la sección de Imagen de la página de precios de Vertex AI).[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)
   - **Navegar a Vertex AI**: Una vez que hayas iniciado sesión, ve a la sección de Vertex AI en Google Cloud Console y localiza las herramientas de Generative AI.

2. **Configurar el entorno**:
   - **Autenticación**: Autentica tu cuenta usando las credenciales de Google Cloud. Puedes generar un token de acceso usando el comando:
     ```bash
     gcloud auth print-access-token
     ```
   - **Proyecto y Ubicación**: Establece tu ID de proyecto de Google Cloud y la ubicación (ej., `us-central1`). Ejemplo:
     ```bash
     export GOOGLE_CLOUD_PROJECT=tu-id-de-proyecto
     export GOOGLE_CLOUD_LOCATION=us-central1
     ```

3. **Usar el modelo Imagen 4**:
   - **Acceso API**: Imagen 4 Preview 0606 se puede acceder a través de la API de Vertex AI. Usa el endpoint del modelo `imagen-4.0-generate-preview-06-06`. Puedes interactuar con él mediante programación usando herramientas como cURL o el Google Gen AI SDK para Python.
   - **Ejemplo de Solicitud cURL**:
     ```bash
     curl -X POST \
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \
     -H "Content-Type: application/json; charset=utf-8" \
     "https://${GOOGLE_CLOUD_LOCATION}-aiplatform.googleapis.com/v1/projects/${GOOGLE_CLOUD_PROJECT}/locations/${GOOGLE_CLOUD_LOCATION}/publishers/google/models/imagen-4.0-generate-preview-06-06:predict" \
     -d '{"instances": [{"prompt": "Un gato leyendo un libro"}], "parameters": {"sampleCount": 1}}'
     ```
     Esto devuelve una imagen codificada en base64.[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)
   - **Ejemplo con Python SDK**:
     ```python
     from google import genai
     from google.genai.types import GenerateImagesConfig
     client = genai.Client()
     image = client.models.generate_images(
         model="imagen-4.0-generate-preview-06-06",
         prompt="Un perro leyendo un periódico",
         config=GenerateImagesConfig(image_size="2K")
     )
     image.generated_images[0].image.save("imagen-salida.png")
     print(f"Imagen de salida creada usando {len(image.generated_images[0].image.image_bytes)} bytes")
     ```
     Esto genera una imagen y la guarda como un archivo PNG.[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)

4. **Crear Prompts Efectivos**:
   - **Estructura del Prompt**: Para obtener los mejores resultados, usa prompts detallados y específicos. Incluye el sujeto, el entorno, el estilo artístico (ej., fotorrealista, abstracto), el estado de ánimo y los elementos compositivos (ej., ángulo de cámara). Ejemplo: “Una ilustración gráfica vibrante de una ciudad futurista al atardecer, estilo cyberpunk, con luces de neón y una perspectiva dramática desde un ángulo bajo.”
   - **Consejos**:
     - Sé preciso: Los prompts vagos pueden llevar a resultados impredecibles.
     - Evita entradas sin sentido (ej., emojis aleatorios), ya que pueden producir salidas inconsistentes.
     - Especifica texto si es necesario, ya que Imagen 4 tiene una renderización de tipografía mejorada.[](https://deepmind.google/models/imagen/)[](https://replicate.com/blog/google-imagen-4)
   - **Prompts Negativos**: Puedes usar un prompt negativo para excluir elementos no deseados (ej., “sin texto” si no quieres texto en la imagen).[](https://docs.aimlapi.com/api-references/image-models/google/imagen-4-preview)

5. **Explorar Variantes**:
   - Imagen 4 Preview 0606 tiene variantes como **Fast** (hasta 10x más rápido, optimizado para generación masiva) y **Ultra** (mayor alineación con los prompts para uso profesional). Verifica si estas están disponibles en tu interfaz de Vertex AI y elige según tus necesidades (ej., Fast para prototipado rápido, Ultra para salidas de alta calidad).[](https://fal.ai/models/fal-ai/imagen4/preview)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)

6. **Revisar la Salida y las Características de Seguridad**:
   - **Formatos de Salida**: Las imágenes se generan en formatos estándar como PNG o JPEG, con una resolución de hasta 2K.[](https://fal.ai/models/fal-ai/imagen4/preview)
   - **Marca de Agua SynthID**: Todas las imágenes incluyen una marca de agua digital invisible para identificarlas como generadas por IA, garantizando transparencia.[](https://deepmind.google/models/imagen/)[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)
   - **Restricciones de Contenido**: Imagen 4 usa filtrado para minimizar contenido dañino, pero puede tener dificultades con composiciones complejas, caras pequeñas o imágenes centradas perfectamente. Revisa las pautas de uso de Google para las restricciones de contenido.[](https://deepmind.google/models/imagen/)[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)

7. **Plataformas Alternativas**:
   - Imagen 4 también está disponible en plataformas de terceros como Replicate, fal.ai, o AI/ML API, que pueden ofrecer interfaces más simples o entornos sandbox para pruebas. Por ejemplo:
     - **Replicate**: Ejecuta Imagen 4 con un prompt como “Un paisaje de montaña sereno al atardecer, estilo hiperrealista.” Consulta la documentación de Replicate para las claves API y el uso.[](https://replicate.com/blog/google-imagen-4)[](https://replicate.com/google/imagen-4-fast)
     - **fal.ai**: Usa su API con una solicitud como:
       ```javascript
       const result = await fal.subscribe("fal-ai/imagen4/preview", {
           input: { prompt: "Un paisaje de montaña sereno al atardecer, estilo hiperrealista" }
       });
       console.log(result.images[0].url);
       ```
       Los precios varían (ej., $0.05/imagen para Standard, $0.04 para Fast, $0.06 para Ultra).[](https://fal.ai/models/fal-ai/imagen4/preview)
   - **App Gemini o Google Workspace**: Imagen 4 está integrado en la app Gemini, Google Slides, Docs y Vids para la generación directa de imágenes en flujos de trabajo. Por ejemplo, en Google Docs, puedes generar imágenes para ilustrar documentos.[](https://www.stablediffusion.blog/imagen4)

8. **Probar e Iterar**:
   - Experimenta con prompts en un entorno sandbox (ej., Google AI Studio para pruebas gratuitas limitadas) antes de integrar en producción.[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)
   - Monitorea el uso de la API y los costos a través del panel de control de la plataforma, ya que las ofertas de vista previa pueden tener soporte limitado o características cambiantes.[](https://fal.ai/models/fal-ai/imagen4/preview)

### Notas Adicionales
- **Precios**: Consulta la página de precios de Vertex AI para los costos de Imagen 4 (ej., $0.04/imagen para Standard, $0.06/imagen para Ultra).[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)[](https://fal.ai/models/fal-ai/imagen4/preview)
- **Limitaciones**: Imagen 4 puede tener dificultades con prompts vagos, caras pequeñas o composiciones perfectamente centradas. Usa prompts claros y estructurados para obtener los mejores resultados.[](https://deepmind.google/models/imagen/)
- **Disponibilidad**: Como oferta de vista previa, las características y el soporte pueden cambiar. Consulta las descripciones de la etapa de lanzamiento de Google Cloud para obtener actualizaciones.[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)

Para documentación detallada, visita la [página de Vertex AI Imagen](https://cloud.google.com/vertex-ai/docs/generative-ai/image/overview) o el [Blog de Google Developers](https://developers.googleblog.com). Para acceso API, consulta [x.ai/api](https://x.ai/api) para orientación general sobre la API de IA, aunque los detalles específicos de Imagen 4 están en Google Cloud.[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)

Si necesitas ayuda con una plataforma o caso de uso específico, ¡avísame!