---
audio: false
generated: false
image: false
lang: es
layout: post
title: Neural Netwrok
translated: true
usemathjax: true
---

Hablemos directamente del núcleo del funcionamiento de las redes neuronales. Es decir, el algoritmo de retropropagación:

1. **Entrada x**: Establece la activación correspondiente $$a^{1}$$ para la capa de entrada.
2. **Propagación hacia adelante**: Para cada l=2,3,…,L, calcula $$z^{l} = w^l a^{l-1}+b^l$$ y $$a^{l} = \sigma(z^{l})$$.
3. **Error de salida $$\delta^{L}$$**: Calcula el vector $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$.
4. **Retropropagación del error**: Para cada l=L−1,L−2,…,2, calcula $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$.
5. **Salida**: El gradiente de la función de costo está dado por $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$ y $$\frac{\partial C}{\partial b^l_j} = \delta^l_j$$.

Esto está copiado del libro *Neural Networks and Deep Learning* de Michael Nelson. ¿Te parece abrumador? Puede serlo la primera vez que lo ves. Pero no lo será después de un mes de estudio alrededor de ello. Permíteme explicar.

## Entrada

Hay 5 fases. La primera fase es la Entrada. Aquí utilizamos dígitos escritos a mano como entrada. Nuestra tarea es reconocerlos. Un dígito escrito a mano tiene 784 píxeles, que es 28*28. En cada píxel, hay un valor de escala de grises que va de 0 a 255. La activación significa que utilizamos alguna función para activarlo, para cambiar su valor original a un nuevo valor con el fin de facilitar el procesamiento.

Digamos que ahora tenemos 1000 imágenes de 784 píxeles. Ahora entrenamos el programa para que reconozca qué dígito muestran. Tenemos 100 imágenes para probar ese efecto de aprendizaje. Si el programa puede reconocer los dígitos de 97 imágenes, decimos que su precisión es del 97%.

Entonces, iteraríamos sobre las 1000 imágenes para entrenar los pesos y los sesgos. Hacemos que los pesos y los sesgos sean más correctos cada vez que le damos una nueva imagen para que aprenda.

El resultado de un entrenamiento por lotes debe reflejarse en 10 neuronas. Aquí, las 10 neuronas representan los números del 0 al 9, y su valor varía entre 0 y 1 para indicar su confianza en la precisión de la predicción.

Y la entrada es de 784 neuronas. ¿Cómo podemos reducir 784 neuronas a 10 neuronas? Aquí está la cosa. Supongamos que tenemos dos capas. ¿Qué significa la capa? Esa es la primera capa, tenemos 784 neuronas. En la segunda capa, tenemos 10 neuronas.

Le damos a cada neurona en las 784 neuronas un peso, digamos,

$$w_1, w_2, w_3, w_4, ... , w_{784}$$

Y dale a la primera capa un sesgo, es decir, $$b_1$$.

Y así, para la primera neurona en la segunda capa, su valor es:

$$w_1*a_1 + w_2*a_2+...+ w_{784}*a_{784}+b_1$$

Pero estos pesos y un sesgo son para $$neuron^2_{1}$$ (el primero en la segunda capa). Para $$neuron^2_{2}$$, necesitamos otro conjunto de pesos y un sesgo.

¿Qué tal la función sigmoide? Usamos la función sigmoide para mapear el valor anterior de 0 a 1.

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

También utilizamos la función sigmoide para activar la primera capa. Dicho esto, transformamos ese valor de escala de grises al rango de 0 a 1. Así que ahora, cada neurona en cada capa tiene un valor entre 0 y 1.

Entonces, para nuestra red de dos capas, la primera capa tiene 784 neuronas y la segunda capa tiene 10 neuronas. La entrenamos para obtener los pesos y los sesgos.

Tenemos 784 * 10 pesos y 10 sesgos. En la segunda capa, para cada neurona, utilizaremos 784 pesos y 1 sesgo para calcular su valor. El código aquí es como,

```python
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
```

## Feedforward

El término **feedforward** se refiere a un proceso en el que la información fluye en una dirección, desde la entrada hacia la salida, sin retroalimentación. Este concepto es ampliamente utilizado en diversos campos, como la ingeniería, la inteligencia artificial y la teoría de control.

En el contexto de las redes neuronales, el **feedforward** es un tipo de arquitectura en la que las señales se mueven en una sola dirección, desde la capa de entrada, a través de las capas ocultas, hasta la capa de salida. Este tipo de red se conoce como **red neuronal feedforward** y es la base de muchas aplicaciones de aprendizaje automático.

### Ejemplo de una Red Neuronal Feedforward

```python
import numpy as np

# Definir la función de activación (sigmoide)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Definir la derivada de la función sigmoide
def sigmoid_derivative(x):
    return x * (1 - x)

# Datos de entrada
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Salidas esperadas
expected_output = np.array([[0], [1], [1], [0]])

# Inicializar pesos aleatoriamente
np.random.seed(42)
weights = np.random.rand(2, 1)

# Tasa de aprendizaje
learning_rate = 0.1

# Entrenamiento de la red
for epoch in range(10000):
    # Feedforward
    input_layer = inputs
    outputs = sigmoid(np.dot(input_layer, weights))

    # Cálculo del error
    error = expected_output - outputs

    # Ajuste de pesos usando el gradiente descendente
    adjustments = error * sigmoid_derivative(outputs)
    weights += np.dot(input_layer.T, adjustments) * learning_rate

print("Salidas después del entrenamiento:")
print(outputs)
```

En este ejemplo, la red neuronal feedforward aprende a realizar la operación XOR a través del proceso de entrenamiento. La información fluye en una sola dirección, desde la entrada hasta la salida, sin retroalimentación.

### Aplicaciones del Feedforward

- **Reconocimiento de patrones**: Las redes feedforward son ampliamente utilizadas en tareas de reconocimiento de imágenes y voz.
- **Predicción**: Se utilizan para predecir resultados basados en datos de entrada, como en modelos de regresión.
- **Clasificación**: Son eficaces en tareas de clasificación, como la detección de spam o la categorización de textos.

El feedforward es un concepto fundamental en el diseño de sistemas que requieren un flujo de información unidireccional y es la base de muchas tecnologías modernas.

> Propagación hacia adelante: Para cada l=2,3,…,L calcula $$z^{l} = w^l a^{l-1}+b^l$$ y $$a^{l} = \sigma(z^{l})$$

Observa aquí que utilizamos el valor de la última capa, es decir, $$a^{l-1}$$, junto con el peso de la capa actual, $$w^l$$, y su sesgo $$b^l$$, para aplicar la función sigmoide y obtener el valor de la capa actual, $$a^{l}$$.

Código:

```python
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # propagación hacia adelante
        activation = x
        activations = [x] 
        zs = [] 
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
```
## Error de salida

> Error de salida $$\delta^{L}$$: Calcular el vector $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$

Veamos qué significa $$\nabla$$.

> Del, o nabla, es un operador utilizado en matemáticas (especialmente en cálculo vectorial) como un operador diferencial vectorial, generalmente representado por el símbolo nabla ∇.

$$
\begin{eqnarray}
  w_k & \rightarrow & w_k' = w_k-\eta \frac{\partial C}{\partial w_k} \\
  b_l & \rightarrow & b_l' = b_l-\eta \frac{\partial C}{\partial b_l}
\end{eqnarray}
$$

Aquí $$\eta $$ es la tasa de aprendizaje. Utilizamos la derivada de C con respecto a los pesos y el sesgo, es decir, la tasa de cambio entre ellos. Esto es `sigmoid_prime` en el siguiente código.

Código:

```python
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
```

*Nota: El código proporcionado no necesita traducción, ya que es un bloque de código en Python y los nombres de variables y funciones deben mantenerse en inglés para mantener la funcionalidad del programa.*

```python
    def cost_derivative(self, output_activations, y):
        return (output_activations-y)
```

En este bloque de código, la función `cost_derivative` calcula la derivada de la función de costo con respecto a las activaciones de salida. La derivada se obtiene restando el valor objetivo `y` de las activaciones de salida `output_activations`. Este resultado se utiliza comúnmente en el proceso de retropropagación para ajustar los pesos de la red neuronal.

## Retropropagar el error

> Retropropagar el error: Para cada l=L−1,L−2,…,2, calcular $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$

```python
     for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)
```

## Salida

> Salida: El gradiente de la función de costo está dado por $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$
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

## Final

Es un artículo corto. Y en su mayor parte, solo muestra el código y la fórmula matemática. Pero para mí está bien. Antes de escribirlo, no lo entendía claramente. Después de escribirlo o simplemente copiar fragmentos de código y del libro, entiendo la mayor parte. Después de ganar confianza gracias al profesor Yin Wang, leer alrededor del 30% del libro *Neural Networks and Deep Learning*, escuchar las conferencias de Andrej Karpathy en Stanford y los cursos de Andrew Ng, discutir con mi amigo Qi, y ajustar las bibliotecas de Anaconda, numpy y Theano para hacer funcionar el código de hace años, ahora lo entiendo.

Uno de los puntos clave son las dimensiones. Debemos conocer las dimensiones de cada símbolo y variable. Y simplemente realiza el cálculo diferenciable. Terminemos con las citas de Yin Wang:

> El aprendizaje automático es realmente útil, incluso se podría decir que es una teoría hermosa, ¡porque simplemente es cálculo después de un cambio de imagen! Es la antigua y gran teoría de Newton y Leibniz, pero en una forma más simple, elegante y poderosa. Básicamente, el aprendizaje automático es el uso del cálculo para derivar y ajustar algunas funciones, y el aprendizaje profundo es el ajuste de funciones más complejas.

> No hay 'inteligencia' en la inteligencia artificial, no hay 'neural' en las redes neuronales, no hay 'aprendizaje' en el aprendizaje automático, y no hay 'profundidad' en el aprendizaje profundo. No hay 'profundidad' en el aprendizaje profundo. Lo que realmente funciona en este campo se llama 'cálculo'. Por eso prefiero llamar a este campo 'computación diferenciable', y el proceso de construir modelos se llama 'programación diferenciable'.