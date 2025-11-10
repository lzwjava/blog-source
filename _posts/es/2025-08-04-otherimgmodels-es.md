---
audio: false
generated: true
image: false
lang: es
layout: post
title: Otros Modelos de Imagen en Vertex AI
translated: true
type: note
---

Si bien Imagen es la familia principal de modelos de generación de imágenes de Google en Vertex AI, existen otras opciones disponibles, especialmente si buscas capacidades diferentes o alternativas de código abierto.

Aquí tienes un desglose de otros modelos relacionados con imágenes que puedes usar en Vertex AI:

### Modelos Gemini (para casos de uso multimodales)
La familia de modelos Gemini es multimodal, lo que significa que pueden procesar y comprender múltiples tipos de datos, incluidos texto, imágenes, video y audio. Si bien son conocidos principalmente por sus salidas basadas en texto, algunos modelos Gemini tienen funciones específicas para tareas relacionadas con imágenes. Por ejemplo, algunos modelos Gemini pueden:
*   **Generar imágenes** a partir de un prompt de texto.
*   **Editar imágenes** usando instrucciones conversacionales.
*   **Realizar preguntas y respuestas visuales (VQA)**, donde puedes hacer una pregunta sobre una imagen y recibir una respuesta basada en texto.
*   **Generar descripciones** para una imagen dada (subtítulos de imágenes).

Esta es una gran opción si estás construyendo una aplicación que necesita manejar tanto texto como imágenes de manera conversacional o integrada, en lugar de solo generar una imagen a partir de un prompt simple.

### Modelos de Código Abierto de Model Garden
**Model Garden** de Vertex AI es un centro centralizado donde puedes descubrir, probar, personalizar e implementar una amplia gama de modelos, incluidos tanto los modelos propietarios de Google como una selección curada de modelos de código abierto. Aquí es donde encontrarás alternativas a Imagen, tales como:

*   **Llama 3-Vision**: Una familia de modelos multimodales optimizados para reconocimiento visual, razonamiento sobre imágenes y generación de subtítulos.
*   **Flux**: Un modelo de transformador de flujo rectificado que genera imágenes de alta calidad a partir de descripciones de texto.
*   **Instant ID**: Un modelo de generación de texto a imagen que preserva la identidad. Esto es útil para generar nuevas imágenes de una persona o sujeto específico manteniendo sus características clave de identidad.

Estos modelos de código abierto a menudo vienen con diferentes términos de licencia, características de rendimiento y opciones de personalización, lo que te brinda más flexibilidad para casos de uso específicos.

### Otros Modelos Relacionados con la Visión
Más allá de la generación de imágenes, Vertex AI ofrece modelos preentrenados para una variedad de tareas de visión, que podrían resultarte útiles:

*   **Multimodal Embeddings**: Genera representaciones vectoriales de imágenes, que puedes usar para tareas como búsqueda de imágenes (encontrar imágenes similares), clasificación o agrupación.
*   **Vertex AI AutoML Image**: Te permite entrenar tus propios modelos de machine learning personalizados para clasificación de imágenes, detección de objetos y segmentación de imágenes sin escribir código.
*   **Modelos de video (Veo)**: Aunque no es un modelo de imágenes, Veo te permite generar videos de alta calidad a partir de prompts de texto o imágenes. Es una herramienta poderosa para la creación de medios que va más allá de las imágenes fijas.