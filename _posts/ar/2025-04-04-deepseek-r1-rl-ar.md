---
audio: false
generated: true
lang: ar
layout: post
title: ديب سيك آر 1
translated: true
type: note
---

يستخدم DeepSeek R1 نهجًا جديدًا في التعلم المعزز (RL) يركز بشكل كبير على **القدرات الاستدلالية** في نماذج اللغة الكبيرة (LLMs). تختلف تقنيتهم عن التعلم المعزز من التغذية الراجعة البشرية (RLHF) التقليدي في عدة جوانب رئيسية.

إليك تفصيلًا للتقنيات التي استخدمها DeepSeek في التعلم المعزز لـ R1:

**1. التعلم المعزز الخالص (RL) للاستدلال الأولي (DeepSeek-R1-Zero):**

* **بدءًا بدون الضبط الدقيق بالإشراف (SFT) على التعليمات:** على عكس العديد من نماذج اللغة الكبيرة التي تخضع أولاً لـ SFT على التعليمات المكتوبة بواسطة البشر، تم تدريب DeepSeek-R1-Zero باستخدام **التعلم المعزز الخالص** مباشرة على النموذج الأساسي (DeepSeek-V3-Base).
* **تحسين السياسة النسبي الجماعي (GRPO):** استخدموا GRPO كخوارزمية التعلم المعزز الأساسية الخاصة بهم. تم تصميم GRPO ليكون أكثر كفاءة من تحسين السياسة التقريبي (PPO) من خلال إلغاء الحاجة إلى شبكة ناقد منفصلة. حيث تقدر المكافآت الأساسية من خلال مقارنة مجموعة من المخرجات المُولَّدة، وتعيين درجات نسبية بناءً على جودتها. يشجع هذا النموذج على توليد استجابات أفضل مقارنة بمحاولاته السابقة.
* **نظام المكافآت القائم على القواعد:** بدلاً من الاعتماد فقط على التفضيلات البشرية لمرحلة التعلم المعزز الأولية، استخدم DeepSeek-R1-Zero **نظام مكافآت قائم على القواعد**. ركز هذا النظام بشكل أساسي على:
    * **مكافآت الدقة:** مكافأة النموذج على تقديم إجابات صحيحة، خاصة في المهام ذات الحلول القابلة للتحقق مثل مسائل الرياضيات (التحقق مما إذا كانت الإجابة النهائية صحيحة).
    * **مكافآت التنسيق:** مكافأة النموذج على الالتزام بتنسيق إخراج محدد، خاصة باستخدام علامات `` لتضمين عملية استدلاله. شجع هذا على ظهور استدلال سلسلة الأفكار.
* **السلوكيات الاستدلالية الناشئة:** سمح هذا النهج بالتعلم المعزز الخالص لـ DeepSeek-R1-Zero بتطوير مهارات استدلالية مذهلة بشكل طبيعي، بما في ذلك التحقق الذاتي، والتأمل، وتوليف شروحات طويلة لسلسلة الأفكار، دون وجود عروض توضيحية بشرية صريحة لهذه السلوكيات.

**2. التدريب متعدد المراحل لتحسين قابلية القراءة والقدرات العامة (DeepSeek-R1):**

لمعالجة قيود DeepSeek-R1-Zero (مثل ضعف قابلية القراءة واختلاط اللغات)، استخدم DeepSeek-R1 خط أنابيب تدريب شامل متعدد المراحل:

* **الضبط الدقيق لبيانات البدء البارد:** قبل مرحلة التعلم المعزز الرئيسية، تم ضبط النموذج الأساسي بدقة على مجموعة بيانات صغيرة من أمثلة الاستدلال طويلة سلسلة الأفكار عالية الجودة المكتوبة بواسطة البشر (أو المُولَّدة والمُنقحة). ساعدت بيانات "البدء البارد" هذه في توجيه النموذج نحو إنتاج خطوات استدلالية أكثر قابلية للقراءة وتماسكًا.
* **التعلم المعزز الموجه للاستدلال (مرحلة التعلم المعزز الثانية):** ثم خضع النموذج لمرحلة ثانية من التعلم المعزز واسع النطاق (مشابه لـ DeepSeek-R1-Zero) ولكن مع **مكافأة إضافية لاتساق اللغة**. عاقبت هذه المكافأة النموذج على خلط اللغات داخل عملية استدلاله.
* **الضبط الدقيق بالإشراف (SFT):** بعد التعلم المعزز الموجه للاستدلال، تم ضبط النموذج بدقة أكثر على مجموعة بيانات متنوعة شملت كلًا من بيانات الاستدلال (المُركَّبة باستخدام أخذ العينات بالرفض من نموذج RL، محكوم عليها بواسطة DeepSeek-V3) وبيانات عامة غير استدلالية (معززة بسلسلة الأفكار). هدفت مرحلة SFT هذه إلى تحسين مدى مساعدة النموذج وأمانه مع الحفاظ على قدراته الاستدلالية القوية.
* **التعلم المعزز لجميع السيناريوهات (مرحلة التعلم المعزز الثالثة):** تم إجراء مرحلة تعلم معزز أخيرة باستخدام مطالبات من نطاق أوسع من السيناريوهات لصقل قدرات النموذج العامة ومحاذاة سلوكياته مع السلوكيات المرغوبة بشكل أكبر.

**الاختلافات الرئيسية عن RLHF التقليدي:**

* **تقليل الاعتماد على بيانات التفضيل البشري المكثفة:** بينما قد تكون بعض التقييمات البشرية قد شاركت في الحكم على جودة البيانات المُركَّبة، فإن التدريب الأساسي للتعلم المعزز في DeepSeek-R1 استفاد بشكل كبير من المكافآت القائمة على القواعد، خاصة في المراحل الأولية. يقلل هذا من تكلفة وتعقيد جمع كميات كبيرة من مقارنات التفضيل البشري المباشر.
* **التركيز على الاستدلال الناشئ:** هدف نهج التعلم المعزز الخالص إلى حث النموذج على *اكتشاف* استراتيجيات الاستدلال الفعالة بنفسه، بدلاً من التعلم فقط من الأمثلة التي يقدمها البشر للاستدلال.
* **النهج متعدد المراحل:** يتضمن خط أنابيب DeepSeek سلسلة مُحكمة من التدريب المسبق، والضبط الدقيق المستهدف، ومراحل متعددة من التعلم المعزز بإشارات مكافأة مختلفة لتحقيق كل من القدرات الاستدلالية القوية وقدرات اللغة العامة.

**كود لتوضيح التعلم المعزز (مفاهيمي ومبسط):**

من الصعب تقديم مثال كود مباشر وقابل للتشغيل يكرر بالكامل عملية تدريب التعلم المعزز لـ DeepSeek بسبب تعقيدها وحجمها. ومع ذلك، فإن مقتطف PyTorch المفاهيمي التالي يوضح الفكرة الأساسية لـ GRPO ومكافأة قائمة على القواعد:

```python
import torch
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

# افترض أن لديك نموذج لغة مدرب مسبقًا ورمزًا مميزًا
model_name = "gpt2"  # استبدلها بنموذج أساسي أكثر ملاءمة
policy_model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
optimizer = optim.AdamW(policy_model.parameters(), lr=5e-6)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_model.to(device)

def generate_responses(prompt, num_responses=4, max_length=128):
    input_tokens = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = policy_model.generate(
        input_tokens.input_ids,
        max_length=max_length,
        num_return_sequences=num_responses,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )
    responses = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return responses

def calculate_accuracy_reward(response):
    # مثال مبسط لمسألة رياضية: "What is 2 + 2?"
    if "2 + 2" in response and "4" in response:
        return 1.0
    else:
        return 0.0

def calculate_format_reward(response):
    if "" in response:
        return 0.5
    else:
        return 0.0

def calculate_combined_reward(response):
    accuracy_reward = calculate_accuracy_reward(response)
    format_reward = calculate_format_reward(response)
    return accuracy_reward + format_reward

def train_step(prompt, num_samples=4):
    optimizer.zero_grad()
    responses = generate_responses(prompt, num_samples=num_samples)
    rewards = torch.tensor([calculate_combined_reward(resp) for resp in responses]).float().to(device)

    # تحديث شبيه بـ GRPO مبسط: تشجيع الاستجابات ذات المكافأة الأعلى
    best_reward_index = torch.argmax(rewards)
    best_response = responses[best_reward_index]
    inputs = tokenizer(prompt + best_response, return_tensors="pt").to(device)
    outputs = policy_model(**inputs, labels=inputs.input_ids)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
    return loss.item(), best_response, rewards.tolist()

# حلقة التدريب (مبسطة جدًا)
num_episodes = 10
training_prompts = ["Solve: 2 + 2 = ?", "Explain the concept of gravity