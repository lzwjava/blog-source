---
audio: false
generated: true
lang: fr
layout: post
title: Réseaux antagonistes génératifs
translated: true
type: note
---

**Définition** :  
Les GANs sont une classe de frameworks d'apprentissage automatique dans laquelle deux réseaux de neurones, le **générateur** (\\(G\\)) et le **discriminateur** (\\(D\\)), sont en compétition adversariale. Le générateur crée des données synthétiques, tandis que le discriminateur évalue si les données sont réelles (provenant de l'ensemble d'entraînement) ou fausses (provenant de \\(G\\)). Grâce à cette compétition, \\(G\\) améliore sa capacité à générer des données réalistes, et \\(D\\) devient meilleur pour distinguer les vraies des fausses données.

---

### Formulation Mathématique

L'entraînement adversarial est formalisé comme un **jeu minimax** avec la fonction de valeur \\(V(D, G)\\) :

\\[
\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}(x)}[\log D(x)] + \mathbb{E}_{z \sim p_z(z)}[\log(1 - D(G(z)))]
\\]

- **Perte du Discriminateur** : Maximiser la probabilité de classer correctement les données réelles et fausses :
  \\[
  L_D = -\left[\mathbb{E}[\log D(x)] + \mathbb{E}[\log(1 - D(G(z)))]\right]
  \\]

- **Perte du Générateur** : Minimiser la probabilité que le discriminateur identifie correctement les données fausses (version non saturante pour de meilleurs gradients) :
  \\[
  L_G = -\mathbb{E}[\log D(G(z))]
  \\]

---

### Exemple de Code (PyTorch)

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Hyperparamètres
latent_dim = 100
img_dim = 784  # 28x28 MNIST
batch_size = 64
epochs = 50
lr = 0.0002

# Réseau Générateur
class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, img_dim),
            nn.Tanh()  # Sorties dans [-1, 1]
        )
    
    def forward(self, z):
        return self.model(z)

# Réseau Discriminateur
class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(img_dim, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 1),
        )
    
    def forward(self, img):
        return self.model(img)

# Initialisation des modèles, optimiseurs et perte
generator = Generator()
discriminator = Discriminator()
optimizer_G = optim.Adam(generator.parameters(), lr=lr)
optimizer_D = optim.Adam(discriminator.parameters(), lr=lr)
criterion = nn.BCEWithLogitsLoss()

# Chargement des données (MNIST)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # Normaliser vers [-1, 1]
])
dataloader = DataLoader(
    datasets.MNIST("./data", train=True, download=True, transform=transform),
    batch_size=batch_size,
    shuffle=True
)

# Boucle d'entraînement
for epoch in range(epochs):
    for i, (real_imgs, _) in enumerate(dataloader):
        real_imgs = real_imgs.view(-1, img_dim)
        batch_size = real_imgs.size(0)
        
        # Générer des images fausses
        z = torch.randn(batch_size, latent_dim)
        fake_imgs = generator(z)
        
        # Entraîner le Discriminateur
        optimizer_D.zero_grad()
        
        # Perte sur les images réelles
        real_labels = torch.ones(batch_size, 1)
        real_outputs = discriminator(real_imgs)
        d_loss_real = criterion(real_outputs, real_labels)
        
        # Perte sur les images fausses
        fake_labels = torch.zeros(batch_size, 1)
        fake_outputs = discriminator(fake_imgs.detach())
        d_loss_fake = criterion(fake_outputs, fake_labels)
        
        d_loss = d_loss_real + d_loss_fake
        d_loss.backward()
        optimizer_D.step()
        
        # Entraîner le Générateur
        optimizer_G.zero_grad()
        
        # Tromper le discriminateur
        outputs = discriminator(fake_imgs)
        g_loss = criterion(outputs, real_labels)
        g_loss.backward()
        optimizer_G.step()
        
    # Afficher les pertes ou générer des échantillons périodiquement
    print(f"Epoch [{epoch}/{epochs}] | D Loss: {d_loss.item():.4f} | G Loss: {g_loss.item():.4f}")

# Générer des échantillons
z = torch.randn(1, latent_dim)
generated_img = generator(z).view(28, 28).detach().numpy()
```

---

### Explication du Code

1. **Réseaux** :
   - **Générateur** : Transforme du bruit (\\(z\\)) en images (de type MNIST) en utilisant des couches linéaires et `LeakyReLU`.
   - **Discriminateur** : Classe les images comme réelles/fausses en utilisant des couches linéaires et `LeakyReLU`.

2. **Entraînement** :
   - **Discriminateur** : Maximise \\(\log D(x) + \log(1 - D(G(z)))\\).
   - **Générateur** : Minimise \\(\log(1 - D(G(z)))\\) (ou, de manière équivalente, maximise \\(\log D(G(z))\\)).

3. **Données** :
   - Les images MNIST sont normalisées vers \\([-1, 1]\\) pour correspondre à la sortie `Tanh` du générateur.

4. **Optimisation** :
   - Optimiseur Adam pour les deux réseaux.
   - BCEWithLogitsLoss combine l'activation sigmoid et l'entropie croisée binaire.

---

### Exemple de Sortie

Après l'entraînement, le générateur peut produire des chiffres de type MNIST. Utilisez matplotlib pour visualiser les images générées :

```python
import matplotlib.pyplot as plt

# Générer et afficher une image
z = torch.randn(1, latent_dim)
generated_img = generator(z).view(28, 28).detach().numpy()
plt.imshow(generated_img, cmap="gray")
plt.axis("off")
plt.show()
```

Ce code fournit une compréhension fondamentale des GANs, de leurs mathématiques et de leur implémentation. Pour une performance améliorée, envisagez des réseaux plus profonds, des couches convolutionnelles et des techniques avancées comme le *learning rate scheduling* ou les pénalités de gradient.