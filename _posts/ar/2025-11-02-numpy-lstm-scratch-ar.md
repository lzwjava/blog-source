---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تنفيذ LSTM من NumPy من الصفر
translated: true
type: note
---

هذا تنفيذ أساسي لشبكة الذاكرة طويلة المدى قصيرة المدى (LSTM) باستخدام NumPy فقط، مستوحى من المفاهيم في منشور المدونة الخاص بـ Christopher Olah حول فهم شبكات LSTM. يتضمن البوابات الأساسية (النسيان، والإدخال، والخلية المرشحة، والإخراج) ويركز على التمرير الأمامي. تتولى الفئة معالجة خطوة زمنية واحدة عبر `forward()` وتسلسل كامل عبر `forward_sequence()`.

يتم تهيئة الأوزان بشكل عشوائي (في الممارسة العملية، استخدم التهيئة الأفضل مثل Xavier/Glorot). لا يتم تضمين تمرير عكسي أو تدريب هنا — قم بالتوسيع باستخدام الانتشار الخلفي عبر الزمن (BPTT) لذلك.

```python
import numpy as np

class LSTM:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        # Initialize weights and biases for forget, input, cell, and output gates
        self.Wf = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wi = np.random.randn(hidden_size, hidden_size + input_size)
        self.WC = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wo = np.random.randn(hidden_size, hidden_size + input_size)
        self.bf = np.zeros((hidden_size, 1))
        self.bi = np.zeros((hidden_size, 1))
        self.bC = np.zeros((hidden_size, 1))
        self.bo = np.zeros((hidden_size, 1))

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def tanh(self, z):
        return np.tanh(z)

    def forward(self, x, h_prev, C_prev):
        # x: (input_size, 1), h_prev and C_prev: (hidden_size, 1)
        # Concatenate hidden state and input
        concat = np.vstack((h_prev, x))
        # Forget gate
        f_t = self.sigmoid(np.dot(self.Wf, concat) + self.bf)
        # Input gate
        i_t = self.sigmoid(np.dot(self.Wi, concat) + self.bi)
        C_tilda = self.tanh(np.dot(self.WC, concat) + self.bC)
        # Cell state update
        C_t = f_t * C_prev + i_t * C_tilda
        # Output gate
        o_t = self.sigmoid(np.dot(self.Wo, concat) + self.bo)
        # Hidden state update
        h_t = o_t * self.tanh(C_t)
        return h_t, C_t

    def forward_sequence(self, X):
        # X: (seq_len, input_size)
        h = np.zeros((self.hidden_size, 1))
        C = np.zeros((self.hidden_size, 1))
        outputs = []
        for x in X:
            h, C = self.forward(x.reshape(-1, 1), h, C)
            outputs.append(h)
        return np.hstack(outputs).T  # Returns (seq_len, hidden_size)

# Example usage
input_size = 3
hidden_size = 5
lstm = LSTM(input_size, hidden_size)

# Single step
x_t = np.random.randn(input_size, 1)
h_prev = np.zeros((hidden_size, 1))
C_prev = np.zeros((hidden_size, 1))
h_t, C_t = lstm.forward(x_t, h_prev, C_prev)
print("Single step - Hidden state shape:", h_t.shape)

# Sequence
X = np.random.randn(4, input_size)  # seq_len=4
outputs = lstm.forward_sequence(X)
print("Sequence outputs shape:", outputs.shape)
```

### شرح سريع
- **التهيئة**: تربط الأوزان الإدخال المدمج (الحالة المخفية السابقة + الإدخال الحالي) بكل بوابة. يتم تهيئة الانحيازات بصفر.
- **البوابات**:
  - **بوابة النسيان** (`f_t`): تقرر ما يجب نسيانه من حالة الخلية السابقة (sigmoid: 0-1).
  - **بوابة الإدخال** (`i_t`) و **الخلية المرشحة** (`C_tilda`): تقرران المعلومات الجديدة المطلوب إضافتها (sigmoid + tanh).
  - **بوابة الإخراج** (`o_t`): ترشح حالة الخلية لإنتاج الحالة المخفية (sigmoid + tanh على الخلية).
- **حالة الخلية** (`C_t`): تدفق خطي مع تحديات إضافية للذاكرة طويلة المدى.
- **الاستخدام**: للتسلسلات، قم بالتكرار خلال الخطوات الزمنية، وتحديث الحالات المخفية وحالات الخلية بشكل تدريجي.

هذا يتطابق مع بنية LSTM من مدونة كولاه: حالة الخلية كـ "طريق سريع" يتم التحكم فيه بواسطة البوابات.

[Understanding LSTMs: Implementation from Scratch](https://medium.com/@samina.amin/understanding-lstms-lstm-implementation-from-scratch-18965a150eca)