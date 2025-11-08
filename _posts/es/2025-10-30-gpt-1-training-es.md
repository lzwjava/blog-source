---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: 'Arquitectura y Entrenamiento de GPT-1: Una Visión General'
translated: true
type: note
---

### Descripción General de la Arquitectura GPT-1

GPT-1 (Generative Pre-trained Transformer 1) es el modelo fundacional introducido por OpenAI en 2018. Fue pionero en el enfoque de pre-entrenar un modelo de lenguaje grande en texto no etiquetado utilizando un objetivo de modelado de lenguaje, seguido de un ajuste fino para tareas específicas. La arquitectura es un **Transformer de solo decodificador**, adaptado del artículo original del Transformer (Vaswani et al., 2017), pero reducido a solo la pila del decodificador para la generación autoregresiva. Este diseño permite al modelo predecir el siguiente token en una secuencia, haciéndolo adecuado para tareas que involucran texto continuo.

A diferencia de modelos bidireccionales como BERT, GPT-1 utiliza **autoatención enmascarada** para garantizar la causalidad: cada posición solo puede atender a posiciones anteriores, evitando la fuga de información de tokens futuros.

### Componentes Clave e Hiperparámetros

- **Tipo de Modelo**: Decodificador Transformer multicapa con autoatención multicabezal enmascarada y redes feed-forward posicionales.
- **Número de Capas**: 12 bloques Transformer (capas).
- **Mecanismo de Atención**: 12 cabezas de atención por capa, cada una procesando estados de 64 dimensiones (dimensión total del modelo: 768).
- **Dimensiones de Embedding**:
  - Tamaño oculto (d_model): 768.
  - Dimensión interna feed-forward (d_ff): 3072 (4x el tamaño oculto, estándar para Transformers).
- **Codificación Posicional**: Embeddings posicionales aprendidos añadidos a los embeddings de token (no se utilizan codificaciones sinusoidales).
- **Función de Activación**: Gaussian Error Linear Units (GELU) en las capas feed-forward.
- **Vocabulario y Tokenización**: Byte-Pair Encoding (BPE) con 40,000 fusiones, entrenado en el corpus.
- **Parámetros Totales**: Aproximadamente 117 millones.
- **Longitud de Secuencia**: Entrenado en secuencias de 512 tokens.
- **Regularización**:
  - Dropout: 0.1 en residuos, embeddings y atención.
  - Decaimiento de peso: Regularización L2 modificada (0.01) en pesos que no son de sesgo ni de capa de normalización.
- **Inicialización**: Pesos inicializados desde una distribución normal N(0, 0.02).

### Detalles del Entrenamiento

- **Pre-entrenamiento**:
  - **Conjunto de Datos**: BooksCorpus, una colección de ~7,000 libros no publicados (total ~800 millones de palabras) en géneros como Fantasía, Romance y Aventura. El texto se limpió (por ejemplo, mediante la biblioteca ftfy) y se tokenizó con spaCy.
  - **Objetivo**: Modelado de lenguaje no supervisado (predicción del siguiente token).
  - **Optimizador**: Adam con β1=0.9, β2=0.999, ε=1e-8.
  - **Programación de Tasa de Aprendizaje**: Calentamiento lineal durante 2,000 actualizaciones hasta un máximo de 2.5×10⁻⁴, luego enfriamiento coseno hasta 0.
  - **Tamaño del Lote**: 64 secuencias por minilote.
  - **Épocas**: 100.
  - **Métrica de Rendimiento**: Logró una perplejidad de 18.4 en el corpus de entrenamiento.
- **Ajuste Fino**:
  - Cambios mínimos: Se añade una capa de salida lineal para predicciones específicas de la tarea y se utilizan tokens delimitadores (por ejemplo, <s>, <e>, $) para estructurar las entradas como secuencias únicas.
  - Pérdida auxiliar de modelado de lenguaje ponderada en 0.5 durante el ajuste fino.
  - Hiperparámetros: Tasa de aprendizaje más baja (6.25×10⁻⁵), tamaño de lote 32, 3 épocas, con 0.2% de calentamiento y decaimiento lineal.
  - Este enfoque de aprendizaje por transferencia permitió un rendimiento sólido en tareas como implicación textual y respuesta a preguntas sin necesidad de arquitecturas específicas por tarea.

### Innovaciones y Limitaciones Notables

GPT-1 demostró que un único modelo pre-entrenado podía transferirse efectivamente a diversas tareas de PLN mediante un simple formato de entrada, superando a algunos modelos ajustados por tarea en su momento. Sin embargo, era relativamente pequeño en comparación con los LLM modernos (por ejemplo, GPT-3 tiene 175B parámetros) y estaba limitado a contextos de 512 tokens. La arquitectura sentó las bases para toda la serie GPT, enfatizando la escalabilidad en el pre-entrenamiento.

[Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)  
[GPT-1 - Wikipedia](https://en.wikipedia.org/wiki/GPT-1)