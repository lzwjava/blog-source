---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Ejemplo Simple de RNN con PyTorch
translated: true
type: note
---

### Ejemplo Simple de RNN en PyTorch

Las Redes Neuronales Recurrentes (RNNs) son excelentes para manejar datos secuenciales como series de tiempo o texto. Aquí hay un ejemplo básico usando PyTorch para construir una RNN simple para clasificar secuencias (por ejemplo, clasificación binaria en secuencias aleatorias). Esto asume que tienes PyTorch instalado (`import torch` e `import torch.nn as nn`).

```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Hiperparámetros
input_size = 1      # Tamaño de la característica (ej., serie de tiempo univariada)
hidden_size = 32    # Tamaño del estado oculto
output_size = 1     # Salida binaria (sigmoide para clasificación)
sequence_length = 10  # Longitud de cada secuencia
batch_size = 32
num_epochs = 10

# Generar datos dummy: secuencias de longitud 10, etiquetas basadas en la suma (binaria)
def generate_data(num_samples):
    X = torch.randn(num_samples, sequence_length, input_size)
    y = (torch.sum(X, dim=1) > 0).float().unsqueeze(1)
    return X, y

# Modelo RNN Simple
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        # forma de x: (batch, seq_len, input_size)
        h0 = torch.zeros(1, x.size(0), self.hidden_size)  # Estado oculto inicial
        out, _ = self.rnn(x, h0)
        # Tomar la última salida para la clasificación
        out = self.fc(out[:, -1, :])  # Último paso de tiempo
        return self.sigmoid(out)

# Inicializar modelo, pérdida, optimizador
model = SimpleRNN(input_size, hidden_size, output_size)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Bucle de entrenamiento
num_samples = 1000
X, y = generate_data(num_samples)
dataset = torch.utils.data.TensorDataset(X, y)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

for epoch in range(num_epochs):
    for batch_X, batch_y in dataloader:
        optimizer.zero_grad()
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Ejemplo de inferencia
test_seq = torch.randn(1, sequence_length, input_size)
prediction = model(test_seq)
print(f'Prediction: {prediction.item():.4f}')
```

#### Cómo Funciona:
- **Generación de Datos**: Crea secuencias aleatorias de longitud 10 con una etiqueta binaria (1 si la suma > 0, si no 0).
- **Modelo**: Usa `nn.RNN` (celda RNN básica). El pase hacia adelante procesa la secuencia paso a paso, usando el último estado oculto para la salida.
- **Entrenamiento**: Bucle estándar de PyTorch con pérdida BCE para clasificación binaria.
- **Salida**: La activación sigmoide da una probabilidad entre 0 y 1.

Esta es una RNN básica; para un mejor rendimiento en secuencias largas, considera las variantes LSTM o GRU (por ejemplo, reemplaza `nn.RNN` con `nn.LSTM`).

### Variante LSTM (Extensión Rápida)
Para los gradientes que se desvanecen, cámbiate a LSTM:

```python
# En la clase del modelo, reemplaza:
self.rnn = nn.LSTM(input_size, hidden_size, batch_first=True)

# Y en forward:
h0 = torch.zeros(1, x.size(0), self.hidden_size)
c0 = torch.zeros(1, x.size(0), self.hidden_size)  # LSTM necesita estado de celda
out, (hn, cn) = self.rnn(x, (h0, c0))
```

¡Ejecuta esto en un entorno de PyTorch para experimentar!

[Documentación de RNN en PyTorch](https://pytorch.org/docs/stable/generated/torch.nn.RNN.html)  
[Documentación de LSTM en PyTorch](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)