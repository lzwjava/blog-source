---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Exemple Simple de RNN avec PyTorch
translated: true
type: note
---

### Exemple simple de RNN avec PyTorch

Les réseaux de neurones récurrents (RNN) sont excellents pour traiter des données séquentielles comme les séries temporelles ou le texte. Voici un exemple basique utilisant PyTorch pour construire un RNN simple destiné à classer des séquences (par exemple, classification binaire sur des séquences aléatoires). Ceci suppose que PyTorch est installé (`import torch` et `import torch.nn as nn`).

```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Hyperparamètres
input_size = 1      # Taille des caractéristiques (ex: série temporelle univariée)
hidden_size = 32    # Taille de l'état caché
output_size = 1     # Sortie binaire (sigmoid pour la classification)
sequence_length = 10  # Longueur de chaque séquence
batch_size = 32
num_epochs = 10

# Générer des données factices : séquences de longueur 10, étiquettes basées sur la somme (binaire)
def generate_data(num_samples):
    X = torch.randn(num_samples, sequence_length, input_size)
    y = (torch.sum(X, dim=1) > 0).float().unsqueeze(1)
    return X, y

# Modèle RNN simple
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        # Forme de x : (batch, seq_len, input_size)
        h0 = torch.zeros(1, x.size(0), self.hidden_size)  # État caché initial
        out, _ = self.rnn(x, h0)
        # Prendre la dernière sortie pour la classification
        out = self.fc(out[:, -1, :])  # Dernier pas de temps
        return self.sigmoid(out)

# Initialiser le modèle, la fonction de perte, l'optimiseur
model = SimpleRNN(input_size, hidden_size, output_size)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Boucle d'entraînement
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

# Exemple d'inférence
test_seq = torch.randn(1, sequence_length, input_size)
prediction = model(test_seq)
print(f'Prediction: {prediction.item():.4f}')
```

#### Fonctionnement :
- **Génération des données** : Crée des séquences aléatoires de longueur 10 avec une étiquette binaire (1 si somme > 0, sinon 0).
- **Modèle** : Utilise `nn.RNN` (cellule RNN basique). La passe forward traite la séquence pas à pas, en utilisant le dernier état caché pour la sortie.
- **Entraînement** : Boucle PyTorch standard avec la perte BCE pour la classification binaire.
- **Sortie** : L'activation sigmoid donne une probabilité entre 0 et 1.

Il s'agit d'un RNN classique ; pour de meilleures performances sur les longues séquences, envisagez les variantes LSTM ou GRU (par exemple, remplacez `nn.RNN` par `nn.LSTM`).

### Variante LSTM (Extension rapide)
Pour les problèmes de gradients disparaissants, passez au LSTM :

```python
# Dans la classe du modèle, remplacez :
self.rnn = nn.LSTM(input_size, hidden_size, batch_first=True)

# Et dans forward :
h0 = torch.zeros(1, x.size(0), self.hidden_size)
c0 = torch.zeros(1, x.size(0), self.hidden_size)  # Le LSTM a besoin d'un état de cellule
out, (hn, cn) = self.rnn(x, (h0, c0))
```

Exécutez ce code dans un environnement PyTorch pour expérimenter !

[Documentation PyTorch RNN](https://pytorch.org/docs/stable/generated/torch.nn.RNN.html)  
[Documentation PyTorch LSTM](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)