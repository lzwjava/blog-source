---
audio: false
generated: true
image: false
lang: de
layout: post
title: Muon-Optimierer mit Orthogonalisierung für PyTorch
translated: true
type: note
---

Verstanden – hier ist eine saubere PyTorch-Referenzimplementierung, die du direkt in ein Projekt einfügen kannst. Sie beinhaltet:

* Eine kleine Newton–Schulz-Inverse-Quadratwurzel zur Orthogonalisierung von 2-D-Updates
* Einen `Muon`-Optimierer (AdamW-artiger Weight Decay, Momentum, optionale RMS-Skalierung)
* Einen Fallback für 1-D-Tensoren (Bias, LayerNorm-Gewichte)
* Ein minimales Trainingsbeispiel

---

### 1) Hilfsfunktionen zur Matrixorthogonalisierung

```python
# muon_utils.py
import torch

@torch.no_grad()
def orthogonalize_by_svd(G: torch.Tensor) -> torch.Tensor:
    """
    Nächstgelegene orthogonale Matrix (Procrustes): Q = U @ Vh, wobei G = U S Vh.
    Exakt, kann aber bei großen Matrizen langsamer sein.
    """
    U, _, Vh = torch.linalg.svd(G, full_matrices=False)
    return U @ Vh

@torch.no_grad()
def inv_sqrt_newton_schulz(A: torch.Tensor, iters: int = 5, eps: float = 1e-6) -> torch.Tensor:
    """
    Berechne A^{-1/2} für SPD A mittels Newton–Schulz.
    Nimmt an, dass A symmetrisch positiv definit ist (z.B. G^T G + eps I).
    """
    # Normalisierung für bessere Konvergenz
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
    Q ≈ G (G^T G)^{-1/2}, unter Verwendung von Newton–Schulz für die inverse Quadratwurzel.
    """
    # Mache SPD; füge eps*I für numerische Stabilität hinzu
    S = G.transpose(-1, -2) @ G
    n = S.size(-1)
    S = S + eps * torch.eye(n, device=S.device, dtype=S.dtype)
    S_inv_sqrt = inv_sqrt_newton_schulz(S, iters=iters, eps=eps)
    return G @ S_inv_sqrt
```

---

### 2) Muon-Optimierer

```python
# muon.py
from torch.optim.optimizer import Optimizer
import torch
from muon_utils import orthogonalize_by_newton_schulz, orthogonalize_by_svd

class Muon(Optimizer):
    r"""
    Muon: strukturbewusster, matrixorthogonalisierender Optimierer.
    - Momentum auf Gradienten
    - Entkoppelter Weight Decay (AdamW-Stil)
    - Für 2D-Params: Orthogonalisiere den Momentum-avg-Update (Newton–Schulz oder SVD)
    - Für 1D/andere Formen: RMS-Skalierung auf Momentum wie bei Adam (keine Orthogonalisierung)

    Args:
        params: iterierbare Parameter
        lr (float): Lernrate
        beta (float): Momentum-Faktor (default 0.9)
        weight_decay (float): entkoppelter Weight Decay (default 0.01)
        eps (float): numerisches Epsilon (default 1e-8)
        ns_iters (int): Newton–Schulz-Iterationen für Orthogonalisierung (default 5)
        method (str): 'ns' für Newton–Schulz (default), oder 'svd'
        rms_scale (bool): RMS-Normalisierung pro Tensor für Nicht-2D-Tensoren anwenden (default True)
        clip_grad_norm (float|None): falls gesetzt, begrenze Momentum-Update per L2-Norm vor Anwendung (default None)
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
            raise ValueError("Ungültige Lernrate")
        if not 0.0 <= beta < 1.0:
            raise ValueError("Ungültiges Beta")
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

                # Momentum-Puffer
                if "momentum" not in state:
                    state["momentum"] = torch.zeros_like(p, memory_format=torch.preserve_format)
                m = state["momentum"]

                # m_t = beta*m_{t-1} + (1-beta)*g_t
                m.mul_(beta).add_(grad, alpha=(1.0 - beta))

                # Optionale globale Begrenzung der Update-Richtung (Momentum)
                if clip_gn is not None:
                    gnorm = m.norm()
                    if gnorm > clip_gn:
                        m.mul_(clip_gn / (gnorm + 1e-12))

                # Entkoppelter Weight Decay auf Parametern
                if wd != 0.0:
                    p.mul_(1.0 - lr * wd)

                # Berechne Update-Richtung U
                if p.ndim == 2:
                    # Orthogonalisiere das Matrix-Update
                    if method == "svd":
                        U = orthogonalize_by_svd(m)
                    else:
                        U = orthogonalize_by_newton_schulz(m, iters=ns_iters, eps=eps)
                else:
                    # Nicht-Matrix-Tensoren: RMS-Skalierung (Adam-ähnlich) zur Balancierung der Schrittweiten
                    if rms_scale:
                        rms = torch.sqrt(m.pow(2).mean() + eps)
                        U = m / rms
                    else:
                        U = m

                # Parameter-Update
                p.add_(U, alpha=-lr)

        return loss
```

---

### 3) Minimales Anwendungsbeispiel

```python
# demo_muon.py
import torch
from torch import nn
from muon import Muon

# Beispielmodell
model = nn.Sequential(
    nn.Linear(256, 512),
    nn.ReLU(),
    nn.Linear(512, 256),
)

x = torch.randn(32, 256)
y = torch.randn(32, 256)

criterion = nn.MSELoss()

# Versuche Newton–Schulz-Orthogonalisierung (schnell & skalierbar). Verwende method='svd' für exakt.
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

### Hinweise & Tipps

* Für sehr große Gewichtsmatrizen vermeidet `method="ns"` SVD und ist typischerweise viel schneller. Wenn du die Korrektheit auf kleinen Layern validierst, vergleiche mit `method="svd"` zur Kontrolle.
* `ns_iters=3..6` ist ein guter praktischer Bereich. Weniger Iterationen = schneller, aber etwas weniger präzise Orthogonalisierung.
* Behalte einen kleinen `weight_decay` (entkoppelt) und ein moderates `beta` (z.B. 0.9). Eine Lernrate um `1e-3` bis `3e-4` ist ein vernünftiger Startpunkt für Transformer/MLPs.
* Falls das Training sprunghaft wird, aktiviere `clip_grad_norm` (z.B. `1.0–5.0`) im Konstruktor.

Falls gewünscht, kann ich dies an dein exaktes Modell-Setup anpassen (z.B. torch.compile, FSDP/ZeRO, MoE-Layer, benutzerdefinierte Per-Param-Konfigurationen).