---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Implémentation LSTM NumPy à partir de zéro
translated: true
type: note
---

Ceci est une implémentation basique d'un réseau Long Short-Term Memory (LSTM) utilisant uniquement NumPy, inspirée par les concepts du billet de blog de Christopher Olah sur Understanding LSTM Networks. Elle inclut les portes principales (oubli, entrée, cellule candidate et sortie) et se concentre sur la passe avant. La classe gère un seul pas de temps via `forward()` et une séquence entière via `forward_sequence()`.

Les poids sont initialisés aléatoirement (en pratique, utilisez une meilleure initialisation comme Xavier/Glorot). Aucune passe arrière ou entraînement n'est inclus ici — étendez avec la rétropropagation dans le temps (BPTT) pour cela.

```python
import numpy as np

class LSTM:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        # Initialiser les poids et les biais pour les portes d'oubli, d'entrée, de cellule et de sortie
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
        # x: (input_size, 1), h_prev et C_prev: (hidden_size, 1)
        # Concaténer l'état caché et l'entrée
        concat = np.vstack((h_prev, x))
        # Porte d'oubli
        f_t = self.sigmoid(np.dot(self.Wf, concat) + self.bf)
        # Porte d'entrée
        i_t = self.sigmoid(np.dot(self.Wi, concat) + self.bi)
        C_tilda = self.tanh(np.dot(self.WC, concat) + self.bC)
        # Mise à jour de l'état de cellule
        C_t = f_t * C_prev + i_t * C_tilda
        # Porte de sortie
        o_t = self.sigmoid(np.dot(self.Wo, concat) + self.bo)
        # Mise à jour de l'état caché
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
        return np.hstack(outputs).T  # Retourne (seq_len, hidden_size)

# Exemple d'utilisation
input_size = 3
hidden_size = 5
lstm = LSTM(input_size, hidden_size)

# Pas unique
x_t = np.random.randn(input_size, 1)
h_prev = np.zeros((hidden_size, 1))
C_prev = np.zeros((hidden_size, 1))
h_t, C_t = lstm.forward(x_t, h_prev, C_prev)
print("Pas unique - Forme de l'état caché :", h_t.shape)

# Séquence
X = np.random.randn(4, input_size)  # seq_len=4
outputs = lstm.forward_sequence(X)
print("Forme des sorties de la séquence :", outputs.shape)
```

### Explication rapide
- **Initialisation** : Les poids connectent l'entrée concaténée (état caché précédent + entrée actuelle) à chaque porte. Les biais sont initialisés à zéro.
- **Portes** :
  - **Porte d'oubli** (`f_t`) : Décide quoi oublier de l'état de cellule précédent (sigmoid : 0-1).
  - **Porte d'entrée** (`i_t`) et **cellule candidate** (`C_tilda`) : Décident quelles nouvelles informations ajouter (sigmoid + tanh).
  - **Porte de sortie** (`o_t`) : Filtre l'état de cellule pour produire l'état caché (sigmoid + tanh sur la cellule).
- **État de cellule** (`C_t`) : Flux linéaire avec des mises à jour additives pour la mémoire à long terme.
- **Utilisation** : Pour les séquences, bouclez à travers les pas de temps, en mettant à jour progressivement les états cachés et de cellule.

Cela correspond à l'architecture LSTM du blog de Colah : l'état de cellule comme une "autoroute" contrôlée par des portes.

[Understanding LSTMs: Implementation from Scratch](https://medium.com/@samina.amin/understanding-lstms-lstm-implementation-from-scratch-18965a150eca)