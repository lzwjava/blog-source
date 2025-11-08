---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: मिश्रित-परिशुद्धता प्रशिक्षण के लिए ग्रेड स्केलर
translated: true
type: note
---

`torch.cuda.amp.GradScaler` एक PyTorch utility class है जो **Automatic Mixed Precision (AMP)** का उपयोग करते हुए mixed-precision training के दौरान **gradients को स्वचालित रूप से scale** करने के लिए डिज़ाइन किया गया है। यह gradients में underflow को रोकने में मदद करता है जब `float16` (half-precision) tensors का उपयोग किया जाता है, जो अन्यथा सटीक रूप से represent करने के लिए बहुत छोटे हो सकते हैं।

---

### `GradScaler` का उपयोग क्यों करें?

Mixed-precision training में:
- **Forward/backward passes** गति और मेमोरी बचत के लिए `float16` का उपयोग करते हैं।
- `float16` में computed **gradients** बहुत छोटे हो सकते हैं → **शून्य में underflow**।
- `GradScaler` backward pass से पहले **loss** को एक factor (जैसे, 2¹⁵ = 32768) से scale करता है।
- Gradients आनुपातिक रूप से scaled होते हैं → representable range में रहते हैं।
- Optimizer step से पहले, gradients को वापस सामान्य अवस्था में **unscaled** किया जाता है।

---

### मूल उपयोग

```python
import torch
from torch.cuda.amp import autocast, GradScaler

model = MyModel().cuda()
optimizer = torch.optim.Adam(model.parameters())
scaler = GradScaler()  # Default init_scale=2**16

for data, target in dataloader:
    optimizer.zero_grad()

    # 1. Autocast for forward
    with autocast():
        output = model(data)
        loss = loss_fn(output, target)

    # 2. Scale loss and backward
    scaler.scale(loss).backward()

    # 3. Unscale + optimizer step
    scaler.step(optimizer)

    # 4. Update the scale for next iteration
    scaler.update()
```

---

### मुख्य Methods

| Method | उद्देश्य |
|-------|--------|
| `scaler.scale(loss)` | `.backward()` से पहले loss को scale करता है |
| `scaler.step(optimizer)` | Grads को unscaled करता है और `optimizer.step()` को call करता है |
| `scaler.update()` | अगले iteration के लिए scaling factor को adjust करता है |
| `scaler.unscale_(optimizer)` | Grads को manually unscale करता है (शायद ही आवश्यक हो) |
| `scaler.get_scale()` | वर्तमान scale factor को return करता है |

---

### Scaling कैसे काम करती है (आंतरिक रूप से)

1. **प्रारंभिक scale**: आमतौर पर `2**16 = 65536`
2. `backward()` के बाद, gradients में **inf/NaN** की जांच करता है।
3. यदि **कोई inf/NaN नहीं** है → scale **बढ़ सकता है** (जैसे, ×2) अगली बार।
4. यदि **inf/NaN मिलता है** → `optimizer.step()` को skip करें, **scale घटाएं** (जैसे, ÷2), और बाद में पुनः प्रयास करें।

यह training को occasional overflow के प्रति **मजबूत** बनाता है।

---

### सामान्य Parameters

```python
scaler = GradScaler(
    init_scale=2.**16,     # Starting scale
    growth_factor=2.0,     # Multiply when no inf
    backoff_factor=0.5,    # Divide when inf
    growth_interval=2000,  # Steps before growing scale
    enabled=True
)
```

---

### Gradient Clipping के साथ उदाहरण

```python
scaler.scale(loss).backward()
scaler.unscale_(optimizer)  # Need to unscale before clipping
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
scaler.step(optimizer)
scaler.update()
```

> **नोट**: Gradients को inspect करने या clipping करने से **पहले** हमेशा `unscale_` करें।

---

### सर्वोत्तम अभ्यास

- `torch.cuda.amp.autocast()` के साथ उपयोग करें
- `autocast()` में **केवल forward + loss** को wrap करें
- `scaler.update()` को **हर iteration** में call करें
- गति के लिए `torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction=True` का उपयोग करें

---

### कब उपयोग न करें

- Pure `float32` training
- CPU training
- Custom training loops जो manually scaling को handle करते हैं

---

### आधिकारिक दस्तावेज़

[https://pytorch.org/docs/stable/amp.html#torch.cuda.amp.GradScaler](https://pytorch.org/docs/stable/amp.html#torch.cuda.amp.GradScaler)

---

मुझे बताएं यदि आप एक पूर्ण training loop उदाहरण या manual scaling के साथ तुलना चाहते हैं!