---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: بارامتر PyTorch للأوزان القابلة للتعلم
translated: true
type: note
---

`torch.nn.Parameter` هو فئة فرعية من `torch.Tensor` في PyTorch، مُصممة خصيصًا لتمثيل المعلمات القابلة للتعلّم في وحدات الشبكات العصبية. الهدف الرئيسي منه هو تسجيل الـ tensors تلقائيًا كمعلمات للوحدة عندما يتم تعيينها كسمات لوحدة `torch.nn.Module`، مما يجعلها قابلة للوصول عبر طرق مثل `module.parameters()` أو `module.named_parameters()`. هذا يساعد على التمييز بين الأوزان القابلة للتدريب (مثل تلك الخاصة بالطبقات) وبين الـ tensors العادية، مما يمنع المعالجات المؤقتة (مثل الحالات المخبأة في RNNs) من أن يتم التعامل معها عن طريق الخطأ على أنها معلمات.

### الميزات الرئيسية
- **التسجيل التلقائي**: عندما تقوم بتعيين `Parameter` لوحدة (على سبيل المثال، `self.weight = nn.Parameter(torch.randn(3, 3))` في دالة `__init__` لوحدة مخصصة)، يتم إضافته إلى قائمة معلمات الوحدة دون الحاجة إلى كود إضافي.
- **تتبع التدرج (Gradient)**: بشكل افتراضي، `requires_grad=True`، لذا يشارك في عملية الانتشار العكسي (backpropagation). يظل هذا ساريًا حتى داخل سياق `torch.no_grad()` — استخدم تعطيل autograd المحلي للتحكم الدقيق.
- **السمات**: يرث جميع خصائص `Tensor` ولكنه لا يضيف أي سمات جديدة بخلاف سلوكه الخاص بالوحدات.

### الاستخدام الأساسي
إليك مثالًا بسيطًا في وحدة مخصصة:

```python
import torch
import torch.nn as nn

class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        # هذا يتم تسجيله تلقائيًا كمعلمة
        self.weight = nn.Parameter(torch.randn(2, 3))
        # الـ tensor العادي لن يتم تسجيله
        self.bias = torch.zeros(3)

    def forward(self, x):
        return x @ self.weight + self.bias

model = MyModule()
print(list(model.parameters()))  # المخرجات: [Parameter containing: tensor(...)]
```

لمزيد من التفاصيل، راجع الوثائق الرسمية: [Parameter — PyTorch 2.9 documentation](https://pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html)