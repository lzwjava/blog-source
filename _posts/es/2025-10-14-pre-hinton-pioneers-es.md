---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Pioneros del Aprendizaje Profundo Antes de Hinton
translated: true
type: note
---

### Trabajo de Alexey Ivakhnenko

Alexey Grigoryevich Ivakhnenko, un cibernético ucraniano-soviético, es a menudo llamado el "padrino del aprendizaje profundo" por sus esfuerzos pioneros en las décadas de 1960 y 1970. Trabajando bajo limitaciones de recursos durante la era de la Guerra Fría—cuando el poder de cómputo era millones de veces más limitado que hoy—se centró en redes neuronales multicapa que podían aprender automáticamente representaciones jerárquicas de los datos.

- **1965: Método Grupal de Manejo de Datos (GMDH)**: Junto a Valentin Lapa, Ivakhnenko publicó el primer algoritmo de aprendizaje general y funcional para perceptrones multicapa (MLPs) profundos y feedforward supervisados. Este método entrenaba las redes capa por capa utilizando análisis de regresión en pares de datos de entrada-salida. Incrementaba las capas gradualmente, las entrenaba secuencialmente e incluía la poda de unidades ocultas innecesarias mediante conjuntos de validación. Crucialmente, permitía que las redes aprendieran representaciones internas y distribuidas de los datos de entrada—una idea central en el aprendizaje profundo moderno—sin ingeniería manual de características. Esto precedió por décadas a conceptos similares en la IA occidental y se aplicó a problemas del mundo real como reconocimiento de patrones y pronósticos.

- **1971: Implementación de Red Profunda**: Ivakhnenko demostró una red neuronal profunda de 8 capas utilizando los principios del GMDH, mostrando una profundidad escalable para tareas complejas. Su enfoque trataba las redes profundas como una forma de aproximación polinomial, permitiendo la selección automática de modelos y evitando la "maldición de la dimensionalidad" en arquitecturas de muchas capas.

El GMDH de Ivakhnenko evolucionó hacia un marco de modelado inductivo más amplio, influyendo en campos como sistemas de control y economía. A pesar de su impacto, gran parte de su trabajo se publicó en ruso y fue pasado por alto en los círculos de IA de habla inglesa.

### Trabajo de Shun-ichi Amari

Shun-ichi Amari, un matemático y neurocientífico japonés, realizó contribuciones fundamentales a la teoría de las redes neuronales en las décadas de 1960 y 1970, enfatizando el aprendizaje adaptativo y las perspectivas geométricas sobre el procesamiento de información. Su investigación tendió un puente entre la neurociencia y la computación, sentando las bases para los sistemas auto-organizativos.

- **1967-1968: Clasificación Adaptativa de Patrones y Descenso de Gradiente Estocástico (SGD)**: Amari propuso el primer método para el entrenamiento de principio a fin de MLPs profundos usando SGD, una técnica de optimización que data de 1951 pero recién aplicada a redes multicapa. En simulaciones con una red de cinco capas (dos capas modificables), su sistema aprendió a clasificar patrones no linealmente separables ajustando los pesos directamente a través de las capas. Esto permitió que emergieran representaciones internas a través de actualizaciones basadas en gradientes, un precursor directo de métodos similares a la retropropagación, todo bajo restricciones de cómputo miles de millones de veces más severas que los estándares modernos.

- **1972: Redes de Memoria Asociativa Adaptativa**: Basándose en el modelo de Lenz-Ising de 1925 (una arquitectura recurrente basada en la física), Amari introdujo una versión adaptativa que aprendía a almacenar y recordar patrones sintonizando los pesos de conexión basándose en correlaciones. Maneja el procesamiento de secuencias y recupera patrones almacenados a partir de entradas ruidosas o parciales mediante dinámicas neuronales. Publicado primero en japonés en 1969, este trabajo es visto como el origen de la "red de Hopfield" para la memoria asociativa.

Amari también fundó la geometría de la información, un campo que utiliza geometría diferencial para analizar modelos estadísticos y dinámicas neuronales, y que sustenta las redes neuronales probabilísticas modernas.

### Contexto en la Polémica del Nobel de 2024

En su informe de 2024 "Un Premio Nobel por Plagio", Jürgen Schmidhuber argumenta que las ideas ganadoras del Nobel de Hinton y Hopfield—como la máquina de Boltzmann (1985) para el aprendizaje de representaciones y la red de Hopfield (1982) para la memoria asociativa—reempaquetaron el aprendizaje profundo capa por capa de Ivakhnenko y los modelos recurrentes adaptativos/SGD de Amari sin atribución. Por ejemplo, la máquina de Boltzmann omitió las citas al aprendizaje de representaciones internas de Ivakhnenko de 1965 y al SGD de Amari de 1967, mientras que la red de Hopfield ignoró el modelo de Ising adaptativo de Amari de 1972. Schmidhuber afirma que esta omisión persistió en estudios posteriores y en el documento de antecedentes científicos del Nobel, resaltando un sesgo centrado en Occidente en la historia de la IA.

[Alexey Ivakhnenko - Wikipedia](https://en.wikipedia.org/wiki/Alexey_Ivakhnenko)  
[Deep Learning in a Nutshell: History and Training - NVIDIA Developer](https://developer.nvidia.com/blog/deep-learning-nutshell-history-training/)  
[Shun-ichi Amari | Kyoto Prize](https://www.kyotoprize.org/en/laureates/shun-ichi_amari/)  
[Japanese scientists were pioneers of AI, yet they're being written out of history](https://modernsciences.org/japanese-ai-pioneers-history-shuninchi-amari-kunihiko-fukushima-december-2024/)  
[A Nobel Prize for Plagiarism - Technical Report IDSIA-24-24](https://people.idsia.ch/~juergen/physics-nobel-2024-plagiarism.pdf)  
[Machine Learning Stirs Controversy in Nobel Prize in Physics - Harvard Technology Review](https://harvardtechnologyreview.com/2024/11/18/machine-learning-stirs-controversy-in-nobel-prize-in-physics/)