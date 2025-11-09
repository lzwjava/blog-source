---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: Implementierungsbeispiel für LoRA mit PyTorch
translated: true
type: note
---

Hier folgt ein Python-Codebeispiel, das demonstriert, wie LoRA (Low-Rank Adaptation) mit PyTorch zur Feinabstimmung eines einfachen neuronalen Netzwerks implementiert werden kann. Dieses Beispiel konzentriert sich auf die Anpassung einer vortrainierten linearen Schicht mit LoRA, wobei die ursprünglichen Gewichte eingefroren bleiben und Low-Rank-Aktualisierungsmatrizen eingeführt werden. Der Code enthält einen grundlegenden Aufbau mit einem Toy-Datensatz und eine minimale Trainingsschleife, um das Konzept zu veranschaulichen.

<xaiArtifact artifact_id="1327e99b-24b5-4b0d-9ffd-5b4c2d1472af" artifact_version_id="4053525d-2225-4913-a3b9-b7d66b48daea" title="lora_demo.py" contentType="text/python">
import torch
import torch.nn as nn
import torch.optim as optim

# LoRA-Schicht definieren
class LoRALayer(nn.Module):
    def __init__(self, in_features, out_features, rank=4):
        super(LoRALayer, self).__init__()
        # Ursprüngliche eingefrorene Gewichte
        self.linear = nn.Linear(in_features, out_features)
        self.linear.weight.requires_grad = False  # Ursprüngliche Gewichte einfrieren
        # LoRA-Parameter: Low-Rank-Matrizen A und B
        self.lora_A = nn.Parameter(torch.randn(in_features, rank))
        self.lora_B = nn.Parameter(torch.randn(rank, out_features))
        self.scaling = 1.0  # Skalierungsfaktor für LoRA-Updates

    def forward(self, x):
        # Ursprüngliche lineare Transformation + LoRA-Anpassung
        original = self.linear(x)
        lora_adjustment = self.scaling * torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)
        return original + lora_adjustment

# Toy-Datensatz zur Demonstration
def create_toy_dataset(n_samples=1000):
    X = torch.randn(n_samples, 64)  # Zufällige Eingabemerkmale
    y = torch.randn(n_samples, 10)  # Zufällige Zielausgaben
    return X, y

# Trainingsfunktion
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

# Hauptausführung
def main():
    # Zufälligen Seed für Reproduzierbarkeit setzen
    torch.manual_seed(42)
    
    # Toy-Datensatz erstellen
    X, y = create_toy_dataset()
    
    # Modell mit LoRA initialisieren
    model = LoRALayer(in_features=64, out_features=10, rank=4)
    
    # Trainierbare Parameter zählen
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Trainable parameters: {trainable_params}")
    print(f"Total parameters: {total_params}")
    
    # Das Modell trainieren
    train_model(model, X, y)

if __name__ == "__main__":
    main()
</xaiArtifact>

Dieser Code definiert eine `LoRALayer`, die eine Standard-Linearschicht mit Low-Rank-Adaptierungsmatrizen (`lora_A` und `lora_B`) umschließt. Die ursprünglichen Gewichte sind eingefroren, und nur die LoRA-Parameter werden während des Trainings aktualisiert. Der Toy-Datensatz und die Trainingsschleife demonstrieren, wie LoRA die Anzahl der trainierbaren Parameter reduziert und dennoch eine Feinabstimmung ermöglicht. Sie können diesen Code mit installiertem PyTorch ausführen, um den Trainingsprozess und die Parameter-Effizienz in Aktion zu sehen.

[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)