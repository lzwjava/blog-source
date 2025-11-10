---
audio: false
generated: true
image: false
lang: ja
layout: post
title: PyTorch向け直交化機能付きミューオンオプティマイザー
translated: true
type: note
---

了解しました。プロジェクトにそのまま組み込めるクリーンなPyTorchリファレンス実装を以下に示します。これには以下が含まれます：

* 2次元更新を直交化する小さなNewton–Schulz逆平方根関数
* `Muon`オプティマイザ（AdamWスタイルの重み減衰、モーメンタム、オプションのRMSスケーリング）
* 1次元テンソル用のフォールバック（バイアス、LayerNormの重み）
* 最小限のトレーニング例

---

### 1) 行列直交化ヘルパー

```python
# muon_utils.py
import torch

@torch.no_grad()
def orthogonalize_by_svd(G: torch.Tensor) -> torch.Tensor:
    """
    最近接直交行列（Procrustes問題）: Q = U @ Vh、ここで G = U S Vh。
    正確だが大きな行列では遅くなる可能性があります。
    """
    U, _, Vh = torch.linalg.svd(G, full_matrices=False)
    return U @ Vh

@torch.no_grad()
def inv_sqrt_newton_schulz(A: torch.Tensor, iters: int = 5, eps: float = 1e-6) -> torch.Tensor:
    """
    Newton–Schulz法を使用して対称正定行列（SPD）Aの A^{-1/2} を計算します。
    Aが対称正定行列（例：G^T G + eps I）であることを前提とします。
    """
    # 収束性向上のための正規化
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
    Q ≈ G (G^T G)^{-1/2}、逆平方根にNewton–Schulz法を使用。
    """
    # 対称正定行列（SPD）化。数値安定性のために eps*I を追加
    S = G.transpose(-1, -2) @ G
    n = S.size(-1)
    S = S + eps * torch.eye(n, device=S.device, dtype=S.dtype)
    S_inv_sqrt = inv_sqrt_newton_schulz(S, iters=iters, eps=eps)
    return G @ S_inv_sqrt
```

---

### 2) Muonオプティマイザ

```python
# muon.py
from torch.optim.optimizer import Optimizer
import torch
from muon_utils import orthogonalize_by_newton_schulz, orthogonalize_by_svd

class Muon(Optimizer):
    r"""
    Muon: 構造を考慮した、行列を直交化するオプティマイザ。
    - 勾配に対するモーメンタム
    - 分離された重み減衰（AdamWスタイル）
    - 2次元パラメータの場合：モーメンタム平均更新を直交化（Newton–SchulzまたはSVD）
    - 1次元/その他の形状の場合：AdamのようなモーメンタムへのRMSスケーリング（直交化なし）

    引数:
        params: パラメータのイテラブル
        lr (float): 学習率
        beta (float): モーメンタム係数（デフォルト 0.9）
        weight_decay (float): 分離された重み減衰（デフォルト 0.01）
        eps (float): 数値計算用eps（デフォルト 1e-8）
        ns_iters (int): 直交化のためのNewton–Schulz反復回数（デフォルト 5）
        method (str): 'ns'（Newton–Schulz、デフォルト）または 'svd'
        rms_scale (bool): 2次元以外のテンソルに対してモーメンタムにテンソル単位のRMS正規化を適用する（デフォルト True）
        clip_grad_norm (float|None): 設定された場合、適用前にL2ノルムでモーメンタム更新をクリップする（デフォルト None）
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

                # モーメンタムバッファ
                if "momentum" not in state:
                    state["momentum"] = torch.zeros_like(p, memory_format=torch.preserve_format)
                m = state["momentum"]

                # m_t = beta*m_{t-1} + (1-beta)*g_t
                m.mul_(beta).add_(grad, alpha=(1.0 - beta))

                # 更新方向（モーメンタム）に対するオプションのグローバルクリップ
                if clip_gn is not None:
                    gnorm = m.norm()
                    if gnorm > clip_gn:
                        m.mul_(clip_gn / (gnorm + 1e-12))

                # パラメータに対する分離された重み減衰
                if wd != 0.0:
                    p.mul_(1.0 - lr * wd)

                # 更新方向Uを計算
                if p.ndim == 2:
                    # 行列更新を直交化
                    if method == "svd":
                        U = orthogonalize_by_svd(m)
                    else:
                        U = orthogonalize_by_newton_schulz(m, iters=ns_iters, eps=eps)
                else:
                    # 非行列テンソル：ステップサイズを均衡に保つためのRMSスケーリング（Adam風）
                    if rms_scale:
                        rms = torch.sqrt(m.pow(2).mean() + eps)
                        U = m / rms
                    else:
                        U = m

                # パラメータ更新
                p.add_(U, alpha=-lr)

        return loss
```

---

### 3) 最小限の使用例

```python
# demo_muon.py
import torch
from torch import nn
from muon import Muon

# トイモデル
model = nn.Sequential(
    nn.Linear(256, 512),
    nn.ReLU(),
    nn.Linear(512, 256),
)

x = torch.randn(32, 256)
y = torch.randn(32, 256)

criterion = nn.MSELoss()

# Newton–Schulz直交化を試す（高速でスケーラブル）。正確な計算にはmethod='svd'を使用。
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

### 注意点とヒント

* 非常に大きな重み行列の場合、`method="ns"`はSVDを回避し、通常はるかに高速です。小さなレイヤーで正確性を検証する場合、`method="svd"`と比較してサニティチェックを行ってください。
* `ns_iters=3..6`が実用的な範囲です。反復回数が少ないほど高速ですが、直交化の精度はわずかに低下します。
* 小さな`weight_decay`（分離型）と適度な`beta`（例：0.9）を維持してください。学習率は`1e-3`から`3e-4`程度がトランスフォーマー/MLPの合理的な出発点です。
* トレーニングが不安定になる場合は、コンストラクタで`clip_grad_norm`（例：`1.0–5.0`）を有効にしてください。

必要に応じて、これを正確なモデル設定（例：torch.compile、FSDP/ZeRO、MoEレイヤー、カスタムのパラメータ単位設定）に適合させることもできます。