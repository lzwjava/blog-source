---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: مثال بسيط للشبكة العصبية المتكررة باستخدام PyTorch
translated: true
type: note
---

### مثال بسيط على RNN في PyTorch

الشبكات العصبية المتكررة (RNNs) رائعة في التعامل مع البيانات المتسلسلة مثل السلاسل الزمنية أو النصوص. إليك مثالًا أساسيًا باستخدام PyTorch لبناء RNN بسيط لتصنيف المتواليات (مثل التصنيف الثنائي على متواليات عشوائية). يفترض هذا أن لديك PyTorch مثبتًا (`import torch` و `import torch.nn as nn`).

```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# المعلمات الفائقة
input_size = 1      # حجم الميزة (مثل السلسلة الزمنية أحادية المتغير)
hidden_size = 32    # حجم الحالة المخفية
output_size = 1     # المخرج الثنائي (sigmoid للتصنيف)
sequence_length = 10  # طول كل متوالية
batch_size = 32
num_epochs = 10

# توليد بيانات وهمية: متواليات بطول 10، وتسميات تعتمد على المجموع (ثنائي)
def generate_data(num_samples):
    X = torch.randn(num_samples, sequence_length, input_size)
    y = (torch.sum(X, dim=1) > 0).float().unsqueeze(1)
    return X, y

# نموذج RNN البسيط
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        # شكل x: (batch, seq_len, input_size)
        h0 = torch.zeros(1, x.size(0), self.hidden_size)  # الحالة المخفية الأولية
        out, _ = self.rnn(x, h0)
        # أخذ آخر مخرج للتصنيف
        out = self.fc(out[:, -1, :])  # آخر خطوة زمنية
        return self.sigmoid(out)

# تهيئة النموذج، دالة الخسارة، المُحسّن
model = SimpleRNN(input_size, hidden_size, output_size)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# حلقة التدريب
num_samples = 1000
X, y = generate_data(num_samples)
dataset = torch.utils.data.TensorDataset(X, y)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

for epoch in range(num_epochs):
    for batch_X, batch_y in dataloader:
        optimizer.zero_grad()
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# مثال الاستدلال
test_seq = torch.randn(1, sequence_length, input_size)
prediction = model(test_seq)
print(f'Prediction: {prediction.item():.4f}')
```

#### آلية العمل:
- **توليد البيانات**: ينشئ متواليات عشوائية بطول 10 مع تسمية ثنائية (1 إذا كان المجموع > 0، وإلا 0).
- **النموذج**: يستخدم `nn.RNN` (خلية RNN أساسية). تمريرة الأمامية تعالج المتوالية خطوة بخطوة، باستخدام الحالة المخفية الأخيرة للمخرج.
- **التدريب**: حلقة PyTorch قياسية مع خسارة BCE للتصنيف الثنائي.
- **المخرج**: تنشيط Sigmoid يعطي احتمالية بين 0 و 1.

هذا نموذج RNN أساسي؛ للحصول على أداء أفضل على المتواليات الطويلة، فكر في استخدام متغيرات LSTM أو GRU (مثل استبدال `nn.RNN` بـ `nn.LSTM`).

### متغير LSTM (امتداد سريع)
لمشكلة تلاشي التدرج، استبدل بـ LSTM:

```python
# في فئة النموذج، استبدل:
self.rnn = nn.LSTM(input_size, hidden_size, batch_first=True)

# وفي التمريرة الأمامية:
h0 = torch.zeros(1, x.size(0), self.hidden_size)
c0 = torch.zeros(1, x.size(0), self.hidden_size)  # LSTM تحتاج حالة الخلية
out, (hn, cn) = self.rnn(x, (h0, c0))
```

شغّل هذا في بيئة PyTorch للتجربة!

[PyTorch RNN Documentation](https://pytorch.org/docs/stable/generated/torch.nn.RNN.html)  
[PyTorch LSTM Documentation](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html)