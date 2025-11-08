---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Descripción General de Vision Transformer
translated: true
type: note
---

### Introducción a Vision Transformer (ViT)

Vision Transformer (ViT) es una arquitectura de red neuronal que adapta el modelo transformer—originalmente diseñado para procesamiento de lenguaje natural (NLP)—a tareas de visión por computadora, particularmente clasificación de imágenes. Introducido en 2020 por Alexey Dosovitskiy y sus colegas en Google en el artículo *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale*, ViT trata las imágenes como secuencias de parches en lugar de procesarlas con redes neuronales convolucionales (CNNs) tradicionales. Esto le permite aprovechar las fortalezas del transformer para manejar dependencias de largo alcance y computación paralela.

ViT ha demostrado un rendimiento competitivo o superior al de las CNNs en conjuntos de datos a gran escala como ImageNet, especialmente cuando se pre-entrena con cantidades masivas de datos (por ejemplo, JFT-300M). Variantes como DeiT (Data-efficient Image Transformers) lo hacen más eficiente para conjuntos de datos más pequeños. Hoy en día, los modelos inspirados en ViT impulsan muchas tareas de visión en modelos como DALL-E, Stable Diffusion y clasificadores modernos.

### Cómo funciona ViT: Arquitectura General y Flujo de Trabajo

La idea central de ViT es "tokenizar" una imagen en una secuencia de parches de tamaño fijo, similar a cómo el texto se divide en palabras o tokens. Esta secuencia luego es procesada por un codificador transformer estándar (sin decodificador, a diferencia de los modelos de texto generativos). Aquí hay un desglose paso a paso de cómo funciona:

1.  **Preprocesamiento de Imagen y Extracción de Parches**:
    *   Comienza con una imagen de entrada de tamaño \\(H \times W \times C\\) (altura × ancho × canales, por ejemplo, 224 × 224 × 3 para RGB).
    *   Divide la imagen en parches no superpuestos de tamaño fijo \\(P \times P\\) (por ejemplo, 16 × 16 píxeles). Esto produce \\(N = \frac{HW}{P^2}\\) parches (por ejemplo, 196 parches para una imagen de 224×224 con parches de 16×16).
    *   Cada parche se aplana en un vector 1D de longitud \\(P^2 \cdot C\\) (por ejemplo, 768 dimensiones para 16×16×3).
    *   ¿Por qué parches? Los píxeles en bruto crearían una secuencia imprácticamente larga (por ejemplo, millones para una imagen de alta resolución), por lo que los parches actúan como "palabras visuales" para reducir la dimensionalidad.

2.  **Incrustación de Parches (Patch Embedding)**:
    *   Aplica una proyección lineal entrenable (una simple capa totalmente conectada) a cada vector de parche aplanado, mapeándolo a una dimensión de incrustación fija \\(D\\) (por ejemplo, 768, igualando transformers del tipo BERT).
    *   Esto produce \\(N\\) vectores de incrustación, cada uno de tamaño \\(D\\).
    *   Opcionalmente, añade una incrustación de token [CLS] especial (un vector entrenable de tamaño \\(D\\)) antepuesto a la secuencia, similar a BERT para tareas de clasificación.

3.  **Incrustaciones Posicionales (Positional Embeddings)**:
    *   Añade incrustaciones posicionales 1D entrenables a las incrustaciones de parches para codificar información espacial (los transformers son invariantes a permutaciones sin esto).
    *   La secuencia de entrada completa es ahora: \\([ \text{[CLS]}, \text{parche}_1, \text{parche}_2, \dots, \text{parche}_N ] + \text{posiciones}\\), una matriz de forma \\((N+1) \times D\\).

4.  **Bloques del Codificador Transformer**:
    *   Alimenta la secuencia en \\(L\\) capas de codificador transformer apiladas (por ejemplo, 12 capas).
    *   Cada capa consiste en:
        *   **Autoatención Multi-Cabeza (MSA)**: Calcula puntuaciones de atención entre todos los pares de parches (incluyendo [CLS]). Esto permite al modelo capturar relaciones globales, como "esta oreja del gato se relaciona con el bigote a 100 parches de distancia", a diferencia de los campos receptivos locales de las CNNs.
            *   Fórmula: Atención(Q, K, V) = \\(\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V\\), donde Q, K, V son proyecciones de la entrada.
        *   **Perceptrón Multicapa (MLP)**: Una red de alimentación hacia adelante (dos capas lineales con activación GELU) aplicada posición por posición.
        *   Normalización de capa y conexiones residuales: Entrada + MSA → Norm → MLP → Norm + Entrada.
    *   Salida: Una secuencia de incrustaciones refinadas, todavía de forma \\((N+1) \times D\\).

5.  **Cabeza de Clasificación**:
    *   Para clasificación de imágenes, extrae la salida del token [CLS] (o toma la media de todas las incrustaciones de parches).
    *   Pásala a través de una cabeza MLP simple (por ejemplo, una o dos capas lineales) para generar los logits de clase.
    *   Durante el entrenamiento, se usa la pérdida de entropía cruzada en datos etiquetados. El pre-entrenamiento a menudo implica predicción de parches enmascarados u otras tareas auto-supervisadas.

**Hiperparámetros Clave** (del modelo original ViT-Base):
*   Tamaño de parche \\(P\\): 16
*   Dimensión de incrustación \\(D\\): 768
*   Capas \\(L\\): 12
*   Cabezas: 12
*   Parámetros: ~86M

ViT escala bien: Modelos más grandes (por ejemplo, ViT-Large con \\(D=1024\\), \\(L=24\\)) funcionan mejor pero necesitan más datos/computación.

**Entrenamiento e Inferencia**:
*   **Entrenamiento**: De extremo a extremo en datos etiquetados; se beneficia enormemente del pre-entrenamiento en miles de millones de imágenes.
*   **Inferencia**: Paso hacia adelante a través del codificador (~O(N²) en tiempo debido a la atención, pero eficiente con optimizaciones como FlashAttention).
*   A diferencia de las CNNs, ViT no tiene sesgos inductivos como la invariancia traslacional: todo se aprende.

### Comparación con Transformers de Texto: Similitudes y Diferencias

ViT es fundamentalmente la *misma arquitectura* que la parte del codificador de los transformers de texto (por ejemplo, BERT), pero adaptada para datos visuales 2D. Aquí hay una comparación lado a lado:

| Aspecto              | Transformer de Texto (ej. BERT)                  | Vision Transformer (ViT)                       |
|---------------------|------------------------------------------------|------------------------------------------------|
| **Representación de Entrada** | Secuencia de tokens (palabras/subpalabras) incrustadas en vectores. | Secuencia de parches de imagen incrustados en vectores. Los parches son como "tokens visuales". |
| **Longitud de Secuencia** | Variable (ej. 512 tokens para una oración).   | Fija según el tamaño de imagen/tamaño de parche (ej. 197 con [CLS]). |
| **Codificación Posicional** | 1D (absoluta o relativa) para el orden de palabras.     | 1D (entrenable) para el orden de parches (ej. aplanamiento fila-principal). Sin estructura 2D incorporada. |
| **Mecanismo Central**  | Autoatención sobre tokens para modelar dependencias. | Autoatención sobre parches—la misma matemática, pero atiende a "relaciones" espaciales en lugar de sintácticas. |
| **Salida/Tareas**    | Codificador para clasificación/LM Enmascarado; decodificador para generación. | Solo codificador para clasificación; puede extenderse para detección/segmentación. |
| **Fortalezas**       | Maneja dependencias de largo alcance en texto.         | Contexto global en imágenes (ej. comprensión de escena completa). |
| **Debilidades**      | Necesita corpus de texto enormes.                      | Requiere muchos datos; tiene dificultades en conjuntos de datos pequeños sin pre-entrenamiento con CNN. |
| **Estilo de Predicción**| Predicción del siguiente token en decodificadores (autoregresivo). | No hay predicción del "siguiente" inherentemente—clasifica toda la imagen de manera holística. |

En esencia, ViT es un intercambio "plug-and-play": Reemplaza las incrustaciones de tokens con incrustaciones de parches, y obtienes un modelo de visión. Ambos dependen de la atención para ponderar las relaciones en una secuencia, pero el texto es inherentemente secuencial/lineal, mientras que las imágenes son espaciales (ViT aprende esto a través de la atención).

### Abordando "Siguiente Token" vs. "Siguiente Pixel" en ViT

No, ViT *no* predice el "siguiente píxel" como un transformer de texto predice el "siguiente token" en generación autoregresiva (por ejemplo, GPT). He aquí por qué:

*   **Transformers de Texto (Autoregresivos)**: En modelos como GPT, el decodificador genera secuencialmente—un token a la vez, condicionando a todos los anteriores. Es píxel por píxel para imágenes en algunos modelos generativos (por ejemplo, PixelRNN), pero ineficiente.

*   **Enfoque de ViT**: ViT es *no autoregresivo* y holístico. Procesa la imagen *completa* (todos los parches) en paralelo a través del codificador. No hay predicción secuencial del "siguiente" durante la inferencia—la atención calcula las relaciones entre *todos* los parches simultáneamente. Para tareas de generación (por ejemplo, inpainting), las variantes de ViT podrían usar un decodificador para predecir parches enmascarados de manera autoregresiva, pero el ViT base es para clasificación, no para generación.

*   **¿Por qué no Píxeles?** Tratar píxeles individuales como tokens explotaría la longitud de la secuencia (por ejemplo, 224×224×3 = ~150K tokens), haciendo que la atención cuadrática sea computacionalmente inviable (O(N²) = billones de operaciones). Los parches agrupan ~256 píxeles (16×16) en un "token", manteniendo N manejable (~200).

Si deseas visión generativa (como siguiente-píxel o siguiente-parche), busca modelos como VQ-VAE + Transformer o Parti, que se basan en ideas de ViT.

Para más detalles, consulta el artículo original: [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929). ¡Si deseas ejemplos de código (por ejemplo, en PyTorch) o comparaciones con variantes específicas, házmelo saber