---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Rendimiento y Eficiencia de DeepSeek OCR
translated: true
type: note
---

### ¿Es bueno DeepSeek OCR?

DeepSeek OCR es un modelo de lenguaje visual (VLM) recién lanzado de 3B parámetros de DeepSeek AI, lanzado el 20 de octubre de 2025, específicamente optimizado para el reconocimiento óptico de caracteres (OCR) y el procesamiento estructurado de documentos. Según las primeras evaluaciones y benchmarks, está mostrando un rendimiento sólido:

- **Eficiencia de compresión**: Utiliza "compresión de contexto óptico" para reducir los datos visuales a muchos menos tokens (por ejemplo, 100 tokens visuales en lugar de 1000+ tokens de texto para el mismo contenido), logrando ~97% de precisión en la decodificación con ratios de compresión de 10x y resultados casi sin pérdidas hasta 20x. Esto lo hace muy eficiente para manejar documentos grandes sin perder detalles clave.

- **Rendimiento**: En una sola GPU, puede procesar más de 200,000 páginas por día, lo que supone un salto significativo para aplicaciones del mundo real como la digitalización de archivos o la automatización de la extracción de formularios.

- **Rendimiento en benchmarks**: Supera a otros modelos de OCR de código abierto (por ejemplo, en tareas de comprensión de documentos) y iguala o se acerca a los líderes de código cerrado como GPT-4V en precisión para salidas estructuradas. Las primeras pruebas destacan su ventaja para manejar diseños complejos, tablas y texto multilingüe.

Dicho esto, es muy nuevo, por lo que la adopción en el mundo real está comenzando. Hay informes de desafíos de configuración para ejecuciones locales (por ejemplo, en Apple Silicon o configuraciones NVIDIA que requieren ajustes), pero una vez en funcionamiento, los usuarios lo describen como "bastante bueno" para uso experimental. En general, si te interesa un OCR eficiente y de alta precisión para documentos, es una opción sólida, especialmente como una opción de código abierto. Para OCR de imágenes generales (por ejemplo, memes o escritura a mano), aún podría necesitar ajustes finos en comparación con herramientas especializadas como Tesseract.

### ¿Qué es un Token Visual?

En los modelos de IA, particularmente en los modelos de lenguaje visual multimodal (VLM) como los de OpenAI, DeepSeek o LLaVA, un **token visual** es una representación numérica compacta de un pequeño fragmento de datos visuales. Aquí tienes un desglose:

- **Cómo funciona**: Las imágenes no se alimentan directamente a los modelos de lenguaje (que procesan texto). En su lugar, la imagen se divide en parches de tamaño fijo (por ejemplo, 14x14 píxeles). Cada parche se incrusta en un vector, un "token", similar a cómo las palabras se convierten en tokens en el texto. Estos tokens visuales capturan características como bordes, colores o texturas, permitiendo al modelo "entender" y razonar sobre la imagen junto con los tokens de texto.

- **Por qué es importante**: Esta tokenización permite un procesamiento eficiente. Por ejemplo, una imagen de 512x512 podría generar cientos de tokens visuales, pero técnicas avanzadas (como en DeepSeek OCR) los comprimen aún más para reducir los costes de computación preservando la precisión. Es clave para tareas como el subtitulado de imágenes, preguntas y respuestas visuales u OCR, donde el modelo combina información visual y textual.

- **Ejemplo**: En GPT-4V, una foto cargada se convierte en ~85 tokens visuales (redimensionada y dividida en parches), que el modelo trata como palabras de entrada para generar respuestas.

Los tokens visuales cierran la brecha entre los píxeles y el lenguaje, haciendo que la IA "vea" de una manera computacionalmente factible.

**Referencias**  
[DeepSeek Just Released a 3B OCR Model](https://www.marktechpost.com/2025/10/20/deepseek-just-released-a-3b-ocr-model-a-3b-vlm-designed-for-high-performance-ocr-and-structured-document-conversion/)  
[DeepSeek-OCR Isn't About OCR, It's About Token Compression](https://medium.com/@olimiemma/deepseek-ocr-isnt-about-ocr-it-s-about-token-compression-db1747602e29)  
[DeepSeek's New OCR Model Can Process Over 2 Lakh Pages Daily](https://analyticsindiamag.com/ai-news-updates/deepseeks-new-ocr-model-can-process-over-2-lakh-pages-daily-on-a-single-gpu/)  
[Token: AI & ML Definition](https://www.ultralytics.com/glossary/token)  
[Revolutionizing AI Vision: Visual Perception Tokens](https://kitemetric.com/blogs/revolutionizing-ai-vision-introducing-visual-perception-tokens)