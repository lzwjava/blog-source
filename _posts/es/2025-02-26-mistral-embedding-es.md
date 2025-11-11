---
audio: false
generated: true
lang: es
layout: post
title: Incrustaciones de Mistral IA
translated: true
type: note
---

Para proporcionar ejemplos de embedding usando Mistral AI, puedes aprovechar su API de embeddings para generar representaciones numéricas (embeddings) de texto que capturan el significado semántico. Estos embeddings son útiles para tareas como detección de similitud, agrupamiento, clasificación o búsqueda. A continuación, demostraré cómo generar embeddings para un conjunto de oraciones y calcular sus similitudes usando el endpoint de embeddings de Mistral AI. Este ejemplo se basa en la estructura del código proporcionado pero lo adapta específicamente para embeddings, como se describe en la documentación: [Mistral AI Embeddings](https://docs.mistral.ai/capabilities/embeddings/).

### Prerrequisitos

Antes de ejecutar el ejemplo, asegúrate de tener:
1. **Clave API**: Una clave API válida de Mistral AI almacenada en la variable de entorno `MISTRAL_API_KEY`.
2. **Dependencias**: Los paquetes de Python requeridos instalados. Puedes instalarlos con:
   ```bash
   pip install requests numpy
   ```

### Código de Ejemplo

Aquí tienes un script de Python completo que genera embeddings para tres oraciones y calcula sus similitudes por pares:

```python
import os
import requests
import numpy as np

def call_mistral_embeddings_api(texts, model="mistral-embed"):
    """
    Llama a la API de embeddings de Mistral AI para generar embeddings para una lista de textos.
    
    Args:
        texts (list): Lista de cadenas de texto para convertir en embeddings.
        model (str): El modelo de embedding a usar (por defecto: "mistral-embed").
    
    Returns:
        list: Lista de vectores de embedding, o None si la solicitud falla.
    """
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY environment variable not set.")
        return None
    
    url = "https://api.mistral.ai/v1/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "input": texts
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json and "data" in response_json:
            embeddings = [item["embedding"] for item in response_json["data"]]
            return embeddings
        else:
            print(f"Mistral Embeddings API Error: Invalid response format: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral Embeddings API Error: {e}")
        if e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None

def calculate_similarity(emb1, emb2):
    """
    Calcula la similitud entre dos embeddings usando el producto punto.
    
    Args:
        emb1 (list): Primer vector de embedding.
        emb2 (list): Segundo vector de embedding.
    
    Returns:
        float: Puntuación de similitud (producto punto, equivalente a la similitud del coseno para vectores normalizados).
    """
    return np.dot(emb1, emb2)

if __name__ == "__main__":
    # Textos de ejemplo para convertir en embeddings
    texts = [
        "I love programming in Python.",
        "Python is a great programming language.",
        "The weather is sunny today."
    ]
    
    # Generar embeddings
    embeddings = call_mistral_embeddings_api(texts)
    if embeddings:
        # Imprimir la dimensión del embedding
        print(f"Embedding dimension: {len(embeddings[0])}")
        
        # Calcular similitudes por pares
        sim_12 = calculate_similarity(embeddings[0], embeddings[1])
        sim_13 = calculate_similarity(embeddings[0], embeddings[2])
        sim_23 = calculate_similarity(embeddings[1], embeddings[2])
        
        # Mostrar resultados
        print(f"\nSimilarity Results:")
        print(f"Text 1: '{texts[0]}'")
        print(f"Text 2: '{texts[1]}'")
        print(f"Text 3: '{texts[2]}'")
        print(f"\nSimilarity between Text 1 and Text 2: {sim_12:.4f}")
        print(f"Similarity between Text 1 and Text 3: {sim_13:.4f}")
        print(f"Similarity between Text 2 and Text 3: {sim_23:.4f}")
```

### Cómo Ejecutarlo

1. **Establecer la Clave API**:
   ```bash
   export MISTRAL_API_KEY="tu_clave_api_aqui"
   ```

2. **Guardar y Ejecutar**:
   Guarda el script (por ejemplo, como `embedding_example.py`) y ejecútalo:
   ```bash
   python embedding_example.py
   ```

### Salida Esperada

Suponiendo que la llamada a la API tiene éxito, verás una salida similar a esta (los valores exactos dependen de los embeddings devueltos):
```
Embedding dimension: 1024

Similarity Results:
Text 1: 'I love programming in Python.'
Text 2: 'Python is a great programming language.'
Text 3: 'The weather is sunny today.'

Similarity between Text 1 and Text 2: 0.9200
Similarity between Text 1 and Text 3: 0.6500
Similarity between Text 2 and Text 3: 0.6700
```

### Explicación

- **Endpoint API**: La función `call_mistral_embeddings_api` envía una solicitud POST a `https://api.mistral.ai/v1/embeddings`, pasando una lista de textos y el modelo `"mistral-embed"`. La API devuelve una respuesta JSON que contiene los embeddings bajo la clave `"data"`.

- **Embeddings**: Cada embedding es un vector de 1024 dimensiones (según la documentación de Mistral), que representa el contenido semántico del texto de entrada. Los embeddings están normalizados a una norma de 1.

- **Cálculo de Similitud**: Dado que los embeddings están normalizados, el producto punto (`np.dot`) entre dos embeddings es igual a su similitud de coseno. Valores más altos indican mayor similitud semántica:
  - **Texto 1 y Texto 2**: Ambos tratan sobre programación en Python, por lo que su similitud debería ser alta (ej. ~0.92).
  - **Texto 1 y Texto 3**: Uno trata sobre programación, el otro sobre el clima, por lo que su similitud debería ser menor (ej. ~0.65).
  - **Texto 2 y Texto 3**: Patrón similar, menor similitud debido a temas diferentes.

### Casos de Uso Adicionales

Los embeddings de Mistral AI se pueden aplicar más allá de la detección de similitud:
- **Agrupamiento (Clustering)**: Agrupa textos similares usando algoritmos como K-means (requiere `scikit-learn`).
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=2).fit(np.array(embeddings))
  print(kmeans.labels_)
  ```
- **Búsqueda (Search)**: Convierte una consulta en embedding y encuentra el texto más similar:
  ```python
  query = "Tell me about Python."
  query_emb = call_mistral_embeddings_api([query])[0]
  similarities = [calculate_similarity(query_emb, emb) for emb in embeddings]
  most_similar = texts[np.argmax(similarities)]
  print(f"Most similar text: '{most_similar}'")
  ```
- **Clasificación**: Usa los embeddings como características en un modelo de machine learning.

### Notas

- **Modelo**: El modelo `"mistral-embed"` está optimizado para embeddings. Consulta la [documentación](https://docs.mistral.ai/capabilities/embeddings/) para actualizaciones o modelos adicionales.
- **Procesamiento por Lotes (Batching)**: La API procesa múltiples textos en una sola llamada, mejorando la eficiencia.
- **Aplicaciones Avanzadas**: Para búsqueda de similitud a gran escala, integra con bases de datos vectoriales como Faiss o Milvus.

Este ejemplo proporciona una introducción práctica al uso de los embeddings de Mistral AI, adaptable a la estructura del código de completado de chat proporcionado cambiando el endpoint y el formato de datos.