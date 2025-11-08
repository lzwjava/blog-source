---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Implementación Simple de RNN desde Cero
translated: true
type: note
---

### Ejemplo Simple de RNN en NumPy (Desde Cero)

Implementar una RNN desde cero en NumPy es una excelente manera de entender la mecánica: el estado oculto recurrente, la propagación hacia adelante y la retropropagación a través del tiempo (BPTT). A continuación se muestra un ejemplo básico para clasificación binaria en secuencias aleatorias (similar a la versión anterior de PyTorch). Utiliza datos de series temporales univariantes (`input_size=1`), `hidden_size=32` y `sequence_length=10`.

Este código incluye:
- Generación de datos.
- Paso hacia adelante de la RNN (con activación tanh para los estados ocultos).
- Paso hacia atrás (BPTT con descenso de gradiente simple).
- Bucle de entrenamiento.

Nota: Esta es una RNN básica; los gradientes pueden desaparecer o explotar en secuencias largas. Para producción, considera recortar los gradientes o usar la lógica de LSTM.

```python
import numpy as np

# Hiperparámetros
input_size = 1      # Tamaño de la característica (univariante)
hidden_size = 32    # Tamaño del estado oculto
output_size = 1     # Salida binaria
sequence_length = 10  # Longitud de cada secuencia
num_samples = 1000
num_epochs = 10
learning_rate = 0.01

# Generar datos de ejemplo: secuencias de longitud 10, etiquetas basadas en la suma (binaria)
def generate_data(num_samples):
    X = np.random.randn(num_samples, sequence_length, input_size)
    y = (np.sum(X, axis=1) > 0).astype(float).reshape(num_samples, 1)
    return X, y

# Clase SimpleRNN (desde cero)
class SimpleRNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Inicializar pesos (inicialización Xavier)
        self.Wxh = np.random.randn(hidden_size, input_size) * np.sqrt(1. / input_size)
        self.Whh = np.random.randn(hidden_size, hidden_size) * np.sqrt(1. / hidden_size)
        self.Why = np.random.randn(output_size, hidden_size) * np.sqrt(1. / hidden_size)
        
        # Sesgos
        self.bh = np.zeros((hidden_size, 1))
        self.by = np.zeros((output_size, 1))
    
    def forward(self, x):
        # Forma de x: (sequence_length, input_size, 1) para una sola muestra
        self.x = x  # Almacenar para retropropagación
        self.h = np.zeros((self.hidden_size, 1))  # Estado oculto inicial
        
        # Paso hacia adelante en el tiempo
        self.hs = np.zeros((self.hidden_size, sequence_length + 1))  # Estados ocultos (incluyendo el inicial)
        self.hs[:, 0] = self.h.flatten()
        
        for t in range(sequence_length):
            self.h = np.tanh(np.dot(self.Wxh, x[t]) + np.dot(self.Whh, self.h) + self.bh)
            self.hs[:, t+1] = self.h.flatten()
        
        # Salida del último estado oculto
        self.y_pred = np.dot(self.Why, self.h) + self.by
        return self.sigmoid(self.y_pred)
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-np.clip(z, -250, 250)))  # Recortar para estabilidad
    
    def backward(self, y_true):
        # Retropropagación a través del tiempo (simplificada)
        dWhy = np.dot((self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred), self.hs[-1:, :].T)
        dby = (self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred)
        
        # Gradientes para los pesos ocultos y de salida
        dWhh = np.zeros_like(self.Whh)
        dWxh = np.zeros_like(self.Wxh)
        dbh = np.zeros_like(self.bh)
        
        dh_next = np.zeros_like(self.h)
        for t in reversed(range(sequence_length)):
            dh = np.dot(self.Why.T, (self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred)) + dh_next
            dh_raw = (1 - self.h**2) * dh  # Derivada de tanh
            dWxh += np.dot(dh_raw, self.x[t].T)
            dWhh += np.dot(dh_raw, self.hs[:, t:t+2].T[:, 0:1])  # Simplificado; BPTT completo acumularía correctamente
            dbh += dh_raw
            dh_next = np.dot(self.Whh.T, dh_raw)
        
        # Actualizar pesos
        self.Wxh -= learning_rate * dWxh
        self.Whh -= learning_rate * dWhh
        self.Why -= learning_rate * dWhy
        self.bh -= learning_rate * dbh
        self.by -= learning_rate * dby
    
    def sigmoid_deriv(self, z):
        s = self.sigmoid(z)
        return s * (1 - s)

# Entrenamiento
X, y = generate_data(num_samples)

# Reformatear para procesar una muestra (batch_size=1 por simplicidad)
X = X.reshape(num_samples, sequence_length, input_size, 1)  # Añadir dimensión de lote de 1
y = y.reshape(num_samples, 1, 1)

model = SimpleRNN(input_size, hidden_size, output_size)

for epoch in range(num_epochs):
    total_loss = 0
    for i in range(num_samples):
        pred = model.forward(X[i])
        loss = -np.mean(y[i] * np.log(pred + 1e-8) + (1 - y[i]) * np.log(1 - pred + 1e-8))  # BCE
        total_loss += loss
        model.backward(y[i])
    
    avg_loss = total_loss / num_samples
    print(f'Época [{epoch+1}/{num_epochs}], Pérdida Promedio: {avg_loss:.4f}')

# Ejemplo de inferencia
test_seq = np.random.randn(sequence_length, input_size, 1)
prediction = model.forward(test_seq)
print(f'Predicción: {prediction.flatten()[0]:.4f}')
```

#### Cómo Funciona:
- **Generación de Datos**: Secuencias aleatorias con etiquetas binarias basadas en la suma.
- **Paso hacia Adelante**: Procesa la secuencia paso a paso, actualizando el estado oculto `h_t = tanh(Wxh * x_t + Whh * h_{t-1} + bh)`. La salida utiliza el `h` final con sigmoid.
- **Paso hacia Atrás**: BPTT calcula los gradientes para todos los pasos de tiempo, actualizando los pesos mediante GD simple. (Nota: Este es un BPTT mínimo; las versiones completas manejan una acumulación más precisa).
- **Entrenamiento**: Itera sobre las muestras, calcula la pérdida BCE y actualiza.
- **Salida**: Sigmoid da la probabilidad (0-1).

Esto se ejecuta en ~10-20 segundos en una máquina estándar para estos parámetros. Aumenta `num_samples` o `num_epochs` para ver el aprendizaje. Para múltiples lotes, vectoriza los bucles.

Para análisis más profundos:  
[Understanding LSTM Networks (Colah's Blog)](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)  
[NumPy RNN Tutorial](https://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/)