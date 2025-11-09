---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast:free
title: Ejemplo de Implementación LoRA con PyTorch
translated: true
type: note
---

A continuación se muestra un ejemplo de código Python que demuestra cómo implementar LoRA (Low-Rank Adaptation) usando PyTorch para el fine-tuning de una red neuronal simple. Este ejemplo se centra en adaptar una capa lineal pre-entrenada con LoRA, manteniendo los pesos originales congelados e introduciendo matrices de actualización de bajo rango. El código incluye una configuración básica con un dataset de juguete y un bucle de entrenamiento mínimo para ilustrar el concepto.

<xaiArtifact artifact_id="1327e99b-24b5-4b0d-9ffd-5b4c2d1472af" artifact_version_id="4053525d-2225-4913-a3b9-b7d66b48daea" title="lora_demo.py" contentType="text/python">
import torch
import torch.nn as nn
import torch.optim as optim

# Definir la capa LoRA
class LoRALayer(nn.Module):
    def __init__(self, in_features, out_features, rank=4):
        super(LoRALayer, self).__init__()
        # Pesos originales congelados
        self.linear = nn.Linear(in_features, out_features)
        self.linear.weight.requires_grad = False  # Congelar pesos originales
        # Parámetros LoRA: matrices de bajo rango A y B
        self.lora_A = nn.Parameter(torch.randn(in_features, rank))
        self.lora_B = nn.Parameter(torch.randn(rank, out_features))
        self.scaling = 1.0  # Factor de escala para las actualizaciones LoRA

    def forward(self, x):
        # Transformación lineal original + ajuste LoRA
        original = self.linear(x)
        lora_adjustment = self.scaling * torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)
        return original + lora_adjustment

# Dataset de juguete para demostración
def create_toy_dataset(n_samples=1000):
    X = torch.randn(n_samples, 64)  # Características de entrada aleatorias
    y = torch.randn(n_samples, 10)  # Salidas objetivo aleatorias
    return X, y

# Función de entrenamiento
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

# Ejecución principal
def main():
    # Establecer semilla aleatoria para reproducibilidad
    torch.manual_seed(42)
    
    # Crear dataset de juguete
    X, y = create_toy_dataset()
    
    # Inicializar modelo con LoRA
    model = LoRALayer(in_features=64, out_features=10, rank=4)
    
    # Contar parámetros entrenables
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Trainable parameters: {trainable_params}")
    print(f"Total parameters: {total_params}")
    
    # Entrenar el modelo
    train_model(model, X, y)

if __name__ == "__main__":
    main()
</xaiArtifact>

Este código define una `LoRALayer` que envuelve una capa lineal estándar con matrices de adaptación de bajo rango (`lora_A` y `lora_B`). Los pesos originales se congelan y solo los parámetros LoRA se actualizan durante el entrenamiento. El dataset de juguete y el bucle de entrenamiento demuestran cómo LoRA reduce el número de parámetros entrenables mientras aún permite el fine-tuning. Puedes ejecutar este código con PyTorch instalado para ver el proceso de entrenamiento y la eficiencia de parámetros en acción.

[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)