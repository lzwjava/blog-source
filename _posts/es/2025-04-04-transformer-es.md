---
audio: false
generated: true
lang: es
layout: post
title: Transformador
translated: true
type: note
---

El **Transformer** es una arquitectura de red neuronal revolucionaria que se ha convertido en la base de la mayoría de los Modelos de Lenguaje Grandes (LLMs) modernos. Fue presentada en el influyente artículo de 2017 "Attention Is All You Need" por Vaswani et al. y desde entonces ha cambiado fundamentalmente el campo del Procesamiento del Lenguaje Natural (NLP).

A diferencia de arquitecturas dominantes anteriores como las Redes Neuronales Recurrentes (RNNs), que procesan datos secuenciales paso a paso, el Transformer procesa secuencias de entrada completas **en paralelo**. Esta diferencia clave permite mejoras significativas en la velocidad de entrenamiento y la capacidad de capturar dependencias de largo alcance dentro del texto.

Aquí hay un análisis profundo de los componentes clave y conceptos de la arquitectura Transformer en el contexto de los LLMs:

**1. Idea Central: Mecanismo de Atención**

La innovación central del Transformer es el **mecanismo de atención**, particularmente la **auto-atención**. Este mecanismo permite al modelo sopesar la importancia de diferentes palabras (o tokens) en la secuencia de entrada al procesar una palabra específica. En lugar de depender solo de las palabras inmediatamente precedentes (como las RNNs), la auto-atención permite al modelo considerar todo el contexto para comprender el significado y las relaciones entre las palabras.

Piénsalo así: cuando lees una oración, no procesas cada palabra de forma aislada. Tu cerebro considera simultáneamente todas las palabras para entender el significado general y cómo cada palabra contribuye a él. El mecanismo de auto-atención imita este comportamiento.

**Cómo Funciona la Auto-Atención (Simplificado):**

Para cada palabra en la secuencia de entrada, el Transformer calcula tres vectores:

*   **Consulta (Q):** Representa lo que la palabra actual está "buscando" en las otras palabras.
*   **Clave (K):** Representa qué información "contiene" cada otra palabra.
*   **Valor (V):** Representa la información real que contiene cada otra palabra y que podría ser relevante.

El mecanismo de auto-atención luego realiza los siguientes pasos:

1.  **Calcular Puntajes de Atención:** Se calcula el producto punto entre el vector Consulta de una palabra y el vector Clave de todas las demás palabras en la secuencia. Estos puntajes indican cuán relevante es la información de cada otra palabra para la palabra actual.
2.  **Escalar los Puntajes:** Los puntajes se dividen por la raíz cuadrada de la dimensión de los vectores Clave (`sqrt(d_k)`). Este escalado ayuda a estabilizar los gradientes durante el entrenamiento.
3.  **Aplicar Softmax:** Los puntajes escalados se pasan a través de una función softmax, que los normaliza en probabilidades entre 0 y 1. Estas probabilidades representan los **pesos de atención** – cuánta "atención" debe prestar la palabra actual a cada una de las otras palabras.
4.  **Calcular Valores Ponderados:** El vector Valor de cada palabra se multiplica por su correspondiente peso de atención.
5.  **Sumar los Valores Ponderados:** Los vectores Valor ponderados se suman para producir el **vector de salida** para la palabra actual. Este vector de salida ahora contiene información de todas las demás palabras relevantes en la secuencia de entrada, ponderadas por su importancia.

**2. Atención Multi-Cabeza**

Para mejorar aún más la capacidad del modelo para capturar diferentes tipos de relaciones, el Transformer emplea la **atención multi-cabeza**. En lugar de realizar el mecanismo de auto-atención solo una vez, lo hace múltiples veces en paralelo con diferentes conjuntos de matrices de peso de Consulta, Clave y Valor. Cada "cabeza" aprende a enfocarse en diferentes aspectos de las relaciones entre las palabras (por ejemplo, dependencias gramaticales, conexiones semánticas). Las salidas de todas las cabezas de atención se concatenan y se transforman linealmente para producir la salida final de la capa de atención multi-cabeza.

**3. Codificación Posicional**

Dado que el Transformer procesa todas las palabras en paralelo, pierde información sobre el **orden** de las palabras en la secuencia. Para abordar esto, se añade una **codificación posicional** a las incrustaciones de entrada. Estas codificaciones son vectores que representan la posición de cada palabra en la secuencia. Típicamente son patrones fijos (por ejemplo, funciones sinusoidales) o incrustaciones aprendidas. Al añadir codificaciones posicionales, el Transformer puede entender la naturaleza secuencial del lenguaje.

**4. Pilas de Codificador y Decodificador**

La arquitectura Transformer consiste típicamente en dos partes principales: un **codificador** y un **decodificador**, ambos compuestos por múltiples capas idénticas apiladas una sobre otra.

*   **Codificador:** La función del codificador es procesar la secuencia de entrada y crear una representación enriquecida de la misma. Cada capa del codificador contiene típicamente:
    *   Una subcapa de **auto-atención multi-cabeza**.
    *   Una subcapa de **red neuronal de propagación hacia adelante**.
    *   **Conexiones residuales** alrededor de cada subcapa, seguidas de **normalización de capa**. Las conexiones residuales ayudan con el flujo de gradientes durante el entrenamiento, y la normalización de capa estabiliza las activaciones.

*   **Decodificador:** La función del decodificador es generar la secuencia de salida (por ejemplo, en traducción automática o generación de texto). Cada capa del decodificador contiene típicamente:
    *   Una subcapa de **auto-atención multi-cabeza enmascarada**. El "enmascaramiento" evita que el decodificador vea los tokens futuros en la secuencia objetivo durante el entrenamiento, asegurando que solo use los tokens previamente generados para predecir el siguiente.
    *   Una subcapa de **atención multi-cabeza** que atiende a la salida del codificador. Esto permite al decodificador enfocarse en las partes relevantes de la secuencia de entrada mientras genera la salida.
    *   Una subcapa de **red neuronal de propagación hacia adelante**.
    *   **Conexiones residuales** y **normalización de capa** similares al codificador.

**5. Redes de Propagación hacia Adelante**

Cada capa del codificador y decodificador contiene una red neuronal de propagación hacia adelante (FFN). Esta red se aplica a cada token de forma independiente y ayuda a procesar aún más las representaciones aprendidas por los mecanismos de atención. Típicamente consiste en dos transformaciones lineales con una función de activación no lineal (por ejemplo, ReLU) en medio.

**Cómo se Usan los Transformers en los LLMs:**

Los LLMs se basan principalmente en la arquitectura Transformer **solo de decodificador** (como los modelos GPT) o en la arquitectura **codificador-decodificador** (como T5).

*   **Modelos solo de decodificador:** Estos modelos están entrenados para predecir el siguiente token en una secuencia dados los tokens precedentes. Apilan múltiples capas de decodificador. La indicación de entrada se pasa a través de las capas, y la capa final predice la distribución de probabilidad sobre el vocabulario para el siguiente token. Al muestrear de forma autoregresiva a partir de esta distribución, el modelo puede generar texto coherente y contextualmente relevante.

*   **Modelos codificador-decodificador:** Estos modelos toman una secuencia de entrada y generan una secuencia de salida. Utilizan la arquitectura completa de codificador-decodificador. El codificador procesa la entrada, y el decodificador utiliza la salida del codificador para generar la secuencia objetivo. Estos son adecuados para tareas como traducción, resumen y respuesta a preguntas.

**Comprendiendo Profundamente la Significancia:**

El impacto de la arquitectura Transformer en los LLMs es profundo:

*   **Manejo de Dependencias de Largo Alcance:** El mecanismo de auto-atención permite al modelo conectar directamente palabras que están muy separadas en la secuencia, superando las limitaciones de las RNNs para capturar contexto de largo alcance.
*   **Procesamiento en Paralelo:** Procesar toda la secuencia en paralelo reduce significativamente el tiempo de entrenamiento y permite el uso de conjuntos de datos y modelos mucho más grandes.
*   **Escalabilidad:** La arquitectura Transformer escala bien con el aumento de datos y el tamaño del modelo, lo que lleva al desarrollo de LLMs extremadamente potentes con miles de millones o incluso billones de parámetros.
*   **Comprensión Contextual:** El mecanismo de atención permite al modelo comprender el contexto de las palabras de una manera más matizada, lo que lleva a una mejor comprensión y generación del lenguaje.
*   **Fundamento para la Innovación:** La arquitectura Transformer ha servido como base para numerosos avances y variaciones, lo que ha llevado al diverso panorama de los LLMs modernos.

En resumen, la arquitectura Transformer, con su mecanismo central de auto-atención, capacidades de procesamiento en paralelo y estructura codificador-decodificador (o variaciones solo de decodificador), ha revolucionado el campo del NLP y es la fuerza impulsora detrás de las notables capacidades de los Modelos de Lenguaje Grandes modernos.