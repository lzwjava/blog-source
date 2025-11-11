---
audio: false
generated: true
lang: ar
layout: post
title: الشبكات العدوّة التوليدية
translated: true
type: note
---

**التعريف**:  
شبكات الخصومة التوليدية (GANs) هي فئة من أطر تعلم الآلة حيث تتنافس شبكتان عصبونيتان، **المُولِّد** (\\(G\\)) و**المُميِّز** (\\(D\\)), بشكل خصومي. يقوم المُولِّد بإنشاء بيانات اصطناعية، بينما يقوم المُميِّز بتقييم ما إذا كانت البيانات حقيقية (من مجموعة التدريب) أو مُزيفة (من \\(G\\)). من خلال هذا التنافس، يتحسن \\(G\\) في قدرته على توليد بيانات واقعية، ويصبح \\(D\\) أفضل في التمييز بين الحقيقي والمُزيف.

---

### الصياغة الرياضية

يتم صياغة التدريب الخصومي على أنه **لعبة minimax** بدالة القيمة \\(V(D, G)\\):

\\[
\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}(x)[\log D(x)] + \mathbb{E}_{z \sim p_z(z)}[\log(1 - D(G(z)))]
\\]

- **خسارة المُميِّز**: زيادة احتمالية التصنيف الصحيح للبيانات الحقيقية والمُزيفة:
  \\[
  L_D = -\left[\mathbb{E}[\log D(x)] + \mathbb{E}[\log(1 - D(G(z)))]\right]
  \\]

- **خسارة المُولِّد**: تقليل احتمالية قيام المُميِّز بتحديد البيانات المُزيفة بشكل صحيح (الإصدار غير المشبع للحصول على تدرجات أفضل):
  \\[
  L_G = -\mathbb{E}[\log D(G(z))]
  \\]

---

### مثال على الكود (PyTorch)

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Hyperparameters
latent_dim = 100
img_dim = 784  # 28x28 MNIST
batch_size = 64
epochs = 50
lr = 0.0002

# Generator Network
class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, img_dim),
            nn.Tanh()  # Outputs in [-1, 1]
        )
    
    def forward(self, z):
        return self.model(z)

# Discriminator Network
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

# Initialize models, optimizers, and loss
generator = Generator()
discriminator = Discriminator()
optimizer_G = optim.Adam(generator.parameters(), lr=lr)
optimizer_D = optim.Adam(discriminator.parameters(), lr=lr)
criterion = nn.BCEWithLogitsLoss()

# Data loading (MNIST)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # Normalize to [-1, 1]
])
dataloader = DataLoader(
    datasets.MNIST("./data", train=True, download=True, transform=transform),
    batch_size=batch_size,
    shuffle=True
)

# Training loop
for epoch in range(epochs):
    for i, (real_imgs, _) in enumerate(dataloader):
        real_imgs = real_imgs.view(-1, img_dim)
        batch_size = real_imgs.size(0)
        
        # Generate fake images
        z = torch.randn(batch_size, latent_dim)
        fake_imgs = generator(z)
        
        # Train Discriminator
        optimizer_D.zero_grad()
        
        # Loss on real images
        real_labels = torch.ones(batch_size, 1)
        real_outputs = discriminator(real_imgs)
        d_loss_real = criterion(real_outputs, real_labels)
        
        # Loss on fake images
        fake_labels = torch.zeros(batch_size, 1)
        fake_outputs = discriminator(fake_imgs.detach())
        d_loss_fake = criterion(fake_outputs, fake_labels)
        
        d_loss = d_loss_real + d_loss_fake
        d_loss.backward()
        optimizer_D.step()
        
        # Train Generator
        optimizer_G.zero_grad()
        
        # Fool the discriminator
        outputs = discriminator(fake_imgs)
        g_loss = criterion(outputs, real_labels)
        g_loss.backward()
        optimizer_G.step()
        
    # Print losses or generate samples periodically
    print(f"Epoch [{epoch}/{epochs}] | D Loss: {d_loss.item():.4f} | G Loss: {g_loss.item():.4f}")

# Generate samples
z = torch.randn(1, latent_dim)
generated_img = generator(z).view(28, 28).detach().numpy()
```

---

### شرح الكود

1. **الشبكات**:
   - **المُولِّد**: يحول الضوضاء (\\(z\\)) إلى صور (تشبه MNIST) باستخدام طبقات خطية و `LeakyReLU`.
   - **المُميِّز**: يصنف الصور على أنها حقيقية/مُزيفة باستخدام طبقات خطية و `LeakyReLU`.

2. **التدريب**:
   - **المُميِّز**: يزيد من قيمة \\(\log D(x) + \log(1 - D(G(z)))\\).
   - **المُولِّد**: يقلل من قيمة \\(\log(1 - D(G(z)))\\) (أو ما يعادل ذلك، يزيد من قيمة \\(\log D(G(z))\\)).

3. **البيانات**:
   - يتم تسوية صور MNIST إلى المدى \\([-1, 1]\\) لتتوافق مع خرج المُولِّد `Tanh`.

4. **التحسين**:
   - مُحسِّن Adam لكلا الشبكتين.
   - BCEWithLogitsLoss يجمع بين تفعيل sigmoid والانتروبيا التبادلية الثنائية.

---

### مثال على الناتج

بعد التدريب، يمكن للمُولِّد إنتاج أرقام تشبه أرقام MNIST. استخدم matplotlib لتصور الصور المُولَّدة:

```python
import matplotlib.pyplot as plt

# Generate and plot an image
z = torch.randn(1, latent_dim)
generated_img = generator(z).view(28, 28).detach().numpy()
plt.imshow(generated_img, cmap="gray")
plt.axis("off")
plt.show()
```

يوفر هذا الكود فهمًا أساسيًا لشبكات GANs ورياضياتها وتنفيذها. لتحسين الأداء، فكر في استخدام شبكات أعمق، وطبقات تلافيفية، وتقنيات متقدمة مثل جدولة معدل التعلم أو عقوبات التدرج.