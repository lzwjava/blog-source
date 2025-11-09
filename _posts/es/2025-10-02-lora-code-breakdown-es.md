---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast:free
title: Desglose y Explicación del Código LoRA
translated: true
type: note
---

Desglosaré el código de demostración de LoRA en partes clave, explicando cada una en detalle antes de pasar a la siguiente. Esto ayudará a ilustrar cómo funciona LoRA de manera clara y paso a paso. El código se basa en el ejemplo anterior, utilizando PyTorch para implementar LoRA en una capa lineal simple.

### Fragmento de Código 1: Definición de la Capa LoRA
```python
import torch
import torch.nn as nn

class LoRALayer(nn.Module):
    def __init__(self, in_features, out_features, rank=4):
        super(LoRALayer, self).__init__()
        # Pesos originales congelados
        self.linear = nn.Linear(in_features, out_features)
        self.linear.weight.requires_grad = False  # Congelar pesos originales
        # Parámetros LoRA: matrices de bajo rango A y B
        self.lora_A = nn.Parameter(torch.randn(in_features, rank))
        self.lora_B = nn.Parameter(torch.randn(rank, out_features))
        self.scaling = 1.0  # Factor de escala para las actualizaciones de LoRA
```

#### Explicación
Este fragmento define la clase `LoRALayer`, que implementa la técnica LoRA. Esto es lo que sucede:

- **Importaciones y Configuración de la Clase**: Importamos PyTorch (`torch`) y su módulo de red neuronal (`nn`). La clase `LoRALayer` hereda de `nn.Module`, lo que la convierte en un módulo de PyTorch que puede integrarse en modelos más grandes.
- **Capa Lineal Original**: `self.linear = nn.Linear(in_features, out_features)` crea una capa lineal estándar (como una capa completamente conectada en una red neuronal) con `in_features` entradas y `out_features` salidas. Esto representa los pesos preentrenados que queremos adaptar.
- **Congelar Pesos**: `self.linear.weight.requires_grad = False` congela los pesos originales de la capa lineal, asegurando que no se actualicen durante el entrenamiento. Esto es clave para la eficiencia de LoRA, ya que evita modificar el modelo preentrenado grande.
- **Parámetros LoRA**: `self.lora_A` y `self.lora_B` son matrices de bajo rango. `lora_A` tiene forma `(in_features, rank)`, y `lora_B` tiene forma `(rank, out_features)`. El parámetro `rank` (por defecto=4) controla el tamaño de estas matrices, manteniéndolas mucho más pequeñas que la matriz de pesos original (forma `in_features x out_features`). Estas matrices son entrenables (`nn.Parameter`) e inicializadas con valores aleatorios (`torch.randn`).
- **Factor de Escala**: `self.scaling = 1.0` es un hiperparámetro para escalar el ajuste de LoRA, permitiendo un ajuste fino de la fuerza de la adaptación.

Esta configuración asegura que solo las pequeñas matrices `lora_A` y `lora_B` se actualicen durante el entrenamiento, reduciendo drásticamente el número de parámetros entrenables.

---

### Fragmento de Código 2: Paso Forward de LoRA
```python
    def forward(self, x):
        # Transformación lineal original + ajuste LoRA
        original = self.linear(x)
        lora_adjustment = self.scaling * torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)
        return original + lora_adjustment
```

#### Explicación
Este fragmento define el paso forward de la `LoRALayer`, que calcula la salida de la capa:

- **Entrada**: La entrada `x` es un tensor de forma `(batch_size, in_features)`, que representa un lote de datos de entrada.
- **Salida Original**: `original = self.linear(x)` calcula la salida de la capa lineal congelada, aplicando los pesos preentrenados a la entrada.
- **Ajuste LoRA**: El término `torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)` calcula la adaptación de bajo rango. Primero, `x` se multiplica por `lora_A` (forma `in_features x rank`), produciendo un tensor de forma `(batch_size, rank)`. Luego, esto se multiplica por `lora_B` (forma `rank x out_features`), dando un tensor de forma `(batch_size, out_features)`—la misma forma que la salida original. Este ajuste representa la actualización específica de la tarea.
- **Escalado y Combinación**: El ajuste se escala por `self.scaling` y se añade a la salida original, produciendo la salida final. Esto asegura que el modelo retenga el conocimiento preentrenado mientras incorpora adaptaciones específicas de la tarea.

La estructura de bajo rango (`rank` es pequeño, ej. 4) asegura que el ajuste sea computacionalmente barato y eficiente en parámetros en comparación con actualizar la matriz de pesos completa.

---

### Fragmento de Código 3: Conjunto de Datos de Juguete y Entrenamiento
```python
def create_toy_dataset(n_samples=1000):
    X = torch.randn(n_samples, 64)  # Características de entrada aleatorias
    y = torch.randn(n_samples, 10)  # Salidas objetivo aleatorias
    return X, y

def train_model(model, X, y, epochs=10, lr=0.01):
    criterion = nn.MSELoss()
    optimizer = optim.Adam([param for param in model.parameters() if param.requires_grad], lr=lr)
    
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")
```

#### Explicación
Este fragmento crea un conjunto de datos de juguete y entrena el modelo adaptado con LoRA:

- **Conjunto de Datos de Juguete**: La función `create_toy_dataset` genera datos sintéticos para la demostración. `X` es un tensor de forma `(1000, 64)` (1000 muestras, 64 características), e `y` es un tensor de forma `(1000, 10)` (1000 muestras, 10 dimensiones de salida). Estos son tensores aleatorios para simular pares entrada-salida.
- **Función de Entrenamiento**: La función `train_model` configura un bucle de entrenamiento simple:
  - **Función de Pérdida**: `nn.MSELoss()` define el error cuadrático medio como la pérdida, adecuado para esta tarea de juguete similar a una regresión.
  - **Optimizador**: `optim.Adam` optimiza solo los parámetros entrenables (`param.requires_grad` es `True`), que son `lora_A` y `lora_B`. El `linear.weight` congelado se excluye, asegurando eficiencia.
  - **Bucle de Entrenamiento**: Para cada época, el modelo calcula las salidas, calcula la pérdida, realiza la retropropagación (`loss.backward()`) y actualiza los parámetros de LoRA (`optimizer.step()`). La pérdida se imprime para monitorear el progreso del entrenamiento.

Esta configuración demuestra cómo LoRA ajusta finamente solo las matrices de bajo rango, manteniendo el proceso ligero.

---

### Fragmento de Código 4: Ejecución Principal y Conteo de Parámetros
```python
def main():
    # Establecer semilla aleatoria para reproducibilidad
    torch.manual_seed(42)
    
    # Crear conjunto de datos de juguete
    X, y = create_toy_dataset()
    
    # Inicializar modelo con LoRA
    model = LoRALayer(in_features=64, out_features=10, rank=4)
    
    # Contar parámetros entrenables
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Parámetros entrenables: {trainable_params}")
    print(f"Parámetros totales: {total_params}")
    
    # Entrenar el modelo
    train_model(model, X, y)

if __name__ == "__main__":
    main()
```

#### Explicación
Este fragmento une todo y resalta la eficiencia de LoRA:

- **Semilla Aleatoria**: `torch.manual_seed(42)` asegura la reproducibilidad de las inicializaciones aleatorias.
- **Conjunto de Datos y Modelo**: Se crea el conjunto de datos de juguete y se inicializa un `LoRALayer` con `in_features=64`, `out_features=10` y `rank=4`.
- **Conteo de Parámetros**: El código calcula:
  - **Parámetros entrenables**: Solo `lora_A` (64 × 4 = 256) y `lora_B` (4 × 10 = 40), totalizando 296 parámetros.
  - **Parámetros totales**: Incluye el `linear.weight` congelado (64 × 10 = 640) y `linear.bias` (10), más los parámetros de LoRA, totalizando 946.
  - Esto muestra la eficiencia de LoRA: solo ~31% (296/946) de los parámetros son entrenables, en comparación con el 100% en el ajuste fino completo.
- **Entrenamiento**: Se llama a la función `train_model` para ajustar finamente los parámetros de LoRA en el conjunto de datos de juguete.

Cuando ejecutes esto, verás que el número de parámetros entrenables es mucho menor que el total, y el modelo se entrena rápidamente debido a las actualizaciones de bajo rango.

---

### Ejecutar el Código
Para ejecutar esto, necesitas tener PyTorch instalado (`pip install torch`). Guarda el código completo en un archivo `.py` y ejecútalo. La salida mostrará el número de parámetros y la pérdida de entrenamiento a lo largo de 10 épocas, demostrando la eficiencia de LoRA en el ajuste fino.

[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

¡Házme saber si te gustaría profundizar en alguna parte o modificar el ejemplo!