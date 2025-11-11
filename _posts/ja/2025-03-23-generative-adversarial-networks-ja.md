---
audio: false
generated: true
lang: ja
layout: post
title: 生成的敵対的ネットワーク（GAN）
translated: true
type: note
---

**定義**:  
GANは、**ジェネレータ** (\\(G\\)) と **ディスクリミネータ** (\\(D\\)) という2つのニューラルネットワークが敵対的に競合する機械学習フレームワークの一種です。ジェネレータは合成データを生成し、ディスクリミネータはデータが本物（トレーニングセット由来）か偽物（\\(G\\) 由来）かを評価します。この競合を通じて、\\(G\\) は現実的なデータを生成する能力を向上させ、\\(D\\) は本物と偽物を区別する能力を向上させます。

---

### 数式による定式化

この敵対的トレーニングは、価値関数 \\(V(D, G)\\) を用いた **ミニマックスゲーム** として定式化されます：

\\[
\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}(x)}[\log D(x)] + \mathbb{E}_{z \sim p_z(z)}[\log(1 - D(G(z)))]
\\]

- **ディスクリミネータの損失**: 本物と偽物のデータを正しく分類する確率を最大化します：
  \\[
  L_D = -\left[\mathbb{E}[\log D(x)] + \mathbb{E}[\log(1 - D(G(z)))]\right]
  \\]

- **ジェネレータの損失**: ディスクリミネータが偽データを正しく識別する確率を最小化します（勾配を改善するための非飽和版）：
  \\[
  L_G = -\mathbb{E}[\log D(G(z))]
  \\]

---

### コード例 (PyTorch)

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# ハイパーパラメータ
latent_dim = 100
img_dim = 784  # 28x28 MNIST
batch_size = 64
epochs = 50
lr = 0.0002

# ジェネレータネットワーク
class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, img_dim),
            nn.Tanh()  # 出力範囲 [-1, 1]
        )
    
    def forward(self, z):
        return self.model(z)

# ディスクリミネータネットワーク
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

# モデル、オプティマイザ、損失関数の初期化
generator = Generator()
discriminator = Discriminator()
optimizer_G = optim.Adam(generator.parameters(), lr=lr)
optimizer_D = optim.Adam(discriminator.parameters(), lr=lr)
criterion = nn.BCEWithLogitsLoss()

# データローディング (MNIST)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # [-1, 1] に正規化
])
dataloader = DataLoader(
    datasets.MNIST("./data", train=True, download=True, transform=transform),
    batch_size=batch_size,
    shuffle=True
)

# トレーニングループ
for epoch in range(epochs):
    for i, (real_imgs, _) in enumerate(dataloader):
        real_imgs = real_imgs.view(-1, img_dim)
        batch_size = real_imgs.size(0)
        
        # 偽画像を生成
        z = torch.randn(batch_size, latent_dim)
        fake_imgs = generator(z)
        
        # ディスクリミネータのトレーニング
        optimizer_D.zero_grad()
        
        # 本物画像に対する損失
        real_labels = torch.ones(batch_size, 1)
        real_outputs = discriminator(real_imgs)
        d_loss_real = criterion(real_outputs, real_labels)
        
        # 偽画像に対する損失
        fake_labels = torch.zeros(batch_size, 1)
        fake_outputs = discriminator(fake_imgs.detach())
        d_loss_fake = criterion(fake_outputs, fake_labels)
        
        d_loss = d_loss_real + d_loss_fake
        d_loss.backward()
        optimizer_D.step()
        
        # ジェネレータのトレーニング
        optimizer_G.zero_grad()
        
        # ディスクリミネータを欺く
        outputs = discriminator(fake_imgs)
        g_loss = criterion(outputs, real_labels)
        g_loss.backward()
        optimizer_G.step()
        
    # 定期的に損失を表示またはサンプルを生成
    print(f"Epoch [{epoch}/{epochs}] | D Loss: {d_loss.item():.4f} | G Loss: {g_loss.item():.4f}")

# サンプル生成
z = torch.randn(1, latent_dim)
generated_img = generator(z).view(28, 28).detach().numpy()
```

---

### コードの説明

1. **ネットワーク**:
   - **ジェネレータ**: 線形層と `LeakyReLU` を使用して、ノイズ (\\(z\\)) を画像（MNIST風）に変換します。
   - **ディスクリミネータ**: 線形層と `LeakyReLU` を使用して、画像が本物か偽物かを分類します。

2. **トレーニング**:
   - **ディスクリミネータ**: \\(\log D(x) + \log(1 - D(G(z)))\\) を最大化します。
   - **ジェネレータ**: \\(\log(1 - D(G(z)))\\) を最小化します（または、等価的に \\(\log D(G(z))\\) を最大化します）。

3. **データ**:
   - MNIST画像は、ジェネレータの `Tanh` 出力に合わせて \\([-1, 1]\\) に正規化されます。

4. **最適化**:
   - 両ネットワークにAdamオプティマイザを使用。
   - BCEWithLogitsLossはシグモイド活性化関数と二値交差エントロピーを組み合わせたものです。

---

### サンプル出力

トレーニング後、ジェネレータはMNIST風の数字を生成できるようになります。生成された画像を可視化するにはmatplotlibを使用します：

```python
import matplotlib.pyplot as plt

# 画像を生成してプロット
z = torch.randn(1, latent_dim)
generated_img = generator(z).view(28, 28).detach().numpy()
plt.imshow(generated_img, cmap="gray")
plt.axis("off")
plt.show()
```

このコードは、GANの基礎的な理解、その数学的基礎、および実装を提供します。性能を向上させるには、より深いネットワーク、畳み込み層、学習率スケジューリングや勾配ペナルティなどの高度な技術を検討してください。