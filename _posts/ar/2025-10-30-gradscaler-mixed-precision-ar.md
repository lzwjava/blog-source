---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: مقياس التدرج للتدريب بدقة مختلطة
translated: true
type: note
---

`torch.cuda.amp.GradScaler` هي فائدة مساعدة في PyTorch مصممة **لقياس التدرجات (الغرافيانت) تلقائياً** أثناء التدريب باستخدام الدقة المختلطة عبر **الدقة المختلطة التلقائية (AMP)**. تساعد في منع التدفق تحت العتبة (underflow) في التدرجات عند استخدام موترات `float16` (نصف الدقة)، والتي قد تصبح صغيرة جداً لدرجة لا يمكن تمثيلها بدقة بخلاف ذلك.

---

### لماذا تستخدم `GradScaler`؟

في التدريب بالدقة المختلطة:
- **عمليات التمرير الأمامي والعكسي** تستخدم `float16` للسرعة وتوفير الذاكرة.
- **التدرجات** المحسوبة بـ `float16` قد تصبح صغيرة جداً → **تدفق تحت العتبة إلى الصفر**.
- `GradScaler` يقيس **الخسارة** بعامل (مثال: 2¹⁵ = 32768) قبل عملية التمرير العكسي.
- يتم قياس التدرجات بشكل متناسب → تبقى في النطاق القابل للتمثيل.
- قبل خطوة المُحسّن (optimizer)، يتم **إعادة التدرجات إلى قياسها الطبيعي**.

---

### الاستخدام الأساسي

```python
import torch
from torch.cuda.amp import autocast, GradScaler

model = MyModel().cuda()
optimizer = torch.optim.Adam(model.parameters())
scaler = GradScaler()  # الإعداد الافتراضي init_scale=2**16

for data, target in dataloader:
    optimizer.zero_grad()

    # 1. Autocast للتمرير الأمامي
    with autocast():
        output = model(data)
        loss = loss_fn(output, target)

    # 2. قياس الخسارة والتمرير العكسي
    scaler.scale(loss).backward()

    # 3. إعادة القياس إلى الطبيعي + خطوة المُحسّن
    scaler.step(optimizer)

    # 4. تحديث عامل القياس للدورة التالية
    scaler.update()
```

---

### الطرق الرئيسية

| الطريقة | الغرض |
|-------|--------|
| `scaler.scale(loss)` | يقيس الخسارة قبل `.backward()` |
| `scaler.step(optimizer)` | يعيد قياس التدرجات وينفذ `optimizer.step()` |
| `scaler.update()` | يضبط عامل القياس للدورة التالية |
| `scaler.unscale_(optimizer)` | يعيد قياس التدرجات يدوياً (نادراً ما يحتاج) |
| `scaler.get_scale()` | يُرجع عامل القياس الحالي |

---

### كيف يعمل القياس (داخلياً)

1. **القياس الابتدائي**: عادة `2**16 = 65536`
2. بعد `backward()`، يتحقق من وجود **inf/NaN** في التدرجات.
3. إذا **لم يُعثر على inf/NaN** → قد **يزداد** عامل القياس (مثال: ×2) في المرة القادمة.
4. إذا **وُجد inf/NaN** → يتخطى `optimizer.step()`، **يقلل عامل القياس** (مثال: ÷2)، ويعيد المحاولة لاحقاً.

هذا يجعل التدريب **مقاوماً** للفيضان (overflow) العَرَضي.

---

### المُعاملات الشائعة

```python
scaler = GradScaler(
    init_scale=2.**16,     # عامل القياس الابتدائي
    growth_factor=2.0,     # الضرب عند عدم وجود inf
    backoff_factor=0.5,    # القسمة عند وجود inf
    growth_interval=2000,  # عدد الخطوات قبل زيادة القياس
    enabled=True
)
```

---

### مثال مع تقليم التدرجات (Gradient Clipping)

```python
scaler.scale(loss).backward()
scaler.unscale_(optimizer)  # يجب إعادة القياس إلى الطبيعي قبل التقليم
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
scaler.step(optimizer)
scaler.update()
```

> **ملاحظة**: دائماً استخدم `unscale_` **قبل** تقليم التدرجات أو فحصها.

---

### أفضل الممارسات

- استخدم مع `torch.cuda.amp.autocast()`
- ضع **فقط التمرير الأمامي + الخسارة** داخل `autocast()`
- نادِ على `scaler.update()` **في كل دورة**
- استخدم `torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction=True` للسرعة

---

### متى لا تستخدم

- التدريب باستخدام `float32` بحتة
- التدريب على وحدة المعالجة المركزية (CPU)
- حلقات تدريب مخصصة تتعامل مع القياس يدوياً

---

### الوثائق الرسمية

[https://pytorch.org/docs/stable/amp.html#torch.cuda.amp.GradScaler](https://pytorch.org/docs/stable/amp.html#torch.cuda.amp.GradScaler)

---

أعلمني إذا كنت تريد مثالاً كاملاً لحلقة التدريب أو مقارنة مع القياس اليدوي!