---
audio: false
generated: true
lang: es
layout: post
title: Script de Word2Vec con Gensim
translated: true
type: note
---

Para proporcionarte un script de Python para Word2Vec, necesito hacer un par de suposiciones sobre lo que buscas, ya que "un script sobre Word2Vec" puede ser bastante amplio. Proporcionaré dos escenarios comunes:

1.  **Un script simple usando `gensim` para entrenamiento y uso básico:** Esta es la forma más común y práctica de usar Word2Vec en Python.
2.  **Una implementación conceptual muy básica desde cero:** Esto es más para comprender los algoritmos centrales, pero menos práctico para uso en el mundo real debido a la complejidad y la optimización.

Dada tu solicitud, priorizaré el enfoque con `gensim` ya que es lo que la mayoría de la gente usaría.

-----

### Script de Python para Word2Vec usando `gensim`

Este script demostrará:

  * Preparar datos de texto de ejemplo.
  * Entrenar un modelo Word2Vec.
  * Encontrar palabras más similares.
  * Realizar analogías de palabras.
  * Guardar y cargar el modelo.

**Prerrequisitos:**

Necesitarás instalar la librería `gensim`:

```bash
pip install gensim
```

**Script de Python (`word2vec_gensim_example.py`):**

```python
import gensim
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import logging

# Configurar logging para ver el progreso del entrenamiento
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# --- 1. Preparar Datos de Texto de Ejemplo ---
# En un escenario real, cargarías tus datos de texto desde archivos.
# Aquí, usamos una simple lista de oraciones.
raw_sentences = [
    "I love natural language processing.",
    "Word embeddings are a fascinating topic.",
    "Machine learning revolutionizes many industries.",
    "Deep learning is a subset of machine learning.",
    "Natural language processing uses various techniques.",
    "Computers understand human language better with word vectors.",
    "The quick brown fox jumps over the lazy dog.",
    "Dog and cat are common pets.",
    "King is to Queen as Man is to Woman."
]

# Preprocesar las oraciones: tokenizar y convertir a minúsculas
# simple_preprocess de gensim es conveniente para esto
tokenized_sentences = [simple_preprocess(sentence) for sentence in raw_sentences]

print("\n--- Oraciones Tokenizadas ---")
for sentence in tokenized_sentences:
    print(sentence)

# --- 2. Entrenar el Modelo Word2Vec ---
# Parámetros explicados:
#   vector_size: Dimensionalidad de los vectores de palabras.
#   window: Distancia máxima entre la palabra actual y la palabra predicha dentro de una oración.
#   min_count: Ignora todas las palabras con una frecuencia total inferior a este valor.
#   sg: Algoritmo de entrenamiento: 0 para CBOW, 1 para Skip-gram. Skip-gram es generalmente mejor para palabras raras.
#   workers: Usa esta cantidad de hilos de trabajo para entrenar el modelo (=entrenamiento más rápido).
#   epochs: Número de iteraciones (épocas) sobre el corpus.
model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=100,      # Ejemplo: vectores de 100 dimensiones
    window=5,             # Ventana de contexto de 5 palabras a cada lado
    min_count=1,          # Incluir todas las palabras (para este pequeño ejemplo)
    sg=1,                 # Usar Skip-gram (sg=1)
    workers=4,            # Usar 4 núcleos de CPU para el entrenamiento
    epochs=10             # Entrenar durante 10 épocas
)

print("\n--- Entrenamiento del Modelo Completado ---")

# --- 3. Explorar el Modelo ---

# Obtener el vector para una palabra específica
try:
    word_vector = model.wv['machine']
    print(f"\nVector para 'machine' (primeras 10 dimensiones): {word_vector[:10]}")
    print(f"Vector para 'machine' forma: {word_vector.shape}")
except KeyError:
    print("\n'machine' no encontrada en el vocabulario.")

# Encontrar las palabras más similares
print("\n--- Palabras Más Similares a 'machine' ---")
try:
    similar_words = model.wv.most_similar('machine')
    for word, similarity in similar_words:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n'machine' no encontrada en el vocabulario.")

print("\n--- Palabras Más Similares a 'dog' ---")
try:
    similar_words_dog = model.wv.most_similar('dog')
    for word, similarity in similar_words_dog:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n'dog' no encontrada en el vocabulario.")


# Realizar analogías de palabras (ej., King - Man + Woman = Queen)
# Esto puede no funcionar perfectamente con conjuntos de datos muy pequeños, pero demuestra el concepto.
print("\n--- Analogías de Palabras (King - Man + Woman = ?) ---")
try:
    result = model.wv.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
    if result:
        print(f"King - Man + Woman es similar a: {result[0][0]} (similitud: {result[0][1]:.4f})")
    else:
        print("No hay resultado para la analogía. El vocabulario podría ser demasiado pequeño.")
except KeyError as e:
    print(f"Una o más palabras para la analogía no encontradas en el vocabulario: {e}")
except Exception as e:
    print(f"Ocurrió un error durante la analogía: {e}")

# Verificar la similitud entre dos palabras
print("\n--- Similitud entre 'machine' y 'learning' ---")
try:
    similarity = model.wv.similarity('machine', 'learning')
    print(f"Similitud: {similarity:.4f}")
except KeyError:
    print("Una o ambas palabras no encontradas en el vocabulario.")

print("\n--- Similitud entre 'dog' y 'cat' ---")
try:
    similarity_pets = model.wv.similarity('dog', 'cat')
    print(f"Similitud: {similarity_pets:.4f}")
except KeyError:
    print("Una o ambas palabras no encontradas en el vocabulario.")

print("\n--- Similitud entre 'dog' y 'computer' ---")
try:
    similarity_diff = model.wv.similarity('dog', 'computer')
    print(f"Similitud: {similarity_diff:.4f}")
except KeyError:
    print("Una o ambas palabras no encontradas en el vocabulario.")

# --- 4. Guardar y Cargar el Modelo ---
model_path = "word2vec_model.bin"
model.save(model_path)
print(f"\nModelo guardado en {model_path}")

# Cargar el modelo de nuevo
loaded_model = Word2Vec.load(model_path)
print(f"Modelo cargado desde {model_path}")

# Verificar el modelo cargado
print("\n--- Verificar Modelo Cargado (Palabras Más Similares a 'machine' usando el modelo cargado) ---")
try:
    similar_words_loaded = loaded_model.wv.most_similar('machine')
    for word, similarity in similar_words_loaded:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n'machine' no encontrada en el vocabulario en el modelo cargado.")

print("\nEjecución del script completada.")
```

**Cómo Ejecutar el Script:**

1.  Guarda el código anterior como un archivo de Python (ej., `word2vec_gensim_example.py`).
2.  Abre tu terminal o símbolo del sistema.
3.  Navega al directorio donde guardaste el archivo.
4.  Ejecuta el script usando: `python word2vec_gensim_example.py`

-----

### Conceptos Clave en Word2Vec (implementación de `gensim`)

  * **`gensim.models.Word2Vec`**: La clase principal para el entrenamiento.
  * **`sentences`**: Un iterable de iterables, donde el iterable externo es el corpus y los iterables internos son listas de palabras (oraciones tokenizadas).
  * **`vector_size`**: El número de dimensiones para los vectores de palabras. Dimensiones más altas pueden capturar más matices pero requieren más datos y computación.
  * **`window`**: La distancia máxima entre la palabra actual y las palabras a su alrededor en una oración.
  * **`min_count`**: Las palabras que aparecen menos veces que `min_count` son ignoradas. Esto ayuda a filtrar palabras muy raras que podrían no tener embeddings significativos.
  * **`sg` (Skip-gram vs. CBOW)**:
      * `sg=0` (CBOW - Continuous Bag of Words): Predice la palabra actual basándose en su contexto. Más rápido de entrenar.
      * `sg=1` (Skip-gram): Predice las palabras circundantes dada la palabra actual. Generalmente funciona mejor para palabras raras.
  * **`workers`**: Número de núcleos de CPU a usar para el entrenamiento, acelerando el proceso.
  * **`epochs`**: Número de veces que el algoritmo itera sobre todo el conjunto de datos. Más épocas pueden conducir a embeddings de mejor calidad pero también toman más tiempo.
  * **`model.wv`**: El objeto "vectores de palabras" (`KeyedVectors`) que contiene los embeddings de palabras entrenados y métodos como `most_similar`, `similarity`, etc. También puedes acceder a los vectores directamente como `model.wv['word']`.

-----

Este script de `gensim` proporciona una base sólida para trabajar con Word2Vec. Para aplicaciones del mundo real, normalmente usarías un corpus mucho más grande (ej., Wikipedia, Common Crawl) y ajustarías los hiperparámetros para un rendimiento óptimo.