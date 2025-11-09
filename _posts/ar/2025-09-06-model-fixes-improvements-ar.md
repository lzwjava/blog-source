---
audio: false
date: 2025-09-06
generated: true
image: false
lang: ar
layout: post
title: إصلاحات وتحسينات شكل النموذج
translated: true
type: note
---

إليك ما يفعله نصّك البرمجي، قطعة قطعة، بالإضافة إلى بعض الإصلاحات المهمة التي من المحتمل أنك ترغب في إجرائها.

# ما هو النموذج

* أنت تُعرّف **متنبئًا صغيرًا بالرمز المميز التالي على مستوى الحرف/الكلمة**:

  * `nn.LSTM(input_size=vocab_size, hidden_size=50, num_layers=1)` تعالج تسلسلًا لمتجهات one-hot (حجمها = `vocab_size`) وتنتج حالة خفية بحجم 50 في كل خطوة زمنية.
  * `nn.Linear(50, vocab_size, bias=False)` تُحوّل الحالة الخفية لكل خطوة زمنية إلى **قيم logits عبر المفردات**.

# الأشكال المتوقعة للموتر (أمر بالغ الأهمية)

الشكل الافتراضي للإدخال في PyTorch LSTM هو **(seq\_len, batch\_size, input\_size)** لأنك لم تضبط `batch_first=True`.

* لتسلسل واحد في دفعة batch حجمها 1:

  * يجب أن تكون مدخلات LSTM بالشكل `(seq_len, 1, vocab_size)`.
  * مخرجات LSTM `x` تكون بالشكل `(seq_len, 1, hidden_size)`.
  * ثم تستخدم `view(-1, hidden_size)` → `(seq_len, hidden_size)` حتى تنتج الطبقة الخطية `(seq_len, vocab_size)`.
  * تتوقع `CrossEntropyLoss`:

    * `outputs`: `(N, C)` = `(seq_len, vocab_size)`
    * `targets`: `(N,)` = `(seq_len,)` (فهارس الرموز المميزة tokens)

# حيث من المحتمل أن ينحرف الكود الخاص بك (الشكل)

أنت تفعل:

```python
inputs_one_hot = inputs_one_hot.permute(0, 2, 1)
```

إذا كانت `one_hot_encode_sequence` تُرجع `(batch, seq_len, vocab)`، فإن التبديل الصحيح لـ LSTM الافتراضي هو **`permute(1, 0, 2)`** (للحصول على `(seq_len, batch, vocab)`). التبديل الحالي `permute(0,2,1)` يُعطي `(batch, vocab, seq_len)`، وهو غير متطابق وسيؤدي إما إلى خطأ أو سيتعلم بصمت هراء إذا كان الشكل السابق مختلفًا عما هو مفترض.

خياران نظيفان (اختر واحدًا):

**أ) الاحتفاظ بـ LSTM الافتراضي (batch\_second):**

```python
# نريد (seq_len, batch, input_size)
inputs_one_hot = inputs_one_hot.permute(1, 0, 2)  # (seq_len, 1, vocab_size)
```

**ب) جعله batch-first (أبسط غالبًا):**

```python
self.lstm = nn.LSTM(input_size=vocab_size, hidden_size=50, batch_first=True)
# نريد (batch, seq_len, input_size)
# ثم لا تقم بالتبديل permute؛ اتركه كما هو (1, seq_len, vocab_size)
```

# منطق حلقة التدريب

* تحتفظ بمجموعين متراكمين لكل دورة تدريب epoch: `epoch_training_loss` و `epoch_validation_loss`.
* **مرحلة التحقق من الصحة Validation phase** (`net.eval()` + لا توجد خطوات تدرج gradient):

  * لكل (inputs, targets) في `validation_set`:

    * ترميز المدخلات one-hot، تحويل الأهداف targets إلى فهارس indices.
    * تمريرة أمامية forward pass → قيم logits بالشكل `(seq_len, vocab_size)` (بافتراض ثبات الأشكال).
    * فقدان CE مقابل فهارس الأهداف targets بالشكل `(seq_len,)`.
    * تراكم الخسارة loss.
* **مرحلة التدريب Training phase** (`net.train()`):

  * نفس المعالجة المسبقة.
  * تمريرة أمامية → خسارة → `optimizer.zero_grad()` → `loss.backward()` → `optimizer.step()`.
* تسجل متوسط الخسائر وتطبع كل 5 دورات تدريب epochs.

# الاستدلال Inference والطباعة

* تختار عينة من `test_set`، تشغّل النموذج، تحصل على قيم logits لكل خطوة زمنية، تأخذ `argmax` لكل خطوة زمنية → الرموز المميزة المتوقعة predicted tokens.
* تطبع كلمات الإدخال، وكلمات الهدف، والكلمات المتوقعة.
* ترسم مخططًا للخسارة في التدريب مقابل الخسارة في التحقق عبر الدورات التدريبية.

# تحسينات صغيرة ذات تأثير كبير

1.  **إصلاح شكل الإدخال** (الأهم). استخدم إما أ أو ب أعلاه. إذا اخترت batch-first، غيّر التمريرة الأمامية إلى:

    ```python
    x, (h, c) = self.lstm(x)         # x: (batch, seq, hidden)
    x = x.reshape(-1, self.lstm.hidden_size)  # (batch*seq, hidden)
    ```
2.  **استخدم `with torch.no_grad()` للتقييم/الاستدلال** لتجنب تتبع التدرجات وللسرعة/الذاكرة:

    ```python
    net.eval()
    with torch.no_grad():
        outputs = net(inputs_one_hot)
        loss = criterion(outputs, targets_idx)
    ```

    وللتحويل إلى numpy:

    ```python
    outputs = net(inputs_one_hot).detach().numpy()
    ```
3.  **إعداد بذرة العشوائية لـ PyTorch أيضًا** لإمكانية إعادة النتائج:

    ```python
    torch.manual_seed(42)
    ```
4.  **التعامل مع الجهاز device** (إذا كنت تستخدم GPU):

    ```python
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net.to(device)
    inputs_one_hot = inputs_one_hot.to(device)
    targets_idx = targets_idx.to(device)
    ```
5.  **محاذاة الأهداف targets**: تأكد من أن `targets` هي **الرموز المميزة التالية** محاذية مع كل خطوة إدخال زمنية. إذا كانت مجموعة البيانات الخاصة بك تقترن `(inputs, targets)` بهذه الطريقة، فأنت على ما يرام. وإلا، أنشئ `targets = inputs[1:]` وأسقط آخر إدخال أو ما شابه.
6.  **أسقط `.bias=False` ما لم يكن لديك سبب**؛ عادةً ما يكون الانحياز bias في طبقة الإخراج غير ضار/مفيد.
7.  **الحشو Padding/أطوال متغيرة** (اختياري): إذا كانت التسلسلات ذات أطوال متفاوتة، ففكر في `pack_padded_sequence` لتجنب التدريب على رموز الحشو.
8.  **المراقبة**: يمكن أن تكون دقة التنبؤات للرمز المميز التالي أكثر قابلية للتفسير من الخسارة وحدها — احسب `% correct argmax` في بيانات التحقق.

# snippet مصححة minimal (إصدار batch-first)

```python
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(input_size=vocab_size, hidden_size=50, num_layers=1, batch_first=True)
        self.l_out = nn.Linear(50, vocab_size)

    def forward(self, x):
        # x: (batch, seq, vocab_size)
        x, _ = self.lstm(x)                    # (batch, seq, hidden)
        x = x.reshape(-1, self.lstm.hidden_size)  # (batch*seq, hidden)
        x = self.l_out(x)                      # (batch*seq, vocab)
        return x

# ... في الحلقة الخاصة بك، أزل التبديل permute؛ تأكد من أن inputs_one_hot هو (batch, seq, vocab)
# استخدم `with torch.no_grad()` و `.detach()` في التحقق/الاستدلال
```

إذا شاركت الشكل الدقيق الذي تُرجعه `one_hot_encode_sequence` (مثل `(seq, vocab)` مقابل `(1, seq, vocab)`)، يمكنني تخصيص أسطر التبديل/إعادة التشكيل بدقة لحالتك.