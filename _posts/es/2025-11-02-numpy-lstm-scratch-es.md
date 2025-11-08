---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Implementación de LSTM con NumPy desde Cero
translated: true
type: note
---

Esta es una implementación básica de una red de memoria a largo plazo (LSTM) utilizando únicamente NumPy, inspirada en los conceptos de la publicación del blog de Christopher Olah "Understanding LSTM Networks". Incluye las compuertas principales (olvido, entrada, celda candidata y salida) y se centra en el pase hacia adelante. La clase maneja un único paso de tiempo mediante `forward()` y una secuencia completa mediante `forward_sequence()`.

Los pesos se inicializan aleatoriamente (en la práctica, utilice una inicialización mejor como Xavier/Glorot). No se incluye el pase hacia atrás ni el entrenamiento aquí—extiéndalo con retropropagación a través del tiempo (BPTT) para eso.

```python
import numpy as np

class LSTM:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        # Inicializar pesos y sesgos para las compuertas de olvido, entrada, celda y salida
        self.Wf = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wi = np.random.randn(hidden_size, hidden_size + input_size)
        self.WC = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wo = np.random.randn(hidden_size, hidden_size + input_size)
        self.bf = np.zeros((hidden_size, 1))
        self.bi = np.zeros((hidden_size, 1))
        self.bC = np.zeros((hidden_size, 1))
        self.bo = np.zeros((hidden_size, 1))

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def tanh(self, z):
        return np.tanh(z)

    def forward(self, x, h_prev, C_prev):
        # x: (input_size, 1), h_prev y C_prev: (hidden_size, 1)
        # Concatenar el estado oculto y la entrada
        concat = np.vstack((h_prev, x))
        # Compuerta de olvido
        f_t = self.sigmoid(np.dot(self.Wf, concat) + self.bf)
        # Compuerta de entrada
        i_t = self.sigmoid(np.dot(self.Wi, concat) + self.bi)
        C_tilda = self.tanh(np.dot(self.WC, concat) + self.bC)
        # Actualización del estado de celda
        C_t = f_t * C_prev + i_t * C_tilda
        # Compuerta de salida
        o_t = self.sigmoid(np.dot(self.Wo, concat) + self.bo)
        # Actualización del estado oculto
        h_t = o_t * self.tanh(C_t)
        return h_t, C_t

    def forward_sequence(self, X):
        # X: (seq_len, input_size)
        h = np.zeros((self.hidden_size, 1))
        C = np.zeros((self.hidden_size, 1))
        outputs = []
        for x in X:
            h, C = self.forward(x.reshape(-1, 1), h, C)
            outputs.append(h)
        return np.hstack(outputs).T  # Devuelve (seq_len, hidden_size)

# Ejemplo de uso
input_size = 3
hidden_size = 5
lstm = LSTM(input_size, hidden_size)

# Paso único
x_t = np.random.randn(input_size, 1)
h_prev = np.zeros((hidden_size, 1))
C_prev = np.zeros((hidden_size, 1))
h_t, C_t = lstm.forward(x_t, h_prev, C_prev)
print("Paso único - Forma del estado oculto:", h_t.shape)

# Secuencia
X = np.random.randn(4, input_size)  # seq_len=4
outputs = lstm.forward_sequence(X)
print("Forma de las salidas de la secuencia:", outputs.shape)
```

### Explicación Rápida
- **Inicialización**: Los pesos conectan la entrada concatenada (estado oculto anterior + entrada actual) a cada compuerta. Los sesgos se inicializan en cero.
- **Compuertas**:
  - **Compuerta de olvido** (`f_t`): Decide qué olvidar del estado de celda anterior (sigmoid: 0-1).
  - **Compuerta de entrada** (`i_t`) y **celda candidata** (`C_tilda`): Deciden qué nueva información añadir (sigmoid + tanh).
  - **Compuerta de salida** (`o_t`): Filtra el estado de celda para producir el estado oculto (sigmoid + tanh en la celda).
- **Estado de celda** (`C_t`): Flujo lineal con actualizaciones aditivas para la memoria a largo plazo.
- **Uso**: Para secuencias, recorra los pasos de tiempo, actualizando los estados ocultos y de celda progresivamente.

Esto coincide con la arquitectura LSTM del blog de Colah: el estado de celda como una "carretera" controlada por compuertas.

[Understanding LSTMs: Implementation from Scratch](https://medium.com/@samina.amin/understanding-lstms-lstm-implementation-from-scratch-18965a150eca)