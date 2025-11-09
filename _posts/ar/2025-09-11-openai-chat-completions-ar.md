---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: العمل مع نماذج الدردشة المكتملة من OpenAI
translated: true
type: note
---

لقد قمت بربط مقال Microsoft Learn **"العمل مع نماذج إكمال الدردشة"** (المنشور في **1 سبتمبر 2025**). إليك ملخص واضح وموجز لنقاطه الأساسية:

---

### أبرز النقاط

*   **نماذج موجهة للدردشة**
    تختلف نماذج الدردشة الأحدث عن نماذج GPT-3 السابقة. بدلاً من نمط "نص يدخل، نص يخرج"، تستخدم هذه النماذج تنسيق **محادثة تدخل، رسالة تخرج**. جوهريًا، يتم هيكلة المدخلات مثل محضر محادثة (مع أدوار مثل *النظام*، *المستخدم*، *المساعد*)، ويعيد النموذج رسالة واحدة لمتابعة المحادثة ([Microsoft Learn][1]).

*   **مصممة للحوار**
    هذه البنية مُحسَّنة للمحادثات متعددة الجولات ذهابًا وإيابًا. كما أنها تعمل بشكل جيد في سيناريوهات المطالبة الفردية، لكن تنسيق المحادثة يمكّن تفاعلات أكثر سلاسة ([Microsoft Learn][1]).

*   **لا تعاملها مثل النماذج الأقدم**
    نماذج الدردشة هذه أكثر ثراءً بالكلام وغالبًا ما تنتج إجابات أقل فائدة إذا تعاملت معها مثل GPT-3. يُوصى باستخدام واجهة نمط الدردشة الجديدة للحصول على أفضل النتائج ([Microsoft Learn][1]).

*   **مقتطف كود نموذجي**
    يتضمن المقال نموذج كود أساسي يستخدم بناء جملة مشابه لـ Python لاستدعاء واجهة برمجة تطبيقات (API) إكمال الدردشة من Azure:

  ```python
  from openai import OpenAI
  import os

  client = OpenAI(
      api_key=os.getenv("AZURE_OPENAI_API_KEY"),
      base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/"
  )

  response = client.chat.completions.create(
      model="gpt-4o",  # or deployment_name
      messages=[
          {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
          {"role": "user", "content": "Who were the founders of Microsoft?"}
      ]
  )

  print(response.model_dump_json(indent=2))
  print(response.choices[0].message.content)
  ```

    يوضح ذلك كيفية إرسال الرسائل بشكل صحيح (مع فصل الأدوار) واسترداد إجابة النموذج ([Microsoft Learn][1]).

---

### لماذا هذا مهم

1.  **تحسين سياق المحادثة** — تحافظ نماذج الدردشة على تدفق وسياق المحادثة عبر التفاعلات متعددة الجولات بشكل أفضل.
2.  **تحسين قابلية الاستخدام** — استخدام الأدوار (system, user, assistant) يسمح بتعليمات أكثر وضوحًا، أو تحديد شخصية النموذج، أو فرض قيود.
3.  **تجنب الأخطاء** — معاملة نماذج الدردشة مثل الجيل السابق يمكن أن يؤدي إلى جودة ردود منخفضة؛ استخدم واجهة برمجة تطبيقات الدردشة كما هو مقصود.

---

أعلمني إذا كنت تريد المساعدة في شرح نموذج الكود، أو تكييفه مع إعداداتك، أو استكشاف أدلة ذات صلة — يسعدني الغوص في التفاصيل!

وكما تفضلت، حافظت على هذا بتنسيق بسيط وسهل القراءة دون جداول.

[1]: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/chatgpt?utm_source=chatgpt.com "Work with chat completion models - Azure OpenAI in ..."