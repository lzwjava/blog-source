---
audio: false
generated: true
image: false
lang: ar
layout: post
title: محسن الميون مع التعامد لـ PyTorch
translated: true
type: note
---

حسناً—إليك تنفيذ مرجعي نظيف في PyTorch يمكنك إدراجه مباشرة في مشروعك. يشمل:

* خوارزمية Newton–Schulz صغيرة لحساب الجذر التربيعي العكسي لتتعامد تحديثات المصفوفات ثنائية الأبعاد.
* مُحسّن `Muon` (تناقص الوزن على غرار AdamW، الزخم، تحجيم RMS اختياري).
* حل بديل للموترات أحادية البعد (مثل الانحياز، وأوزان LayerNorm).
* مثال تدريب بسيط.

---

### 1) دواعد تعامد المصفوفات

```python
# muon_utils.py
import torch

@torch.no_grad()
def orthogonalize_by_svd(G: torch.Tensor) -> torch.Tensor:
    """
    أقرب مصفوفة متعامدة (Procrustes): Q = U @ Vh، حيث G = U S Vh.
    دقيق ولكن يمكن أن يكون أبطأ على المصفوفات الكبيرة.
    """
    U, _, Vh = torch.linalg.svd(G, full_matrices=False)
    return U @ Vh

@torch.no_grad()
def inv_sqrt_newton_schulz(A: torch.Tensor, iters: int = 5, eps: float = 1e-6) -> torch.Tensor:
    """
    احسب A^{-1/2} للمصفوفة المتناظرة موجبة التحديد (SPD) باستخدام Newton–Schulz.
    تفترض أن A متناظرة موجبة التحديد (مثل G^T G + eps I).
    """
    # تطبيع لتحسين التقارب
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
    Q ≈ G (G^T G)^{-1/2}، باستخدام Newton–Schulz لحساب الجذر التربيعي العكسي.
    """
    # اجعلها متناظرة موجبة التحديد (SPD); أضف eps*I للاستقرار العددي
    S = G.transpose(-1, -2) @ G
    n = S.size(-1)
    S = S + eps * torch.eye(n, device=S.device, dtype=S.dtype)
    S_inv_sqrt = inv_sqrt_newton_schulz(S, iters=iters, eps=eps)
    return G @ S_inv_sqrt
```

---

### 2) مُحسّن Muon

```python
# muon.py
from torch.optim.optimizer import Optimizer
import torch
from muon_utils import orthogonalize_by_newton_schulz, orthogonalize_by_svd

class Muon(Optimizer):
    r"""
    Muon: مُحسّن يراعي البنية ويُعامل المصفوفات.
    - زخم على المتجهات التفاضلية (grads)
    - تناقص وزن منفصل (على غرار AdamW)
    - للمعاملات ثنائية الأبعاد: جعل تحديث متوسط الزخم متعامداً (باستخدام Newton–Schulz أو SVD)
    - للأشكال أحادية البعد/أخرى: تطبيق تحجيم RMS على الزخم مثل Adam (بدون تعامد)

    الوسائط:
        params: كائن قابل للتكرار للمعاملات
        lr (float): معدل التعلم
        beta (float): معامل الزخم (الافتراضي 0.9)
        weight_decay (float): تناقص الوزن المنفصل (الافتراضي 0.01)
        eps (float): قيمة إبسيلون عددية (الافتراضي 1e-8)
        ns_iters (int): تكرارات Newton–Schulz للتعامد (الافتراضي 5)
        method (str): 'ns' لـ Newton–Schulz (الافتراضي)، أو 'svd'
        rms_scale (bool): تطبيع RMS لكل موتر على الموترات غير ثنائية الأبعاد (الافتراضي True)
        clip_grad_norm (float|None): إذا تم تعيينه، اقتص تحديث الزخم بالمعيار L2 قبل التطبيق (الافتراضي None)
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
            raise ValueError("معدل التعلم غير صالح")
        if not 0.0 <= beta < 1.0:
            raise ValueError("قيمة beta غير صالحة")
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

                # مخزن مؤقت للزخم
                if "momentum" not in state:
                    state["momentum"] = torch.zeros_like(p, memory_format=torch.preserve_format)
                m = state["momentum"]

                # m_t = beta*m_{t-1} + (1-beta)*g_t
                m.mul_(beta).add_(grad, alpha=(1.0 - beta))

                # اقتص عام اختياري لاتجاه التحديث (الزخم)
                if clip_gn is not None:
                    gnorm = m.norm()
                    if gnorm > clip_gn:
                        m.mul_(clip_gn / (gnorm + 1e-12))

                # تناقص الوزن المنفصل على المعاملات
                if wd != 0.0:
                    p.mul_(1.0 - lr * wd)

                # احسب اتجاه التحديث U
                if p.ndim == 2:
                    # جعل تحديث المصفوفة متعامداً
                    if method == "svd":
                        U = orthogonalize_by_svd(m)
                    else:
                        U = orthogonalize_by_newton_schulz(m, iters=ns_iters, eps=eps)
                else:
                    # الموترات غير المصفوفية: تحجيم RMS (مشابه لـ Adam) للحفاظ على توازن أحجام الخطوات
                    if rms_scale:
                        rms = torch.sqrt(m.pow(2).mean() + eps)
                        U = m / rms
                    else:
                        U = m

                # تحديث المعامل
                p.add_(U, alpha=-lr)

        return loss
```

---

### 3) مثال استخدام بسيط

```python
# demo_muon.py
import torch
from torch import nn
from muon import Muon

# نموذج بسيط
model = nn.Sequential(
    nn.Linear(256, 512),
    nn.ReLU(),
    nn.Linear(512, 256),
)

x = torch.randn(32, 256)
y = torch.randn(32, 256)

criterion = nn.MSELoss()

# جرب التعامد باستخدام Newton–Schulz (سريع وقابل للتوسع). استخدم method='svd' للدقة.
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

### ملاحظات ونصائح

* بالنسبة لمصفوفات الأوزان كبيرة الحجم جداً، `method="ns"` يتجنب SVD وعادة ما يكون أسرع بكثير. إذا كنت تتحقق من الصحة على طبقات صغيرة، قارن مع `method="svd"` للتحقق من السلامة.
* `ns_iters=3..6` نطاق عملي جيد. تكرارات أقل = أسرع ولكن مع تعامد أقل دقة قليلاً.
* حافظ على `weight_decay` صغير (منفصل) و `beta` معتدل (مثلاً 0.9). معدل تعلم حول `1e-3` إلى `3e-4` نقطة بداية معقولة لمحولات الطاقة/شبكات MLP.
* إذا أصبح التدريب متقلباً، شغّل `clip_grad_norm` (مثلاً `1.0–5.0`) في المُنشئ.

إذا أردت، يمكنني تكييف هذا مع إعدادات نموذجك الدقيقة (مثلاً، torch.compile، FSDP/ZeRO، طبقات MoE، إعدادات مخصصة لكل معامل).