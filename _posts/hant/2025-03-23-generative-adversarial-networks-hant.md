---
audio: false
generated: true
lang: hant
layout: post
title: 生成對抗網絡
translated: true
type: note
---

**定義**：  
GANs 是一類機器學習框架，其中兩個神經網絡——**生成器**（\\(G\\)）與**判別器**（\\(D\\)）——以對抗方式競爭。生成器負責創建合成數據，而判別器則評估數據是真實的（來自訓練集）還是虛假的（來自 \\(G\\)）。透過這種競爭，\\(G\\) 提升生成逼真數據的能力，而 \\(D\\) 則變得更擅長區分真實與虛假數據。

---

### 數學公式

對抗訓練被形式化為一個帶有價值函數 \\(V(D, G)\\) 的**極小極大博弈**：

\\[
\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}(x)}[\log D(x)] + \mathbb{E}_{z \sim p_z(z)}[\log(1 - D(G(z)))]
\\]

- **判別器損失**：最大化正確分類真實與虛假數據的概率：
  \\[
  L_D = -\left[\mathbb{E}[\log D(x)] + \mathbb{E}[\log(1 - D(G(z)))]\right]
  \\]

- **生成器損失**：最小化判別器正確識別虛假數據的概率（為獲得更好的梯度，採用非飽和版本）：
  \\[
  L_G = -\mathbb{E}[\log D(G(z))]
  \\]

---

### 代碼示例 (PyTorch)

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 超參數
latent_dim = 100
img_dim = 784  # 28x28 MNIST
batch_size = 64
epochs = 50
lr = 0.0002

# 生成器網絡
class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, img_dim),
            nn.Tanh()  # 輸出範圍 [-1, 1]
        )
    
    def forward(self, z):
        return self.model(z)

# 判別器網絡
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

# 初始化模型、優化器和損失函數
generator = Generator()
discriminator = Discriminator()
optimizer_G = optim.Adam(generator.parameters(), lr=lr)
optimizer_D = optim.Adam(discriminator.parameters(), lr=lr)
criterion = nn.BCEWithLogitsLoss()

# 數據加載 (MNIST)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # 標準化至 [-1, 1]
])
dataloader = DataLoader(
    datasets.MNIST("./data", train=True, download=True, transform=transform),
    batch_size=batch_size,
    shuffle=True
)

# 訓練循環
for epoch in range(epochs):
    for i, (real_imgs, _) in enumerate(dataloader):
        real_imgs = real_imgs.view(-1, img_dim)
        batch_size = real_imgs.size(0)
        
        # 生成虛假圖像
        z = torch.randn(batch_size, latent_dim)
        fake_imgs = generator(z)
        
        # 訓練判別器
        optimizer_D.zero_grad()
        
        # 真實圖像的損失
        real_labels = torch.ones(batch_size, 1)
        real_outputs = discriminator(real_imgs)
        d_loss_real = criterion(real_outputs, real_labels)
        
        # 虛假圖像的損失
        fake_labels = torch.zeros(batch_size, 1)
        fake_outputs = discriminator(fake_imgs.detach())
        d_loss_fake = criterion(fake_outputs, fake_labels)
        
        d_loss = d_loss_real + d_loss_fake
        d_loss.backward()
        optimizer_D.step()
        
        # 訓練生成器
        optimizer_G.zero_grad()
        
        # 欺騙判別器
        outputs = discriminator(fake_imgs)
        g_loss = criterion(outputs, real_labels)
        g_loss.backward()
        optimizer_G.step()
        
    # 定期打印損失或生成樣本
    print(f"Epoch [{epoch}/{epochs}] | D Loss: {d_loss.item():.4f} | G Loss: {g_loss.item():.4f}")

# 生成樣本
z = torch.randn(1, latent_dim)
generated_img = generator(z).view(28, 28).detach().numpy()
```

---

### 代碼解釋

1. **網絡**：
   - **生成器**：使用線性層和 `LeakyReLU` 將噪聲 (\\(z\\)) 轉換為圖像（類似 MNIST）。
   - **判別器**：使用線性層和 `LeakyReLU` 將圖像分類為真實或虛假。

2. **訓練**：
   - **判別器**：最大化 \\(\log D(x) + \log(1 - D(G(z)))\\)。
   - **生成器**：最小化 \\(\log(1 - D(G(z)))\\)（或等效地，最大化 \\(\log D(G(z))\\)）。

3. **數據**：
   - MNIST 圖像被標準化至 \\([-1, 1]\\)，以匹配生成器的 `Tanh` 輸出。

4. **優化**：
   - 兩個網絡均使用 Adam 優化器。
   - BCEWithLogitsLoss 結合了 sigmoid 激活函數和二元交叉熵。

---

### 樣本輸出

訓練後，生成器能夠產生類似 MNIST 的數字。使用 matplotlib 可視化生成的圖像：

```python
import matplotlib.pyplot as plt

# 生成並繪製圖像
z = torch.randn(1, latent_dim)
generated_img = generator(z).view(28, 28).detach().numpy()
plt.imshow(generated_img, cmap="gray")
plt.axis("off")
plt.show()
```

此代碼提供了對 GANs 及其數學原理和實現的基礎理解。為提升性能，可考慮使用更深的網絡、卷積層以及進階技術，如學習率調度或梯度懲罰。