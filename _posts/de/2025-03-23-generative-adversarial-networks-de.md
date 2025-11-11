---
audio: false
generated: true
lang: de
layout: post
title: Generative Adversarial Networks
translated: true
type: note
---

**Definition**:  
GANs sind eine Klasse von Machine-Learning-Frameworks, bei denen zwei neuronale Netze, der **Generator** (\\(G\\)) und der **Diskriminator** (\\(D\\)), gegeneinander antreten. Der Generator erzeugt synthetische Daten, während der Diskriminator bewertet, ob die Daten echt (vom Trainingssatz) oder gefälscht (von \\(G\\)) sind. Durch diesen Wettbewerb verbessert \\(G\\) seine Fähigkeit, realistische Daten zu erzeugen, und \\(D\\) wird besser darin, echt von gefälscht zu unterscheiden.

---

### Mathematische Formulierung

Das adversarielle Training wird als **Minimax-Spiel** mit der Wertfunktion \\(V(D, G)\\) formalisiert:

\\[
\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}(x)}[\log D(x)] + \mathbb{E}_{z \sim p_z(z)}[\log(1 - D(G(z)))]
\\]

- **Diskriminator-Loss**: Maximiere die Wahrscheinlichkeit, echte und gefälschte Daten korrekt zu klassifizieren:
  \\[
  L_D = -\left[\mathbb{E}[\log D(x)] + \mathbb{E}[\log(1 - D(G(z)))]\right]
  \\]

- **Generator-Loss**: Minimiere die Wahrscheinlichkeit, dass der Diskriminator gefälschte Daten korrekt identifiziert (nicht-sättigende Version für bessere Gradienten):
  \\[
  L_G = -\mathbb{E}[\log D(G(z))]
  \\]

---

### Code-Beispiel (PyTorch)

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Hyperparameter
latent_dim = 100
img_dim = 784  # 28x28 MNIST
batch_size = 64
epochs = 50
lr = 0.0002

# Generator-Netzwerk
class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, img_dim),
            nn.Tanh()  # Ausgaben in [-1, 1]
        )
    
    def forward(self, z):
        return self.model(z)

# Diskriminator-Netzwerk
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

# Initialisiere Modelle, Optimierer und Loss
generator = Generator()
discriminator = Discriminator()
optimizer_G = optim.Adam(generator.parameters(), lr=lr)
optimizer_D = optim.Adam(discriminator.parameters(), lr=lr)
criterion = nn.BCEWithLogitsLoss()

# Data Loading (MNIST)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # Normalisiere auf [-1, 1]
])
dataloader = DataLoader(
    datasets.MNIST("./data", train=True, download=True, transform=transform),
    batch_size=batch_size,
    shuffle=True
)

# Training Loop
for epoch in range(epochs):
    for i, (real_imgs, _) in enumerate(dataloader):
        real_imgs = real_imgs.view(-1, img_dim)
        batch_size = real_imgs.size(0)
        
        # Erzeuge gefälschte Bilder
        z = torch.randn(batch_size, latent_dim)
        fake_imgs = generator(z)
        
        # Trainiere Diskriminator
        optimizer_D.zero_grad()
        
        # Loss für echte Bilder
        real_labels = torch.ones(batch_size, 1)
        real_outputs = discriminator(real_imgs)
        d_loss_real = criterion(real_outputs, real_labels)
        
        # Loss für gefälschte Bilder
        fake_labels = torch.zeros(batch_size, 1)
        fake_outputs = discriminator(fake_imgs.detach())
        d_loss_fake = criterion(fake_outputs, fake_labels)
        
        d_loss = d_loss_real + d_loss_fake
        d_loss.backward()
        optimizer_D.step()
        
        # Trainiere Generator
        optimizer_G.zero_grad()
        
        # Täusche den Diskriminator
        outputs = discriminator(fake_imgs)
        g_loss = criterion(outputs, real_labels)
        g_loss.backward()
        optimizer_G.step()
        
    # Gib Losses aus oder erzeuge periodisch Samples
    print(f"Epoch [{epoch}/{epochs}] | D Loss: {d_loss.item():.4f} | G Loss: {g_loss.item():.4f}")

# Erzeuge Samples
z = torch.randn(1, latent_dim)
generated_img = generator(z).view(28, 28).detach().numpy()
```

---

### Erklärung des Codes

1. **Netzwerke**:
   - **Generator**: Transformiert Rauschen (\\(z\\)) unter Verwendung von linearen Layern und `LeakyReLU` in Bilder (MNIST-ähnlich).
   - **Diskriminator**: Klassifiziert Bilder mithilfe von linearen Layern und `LeakyReLU` als echt/gefälscht.

2. **Training**:
   - **Diskriminator**: Maximiert \\(\log D(x) + \log(1 - D(G(z))\\).
   - **Generator**: Minimiert \\(\log(1 - D(G(z))\\) (oder maximiert äquivalent \\(\log D(G(z))\\)).

3. **Daten**:
   - MNIST-Bilder werden auf \\([-1, 1]\\) normalisiert, um zur `Tanh`-Ausgabe des Generators zu passen.

4. **Optimierung**:
   - Adam-Optimierer für beide Netzwerke.
   - BCEWithLogitsLoss kombiniert Sigmoid-Aktivierung und binäre Kreuzentropie.

---

### Beispielausgabe

Nach dem Training kann der Generator MNIST-ähnliche Ziffern erzeugen. Verwende matplotlib, um die generierten Bilder zu visualisieren:

```python
import matplotlib.pyplot as plt

# Erzeuge und plotte ein Bild
z = torch.randn(1, latent_dim)
generated_img = generator(z).view(28, 28).detach().numpy()
plt.imshow(generated_img, cmap="gray")
plt.axis("off")
plt.show()
```

Dieser Code vermittelt ein grundlegendes Verständnis von GANs, ihrer Mathematik und Implementierung. Für eine verbesserte Performance sollten tiefere Netzwerke, Convolutional Layers und fortgeschrittene Techniken wie Learning Rate Scheduling oder Gradient Penalties in Betracht gezogen werden.