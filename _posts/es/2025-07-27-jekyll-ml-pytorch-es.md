---
audio: false
generated: true
image: false
lang: es
layout: post
title: Mejora de Blog de Jekyll con PyTorch
translated: true
type: note
---

### Mejorar tu Blog de Jekyll con ML/IA Usando PyTorch

Dado que estás ejecutando un blog de Jekyll (un generador de sitios estáticos), integrar funciones de ML/IA como recomendaciones o categorización requiere algo de creatividad. Jekyll genera HTML estático, por lo que los elementos dinámicos (por ejemplo, recomendaciones en tiempo real) podrían necesitar JavaScript del lado del cliente o precomputarse durante el proceso de compilación mediante plugins o scripts de Jekyll. Mencionaste que quieres evitar las APIs de LLM y centrarte en tus propias redes neuronales con PyTorch—excelente, ya que esto mantiene todo local y personalizable. Esbozaré ideas prácticas, centrándome en implementaciones con PyTorch. Estas asumen que tienes acceso a bibliotecas básicas como NumPy (para el manejo de datos) y puedes manejar el preprocesamiento de texto manualmente o con una tokenización simple (ya que no se mencionan bibliotecas avanzadas de NLP como Hugging Face en tu configuración, pero puedes agregarlas localmente si es necesario).

Es probable que crees scripts de Python (por ejemplo, en tu directorio `scripts/`) que se ejecuten durante el proceso de compilación de Jekyll (a través de un hook en un Makefile o GitHub Actions si se despliega). Por ejemplo, procesa las publicaciones en Markdown en `_posts/`, genera datos JSON y los inyecta en tu sitio a través de las plantillas Liquid.

#### 1. Categorización de Artículos con un Clasificador de PyTorch
Categoriza las publicaciones automáticamente (por ejemplo, en temas como "ML", "Notes", "Latex") entrenando una red neuronal clasificadora simple. Esto es aprendizaje supervisado: necesitarás etiquetar manualmente un subconjunto de tus publicaciones como datos de entrenamiento. Si no tienes etiquetas, comienza con agrupamiento no supervisado (ver más abajo).

**Pasos:**
- **Preparación de Datos:** Analiza tus archivos Markdown en `_posts/`. Extrae el contenido de texto (omite el frontmatter). Crea un conjunto de datos: lista de pares (texto, etiqueta). Usa un CSV o una lista para ~50-100 ejemplos etiquetados inicialmente.
- **Preprocesamiento:** Tokeniza el texto (división simple por espacios/espacios en blanco), construye un vocabulario, convierte a índices numéricos. Usa codificación one-hot o incrustaciones básicas.
- **Modelo:** Una red neuronal feedforward básica en PyTorch para clasificación multi-clase.
- **Entrenamiento:** Entrena en tu máquina local. Usa pérdida de entropía cruzada y el optimizador Adam.
- **Integración:** Ejecuta el script durante la compilación para clasificar todas las publicaciones, genera un archivo `categories.json` y úsalo en Jekyll para etiquetar páginas o crear índices de categorías.

**Fragmento de Código de PyTorch de Ejemplo (en un script como `scripts/categorize_posts.py`):**
```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import os
from collections import Counter

# Paso 1: Cargar y preprocesar datos (simplificado)
def load_posts(posts_dir='_posts'):
    texts = []
    labels = []  # Asume etiquetas manuales: 0=ML, 1=Notes, etc.
    for file in os.listdir(posts_dir):
        if file.endswith('.md'):
            with open(os.path.join(posts_dir, file), 'r') as f:
                content = f.read().split('---')[2].strip()  # Omitir frontmatter
                texts.append(content)
                # Marcador de posición: cargar etiqueta desde un dict o CSV
                labels.append(0)  # Reemplazar con etiquetas reales
    return texts, labels

texts, labels = load_posts()
# Construir vocabulario (top 1000 palabras)
all_words = ' '.join(texts).lower().split()
vocab = {word: idx for idx, word in enumerate(Counter(all_words).most_common(1000))}
vocab_size = len(vocab)

# Convertir texto a vectores (bag-of-words)
def text_to_vec(text):
    vec = np.zeros(vocab_size)
    for word in text.lower().split():
        if word in vocab:
            vec[vocab[word]] += 1
    return vec

X = np.array([text_to_vec(t) for t in texts])
y = torch.tensor(labels, dtype=torch.long)

# Paso 2: Definir modelo
class Classifier(nn.Module):
    def __init__(self, input_size, num_classes):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, num_classes)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = Classifier(vocab_size, num_classes=3)  # Ajustar num_classes

# Paso 3: Entrenar
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()
X_tensor = torch.tensor(X, dtype=torch.float32)

for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X_tensor)
    loss = loss_fn(outputs, y)
    loss.backward()
    optimizer.step()
    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# Paso 4: Inferencia en una nueva publicación
def classify_post(text):
    vec = torch.tensor(text_to_vec(text), dtype=torch.float32).unsqueeze(0)
    with torch.no_grad():
        pred = model(vec).argmax(1).item()
    return pred  # Mapear de vuelta al nombre de la categoría

# Guardar modelo: torch.save(model.state_dict(), 'classifier.pth')
# En el script de compilación: clasificar todas las publicaciones y escribir a JSON
```

**Mejoras:** Para una mejor precisión, usa incrustaciones de palabras (entrena una capa de Embedding simple en PyTorch) o agrega más capas. Si no hay etiquetas, cambia a agrupamiento (por ejemplo, KMeans en incrustaciones—ver la siguiente sección). Ejecuta este script en tu Makefile: `jekyll build && python scripts/categorize_posts.py`.

#### 2. Sistema de Recomendación con Incrustaciones de PyTorch
Recomienda artículos similares a los lectores (por ejemplo, "También te podría gustar..."). Usa recomendación basada en contenido: aprende incrustaciones para cada publicación, luego calcula la similitud (distancia coseno). No se necesitan datos de usuario—solo el contenido de la publicación.

**Pasos:**
- **Datos:** Igual que antes—extrae texto de las publicaciones.
- **Modelo:** Entrena un autoencoder en PyTorch para comprimir texto en incrustaciones de baja dimensión (por ejemplo, vectores de 64 dimensiones).
- **Entrenamiento:** Minimiza la pérdida de reconstrucción para aprender representaciones significativas.
- **Recomendaciones:** Para una publicación dada, encuentra los vecinos más cercanos en el espacio de incrustaciones.
- **Integración:** Precalcula las incrustaciones durante la compilación, almacénalas en JSON. Usa JS en el sitio para mostrar recomendaciones (o Liquid para listas estáticas).

**Fragmento de Código de PyTorch de Ejemplo (en `scripts/recommend_posts.py`):**
```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
# Reutilizar load_posts y text_to_vec de arriba

texts, _ = load_posts()  # Ignorar etiquetas
X = np.array([text_to_vec(t) for t in texts])
X_tensor = torch.tensor(X, dtype=torch.float32)

# Modelo Autoencoder
class Autoencoder(nn.Module):
    def __init__(self, input_size, embedding_size=64):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_size, 256),
            nn.ReLU(),
            nn.Linear(256, embedding_size)
        )
        self.decoder = nn.Sequential(
            nn.Linear(embedding_size, 256),
            nn.ReLU(),
            nn.Linear(256, input_size)
        )
    
    def forward(self, x):
        emb = self.encoder(x)
        return self.decoder(emb)

model = Autoencoder(vocab_size)
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.MSELoss()

for epoch in range(200):
    optimizer.zero_grad()
    reconstructed = model(X_tensor)
    loss = loss_fn(reconstructed, X_tensor)
    loss.backward()
    optimizer.step()
    if epoch % 20 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# Obtener incrustaciones
with torch.no_grad():
    embeddings = model.encoder(X_tensor).numpy()

# Recomendar: para la publicación i, encontrar las 3 más similares
similarities = cosine_similarity(embeddings)
for i in range(len(texts)):
    rec_indices = similarities[i].argsort()[-4:-1][::-1]  # Top 3 excluyéndose a sí misma
    print(f'Recs for post {i}: {rec_indices}')

# Guardar incrustaciones en JSON para Jekyll
import json
with open('embeddings.json', 'w') as f:
    json.dump({'embeddings': embeddings.tolist(), 'posts': [f'post_{i}' for i in range(len(texts))]}, f)
```

**Mejoras:** Usa un autoencoder variacional para mejores incrustaciones. Si tienes vistas de usuarios (a través de analytics), agrega filtrado colaborativo con un modelo de factorización de matrices en PyTorch. Lado del cliente: Carga JSON en JS y calcula similitudes sobre la marcha para personalización.

#### 3. Otras Ideas con PyTorch
- **Agrupamiento No Supervisado para Etiquetado Automático:** Si el etiquetado es tedioso, usa incrustaciones (del autoencoder anterior) + agrupamiento KMeans para agrupar publicaciones en temas. PyTorch para incrustaciones, NumPy/SciPy para el agrupamiento.
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=5)
  clusters = kmeans.fit_predict(embeddings)
  # Asignar etiquetas basadas en los clusters
  ```
  Integrar: Genera etiquetas en el frontmatter a través de un script.

- **Mejora de Búsqueda Semántica:** Incrusta consultas y publicaciones de manera similar, luego usa la similitud coseno para una barra de búsqueda. Precalcula las incrustaciones de las publicaciones; usa JS para incrustar consultas (pero como PyTorch es Python, exporta el modelo a ONNX para inferencia en JS a través de ONNX.js, o mantén la búsqueda estática).

- **Resumen de Publicaciones:** Entrena un modelo seq2seq (RNN/LSTM en PyTorch) en datos emparejados (texto completo, resumen manual). Desafiante sin grandes conjuntos de datos, pero comienza pequeño con tus publicaciones. Úsalo para generar extractos.

**Consejos Generales:**
- **Escalabilidad:** Para un blog pequeño, entrena en CPU; PyTorch lo maneja bien. Guarda modelos con `torch.save` y cárgalos para inferencia.
- **Integración en la Compilación:** Agrega al Makefile: `train: python scripts/train_models.py` luego `build: jekyll build && python scripts/generate_features.py`.
- **Limitaciones:** Sin NLP avanzado (por ejemplo, transformers), los resultados son básicos—considera agregar `torchtext` o incrustaciones GloVe manuales localmente. Prueba en tus directorios `ml/` o `notes/`.
- **Despliegue:** Si estás en GitHub Pages, ejecuta los scripts en CI. Para cosas dinámicas, considera agregar un backend Flask ligero, pero eso se desvía de Jekyll estático.

Si compartes más detalles (por ejemplo, número de publicaciones, temas), ¡puedo refinar esto!