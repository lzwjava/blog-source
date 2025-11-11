---
audio: false
generated: true
lang: hi
layout: post
title: जनरेटिव एडवरसैरियल नेटवर्क्स (जीएएन)
translated: true
type: note
---

**परिभाषा**:  
GANs मशीन लर्निंग फ्रेमवर्क्स का एक वर्ग है जहाँ दो न्यूरल नेटवर्क, **जनरेटर** (\\(G\\)) और **डिस्क्रिमिनेटर** (\\(D\\)), प्रतिस्पर्धात्मक रूप से एक-दूसरे के विरुद्ध प्रतिस्पर्धा करते हैं। जनरेटर सिंथेटिक डेटा बनाता है, जबकि डिस्क्रिमिनेटर मूल्यांकन करता है कि डेटा वास्तविक (ट्रेनिंग सेट से) है या नकली (\\(G\\) से)। इस प्रतिस्पर्धा के माध्यम से, \\(G\\) यथार्थवादी डेटा जनरेट करने की अपनी क्षमता में सुधार करता है, और \\(D\\) वास्तविक और नकली डेटा के बीच अंतर करने में बेहतर हो जाता है।

---

### गणितीय सूत्रीकरण

प्रतिस्पर्धात्मक ट्रेनिंग को एक **मिनिमैक्स गेम** के रूप में औपचारिक रूप दिया जाता है, जिसमें मान फ़ंक्शन \\(V(D, G)\\) होता है:

\\[
\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}(x)[\log D(x)] + \mathbb{E}_{z \sim p_z(z)}[\log(1 - D(G(z)))]
\\]

- **डिस्क्रिमिनेटर लॉस**: वास्तविक और नकली डेटा को सही ढंग से वर्गीकृत करने की संभावना को अधिकतम करें:
  \\[
  L_D = -\left[\mathbb{E}[\log D(x)] + \mathbb{E}[\log(1 - D(G(z)))]\right]
  \\]

- **जनरेटर लॉस**: डिस्क्रिमिनेटर द्वारा नकली डेटा की सही पहचान करने की संभावना को कम करें (बेहतर ग्रेडिएंट्स के लिए नॉन-सैचुरेटिंग वर्जन):
  \\[
  L_G = -\mathbb{E}[\log D(G(z))]
  \\]

---

### कोड उदाहरण (PyTorch)

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# हाइपरपैरामीटर्स
latent_dim = 100
img_dim = 784  # 28x28 MNIST
batch_size = 64
epochs = 50
lr = 0.0002

# जनरेटर नेटवर्क
class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, img_dim),
            nn.Tanh()  # आउटपुट [-1, 1] में
        )
    
    def forward(self, z):
        return self.model(z)

# डिस्क्रिमिनेटर नेटवर्क
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

# मॉडल्स, ऑप्टिमाइज़र्स और लॉस को इनिशियलाइज़ करें
generator = Generator()
discriminator = Discriminator()
optimizer_G = optim.Adam(generator.parameters(), lr=lr)
optimizer_D = optim.Adam(discriminator.parameters(), lr=lr)
criterion = nn.BCEWithLogitsLoss()

# डेटा लोडिंग (MNIST)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # [-1, 1] में नॉर्मलाइज़ करें
])
dataloader = DataLoader(
    datasets.MNIST("./data", train=True, download=True, transform=transform),
    batch_size=batch_size,
    shuffle=True
)

# ट्रेनिंग लूप
for epoch in range(epochs):
    for i, (real_imgs, _) in enumerate(dataloader):
        real_imgs = real_imgs.view(-1, img_dim)
        batch_size = real_imgs.size(0)
        
        # नकली इमेजेज जनरेट करें
        z = torch.randn(batch_size, latent_dim)
        fake_imgs = generator(z)
        
        # डिस्क्रिमिनेटर को ट्रेन करें
        optimizer_D.zero_grad()
        
        # वास्तविक इमेजेज पर लॉस
        real_labels = torch.ones(batch_size, 1)
        real_outputs = discriminator(real_imgs)
        d_loss_real = criterion(real_outputs, real_labels)
        
        # नकली इमेजेज पर लॉस
        fake_labels = torch.zeros(batch_size, 1)
        fake_outputs = discriminator(fake_imgs.detach())
        d_loss_fake = criterion(fake_outputs, fake_labels)
        
        d_loss = d_loss_real + d_loss_fake
        d_loss.backward()
        optimizer_D.step()
        
        # जनरेटर को ट्रेन करें
        optimizer_G.zero_grad()
        
        # डिस्क्रिमिनेटर को बेवकूफ बनाएं
        outputs = discriminator(fake_imgs)
        g_loss = criterion(outputs, real_labels)
        g_loss.backward()
        optimizer_G.step()
        
    # लॉस प्रिंट करें या समय-समय पर सैंपल जनरेट करें
    print(f"Epoch [{epoch}/{epochs}] | D Loss: {d_loss.item():.4f} | G Loss: {g_loss.item():.4f}")

# सैंपल जनरेट करें
z = torch.randn(1, latent_dim)
generated_img = generator(z).view(28, 28).detach().numpy()
```

---

### कोड की व्याख्या

1. **नेटवर्क्स**:
   - **जनरेटर**: लीनियर लेयर्स और `LeakyReLU` का उपयोग करके नॉइज़ (\\(z\\)) को इमेजेज (MNIST जैसी) में बदलता है।
   - **डिस्क्रिमिनेटर**: लीनियर लेयर्स और `LeakyReLU` का उपयोग करके इमेजेज को वास्तविक/नकली के रूप में वर्गीकृत करता है।

2. **ट्रेनिंग**:
   - **डिस्क्रिमिनेटर**: \\(\log D(x) + \log(1 - D(G(z))\\) को अधिकतम करता है।
   - **जनरेटर**: \\(\log(1 - D(G(z))\\) को कम करता है (या समकक्ष रूप से, \\(\log D(G(z))\\) को अधिकतम करता है)।

3. **डेटा**:
   - MNIST इमेजेज को जनरेटर के `Tanh` आउटपुट से मेल खाने के लिए \\([-1, 1]\\) में नॉर्मलाइज़ किया जाता है।

4. **ऑप्टिमाइज़ेशन**:
   - दोनों नेटवर्क्स के लिए Adam ऑप्टिमाइज़र।
   - BCEWithLogitsLoss सिग्मॉइड एक्टिवेशन और बाइनरी क्रॉस-एन्ट्रोपी को जोड़ता है।

---

### सैंपल आउटपुट

ट्रेनिंग के बाद, जनरेटर MNIST जैसे अंक उत्पन्न कर सकता है। जनरेट की गई इमेजेज को विज़ुअलाइज़ करने के लिए matplotlib का उपयोग करें:

```python
import matplotlib.pyplot as plt

# एक इमेज जनरेट करें और प्लॉट करें
z = torch.randn(1, latent_dim)
generated_img = generator(z).view(28, 28).detach().numpy()
plt.imshow(generated_img, cmap="gray")
plt.axis("off")
plt.show()
```

यह कोड GANs, उनके गणित और इम्प्लीमेंटेशन की मूलभूत समझ प्रदान करता है। बेहतर परफॉर्मेंस के लिए, गहरे नेटवर्क्स, कन्वोल्यूशनल लेयर्स और लर्निंग रेट शेड्यूलिंग या ग्रेडिएंट पेनल्टी जैसी उन्नत तकनीकों पर विचार करें।