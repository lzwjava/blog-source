---
audio: false
generated: true
lang: es
layout: post
title: Modelos de lenguaje multimodales
translated: true
type: note
---

Desglosemos esto paso a paso para explicar cómo funciona la implementación multimodal en los modelos de lenguaje grandes (LLM) y abordar tus preguntas sobre cómo las imágenes y el texto se convierten en vectores.

### LLM multimodales: Cómo funcionan
Un LLM multimodal está diseñado para procesar y generar respuestas basadas en múltiples tipos de datos, como texto, imágenes, audio o incluso datos estructurados como tablas. A diferencia de los LLM tradicionales que solo manejan texto, los modelos multimodales integran estas diferentes "modalidades" en un marco unificado. Así es como se implementa típicamente:

1.  **Codificadores separados para cada modalidad**:
    - **Texto**: El texto se procesa usando un tokenizador (por ejemplo, dividiéndolo en palabras o subpalabras) y luego se convierte en representaciones numéricas llamadas *embeddings* (vectores) usando un vocabulario o una capa de *embedding* preentrenada. Esto es estándar en modelos como BERT o GPT.
    - **Imágenes**: Las imágenes se procesan usando un modelo de visión, como una red neuronal convolucional (CNN) o un Vision Transformer (ViT). Estos modelos extraen características de la imagen (como bordes, formas u objetos) y las convierten en una representación vectorial en un espacio de alta dimensión.
    - Otras modalidades (por ejemplo, audio) siguen un proceso similar con codificadores especializados (por ejemplo, convirtiendo ondas sonoras en espectrogramas y luego en vectores).

2.  **Representación unificada**:
    - Una vez que cada modalidad está codificada en vectores, el modelo alinea estas representaciones para que puedan "comunicarse" entre sí. Esto puede implicar proyectarlas en un espacio de *embedding* compartido donde los vectores de texto y los vectores de imagen sean compatibles. Técnicas como los mecanismos de atención cruzada (tomados de los Transformers) ayudan al modelo a comprender las relaciones entre modalidades; por ejemplo, vincular la palabra "gato" en el texto con una imagen de un gato.

3.  **Entrenamiento**:
    - El modelo se entrena con conjuntos de datos que emparejan modalidades (por ejemplo, imágenes con subtítulos) para que aprenda a asociar descripciones de texto con características visuales. Esto podría implicar aprendizaje contrastivo (por ejemplo, CLIP) o entrenamiento conjunto donde el modelo predice texto a partir de imágenes o viceversa.

4.  **Generación de salida**:
    - Al generar una respuesta, el modelo utiliza su decodificador (o una arquitectura Transformer unificada) para producir texto, imágenes o ambos, dependiendo de la tarea. Por ejemplo, podría generar un subtítulo para una imagen o responder una pregunta sobre una imagen.

### ¿Una imagen también se cambia a un vector?
¡Sí, absolutamente! Al igual que el texto, las imágenes se convierten en vectores en los LLM multimodales:
-   **Cómo funciona**: Una imagen se introduce en un codificador de visión (por ejemplo, un ResNet o ViT preentrenado). Este codificador procesa los datos de píxeles en bruto y genera un vector de tamaño fijo (o una secuencia de vectores) que captura el contenido semántico de la imagen, como objetos, colores o patrones.
-   **Ejemplo**: Una foto de un perro podría transformarse en un vector de 512 dimensiones que codifique características "parecidas a un perro". Este vector no se parece a la imagen para nosotros, pero contiene información numérica que el modelo puede usar.
-   **Diferencia con el texto**: Mientras que los vectores de texto provienen de un vocabulario (por ejemplo, *embeddings* de palabras para "perro" o "gato"), los vectores de imagen provienen de características espaciales y visuales extraídas por el modelo de visión. Ambos terminan como números en un espacio vectorial.

### Texto a vectores: Construyendo un vocabulario
Mencionaste que el texto se cambia a vectores construyendo un vocabulario; así es como sucede:
-   **Tokenización**: El texto se divide en unidades más pequeñas (tokens), como palabras o subpalabras (por ejemplo, "playing" podría dividirse en "play" y "##ing" en modelos como BERT).
-   **Vocabulario**: Un vocabulario predefinido asigna cada token a un ID único. Por ejemplo, "perro" podría ser el ID 250 y "gato" el ID 300.
-   **Capa de Embedding**: Cada ID de token se convierte en un vector denso (por ejemplo, un vector de 768 dimensiones) usando una matriz de *embeddings*. Estos vectores se aprenden durante el entrenamiento para capturar el significado semántico; las palabras con significados similares (como "perro" y "cachorro") terminan con vectores similares.
-   **Contextualización**: En los LLM modernos, un Transformer luego refina estos vectores basándose en el contexto (por ejemplo, "banco" en "banco del río" vs. "banco de dinero" obtiene vectores diferentes).

### Similitud clave entre texto e imágenes
Tanto el texto como las imágenes están representados en última instancia como vectores en un espacio de alta dimensión. La magia de los modelos multimodales reside en alinear estos espacios para que el modelo pueda razonar a través de ellos. Por ejemplo:
-   Una imagen de un perro y la palabra "perro" podrían mapearse a puntos cercanos en este espacio compartido.
-   El modelo puede entonces responder preguntas como "¿Qué hay en esta imagen?" haciendo un puente entre el vector de imagen y los vectores de texto.

### Desafíos en la implementación multimodal
-   **Alineación**: Garantizar que los vectores de texto e imagen estén relacionados de manera significativa es complicado y requiere grandes conjuntos de datos emparejados.
-   **Cómputo**: Procesar imágenes junto con texto requiere muchos recursos en comparación con los modelos de solo texto.
-   **Interpretación**: El modelo necesita "entender" cuándo priorizar una modalidad sobre otra basándose en la entrada.

¿Aclara eso las cosas? Si quieres que profundice en alguna parte, como cómo funcionan los codificadores de visión o cómo se ve un espacio vectorial, ¡házmelo saber