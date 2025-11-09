---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Exemple d'implémentation LoRA avec PyTorch
translated: true
type: note
---

Voici un exemple de code Python démontrant comment implémenter LoRA (Low-Rank Adaptation) en utilisant PyTorch pour le fine-tuning d'un réseau de neurones simple. Cet exemple se concentre sur l'adaptation d'une couche linéaire pré-entraînée avec LoRA, en gardant les poids originaux gelés et en introduisant des matrices de mise à jour de faible rang. Le code inclut une configuration de base avec un jeu de données jouet et une boucle d'entraînement minimale pour illustrer le concept.

<xaiArtifact artifact_id="1327e99b-24b5-4b0d-9ffd-5b4c2d1472af" artifact_version_id="4053525d-2225-4913-a3b9-b7d66b48daea" title="lora_demo.py" contentType="text/python">
import torch
import torch.nn as nn
import torch.optim as optim

# Définir la couche LoRA
class LoRALayer(nn.Module):
    def __init__(self, in_features, out_features, rank=4):
        super(LoRALayer, self).__init__()
        # Poids originaux gelés
        self.linear = nn.Linear(in_features, out_features)
        self.linear.weight.requires_grad = False  # Geler les poids originaux
        # Paramètres LoRA : matrices de faible rang A et B
        self.lora_A = nn.Parameter(torch.randn(in_features, rank))
        self.lora_B = nn.Parameter(torch.randn(rank, out_features))
        self.scaling = 1.0  # Facteur d'échelle pour les mises à jour LoRA

    def forward(self, x):
        # Transformation linéaire originale + ajustement LoRA
        original = self.linear(x)
        lora_adjustment = self.scaling * torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)
        return original + lora_adjustment

# Jeu de données jouet pour démonstration
def create_toy_dataset(n_samples=1000):
    X = torch.randn(n_samples, 64)  # Caractéristiques d'entrée aléatoires
    y = torch.randn(n_samples, 10)  # Sorties cibles aléatoires
    return X, y

# Fonction d'entraînement
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

# Exécution principale
def main():
    # Définir la graine aléatoire pour la reproductibilité
    torch.manual_seed(42)
    
    # Créer le jeu de données jouet
    X, y = create_toy_dataset()
    
    # Initialiser le modèle avec LoRA
    model = LoRALayer(in_features=64, out_features=10, rank=4)
    
    # Compter les paramètres entraînables
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Paramètres entraînables: {trainable_params}")
    print(f"Paramètres totaux: {total_params}")
    
    # Entraîner le modèle
    train_model(model, X, y)

if __name__ == "__main__":
    main()
</xaiArtifact>

Ce code définit une `LoRALayer` qui encapsule une couche linéaire standard avec des matrices d'adaptation de faible rang (`lora_A` et `lora_B`). Les poids originaux sont gelés, et seuls les paramètres LoRA sont mis à jour pendant l'entraînement. Le jeu de données jouet et la boucle d'entraînement démontrent comment LoRA réduit le nombre de paramètres entraînables tout en permettant toujours le fine-tuning. Vous pouvez exécuter ce code avec PyTorch installé pour observer le processus d'entraînement et l'efficacité des paramètres en action.

[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)