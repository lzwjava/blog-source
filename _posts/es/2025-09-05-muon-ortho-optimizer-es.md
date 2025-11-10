---
audio: false
generated: true
image: false
lang: es
layout: post
title: Optimizador de Muones con Ortogonalización para PyTorch
translated: true
type: note
---

Entendido—aquí tienes una implementación de referencia limpia en PyTorch que puedes incorporar directamente en un proyecto. Incluye:

* Una pequeña función Newton–Schulz de raíz cuadrada inversa para ortogonalizar actualizaciones 2-D
* Un optimizador `Muon` (decaimiento de pesos estilo AdamW, momentum, escalado RMS opcional)
* Un respaldo para tensores 1-D (sesgos, pesos de LayerNorm)
* Un ejemplo mínimo de entrenamiento

---

### 1) Ayudantes de ortogonalización de matrices

```python
# muon_utils.py
import torch

@torch.no_grad()
def orthogonalize_by_svd(G: torch.Tensor) -> torch.Tensor:
    """
    Ortogonal más cercano (Procrustes): Q = U @ Vh, donde G = U S Vh.
    Exacto pero puede ser más lento en matrices grandes.
    """
    U, _, Vh = torch.linalg.svd(G, full_matrices=False)
    return U @ Vh

@torch.no_grad()
def inv_sqrt_newton_schulz(A: torch.Tensor, iters: int = 5, eps: float = 1e-6) -> torch.Tensor:
    """
    Calcula A^{-1/2} para A SPD usando Newton–Schulz.
    Asume que A es simétrica definida positiva (ej., G^T G + eps I).
    """
    # Normalizar para mejor convergencia
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
    Q ≈ G (G^T G)^{-1/2}, usando Newton–Schulz para la raíz cuadrada inversa.
    """
    # Hacer SPD; añadir eps*I para estabilidad numérica
    S = G.transpose(-1, -2) @ G
    n = S.size(-1)
    S = S + eps * torch.eye(n, device=S.device, dtype=S.dtype)
    S_inv_sqrt = inv_sqrt_newton_schulz(S, iters=iters, eps=eps)
    return G @ S_inv_sqrt
```

---

### 2) Optimizador Muon

```python
# muon.py
from torch.optim.optimizer import Optimizer
import torch
from muon_utils import orthogonalize_by_newton_schulz, orthogonalize_by_svd

class Muon(Optimizer):
    r"""
    Muon: optimizador que ortogonaliza matrices y es consciente de la estructura.
    - Momentum en los gradientes
    - Decaimiento de pesos desacoplado (estilo AdamW)
    - Para parámetros 2D: ortogonaliza la actualización promediada por momentum (Newton–Schulz o SVD)
    - Para formas 1D/otras: escalado RMS en el momentum como Adam (sin ortogonalización)

    Args:
        params: iterable de parámetros
        lr (float): tasa de aprendizaje
        beta (float): factor de momentum (por defecto 0.9)
        weight_decay (float): decaimiento de pesos desacoplado (por defecto 0.01)
        eps (float): épsilon numérico (por defecto 1e-8)
        ns_iters (int): iteraciones de Newton–Schulz para ortogonalización (por defecto 5)
        method (str): 'ns' para Newton–Schulz (por defecto), o 'svd'
        rms_scale (bool): aplicar normalización RMS por tensor al momentum para tensores no 2D (por defecto True)
        clip_grad_norm (float|None): si se establece, recorta la actualización de momentum por norma L2 antes de aplicar (por defecto None)
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
            raise ValueError("Tasa de aprendizaje inválida")
        if not 0.0 <= beta < 1.0:
            raise ValueError("Beta inválido")
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

                # Búfer de momentum
                if "momentum" not in state:
                    state["momentum"] = torch.zeros_like(p, memory_format=torch.preserve_format)
                m = state["momentum"]

                # m_t = beta*m_{t-1} + (1-beta)*g_t
                m.mul_(beta).add_(grad, alpha=(1.0 - beta))

                # Recorte global opcional en la dirección de actualización (momentum)
                if clip_gn is not None:
                    gnorm = m.norm()
                    if gnorm > clip_gn:
                        m.mul_(clip_gn / (gnorm + 1e-12))

                # Decaimiento de pesos desacoplado en los parámetros
                if wd != 0.0:
                    p.mul_(1.0 - lr * wd)

                # Calcular dirección de actualización U
                if p.ndim == 2:
                    # Ortogonalizar la actualización de la matriz
                    if method == "svd":
                        U = orthogonalize_by_svd(m)
                    else:
                        U = orthogonalize_by_newton_schulz(m, iters=ns_iters, eps=eps)
                else:
                    # Tensores no matriciales: escalado RMS (estilo Adam) para mantener equilibrados los tamaños de paso
                    if rms_scale:
                        rms = torch.sqrt(m.pow(2).mean() + eps)
                        U = m / rms
                    else:
                        U = m

                # Actualización del parámetro
                p.add_(U, alpha=-lr)

        return loss
```

---

### 3) Ejemplo mínimo de uso

```python
# demo_muon.py
import torch
from torch import nn
from muon import Muon

# Modelo de juguete
model = nn.Sequential(
    nn.Linear(256, 512),
    nn.ReLU(),
    nn.Linear(512, 256),
)

x = torch.randn(32, 256)
y = torch.randn(32, 256)

criterion = nn.MSELoss()

# Probar ortogonalización Newton–Schulz (rápida y escalable). Usar method='svd' para exactitud.
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

### Notas y consejos

* Para matrices de pesos muy grandes, `method="ns"` evita SVD y es típicamente mucho más rápido. Si estás validando corrección en capas pequeñas, compara con `method="svd"` para verificar.
* `ns_iters=3..6` es un rango práctico bueno. Menos iteraciones = más rápido pero ortogonalización ligeramente menos precisa.
* Mantén un `weight_decay` pequeño (desacoplado) y un `beta` moderado (ej., 0.9). Una tasa de aprendizaje alrededor de `1e-3` a `3e-4` es un punto de partida razonable para transformers/MLPs.
* Si el entrenamiento se vuelve irregular, habilita `clip_grad_norm` (ej., `1.0–5.0`) en el constructor.

Si lo deseas, puedo adaptar esto a tu configuración exacta de modelo (ej., torch.compile, FSDP/ZeRO, capas MoE, configuraciones personalizadas por parámetro).