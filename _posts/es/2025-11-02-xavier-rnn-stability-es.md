---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Inicialización Xavier para la Estabilidad de RNN
translated: true
type: note
---

### ¿Por qué la Inicialización Xavier en RNNs?

Las RNNs (Redes Neuronales Recurrentes) dependen de la inicialización Xavier (también llamada Glorot) para sus matrices de pesos—como `Wxh` (entrada-a-oculta), `Whh` (oculta-a-oculta, los pesos recurrentes) y `Why` (oculta-a-salida)—para mantener una dinámica de entrenamiento estable. La forma específica en tu código utiliza una distribución Gaussiana (normal) escalada por `sqrt(1 / fan_in)`, donde `fan_in` es el número de neuronas de entrada a esa capa. Esto mantiene la varianza de los pesos alrededor de `1 / fan_in`, asegurando que las señales entrantes no se amplifiquen o compriman de forma demasiado agresiva.

He aquí por qué esto es crucial para las RNNs, y por qué una simple extracción aleatoria uniforme de [0, 1] causaría problemas:

#### 1. **Preservar la Varianza de la Señal a través de Capas y Pasos de Tiempo**
   - En las redes feedforward, Xavier ayuda a mantener la *varianza de las activaciones* aproximadamente constante a medida que las señales se propagan hacia adelante (y los gradientes hacia atrás). Sin ella, las capas profundas podrían ver explotar las activaciones (volverse enormes) o desaparecer (caer a casi cero), haciendo imposible el entrenamiento.
   - Las RNNs son como redes "profundas" *desplegadas en el tiempo*: El peso recurrente `Whh` multiplica el estado oculto en cada paso de tiempo, creando una cadena de multiplicaciones (por ejemplo, para una longitud de secuencia *T*, es como *T* capas de profundidad). Si los pesos en `Whh` tienen una varianza >1, los gradientes explotan exponencialmente hacia atrás (malo para secuencias largas). Si es <1, desaparecen.
   - El escalado de Xavier (por ejemplo, `* sqrt(1. / hidden_size)` para `Whh`) asegura que la varianza esperada del estado oculto se mantenga ~1, previniendo esto. Para una inicialización uniforme [0,1]:
     - Media ~0.5 (sesgada positivamente, causando derivas).
     - Varianza ~1/12 ≈ 0.083—demasiado pequeña para un `hidden_size` grande (por ejemplo, 512), lo que lleva a que las señales desaparezcan rápidamente.

#### 2. **Adaptarse a las Dimensiones de la Capa**
   - Xavier tiene en cuenta *fan_in* (entradas a la capa) y a veces *fan_out* (salidas). Para `Wxh`, escalar por `sqrt(1 / input_size)` normaliza en función del tamaño del vocabulario o las dimensiones de embedding. Para `Whh`, se basa en `hidden_size` para coincidir con el bucle recurrente.
   - [0,1] ignora las dimensiones: En una capa oculta grande (por ejemplo, 1000 unidades), sumar muchas entradas [0,1] sin escalar abrumaría la siguiente capa. En capas pequeñas, causaría subflujo.

#### 3. **Flujo de Gradientes en la Retropropagación a través del Tiempo (BPTT)**
   - El entrenamiento de RNNs utiliza BPTT, donde los gradientes fluyen hacia atrás a lo largo de *T* pasos. Una mala inicialización conduce al "problema del gradiente vanishing" (común en RNNs vanilla, por qué existen LSTMs/GRUs). Xavier mitiga esto comenzando con magnitudes equilibradas.
   - Estudios empíricos (por ejemplo, el artículo original de Glorot & Bengio) muestran que Xavier reduce las épocas necesarias para la convergencia en 2-10x en redes profundas/recurrentes.

#### Alternativas y Cuándo [0,1] Podría "Funcionar"
- [0,1] podría "funcionar" para modelos de juguete muy pequeños (por ejemplo, una sola capa, secuencias cortas) pero falla a escala—piensa en pérdidas que explotan o NaNs.
- Ajustes modernos: Inicialización He (para ReLUs, escala por `sqrt(2 / fan_in)`) o inicialización ortogonal (para RNNs, preserva las normas exactamente). Pero Xavier es un valor por defecto seguro para activaciones sigmoid/tanh comunes en RNNs.

En resumen, Xavier se trata de *estabilidad primero*: Establece los pesos pequeños-pero-no-demasiado-pequeños, consciente de las dimensiones, para permitir que los gradientes fluyan libremente. Aleatorio [0,1] es demasiado crudo—como pisar el acelerador de un coche sin equilibrar las ruedas.

Para análisis más profundos:  
[Understanding the Difficulty of Training Deep Feedforward Neural Networks](http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf) (Glorot & Bengio, 2010)  
[Recurrent Neural Network Regularization](https://arxiv.org/abs/1409.2329) (Zaremba et al., sobre problemas de inicialización en RNNs)