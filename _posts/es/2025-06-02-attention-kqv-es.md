---
audio: false
generated: true
lang: es
layout: post
title: Mecanismo K, Q, V en Transformadores
translated: true
type: note
---

El mecanismo de **Clave (K), Consulta (Q) y Valor (V)** es un componente fundamental del mecanismo de **autoatención** en los modelos de lenguaje grandes (LLMs) basados en Transformer. Este mecanismo, introducido en el artículo seminal *"Attention is All You Need"* (Vaswani et al., 2017), permite a los modelos sopesar la importancia de diferentes palabras en una secuencia al procesar o generar texto. A continuación, proporciono una introducción completa sobre cómo funciona el mecanismo **K, Q, V** en el contexto de los LLMs Transformer, cubriendo su intuición, formulación matemática, implementación en la autoatención y su papel en la arquitectura general.

---

### 1. **Intuición detrás de K, Q, V en la Autoatención**
El mecanismo de autoatención permite a un modelo Transformer procesar una secuencia de entrada centrándose en las partes relevantes de la secuencia para cada palabra (o token). Los componentes **K, Q, V** son los bloques de construcción de este proceso, permitiendo al modelo determinar dinámicamente qué partes de la entrada son más relevantes entre sí.

- **Consulta (Q):** Representa la "pregunta" que un token hace sobre otros tokens en la secuencia. Para cada token, el vector de consulta codifica qué información busca el token del resto de la secuencia.
- **Clave (K):** Representa la "descripción" de cada token en la secuencia. El vector clave codifica qué información puede proporcionar un token a los demás.
- **Valor (V):** Representa el contenido o información real que lleva un token. Una vez que el modelo determina qué tokens son relevantes (a través de las interacciones Q y K), recupera los vectores de valor correspondientes para construir la salida.

La interacción entre **Q** y **K** determina cuánta atención debe prestar cada token a todos los demás tokens, y los vectores **V** se ponderan y combinan en función de esta atención para producir la salida de cada token.

Piensa en ello como una búsqueda en una biblioteca:
- **Consulta**: Tu consulta de búsqueda (por ejemplo, "machine learning").
- **Clave**: Los títulos o metadatos de los libros en la biblioteca, que comparas con tu consulta para encontrar libros relevantes.
- **Valor**: El contenido real de los libros que recuperas después de identificar los relevantes.

---

### 2. **Cómo funcionan K, Q, V en la Autoatención**
El mecanismo de autoatención calcula una suma ponderada de los vectores **Valor**, donde los pesos están determinados por la similitud entre los vectores **Consulta** y **Clave**. Aquí tienes un desglose paso a paso del proceso:

#### Paso 1: Representación de la Entrada
- La entrada a una capa Transformer es una secuencia de tokens (por ejemplo, palabras o subpalabras), cada una representada como un vector de embedding de alta dimensión (por ejemplo, dimensión \\( d_{\text{model}} = 512 \\)).
- Para una secuencia de \\( n \\) tokens, la entrada es una matriz \\( X \in \mathbb{R}^{n \times d_{\text{model}}} \\), donde cada fila es el embedding de un token.

#### Paso 2: Transformaciones Lineales para Generar K, Q, V
- Para cada token, se calculan tres vectores: **Consulta (Q)**, **Clave (K)** y **Valor (V)**. Estos se obtienen aplicando transformaciones lineales aprendidas a los embeddings de entrada:
  \\[
  Q = X W_Q, \quad K = X W_K, \quad V = X W_V
  \\]
  - \\( W_Q, W_K, W_V \in \mathbb{R}^{d_{\text{model}} \times d_k} \\) son matrices de peso aprendidas.
  - Típicamente, \\( d_k = d_v \\), y a menudo se establecen en \\( d_{\text{model}} / h \\) (donde \\( h \\) es el número de cabezas de atención, explicado más adelante).
  - El resultado es:
    - \\( Q \in \mathbb{R}^{n \times d_k} \\): Matriz de Consulta para todos los tokens.
    - \\( K \in \mathbb{R}^{n \times d_k} \\): Matriz de Clave para todos los tokens.
    - \\( V \in \mathbb{R}^{n \times d_v} \\): Matriz de Valor para todos los tokens.

#### Paso 3: Calcular las Puntuaciones de Atención
- El mecanismo de atención calcula cuánto debe atender cada token a todos los demás tokens calculando el **producto punto** entre el vector de consulta de un token y los vectores clave de todos los tokens:
  \\[
  \text{Puntuaciones de Atención} = Q K^T
  \\]
  - Esto produce una matriz \\( \in \mathbb{R}^{n \times n} \\), donde cada entrada \\( (i, j) \\) representa la similitud no normalizada entre la consulta del token \\( i \\) y la clave del token \\( j \\).
- Para estabilizar los gradientes y evitar valores grandes, las puntuaciones se escalan por la raíz cuadrada de la dimensión de la clave:
  \\[
  \text{Puntuaciones Escaladas} = \frac{Q K^T}{\sqrt{d_k}}
  \\]
  - Esto se llama **atención de producto punto escalado**.

#### Paso 4: Aplicar Softmax para Obtener los Pesos de Atención
- Las puntuaciones escaladas se pasan por una función **softmax** para convertirlas en probabilidades (pesos de atención) que suman 1 para cada token:
  \\[
  \text{Pesos de Atención} = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right)
  \\]
  - El resultado es una matriz \\( \in \mathbb{R}^{n \times n} \\), donde cada fila representa la distribución de atención para un token sobre todos los tokens en la secuencia.
  - Los pesos de atención altos indican que los tokens correspondientes son muy relevantes entre sí.

#### Paso 5: Calcular la Salida
- Los pesos de atención se utilizan para calcular una suma ponderada de los vectores **Valor**:
  \\[
  \text{Salida de Atención} = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V
  \\]
  - La salida es una matriz \\( \in \mathbb{R}^{n \times d_v} \\), donde cada fila es una nueva representación de un token, incorporando información de todos los demás tokens en función de su relevancia.

#### Paso 6: Atención Multi-Cabeza
- En la práctica, los Transformers utilizan **atención multi-cabeza**, donde el proceso anterior se realiza múltiples veces en paralelo (con diferentes \\( W_Q, W_K, W_V \\)) para capturar diferentes tipos de relaciones:
  - La entrada se divide en \\( h \\) cabezas, cada una con vectores \\( Q, K, V \\) más pequeños de dimensión \\( d_k = d_{\text{model}} / h \\).
  - Cada cabeza calcula su propia salida de atención.
  - Las salidas de todas las cabezas se concatenan y se pasan a través de una transformación lineal final:
    \\[
    \text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \text{head}_2, \dots, \text{head}_h) W_O
    \\]
    donde \\( W_O \in \mathbb{R}^{h \cdot d_v \times d_{\text{model}}} \\) es una matriz de proyección de salida aprendida.

---

### 3. **Papel de K, Q, V en los LLMs Transformer**
El mecanismo **K, Q, V** se utiliza en diferentes partes de la arquitectura Transformer, dependiendo del tipo de atención:

- **Autoatención en el Codificador (por ejemplo, BERT):**
  - Todos los tokens atienden a todos los demás tokens en la secuencia de entrada (atención bidireccional).
  - \\( Q, K, V \\) se derivan todos de la misma secuencia de entrada \\( X \\).
  - Esto permite al modelo capturar contexto tanto de los tokens precedentes como de los siguientes, lo que es útil para tareas como clasificación de texto o respuesta a preguntas.

- **Autoatención en el Decodificador (por ejemplo, GPT):**
  - En modelos autoregresivos como GPT, el decodificador utiliza **autoatención enmascarada** para evitar atender a tokens futuros (ya que el modelo genera texto secuencialmente).
  - La máscara asegura que para cada token \\( i \\), las puntuaciones de atención para tokens \\( j > i \\) se establezcan en \\(-\infty\\) antes del softmax, dándoles efectivamente un peso cero.
  - \\( Q, K, V \\) todavía se derivan de la secuencia de entrada, pero la atención es causal (solo atiende a tokens anteriores).

- **Atención Cruzada en Modelos Codificador-Decodificador (por ejemplo, T5):**
  - En arquitecturas codificador-decodificador, el decodificador utiliza atención cruzada para atender a la salida del codificador.
  - Aquí, \\( Q \\) se deriva de la entrada del decodificador, mientras que \\( K \\) y \\( V \\) provienen de la salida del codificador, permitiendo al decodificador centrarse en partes relevantes de la secuencia de entrada al generar la salida.

---

### 4. **Por qué K, Q, V funcionan tan bien**
El mecanismo **K, Q, V** es poderoso por varias razones:
- **Contextualización Dinámica**: Permite que cada token recoja información de otros tokens en función de su contenido, en lugar de depender de patrones fijos (por ejemplo, como en RNNs o CNNs).
- **Paralelización**: A diferencia de las redes neuronales recurrentes, la autoatención procesa todos los tokens simultáneamente, lo que la hace muy eficiente en hardware moderno como GPUs.
- **Flexibilidad**: La atención multi-cabeza permite al modelo capturar relaciones diversas (por ejemplo, sintácticas, semánticas) aprendiendo diferentes proyecciones para \\( Q, K, V \\).
- **Escalabilidad**: El mecanismo escala bien a secuencias largas (aunque el coste computacional crece cuadráticamente con la longitud de la secuencia, mitigado por técnicas como atención dispersa o Transformers eficientes).

---

### 5. **Resumen Matemático**
La fórmula de atención de producto punto escalado es:
\\[
\text{Atención}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V
\\]
Para la atención multi-cabeza:
\\[
\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W_O
\\]
donde:
\\[
\text{head}_i = \text{Atención}(Q W_{Q_i}, K W_{K_i}, V W_{V_i})
\\]

---

### 6. **Ejemplo Práctico**
Considera la frase: *"El gato se sentó en la alfombra."*
- **Entrada**: Cada palabra se convierte en un vector de embedding (por ejemplo, a través de una capa de embedding de palabras).
- **Cálculo de Q, K, V**: Para cada token, el modelo calcula vectores de consulta, clave y valor utilizando pesos aprendidos.
- **Puntuaciones de Atención**: Para la palabra "gato", el vector de consulta podría asignar altas puntuaciones de atención a "sentó" y "alfombra" porque son contextualmente relevantes, mientras que da puntuaciones más bajas a "el".
- **Salida**: El mecanismo de atención produce una nueva representación para "gato" que incorpora información de "sentó" y "alfombra", ponderada por sus puntuaciones de atención.

---

### 7. **Extensiones y Optimizaciones**
- **Atención Eficiente**: Para manejar secuencias largas, variantes como Performer, Linformer o Longformer reducen la complejidad computacional de la atención.
- **Codificaciones Posicionales**: Dado que la autoatención es invariante a permutaciones, los Transformers añaden codificaciones posicionales a los embeddings de entrada para capturar el orden de las palabras, lo que influye indirectamente en \\( Q, K, V \\).
- **Apilamiento de Capas**: Los Transformers apilan múltiples capas de autoatención, permitiendo que \\( Q, K, V \\) operen en representaciones cada vez más abstractas.

---

### 8. **Conclusión**
El mecanismo **K, Q, V** es el corazón de la autoatención del Transformer, permitiendo a los LLMs modelar relaciones complejas en el texto de manera eficiente y efectiva. Al calcular las puntuaciones de atención basadas en consultas y claves, y agregar información de los vectores de valor, los Transformers logran un rendimiento de vanguardia en tareas como modelado de lenguaje, traducción y más. Comprender este mecanismo es clave para captar cómo los LLMs modernos procesan y generan texto similar al humano.

Si deseas una inmersión más profunda en algún aspecto específico (por ejemplo, atención multi-cabeza, implementación de código o aplicaciones en modelos específicos), ¡házmelo saber