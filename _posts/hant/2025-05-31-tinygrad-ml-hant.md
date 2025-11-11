---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: TinyGrad 輕量級機器學習庫
translated: true
type: note
---

### TinyGrad 簡介
TinyGrad 是一個輕量級、極簡主義的 Python 機器學習與深度學習函式庫，專為教育與簡潔性而設計。它像 PyTorch 一樣實作自動微分（autograd），但體積小得多——僅約 1000 行程式碼。非常適合學習 ML 概念或建構小型模型，無需大型函式庫的負擔。它支援張量、神經網路和基本運算，包括透過 PyTorch 或 Metal 實現的 GPU 加速。

你可以在以下位置找到官方儲存庫：[tinygrad GitHub](https://github.com/geohot/tinygrad)。注意：它是實驗性的，在生產環境中不如 PyTorch 或 TensorFlow 穩定。

### 安裝
透過 pip 安裝 TinyGrad：

```bash
pip install tinygrad
```

它具有最少的依賴項，但可選地使用 PyTorch 作為部分後端。如需 GPU 支援，請確保已安裝 PyTorch。

### 基本用法
首先導入並設定上下文（TinyGrad 要求指定是訓練還是推論，因為梯度計算方式不同）。

#### 導入與上下文設定
```python
from tinygrad import Tensor
from tinygrad.nn import Linear, BatchNorm2d  # 用於神經網路

# 設定上下文：訓練（用於梯度計算）或推論
Tensor.training = True  # 啟用梯度追蹤
```

#### 建立與操作張量
張量是核心資料結構，類似 NumPy 陣列或 PyTorch 張量。

```python
# 從列表、NumPy 陣列或形狀建立張量
a = Tensor([1, 2, 3])          # 從列表建立
b = Tensor.zeros(3)            # 形狀為 (3,) 的零張量
c = Tensor.rand(2, 3)          # 形狀為 (2, 3) 的隨機張量

# 基本運算
d = a + b                      # 逐元素加法
e = d * 2                      # 純量乘法
f = a @ Tensor([[1], [2], [3]])  # 矩陣乘法（a 為 1D，隱含轉置）

print(e.numpy())               # 轉換為 NumPy 以列印或進一步使用
```

#### 自動微分（反向傳播）
TinyGrad 使用鏈式法則自動計算梯度。

```python
# 啟用梯度追蹤
Tensor.training = True

x = Tensor([1.0, 2.0, 3.0])
y = (x * 2).sum()             # 某些運算；y 為純量

y.backward()                  # 計算梯度
print(x.grad.numpy())         # 相對於 x 的梯度：應為 [2, 2, 2]
```

匯出至 NumPy 時，使用 `.numpy()`——梯度會累積，除非重置。

#### 神經網路與訓練
TinyGrad 包含基本層和優化器。以下是一個簡單的 MLP 範例：

```python
from tinygrad.nn import Linear, optim

# 定義簡單模型（例如線性層）
model = Linear(3, 1)          # 輸入 3，輸出 1

# 虛擬資料
x = Tensor.rand(4, 3)         # 4 個樣本的批次，3 個特徵
y_true = Tensor.rand(4, 1)    # 目標

# 前向傳播
pred = model(x).sigmoid()      # 假設為二元分類

# 損失（例如均方誤差）
loss = ((pred - y_true) ** 2).mean()

# 反向傳播與優化
loss.backward()
optim.Adam([model], lr=0.01).step()
```

對於卷積網路，使用 `tinygrad.nn` 中的 `Conv2d`。

### 進階功能
- **損失函數與激活函數**：在 `tinygrad.nn` 中可用（例如 `sigmoid`、`relu`、`cross_entropy`）。
- **優化器**：`tinygrad.nn.optim` 中的 `SGD`、`Adam`。
- **層**：`Linear`、`Conv2d`、`BatchNorm` 等。
- **儲存/載入**：模型可儲存為狀態字典（類似 PyTorch）。
- **GPU/加速**：TinyGrad 可透過 PyTorch 後端在 GPU 上執行：`TESOR_SET_DEVICE='cuda:0'`。亦支援 macOS 上的 Metal。
- **視覺/去噪範例**：儲存庫中包含如訓練 MNIST 上的 ResNet 等範例。

完整範例請參閱 GitHub 儲存庫中的 `examples/` 資料夾，例如影像分類或強化學習。

### 範例：訓練神經網路
以下是一個完整的簡單腳本，用於訓練 XOR 問題的網路：

```python
from tinygrad import Tensor
from tinygrad.nn import Linear, optim

# 資料
X = Tensor([[0,0], [0,1], [1,0], [1,1]])
Y = Tensor([[0], [1], [1], [0]])

# 模型
model = Linear(2, 1)
opt = optim.Adam([model], lr=0.1)

Tensor.training = True

for epoch in range(1000):
    pred = model(X).sigmoid()
    loss = ((pred - Y) ** 2).mean()
    loss.backward()
    opt.step()
    opt.zero_grad()

# 測試
print(model(Tensor([[0,0]])))  # 應約為 0
```

### 提示與注意事項
- **模式切換**：訓練時務必設定 `Tensor.training = True`；推論時切換至 `False` 以避免梯度計算。
- **形狀處理**：張量遵循 NumPy 風格的廣播，但需注意小型模型中的溢位問題。
- **除錯**：使用 `.numpy()` 檢查數值。若出現錯誤，請檢查形狀是否匹配。
- **效能**：對於大型模型較慢——生產環境請使用 PyTorch。
- **更新**：TinyGrad 發展迅速；請查看儲存庫以獲取最新版本。

更多詳細資訊，請參閱 [docs/README.md](https://github.com/geohot/tinygrad/blob/master/README.md) 或本地執行範例。如果你有特定使用案例，請提供更多細節以獲得量身定制的建議！