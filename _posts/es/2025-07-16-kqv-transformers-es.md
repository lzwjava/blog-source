---
audio: false
generated: false
image: false
lang: es
layout: post
title: KQV, transformadores y GPT
translated: true
---

## Cómo Aprendí el Mecanismo KQV en los Transformers

*2025.07.16*

Después de leer [Mecanismo K, Q, V en Transformers](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en), de alguna manera entendí cómo funcionan K, Q y V.

Q significa *Query* (consulta), K significa *Key* (clave) y V significa *Value* (valor). Para una oración, la *Query* es una matriz que almacena el valor de un token que necesita preguntar a otros tokens. La *Key* representa la descripción de los tokens, y el *Value* representa la matriz de significado real de los tokens.

Tienen formas específicas, por lo que es necesario conocer sus dimensiones y detalles.

Lo entendí alrededor de principios de junio de 2025. Lo conocí por primera vez a finales de 2023. En ese momento, leí artículos como [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), pero no entendí mucho.

Después de unos dos años, ahora me resulta más fácil entenderlo. Durante estos dos años, me enfoqué en el trabajo de backend y en prepararme para los exámenes de mi título asociado, y no leí ni aprendí mucho sobre aprendizaje automático. Sin embargo, de vez en cuando reflexionaba sobre estos conceptos mientras conducía o hacía otras cosas.

Esto me recuerda al efecto del tiempo. Podemos aprender muchas cosas a primera vista, aunque no las comprendamos del todo. Pero de alguna manera, desencadena un punto de partida para nuestro pensamiento.

Con el tiempo, descubrí que, en cuanto al conocimiento y el descubrimiento, es difícil pensar o entender las cosas la primera vez. Pero más adelante, parece más fácil aprender y asimilarlas.

Una razón es que, en la era de la IA, es más fácil aprender porque puedes profundizar en cualquier detalle o aspecto para resolver tus dudas. También hay más videos relacionados con IA disponibles. Lo más importante es que ves que muchas personas están aprendiendo y construyendo proyectos basados en ello, como [llama.cpp](https://github.com/ggml-org/llama.cpp).

La historia de Georgi Gerganov es inspiradora. Como nuevo aprendiz de aprendizaje automático desde alrededor de 2021, tuvo un impacto poderoso en la comunidad de IA.

Este tipo de cosas ocurrirán una y otra vez. Así que, para el aprendizaje por refuerzo y los últimos conocimientos en IA, aunque todavía no pueda dedicarles mucho tiempo, creo que puedo encontrar algo de tiempo para aprender rápidamente y tratar de reflexionar mucho sobre ellos. El cerebro hará su trabajo.

---

## De Redes Neuronales a GPT

*2023.09.28*

### Videos de YouTube

Andrej Karpathy - Construyamos GPT: desde cero, en código, explicado paso a paso.

Umar Jamil - Attention is all you need (Transformer) - Explicación del modelo (incluyendo matemáticas), Inferencia y Entrenamiento.

StatQuest con Josh Starmer - Redes Neuronales Transformer, los cimientos de ChatGPT, ¡Explicado claramente!

Pascal Poupart - CS480/680 Clase 19: Mecanismos de Atención y Redes Transformer.

The A.I. Hacker - Michael Phi - Guía Ilustrada de la Red Neural Transformer: una explicación paso a paso.

### Cómo Aprendo

Una vez que había leído la mitad del libro *"Neural Networks and Deep Learning"*, comencé a replicar el ejemplo de red neuronal para reconocer dígitos escritos a mano. Creé un repositorio en GitHub, [https://github.com/lzwjava/neural-networks-and-zhiwei-learning](https://github.com/lzwjava/neural-networks-and-zhiwei-learning).

Esa es la parte realmente difícil. Si alguien puede escribirlo desde cero sin copiar ningún código, entonces lo entiende muy bien.

Mi código replicado aún carece de la implementación de *update_mini_batch* y *backprop*. Sin embargo, al observar cuidadosamente las variables en las fases de carga de datos, propagación hacia adelante y evaluación, obtuve una comprensión mucho mejor del vector, la dimensionalidad, la matriz y la forma de los objetos.

Y comencé a aprender la implementación de GPT y el transformer. Mediante el *embedding* de palabras y la codificación posicional, el texto se convierte en números. Luego, en esencia, no hay diferencia con la red neuronal simple para reconocer dígitos escritos a mano.

La charla de Andrej Karpathy *"Let's build GPT"* es muy buena. Explica las cosas muy bien.

La primera razón es que realmente parte desde cero. Primero vemos cómo generar el texto. Es un poco difuso y aleatorio. La segunda razón es que Andrej puede explicar las cosas de manera muy intuitiva. Andrej trabajó en el proyecto *nanoGPT* durante varios meses.

Acabo de tener una nueva idea para juzgar la calidad de una charla. ¿Puede el autor escribir realmente estos códigos? ¿Por qué no entiendo y qué tema omite el autor? Además de esos diagramas y animaciones elegantes, ¿cuáles son sus defectos y carencias?

Volviendo al tema del aprendizaje automático en sí. Como menciona Andrej, el *dropout*, la conexión residual, la *Self-Attention*, la *Multi-Head Attention*, la *Masked Attention*.

Al ver más videos como los mencionados, comencé a entender un poco.

Mediante la codificación posicional con funciones *sin* y *cos*, obtenemos algunos pesos. Mediante el *embedding* de palabras, convertimos las palabras en números.

$$
    PE_{(pos,2i)} = sin(pos/10000^{2i/d_{model}}) \\
    PE_{(pos,2i+1)} = cos(pos/10000^{2i/d_{model}})
$$

> La pizza salió del horno y sabía bien.

En esta oración, ¿cómo sabe el algoritmo si se refiere a *pizza* u *horno*? ¿Cómo calculamos las similitudes para cada palabra en la oración?

Queremos un conjunto de pesos. Si usamos la red transformer para hacer la tarea de traducción, cada vez que ingresamos una oración, puede generar la oración correspondiente en otro idioma.

Sobre el producto punto aquí. Una razón por la que usamos el producto punto es que considera cada número en el vector. ¿Qué pasa si usamos el producto punto al cuadrado? Primero calculamos el cuadrado de los números y luego hacemos el producto punto. ¿Qué pasa si hacemos algún producto punto inverso?

Sobre el *masked* aquí, cambiamos los números de la mitad de la matriz a infinito negativo. Luego usamos *softmax* para que los valores varíen entre 0 y 1. ¿Qué pasa si cambiamos los números de la parte inferior izquierda a infinito negativo?

### Plan

Seguir leyendo código y artículos, y viendo videos. Solo divertirse y seguir mi curiosidad.

[https://github.com/karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)

[https://github.com/jadore801120/attention-is-all-you-need-pytorch](https://github.com/jadore801120/attention-is-all-you-need-pytorch)