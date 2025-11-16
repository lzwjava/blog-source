---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: नैनोजीपीटी में पाइटॉर्च ब्रॉडकास्टिंग को समझना
translated: true
type: note
---

बढ़िया सवाल! NanoGPT या GPT-2 कोड को पहली बार देखते समय यह एक बहुत ही आम भ्रम का बिंदु है।

आइए आकृतियों (shapes) को ध्यान से देखें:

```python
tok_emb = self.transformer.wte(idx)    # आकार: (B, T, n_embd)
pos_emb = self.transformer.wpe(pos)    # आकार: (T, n_embd)   ← केवल 1D!
```

आप `(B, T, n_embd)` + `(T, n_embd)` कैसे जोड़ सकते हैं?

**उत्तर: PyTorch स्वचालित रूप से बैच आयाम (batch dimension) में पोजीशन एम्बेडिंग्स को प्रसारित (broadcast) कर देता है।**

जब PyTorch यह देखता है:
```python
tok_emb + pos_emb
```
यह `pos_emb` (आकार `(T, n_embd)`) को ऐसे मानता है जैसे कि यह `(1, T, n_embd)` हो और फिर इसे `(B, T, n_embd)` से मेल खाने के लिए **प्रसारित (broadcast)** कर देता है।

तो यह जोड़ इस प्रकार बन जाता है:
```
(B, T, n_embd)
     + 
(1, T, n_embd)   ← प्रसारण द्वारा स्वचालित रूप से जोड़ा गया
     =
(B, T, n_embd)
```

यह ठीक वैसे ही काम करता है जैसे मूल GPT-2 और सभी आधुनिक ट्रांसफॉर्मर कार्यान्वयन करते हैं — पोजीशन एम्बेडिंग्स बैच में सभी अनुक्रमों (sequences) में साझा की जाती हैं।

आप पुष्टि कर सकते हैं कि यह Python में काम करता है:

```python
import torch
B, T, C = 2, 3, 768
tok_emb = torch.randn(B, T, C)
pos_emb = torch.randn(T, C)

result = tok_emb + pos_emb
print(result.shape)  # → torch.Size([2, 3, 768])
```

कोई त्रुटि नहीं, बिल्कुल सही काम करता है।

इसलिए NanoGPT (और मूल GPT-2) में, यह पंक्ति 100% सही और जानबूझकर की गई है:

```python
x = self.transformer.drop(tok_emb + pos_emb)
```

यह PyTorch के प्रसारण (broadcasting) पर निर्भर करता है — साफ, कुशल, और मानक अभ्यास।

`pos_emb.unsqueeze(0)` या किसी और चीज़ की आवश्यकता नहीं है। प्रसारण (Broadcasting) यह काम सुरुचिपूर्ण ढंग से कर देता है।