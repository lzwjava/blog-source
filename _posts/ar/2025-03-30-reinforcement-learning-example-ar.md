---
audio: false
generated: true
lang: ar
layout: post
title: مثال على التعلم المعزز
translated: true
type: note
---

فيما يلي بعض الأمثلة المفاهيمية البسيطة على التعلم المعزز (RL) تليها مثال أساسي على كود Python باستخدام سيناريو بسيط. يتضمن RL وكيلًا يتعلم لتعزيز المكافأة من خلال التفاعل مع البيئة، لذا فإن الأمثلة والكود ستعكس ذلك.

### أمثلة بسيطة على التعلم المعزز

1. **طفل يتعلم المشي**  
   - **الوكيل**: الطفل.  
   - **البيئة**: الأرضية أو الغرفة.  
   - **الإجراء**: اتخاذ خطوة، الزحف، أو البقاء ساكنًا.  
   - **المكافأة**: التحرك للأمام (+1)، السقوط (-1).  
   - **التعلم**: يتعلم الطفل من خلال التجربة والخطأ أن اتخاذ خطوات متوازنة يؤدي إلى التقدم.

2. **تدريب ذراع روبوت على التقاط الأشياء**  
   - **الوكيل**: الذراع الآلي.  
   - **البيئة**: طاولة عليها أشياء.  
   - **الإجراء**: التحرك لأعلى، لأسفل، لليسار، لليمين، أو الإمساك.  
   - **المكافأة**: التقاط جسم بنجاح (+10)، إسقاطه (-5).  
   - **التعلم**: يضبط الذراع حركاته لتعزيز عمليات الإمساك الناجحة.

3. **لعبة عالم الشبكة (Grid World)**  
   - **الوكيل**: شخصية في شبكة.  
   - **البيئة**: شبكة 3x3 بها هدف وعقبات.  
   - **الإجراء**: التحرك لأعلى، لأسفل، لليسار، أو لليمين.  
   - **المكافأة**: الوصول للهدف (+10)، الاصطدام بحاجز (-1).  
   - **التعلم**: تتعلم الشخصية أقصر مسار للوصول إلى الهدف.

---

### مثال بسيط على كود Python: التعلم Q في عالم شبكة بسيط

إليك تنفيذ أساسي لـ Q-Learning، وهي خوارزمية RL شائعة، في "عالم" أحادي البعد حيث يتحرك وكيل لليسار أو لليمين للوصول إلى هدف. يتعلم الوكيل عن طريق تحديث جدول Q بناءً على المكافآت.

```python
import numpy as np
import random

# إعداد البيئة: عالم أحادي البعد ب5 مواقع (0 إلى 4)، الهدف عند الموقع 4
state_space = 5  # المواقع: [0, 1, 2, 3, 4]
action_space = 2  # الإجراءات: 0 = تحرك لليسار, 1 = تحرك لليمين
goal = 4

# تهيئة جدول Q بالأصفار (الحالات × الإجراءات)
q_table = np.zeros((state_space, action_space))

# المعاملات الفائقة (Hyperparameters)
learning_rate = 0.1
discount_factor = 0.9
exploration_rate = 1.0
exploration_decay = 0.995
min_exploration_rate = 0.01
episodes = 1000

# دالة المكافأة
def get_reward(state):
    if state == goal:
        return 10  # مكافأة كبيرة للوصول إلى الهدف
    return -1  # عقوبة صغيرة لكل خطوة

# دالة الخطوة: تحريك الوكيل والحصول على حالة جديدة
def step(state, action):
    if action == 0:  # تحرك لليسار
        new_state = max(0, state - 1)
    else:  # تحرك لليمين
        new_state = min(state_space - 1, state + 1)
    reward = get_reward(new_state)
    done = (new_state == goal)
    return new_state, reward, done

# حلقة التدريب
for episode in range(episodes):
    state = 0  # البدء من الموقع 0
    done = False
    
    while not done:
        # الاستكشاف مقابل الاستغلال
        if random.uniform(0, 1) < exploration_rate:
            action = random.randint(0, action_space - 1)  # استكشف
        else:
            action = np.argmax(q_table[state])  # استغل
        
        # تنفيذ الإجراء وملاحظة النتيجة
        new_state, reward, done = step(state, action)
        
        # تحديث جدول Q باستخدام صيغة Q-learning
        old_value = q_table[state, action]
        next_max = np.max(q_table[new_state])
        new_value = (1 - learning_rate) * old_value + learning_rate * (reward + discount_factor * next_max)
        q_table[state, action] = new_value
        
        # الانتقال إلى الحالة الجديدة
        state = new_state
    
    # تقليل معدل الاستكشاف
    exploration_rate = max(min_exploration_rate, exploration_rate * exploration_decay)

# اختبار السياسة المكتسبة
state = 0
steps = 0
print("Testing the learned policy:")
while state != goal:
    action = np.argmax(q_table[state])
    state, reward, done = step(state, action)
    steps += 1
    print(f"Step {steps}: Moved to state {state}, Action: {'Left' if action == 0 else 'Right'}")
print(f"Reached goal in {steps} steps!")

# طباعة جدول Q
print("\nLearned Q-table:")
print(q_table)
```

---

### شرح الكود

1.  **البيئة**: خط أحادي البعد به 5 مواقع (0 إلى 4). الهدف عند الموقع 4.
2.  **الإجراءات**: يمكن للوكيل التحرك لليسار (0) أو لليمين (1).
3.  **المكافآت**: +10 للوصول إلى الهدف، -1 لكل خطوة (لتشجيع الكفاءة).
4.  **جدول Q**: جدول يخزن المكافآت المستقبلية المتوقعة لكل زوج حالة-إجراء.
5.  **التعلم Q**: يقوم الوكيل بتحديث جدول Q باستخدام الصيغة:  
    `Q(s, a) = (1 - α) * Q(s, a) + α * (reward + γ * max(Q(s', a')))`، حيث:
    - `α` = معدل التعلم
    - `γ` = عامل الخصم
    - `s` = الحالة الحالية, `a` = الإجراء, `s'` = الحالة التالية

6.  **الاستكشاف مقابل الاستغلال**: يختار الوكيل أحيانًا إجراءات عشوائية (استكشاف) وأحيانًا أخرى يستخدم جدول Q (استغلال)، ويتم التحكم في ذلك بواسطة `exploration_rate`.

---

### نموذج للإخراج

```
Testing the learned policy:
Step 1: Moved to state 1, Action: Right
Step 2: Moved to state 2, Action: Right
Step 3: Moved to state 3, Action: Right
Step 4: Moved to state 4, Action: Right
Reached goal in 4 steps!

Learned Q-table:
[[-2.5   2.3]
 [-1.8   4.5]
 [-1.2   6.8]
 [-0.5   9. ]
 [ 0.    0. ]]
```

يتعلم الوكيل التحرك دائمًا إلى اليمين من أي موقع بدء للوصول إلى الهدف بكفاءة. يظهر جدول Q قيماً أعلى لإجراءات "التحرك لليمين" كلما اقتربت من الهدف.

هذا مثال أساسي جدًا، لكنه يلتقط جوهر RL. بالنسبة لسيناريوهات أكثر تعقيدًا (مثل شبكات ثنائية الأبعاد أو ألعاب)، يمكنك توسيع فضاءات الحالة والإجراءات وفقًا لذلك!