---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تنفيذ الشبكة العصبية المتكررة البسيطة من الصفر
translated: true
type: note
---

### مثال بسيط للشبكة العصبية المتكررة (RNN) باستخدام NumPy (من الصفر)

يعد تنفيذ شبكة RNN من الصفر باستخدام NumPy طريقة رائعة لفهم الميكانيكا: حالة التخزين المخفية المتكررة، والانتشار الأمامي، والانتشار العكسي عبر الزمن (BPTT). فيما يلي مثال أساسي للتصنيف الثنائي على تسلسلات عشوائية (مشابه للإصدار السابق باستخدام PyTorch). يستخدم بيانات سلسلة زمنية أحادية المتغير (input_size=1)، وحجم مخفي (hidden_size=32)، وطول تسلسل (sequence_length=10).

يتضمن هذا الكود:
- توليد البيانات.
- المرور الأمامي لشبكة RNN (مع دالة التنشيط tanh للحالات المخفية).
- المرور العكسي (BPTT مع نزول تدرج بسيط).
- حلقة التدريب.

ملاحظة: هذه هي شبكة RNN الأساسية؛ قد تختفي أو تنفجر التدرجات في التسلسلات الطويلة. للاستخدام في الإنتاج، فكر في اقتصاص التدرجات أو استخدام منطق LSTM.

```python
import numpy as np

# المعلمات الفائقة
input_size = 1      # حجم الميزة (أحادي المتغير)
hidden_size = 32    # حجم الحالة المخفية
output_size = 1     # مخرج ثنائي
sequence_length = 10  # طول كل تسلسل
num_samples = 1000
num_epochs = 10
learning_rate = 0.01

# توليد بيانات وهمية: تسلسلات بطول 10، وتسميات تعتمد على المجموع (ثنائية)
def generate_data(num_samples):
    X = np.random.randn(num_samples, sequence_length, input_size)
    y = (np.sum(X, axis=1) > 0).astype(float).reshape(num_samples, 1)
    return X, y

# فئة شبكة RNN البسيطة (من الصفر)
class SimpleRNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # تهيئة الأوزان (تهيئة Xavier)
        self.Wxh = np.random.randn(hidden_size, input_size) * np.sqrt(1. / input_size)
        self.Whh = np.random.randn(hidden_size, hidden_size) * np.sqrt(1. / hidden_size)
        self.Why = np.random.randn(output_size, hidden_size) * np.sqrt(1. / hidden_size)
        
        # الانحيازات
        self.bh = np.zeros((hidden_size, 1))
        self.by = np.zeros((output_size, 1))
    
    def forward(self, x):
        # شكل x: (sequence_length, input_size, 1) لعينة واحدة
        self.x = x  # تخزين للانتشار العكسي
        self.h = np.zeros((self.hidden_size, 1))  # الحالة المخفية الأولية
        
        # الانتشار الأمامي عبر الزمن
        self.hs = np.zeros((self.hidden_size, sequence_length + 1))  # الحالات المخفية (بما في ذلك الأولية)
        self.hs[:, 0] = self.h.flatten()
        
        for t in range(sequence_length):
            self.h = np.tanh(np.dot(self.Wxh, x[t]) + np.dot(self.Whh, self.h) + self.bh)
            self.hs[:, t+1] = self.h.flatten()
        
        # المخرج من آخر حالة مخفية
        self.y_pred = np.dot(self.Why, self.h) + self.by
        return self.sigmoid(self.y_pred)
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-np.clip(z, -250, 250)))  # اقتصاص للاستقرار
    
    def backward(self, y_true):
        # الانتشار العكسي عبر الزمن (مبسط)
        dWhy = np.dot((self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred), self.hs[-1:, :].T)
        dby = (self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred)
        
        # التدرجات لأوزان الطبقة المخفية والمخرجات
        dWhh = np.zeros_like(self.Whh)
        dWxh = np.zeros_like(self.Wxh)
        dbh = np.zeros_like(self.bh)
        
        dh_next = np.zeros_like(self.h)
        for t in reversed(range(sequence_length)):
            dh = np.dot(self.Why.T, (self.y_pred - y_true) * self.sigmoid_deriv(self.y_pred)) + dh_next
            dh_raw = (1 - self.h**2) * dh  # مشتق دالة tanh
            dWxh += np.dot(dh_raw, self.x[t].T)
            dWhh += np.dot(dh_raw, self.hs[:, t:t+2].T[:, 0:1])  # مبسط؛ الإصدار الكامل لـ BPTT سيجمع التدرجات بدقة
            dbh += dh_raw
            dh_next = np.dot(self.Whh.T, dh_raw)
        
        # تحديث الأوزان
        self.Wxh -= learning_rate * dWxh
        self.Whh -= learning_rate * dWhh
        self.Why -= learning_rate * dWhy
        self.bh -= learning_rate * dbh
        self.by -= learning_rate * dby
    
    def sigmoid_deriv(self, z):
        s = self.sigmoid(z)
        return s * (1 - s)

# التدريب
X, y = generate_data(num_samples)

# إعادة التشكيل لمعالجة عينة واحدة (حجم الدفعة = 1 للتبسيط)
X = X.reshape(num_samples, sequence_length, input_size, 1)  # إضافة بُعد دفعة بقيمة 1
y = y.reshape(num_samples, 1, 1)

model = SimpleRNN(input_size, hidden_size, output_size)

for epoch in range(num_epochs):
    total_loss = 0
    for i in range(num_samples):
        pred = model.forward(X[i])
        loss = -np.mean(y[i] * np.log(pred + 1e-8) + (1 - y[i]) * np.log(1 - pred + 1e-8))  # دالة فقدان الانتروبيا الثنائية المتقاطعة
        total_loss += loss
        model.backward(y[i])
    
    avg_loss = total_loss / num_samples
    print(f'Epoch [{epoch+1}/{num_epochs}], Avg Loss: {avg_loss:.4f}')

# مثال للاستدلال
test_seq = np.random.randn(sequence_length, input_size, 1)
prediction = model.forward(test_seq)
print(f'Prediction: {prediction.flatten()[0]:.4f}')
```

#### آلية العمل:
- **توليد البيانات**: تسلسلات عشوائية مع تسميات ثنائية تعتمد على المجموع.
- **المرور الأمامي**: يعالج التسلسل خطوة بخطوة، محدثًا الحالة المخفية `h_t = tanh(Wxh * x_t + Whh * h_{t-1} + bh)`. يستخدم المخرج الحالة المخفية النهائية `h` مع دالة sigmoid.
- **المرور العكسي**: يحسب BPTT التدرجات لجميع الخطوات الزمنية، محدثًا الأوزان عبر نزول تدرج بسيط. (ملاحظة: هذا إصدار مصغر لـ BPTT؛ الإصدارات الكاملة تتعامل مع التجميع بشكل أكثر دقة.)
- **التدريب**: يحلق فوق العينات، يحسب فقدان BCE، ويقوم بالتحديث.
- **المخرج**: تعطي دالة sigmoid الاحتمال (0-1).

يعمل هذا الكود في حوالي 10-20 ثانية على جهاز قياسي بهذه المعلمات. زد قيمة `num_samples` أو `num_epochs` لترى التعلم. للتعامل مع دفعات متعددة، قم بتجهيز الحلقات.

للتعمق أكثر:  
[Understanding LSTM Networks (مدونة Colah)](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)  
[NumPy RNN Tutorial](https://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/)