---
audio: false
generated: true
image: false
lang: hi
layout: post
title: पाइटॉर्च के लिए ऑर्थोगोनलाइज़ेशन युक्त म्यूऑन ऑप्टिमाइज़र
translated: true
type: note
---

ठीक है—यहाँ एक साफ-सुथरा PyTorch संदर्भ कार्यान्वयन है जिसे आप किसी प्रोजेक्ट में सीधे इस्तेमाल कर सकते हैं। इसमें शामिल है:

* 2-D अपडेट्स को ऑर्थोगोनलाइज़ करने के लिए एक छोटा Newton–Schulz व्युत्क्रम-वर्गमूल
* एक `Muon` ऑप्टिमाइज़र (AdamW-स्टाइल वेट डिके, मोमेंटम, वैकल्पिक RMS स्केलिंग)
* 1-D टेंसर्स (बायस, LayerNorm वेट) के लिए एक फॉलबैक
* एक न्यूनतम ट्रेनिंग उदाहरण

---

### 1) मैट्रिक्स ऑर्थोगोनलाइज़ेशन सहायक

```python
# muon_utils.py
import torch

@torch.no_grad()
def orthogonalize_by_svd(G: torch.Tensor) -> torch.Tensor:
    """
    निकटतम ऑर्थोगोनल (Procrustes): Q = U @ Vh, जहाँ G = U S Vh.
    सटीक लेकिन बड़े मैट्रिक्स पर धीमा हो सकता है।
    """
    U, _, Vh = torch.linalg.svd(G, full_matrices=False)
    return U @ Vh

@torch.no_grad()
def inv_sqrt_newton_schulz(A: torch.Tensor, iters: int = 5, eps: float = 1e-6) -> torch.Tensor:
    """
    SPD A के लिए Newton–Schulz का उपयोग करके A^{-1/2} की गणना करें।
    मानता है कि A सममित और पॉजिटिव डेफिनिट है (जैसे, G^T G + eps I)।
    """
    # बेहतर अभिसरण के लिए सामान्यीकरण करें
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
    Q ≈ G (G^T G)^{-1/2}, व्युत्क्रम वर्गमूल के लिए Newton–Schulz का उपयोग करते हुए।
    """
    # SPD बनाएं; संख्यात्मक स्थिरता के लिए eps*I जोड़ें
    S = G.transpose(-1, -2) @ G
    n = S.size(-1)
    S = S + eps * torch.eye(n, device=S.device, dtype=S.dtype)
    S_inv_sqrt = inv_sqrt_newton_schulz(S, iters=iters, eps=eps)
    return G @ S_inv_sqrt
```

---

### 2) Muon ऑप्टिमाइज़र

```python
# muon.py
from torch.optim.optimizer import Optimizer
import torch
from muon_utils import orthogonalize_by_newton_schulz, orthogonalize_by_svd

class Muon(Optimizer):
    r"""
    Muon: संरचना-जागरूक, मैट्रिक्स-ऑर्थोगोनलाइज़िंग ऑप्टिमाइज़र।
    - ग्रेडिएंट्स पर मोमेंटम
    - डिकपल्ड वेट डिके (AdamW-स्टाइल)
    - 2D पैरामीटर्स के लिए: मोमेंटम-औसत अपडेट को ऑर्थोगोनलाइज़ करें (Newton–Schulz या SVD)
    - 1D/अन्य आकृतियों के लिए: Adam की तरह मोमेंटम पर RMS स्केलिंग (कोई ऑर्थोगोनलाइज़ेशन नहीं)

    आर्ग्स:
        params: पैरामीटर्स की इटरेबल
        lr (float): लर्निंग रेट
        beta (float): मोमेंटम फैक्टर (डिफॉल्ट 0.9)
        weight_decay (float): डिकपल्ड वेट डिके (डिफॉल्ट 0.01)
        eps (float): न्यूमेरिकल eps (डिफॉल्ट 1e-8)
        ns_iters (int): ऑर्थोगोनलाइज़ेशन के लिए Newton–Schulz इटरेशन (डिफॉल्ट 5)
        method (str): 'ns' Newton–Schulz के लिए (डिफॉल्ट), या 'svd'
        rms_scale (bool): गैर-2D टेंसर्स के लिए मोमेंटम पर प्रति-टेंसर RMS सामान्यीकरण लागू करें (डिफॉल्ट True)
        clip_grad_norm (float|None): अगर सेट है, तो लागू करने से पहले L2 नॉर्म द्वारा मोमेंटम अपडेट को क्लिप करें (डिफॉल्ट None)
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
            raise ValueError("अमान्य लर्निंग रेट")
        if not 0.0 <= beta < 1.0:
            raise ValueError("अमान्य बीटा")
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

                # मोमेंटम बफर
                if "momentum" not in state:
                    state["momentum"] = torch.zeros_like(p, memory_format=torch.preserve_format)
                m = state["momentum"]

                # m_t = beta*m_{t-1} + (1-beta)*g_t
                m.mul_(beta).add_(grad, alpha=(1.0 - beta))

                # अपडेट दिशा (मोमेंटम) पर वैकल्पिक ग्लोबल क्लिप
                if clip_gn is not None:
                    gnorm = m.norm()
                    if gnorm > clip_gn:
                        m.mul_(clip_gn / (gnorm + 1e-12))

                # पैरामीटर्स पर डिकपल्ड वेट डिके
                if wd != 0.0:
                    p.mul_(1.0 - lr * wd)

                # अपडेट दिशा U की गणना करें
                if p.ndim == 2:
                    # मैट्रिक्स अपडेट को ऑर्थोगोनलाइज़ करें
                    if method == "svd":
                        U = orthogonalize_by_svd(m)
                    else:
                        U = orthogonalize_by_newton_schulz(m, iters=ns_iters, eps=eps)
                else:
                    # गैर-मैट्रिक्स टेंसर्स: स्टेप साइज को संतुलित रखने के लिए RMS स्केलिंग (Adam-जैसा)
                    if rms_scale:
                        rms = torch.sqrt(m.pow(2).mean() + eps)
                        U = m / rms
                    else:
                        U = m

                # पैरामीटर अपडेट
                p.add_(U, alpha=-lr)

        return loss
```

---

### 3) न्यूनतम उपयोग उदाहरण

```python
# demo_muon.py
import torch
from torch import nn
from muon import Muon

# टॉय मॉडल
model = nn.Sequential(
    nn.Linear(256, 512),
    nn.ReLU(),
    nn.Linear(512, 256),
)

x = torch.randn(32, 256)
y = torch.randn(32, 256)

criterion = nn.MSELoss()

# Newton–Schulz ऑर्थोगोनलाइज़ेशन आज़माएं (तेज़ और स्केलेबल)। सटीकता के लिए method='svd' का उपयोग करें।
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

### नोट्स और सुझाव

* बहुत बड़े वेट मैट्रिक्स के लिए, `method="ns"` SVD से बचता है और आमतौर पर बहुत तेज़ होता है। अगर आप छोटी लेयर्स पर शुद्धता सत्यापित कर रहे हैं, तो तुलना के लिए `method="svd"` का उपयोग करें।
* `ns_iters=3..6` एक अच्छी प्रैक्टिकल रेंज है। कम इटरेशन = तेज़ लेकिन थोड़ा कम सटीक ऑर्थोगोनलाइज़ेशन।
* एक छोटा `weight_decay` (डिकपल्ड) और मध्यम `beta` (जैसे, 0.9) रखें। transformers/MLPs के लिए लर्निंग रेट लगभग `1e-3` से `3e-4` एक उचित शुरुआती बिंदु है।
* अगर ट्रेनिंग स्पाइकी हो जाती है, तो कंस्ट्रक्टर में `clip_grad_norm` (जैसे, `1.0–5.0`) सक्षम करें।

अगर आप चाहें, तो मैं इसे आपके सटीक मॉडल सेटअप के अनुकूल बना सकता हूँ (जैसे, torch.compile, FSDP/ZeRO, MoE लेयर्स, कस्टम प्रति-पैराम कॉन्फ़िग)।