---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 緲子優化器介紹與概覽
translated: true
type: note
---

### Muon Optimizer 全面介紹

Muon Optimizer 是一種專為神經網絡中線性層（例如全連接層或嵌入層）訓練而設計的專用、受二階優化啟發的優化算法，儘管它也可以擴展到其他層。它最初於 2024 年底由包括 Keller Jordan 和 Jeremy Bernstein 在內的研究人員提出，其根源於幾何優化技術，如極座標初始化（polar initialization）和模塊對偶框架（modular duality framework）[1][2]。Moonshot AI 和 Kimi AI 的創始人楊植麟在討論其 Kimi K2 模型——一個擁有 1 萬億參數的大型語言模型（LLM）——的訓練時，強調了 Muon 的作用，它作為高效、高秩更新的骨幹，能夠適應損失景觀的幾何形狀[3][4]。然而，其基準版本存在不穩定性（例如，在長時間訓練期間出現損失峰值），這促使 Moonshot AI 開發了 MuonClip，這是一個增強變體，具有穩定性機制，例如用於注意力層的 QK-clipping[3][2]。

Muon 以其令牌效率著稱：與 AdamW 等一階優化器相比，它需要更少的訓練令牌即可達到相當的性能，這使其對於像 LLM 預訓練這樣資源密集型的任務非常有價值。它旨在近似二階方法（例如牛頓法），而無需其全部計算成本，專注於通過高秩矩陣更新進行特徵值適應。這在梯度嘈雜的大規模模型中特別有用，因為 Muon 利用了受自然梯度和矩陣平方根啟發的預處理（preconditioning）。

#### 關鍵原理與推導
- **核心概念**：Muon 植根於幾何優化，使更新適應損失函數的「能量景觀」。它使用基於費雪信息矩陣（或近似值）的預處理器來縮放梯度，類似於 AdaGrad 或 Shampoo，但針對密集線性層進行了優化[1][2]。
- **算法步驟**：
  1. **梯度計算**：計算線性層中權重 \(W\) 的標準梯度 \(\nabla W\)。
  2. **預處理**：使用 Newton-Schulz 迭代來近似預處理器（例如，源自層統計數據）的矩陣平方根。這使得無需進行完整的特徵分解即可實現秩適應。
  3. **更新規則**：應用一個能更有效縮放高秩分量的更新，通常結合動量或裁剪以確保穩定性。
- **數學洞察**：如果 \(G\) 是梯度矩陣，Muon 近似於像 \(W \leftarrow W - \eta \cdot \sqrt{P}^{-1} G\) 這樣的更新，其中 \(\sqrt{P}\) 使用迭代矩陣平方根[2][5]。這與 AdamW 的對角線或基於動量的縮放形成對比，使 Muon 能夠更好地捕捉參數間的相關性。
- **效率提升**：在某些基準測試中，Muon 可以將訓練步數減少 20-50%，如在 NanoGPT 記錄中所見[1]。

#### 優點與缺點
- **優點**：
  - **在線性層上更好的收斂性**：在 LLM 典型的密集、高維空間中表現出色，從而用更少的令牌實現更低的損失[4][6]。
  - **資源高效**：由於所需的梯度計算更少，每輪訓練速度更快。
  - **開源且可擴展**：存在多種實現，包括像 Flash-Muon 這樣用於 GPU 加速的特定實現[4][7]。
- **缺點**：
  - **不穩定性**：在更深層的網絡或稀疏層中容易發散；MuonClip 通過在訓練期間裁剪注意力分數（例如，查詢-鍵乘積）來解決這個問題[3][2]。
  - **層特異性**：不適用於卷積層或循環層；它偏向於線性/MoE 架構。Keras 指出它不應用於非線性層[8]。
  - **超參數敏感性**：需要針對學習率（\(\eta\)）和誘導正交性的操作進行調優；未經調整可能無法跨模型尺寸遷移[2]。
- **MuonClip 變體（Kimi 專用）**：這是 Muon 的演進版本，與 QK-clipping 集成，以防止在 15.5 萬億令牌預訓練中出現不穩定。它穩定了 Kimi K2 的 320 億激活參數，實現了零損失峰值的訓練和卓越的基準測試成績（例如，在 Tau2-Bench 上達到 66.1 分）[3][8]。雖然目前沒有公開代碼，它是專有的，但建立在開源 Muon 的基礎上。

Muon 影響了 AI 優化領域，出現在像 Scion 這樣的基準測試中以及 Reddit/X 上的討論，常因其「幾何直覺」而受到讚揚。關於完整推導，請參閱 Jeremy Bernstein 的博客[2]。現在，讓我們來看一個實際的實現。

### 代碼示例：在 PyTorch 中實現 Muon Optimizer
以下是基本 Muon 優化器的 PyTorch 實現，改編自官方存儲庫 (https://github.com/KellerJordan/Muon)。這是針對密集線性層的簡化版本；它包括用於預處理器的 Newton-Schulz 迭代。

```python
import torch
import torch.nn as nn

class Muon(torch.optim.Optimizer):
    """
    用於線性層的 Muon 優化器。
    源自：https://github.com/KellerJordan/Muon
    """
    def __init__(self, params, lr=1e-3, lr_b=2e-3, b2=0.95, wd=0.0):
        defaults = dict(lr=lr, lr_b=lr_b, b2=b2, wd=wd)
        super().__init__(params, defaults)

    def step(self):
        for group in self.param_groups:
            lr = group['lr']
            lr_b = group['lr_b']
            b2 = group['b2']
            wd = group['wd']

            for p in group['params']:
                if p.grad is None:
                    continue

                grad = p.grad.data.float()
                state = self.state[p]
                if 'momentum' not in state:
                    state['momentum'] = torch.zeros_like(grad)

                # 動量更新
                state['momentum'].mul_(b2).add_(grad)

                # 權重衰減
                if wd != 0:
                    p.data.mul_(1 - lr * wd)

                # Muon 的正交化（秩適應）
                grad_vec = state['momentum'].view(-1, grad.shape[-1])
                p_vec = p.data.view(-1, p.shape[-1])

                # 用於矩陣平方根近似的 Newton-Schulz（簡化版）
                G = grad_vec @ grad_vec.t() / grad_vec.shape[0]
                # 在完整實現中，這是迭代的；此處使用冪級數近似
                sqrt_G = torch.sqrt(G + 1e-6 * torch.eye(G.shape[0], device=G.device))

                # 更新
                update = grad_vec.t() @ sqrt_G @ grad_vec / sqrt_G.shape[0]
                p.data.sub_(lr_b * update.view(p.shape))

# 使用示例
model = nn.Linear(768, 768)  # 密集層
optimizer = Muon(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()
data = torch.randn(32, 768)
target = torch.randn(32, 768)

for epoch in range(10):
    optimizer.zero_grad()
    output = model(data)
    loss = loss_fn(output, target)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")
```

**關於代碼的說明**：
- 這是一個精簡版本；完整的 GitHub 存儲庫包含用於效率的 CUDA 內核（例如，用於更快矩陣乘法的 Flash-Muon）[3][4]。
- 對於 Keras/TensorFlow：使用 `from keras.optimizers import Muon; opt = Muon(learning_rate=0.01)`[8]。
- 經過調優的超參數（例如 `lr_b=2e-3`）至關重要；請針對您的模型進行實驗。對於 Kimi K2 的 MuonClip，目前沒有公開代碼，但它在注意力前向傳播中添加了裁剪邏輯[2][5]。

如果您需要擴展或基準測試，請告訴我！

引用文獻：
[1] https://kellerjordan.github.io/posts/muon/
[2] https://jeremybernste.in/writing/deriving-muon
[3] https://github.com/KellerJordan/Muon
[4] https://github.com/nil0x9/flash-muon
[5] https://www.lakernewhouse.com/writing/muon-2
[6] https://medium.com/@kyeg/building-the-muon-optimizer-in-pytorch-a-geometric-approach-to-neural-network-optimization-17f4601be548
[7] https://discuss.huggingface.co/t/tutorial-understanding-and-implementing-the-muon-optimizer/167717
[8] https://keras.io/api/optimizers/muon/