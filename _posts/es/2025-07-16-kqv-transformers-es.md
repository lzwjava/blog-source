---
audio: false
generated: false
image: false
lang: es
layout: post
title: Red Neuronal, Transformer y GPT
translated: true
---

### Tabla de Contenidos

1. [Cómo aprendí el Mecanismo KQV en Transformers](#how-i-learned-the-kqv-mechanism-in-transformers)
   - Las matrices Query, Key, Value representan interacciones de tokens
   - La comprensión requiere conocer dimensiones y formas
   - Los conceptos iniciales se aclaran con el tiempo
   - La era de la IA proporciona abundantes recursos de aprendizaje
   - Historias inspiradoras motivan el aprendizaje continuo

2. [De las Redes Neuronales a GPT](#from-neural-network-to-gpt)
   - Replicar redes neuronales desde cero para entenderlas
   - Los Transformers procesan texto mediante embedding y codificación
   - La autoatención calcula similaridades entre palabras
   - Ver conferencias fundamentales y leer código
   - Seguir la curiosidad a través de proyectos y artículos

3. [Cómo funciona una Red Neuronal](#how-neural-network-works)
   - El algoritmo de retropropagación actualiza pesos y sesgos
   - Los datos de entrada se activan a través de las capas de la red
   - El feedforward calcula las salidas de las capas mediante sigmoide
   - El cálculo de errores guía los ajustes del aprendizaje
   - La comprensión dimensional es crucial para su entendimiento


## Cómo aprendí el Mecanismo KQV en Transformers

*2025.07.16*

Después de leer [Mecanismo K, Q, V en Transformers](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en), de alguna manera entendí cómo funcionan K, Q y V.

Q significa Query (Consulta), K significa Key (Clave) y V significa Value (Valor). Para una oración, la Query es una matriz que almacena el valor de un token que necesita consultar a otros tokens. La Key representa la descripción de los tokens, y la Value representa la matriz de significado real de los tokens.

Tienen formas específicas, por lo que uno necesita conocer sus dimensiones y detalles.

Esto lo entendí alrededor de principios de junio de 2025. Lo aprendí por primera vez a finales de 2023. En ese momento, leí artículos como [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), pero no entendí mucho.

Después de unos dos años, me resultó más fácil de entender ahora. Durante estos dos años, me centré en el trabajo de backend y en la preparación para mis exámenes de grado asociado, y no leí ni aprendí mucho sobre machine learning. Sin embargo, de vez en cuando reflexionaba sobre estos conceptos cuando conducía o hacía otras cosas.

Esto me recuerda el efecto del tiempo. Podemos aprender muchas cosas a primera vista, incluso si no comprendemos mucho. Pero de alguna manera, esto activa un punto de partida para nuestro pensamiento.

Con el tiempo, descubrí que para el conocimiento y el descubrimiento, es difícil pensar o entender las cosas la primera vez. Pero más tarde, parece más fácil aprender y conocer.

Una de las razones es que en la era de la IA, es más fácil aprender porque puedes profundizar en cualquier detalle o aspecto para resolver tus dudas. También hay más videos de IA relacionados disponibles. Más importante aún, ves que muchas personas están aprendiendo y desarrollando proyectos sobre esto, como [llama.cpp](https://github.com/ggml-org/llama.cpp).

La historia de Georgi Gerganov es inspiradora. Como un nuevo estudiante de machine learning que comenzó alrededor de 2021, tuvo un impacto poderoso en la comunidad de IA.

Este tipo de cosas sucederán una y otra vez. Por lo tanto, para el aprendizaje por refuerzo y los últimos conocimientos de IA, aunque todavía no puedo dedicarles mucho tiempo, creo que puedo encontrar algo de tiempo para aprender rápidamente e intentar pensar mucho en ellos. El cerebro hará su trabajo.


---

## De las Redes Neuronales a GPT

*2023.09.28*

### Videos de YouTube

Andrej Karpathy - Let's build GPT: from scratch, in code, spelled out.

Umar Jamil - Attention is all you need (Transformer) - Model explanation (including math), Inference and Training

StatQuest con Josh Starmer - Transformer Neural Networks, ChatGPT's foundation, Clearly Explained!!!

Pascal Poupart - CS480/680 Lecture 19: Attention and Transformer Networks

The A.I. Hacker - Michael Phi - Illustrated Guide to Transformers Neural Network: A step-by-step explanation

### Cómo aprendo

Una vez que había leído la mitad del libro "Redes Neuronales y Deep Learning", comencé a replicar el ejemplo de una red neuronal para reconocer dígitos escritos a mano. Creé un repositorio en GitHub, https://github.com/lzwjava/neural-networks-and-zhiwei-learning.

Esa es la parte realmente difícil. Si uno puede escribirlo desde cero sin copiar ningún código, lo entiende muy bien.

Mi código de replicación aún carece de la implementación de update_mini_batch y backprop. Sin embargo, al observar cuidadosamente las variables en la fase de carga de datos, feed forwarding y evaluación, obtuve una comprensión mucho mejor del vector, la dimensionalidad, la matriz y la forma de los objetos.

Y comencé a aprender la implementación de GPT y transformer. Mediante word embedding y codificación posicional, el texto se convierte en números. Entonces, en esencia, no tiene diferencia con la red neuronal simple para reconocer dígitos escritos a mano.

La conferencia de Andrej Karpathy "Let's build GPT" es muy buena. Explica las cosas bien.

La primera razón es que realmente es desde cero. Primero vemos cómo generar el texto. Es algo borroso y aleatorio. La segunda razón es que Andrej puede explicar las cosas de manera muy intuitiva. Andrej realizó el proyecto nanoGPT durante varios meses.

Acabo de tener una nueva idea para juzgar la calidad de la conferencia. ¿Puede el autor realmente escribir estos códigos? ¿Por qué no lo entiendo y qué tema omite el autor? Además de estos diagramas y animaciones elegantes, ¿cuáles son sus deficiencias y defectos?

Volviendo al tema de machine learning en sí. Como menciona Andrej, el dropout, la conexión residual, el Self-Attention, el Multi-Head Attention, el Masked Attention.

Al ver más videos mencionados, comencé a entender un poco.

Mediante la codificación posicional con funciones sin y cos, obtenemos algunos pesos. Mediante word embedding, cambiamos las palabras a números.

$$
    PE_{(pos,2i)} = sin(pos/10000^{2i/d_{model}}) \\
    PE_{(pos,2i+1)} = cos(pos/10000^{2i/d_{model}})
$$

> La pizza salió del horno y sabía bien.

En esta oración, ¿cómo sabe el algoritmo si se refiere a la pizza o al horno? ¿Cómo calculamos las similitudes para cada palabra en la oración?

Queremos un conjunto de pesos. Si utilizamos la red transformer para la tarea de traducción, cada vez que introducimos una oración, puede generar la oración correspondiente en otro idioma.

Sobre el producto punto aquí. Una razón por la que usamos el producto punto aquí es que el producto punto considerará cada número en el vector. ¿Qué pasa si usamos el producto punto al cuadrado? Primero calculamos el cuadrado de los números, luego los dejamos hacer el producto punto. ¿Qué pasa si hacemos un producto punto inverso?

Sobre la máscara aquí, cambiamos los números de la mitad de la matriz a infinito negativo. Y luego usamos softmax para hacer que los valores estén en el rango de 0 a 1. ¿Qué pasa si cambiamos los números de la parte inferior izquierda a infinito negativo?

### Plan

Continuar leyendo código y artículos y viendo videos. Simplemente diviértete y sigue tu curiosidad.

https://github.com/karpathy/nanoGPT

https://github.com/jadore801120/attention-is-all-you-need-pytorch

---

## Cómo funciona una Red Neuronal

*2023.05.30*

Discutamos directamente el núcleo del trabajo neuronal. Es decir, el algoritmo de retropropagación:

1. Entrada x: Establezca la activación correspondiente $$a^{1}$$ para la capa de entrada.
2. Propagación hacia adelante (Feedforward): Para cada l=2,3,…,L calcule $$z^{l} = w^l a^{l-1}+b^l$$ y $$a^{l} = \sigma(z^{l})$$
3. Error de salida $$\delta^{L}$$: Calcule el vector $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$
4. Retropropagación del error (Backpropagate the error): Para cada l=L−1,L−2,…,2, calcule $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$
5. Salida: El gradiente de la función de costo viene dado por $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$ y $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$

Esto está copiado del libro *Neural Networks and Deep Learning* de Michael Nelson. ¿Es abrumador? Podría ser la primera vez que lo ves. Pero no lo es después de un mes de estudiarlo. Permítanme explicar.

### Entrada

Hay 5 fases. La primera fase es la Entrada. Aquí usamos dígitos escritos a mano como entrada. Nuestra tarea es reconocerlos. Un dígito escrito a mano tiene 784 píxeles, que es 28*28. En cada píxel, hay un valor de escala de grises que va de 0 a 255. Entonces, la activación significa que usamos alguna función para activarlo, para cambiar su valor original a un nuevo valor para facilitar el procesamiento.

Digamos, ahora tenemos 1000 imágenes de 784 píxeles. Ahora la entrenamos para reconocer qué dígito muestran. Ahora tenemos 100 imágenes para probar ese efecto de aprendizaje. Si el programa puede reconocer los dígitos de 97 imágenes, decimos que su precisión es del 97%.

Así que recorreríamos las 1000 imágenes para entrenar los pesos y los sesgos. Hacemos que los pesos y los sesgos sean más correctos cada vez que le damos una nueva imagen para aprender.

Un resultado de entrenamiento por lote se refleja en 10 neuronas. Aquí, las 10 neuronas representan del 0 al 9 y su valor oscila entre 0 y 1 para indicar su confianza en su precisión.

Y la entrada es de 784 neuronas. ¿Cómo podemos reducir 784 neuronas a 10 neuronas? Aquí está la cuestión. Supongamos que tenemos dos capas. ¿Qué significa la capa? Esa es la primera capa, tenemos 784 neuronas. En la segunda capa, tenemos 10 neuronas.

Le damos a cada neurona de las 784 neuronas un peso, por ejemplo,

$$w_1, w_2, w_3, w_4, ... , w_{784}$$

Y le damos a la primera capa, un sesgo, es decir, $$b_1$$.

Y así, para la primera neurona en la segunda capa, su valor es:

$$w_1*a_1 + w_2*a_2+...+ w_{784}*a_{784}+b_1$$

Pero estos pesos y un sesgo son para $$neuron^2_{1}$$(el primero en la segunda capa). Para la $$neuron^2_{2}$$, necesitamos otro conjunto de pesos y un sesgo.

¿Qué pasa con la función sigmoide? Usamos la función sigmoide para mapear el valor de lo anterior de 0 a 1.

$$
\begin{eqnarray}
  \sigma(z) \equiv \frac{1}{1+e^{-z}}
\end{eqnarray}
$$

$$
\begin{eqnarray}
  \frac{1}{1+\exp(-\sum_j w_j x_j-b)}
\end{eqnarray}
$$

También usamos la función sigmoide para activar la primera capa. Es decir, cambiamos ese valor de escala de grises al rango de 0 a 1. Así que ahora, cada neurona en cada capa tiene un valor de 0 a 1.

Así que ahora para nuestra red de dos capas, la primera capa tiene 784 neuronas, y la segunda capa tiene 10 neuronas. La entrenamos para obtener los pesos y los sesgos.

Tenemos 784 * 10 pesos y 10 sesgos. En la segunda capa, para cada neurona, usaremos 784 pesos y 1 sesgo para calcular su valor. El código aquí es como,

```python
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
```

### Propagación hacia adelante (Feedforward)

> Propagación hacia adelante: Para cada l=2,3,…,L calcule $$z^{l} = w^l a^{l-1}+b^l$$ y $$a^{l} = \sigma(z^{l})$$

Nótese que aquí usamos el valor de la última capa, es decir, $$a^{l-1}$$ y el peso de la capa actual, $$w^l$$ y su sesgo $$b^l$$ para realizar la sigmoide y obtener el valor de la capa actual, $$a^{l}$$.

Código:

```python
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x]
        zs = []
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
```
### Error de salida

> Error de salida $$\delta^{L}$$: Calcule el vector $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$

Veamos qué significa $$\nabla$$.

> Del, o nabla, es un operador utilizado en matemáticas (particularmente en cálculo vectorial) como un operador diferencial vectorial, usualmente representado por el símbolo nabla ∇.

$$
\begin{eqnarray}
  w_k & \rightarrow & w_k' = w_k-\eta \frac{\partial C}{\partial w_k} \\
  b_l & \rightarrow & b_l' = b_l-\eta \frac{\partial C}{\partial b_l}
\end{eqnarray}
$$

Aquí $$\eta $$ es la tasa de aprendizaje. Usamos la derivada de C con respecto a los pesos y al sesgo, que es la tasa de cambio entre ellos. Eso es `sigmoid_prime` en lo siguiente.

Código:

```python
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
```

```python
    def cost_derivative(self, output_activations, y):
        return (output_activations-y)
```

### Retropropagación del error

> Retropropagación del error: Para cada l=L−1,L−2,…,2, calcule $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$

```python
     for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)
```

### Salida

> Salida: El gradiente de la función de costo viene dado por $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$
y $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$

```python
    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]
```

### Final

Es un artículo corto. Y en su mayor parte, solo muestra el código y la fórmula matemática. Pero para mí está bien. Antes de escribirlo, no lo entendía claramente. Después de escribir o simplemente copiar fragmentos de código y del libro, entiendo la mayor parte. Después de ganar confianza con el profesor Yin Wang, leer aproximadamente el 30% del libro *Neural Networks and Deep Learning*, escuchar las conferencias de Standford de Andrej Karpathy y los cursos de Andrew Ng, discutir con mi amigo Qi, y manipular las bibliotecas Anaconda, numpy y Theano para hacer funcionar el código de hace años, ahora lo entiendo.

Uno de los puntos clave son las dimensiones. Debemos saber las dimensiones de cada símbolo y variable. Y simplemente realiza el cómputo diferenciable. Terminemos con las citas de Yin Wang:

> El aprendizaje automático es una teoría realmente útil, incluso se podría decir que hermosa, ¡porque es simplemente cálculo después de un cambio de imagen! Es la antigua y gran teoría de Newton, Leibniz, en una forma más simple, elegante y poderosa. El aprendizaje automático es básicamente el uso del cálculo para derivar y ajustar algunas funciones, y el deep learning es el ajuste de funciones más complejas.

> No hay "inteligencia" en la inteligencia artificial, no hay "neural" en la red neuronal, no hay "aprendizaje" en el aprendizaje automático, y no hay "profundidad" en el deep learning. Lo que realmente funciona en este campo se llama "cálculo". Por eso prefiero llamar a este campo "computación diferenciable", y al proceso de construcción de modelos se le llama "programación diferenciable".