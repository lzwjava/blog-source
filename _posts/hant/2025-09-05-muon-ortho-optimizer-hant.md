---
audio: false
generated: true
image: false
lang: hant
layout: post
title: PyTorch 正交化介子優化器
translated: true
type: note
---

瞭解了——這是一個簡潔的 PyTorch 參考實現，你可以直接用在專案中。它包含：

* 一個微型的 Newton–Schulz 逆平方根方法，用於正交化 2-D 更新
* 一個 `Muon` 優化器（AdamW 風格的權重衰減、動量，可選的 RMS 縮放）
* 對 1-D 張量（偏置、LayerNorm 權重）的後備處理
* 一個最小化的訓練範例

---

### 1) 矩陣正交化輔助函數

```python
# muon_utils.py
import torch

@torch.no_grad()
def orthogonalize_by_svd(G: torch.Tensor) -> torch.Tensor:
    """
    最近正交矩陣（Procrustes）：Q = U @ Vh，其中 G = U S Vh。
    精確但對大矩陣可能較慢。
    """
    U, _, Vh = torch.linalg.svd(G, full_matrices=False)
    return U @ Vh

@torch.no_grad()
def inv_sqrt_newton_schulz(A: torch.Tensor, iters: int = 5, eps: float = 1e-6) -> torch.Tensor:
    """
    使用 Newton–Schulz 迭代計算 SPD 矩陣 A 的 A^{-1/2}。
    假設 A 是對稱正定矩陣（例如，G^T G + eps I）。
    """
    # 歸一化以獲得更好的收斂性
    trace = A.diagonal(offset=0, dim1=-2, dim2=-1).sum(-1, keepdim=True).unsqueeze(-1)  # (...,1,1)
    A_norm = A / (trace + eps)

    I = torch.eye(A.size(-1), device=A.device, dtype=A.dtype).expand_as(A)
    Y = A_norm.clone()
    Z = I.clone()

    for _ in range(iters):
        T = 0.5 * (3*I - Z @ Y)
        Y = Y @ T
        Z = T @ Z

    # A^{-1/2} ≈ Z / sqrt(trace)
    return Z / torch.sqrt(trace + eps)

@torch.no_grad()
def orthogonalize_by_newton_schulz(G: torch.Tensor, iters: int = 5, eps: float = 1e-6) -> torch.Tensor:
    """
    Q ≈ G (G^T G)^{-1/2}，使用 Newton–Schulz 迭代計算逆平方根。
    """
    # 使其成為 SPD；添加 eps*I 以確保數值穩定性
    S = G.transpose(-1, -2) @ G
    n = S.size(-1)
    S = S + eps * torch.eye(n, device=S.device, dtype=S.dtype)
    S_inv_sqrt = inv_sqrt_newton_schulz(S, iters=iters, eps=eps)
    return G @ S_inv_sqrt
```

---

### 2) Muon 優化器

```python
# muon.py
from torch.optim.optimizer import Optimizer
import torch
from muon_utils import orthogonalize_by_newton_schulz, orthogonalize_by_svd

class Muon(Optimizer):
    r"""
    Muon：結構感知、矩陣正交化優化器。
    - 梯度動量
    - 解耦權重衰減（AdamW 風格）
    - 對於 2D 參數：正交化動量平均更新（Newton–Schulz 或 SVD）
    - 對於 1D/其他形狀張量：像 Adam 一樣對動量進行 RMS 縮放（無正交化）

    參數：
        params: 參數迭代器
        lr (float): 學習率
        beta (float): 動量因子（預設 0.9）
        weight_decay (float): 解耦權重衰減（預設 0.01）
        eps (float): 數值 epsilon（預設 1e-8）
        ns_iters (int): 正交化的 Newton–Schulz 迭代次數（預設 5）
        method (str): 'ns' 表示 Newton–Schulz（預設），或 'svd'
        rms_scale (bool): 對非 2D 張量應用逐張量 RMS 歸一化到動量（預設 True）
        clip_grad_norm (float|None): 如果設定，在應用前按 L2 範數裁剪動量更新（預設 None）
    """
    def __init__(
        self,
        params,
        lr: float,
        beta: float = 0.9,
        weight_decay: float = 0.01,
        eps: float = 1e-8,
        ns_iters: int = 5,
        method: str = "ns",
        rms_scale: bool = True,
        clip_grad_norm: float | None = None,
    ):
        if lr <= 0:
            raise ValueError("Invalid learning rate")
        if not 0.0 <= beta < 1.0:
            raise ValueError("Invalid beta")
        defaults = dict(
            lr=lr,
            beta=beta,
            weight_decay=weight_decay,
            eps=eps,
            ns_iters=ns_iters,
            method=method,
            rms_scale=rms_scale,
            clip_grad_norm=clip_grad_norm,
        )
        super().__init__(params, defaults)

    @torch.no_grad()
    def step(self, closure=None):
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()

        for group in self.param_groups:
            lr = group["lr"]
            beta = group["beta"]
            wd = group["weight_decay"]
            eps = group["eps"]
            ns_iters = group["ns_iters"]
            method = group["method"]
            rms_scale = group["rms_scale"]
            clip_gn = group["clip_grad_norm"]

            for p in group["params"]:
                if p.grad is None:
                    continue

                grad = p.grad
                state = self.state[p]

                # 動量緩衝區
                if "momentum" not in state:
                    state["momentum"] = torch.zeros_like(p, memory_format=torch.preserve_format)
                m = state["momentum"]

                # m_t = beta*m_{t-1} + (1-beta)*g_t
                m.mul_(beta).add_(grad, alpha=(1.0 - beta))

                # 可選的全局裁剪（對更新方向，即動量）
                if clip_gn is not None:
                    gnorm = m.norm()
                    if gnorm > clip_gn:
                        m.mul_(clip_gn / (gnorm + 1e-12))

                # 對參數進行解耦權重衰減
                if wd != 0.0:
                    p.mul_(1.0 - lr * wd)

                # 計算更新方向 U
                if p.ndim == 2:
                    # 正交化矩陣更新
                    if method == "svd":
                        U = orthogonalize_by_svd(m)
                    else:
                        U = orthogonalize_by_newton_schulz(m, iters=ns_iters, eps=eps)
                else:
                    # 非矩陣張量：RMS 縮放（類 Adam）以保持步長平衡
                    if rms_scale:
                        rms = torch.sqrt(m.pow(2).mean() + eps)
                        U = m / rms
                    else:
                        U = m

                # 參數更新
                p.add_(U, alpha=-lr)

        return loss
```

---

### 3) 最小化使用範例

```python
# demo_muon.py
import torch
from torch import nn
from muon import Muon

# 玩具模型
model = nn.Sequential(
    nn.Linear(256, 512),
    nn.ReLU(),
    nn.Linear(512, 256),
)

x = torch.randn(32, 256)
y = torch.randn(32, 256)

criterion = nn.MSELoss()

# 嘗試 Newton–Schulz 正交化（快速且可擴展）。使用 method='svd' 以獲得精確結果。
optimizer = Muon(model.parameters(), lr=3e-4, beta=0.9, weight_decay=0.02, ns_iters=5, method="ns")

for step in range(200):
    optimizer.zero_grad(set_to_none=True)
    pred = model(x)
    loss = criterion(pred, y)
    loss.backward()
    optimizer.step()

    if (step + 1) % 20 == 0:
        print(f"step {step+1:03d} | loss = {loss.item():.4f}")
```

---

### 注意事項與提示

* 對於非常大的權重矩陣，`method="ns"` 避免了 SVD，通常更快。如果你在小層上驗證正確性，可以與 `method="svd"` 進行比較以進行檢查。
* `ns_iters=3..6` 是一個實用的範圍。迭代次數越少 = 越快但正交化精度稍低。
* 保持較小的 `weight_decay`（解耦）和適中的 `beta`（例如 0.9）。對於 transformers/MLPs，學習率在 `1e-3` 到 `3e-4` 左右是一個合理的起點。
* 如果訓練出現尖峰，請在構造函數中啟用 `clip_grad_norm`（例如 `1.0–5.0`）。

如果你需要，我可以根據你的具體模型設置（例如 torch.compile、FSDP/ZeRO、MoE 層、自定義每參數配置）來調整此代碼。