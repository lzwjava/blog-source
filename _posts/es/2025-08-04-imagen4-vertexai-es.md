---
audio: false
generated: true
image: false
lang: es
layout: post
title: Modelos Imagen 4 de Vertex AI
translated: true
type: note
---

Basándote en el fragmento de código que proporcionaste, estás usando `genai.Client` para interactuar con un modelo de generación de imágenes en Vertex AI. El modelo que has especificado es `"imagen-4.0-generate-preview-06-06"`.

Aquí tienes un desglose de lo que es nuevo y lo que representa este modelo:

### Los Últimos Modelos de Generación de Imágenes en Vertex AI

El modelo que estás usando, `imagen-4.0-generate-preview-06-06`, es parte de la última familia de modelos **Imagen 4** en Vertex AI. Esta familia de modelos también incluye:

*   **`imagen-4.0-generate-preview-06-06`**: Este es el modelo estándar de Imagen 4, que ofrece un equilibrio entre velocidad y calidad.
*   **`imagen-4.0-ultra-generate-preview-06-06`**: Esta versión "Ultra" está diseñada para una mayor calidad, pero es más lenta y costosa.
*   **`imagen-4.0-fast-generate-preview-06-06`**: Esta variante "Fast" prioriza la velocidad y una menor latencia sobre la máxima calidad posible.

Estos modelos de Imagen 4 son una actualización significativa, que se basa en versiones anteriores como Imagen 3 e Imagen 2. Las características clave y las actualizaciones de Imagen 4 incluyen:

*   **Calidad de Imagen Mejorada**: Los nuevos modelos están diseñados para generar imágenes con una calidad superior en comparación con sus predecesores.
*   **Soporte para Más Relaciones de Aspecto**: Imagen 4 admite varias relaciones de aspecto, incluyendo `1:1`, `3:4`, `4:3`, `9:16` y `16:9`, dándote más control sobre el resultado.
*   **Indicaciones Multilingües**: Aunque el inglés es el idioma principal, estos modelos también admiten indicaciones de texto en varios otros idiomas, incluyendo chino (simplificado y tradicional), hindi, japonés, coreano, portugués y español (en vista previa).
*   **Características de Seguridad**: Los modelos incluyen configuraciones de seguridad ajustables por el usuario e incorporan marcas de agua digitales (SynthID) para identificar contenido generado por IA.

Los parámetros `person_generation` y `safety_filter_level` en tu fragmento de código siguen siendo relevantes y te permiten configurar el comportamiento del modelo para una IA responsable, como has hecho con `person_generation="ALLOW_ADULT"` y `safety_filter_level="BLOCK_LOW_AND_ABOVE"`.

### Más Allá de la Generación de Imágenes

Además de los modelos actualizados de Imagen, Google Cloud también ha introducido recientemente otros nuevos modelos de IA generativa en Vertex AI, incluyendo:

*   **Veo 3 y Veo 3 Fast**: Estos son los últimos modelos de generación de video, que te permiten crear videos de alta calidad a partir de indicaciones de texto o imagen. Veo 3 es para videos profesionales de alta calidad con características como audio nativo y sincronización de labios, mientras que Veo 3 Fast está optimizado para la velocidad.
*   **Modelos Gemini 2.5**: Estas son las últimas versiones de la familia de modelos Gemini, incluyendo Gemini 2.5 Pro, Gemini 2.5 Flash y Gemini 2.5 Flash-Lite, que ofrecen razonamiento avanzado, multimodalidad y un rendimiento mejorado para diversas tareas.