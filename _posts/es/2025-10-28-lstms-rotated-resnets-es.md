---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Los LSTM eran solo ResNet rotados
translated: true
type: note
---

En su charla del premio Test of Time de NeurIPS 2024 sobre el artículo de 2014 "Sequence to Sequence Learning with Neural Networks", Ilya Sutskever reflexionó sobre las ideas clave y los errores de esa época. Un punto importante que abordó bajo "lo que nos equivocamos" fue la sobrecomplicación y las limitaciones eventuales de las LSTMs (Long Short-Term Memory networks), que impulsaron los primeros avances en el modelado de secuencias, como la traducción automática.

### La idea errónea central sobre las LSTMs
Tratamos las LSTMs como una arquitectura fundamentalmente novedosa e intrincada, diseñada específicamente para datos secuenciales—algo "especial" que los investigadores de deep learning tuvieron que diseñar minuciosamente para manejar dependencias temporales, gradientes que se desvanecen y recurrencia. En realidad, Sutskever explicó que las LSTMs eran mucho más simples que eso: **esencialmente son una ResNet (Red Residual) rotada 90 grados**.

- **Las ResNets** (introducidas en 2015) revolucionaron el procesamiento de imágenes al añadir conexiones de salto (residuales) que permitían que la información fluyera directamente a través de las capas, permitiendo redes mucho más profundas sin inestabilidad en el entrenamiento.
- Las LSTMs (de 1997) hicieron algo análogo pero en la *dimensión temporal*: sus compuertas y estado de celda actúan como residuales, permitiendo que los gradientes y la información se propaguen a lo largo de secuencias largas sin desvanecerse. Es el mismo principio—solo "rotado" del apilamiento espacial (por ejemplo, píxeles en una imagen) al apilamiento temporal (por ejemplo, palabras en una oración).

Sutskever bromeó: "Para los no familiarizados, una LSTM es algo que los pobres investigadores de deep learning hacían antes de los Transformers. Básicamente es una ResNet pero rotada 90 grados... Y llegó antes; es como una ResNet ligeramente más compleja, con un integrador y algunas multiplicaciones". Esta analogía subraya que las LSTMs no fueron una desviación radical; fueron una aplicación temprana y elegante de las ideas residuales a la recurrencia.

### Por qué esto fue importante (y qué salió mal)
- **Lo que funcionó de manera brillante**: Las LSTMs escalaron sorprendentemente bien para su época, permitiendo que el modelo seq2seq superara a los métodos estadísticos tradicionales en tareas de traducción. Los residuales hicieron que las redes recurrentes profundas fueran entrenables, similar a como lo hicieron más tarde para las redes feedforward.
- **Lo que nos equivocamos (y por qué las LSTMs desaparecieron)**: Subestimamos cómo la naturaleza secuencial de las LSTMs sería un cuello de botella para el escalamiento. A diferencia de las ResNets o los Transformers, que son paralelizables, las LSTMs procesan los datos paso a paso, lo que las hace ineficientes para conjuntos de datos masivos o contextos largos. También añadieron una complejidad innecesaria (por ejemplo, múltiples compuertas) que los mecanismos de atención en los Transformers simplificaron. Para 2017, los Transformers expusieron estos límites, cambiando el enfoque hacia la self-attention para un mejor paralelismo y dependencias de mayor rango.

En retrospectiva, la parte "equivocada" no fue inventar las LSTMs—fueron una solución intermedia heroica—sino aferrarse a ellas como la solución final para las secuencias, en lugar de reconocer los residuales como una herramienta general y avanzar antes hacia arquitecturas más paralelizables.

Esta perspectiva redefine las LSTMs no como una reliquia, sino como un paso fundamental para entender cómo las conexiones de salto desbloquean la profundidad a través de las dimensiones.

[Sequence to Sequence Learning with Neural Networks: What a Decade – Transcripción y Video](https://kingy.ai/news/sequence-to-sequence-learning-with-neural-networks-what-a-decade-transcript-video/)  
[Charla completa de Ilya Sutskever en NeurIPS 2024](https://www.youtube.com/watch?v=1yvBqasHLZs)  
[Reflexiones de la charla completa de Ilya en NeurIPS 2024](https://dlyog.com/papers/one_internet_v1)