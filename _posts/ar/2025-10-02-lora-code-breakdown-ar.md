---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast:free
title: تحليل وشرح كود لورا
translated: true
type: note
---

سأقوم بتقسيم كود تجربة LoRA إلى أجزاء رئيسية، موضحًا كل جزء بالتفصيل قبل الانتقال إلى التالي. سيساعد هذا في توضيح كيفية عمل LoRA بطريقة واضحة خطوة بخطوة. يعتمد الكود على المثال السابق، باستخدام PyTorch لتنفيذ LoRA لطبقة خطية بسيطة.

### الجزء 1: تعريف طبقة LoRA
```python
import torch
import torch.nn as nn

class LoRALayer(nn.Module):
    def __init__(self, in_features, out_features, rank=4):
        super(LoRALayer, self).__init__()
        # الأوزان الأصلية المجمدة
        self.linear = nn.Linear(in_features, out_features)
        self.linear.weight.requires_grad = False  # تجميد الأوزان الأصلية
        # معاملات LoRA: المصفوفات منخفضة الرتبة A و B
        self.lora_A = nn.Parameter(torch.randn(in_features, rank))
        self.lora_B = nn.Parameter(torch.randn(rank, out_features))
        self.scaling = 1.0  # عامل التحجيم لتحديثات LoRA
```

#### الشرح
يحدد هذا الجزء فئة `LoRALayer`، التي تنفذ تقنية LoRA. إليك ما يحدث:

- **الاستيراد وإعداد الفئة**: نستورد PyTorch (`torch`) ووحدة الشبكة العصبية الخاصة به (`nn`). ترث فئة `LoRALayer` من `nn.Module`، مما يجعلها وحدة PyTorch يمكن دمجها في نماذج أكبر.
- **الطبقة الخطية الأصلية**: `self.linear = nn.Linear(in_features, out_features)` تنشئ طبقة خطية قياسية (مثل الطبقة المتصلة بالكامل في الشبكة العصبية) ذات مدخلات `in_features` ومخرجات `out_features`. تمثل هذا الأوزان المدربة مسبقًا والتي نريد تكييفها.
- **تجميد الأوزان**: `self.linear.weight.requires_grad = False` يجمّد الأوزان الأصلية للطبقة الخطية، مما يضمن عدم تحديثها أثناء التدريب. هذا أمر أساسي لكفاءة LoRA، حيث يتجنب تعديل النموذج الكبير المدرب مسبقًا.
- **معاملات LoRA**: `self.lora_A` و `self.lora_B` هما مصفوفتان منخفضتا الرتبة. `lora_A` لها شكل `(in_features, rank)`، و `lora_B` لها شكل `(rank, out_features)`. يتحكم المعامل `rank` (الافتراضي=4) في حجم هذه المصفوفات، مما يبقيها أصغر بكثير من مصفوفة الوزن الأصلية (الشكل `in_features x out_features`). هذه المصفوفات قابلة للتدريب (`nn.Parameter`) وتم تهيئتها بقيم عشوائية (`torch.randn`).
- **عامل التحجيم**: `self.scaling = 1.0` هو معامل فائق لتحجيم تعديل LoRA، مما يسمح بضبط دقيق لقوة التكيف.

يضمن هذا الإعداد تحديث مصفوفتي `lora_A` و `lora_B` الصغيرتين فقط أثناء التدريب، مما يقلل بشكل كبير من عدد المعاملات القابلة للتدريب.

---

### الجزء 2: التمرير الأمامي لـ LoRA
```python
    def forward(self, x):
        # التحويل الخطي الأصلي + تعديل LoRA
        original = self.linear(x)
        lora_adjustment = self.scaling * torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)
        return original + lora_adjustment
```

#### الشرح
يحدد هذا الجزء التمرير الأمامي لـ `LoRALayer`، الذي يحسب مخرجات الطبقة:

- **المدخلات**: المدخل `x` هو موتر ذو شكل `(batch_size, in_features)`، يمثل دفعة من بيانات الإدخال.
- **المخرج الأصلي**: `original = self.linear(x)` يحسب مخرج الطبقة الخطية المجمدة، مطبقًا الأوزان المدربة مسبقًا على المدخل.
- **تعديل LoRA**: العبارة `torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)` تحسب التكيف منخفض الرتبة. أولاً، يُضرب `x` في `lora_A` (الشكل `in_features x rank`)، منتجًا موترًا ذا شكل `(batch_size, rank)`. ثم يُضرب هذا في `lora_B` (الشكل `rank x out_features`)، لينتج موترًا ذا شكل `(batch_size, out_features)` - نفس شكل المخرج الأصلي. يمثل هذا التعديل التحديث المخصص للمهمة.
- **التحجيم والجمع**: يتم تحجيم التعديل بواسطة `self.scaling` وإضافته إلى المخرج الأصلي، منتجًا المخرج النهائي. يضمن هذا احتفاظ النموذج بالمعرفة المدربة مسبقًا مع دمج التكيفات المخصصة للمهمة.

يضمن الهيكل منخفض الرتبة (`rank` صغير، مثلاً 4) أن التعديل فعال من الناحية الحسابية وموفر للمعاملات مقارنة بتحديث مصفوفة الوزن الكاملة.

---

### الجزء 3: مجموعة البيانات الاصطناعية والتدريب
```python
def create_toy_dataset(n_samples=1000):
    X = torch.randn(n_samples, 64)  # ميزات إدخال عشوائية
    y = torch.randn(n_samples, 10)  # مخرجات هدف عشوائية
    return X, y

def train_model(model, X, y, epochs=10, lr=0.01):
    criterion = nn.MSELoss()
    optimizer = optim.Adam([param for param in model.parameters() if param.requires_grad], lr=lr)
    
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")
```

#### الشرح
ينشئ هذا الجزء مجموعة بيانات اصطناعية ويدرب النموذج المكيف بـ LoRA:

- **مجموعة البيانات الاصطناعية**: تقوم الدالة `create_toy_dataset` بتوليد بيانات تركيبية للتوضيح. `X` هو موتر ذو شكل `(1000, 64)` (1000 عينة، 64 ميزة)، و `y` هو موتر ذو شكل `(1000, 10)` (1000 عينة، 10 أبعاد مخرجات). هذه موترات عشوائية لمحاكاة أزواج الإدخال-الإخراج.
- **دالة التدريب**: تقوم الدالة `train_model` بإعداد حلقة تدريب بسيطة:
  - **دالة الخسارة**: `nn.MSELoss()` تحدد خطأ متوسط المربعات كخسارة، مناسب لمهمة اللعب الشبيهة بالانحدار هذه.
  - **المحسن**: `optim.Adam` يحسن فقط المعاملات القابلة للتدريب (`param.requires_grad` هي `True`)، وهي `lora_A` و `lora_B`. يتم استبعاد `linear.weight` المجمد، مما يضمن الكفاءة.
  - **حلقة التدريب**: في كل عصر، يحسب النموذج المخرجات، ويحسب الخسارة، وينفذ الانتشار العكسي (`loss.backward()`)، ويحدث معاملات LoRA (`optimizer.step()`). يتم طباعة الخسارة لمراقبة تقدم التدريب.

يوضح هذا الإعداد كيف تقوم LoRA بضبط المصفوفات منخفضة الرتبة فقط، مع الحفاظ على العملية خفيفة الوزن.

---

### الجزء 4: التنفيذ الرئيسي وعد المعاملات
```python
def main():
    # ضبط البذرة العشوائية لإمكانية إعادة النتائج
    torch.manual_seed(42)
    
    # إنشاء مجموعة البيانات الاصطناعية
    X, y = create_toy_dataset()
    
    # تهيئة النموذج مع LoRA
    model = LoRALayer(in_features=64, out_features=10, rank=4)
    
    # عد المعاملات القابلة للتدريب
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Trainable parameters: {trainable_params}")
    print(f"Total parameters: {total_params}")
    
    # تدريب النموذج
    train_model(model, X, y)

if __name__ == "__main__":
    main()
```

#### الشرح
يربط هذا الجزء كل شيء معًا ويسلط الضوء على كفاءة LoRA:

- **البذرة العشوائية**: `torch.manual_seed(42)` تضمن إمكانية إعادة إنتاج التهيئات العشوائية.
- **مجموعة البيانات والنموذج**: يتم إنشاء مجموعة البيانات الاصطناعية، وتهيئة `LoRALayer` بـ `in_features=64`، و `out_features=10`، و `rank=4`.
- **عد المعاملات**: يحسب الكود:
  - **المعاملات القابلة للتدريب**: فقط `lora_A` (64 × 4 = 256) و `lora_B` (4 × 10 = 40)، بإجمالي 296 معامل.
  - **إجمالي المعاملات**: يشمل `linear.weight` المجمد (64 × 10 = 640) و `linear.bias` (10)، بالإضافة إلى معاملات LoRA، بإجمالي 946 معامل.
  - يوضح هذا كفاءة LoRA: فقط ~31% (296/946) من المعاملات قابلة للتدريب، مقارنة بـ 100% في الضبط الكامل.
- **التدريب**: يتم استدعاء الدالة `train_model` لضبط معاملات LoRA على مجموعة البيانات الاصطناعية.

عند تشغيل هذا، سترى أن عدد المعاملات القابلة للتدريب أقل بكثير من الإجمالي، وأن النموذج يتدرب بسرعة بسبب التحديثات منخفضة الرتبة.

---

### تشغيل الكود
لتشغيل هذا، تحتاج إلى تثبيت PyTorch (`pip install torch`). احفظ الكود الكامل كملف `.py` وقم بتنفيذه. سيظهر المخرج عدد المعاملات وخسارة التدريب على مدى 10 عصور، موضحًا كفاءة LoRA في الضبط الدقيق.

[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

دعني أعلم إذا كنت ترغب في الخوض بشكل أعمق في أي جزء أو تعديل المثال!