---
audio: false
generated: true
lang: ar
layout: post
title: 'الجيمنازيوم: صالة الرياضة الحديثة للتعلم المعزز'
translated: true
type: note
---

تشير مكتبة Gym إلى مجموعة أدوات Python الشهيرة التي طورتها في الأصل OpenAI لتعلم التعزيز (RL)، وهو حقل فرعي من تعلم الآلة حيث تتعلم الوكلات اتخاذ القرارات من خلال التفاعل مع البيئات لتعظيم المكافآت. توفر واجهة برمجة تطبيقات (API) موحدة ومجموعة من البيئات المعيارية (مثل الألعاب، ومحاكاة الروبوتات، ومشاكل التحكم الكلاسيكية) لتطوير واختبار ومقارنة خوارزميات تعلم التعزيز. وهذا يسهل على الباحثين والمطورين إنشاء النماذج الأولية دون الحاجة إلى بناء البيئات من الصفر.

من الميزات الرئيسية:
- **البيئات**: مهام مُعدة مسبقاً مثل CartPole (موازنة عمود)، وألعاب Atari، أو محاكيات فيزياء MuJoCo.
- **بساطة الـ API**: يمكنك إنشاء بيئة باستخدام `gym.make("اسم_البيئة")`، ثم استخدام طرق مثل `()reset` للبدء، و `(action)step` للتفاعل والحصول على الملاحظات/المكافآت، و `()render` للتصور.
- **القدرة على التوسع**: يمكن للمستخدمين إنشاء بيئات مخصصة عن طريق إنشاء فئات فرعية من الفئات الأساسية في Gym.
- **التكامل**: تعمل بشكل جيد مع مكتبات مثل Stable Baselines، و RLlib، أو PyTorch/TensorFlow لتنفيذ وكلات تعلم التعزيز.

ومع ذلك، فإن OpenAI Gym الأصلي لم يعد يُصان بنشاط وتم إهماله منذ حوالي عام 2021. يُوصى باستخدام **Gymnasium**، وهو فرع مباشر واستمرار من قبل Farama Foundation. Gymnasium متوافق بالكامل (يمكنك استيراده كـ `import gymnasium as gym`)، ويضيف تحسينات مثل بيئات متجهية أفضل للتدريب المتوازي، وفحص أكثر صرامة للأنواع، وتحديثات مستمرة. يتم التثبيت عبر `pip install gymnasium`، مع إضافات مثل `pip install gymnasium[atari]` لبيئات محددة.

مثال على الاستخدام الأساسي في Python:
```python
import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

for _ in range(1000):
    action = env.action_space.sample()  # إجراء عشوائي (الوكيل سيتعلم إجراءات أفضل)
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()

env.close()
```

إذا كنت تبدأ في تعلم التعزيز، فإن Gymnasium هو الخيار الأمثل اليوم لمعظم المشاريع.

[OpenAI Gym على GitHub](https://github.com/openai/gym)  
[توثيق Gymnasium](https://gymnasium.farama.org/)  
[توثيق Gym (الإصدار القديم)](https://www.gymlibrary.dev/)