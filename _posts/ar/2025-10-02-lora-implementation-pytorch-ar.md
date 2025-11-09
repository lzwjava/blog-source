---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast:free
title: مثال تطبيق لورا باستخدام باي تورش
translated: true
type: note
---

إليك مثال على كود Python يوضح كيفية تنفيذ LoRA (Low-Rank Adaptation) باستخدام PyTorch لضبط شبكة عصبية بسيطة. يركز هذا المثال على تكييف طبقة خطية مدربة مسبقًا مع LoRA، مع الحفاظ على الأوزان الأصلية مجمدة وإدخال مصفوفات تحديث ذات رتبة منخفضة. يتضمن الكود إعدادًا أساسيًا مع مجموعة بيانات بسيطة وحلقة تدريب مصغرة لتوضيح الفكرة.

<xaiArtifact artifact_id="1327e99b-24b5-4b0d-9ffd-5b4c2d1472af" artifact_version_id="4053525d-2225-4913-a3b9-b7d66b48daea" title="lora_demo.py" contentType="text/python">
import torch
import torch.nn as nn
import torch.optim as optim

# تعريف طبقة LoRA
class LoRALayer(nn.Module):
    def __init__(self, in_features, out_features, rank=4):
        super(LoRALayer, self).__init__()
        # الأوزان الأصلية المجمدة
        self.linear = nn.Linear(in_features, out_features)
        self.linear.weight.requires_grad = False  # تجميد الأوزان الأصلية
        # معاملات LoRA: مصفوفتي الرتبة المنخفضة A و B
        self.lora_A = nn.Parameter(torch.randn(in_features, rank))
        self.lora_B = nn.Parameter(torch.randn(rank, out_features))
        self.scaling = 1.0  # عامل التحجيم لتحديثات LoRA

    def forward(self, x):
        # التحويل الخطي الأصلي + تعديل LoRA
        original = self.linear(x)
        lora_adjustment = self.scaling * torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)
        return original + lora_adjustment

# مجموعة بيانات بسيطة للتوضيح
def create_toy_dataset(n_samples=1000):
    X = torch.randn(n_samples, 64)  # ميزات إدخال عشوائية
    y = torch.randn(n_samples, 10)  # مخرجات هدف عشوائية
    return X, y

# دالة التدريب
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

# التنفيذ الرئيسي
def main():
    # ضبط البذرة العشوائية لإمكانية إعادة النتائج
    torch.manual_seed(42)
    
    # إنشاء مجموعة بيانات بسيطة
    X, y = create_toy_dataset()
    
    # تهيئة النموذج مع LoRA
    model = LoRALayer(in_features=64, out_features=10, rank=4)
    
    # حساب المعاملات القابلة للتدريب
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Trainable parameters: {trainable_params}")
    print(f"Total parameters: {total_params}")
    
    # تدريب النموذج
    train_model(model, X, y)

if __name__ == "__main__":
    main()
</xaiArtifact>

يعرف هذا الكود `LoRALayer` التي تغلف طبقة خطية قياسية بمصفوفات التكيف ذات الرتبة المنخفضة (`lora_A` و `lora_B`). يتم تجميد الأوزان الأصلية، ويتم تحديث معاملات LoRA فقط أثناء التدريب. تظهر مجموعة البيانات البسيطة وحلقة التدريب كيف تقلل LoRA عدد المعاملات القابلة للتدريب مع السماح بالضبط الدقيق. يمكنك تشغيل هذا الكود مع تثبيت PyTorch لرؤية عملية التدريب وكفاءة المعاملات أثناء التنفيذ.

[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)