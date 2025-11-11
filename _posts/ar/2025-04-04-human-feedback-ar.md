---
audio: false
generated: true
lang: ar
layout: post
title: تعلم التعزيز بالملاحظات البشرية مُبسَّط
translated: true
type: note
---

**التعلم المعزز من خلال التغذية الراجعة البشرية (RLHF)** هي تقنية تعلم آلي تُستخدم لضبط النماذج الذكاء الاصطناعي بدقة، وخاصة نماذج اللغة الكبيرة (LLMs)، لتحسين محاذاتها مع تفضيلات البشر وتعليماتهم. بدلاً من الاعتماد فقط على دوال المكافأة المحددة مسبقًا، يدمج RLHF التغذية الراجعة المباشرة من البشر لتوجيه عملية التعلم.

**لماذا يعتبر RLHF مهمًا؟**

*   **المهام الذاتية:** يتفوق RLHF في المهام التي يصعب فيها تحديد النتيجة المرجوة بقواعد صريحة أو مكافآت رقمية، مثل توليد نص إبداعي، أو الدخول في محادثات طبيعية، أو إنتاج محتوى مفيد وغير ضار.
*   **الفروق الدقيقة والمحاذاة:** يساعد نماذج الذكاء الاصطناعي على فهم والالتزام بتفضيلات البشر الدقيقة، والاعتبارات الأخلاقية، وأنماط التفاعل المرغوبة.
*   **أداء محسن:** غالبًا ما تُظهر النماذج المدربة باستخدام RLHF أداءً ورضًا للمستخدم محسنًا بشكل ملحوظ مقارنة بتلك المدربة فقط بالتعلم المعزز التقليدي أو التعلم الخاضع للإشراف.

**كيف يعمل RLHF (عادة في ثلاث مراحل):**

1.  **التدريب المسبق والضبط الدقيق الخاضع للإشراف (SFT):**
    *   يتم أولاً تدريب نموذج لغة أساسي مسبقًا على مجموعة بيانات ضخمة من النص والكود لتعلم الفهم اللغوي العام والتوليد.
    *   ثم يتم غالبًا ضبط هذا النموذج المدرب مسبقًا بدقة باستخدام التعلم الخاضع للإشراف على مجموعة بيانات أصغر تحتوي على عروض توضيحية عالية الجودة للسلوك المطلوب (مثل كتابة البشر لردود مثالية على المطالبات). تساعد هذه الخطوة النموذج على فهم شكل ونمط المخرجات المتوقعة.

2.  **تدريب نموذج المكافأة:**
    *   هذه خطوة حاسمة في RLHF. يتم تدريب **نموذج مكافأة** منفصل للتنبؤ بتفضيلات البشر.
    *   يُعرض على المُعلّمين البشريين مخرجات مختلفة من نموذج SFT (أو إصدار لاحق) لنفس المطالبة. يقومون بترتيب أو تقييم هذه المخرجات بناءً على معايير مختلفة (مثل الفائدة، والتماسك، والسلامة).
    *   تُستخدم بيانات التفضيل هذه (مثل "المخرجات A أفضل من المخرجات B") لتدريب نموذج المكافأة. يتعلم نموذج المكافأة تعيين درجة مكافأة عددية لأي مخرجات نموذج معينة، تعكس مدى تفضيل البشر لها.

3.  **الضبط الدقيق بالتعلم المعزز:**
    *   يتم ضبط نموذج اللغة الأصلي (المهيأ من نموذج SFT) بدقة باستخدام التعلم المعزز.
    *   يعمل نموذج المكافأة المدرب في الخطوة السابقة كدالة المكافأة للبيئة.
    *   يولد وكيل التعلم المعزز (نموذج اللغة) ردودًا على المطالبات، ويقوم نموذج المكافأة بتقييم هذه الردود.
    *   تقوم خوارزمية التعلم المعزز (غالبًا Proximal Policy Optimization - PPO) بتحديث سياسة نموذج اللغة (كيفية توليده للنص) لتعظيم المكافآت المتوقعة من قبل نموذج المكافأة. يشجع هذا نموذج اللغة على توليد مخرجات تتماشى بشكل أكبر مع تفضيلات البشر.
    *   لمنع الضبط الدقيق بالتعلم المعزز من الانحراف بعيدًا عن سلوك نموذج SFT (والذي قد يؤدي إلى نتائج غير مرغوبة)، غالبًا ما يتم تضمين مصطلح تنظيمي (مثل عقوبة اختلاف Kullback-Leibler) في هدف التعلم المعزز.

**كيفية تنفيذ RLHF (خطوات مبسطة):**

1.  **جمع بيانات تفضيلات البشر:**
    *   صمم مطالبات أو مهامًا ذات صلة بسلوك الذكاء الاصطناعي المطلوب.
    *   قم بتوليد ردود متعددة لهذه المطالبات باستخدام نموذجك الحالي.
    *   قم بتوظيف مُعلّمين بشريين لمقارنة هذه الردود والإشارة إلى تفضيلاتهم (مثل ترتيبها، أو اختيار الأفضل، أو تقييمها).
    *   قم بتخزين هذه البيانات كأزواج من (المطالبة، الرد المفضل، الرد الأقل تفضيلاً) أو صيغ مشابهة.

2.  **تدريب نموذج مكافأة:**
    *   اختر بنية نموذج مناسبة لنموذج المكافأة الخاص بك (غالبًا نموذج قائم على المحولات مشابه لنموذج اللغة).
    *   قم بتدريب نموذج المكافأة على بيانات تفضيلات البشر التي تم جمعها. الهدف هو أن يعين نموذج المكافأة درجات أعلى للردود التي فضلها البشر. إحدى دوال الخسارة الشائعة المستخدمة تعتمد على تعظيم الفارق بين درجات الردود المفضلة والأقل تفضيلاً.

3.  **ضبط نموذج اللغة بدقة باستخدام التعلم المعزز:**
    *   قم بتهيئة نموذج اللغة الخاص بك بالأوزان من خطوة SFT (إذا قمت بتنفيذها).
    *   استخدم خوارزمية تعلم معزز (مثل PPO).
    *   لكل خطوة تدريب:
        *   اختر عينة مطالبة.
        *   اجعل نموذج اللغة يولد ردًا.
        *   استخدم نموذج المكافأة المدرب للحصول على درجة مكافأة للرد المُولد.
        *   قم بتحديث معلمات نموذج اللغة بناءً على إشارة المكافأة لتشجيع الإجراءات (توليد الرموز) التي تؤدي إلى مكافآت أعلى.
        *   قم بتضمين مصطلح تنظيمي (مثل اختلاف KL) للحفاظ على السياسة المحدثة قريبة من سياسة SFT.

**مثال برمجي (مفاهيمي ومبسط باستخدام PyTorch):**

هذا مثال مفاهيمي مبسط للغاية لتوضيح الأفكار الأساسية. تنفيذ RLHF كامل أكثر تعقيدًا بكثير ويتضمن استخدام مكتبات مثل Hugging Face Transformers و Accelerate ومكتبات التعلم المعزز.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

# افترض أنك جمعت بيانات تفضيلات بشرية:
# قائمة من tuples: (prompt, preferred_response, less_preferred_response)
preference_data = [
    ("Write a short story about a cat.", "Whiskers the cat lived in a cozy cottage...", "A cat story. The end."),
    ("Summarize this article:", "The article discusses...", "Article summary."),
    # ... المزيد من البيانات
]

# 1. تحميل نموذج اللغة المدرب مسبقًا والموحد
model_name = "gpt2"  # أو أي نموذج مدرب مسبقًا مناسب آخر
policy_model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_model.to(device)

# 2. تعريف نموذج مكافأة بسيط
class RewardModel(nn.Module):
    def __init__(self, base_model):
        super().__init__()
        self.base_model = base_model.transformer  # استخدام طبقات المحولات
        self.v_head = nn.Linear(base_model.config.n_embd, 1)

    def forward(self, input_ids, attention_mask):
        outputs = self.base_model(input_ids=input_ids, attention_mask=attention_mask)
        last_hidden_states = outputs.last_hidden_state
        reward = self.v_head(last_hidden_states[:, -1])  # الحصول على المكافأة من الرمز الأخير
        return reward

reward_model = RewardModel(policy_model)
reward_model.to(device)
reward_optimizer = optim.AdamW(reward_model.parameters(), lr=1e-5)
reward_criterion = nn.MarginRankingLoss(margin=1.0) # تشجيع مكافأة أعلى للمفضل

# تدريب نموذج المكافأة
num_reward_epochs = 3
for epoch in range(num_reward_epochs):
    for prompt, preferred, less_preferred in preference_data:
        preferred_tokens = tokenizer(prompt + preferred, return_tensors="pt", truncation=True, max_length=128).to(device)
        less_preferred_tokens = tokenizer(prompt + less_preferred, return_tensors="pt", truncation=True, max_length=128).to(device)

        preferred_reward = reward_model(**preferred_tokens)
        less_preferred_reward = reward_model(**less_preferred_tokens)

        labels = torch.ones(preferred_reward.size(0)).to(device) # نريد preferred > less preferred
        loss = reward_criterion(preferred_reward, less_preferred_reward, labels)

        reward_optimizer.zero_grad()
        loss.backward()
        reward_optimizer.step()
    print(f"Reward Epoch {epoch+1}, Loss: {loss.item()}")

# 3. الضبط الدقيق بالتعلم المعزز (مفاهيمي - PPO معقد)
policy_optimizer = optim.AdamW(policy_model.parameters(), lr=5e-6)

num_rl_episodes = 5
for episode in range(num_rl_episodes):
    for prompt in [data[0] for data in preference_data]: # عينات من المطالبات
        input_tokens = tokenizer(prompt, return_tensors="pt").to(device)
        output_sequences = policy_model.generate(
            input_tokens.input_ids,
            max_length=60,
            num_return_sequences=1,
            do_sample=True,
            top_k=50,
            top_p=0.95,
        )
        generated_response = tokenizer.decode(output_sequences[0], skip_special_tokens=True)

        response_tokens = tokenizer(prompt + generated_response, return_tensors="pt", truncation=True, max_length=128).to(device)
        reward = reward_model(**response_tokens)

        # (مبسط) تحديث السياسة - في الواقع، يستخدم PPO طرق أكثر تطورًا
        loss = -reward.mean() # محاولة تعظيم المكافأة
        policy_optimizer.zero_grad()
        loss.backward()
        policy_optimizer.step()

    print(f"RL Episode {episode+1}, Reward: {reward.item()}, Response: {generated_response}")

print("RLHF Training Done!")
```

**التحديات الرئيسية في RLHF:**

*   **جمع البيانات:** يمكن أن يكون الحصول على بيانات تفضيلات بشرية عالية الجودة ومتنوعة مكلفًا ويستغرق وقتًا طويلاً.
*   **الذاتية والتحيز:** يمكن أن تكون تفضيلات البشر ذاتية وقد تحتوي على تحيزات، يمكن لنموذج المكافأة تعلمها.
*   **اختراق المكافأة:** قد يجد وكيل التعلم المعزز طرقًا لاستغلال نموذج المكافأة لا تتماشى مع تفضيلات البشر الحقيقية.
*   **القابلية للتوسع:** يتطلب توسيع نطاق RLHF لنماذج ومجموعات بيانات كبيرة جدًا موارد حاسوبية كبيرة وهندسة دقيقة.
*   **عدم الاستقرار:** يمكن أن يكون تدريب نماذج RLHF غير مستقر ويتطلب ضبطًا دقيقًا للمعاملات الفائقة.

على الرغم من هذه التحديات، أثبت RLHF أنه تقنية قوية لمحاذاة نماذج الذكاء الاصطناعي مع القيم البشرية وهو مكون رئيسي في تطوير نماذج اللغة المتطورة مثل ChatGPT وغيرها.