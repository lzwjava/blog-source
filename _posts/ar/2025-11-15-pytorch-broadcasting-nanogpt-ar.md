---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: فهم البث في PyTorch ضمن NanoGPT
translated: true
type: note
---

سؤال رائع! هذه نقطة حيرة شائعة جدًا عند النظر لأول مرة إلى كود NanoGPT أو GPT-2.

لنلقِ نظرة على الأشكال بعناية:

```python
tok_emb = self.transformer.wte(idx)    # الشكل: (B, T, n_embd)
pos_emb = self.transformer.wpe(pos)    # الشكل: (T, n_embd)   ← أحادي البعد فقط!
```

كيف يمكنك جمع `(B, T, n_embd)` + `(T, n_embd)`؟

**الإجابة: PyTorch تقوم تلقائيًا ببث تضمينات الموضع عبر بُعد الدُفعة.**

عندما ترى PyTorch:
```python
tok_emb + pos_emb
```
فإنها تعامل `pos_emb` (الشكل `(T, n_embd)`) كما لو كانت `(1, T, n_embd)` ثم **تبثها** لتطابق `(B, T, n_embd)`.

لذا تصبح هذه العملية:
```
(B, T, n_embd)
     + 
(1, T, n_embd)   ← مُضافة تلقائيًا عن طريق البث
     =
(B, T, n_embd)
```

هذا بالضبط كيف تعمل GPT-2 الأصلية وجميع تنفيذات المحولات الحديثة — يتم مشاركة تضمينات الموضع عبر جميع التسلسلات في الدُفعة.

يمكنك التحقق من أن هذا يعمل في Python:

```python
import torch
B, T, C = 2, 3, 768
tok_emb = torch.randn(B, T, C)
pos_emb = torch.randn(T, C)

result = tok_emb + pos_emb
print(result.shape)  # → torch.Size([2, 3, 768])
```

لا يوجد خطأ، تعمل بشكل مثالي.

لذا في NanoGPT (و GPT-2 الأصلية)، هذا السطر صحيح 100% ومقصود:

```python
x = self.transformer.drop(tok_emb + pos_emb)
```

إنه يعتمد على بث PyTorch — أنيق، فعال، وممارسة قياسية.

لا حاجة لـ `pos_emb.unsqueeze(0)` أو أي شيء آخر. البث يقوم بالمهمة بأناقة.