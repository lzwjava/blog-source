---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Optimiseur de Muons avec Orthogonalisation pour PyTorch
translated: true
type: note
---

Parfait — voici une implémentation de référence PyTorch prête à l'emploi. Elle inclut :

* Une petite méthode Newton–Schulz pour le calcul de la racine carrée inverse afin d'orthogonaliser les mises à jour 2-D
* Un optimiseur `Muon` (décroissance de poids de type AdamW, momentum, mise à l'échelle RMS optionnelle)
* Une solution de repli pour les tenseurs 1-D (biais, poids des LayerNorm)
* Un exemple d'entraînement minimal

---

### 1) Helpers pour l'orthogonalisation de matrices

```python
# muon_utils.py
import torch

@torch.no_grad()
def orthogonalize_by_svd(G: torch.Tensor) -> torch.Tensor:
    """
    Orthogonal le plus proche (Procrustes) : Q = U @ Vh, où G = U S Vh.
    Exact mais peut être plus lent sur les grandes matrices.
    """
    U, _, Vh = torch.linalg.svd(G, full_matrices=False)
    return U @ Vh

@torch.no_grad()
def inv_sqrt_newton_schulz(A: torch.Tensor, iters: int = 5, eps: float = 1e-6) -> torch.Tensor:
    """
    Calcule A^{-1/2} pour A SDP via Newton–Schulz.
    Suppose que A est symétrique définie positive (ex. : G^T G + eps I).
    """
    # Normaliser pour une meilleure convergence
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
    Q ≈ G (G^T G)^{-1/2}, en utilisant Newton–Schulz pour la racine carrée inverse.
    """
    # Rendre SDP ; ajouter eps*I pour la stabilité numérique
    S = G.transpose(-1, -2) @ G
    n = S.size(-1)
    S = S + eps * torch.eye(n, device=S.device, dtype=S.dtype)
    S_inv_sqrt = inv_sqrt_newton_schulz(S, iters=iters, eps=eps)
    return G @ S_inv_sqrt
```

---

### 2) Optimiseur Muon

```python
# muon.py
from torch.optim.optimizer import Optimizer
import torch
from muon_utils import orthogonalize_by_newton_schulz, orthogonalize_by_svd

class Muon(Optimizer):
    r"""
    Muon : un optimiseur qui préserve la structure et orthogonalise les matrices.
    - Momentum sur les gradients
    - Décroissance de poids découplée (style AdamW)
    - Pour les paramètres 2D : orthogonalise la mise à jour moyennée par momentum (Newton–Schulz ou SVD)
    - Pour les autres formes (1D, etc.) : mise à l'échelle RMS sur le momentum comme Adam (pas d'orthogonalisation)

    Args:
        params: itérable de paramètres
        lr (float): taux d'apprentissage
        beta (float): facteur de momentum (défaut 0.9)
        weight_decay (float): décroissance de poids découplée (défaut 0.01)
        eps (float): eps numérique (défaut 1e-8)
        ns_iters (int): itérations de Newton–Schulz pour l'orthogonalisation (défaut 5)
        method (str): 'ns' pour Newton–Schulz (défaut), ou 'svd'
        rms_scale (bool): appliquer une normalisation RMS par tenseur au momentum pour les tenseurs non-2D (défaut True)
        clip_grad_norm (float|None): si défini, limite la norme L2 de la mise à jour de momentum avant application (défaut None)
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
            raise ValueError("Taux d'apprentissage invalide")
        if not 0.0 <= beta < 1.0:
            raise ValueError("Beta invalide")
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

                # Buffer de momentum
                if "momentum" not in state:
                    state["momentum"] = torch.zeros_like(p, memory_format=torch.preserve_format)
                m = state["momentum"]

                # m_t = beta*m_{t-1} + (1-beta)*g_t
                m.mul_(beta).add_(grad, alpha=(1.0 - beta))

                # Optionnel : clipping global sur la direction de mise à jour (momentum)
                if clip_gn is not None:
                    gnorm = m.norm()
                    if gnorm > clip_gn:
                        m.mul_(clip_gn / (gnorm + 1e-12))

                # Décroissance de poids découplée sur les paramètres
                if wd != 0.0:
                    p.mul_(1.0 - lr * wd)

                # Calcul de la direction de mise à jour U
                if p.ndim == 2:
                    # Orthogonaliser la mise à jour matricielle
                    if method == "svd":
                        U = orthogonalize_by_svd(m)
                    else:
                        U = orthogonalize_by_newton_schulz(m, iters=ns_iters, eps=eps)
                else:
                    # Tenseurs non-matriciels : mise à l'échelle RMS (style Adam) pour équilibrer les tailles de pas
                    if rms_scale:
                        rms = torch.sqrt(m.pow(2).mean() + eps)
                        U = m / rms
                    else:
                        U = m

                # Mise à jour du paramètre
                p.add_(U, alpha=-lr)

        return loss
```

---

### 3) Exemple d'utilisation minimal

```python
# demo_muon.py
import torch
from torch import nn
from muon import Muon

# Modèle jouet
model = nn.Sequential(
    nn.Linear(256, 512),
    nn.ReLU(),
    nn.Linear(512, 256),
)

x = torch.randn(32, 256)
y = torch.randn(32, 256)

criterion = nn.MSELoss()

# Essayer l'orthogonalisation Newton–Schulz (rapide et scalable). Utiliser method='svd' pour l'exactitude.
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

### Notes & conseils

* Pour les très grandes matrices de poids, `method="ns"` évite la SVD et est généralement bien plus rapide. Si vous validez la justesse sur de petites couches, comparez avec `method="svd"` pour vérifier.
* `ns_iters=3..6` est une plage pratique. Moins d'itérations = plus rapide mais orthogonalisation légèrement moins précise.
* Gardez une petite `weight_decay` (découplée) et un `beta` modéré (ex. : 0.9). Un taux d'apprentissage autour de `1e-3` à `3e-4` est un point de départ raisonnable pour les transformers/MLPs.
* Si l'entraînement devient instable, activez `clip_grad_norm` (ex. : `1.0–5.0`) dans le constructeur.

Si vous le souhaitez, je peux adapter ceci à votre configuration de modèle exacte (ex. : torch.compile, FSDP/ZeRO, couches MoE, configurations personnalisées par paramètre).