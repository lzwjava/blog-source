---
audio: false
generated: true
lang: ar
layout: post
title: عدم تطابق الأبعاد في الموترات
translated: true
type: note
---

يبدو أنك واجهت خطأ أثناء تدريب نموذج المكافأة كجزء من إعداد التعلم المعزز من التغذية الراجعة البشرية (RLHF) باستخدام PyTorch ومكتبة Transformers. تشير رسالة الخطأ إلى عدم تطابق في الأبعاد في دالة `MarginRankingLoss`، التي تتوقع أن يكون لكل موترات الإدخال (`input1`، `input2`، و `target`) نفس الحجم. دعنا نحلل هذا المشكل ونصلحه.

### الخطأ
يظهر تتبع المكالمات (traceback) ما يلي:
```
RuntimeError: margin_ranking_loss : All input tensors should have same dimension but got sizes: input1: torch.Size([1, 1]), input2: torch.Size([1, 1]), target: torch.Size([1])
```
- `preferred_reward` (input1) و `less_preferred_reward` (input2) لهما الحجم `[1, 1]`.
- `labels` (target) له الحجم `[1]`.

تتوقع `MarginRankingLoss` أن تكون للمدخلات والهدف أبعاد متوافقة. هنا، البعد الإضافي في `preferred_reward` و `less_preferred_reward` (أي `[1, 1]` مقابل `[1]`) هو سبب عدم التطابق. هذا على الأرجح لأن نموذج المكافأة يخرج موترًا ببعد إضافي من الطبقة الخطية (`self.v_head`).

### لماذا يحدث هذا
في `RewardModel` الخاص بك:
```python
reward = self.v_head(last_hidden_states[:, -1])  # Shape: [batch_size, 1]
```
تخرج الطبقة `v_head` نتيجة مكافأة بشكل `[batch_size, 1]` (مثلاً `[1, 1]` لحجم دفعة 1). بينما يتم إنشاء `labels` كالتالي:
```python
labels = torch.ones(preferred_reward.size(0)).to(device)  # Shape: [batch_size]
```
هذا يعطي `labels` شكلاً `[1]`، والذي لا يتطابق مع `[1, 1]` للمكافآت.

### الإصلاح
لحل هذا، تحتاج إلى التأكد من أن موترات المكافأة وموتر الهدف لها أشكال متوافقة. بما أن `MarginRankingLoss` تتوقع موترات 1D (أو على الأقل أشكال متطابقة)، يمكنك ضغط البعد الإضافي من مخرجات المكافأة. إليك كيفية تعديل حلقة التدريب:

#### مقتطف الكود المحدث
```python
# Train the Reward Model
num_reward_epochs = 3
for epoch in range(num_reward_epochs):
    for prompt, preferred, less_preferred in preference_data:
        preferred_tokens = tokenizer(prompt + preferred, return_tensors="pt", truncation=True, max_length=128).to(device)
        less_preferred_tokens = tokenizer(prompt + less_preferred, return_tensors="pt", truncation=True, max_length=128).to(device)

        preferred_reward = reward_model(**preferred_tokens).squeeze()  # Remove extra dimension
        less_preferred_reward = reward_model(**less_preferred_tokens).squeeze()  # Remove extra dimension

        labels = torch.ones(preferred_reward.size(0)).to(device)  # Shape: [batch_size], e.g., [1]
        loss = reward_criterion(preferred_reward, less_preferred_reward, labels)

        reward_optimizer.zero_grad()
        loss.backward()
        reward_optimizer.step()
    print(f"Reward Epoch {epoch+1}, Loss: {loss.item()}")
```

#### التغيير الرئيسي
- أضيف `.squeeze()` إلى `preferred_reward` و `less_preferred_reward` لتقليل شكلهما من `[1, 1]` إلى `[1]`، ليتطابق مع موتر `labels`.

### ملاحظات إضافية
1. **اعتبار حجم الدفعة (Batch Size)**:
   - إذا قمت لاحقًا بزيادة حجم الدفعة (مثلاً معالجة عدة أمثلة في وقت واحد)، تأكد من أن `preferred_tokens` و `less_preferred_tokens` يتم تجميعها بشكل صحيح، وأن الأشكال ستظل متوافقة بعد الضغط.

2. **خرج نموذج المكافأة (Reward Model Output)**:
   - نموذج المكافأة الحالي يأخذ آخر حالة خفية (`last_hidden_states[:, -1]`) ويمررها عبر طبقة خطية. هذا جيد لنموذج مكافأة بسيط، ولكن يمكنك تجميع الحالات الخفية (مثلاً mean pooling) للحصول على تقييم أكثر دقة.

3. **حلقة RL**:
   - حلقة الضبط الدقيق للـ RL الخاصة بك تستخدم دالة خسارة مبسطة (`-reward.mean()`). عمليًا، يستخدم RLHF عادة خوارزميات مثل PPO (Proximal Policy Optimization)، والتي تتطلب إعدادًا أكثر تعقيدًا (مثلاً دالة قيمة، أهداف مقصوصة). حالياً، نهجك يعمل كدليل على المفهوم.

4 **حشو الرماز (Tokenizer Padding)**:
   - قد ترغب في إضافة `padding=True` إلى استدعاءات الرماز لضمان طول مدخلات متسق، على الرغم من أن `truncation=True` مع `max_length` يجب أن تتعامل مع معظم الحالات هنا.

### مثال عمل كامل (مبسط)
إليك نسخة مصححة ومبسطة من حلقة تدريب المكافأة الخاصة بك:
```python
import torch
import torch.nn as nn
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

# Sample data
preference_data = [
    ("Write a story about a cat.", "Whiskers the cat lived in a cozy cottage...", "A cat story. The end."),
]

# Load model and tokenizer
model_name = "gpt2"
policy_model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_model.to(device)

# Reward Model
class RewardModel(nn.Module):
    def __init__(self, base_model):
        super().__init__()
        self.base_model = base_model.transformer
        self.v_head = nn.Linear(base_model.config.n_embd, 1)

    def forward(self, input_ids, attention_mask):
        outputs = self.base_model(input_ids=input_ids, attention_mask=attention_mask)
        last_hidden_states = outputs.last_hidden_state
        reward = self.v_head(last_hidden_states[:, -1])
        return reward

reward_model = RewardModel(policy_model).to(device)
reward_optimizer = optim.AdamW(reward_model.parameters(), lr=1e-5)
reward_criterion = nn.MarginRankingLoss(margin=1.0)

# Train Reward Model
for epoch in range(3):
    for prompt, preferred, less_preferred in preference_data:
        preferred_tokens = tokenizer(prompt + preferred, return_tensors="pt", truncation=True, max_length=128).to(device)
        less_preferred_tokens = tokenizer(prompt + less_preferred, return_tensors="pt", truncation=True, max_length=128).to(device)

        preferred_reward = reward_model(**preferred_tokens).squeeze()
        less_preferred_reward = reward_model(**less_preferred_tokens).squeeze()

        labels = torch.ones(preferred_reward.size(0)).to(device)
        loss = reward_criterion(preferred_reward, less_preferred_reward, labels)

        reward_optimizer.zero_grad()
        loss.backward()
        reward_optimizer.step()
    print(f"Reward Epoch {epoch+1}, Loss: {loss.item()}")
```

هذا يجب أن يحل مشكلة عدم تطابق الأبعاد ويسمح لنموذج المكافأة الخاص بك بالتدريب بنجاح. دعني أعلم إذا كنت بحاجة إلى مزيد من التوضيح أو المساعدة في جزء RL!

---

### فهم وإصلاح IndexError في سكريبت PyTorch الخاص بك

رسالة الخطأ التي واجهتها في سكريبت Python الخاصة بك هي:

```
IndexError: Dimension specified as 0 but tensor has no dimensions
```

يحدث هذا في السطر 44 من سكريبتك، `rl.py`، ضمن السطر التالي:

```python
labels = torch.ones(preferred_reward.size(0)).to(device)
```

يشير الخطأ إلى أن `preferred_reward` هو موتر عددي (أي ليس له أبعاد، بشكل `[]`)، ومحاولة الوصول إلى بعده الأول باستخدام `.size(0)` غير صالحة لأن العددية ليس لها أبعاد للفهرسة.

دعنا نحلل هذا خطوة بخطوة ونقدم حلاً.

---

### لماذا يحدث هذا الخطأ

في سكريبتك، من المحتمل أنك تقوم بتدريب نموذج مكافأة باستخدام دالة خسارة مثل `MarginRankingLoss`، التي تتوقع أن تكون مدخلاتها (`preferred_reward`، `less_preferred_reward`، و `labels`) موترات بأشكال متوافقة—عادة موترات 1D حيث كل عنصر يقابل عينة في دفعة. إليك ما يحدث:

1. **أصل `preferred_reward`:**
   - `preferred_reward` هو ناتج عملية التمرير الأمامي لـ `reward_model`، مثلاً `reward_model(**preferred_tokens)`.
   - بافتراض أن نموذج المكافأة الخاص بك يخرج قيمة واحدة لكل عينة، لحجم دفعة 1، شكل الخرج هو `[1, 1]` (حجم الدفعة × بعد الخرج).

2. **ضغط الموتر (Squeezing the Tensor):**
   - في الكود الأصلي، تطبق `.squeeze()` على `preferred_reward`:
     ```python
     preferred_reward = reward_model(**preferred_tokens).squeeze()
     ```
   - طريقة `.squeeze()` تزيل *كل* الأبعاد ذات الحجم 1. لموتر بشكل `[1, 1]`، هذا يختصره إلى `[]`—موتر عددي بدون أبعاد.

3. **الوصول إلى الحجم (Accessing the Size):**
   - لاحقًا، تحاول إنشاء موتر `labels` بنفس حجم الدفعة مثل `preferred_reward`:
     ```python
     labels = torch.ones(preferred_reward.size(0)).to(device)
     ```
   - بالنسبة لموتر عددي (`[]`)، `preferred_reward.size()` تُرجع `torch.Size([])`، وهي مجموعة أبعاد فارغة. محاولة الوصول إلى البعد الأول باستخدام `.size(0)` ترفع `IndexError` لأنه لا توجد أبعاد للوصول إليها.

4. **السلوك المتوقع (Expected Behavior):**
   - دالة `MarginRankingLoss` تتطلب أن يكون لمدخلاتها (`preferred_reward`، `less_preferred_reward`، و `labels`) نفس الشكل، عادة موترات 1D مثل `[batch_size]`. لحجم دفعة 1، هذا يجب أن يكون `[1]`، وليس عددياً `[]`.

السبب الجذري هو أن `.squeeze()` عدوانية جدًا—فهي تزيل كل الأبعاد المفردة، محولة `[1, 1]` إلى عددية `[]` عندما يكون حجم الدفعة 1، مما يكسر استدعاء `.size(0)` اللاحق.

---

### الإصلاح

لحل هذا، تحتاج إلى التأكد من أن `preferred_reward` و `less_preferred_reward` يبقيان موترات 1D بشكل `[batch_size]`، حتى عندما يكون `batch_size=1`. بدلاً من استخدام `.squeeze()`، التي تزيل كل الأبعاد ذات الحجم 1، استخدم `.squeeze(-1)` لإزالة البعد الأخير فقط. هذا يحول `[1, 1]` إلى `[1]`، محافظًا على بُعد الدفعة.

إليك مقتطف الكود المصحح لحلقة تدريب نموذج المكافأة الخاصة بك:

```python
# Train the Reward Model
num_reward_epochs = 3
for epoch in range(num_reward_epochs):
    for prompt, preferred, less_preferred in preference_data:
        # Tokenize inputs
        preferred_tokens = tokenizer(prompt + preferred, return_tensors="pt", truncation=True, max_length=128).to(device)
        less_preferred_tokens = tokenizer(prompt + less_preferred, return_tensors="pt", truncation=True, max_length=128).to(device)

        # Compute rewards, squeezing only the last dimension
        preferred_reward = reward_model(**preferred_tokens).squeeze(-1)  # Shape: [1]
        less_preferred_reward = reward_model(**less_preferred_tokens).squeeze(-1)  # Shape: [1]

        # Create labels tensor based on batch size
        labels = torch.ones(preferred_reward.size(0)).to(device)  # Shape: [1]
        
        # Compute loss
        loss = reward_criterion(preferred_reward, less_preferred_reward, labels)

        # Backpropagation
        reward_optimizer.zero_grad()
        loss.backward()
        reward_optimizer.step()
    
    print(f"Reward Epoch {epoch+1}, Loss: {loss.item()}")
```

#### كيف يعمل هذا

- **بعد `.squeeze(-1)`:**
  - الشكل الأصلي من `reward_model`: `[1, 1]` (batch_size=1, output_dim=1).
  - بعد `.squeeze(-1)`: `[1]` (يزيل البعد الأخير فقط).
  - `preferred_reward.size(0)` تُرجع `1`، حجم الدفعة.
  - `labels` تصبح موتر 1D بشكل `[1]`، مطابقًا لشكل `preferred_reward` و `less_preferred_reward`.

- **التوافق مع `MarginRankingLoss`:**
  - تتوقع `MarginRankingLoss` أن يكون لـ `input1` (`preferred_reward`)، `input2` (`less_preferred_reward`)، و `target` (`labels`) نفس الشكل. مع كون الثلاثة بشكل `[1]`، عملية حساب الخسارة تستمر بدون أخطاء.

- **القابلية للتوسع (Scalability):**
  - إذا استخدمت لاحقًا حجم دفعة أكبر (مثلاً 2)، مخرجات نموذج المكافأة `[2, 1]`، `.squeeze(-1)` تنتج `[2]`، و `labels` تصبح `[2]`، محافظة على الاتساق.

---

### طرق بديلة

بينما `.squeeze(-1)` هو إصلاح نظيف ودقيق، إليك طريقتين أخريين ستعملان أيضًا:

1. **استخدام الفهرسة (Using Indexing):**
   ```python
   preferred_reward = reward_model(**preferred_tokens)[:, 0]  # Shape: [1]
   less_preferred_reward = reward_model(**less_preferred_tokens)[:, 0]  # Shape: [1]
   ```
   - هذا يختار العنصر الأول (والوحيد) للبعد الأخير، محولاً `[1, 1]` إلى `[1]`.

2. **استخدام `.view(-1)`:**
   ```python
   preferred_reward = reward_model(**preferred_tokens).view(-1)  # Shape: [1]
   less_preferred_reward = reward_model(**less_preferred_tokens).view(-1)  # Shape: [1]
   ```
   - هذا يسطح الموتر إلى موتر 1D. لـ `[1, 1]`، يصبح `[1]` لأنه يحتوي على عنصر واحد فقط.

كلا البديلين يحققان نفس نتيجة `.squeeze(-1)` في هذا السياق، لكن `.squeeze(-1)` مفضل لأنه يستهدف البعد الأخير صراحة، متوافقًا مع هيكل خرج نموذج المكافأة (`[batch_size, 1]`).

---

### ملاحظات إضافية

- **تحذيرات في الخرج (Warnings in the Output):**
  - رسائل `FutureWarning` حول `torch.utils._pytree._register_pytree_node` و `resume_download` غير مرتبطة بـ `IndexError`. هي تأتي من مكتبة `transformers` وتشير إلى دوال أو سلوكيات مهملة سوف تتغير في الإصدارات المستقبلية. حالياً، لا تؤثر على وظيفة سكريبتك ويمكن تجاهلها إلا إذا أردت تحديث الكود الخاص بك لتكون متوافقة مستقبليًا.

- **خرج نموذج المكافأة (Reward Model Output):**
  - يفترض الإصلاح أن `reward_model` الخاص بك يخرج موترًا بشكل `[batch_size, 1]`. إذا كان هيكله مختلفًا (مثلاً يخرج قيمة عددية مباشرة أو شكل مختلف)، ستحتاج للتعديل وفقًا لذلك. بناءً على تصاميم نموذج المكافأة النموذجية، `[batch_size, 1]` هو المعيار بعد رأس خطي.

- **التجميع (Batching):**
   - حلقتك الحالية تعالج زوج تفضيل واحد في كل مرة (حجم دفعة ضمني 1). إذا كنت تخطط للزيادة، فكر في تجميع أزواج متعددة باستخدام DataLoader لتحسين الكفاءة، لكن إصلاح `.squeeze(-1)` سيظل ينطبق.

---

### التحقق (Verification)

لحجم دفعة 1:
- `reward_model(**preferred_tokens)`: `[1, 1]`
- بعد `.squeeze(-1)`: `[1]`
- `preferred_reward.size(0)`: `1`
- `labels`: `[1]`
- مدخلات الخسارة: كلها `[1]`—تعمل بشكل مثالي.

يتم إزالة `IndexError`، ويجب أن يعمل تدريب نموذج المكافأة الخاص بك الآن بسلاسة.

---

### الإجابة النهائية

لإصلاح `IndexError: Dimension specified as 0 but tensor has no dimensions` في السطر 44 من `rl.py`، استبدل `.squeeze()` بـ `.squeeze(-1)` عند حساب `preferred_reward` و `less_preferred_reward`. هذا يضمن بقاءهما موترات 1D بشكل `[1]` (أو `[batch_size]` للدفعات الأكبر)، مما يسمح لـ `preferred_reward.size(0)` باسترداد حجم الدفعة بشكل صحيح لإنشاء موتر `labels`.

طبق هذا التغيير في حلقة تدريب نموذج المكافأة كما هو موضح أعلاه، وسيتم حل الخطأ.