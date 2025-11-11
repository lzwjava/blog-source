---
audio: false
generated: true
lang: es
layout: post
title: Redes Generativas Antagónicas
translated: true
type: note
---

**Definición**:  
Las GANs son una clase de marcos de aprendizaje automático donde dos redes neuronales, el **generador** (\\(G\\)) y el **discriminador** (\\(D\\)), compiten de manera adversarial. El generador crea datos sintéticos, mientras que el discriminador evalúa si los datos son reales (del conjunto de entrenamiento) o falsos (de \\(G\\)). A través de esta competencia, \\(G\\) mejora su capacidad para generar datos realistas y \\(D\\) se vuelve mejor para distinguir lo real de lo falso.

---

### Formulación Matemática

El entrenamiento adversarial se formaliza como un **juego minimax** con la función de valor \\(V(D, G)\\):

\\[
\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}(x)}[\log D(x)] + \mathbb{E}_{z \sim p_z(z)}[\log(1 - D(G(z)))]
\\]

- **Pérdida del Discriminador**: Maximizar la probabilidad de clasificar correctamente los datos reales y falsos:
  \\[
  L_D = -\left[\mathbb{E}[\log D(x)] + \mathbb{E}[\log(1 - D(G(z)))]\right]
  \\]

- **Pérdida del Generador**: Minimizar la probabilidad de que el discriminador identifique correctamente los datos falsos (versión no saturada para mejores gradientes):
  \\[
  L_G = -\mathbb{E}[\log D(G(z))]
  \\]

---

### Ejemplo de Código (PyTorch)

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Hiperparámetros
latent_dim = 100
img_dim = 784  # 28x28 MNIST
batch_size = 64
epochs = 50
lr = 0.0002

# Red Generadora
class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, img_dim),
            nn.Tanh()  # Salidas en [-1, 1]
        )
    
    def forward(self, z):
        return self.model(z)

# Red Discriminadora
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

# Inicializar modelos, optimizadores y pérdida
generator = Generator()
discriminator = Discriminator()
optimizer_G = optim.Adam(generator.parameters(), lr=lr)
optimizer_D = optim.Adam(discriminator.parameters(), lr=lr)
criterion = nn.BCEWithLogitsLoss()

# Carga de datos (MNIST)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # Normalizar a [-1, 1]
])
dataloader = DataLoader(
    datasets.MNIST("./data", train=True, download=True, transform=transform),
    batch_size=batch_size,
    shuffle=True
)

# Bucle de entrenamiento
for epoch in range(epochs):
    for i, (real_imgs, _) in enumerate(dataloader):
        real_imgs = real_imgs.view(-1, img_dim)
        batch_size = real_imgs.size(0)
        
        # Generar imágenes falsas
        z = torch.randn(batch_size, latent_dim)
        fake_imgs = generator(z)
        
        # Entrenar Discriminador
        optimizer_D.zero_grad()
        
        # Pérdida en imágenes reales
        real_labels = torch.ones(batch_size, 1)
        real_outputs = discriminator(real_imgs)
        d_loss_real = criterion(real_outputs, real_labels)
        
        # Pérdida en imágenes falsas
        fake_labels = torch.zeros(batch_size, 1)
        fake_outputs = discriminator(fake_imgs.detach())
        d_loss_fake = criterion(fake_outputs, fake_labels)
        
        d_loss = d_loss_real + d_loss_fake
        d_loss.backward()
        optimizer_D.step()
        
        # Entrenar Generador
        optimizer_G.zero_grad()
        
        # Engañar al discriminador
        outputs = discriminator(fake_imgs)
        g_loss = criterion(outputs, real_labels)
        g_loss.backward()
        optimizer_G.step()
        
    # Imprimir pérdidas o generar muestras periódicamente
    print(f"Epoch [{epoch}/{epochs}] | D Loss: {d_loss.item():.4f} | G Loss: {g_loss.item():.4f}")

# Generar muestras
z = torch.randn(1, latent_dim)
generated_img = generator(z).view(28, 28).detach().numpy()
```

---

### Explicación del Código

1. **Redes**:
   - **Generador**: Transforma ruido (\\(z\\)) en imágenes (similares a MNIST) usando capas lineales y `LeakyReLU`.
   - **Discriminador**: Clasifica imágenes como reales/falsas usando capas lineales y `LeakyReLU`.

2. **Entrenamiento**:
   - **Discriminador**: Maximiza \\(\log D(x) + \log(1 - D(G(z)))\\).
   - **Generador**: Minimiza \\(\log(1 - D(G(z)))\\) (o equivalentemente, maximiza \\(\log D(G(z))\\)).

3. **Datos**:
   - Las imágenes MNIST se normalizan a \\([-1, 1]\\) para que coincidan con la salida `Tanh` del generador.

4. **Optimización**:
   - Optimizador Adam para ambas redes.
   - BCEWithLogitsLoss combina la activación sigmoid y la entropía cruzada binaria.

---

### Salida de Ejemplo

Después del entrenamiento, el generador puede producir dígitos similares a MNIST. Usa matplotlib para visualizar las imágenes generadas:

```python
import matplotlib.pyplot as plt

# Generar y trazar una imagen
z = torch.randn(1, latent_dim)
generated_img = generator(z).view(28, 28).detach().numpy()
plt.imshow(generated_img, cmap="gray")
plt.axis("off")
plt.show()
```

Este código proporciona una comprensión fundamental de las GANs, su matemática e implementación. Para un mejor rendimiento, considera redes más profundas, capas convolucionales y técnicas avanzadas como programación de la tasa de aprendizaje o penalizaciones de gradiente.